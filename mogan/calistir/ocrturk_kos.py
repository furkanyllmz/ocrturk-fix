"""OCRTurk sayfalarini MLX ile bir VLM'e okutur: <cikti>/data_N/data_N.md (ham cikti) + kayit.jsonl (sure, token)."""
import argparse
import glob
import json
import os
import re
import time

from mlx_vlm import generate, load
from mlx_vlm.prompt_utils import apply_chat_template

ISTEM = ("Convert this document page to Markdown. Transcribe all text exactly as written, preserving Turkish characters. "
         "Write tables as HTML <table>, and math as LaTeX ($...$ inline, $$...$$ display). "
         "Skip page headers, footers and page numbers. Output only the page content.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="mlx-community/Qwen3.5-2B-bf16")
    ap.add_argument("--png", required=True)
    ap.add_argument("--cikti", required=True)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--max-tokens", type=int, default=6000)
    a = ap.parse_args()

    model, processor = load(a.model)
    istem = apply_chat_template(processor, model.config, ISTEM, num_images=1)
    sayfalar = sorted(glob.glob(os.path.join(a.png, "data_*.png")), key=lambda p: int(re.findall(r"\d+", os.path.basename(p))[0]))
    if a.limit:
        sayfalar = sayfalar[:a.limit]
    os.makedirs(a.cikti, exist_ok=True)
    kayit = open(os.path.join(a.cikti, "kayit.jsonl"), "a")
    t_top = time.time()
    for i, p in enumerate(sayfalar, 1):
        ad = os.path.splitext(os.path.basename(p))[0]
        hedef = os.path.join(a.cikti, ad, ad + ".md")
        if os.path.exists(hedef):
            continue
        t0 = time.time()
        r = generate(model, processor, istem, image=[p], max_tokens=a.max_tokens, temperature=0.0, verbose=False)
        metin = r.text if hasattr(r, "text") else str(r)
        os.makedirs(os.path.dirname(hedef), exist_ok=True)
        open(hedef, "w").write(metin)
        sure = time.time() - t0
        kayit.write(json.dumps({"sayfa": ad, "sure": round(sure, 1), "girdi": getattr(r, "prompt_tokens", None),
                                "cikti": getattr(r, "generation_tokens", None),
                                "tok_s": getattr(r, "generation_tps", None)}) + "\n")
        kayit.flush()
        print(f"{i}/{len(sayfalar)} {ad}: {sure:.1f} sn, {getattr(r, 'generation_tokens', '?')} token | toplam {(time.time() - t_top) / 60:.1f} dk", flush=True)


if __name__ == "__main__":
    main()
