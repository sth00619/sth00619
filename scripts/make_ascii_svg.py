"""
assets/source-prepped.png 를 읽어서
한 줄씩 타이핑되듯 나타나는 ASCII 아트 SVG 생성.
출력: 저장소 루트의 avi-ascii.svg  (AVIVASHISHTA29 방식과 동일한 파일명 유지)
"""
from pathlib import Path
import numpy as np
from PIL import Image

ROOT       = Path(__file__).resolve().parent.parent
INPUT_PATH = ROOT / "assets" / "source-prepped.png"
OUTPUT_PATH = ROOT / "avi-ascii.svg"

# ASCII 밀도 램프 — 밝을수록 앞(공백), 어두울수록 뒤(밀집)
RAMP = " .`'-+*cs#%@"

# 출력 해상도 (문자 격자 크기)
COLS = 80
ROWS = 42

# SVG 스타일
FS        = 7       # font-size (px)
LH        = 8       # line-height (px)
CHAR_W    = 4.3     # 모노스페이스 한 문자 폭 (px) — FS 7 기준
PAD       = 10
FG_COLOR  = "#c9d1d9"   # 글자색 (GitHub dark 기준 연회색)
BG_COLOR  = "#0d1117"


def img_to_ascii(path: Path, cols: int, rows: int) -> list[str]:
    img = Image.open(path).convert("L")          # 그레이스케일
    img = img.resize((cols, rows), Image.LANCZOS)
    pixels = np.array(img)

    lines = []
    for row in pixels:
        line = ""
        for px in row:
            idx = int(px / 255 * (len(RAMP) - 1))
            line += RAMP[idx]
        lines.append(line)
    return lines


def build_svg(lines: list[str]) -> str:
    cols   = max(len(l) for l in lines)
    width  = int(PAD * 2 + cols * CHAR_W)
    height = PAD * 2 + len(lines) * LH

    parts = []
    parts.append(
        f'<svg width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" '
        f'xmlns="http://www.w3.org/2000/svg" '
        f'font-family="Consolas, Menlo, monospace" '
        f'font-size="{FS}">'
    )
    parts.append(f'<rect width="{width}" height="{height}" fill="{BG_COLOR}"/>')

    # CSS — 각 행이 위에서 아래로 순서대로 타이핑되듯 나타남
    parts.append("<style>")
    parts.append("""
.row {
  opacity: 0;
  animation: type-in 0.15s ease-out forwards;
}
@keyframes type-in {
  from { opacity: 0; transform: translateX(-4px); }
  to   { opacity: 1; transform: translateX(0); }
}
""")
    parts.append("</style>")

    for i, line in enumerate(lines):
        y     = PAD + (i + 1) * LH
        delay = i * 0.04          # 행마다 40ms 딜레이
        # XML 특수문자 이스케이프
        safe = (line
                .replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;"))
        parts.append(
            f'<text class="row" x="{PAD}" y="{y}" '
            f'fill="{FG_COLOR}" '
            f'xml:space="preserve" '
            f'style="animation-delay:{delay:.2f}s">{safe}</text>'
        )

    parts.append("</svg>")
    return "\n".join(parts)


def main():
    print("ASCII 변환 중...")
    lines = img_to_ascii(INPUT_PATH, COLS, ROWS)
    svg   = build_svg(lines)
    OUTPUT_PATH.write_text(svg, encoding="utf-8")
    print(f"저장 완료: {OUTPUT_PATH}")
    print(f"격자: {COLS}×{ROWS}, SVG 행 수: {len(lines)}")


if __name__ == "__main__":
    main()