"""
neofetch 스타일 정보 카드 SVG 생성.
출력: 저장소 루트의 info-card.svg
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_PATH = ROOT / "info-card.svg"

# ── 카드 내용 ──────────────────────────────────────────
HEADER   = "song@github"
DIVIDER  = "─" * 28

ROWS = [
    ("Role",    "Data Engineer / Backend Developer"),
    ("Stack",   "Java · Python · Spring Boot · SQL · LLM"),
    ("Now",     "Startup funding stage · YtoYOU Lab Lead"),
    ("Degree",  "SeoulTech IE+ITM · Northumbria Univ ITM"),
    ("Mail",    "alpngmu99@gmail.com"),
    ("Link",    "linkedin.com/in/taeho-song-seoultech"),
]

# ── 색상 ───────────────────────────────────────────────
BG          = "#0d1117"
COLOR_HEAD  = "#58a6ff"   # 파랑 — 사용자명
COLOR_KEY   = "#39d353"   # 초록 — 키
COLOR_VAL   = "#e6edf3"   # 흰색 계열 — 값
COLOR_DIV   = "#30363d"   # 구분선

# ── 레이아웃 ───────────────────────────────────────────
FONT   = "Consolas, Menlo, monospace"
FS     = 13        # font-size
LH     = 22        # line-height
PAD_X  = 20
PAD_Y  = 30
WIDTH  = 480
# 높이는 내용에 맞게 자동 계산


def build_svg():
    lines = []   # (text_elements, y)

    y = PAD_Y

    # 헤더
    lines.append(
        f'<text x="{PAD_X}" y="{y}" '
        f'font-family="{FONT}" font-size="{FS}" '
        f'font-weight="bold" fill="{COLOR_HEAD}">{HEADER}</text>'
    )
    y += LH

    # 구분선
    lines.append(
        f'<text x="{PAD_X}" y="{y}" '
        f'font-family="{FONT}" font-size="{FS}" '
        f'fill="{COLOR_DIV}">{DIVIDER}</text>'
    )
    y += LH

    # 빈 줄
    y += int(LH * 0.4)

    # 키-값 행
    KEY_W = 56   # 키 컬럼 고정 폭(px) — 값 시작 위치 맞추기용
    for key, val in ROWS:
        # 키
        lines.append(
            f'<text x="{PAD_X}" y="{y}" '
            f'font-family="{FONT}" font-size="{FS}" '
            f'fill="{COLOR_KEY}">{key}</text>'
        )
        # 콜론
        lines.append(
            f'<text x="{PAD_X + KEY_W}" y="{y}" '
            f'font-family="{FONT}" font-size="{FS}" '
            f'fill="{COLOR_DIV}">:</text>'
        )
        # 값
        lines.append(
            f'<text x="{PAD_X + KEY_W + 14}" y="{y}" '
            f'font-family="{FONT}" font-size="{FS}" '
            f'fill="{COLOR_VAL}">{val}</text>'
        )
        y += LH

    height = y + PAD_Y // 2

    svg_parts = [
        f'<svg width="{WIDTH}" height="{height}" '
        f'viewBox="0 0 {WIDTH} {height}" '
        f'xmlns="http://www.w3.org/2000/svg">',
        f'<rect width="{WIDTH}" height="{height}" fill="{BG}" rx="6"/>',
    ]
    svg_parts.extend(lines)
    svg_parts.append("</svg>")

    return "\n".join(svg_parts)


def main():
    svg = build_svg()
    OUTPUT_PATH.write_text(svg, encoding="utf-8")
    print(f"저장 완료: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()