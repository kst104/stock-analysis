#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026-11-19 (목) 장마감 시황 쇼츠 생성기 (4회차 · 주식시장 마감 전용)
- 1편: 장마감 데일리 인사이트 (코스피 5,137.89 · 오전 4,963 이탈 후 오후 반등 · 기타법인 4,514억 · 위클리 만기 · 만기 후 플립 799.5)
- 칠판 분필 드로잉 특강 스타일 / 겅태 캐릭터 감정 매핑 / 투자 면책 고지 상시 노출
- 실행: STOCK_SHORTS_OUTPUT=/workspace/downloads python scripts/generate_stock_1119_market_shorts.py
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

DOWNLOADS = Path(os.environ.get("STOCK_SHORTS_OUTPUT", str(REPO_ROOT / "output")))
DOWNLOADS.mkdir(parents=True, exist_ok=True)

ART = Path(os.environ.get("STOCK_CHALK_ART_DIR", str(REPO_ROOT / "assets" / "chalkboard" / "stock1119")))

MARKET_DIR = REPO_ROOT / "content" / "2026-11-19" / "03_shorts_market" / "stock_chalkboard"

HEADER = ("김승태의 시장 칠판 특강", "2026.11.19 (목) 장마감")

VIDEO = {
    "id": "Stock1_1119",
    "title": "11/19 장마감 시황 — 오전 -2%를 오후에 뒤집었다, 만기 콜이 지수를 붙잡았다",
    "header": HEADER,
    "out": DOWNLOADS / "Stock1_1119_장마감_시황_칠판드로잉_쇼츠.mp4",
    "archive_dir": MARKET_DIR,
    "scenes": [
        {
            "badge": "11월 19일 장마감",
            "keyword": "5,137.89",
            "chalk_img": str(ART / "v1_scene1_index_v_rebound.png"),
            "stats": [
                {"label": "코스피", "value": "5,137.89", "delta": "+70.45 (+1.39%)", "color": "up"},
                {"label": "코스닥", "value": "684.81", "delta": "+22.00 (+3.32%)", "color": "up"},
                {"label": "코스피200", "value": "796.34", "delta": "+1.10%", "color": "up"},
            ],
            "main_text": "코스피 5,137.89\n이틀 연속 상승입니다",
            "sub_text": "수능일이라 10시에 열고 4시 30분에 닫은 장",
            "voice": "십일월 십구일 코스피는 칠십 포인트 오른 오천백삼십칠에 마감했습니다.",
            "character": "expr_happy",
            "character_label": "",
        },
        {
            "badge": "오전엔 5,000선 이탈",
            "keyword": "4,963.61",
            "chalk_img": str(ART / "v1_scene2_dip_below_5000.png"),
            "stats": [
                {"label": "장중 저가", "value": "4,963.61", "delta": "-2.05%", "color": "down"},
                {"label": "종가", "value": "5,137.89", "delta": "+1.39%", "color": "up"},
                {"label": "고저 차", "value": "174p", "delta": "하루 등락", "color": "neutral"},
            ],
            "main_text": "오전에 5,000선을 내줬다가\n오후에 되찾았습니다",
            "sub_text": "코스피200도 771.85까지 내려갔습니다",
            "voice": "오전 열 시 삼십오 분에는 사천구백육십삼까지 밀렸습니다. 오천선을 다시 내준 자리입니다.",
            "character": "expr_surprise",
            "character_label": "",
        },
        {
            "badge": "오후에 판이 뒤집혔다",
            "keyword": "수출 1조달러",
            "chalk_img": str(ART / "v1_scene3_other_corp_buy.png"),
            "stats": [
                {"label": "2시 9분", "value": "수출 1조달러", "delta": "누적 돌파 발표", "color": "up"},
                {"label": "오락·문화", "value": "+9.39%", "delta": "한한령 완화 기대", "color": "up"},
                {"label": "코스닥", "value": "+3.32%", "delta": "상승 1,170종목", "color": "up"},
            ],
            "main_text": "수출 1조달러 소식에\n오후에 올라섰습니다",
            "sub_text": "하이브 +13.69%, 아모레퍼시픽 +9.03%",
            "voice": "오후 두 시, 수출 일조 달러 소식에 반등이 시작됐고 장 막판에 오천백삼십선에 안착했습니다.",
            "character": "pose_point",
            "character_label": "",
        },
        {
            "badge": "받아낸 건 기타법인",
            "keyword": "+4,514억",
            "chalk_img": str(ART / "v1_scene4_foreign_sell_five.png"),
            "stats": [
                {"label": "외국인", "value": "-4,036억", "delta": "5거래일 연속 매도", "color": "down"},
                {"label": "개인", "value": "-652억", "delta": "오후에 차익 실현", "color": "down"},
                {"label": "기타법인", "value": "+4,514억", "delta": "이틀 연속 4,500억대", "color": "up"},
            ],
            "main_text": "외국인과 개인이 팔고\n기타법인이 받았습니다",
            "sub_text": "기관은 192억으로 사실상 중립이었습니다",
            "voice": "외국인 사천삼십육억, 개인 육백오십이억을 팔았고, 기타법인이 사천오백십사억을 받아냈습니다.",
            "character": "expr_explain",
            "character_label": "",
        },
        {
            "badge": "목요일 위클리 만기",
            "keyword": "795~797.5 콜 벽",
            "chalk_img": str(ART / "v1_scene5_weekly_call_wall.png"),
            "stats": [
                {"label": "총 감마", "value": "+1조 3,080억", "delta": "1% 변동당", "color": "up"},
                {"label": "795 콜", "value": "+1조 1,183억", "delta": "미결제 3,915계약", "color": "up"},
                {"label": "797.5 콜", "value": "+3,226억", "delta": "미결제 1,003계약", "color": "up"},
            ],
            "main_text": "만기 콜이 지수를\n795~797.5에 붙잡았습니다",
            "sub_text": "오전 12시 15분엔 감마 -1,899억, 플립 아래였습니다",
            "voice": "위클리 만기였습니다. 구백구십오와 구백구십칠 포인트 오에 콜이 몰렸고, 지수는 그 사이에서 끝났습니다.",
            "character": "pose_point",
            "character_label": "",
        },
        {
            "badge": "만기 뒤엔 부호가 바뀐다",
            "keyword": "플립 799.5",
            "chalk_img": str(ART / "v1_scene6_gamma_flip_after.png"),
            "stats": [
                {"label": "만기 후 감마", "value": "-50억", "delta": "월물 -166억 + 위클리 +116억", "color": "down"},
                {"label": "만기 후 플립", "value": "799.5", "delta": "종가 796.34는 아래", "color": "neutral"},
                {"label": "등가격 IV", "value": "49.91%", "delta": "전일 52.59%", "color": "up"},
            ],
            "main_text": "완충은 오늘로 사라졌습니다\n내일은 799.5가 기준입니다",
            "sub_text": "외국인 현물 순매수 전환인지도 함께 봅니다",
            "voice": "위클리 감마 일조 삼천억은 오늘로 사라졌습니다. 만기 뒤 플립은 칠백구십구 포인트 오, 내일은 그 위 출발이 관건입니다.",
            "character": "pose_wave",
            "character_label": "",
        },
    ],
}


