"""Extract the SOW .docx to text for reading."""
import docx2txt
from pathlib import Path

src = "/home/cmoore/programming/ai_opportunities/lam_research/ip_protection/source/BAYON-MAS-0013142 Sarthak Gupta Mar26.docx"
out = "/home/cmoore/programming/ai_opportunities/lam_research/ip_protection/source/BAYON-MAS-0013142_Sarthak_Gupta_Mar26_extracted.txt"

text = docx2txt.process(src)
Path(out).write_text(text, encoding="utf-8")
print(f"Extracted {len(text)} chars to {out}")
print(f"Line count: {len(text.splitlines())}")
