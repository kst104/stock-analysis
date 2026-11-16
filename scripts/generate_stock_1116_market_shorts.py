#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026-11-16 (월) 장마감 시황 쇼츠 생성기 (1회차 · 주식시장 마감 전용)
- 1편: 장마감 데일리 인사이트 (코스피 5,100.50 · 외국인 반도체 매도 · 선물 역방향)
- 칠판 분필 드로잉 특강 스타일 / 겅태 캐릭터 감정 매핑 / 투자 면책 고지 상시 노출
- 실행: python scripts/generate_stock_1116_market_shorts.py
"""

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent      # scripts/
REPO_ROOT = BASE_DIR.parent                    # 저장소 루트

sys.path.insert(0, str(REPO_ROOT))

from engine.stock_chalkboard_engine import render_stock_shorts, FFMPEG_PATH, DISCLAIMER

# 결과물 mp4 출력 위치 (기본: 저장소 output/, 환경변수로 바꿀 수 있음)
DOWNLOADS = Path(os.environ.get("STOCK_SHORTS_OUTPUT", str(REPO_ROOT / "output")))
DOWNLOADS.mkdir(parents=True, exist_ok=True)

# 칠판 드로잉 원본 이미지 (저장소 assets/chalkboard/<회차>)
ART = Path(os.environ.get("STOCK_CHALK_ART_DIR", str(REPO_ROOT / "assets" / "chalkboard" / "stock1116")))

MARKET_DIR = REPO_ROOT / "content" / "2026-11-16" / "03_shorts_market" / "stock_chalkboard"

HEADER = ("김승태의 시장 칠판 특강", "2026.11.16 (월) 장마감")

VIDEO = {
    "id": "Stock1_1116",
    "title": "11/16 장마감 시황 — 외국인이 반도체를 팔고 선물을 산 날",
    "header": HEADER,
    "out": DOWNLOADS / "Stock1_1116_장마감_시황_칠판드로잉_쇼츠.mp4",
    "archive_dir": MARKET_DIR,
    "scenes": [
        {
            "badge": "11월 16일 장마감",
            "keyword": "3.59% 급락",
            "chalk_img": str(ART / "v1_scene1_index_plunge.png"),
            "stats": [
                {"label": "코스피", "value": "5,100.50", "delta": "-190.03 (-3.59%)", "color": "down"},
                {"label": "VKOSPI", "value": "52.68", "delta": "+5.04% (전일 50.15)", "color": "up"},
                {"label": "거래대금", "value": "15.8조", "delta": "상승 263 / 하락 612", "color": "neutral"},
            ],
            "main_text": "코스피 190포인트 하락\n5,100.50 마감",
            "sub_text": "사흘 연속 하락, 5,100선을 반납했습니다",
            "voice": "십일월 십육일 코스피는 백구십 포인트 내린 오천백 소수 오십, 사흘 연속 하락입니다.",
            "character": "expr_surprise",
            "character_label": "",
        },
        {
            "badge": "세 시장 동반 하락",
            "keyword": "코스닥 -4.86%",
            "chalk_img": str(ART / "v1_scene2_three_markets.png"),
            "stats": [
                {"label": "코스닥", "value": "665.65", "delta": "-34.01 (-4.86%)", "color": "down"},
                {"label": "코스피200", "value": "791.56", "delta": "-33.22 (-4.03%)", "color": "down"},
                {"label": "전기·전자", "value": "-5.65%", "delta": "업종 하락 1위", "color": "down"},
            ],
            "main_text": "코스닥도 코스피200도\n같이 밀렸습니다",
            "sub_text": "지수 하락의 무게중심은 반도체와 부품",
            "voice": "코스닥은 사 점 팔육 퍼센트, 코스피이백은 사 점 영삼 퍼센트 빠졌습니다. 세 시장이 같이 밀렸습니다.",
            "character": "expr_worried",
            "character_label": "",
        },
        {
            "badge": "수급 방향은 하나",
            "keyword": "개인이 다 받았다",
            "chalk_img": str(ART / "v1_scene3_individual_absorb.png"),
            "stats": [
                {"label": "외국인", "value": "-1조3,838억", "delta": "유가증권 순매도", "color": "down"},
                {"label": "기관", "value": "-4,513억", "delta": "연기금 -5,647억", "color": "down"},
                {"label": "개인", "value": "+1조3,398억", "delta": "외국인 매도의 97%", "color": "up"},
            ],
            "main_text": "외국인과 기관이 팔고\n개인이 1조3,398억을 받았습니다",
            "sub_text": "지수를 받아낸 쪽은 개인 한 곳입니다",
            "voice": "외국인이 일조 삼천팔백삼십팔억을 팔았고, 개인은 일조 삼천삼백구십팔억을 받아냈습니다.",
            "character": "expr_explain",
            "character_label": "",
        },
        {
            "badge": "매도는 반도체에 집중",
            "keyword": "두 종목 61%",
            "chalk_img": str(ART / "v1_scene4_chip_outflow.png"),
            "stats": [
                {"label": "삼성전자", "value": "196,800", "delta": "-6,194억 (-4.47%)", "color": "down"},
                {"label": "SK하이닉스", "value": "1,120,000", "delta": "-2,242억 (-7.89%)", "color": "down"},
                {"label": "두 종목 합계", "value": "-8,435억", "delta": "코스피 외국인 매도의 61%", "color": "down"},
            ],
            "main_text": "삼성전자와 SK하이닉스\n매도만 8,435억입니다",
            "sub_text": "지수 하락의 대부분이 이 두 종목에서 나왔습니다",
            "voice": "매도는 반도체에 몰렸습니다. 삼성전자와 에스케이하이닉스, 두 종목이 전체 매도의 육십일 퍼센트입니다.",
            "character": "pose_point",
            "character_label": "",
        },
        {
            "badge": "그런데 선물은 반대",
            "keyword": "선물 +3,238억",
            "chalk_img": str(ART / "v1_scene5_spot_vs_futures.png"),
            "stats": [
                {"label": "선물 계약", "value": "+1,620계약", "delta": "외국인 12월물", "color": "up"},
                {"label": "선물 금액", "value": "+3,239억", "delta": "개인 +718억", "color": "up"},
                {"label": "베이시스", "value": "-2.21pt", "delta": "이론가 대비 괴리 -3.69pt", "color": "neutral"},
            ],
            "main_text": "현물은 팔고\n선물은 3,238억 샀습니다",
            "sub_text": "코스피200 선물 외국인 순매수 1,620계약",
            "voice": "그런데 코스피이백 선물에서는 외국인이 삼천이백삼십팔억을 샀습니다. 현물은 팔고 선물은 산 겁니다.",
            "character": "expr_surprise",
            "character_label": "",
        },
        {
            "badge": "해석은 헷지",
            "keyword": "상승 베팅 아님",
            "chalk_img": str(ART / "v1_scene6_volatility_calendar.png"),
            "stats": [
                {"label": "VKOSPI", "value": "52.68", "delta": "+5.04%", "color": "up"},
                {"label": "원·달러", "value": "1,335.70", "delta": "-1.0원 (주간종가)", "color": "neutral"},
                {"label": "비차익 프로그램", "value": "-5,537억", "delta": "지수 바스켓 매도", "color": "down"},
            ],
            "main_text": "상승 베팅이 아니라\n현물 매도를 방어하는 헷지입니다",
            "sub_text": "이번 주 엔비디아 실적·FOMC 의사록·앤트로픽 상장 확인",
            "voice": "상승 베팅이 아니라 현물 매도를 방어하는 헷지입니다. 이번 주 엔비디아 실적과 연준 의사록을 확인하고 가시죠.",
            "character": "pose_wave",
            "character_label": "",
        },
    ],
}


def ffprobe_meta(path: Path) -> dict:
    """ffmpeg 스트림 정보 파싱 (ffprobe 미설치 환경)."""
    import re as _re

    p = subprocess.run([FFMPEG_PATH, "-i", str(path)], capture_output=True, text=True)
    info = {"duration": 0.0, "size": path.stat().st_size, "streams": []}
    for line in p.stderr.split("\n"):
        if "Duration:" in line:
            h, m, s = line.split("Duration:")[1].split(",")[0].strip().split(":")
            info["duration"] = round(float(h) * 3600 + float(m) * 60 + float(s), 2)
        if "Stream" in line and "Video:" in line:
            m = _re.search(r"Video:\s*([^,\s]+)", line)
            wh = _re.search(r"(\d{2,5})x(\d{2,5})", line)
            fp = _re.search(r"([\d.]+)\s*fps", line)
            info["streams"].append({
                "type": "video", "codec": m.group(1) if m else None,
                "w": int(wh.group(1)) if wh else None,
                "h": int(wh.group(2)) if wh else None,
                "fps": fp.group(1) if fp else None,
            })
        if "Stream" in line and "Audio:" in line:
            m = _re.search(r"Audio:\s*([^,\s]+)", line)
            info["streams"].append({"type": "audio", "codec": m.group(1) if m else None,
                                    "w": None, "h": None, "fps": None})
    return info


def write_screenplay(video: dict):
    d = video["archive_dir"]
    d.mkdir(parents=True, exist_ok=True)
    chars = sum(len(s["voice"]) for s in video["scenes"])
    lines = [
        f"# {video['title']} — 유튜브 쇼츠 대본 (칠판 특강 · 1회차)",
        "",
        f"- 헤더: {video['header'][0]} / {video['header'][1]}",
        "- 규격: 1080x1920 세로형 9:16, 25fps, 칠판 분필 드로잉 시장 특강 스타일, 6개 씬",
        "- 음성: Edge-TTS ko-KR-InJoonNeural, 속도 +5% (차분한 남성 톤)",
        f"- 대본 분량: {chars}자",
        "- 수치 표기: 화면은 아라비아 숫자, 내레이션은 한글 발음(예: 일조 삼천팔백삼십팔억)",
        f"- 하단 고지: {DISCLAIMER}",
        "",
        "| 씬 | 배지 | 키워드 | 수치 카드 | 화면 문구 | 내레이션 | 겅태 |",
        "| :--- | :--- | :--- | :--- | :--- | :--- | :--- |",
    ]
    for i, s in enumerate(video["scenes"], 1):
        cards = " / ".join(f"{c['label']} {c['value']}" for c in s["stats"])
        main = s["main_text"].replace("\n", " ")
        lines.append(f"| {i} | {s['badge']} | {s['keyword']} | {cards} | {main} | {s['voice']} | {s['character']} |")
    lines += ["", "## 연출 메모", "- 겅태 감정 매핑: 급락·반전 훅은 놀람/걱정, 수치 설명은 가리키기·설명, 마무리는 환호·인사.", ""]
    (d / "shorts_script.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"✅ 대본 저장: {d / 'shorts_script.md'} ({chars}자)")


def make_preview(video: dict):
    src = video["out"]
    gif = DOWNLOADS / f"{video['id']}_칠판쇼츠_움직이는미리보기.gif"
    total = ffprobe_meta(src)["duration"]
    subprocess.run([
        FFMPEG_PATH, "-y", "-i", str(src),
        "-vf", "fps=1.6,scale=420:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=192[p];[s1][p]paletteuse=dither=bayer",
        "-loop", "0", str(gif),
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    caps = []
    for idx, frac in enumerate([0.10, 0.42, 0.74], 1):
        cap = DOWNLOADS / f"{video['id']}_씬{idx}_미리보기.png"
        subprocess.run([FFMPEG_PATH, "-y", "-ss", f"{total * frac:.2f}", "-i", str(src),
                        "-frames:v", "1", str(cap)], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        caps.append(cap)
    return gif, caps


def build(video: dict):
    write_screenplay(video)
    render_stock_shorts(
        video["scenes"], str(video["out"]),
        header_title=video["header"][0], header_meta=video["header"][1],
        temp_dir=f"/tmp/{video['id']}_build",
    )
    shutil.copy(video["out"], video["archive_dir"] / "chalkboard_shorts_video.mp4")
    gif, caps = make_preview(video)
    meta = ffprobe_meta(video["out"])
    report = {
        "file": str(video["out"]),
        "duration": round(meta["duration"], 2),
        "size_mb": round(meta["size"] / 1024 / 1024, 2),
        "streams": meta["streams"],
        "gif": str(gif),
        "captures": [str(c) for c in caps],
    }
    (video["archive_dir"] / "render_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return report


def main():
    build(VIDEO)


if __name__ == "__main__":
    main()
