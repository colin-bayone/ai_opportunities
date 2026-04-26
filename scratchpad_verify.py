import re

def count_non_whitespace(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    stripped = re.sub(r'\s+', '', text)
    return len(stripped), len(text)

md_path = '/home/cmoore/programming/ai_opportunities/claude/2026-04-14_pdf_extraction_test/Rivian RFP_DWS Managed Services Support2_PDF_extraction_2026-04-14_183814/Rivian RFP_DWS Managed Services Support2.md'
manual_path = '/home/cmoore/programming/ai_opportunities/claude/2026-04-14_pdf_extraction_test/test.txt'

md_chars, md_total = count_non_whitespace(md_path)
man_chars, man_total = count_non_whitespace(manual_path)

# Subtract markdown formatting overhead (headers, blockquotes, --- dividers)
# from the extracted file for a fair comparison
with open(md_path, 'r', encoding='utf-8') as f:
    md_text = f.read()
# Remove ## Page N headers, --- dividers, and the document header block
md_stripped = re.sub(r'^#.*$', '', md_text, flags=re.MULTILINE)
md_stripped = re.sub(r'^>.*$', '', md_stripped, flags=re.MULTILINE)
md_stripped = re.sub(r'^---$', '', md_stripped, flags=re.MULTILINE)
md_content_chars = len(re.sub(r'\s+', '', md_stripped))

print(f"Markdown (raw):        {md_chars:,} non-ws chars")
print(f"Markdown (no headers): {md_content_chars:,} non-ws chars")
print(f"Manual copy-paste:     {man_chars:,} non-ws chars")
print(f"Diff (content only):   {abs(md_content_chars - man_chars):,} chars ({abs(md_content_chars - man_chars) / max(man_chars, 1) * 100:.2f}%)")