def ffprobe_meta(path: Path) -> dict:
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


def _show(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(Path("/workspace")))
    except Exception:
        try:
            return str(path.resolve().relative_to(REPO_ROOT))
        except Exception:
            return str(path)


def write_screenplay(video: dict):
    d = video["archive_dir"]
    d.mkdir(parents=True, exist_ok=True)
    chars = sum(len(s["voice"]) for s in video["scenes"])
    lines = [
        f"# {video['title']} — 유튜브 쇼츠 대본 (칠판 특강 · 4회차)",
        "",
        f"- 헤더: {video['header'][0]} / {video['header'][1]}",
        f"- 규격: 1080x1920 세로형 9:16, 25fps, 칠판 분필 드로잉 시장 특강 스타일, {len(video['scenes'])}개 씬",
        "- 음성: Edge-TTS ko-KR-InJoonNeural, 속도 +5% (차분한 남성 톤)",
        f"- 대본 분량: {chars}자",
        "- 수치 표기: 화면은 아라비아 숫자, 내레이션은 한글 발음(예: 일조 삼천억)",
        f"- 하단 고지: {DISCLAIMER}",
        "",
        "| 씬 | 배지 | 키워드 | 수치 카드 | 화면 문구 | 내레이션 | 겅태 |",
        "| :--- | :--- | :--- | :--- | :--- | :--- | :--- |",
    ]
    for i, s in enumerate(video["scenes"], 1):
        cards = " / ".join(f"{c['label']} {c['value']}" for c in s["stats"])
        main = s["main_text"].replace("\n", " ")
        lines.append(f"| {i} | {s['badge']} | {s['keyword']} | {cards} | {main} | {s['voice']} | {s['character']} |")
    lines += ["", "## 연출 메모", "- 겅태 감정 매핑: 지수 훅은 기쁨/놀람, 수급 설명은 가리키기·설명, 마무리는 인사.", ""]
    (d / "shorts_script.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"✅ 대본 저장: {d / 'shorts_script.md'} ({chars}자)")


def make_preview(video: dict):
    src = video["out"]
    gif = DOWNLOADS / f"{video['id']}_미리보기.gif"
    total = ffprobe_meta(src)["duration"]
    subprocess.run([
        FFMPEG_PATH, "-y", "-i", str(src),
        "-vf", "fps=1.6,scale=420:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=192[p];[s1][p]paletteuse=dither=bayer",
        "-loop", "0", str(gif),
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    caps = []
    for idx, frac in enumerate([0.10, 0.42, 0.74], 1):
        cap = DOWNLOADS / f"{video['id']}_scene_{idx}.png"
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
    preview_dir = video["archive_dir"] / "preview"
    preview_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy(gif, preview_dir / "moving_preview.gif")
    for i, c in enumerate(caps, 1):
        shutil.copy(c, preview_dir / f"scene{i}_preview.png")
    meta = ffprobe_meta(video["out"])
    report = {
        "file": _show(video["out"]),
        "duration": round(meta["duration"], 2),
        "size_mb": round(meta["size"] / 1024 / 1024, 2),
        "streams": meta["streams"],
        "gif": _show(gif),
        "captures": [_show(c) for c in caps],
    }
    (video["archive_dir"] / "render_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return report


def main():
    build(VIDEO)


if __name__ == "__main__":
    main()
