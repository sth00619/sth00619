"""
data/contributions.json 을 읽어서
53주 x 7일 격자 형태의 애니메이션 SVG 히트맵을 생성.
출력: 저장소 루트의 contrib-heatmap.svg
"""
import json
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "contributions.json"
OUTPUT_PATH = ROOT / "contrib-heatmap.svg"

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]

CELL = 11
GAP  = 3
LEFT_PAD   = 30
TOP_PAD    = 24
BOTTOM_PAD = 32


def load_data():
    raw = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    return raw["days"], raw["stats"]


def group_by_week(days):
    """
    날짜 리스트를 dict로 변환한 뒤,
    첫 날짜 이전 일요일부터 53주치 그리드를 만든다.
    각 주(week)는 7개의 dict (date, level) 리스트.
    """
    by_date = {d["date"]: d["level"] for d in days}

    first = datetime.strptime(days[0]["date"], "%Y-%m-%d")
    last  = datetime.strptime(days[-1]["date"], "%Y-%m-%d")

    # 첫날이 속한 주의 일요일로 이동 (일=6 in Python weekday)
    start = first - timedelta(days=(first.weekday() + 1) % 7)

    weeks = []
    cur = start
    while cur <= last:
        week = []
        for i in range(7):
            d = cur + timedelta(days=i)
            ds = d.strftime("%Y-%m-%d")
            week.append({"date": ds, "level": by_date.get(ds, 0)})
        weeks.append(week)
        cur += timedelta(weeks=1)

    return weeks


def month_labels(weeks):
    labels = []
    last_month = None
    for wi, week in enumerate(weeks):
        m = datetime.strptime(week[0]["date"], "%Y-%m-%d").month
        if m != last_month:
            labels.append((wi, datetime.strptime(week[0]["date"], "%Y-%m-%d").strftime("%b")))
            last_month = m
    return labels


def build_svg(weeks, stats):
    num_weeks = len(weeks)
    width  = LEFT_PAD + num_weeks * (CELL + GAP) + 10
    height = TOP_PAD + 7 * (CELL + GAP) + BOTTOM_PAD

    parts = []
    # width/height 를 명시해야 브라우저가 올바른 비율로 렌더링함
    parts.append(
        f'<svg width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" '
        f'xmlns="http://www.w3.org/2000/svg" '
        f'font-family="Consolas, Menlo, monospace">'
    )
    parts.append(f'<rect width="{width}" height="{height}" fill="#0d1117"/>')

    parts.append("<style>")
    parts.append("""
.cell {
  opacity: 0;
  animation: reveal 0.35s ease-out forwards;
}
@keyframes reveal {
  from { opacity:0; transform:translateY(-5px); }
  to   { opacity:1; transform:translateY(0);   }
}
.mlabel { fill:#8b949e; font-size:10px; }
.slabel { fill:#8b949e; font-size:10px; }
""")
    parts.append("</style>")

    # 월 라벨
    for wi, label in month_labels(weeks):
        x = LEFT_PAD + wi * (CELL + GAP)
        parts.append(f'<text x="{x}" y="{TOP_PAD - 6}" class="mlabel">{label}</text>')

    # 칸 그리기 — week 내 인덱스(0=일 ~ 6=토)
    for wi, week in enumerate(weeks):
        for di, day in enumerate(week):   # di: 0=일요일, 6=토요일
            level = min(day["level"], len(PALETTE) - 1)
            color = PALETTE[level]
            x = LEFT_PAD + wi * (CELL + GAP)
            y = TOP_PAD  + di * (CELL + GAP)
            delay = (wi + di) * 0.005
            parts.append(
                f'<rect class="cell" x="{x}" y="{y}" '
                f'width="{CELL}" height="{CELL}" rx="2" fill="{color}" '
                f'style="animation-delay:{delay:.3f}s">'
                f'<title>{day["date"]}</title></rect>'
            )

    # 하단 통계
    stat = (
        f"{stats['total_contribution_days']} contribution days  ·  "
        f"current streak {stats['current_streak']}  ·  "
        f"longest streak {stats['longest_streak']}"
    )
    parts.append(
        f'<text x="{LEFT_PAD}" y="{height - 10}" class="slabel">{stat}</text>'
    )
    parts.append("</svg>")
    return "\n".join(parts)


def main():
    days, stats = load_data()
    weeks = group_by_week(days)
    svg = build_svg(weeks, stats)
    OUTPUT_PATH.write_text(svg, encoding="utf-8")
    print(f"저장 완료: {OUTPUT_PATH}")
    print(f"주 수: {len(weeks)}")


if __name__ == "__main__":
    main()