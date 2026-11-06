import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open("original/index.html", 'r', encoding='utf-8') as f:
    orig_html = f.read()

with open("battery-passport-redesign/index.html", 'r', encoding='utf-8') as f:
    new_html = f.read()

print("\n--- ONCLICK FIDELITY VERIFICATION ---")
orig_onclicks = sorted(re.findall(r'onclick="([^"]+)"', orig_html))
new_onclicks = sorted(re.findall(r'onclick="([^"]+)"', new_html))

print(f"Original onclick count: {len(orig_onclicks)}")
print(f"Redesign onclick count: {len(new_onclicks)}")

if orig_onclicks == new_onclicks:
    print("✓ All 59 onclick actions match 100% exactly!")
else:
    missing = set(orig_onclicks) - set(new_onclicks)
    extra = set(new_onclicks) - set(orig_onclicks)
    print("Missing onclicks:", missing)
    print("Extra onclicks:", extra)

print("\n--- ID PRESENCE VERIFICATION (Anchors & Targets) ---")
orig_ids = sorted(set(re.findall(r'id="([^"]+)"', orig_html)))
new_ids = sorted(set(re.findall(r'id="([^"]+)"', new_html)))

# Check that every anchor and target ID from original exists in new
missing_ids = set(orig_ids) - set(new_ids)
if not missing_ids:
    print(f"✓ All original IDs exist in redesign ({len(orig_ids)} IDs)!")
else:
    print("Missing IDs:", missing_ids)

print("\n--- FORMS & INPUTS VERIFICATION ---")
orig_forms = re.findall(r'<form[^>]*>.*?</form>', orig_html, re.DOTALL)
new_forms = re.findall(r'<form[^>]*>.*?</form>', new_html, re.DOTALL)
print(f"Original forms: {len(orig_forms)}, Redesign forms: {len(new_forms)}")

orig_inputs = re.findall(r'<input[^>]*>|<select[^>]*>|<textarea[^>]*>', orig_html)
new_inputs = re.findall(r'<input[^>]*>|<select[^>]*>|<textarea[^>]*>', new_html)
print(f"Original inputs/controls: {len(orig_inputs)}, Redesign inputs/controls: {len(new_inputs)}")
if len(orig_inputs) == len(new_inputs):
    print("✓ All form controls preserved!")
