import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open("original/index.html", 'r', encoding='utf-8') as f:
    orig = f.read()

medias = re.findall(r'@media[^{]+\{(?:[^{}]*\{[^{}]*\})*[^{}]*\}', orig)
print(f"Found {len(medias)} media queries in original:")
for m in medias:
    print(m)
    print("="*40)
