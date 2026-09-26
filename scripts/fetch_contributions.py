"""
GitHub 공개 기여도 캘린더를 토큰 없이 스크래핑해서
data/contributions.json 에 저장하는 스크립트.
"""
import json
import re
from pathlib import Path

import requests
from bs4 import BeautifulSoup

USERNAME = "sth00619"
URL = f"https://github.com/users/{USERNAME}/contributions"
OUTPUT_PATH = Path(__file__).resolve().parent.parent / "data" / "contributions.json"


def fetch_contribution_html() -> str:
    headers = {"User-Agent": "Mozilla/5.0 (contribution-fetch-script)"}
    response = requests.get(URL, headers=headers, timeout=15)
    response.raise_for_status()
    return response.text


def parse_days(html: str):
    soup = BeautifulSoup(html, "html.parser")
    days = []

    # GitHub는 <td class="ContributionCalendar-day" ...> 형태로 각 날짜를 렌더링합니다.
    cells = soup.select("td.ContributionCalendar-day")
    for cell in cells:
        date = cell.get("data-date")
        level = cell.get("data-level")
        if date is None:
            continue
        days.append({
            "date": date,
            "level": int(level) if level is not None else 0,
        })

    return days


def compute_stats(days):
    total = 0
    current_streak = 0
    longest_streak = 0
    running_streak = 0

    for day in days:
        has_contribution = day["level"] > 0
        if has_contribution:
            running_streak += 1
            longest_streak = max(longest_streak, running_streak)
        else:
            running_streak = 0

    # 최근 연속일(오늘 기준 역순)은 마지막 날짜부터 거꾸로 계산
    for day in reversed(days):
        if day["level"] > 0:
            current_streak += 1
        else:
            break

    total = sum(1 for d in days if d["level"] > 0)

    return {
        "total_contribution_days": total,
        "current_streak": current_streak,
        "longest_streak": longest_streak,
    }


def main():
    html = fetch_contribution_html()
    days = parse_days(html)

    if not days:
        raise SystemExit(
            "기여도 셀을 하나도 찾지 못했습니다. "
            "GitHub가 마크업을 바꿨거나 사용자명이 틀렸을 수 있습니다."
        )

    stats = compute_stats(days)
    result = {"days": days, "stats": stats}

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"저장 완료: {OUTPUT_PATH}")
    print(f"총 기여일: {stats['total_contribution_days']}")
    print(f"현재 연속: {stats['current_streak']}일")
    print(f"최장 연속: {stats['longest_streak']}일")


if __name__ == "__main__":
    main()