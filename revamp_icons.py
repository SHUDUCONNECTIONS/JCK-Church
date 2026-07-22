import os

BG = "#1e3a5f"   # deep navy circle background
W  = "white"     # icon shapes

def icon(shapes):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256">'
        f'<circle cx="128" cy="128" r="128" fill="{BG}"/>'
        f'{shapes}'
        f'</svg>'
    )

icons = {

"cross": icon(
    f'<rect x="104" y="36" width="48" height="184" rx="12" fill="{W}"/>'
    f'<rect x="36" y="104" width="184" height="48" rx="12" fill="{W}"/>'
),

"faith": icon(
    # Left raised hand
    f'<path d="M40 220 L40 152 L68 152 L68 80 Q68 56 52 56 Q36 56 36 80 L36 152 L36 220Z" fill="{W}"/>'
    f'<path d="M40 220 L96 220 L96 152 L68 152 Z" fill="{W}"/>'
    # Right raised hand
    f'<path d="M216 220 L216 152 L188 152 L188 80 Q188 56 204 56 Q220 56 220 80 L220 152 L220 220Z" fill="{W}"/>'
    f'<path d="M216 220 L160 220 L160 152 L188 152 Z" fill="{W}"/>'
    # Cross between hands
    f'<rect x="114" y="28" width="28" height="180" rx="8" fill="{W}"/>'
    f'<rect x="78" y="92" width="100" height="28" rx="8" fill="{W}"/>'
),

"dove": icon(
    # Body
    f'<ellipse cx="148" cy="152" rx="60" ry="32" fill="{W}"/>'
    # Wing sweeping left and up
    f'<path d="M148 152 Q108 92 44 116 Q88 152 148 152Z" fill="{W}"/>'
    # Head
    f'<circle cx="92" cy="136" r="30" fill="{W}"/>'
    # Tail fork
    f'<path d="M204 152 L240 124 L240 180Z" fill="{W}"/>'
    # Eye (navy dot on white head)
    f'<circle cx="80" cy="126" r="8" fill="{BG}"/>'
    # Beak
    f'<polygon points="68,136 40,128 40,144" fill="{BG}"/>'
),

"choir": icon(
    # Three robed figures — left, centre (taller), right
    f'<circle cx="60"  cy="72"  r="28" fill="{W}"/>'
    f'<rect   x="36"  y="92"  width="48" height="132" rx="24" fill="{W}"/>'
    f'<circle cx="128" cy="56" r="32" fill="{W}"/>'
    f'<rect   x="102" y="80"  width="52" height="148" rx="26" fill="{W}"/>'
    f'<circle cx="196" cy="72" r="28" fill="{W}"/>'
    f'<rect   x="172" y="92"  width="48" height="132" rx="24" fill="{W}"/>'
    # Open mouths (singing)
    f'<ellipse cx="60"  cy="74"  rx="9" ry="7" fill="{BG}"/>'
    f'<ellipse cx="128" cy="58"  rx="10" ry="8" fill="{BG}"/>'
    f'<ellipse cx="196" cy="74"  rx="9" ry="7" fill="{BG}"/>'
    # Music waves
    f'<path d="M90 30 Q108 20 128 28" stroke="{W}" stroke-width="7" fill="none" stroke-linecap="round"/>'
    f'<path d="M110 16 Q128 6 146 14" stroke="{W}" stroke-width="5" fill="none" stroke-linecap="round"/>'
),

"shovel": icon(
    # Handle
    f'<rect x="114" y="24" width="28" height="120" rx="14" fill="{W}"/>'
    # Collar
    f'<rect x="98" y="132" width="60" height="24" rx="8" fill="{W}"/>'
    # Blade
    f'<path d="M76 152 L76 196 Q76 232 128 232 Q180 232 180 196 L180 152Z" fill="{W}"/>'
),

"evangelism": icon(
    # Adult (right, tall)
    f'<circle cx="172" cy="68" r="36" fill="{W}"/>'
    f'<path d="M136 228 Q136 128 172 128 Q208 128 208 228Z" fill="{W}"/>'
    # Child (left, short)
    f'<circle cx="80"  cy="108" r="26" fill="{W}"/>'
    f'<path d="M58 228 Q58 172 80 172 Q102 172 102 228Z" fill="{W}"/>'
    # Arm connecting them
    f'<path d="M102 180 Q120 164 136 162" stroke="{W}" stroke-width="14" fill="none" stroke-linecap="round"/>'
    # Heart above child
    f'<path d="M80 74 Q68 60 56 70 Q44 82 80 102 Q116 82 104 70 Q92 60 80 74Z" fill="{W}"/>'
),

"eye": icon(
    f'<path d="M20 128 Q68 44 128 44 Q188 44 236 128 Q188 212 128 212 Q68 212 20 128Z" fill="{W}"/>'
    f'<circle cx="128" cy="128" r="44" fill="{BG}"/>'
    f'<circle cx="128" cy="128" r="28" fill="{W}"/>'
    f'<circle cx="128" cy="128" r="12" fill="{BG}"/>'
),

"target": icon(
    f'<circle cx="128" cy="128" r="88" fill="{W}"/>'
    f'<circle cx="128" cy="128" r="64" fill="{BG}"/>'
    f'<circle cx="128" cy="128" r="44" fill="{W}"/>'
    f'<circle cx="128" cy="128" r="24" fill="{BG}"/>'
    f'<circle cx="128" cy="128" r="10" fill="{W}"/>'
),

"commandments": icon(
    # Left tablet
    f'<path d="M16 216 L16 100 Q16 48 56 48 Q96 48 96 100 L96 216Z" fill="{W}"/>'
    # Right tablet
    f'<path d="M160 216 L160 100 Q160 48 200 48 Q240 48 240 100 L240 216Z" fill="{W}"/>'
    # Lines on left
    f'<rect x="28" y="108" width="56" height="9" rx="4" fill="{BG}"/>'
    f'<rect x="28" y="128" width="56" height="9" rx="4" fill="{BG}"/>'
    f'<rect x="28" y="148" width="56" height="9" rx="4" fill="{BG}"/>'
    f'<rect x="28" y="168" width="40" height="9" rx="4" fill="{BG}"/>'
    # Lines on right
    f'<rect x="172" y="108" width="56" height="9" rx="4" fill="{BG}"/>'
    f'<rect x="172" y="128" width="56" height="9" rx="4" fill="{BG}"/>'
    f'<rect x="172" y="148" width="56" height="9" rx="4" fill="{BG}"/>'
    f'<rect x="172" y="168" width="40" height="9" rx="4" fill="{BG}"/>'
),

"church-building": icon(
    # Building body
    f'<rect x="28" y="112" width="200" height="132" rx="4" fill="{W}"/>'
    # Roof triangle
    f'<polygon points="128,24 232,116 24,116" fill="{W}"/>'
    # Steeple cross
    f'<rect x="120" y="12" width="16" height="68" rx="5" fill="{W}"/>'
    f'<rect x="100" y="40" width="56" height="16" rx="5" fill="{W}"/>'
    # Door arch
    f'<path d="M104 244 L104 180 Q104 160 128 160 Q152 160 152 180 L152 244Z" fill="{BG}"/>'
    # Two windows
    f'<ellipse cx="68"  cy="158" rx="18" ry="24" fill="{BG}"/>'
    f'<ellipse cx="188" cy="158" rx="18" ry="24" fill="{BG}"/>'
),

"ichthus": icon(
    # Fish body
    f'<path d="M44 128 Q44 68 128 68 Q204 68 232 128 Q204 188 128 188 Q44 188 44 128Z" fill="{W}"/>'
    # Tail V
    f'<path d="M232 128 L264 96 L264 160Z" fill="{W}"/>'
    # Eye
    f'<circle cx="176" cy="108" r="14" fill="{BG}"/>'
    f'<circle cx="176" cy="108" r="6"  fill="{W}"/>'
),

"shield-cross": icon(
    # Shield
    f'<path d="M128 20 L224 60 L224 152 Q224 210 128 244 Q32 210 32 152 L32 60Z" fill="{W}"/>'
    # Cross on shield (navy cutout)
    f'<rect x="112" y="72"  width="32" height="148" rx="8" fill="{BG}"/>'
    f'<rect x="68"  y="112" width="120" height="32" rx="8" fill="{BG}"/>'
    # Cross inner (white again to get cross-on-shield look)
    f'<rect x="116" y="76"  width="24" height="140" rx="6" fill="{W}"/>'
    f'<rect x="72"  y="116" width="112" height="24" rx="6" fill="{W}"/>'
),

"candle": icon(
    # Flame
    f'<path d="M128 28 Q152 68 148 104 Q144 132 128 140 Q112 132 108 104 Q104 68 128 28Z" fill="{W}"/>'
    # Inner flame (nav cutout for detail)
    f'<path d="M128 52 Q140 80 138 104 Q136 120 128 126 Q120 120 118 104 Q116 80 128 52Z" fill="{BG}"/>'
    # Candle body
    f'<rect x="92"  y="140" width="72" height="88"  rx="8" fill="{W}"/>'
    # Wick line
    f'<rect x="125" y="132" width="6"  height="14"  rx="3" fill="{BG}"/>'
    # Base plate
    f'<rect x="72"  y="224" width="112" height="18" rx="9" fill="{W}"/>'
),

"baptism": icon(
    # Water drop (large)
    f'<path d="M128 32 Q168 80 168 128 Q168 168 128 180 Q88 168 88 128 Q88 80 128 32Z" fill="{W}"/>'
    # Cross on the drop (navy)
    f'<rect x="120" y="72"  width="16" height="96" rx="5" fill="{BG}"/>'
    f'<rect x="96"  y="108" width="64" height="16" rx="5" fill="{BG}"/>'
    # Hand below
    f'<path d="M28 200 Q28 184 48 184 L208 184 Q228 184 228 200 Q228 228 128 228 Q28 228 28 200Z" fill="{W}"/>'
),

"saints": icon(
    # Centre person (larger, front)
    f'<circle cx="128" cy="64" r="34" fill="{W}"/>'
    f'<path d="M84 228 L84 152 Q84 128 128 128 Q172 128 172 152 L172 228Z" fill="{W}"/>'
    # Left person
    f'<circle cx="52"  cy="84"  r="26" fill="{W}"/>'
    f'<path d="M20 228 L20 172 Q20 152 52 152 Q72 152 84 164 L84 228Z" fill="{W}"/>'
    # Right person
    f'<circle cx="204" cy="84"  r="26" fill="{W}"/>'
    f'<path d="M236 228 L236 172 Q236 152 204 152 Q184 152 172 164 L172 228Z" fill="{W}"/>'
),

"baby": icon(
    # Head
    f'<circle cx="128" cy="84"  r="56" fill="{W}"/>'
    # Body
    f'<ellipse cx="128" cy="180" rx="52" ry="44" fill="{W}"/>'
    # Eyes (navy)
    f'<circle cx="108" cy="76" r="8" fill="{BG}"/>'
    f'<circle cx="148" cy="76" r="8" fill="{BG}"/>'
    # Smile
    f'<path d="M108 98 Q128 114 148 98" stroke="{BG}" stroke-width="7" fill="none" stroke-linecap="round"/>'
),

"map-pin": icon(
    # Pin shape
    f'<path d="M128 24 Q72 24 72 100 Q72 152 128 232 Q184 152 184 100 Q184 24 128 24Z" fill="{W}"/>'
    # Inner circle (navy)
    f'<circle cx="128" cy="100" r="28" fill="{BG}"/>'
    f'<circle cx="128" cy="100" r="12" fill="{W}"/>'
),

"envelope": icon(
    # Envelope body
    f'<rect x="24" y="64" width="208" height="148" rx="12" fill="{W}"/>'
    # V flap
    f'<path d="M24 72 L128 156 L232 72" stroke="{BG}" stroke-width="16" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
),

"calendar": icon(
    # Body
    f'<rect x="24" y="56" width="208" height="180" rx="12" fill="{W}"/>'
    # Header band (navy)
    f'<rect x="24" y="56" width="208" height="60" rx="12" fill="{BG}"/>'
    f'<rect x="24" y="96" width="208" height="20" fill="{BG}"/>'
    # Tab pegs
    f'<rect x="76"  y="32" width="24" height="48" rx="12" fill="{W}"/>'
    f'<rect x="156" y="32" width="24" height="48" rx="12" fill="{W}"/>'
    # Date dots
    f'<circle cx="72"  cy="176" r="12" fill="{BG}"/>'
    f'<circle cx="128" cy="176" r="12" fill="{BG}"/>'
    f'<circle cx="184" cy="176" r="12" fill="{BG}"/>'
    f'<circle cx="72"  cy="216" r="12" fill="{BG}"/>'
    f'<circle cx="128" cy="216" r="12" fill="{BG}"/>'
),

"music-note": icon(
    # Note head 1
    f'<ellipse cx="76" cy="196" rx="44" ry="32" fill="{W}"/>'
    # Stem 1
    f'<rect x="116" y="44" width="16" height="160" rx="8" fill="{W}"/>'
    # Note head 2
    f'<ellipse cx="180" cy="172" rx="36" ry="26" fill="{W}"/>'
    # Stem 2
    f'<rect x="212" y="44" width="16" height="136" rx="8" fill="{W}"/>'
    # Beam connecting stems
    f'<rect x="116" y="44" width="112" height="16" rx="8" fill="{W}"/>'
),

"user": icon(
    f'<circle cx="128" cy="88" r="52" fill="{W}"/>'
    f'<path d="M20 228 Q20 156 128 156 Q236 156 236 228Z" fill="{W}"/>'
),

"phone": icon(
    f'<path d="M68 32 Q44 32 36 64 Q28 88 48 112 Q72 140 100 160 Q128 180 152 196 Q176 212 196 220 Q216 228 232 216 Q248 204 240 180 L216 152 Q200 136 184 148 L172 160 Q140 144 124 104 L136 92 Q152 76 136 52Z" fill="{W}"/>'
),

"id-badge": icon(
    f'<rect x="44" y="44" width="168" height="208" rx="14" fill="{W}"/>'
    # Clip at top
    f'<rect x="88" y="28" width="80" height="36" rx="10" fill="{W}"/>'
    f'<rect x="96" y="32" width="64" height="28" rx="7" fill="{BG}"/>'
    # Head silhouette
    f'<circle cx="128" cy="120" r="32" fill="{BG}"/>'
    f'<path d="M80 180 Q80 152 128 152 Q176 152 176 180 L176 196 L80 196Z" fill="{BG}"/>'
    # Name line
    f'<rect x="80" y="208" width="96" height="10" rx="5" fill="{BG}"/>'
),

"users": icon(
    # Back person (left)
    f'<circle cx="84"  cy="92"  r="36" fill="{W}"/>'
    f'<path d="M20 228 Q20 164 84 164 Q136 164 156 188 L156 228Z" fill="{W}"/>'
    # Front person (right)
    f'<circle cx="172" cy="80"  r="40" fill="{W}"/>'
    f'<path d="M100 228 Q100 156 172 156 Q244 156 244 228Z" fill="{W}"/>'
),

"plant": icon(
    # Stem
    f'<rect x="122" y="116" width="12" height="116" rx="6" fill="{W}"/>'
    # Left leaf
    f'<path d="M128 228 Q128 148 64 112 Q52 156 92 196 Q108 216 128 228Z" fill="{W}"/>'
    # Right leaf
    f'<path d="M128 228 Q128 148 192 112 Q204 156 164 196 Q148 216 128 228Z" fill="{W}"/>'
    # Top leaf
    f'<path d="M128 120 Q88 76 96 28 Q140 48 148 96 Q148 112 128 120Z" fill="{W}"/>'
),

"heart": icon(
    f'<path d="M128 220 Q20 156 20 92 Q20 44 72 40 Q104 36 128 72 Q152 36 184 40 Q236 44 236 92 Q236 156 128 220Z" fill="{W}"/>'
),

"gift": icon(
    # Box base
    f'<rect x="24" y="116" width="208" height="120" rx="10" fill="{W}"/>'
    # Lid
    f'<rect x="16" y="72"  width="224" height="52"  rx="10" fill="{W}"/>'
    # Vertical ribbon
    f'<rect x="114" y="72"  width="28" height="164" fill="{BG}"/>'
    # Horizontal ribbon
    f'<rect x="16"  y="112" width="224" height="28"  fill="{BG}"/>'
    # Bow left loop
    f'<ellipse cx="92" cy="76" rx="28" ry="18" fill="{W}" transform="rotate(-25 92 76)"/>'
    f'<ellipse cx="92" cy="76" rx="18" ry="10" fill="{BG}" transform="rotate(-25 92 76)"/>'
    # Bow right loop
    f'<ellipse cx="164" cy="76" rx="28" ry="18" fill="{W}" transform="rotate(25 164 76)"/>'
    f'<ellipse cx="164" cy="76" rx="18" ry="10" fill="{BG}" transform="rotate(25 164 76)"/>'
    # Bow centre knot
    f'<circle cx="128" cy="72" r="12" fill="{W}"/>'
),

"bowl": icon(
    # Bowl shape
    f'<path d="M20 120 Q20 216 128 216 Q236 216 236 120Z" fill="{W}"/>'
    # Rim
    f'<rect x="12" y="108" width="232" height="24" rx="12" fill="{W}"/>'
    # Steam lines
    f'<path d="M80 84 Q90 60 80 40"  stroke="{W}" stroke-width="10" fill="none" stroke-linecap="round"/>'
    f'<path d="M128 80 Q138 56 128 36" stroke="{W}" stroke-width="10" fill="none" stroke-linecap="round"/>'
    f'<path d="M176 84 Q186 60 176 40" stroke="{W}" stroke-width="10" fill="none" stroke-linecap="round"/>'
),

"rosette": icon(
    # Star/medal ring outer
    f'<polygon points="128,20 150,76 210,64 188,120 244,144 196,178 216,236 160,214 128,264 96,214 40,236 60,178 12,144 68,120 46,64 106,76" fill="{W}"/>'
    # Inner circles
    f'<circle cx="128" cy="144" r="48" fill="{BG}"/>'
    f'<circle cx="128" cy="144" r="32" fill="{W}"/>'
    f'<circle cx="128" cy="144" r="16" fill="{BG}"/>'
),

"trophy": icon(
    f'<path d="M64 32 L64 144 Q64 196 128 208 Q192 196 192 144 L192 32Z" fill="{W}"/>'
    # Left handle
    f'<path d="M64 52 Q28 52 28 88 Q28 120 64 130" stroke="{W}" stroke-width="20" fill="none" stroke-linecap="round"/>'
    # Right handle
    f'<path d="M192 52 Q228 52 228 88 Q228 120 192 130" stroke="{W}" stroke-width="20" fill="none" stroke-linecap="round"/>'
    # Base stem
    f'<rect x="104" y="208" width="48" height="16" rx="8" fill="{W}"/>'
    # Base plate
    f'<rect x="72"  y="220" width="112" height="20" rx="10" fill="{W}"/>'
),

"seedling": icon(
    # Stem
    f'<rect x="122" y="136" width="12" height="96"  rx="6" fill="{W}"/>'
    # Left leaf
    f'<path d="M128 136 Q128 80 72 56 Q52 92 76 136Z" fill="{W}"/>'
    # Right leaf
    f'<path d="M128 156 Q128 100 184 76 Q204 112 180 156Z" fill="{W}"/>'
),

"package": icon(
    f'<path d="M128 20 L236 76 L236 180 L128 236 L20 180 L20 76Z" fill="{W}"/>'
    # Top face darker
    f'<path d="M128 20 L236 76 L128 132 L20 76Z" fill="{BG}" opacity="0.35"/>'
    # Centre line
    f'<line x1="128" y1="132" x2="128" y2="236" stroke="{BG}" stroke-width="8" opacity="0.35"/>'
    # Band
    f'<path d="M72 50 L184 104" stroke="{BG}" stroke-width="8" opacity="0.35"/>'
),

"cash": icon(
    f'<rect x="16" y="72" width="224" height="144" rx="16" fill="{W}"/>'
    # Centre oval
    f'<circle cx="128" cy="144" r="40" fill="{BG}"/>'
    f'<circle cx="128" cy="144" r="26" fill="{W}"/>'
    # R symbol
    f'<text x="128" y="154" text-anchor="middle" font-size="28" font-weight="bold" fill="{BG}" font-family="serif">R</text>'
    # Corner ovals
    f'<circle cx="44"  cy="100" r="18" fill="{BG}"/>'
    f'<circle cx="212" cy="188" r="18" fill="{BG}"/>'
),

"shovel": icon(
    # Long handle
    f'<rect x="116" y="20" width="24" height="120" rx="12" fill="{W}"/>'
    # Socket collar
    f'<rect x="100" y="128" width="56" height="22" rx="8" fill="{W}"/>'
    # Spade blade
    f'<path d="M78 148 L78 196 Q78 236 128 236 Q178 236 178 196 L178 148Z" fill="{W}"/>'
),

"bible": icon(
    # Book body
    f'<rect x="28" y="20" width="200" height="216" rx="14" fill="{W}"/>'
    # Spine
    f'<rect x="28" y="20" width="32" height="216" rx="14" fill="{BG}" opacity="0.4"/>'
    # Cross on cover
    f'<rect x="112" y="72"  width="32" height="120" rx="8" fill="{BG}"/>'
    f'<rect x="76"  y="108" width="104" height="32" rx="8" fill="{BG}"/>'
),

"bulb": icon(
    # Bulb globe
    f'<circle cx="128" cy="96" r="72" fill="{W}"/>'
    # Base ridges
    f'<rect x="92"  y="156" width="72" height="16" rx="8" fill="{W}"/>'
    f'<rect x="96"  y="178" width="64" height="16" rx="8" fill="{W}"/>'
    f'<rect x="100" y="200" width="56" height="16" rx="8" fill="{W}"/>'
    # Light rays (navy on white bulb)
    f'<rect x="124" y="40" width="8"  height="20" rx="4" fill="{BG}"/>'
    f'<path d="M80 60 L68 48"   stroke="{BG}" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M176 60 L188 48" stroke="{BG}" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M56 96 L40 96"   stroke="{BG}" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M200 96 L216 96" stroke="{BG}" stroke-width="7" stroke-linecap="round"/>'
),

"car": icon(
    # Body
    f'<rect x="16" y="128" width="224" height="80" rx="12" fill="{W}"/>'
    # Cabin
    f'<path d="M48 128 L72 72 L184 72 L208 128Z" fill="{W}"/>'
    # Wheels
    f'<circle cx="68"  cy="208" r="32" fill="{BG}"/>'
    f'<circle cx="68"  cy="208" r="16" fill="{W}"/>'
    f'<circle cx="188" cy="208" r="32" fill="{BG}"/>'
    f'<circle cx="188" cy="208" r="16" fill="{W}"/>'
    # Window
    f'<path d="M80 128 L98 84 L158 84 L176 128Z" fill="{BG}"/>'
),

"shirt": icon(
    f'<path d="M44 36 L16 96 L72 116 L72 228 L184 228 L184 116 L240 96 L216 36 L176 64 Q160 84 128 84 Q96 84 80 64Z" fill="{W}"/>'
),

"football": icon(
    f'<circle cx="128" cy="128" r="100" fill="{W}"/>'
    # Pentagon centre
    f'<polygon points="128,76 154,96 144,124 112,124 102,96" fill="{BG}"/>'
    # Side pentagons
    f'<polygon points="64,86 90,86 98,112 76,128 54,112"   fill="{BG}"/>'
    f'<polygon points="192,86 202,112 180,128 158,112 166,86" fill="{BG}"/>'
    f'<polygon points="84,168 96,140 128,140 160,140 172,168 128,196" fill="{BG}"/>'
),

"graduation-cap": icon(
    # Board (diamond shape for mortarboard)
    f'<polygon points="128,32 240,84 128,136 16,84" fill="{W}"/>'
    # Cap top (navy square on white diamond)
    f'<rect x="96" y="52" width="64" height="64" rx="4" fill="{BG}" transform="rotate(45 128 84)"/>'
    # Gown/body below
    f'<path d="M72 108 L72 168 Q72 200 128 208 Q184 200 184 168 L184 108 L128 132Z" fill="{W}"/>'
    # Tassel
    f'<rect x="216" y="84" width="12" height="64" rx="6" fill="{W}"/>'
    f'<circle cx="222" cy="148" r="16" fill="{W}"/>'
),

"building": icon(
    # Triangle roof
    f'<polygon points="128,20 220,64 36,64" fill="{W}"/>'
    # Cross on top
    f'<rect x="121" y="12" width="14" height="52" rx="5" fill="{W}"/>'
    f'<rect x="105" y="28" width="46" height="14" rx="5" fill="{W}"/>'
    # Building block
    f'<rect x="32" y="60" width="192" height="184" rx="4" fill="{W}"/>'
    # Door
    f'<path d="M104 244 L104 188 Q104 168 128 168 Q152 168 152 188 L152 244Z" fill="{BG}"/>'
    # Windows (4)
    f'<rect x="52"  y="84"  width="40" height="36" rx="4" fill="{BG}"/>'
    f'<rect x="164" y="84"  width="40" height="36" rx="4" fill="{BG}"/>'
    f'<rect x="52"  y="140" width="40" height="36" rx="4" fill="{BG}"/>'
    f'<rect x="164" y="140" width="40" height="36" rx="4" fill="{BG}"/>'
),

"megaphone": icon(
    # Horn body
    f'<path d="M24 164 L24 100 L176 52 L212 52 Q232 52 232 88 Q232 124 212 124 L176 124Z" fill="{W}"/>'
    # Speaker box
    f'<rect x="24" y="100" width="60" height="64" rx="6" fill="{BG}"/>'
    f'<rect x="30" y="106" width="48" height="52" rx="4" fill="{W}"/>'
    # Handle
    f'<path d="M84 164 L84 224 Q84 236 68 236 Q52 236 52 224 L52 164Z" fill="{W}"/>'
    # Sound waves
    f'<path d="M228 72 Q248 72 248 88 Q248 104 228 108" stroke="{W}" stroke-width="10" fill="none" stroke-linecap="round"/>'
),

"book-open": icon(
    f'<path d="M24 56 L24 216 Q28 224 48 218 L128 196 L128 44Z" fill="{W}"/>'
    f'<path d="M232 56 L232 216 Q228 224 208 218 L128 196 L128 44Z" fill="{W}"/>'
    # Spine lines
    f'<path d="M128 44 L128 196" stroke="{BG}" stroke-width="8"/>'
    # Page lines (left)
    f'<path d="M60 100 L112 88"  stroke="{BG}" stroke-width="6" stroke-linecap="round"/>'
    f'<path d="M56 120 L112 108" stroke="{BG}" stroke-width="6" stroke-linecap="round"/>'
    f'<path d="M52 140 L112 128" stroke="{BG}" stroke-width="6" stroke-linecap="round"/>'
    # Page lines (right)
    f'<path d="M144 88 L196 100"  stroke="{BG}" stroke-width="6" stroke-linecap="round"/>'
    f'<path d="M144 108 L200 120" stroke="{BG}" stroke-width="6" stroke-linecap="round"/>'
    f'<path d="M144 128 L204 140" stroke="{BG}" stroke-width="6" stroke-linecap="round"/>'
),

"user-check": icon(
    f'<circle cx="96" cy="76" r="52" fill="{W}"/>'
    f'<path d="M20 228 L180 228 L180 188 Q156 152 96 152 Q20 152 20 228Z" fill="{W}"/>'
    # Checkmark
    f'<path d="M168 188 L192 216 L240 156" stroke="{W}" stroke-width="20" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
),

}

out_dir = r"c:\Users\tshik\Downloads\church\images\icons"
os.makedirs(out_dir, exist_ok=True)
for name, svg in icons.items():
    with open(os.path.join(out_dir, f"{name}.svg"), "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"  {name}.svg")
print(f"\n{len(icons)} icons written.")
