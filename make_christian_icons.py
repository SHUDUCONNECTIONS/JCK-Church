import os

D = "#1e3a5f"
L = "#4a9fd4"

icons = {

# Raised hands lifting a cross — Faith / Spiritual Growth
"faith": f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256">
  <path d="M36 232 Q32 162 52 142 L84 142 L84 68 Q84 46 67 46 Q50 46 50 68 L50 142 Q28 166 28 232 Z" fill="{L}"/>
  <path d="M220 232 Q224 162 204 142 L172 142 L172 68 Q172 46 189 46 Q206 46 206 68 L206 142 Q228 166 228 232 Z" fill="{L}"/>
  <rect x="108" y="20" width="40" height="220" rx="12" fill="{L}"/>
  <rect x="68" y="88" width="120" height="40" rx="12" fill="{L}"/>
  <path d="M44 228 Q40 166 58 148 L84 148 L84 72 Q84 54 68 54 Q56 54 56 72 L56 148 Q36 170 36 228 Z" fill="{D}"/>
  <path d="M212 228 Q216 166 198 148 L172 148 L172 72 Q172 54 188 54 Q200 54 200 72 L200 148 Q220 170 220 228 Z" fill="{D}"/>
  <rect x="114" y="24" width="28" height="212" rx="9" fill="{D}"/>
  <rect x="74" y="94" width="108" height="28" rx="9" fill="{D}"/>
</svg>''',

# Flying dove — Holy Spirit / Wisemens' Dept
"dove": f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256">
  <ellipse cx="140" cy="156" rx="64" ry="36" fill="{L}"/>
  <path d="M140 156 Q108 96 48 124 Q84 156 140 156 Z" fill="{L}"/>
  <path d="M140 156 Q164 112 212 128 Q188 156 140 156 Z" fill="{L}" opacity="0.7"/>
  <circle cx="84" cy="140" r="32" fill="{L}"/>
  <path d="M196 156 L232 128 L232 184 Z" fill="{L}"/>
  <ellipse cx="138" cy="154" rx="52" ry="27" fill="{D}"/>
  <path d="M138 154 Q110 100 58 126 Q90 154 138 154 Z" fill="{D}"/>
  <path d="M138 154 Q160 114 204 130 Q184 154 138 154 Z" fill="{D}"/>
  <circle cx="84" cy="138" r="24" fill="{D}"/>
  <path d="M192 154 L224 130 L224 178 Z" fill="{D}"/>
  <circle cx="74" cy="130" r="7" fill="white"/>
  <path d="M64 138 L40 130 L46 148 Z" fill="{D}"/>
  <path d="M100 70 Q120 50 128 20 Q148 44 148 72" stroke="{L}" stroke-width="8" fill="none" stroke-linecap="round"/>
</svg>''',

# Two stone tablets — Executive Committee / Commandments
"commandments": f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256">
  <path d="M12 220 L12 96 Q12 40 60 40 Q108 40 108 96 L108 220 Z" fill="{L}"/>
  <path d="M148 220 L148 96 Q148 40 196 40 Q244 40 244 96 L244 220 Z" fill="{L}"/>
  <path d="M20 216 L20 100 Q20 52 60 52 Q100 52 100 100 L100 216 Z" fill="{D}"/>
  <path d="M156 216 L156 100 Q156 52 196 52 Q236 52 236 100 L236 216 Z" fill="{D}"/>
  <rect x="32" y="104" width="56" height="9" rx="4" fill="{L}"/>
  <rect x="32" y="124" width="56" height="9" rx="4" fill="{L}"/>
  <rect x="32" y="144" width="56" height="9" rx="4" fill="{L}"/>
  <rect x="32" y="164" width="56" height="9" rx="4" fill="{L}"/>
  <rect x="32" y="184" width="40" height="9" rx="4" fill="{L}"/>
  <rect x="168" y="104" width="56" height="9" rx="4" fill="{L}"/>
  <rect x="168" y="124" width="56" height="9" rx="4" fill="{L}"/>
  <rect x="168" y="144" width="56" height="9" rx="4" fill="{L}"/>
  <rect x="168" y="164" width="56" height="9" rx="4" fill="{L}"/>
  <rect x="168" y="184" width="40" height="9" rx="4" fill="{L}"/>
</svg>''',

# Lit candle — Women / Pastoral Care / Light
"candle": f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256">
  <path d="M128 20 Q152 56 152 100 Q152 126 128 136 Q104 126 104 100 Q104 56 128 20Z" fill="{L}"/>
  <path d="M128 36 Q146 66 146 100 Q146 120 128 130 Q110 120 110 100 Q110 66 128 36Z" fill="{D}"/>
  <path d="M128 72 Q138 88 128 112 Q118 88 128 72Z" fill="{L}"/>
  <ellipse cx="128" cy="136" rx="40" ry="12" fill="{L}"/>
  <ellipse cx="128" cy="134" rx="32" ry="9" fill="{D}"/>
  <rect x="88" y="134" width="80" height="96" rx="10" fill="{L}"/>
  <rect x="94" y="140" width="68" height="86" rx="8" fill="{D}"/>
  <rect x="106" y="172" width="8" height="44" rx="4" fill="{L}"/>
  <rect x="142" y="172" width="8" height="44" rx="4" fill="{L}"/>
  <rect x="72" y="226" width="112" height="18" rx="9" fill="{L}"/>
  <rect x="78" y="230" width="100" height="12" rx="6" fill="{D}"/>
</svg>''',

# Shield with cross — Men / Protection
"shield-cross": f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256">
  <path d="M128 16 L232 58 L232 152 Q232 216 128 248 Q24 216 24 152 L24 58 Z" fill="{L}"/>
  <path d="M128 28 L222 66 L222 152 Q222 206 128 234 Q34 206 34 152 L34 66 Z" fill="{D}"/>
  <rect x="110" y="70" width="36" height="148" rx="10" fill="{L}"/>
  <rect x="70" y="108" width="116" height="36" rx="10" fill="{L}"/>
  <rect x="116" y="76" width="24" height="136" rx="7" fill="{D}"/>
  <rect x="76" y="114" width="104" height="24" rx="7" fill="{D}"/>
  <rect x="118" y="78" width="20" height="132" rx="5" fill="{L}"/>
  <rect x="78" y="116" width="100" height="20" rx="5" fill="{L}"/>
</svg>''',

# Christian fish (Ichthus) — Evangelism / spreading the faith
"ichthus": f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256">
  <path d="M48 128 Q48 64 128 64 Q200 64 232 128 Q200 192 128 192 Q48 192 48 128Z" fill="{L}"/>
  <path d="M232 128 L268 96 L268 160 Z" fill="{L}"/>
  <path d="M56 128 Q56 72 128 72 Q196 72 224 128 Q196 184 128 184 Q56 184 56 128Z" fill="{D}"/>
  <path d="M228 128 L260 100 L260 156 Z" fill="{D}"/>
  <circle cx="176" cy="108" r="16" fill="{L}"/>
  <circle cx="176" cy="108" r="9" fill="{D}"/>
  <circle cx="176" cy="108" r="3" fill="{L}"/>
  <rect x="108" y="116" width="32" height="8" rx="4" fill="{L}"/>
  <rect x="108" y="132" width="24" height="8" rx="4" fill="{L}"/>
</svg>''',

# Church building with cross steeple — Church / Pastors
"church-building": f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256">
  <rect x="24" y="108" width="208" height="148" rx="6" fill="{L}"/>
  <polygon points="128,16 236,112 20,112" fill="{L}"/>
  <rect x="32" y="116" width="192" height="132" rx="4" fill="{D}"/>
  <polygon points="128,28 224,112 32,112" fill="{D}"/>
  <rect x="118" y="8" width="20" height="80" rx="6" fill="{L}"/>
  <rect x="96" y="40" width="64" height="20" rx="6" fill="{L}"/>
  <rect x="120" y="12" width="16" height="72" rx="4" fill="{D}"/>
  <rect x="100" y="44" width="56" height="14" rx="4" fill="{D}"/>
  <path d="M100 256 L100 182 Q100 158 128 158 Q156 158 156 182 L156 256 Z" fill="{L}"/>
  <path d="M106 252 L106 184 Q106 164 128 164 Q150 164 150 184 L150 252 Z" fill="{D}"/>
  <rect x="52" y="136" width="44" height="48" rx="22" fill="{L}"/>
  <rect x="160" y="136" width="44" height="48" rx="22" fill="{L}"/>
  <rect x="58" y="140" width="32" height="40" rx="16" fill="{D}"/>
  <rect x="166" y="140" width="32" height="40" rx="16" fill="{D}"/>
</svg>''',

# Baptism — hand + water drop with cross
"baptism": f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256">
  <path d="M128 16 Q156 56 156 96 Q156 136 128 148 Q100 136 100 96 Q100 56 128 16Z" fill="{L}"/>
  <path d="M128 32 Q150 66 150 96 Q150 128 128 140 Q106 128 106 96 Q106 66 128 32Z" fill="{D}"/>
  <rect x="118" y="72" width="20" height="64" rx="6" fill="{L}"/>
  <rect x="96" y="94" width="64" height="20" rx="6" fill="{L}"/>
  <rect x="120" y="76" width="16" height="56" rx="4" fill="{D}"/>
  <rect x="100" y="98" width="56" height="14" rx="4" fill="{D}"/>
  <path d="M24 220 Q24 180 64 180 L192 180 Q224 180 228 220 Q200 240 128 240 Q56 240 24 220Z" fill="{L}"/>
  <path d="M32 218 Q36 186 64 188 L192 188 Q216 188 220 218 Q196 232 128 232 Q60 232 32 218Z" fill="{D}"/>
  <path d="M40 188 Q72 168 128 168 Q184 168 216 188" stroke="{L}" stroke-width="10" fill="none" stroke-linecap="round"/>
</svg>''',

# Saints / Community — three figures with cross halo
"saints": f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256">
  <circle cx="128" cy="56" r="36" fill="{L}"/>
  <circle cx="128" cy="52" r="28" fill="{D}"/>
  <path d="M80 228 L80 148 Q80 128 128 128 Q176 128 176 148 L176 228Z" fill="{L}"/>
  <path d="M88 224 L88 152 Q88 136 128 136 Q168 136 168 152 L168 224Z" fill="{D}"/>
  <circle cx="44" cy="76" r="26" fill="{L}"/>
  <circle cx="44" cy="72" r="20" fill="{D}"/>
  <path d="M12 228 L12 164 Q12 148 44 148 Q68 148 80 160 L80 228Z" fill="{L}"/>
  <path d="M18 224 L18 166 Q18 152 44 152 Q66 152 76 162 L76 224Z" fill="{D}"/>
  <circle cx="212" cy="76" r="26" fill="{L}"/>
  <circle cx="212" cy="72" r="20" fill="{D}"/>
  <path d="M244 228 L244 164 Q244 148 212 148 Q188 148 176 160 L176 228Z" fill="{L}"/>
  <path d="M238 224 L238 166 Q238 152 212 152 Q190 152 180 162 L180 224Z" fill="{D}"/>
</svg>''',

}

out_dir = r"c:\Users\tshik\Downloads\church\images\icons"
for name, svg in icons.items():
    path = os.path.join(out_dir, f"{name}.svg")
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Created {name}.svg")

print(f"\nTotal: {len(icons)} icons created.")
