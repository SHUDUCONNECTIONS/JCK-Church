import os, re

# Mapping: tabler icon name -> custom svg filename
MAPPING = {
    "cross": "cross",
    "hands-praying": "hands-praying",
    "users": "users",
    "friends": "users",
    "baby-carriage": "baby",
    "music": "music-note",
    "plant-2": "plant",
    "book-2": "book-open",
    "eye": "eye",
    "target": "target",
    "clipboard-list": "clipboard-text",
    "flame": "fire",
    "user-check": "user-check",
    "speakerphone": "megaphone",
    "star": "star",
    "shield": "shield",
    "map-pin": "map-pin",
    "mail": "envelope",
    "calendar": "calendar",
    "phone": "phone",
    "user": "user",
    "id-badge-2": "id-badge",
    "building": "building",
    "rosette": "rosette",
    "bible": "bible",
    "package": "package",
    "cash": "cash",
    "trophy": "trophy",
    "seeding": "seedling",
    "tool": "shovel",
    "home": "building",
    "shovel": "shovel",
    "gift": "gift",
    "heart-handshake": "heart",
    "heart": "heart",
    "car": "car",
    "bulb": "bulb",
    "hand-finger": "bulb",
    "bowl-spoon": "bowl",
    "soup": "bowl",
    "social": "megaphone",
    "shirt": "shirt",
    "ball-football": "football",
    "school": "graduation-cap",
}

# Icons to keep as Tabler (not replaced)
KEEP = {"menu-2", "x", "chevron-down", "arrow-right", "arrow-left", "refresh"}

def replace_icons(html, prefix):
    def replacer(m):
        ti_name = m.group(1)
        if ti_name in KEEP:
            return m.group(0)  # leave unchanged
        custom = MAPPING.get(ti_name)
        if not custom:
            print(f"  WARNING: no mapping for ti-{ti_name}")
            return m.group(0)
        return f'<img class="jck-icon" src="{prefix}images/icons/{custom}.svg" alt="" loading="lazy">'

    pattern = r'<i\s+class="ti\s+ti-([\w-]+)"[^>]*></i>'
    return re.sub(pattern, replacer, html)

church_dir = r"c:\Users\tshik\Downloads\church"

files = {
    # root pages
    "index.html": "",
    "about.html": "",
    "contact.html": "",
    "departments.html": "",
    "lifechangers.html": "",
    # lifechangers subdir -> go up one level
    "lifechangers/index.html": "../",
    "lifechangers/farming.html": "../",
    "lifechangers/gardens.html": "../",
    "lifechangers/elderly.html": "../",
    "lifechangers/food-parcels.html": "../",
    "lifechangers/soup-drive.html": "../",
    "lifechangers/dignity.html": "../",
    "lifechangers/prison.html": "../",
    "lifechangers/sport.html": "../",
}

for rel_path, prefix in files.items():
    full_path = os.path.join(church_dir, rel_path.replace("/", os.sep))
    with open(full_path, "r", encoding="utf-8") as f:
        original = f.read()
    updated = replace_icons(original, prefix)
    if updated != original:
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(updated)
        count = len(re.findall(r'jck-icon', updated))
        print(f"Updated {rel_path}: {count} icons replaced")
    else:
        print(f"No changes in {rel_path}")
