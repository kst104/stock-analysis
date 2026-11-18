#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026-11-18 (수) 장마감 시황 쇼츠 생성기 (3회차 · 주식시장 마감 전용)
- 1편: 장마감 데일리 인사이트 (코스피 5,067.44 · 5,000선 회복 · 190포인트 왕복 · 기관 매수 · 외국인 오후 매도 · 종가 선물 청산)
- 칠판 분필 드로잉 특강 스타일 / 겅태 캐릭터 감정 매핑 / 투자 면책 고지 상시 노출
- 실행: STOCK_SHORTS_OUTPUT=/workspace/downloads python scripts/generate_stock_1118_market_shorts.py
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
ART = Path(os.environ.get("STOCK_CHALK_ART_DIR", str(REPO_ROOT / "assets" / "chalkboard" / "stock1118")))

MARKET_DIR = REPO_ROOT / "content" / "2026-11-18" / "03_shorts_market" / "stock_chalkboard"

HEADER = ("김승태의 시장 칠판 특강", "2026.11.18 (수) 장마감")

VIDEO = {
    "id": "Stock1_1118",
    "title": "11/18 장마감 시황 — 5,000선을 되찾았는데 외국인은 다 팔았다",
    "header": HEADER,
    "out": DOWNLOADS / "Stock1_1118_장마감_시황_칠판드로잉_쇼츠.mp4",
    "archive_dir": MARKET_DIR,
    "scenes": [
        {
            "badge": "11월 18일 장마감",
            "keyword": "5,000선 회복",
            "chalk_img": str(ART / "v1_scene1_5000_reclaim.png"),
            "stats": [
                {"label": "코스피", "value": "5,067.44", "delta": "+98.96 (+1.99%)", "color": "up"},
                {"label": "코스피200", "value": "787.71", "delta": "+16.97 (+2.20%)", "color": "up"},
                {"label": "코스닥", "value": "662.81", "delta": "+12.75 (+1.96%)", "color": "up"},
            ],
            "main_text": "코스피 5,067.44\n5,000선을 되찾았습니다",
            "sub_text": "9개월 반 만에 내줬던 5,000선, 하루 만의 회복",
            "voice": "십일월 십팔일 코스피는 구십팔 포인트 오른 오천육십칠에 마감했습니다. 하루 만에 오천선을 되찾았습니다.",
            "character": "expr_happy",
            "character_label": "",
        },
        {
            "badge": "하루에 190포인트",
            "keyword": "일중 3.82%",
            "chalk_img": str(ART / "v1_scene2_intraday_swing.png"),
            "stats": [
                {"label": "고가", "value": "5,133.14", "delta": "+3.31%", "color": "up"},
                {"label": "저가", "value": "4,943.17", "delta": "-0.51%", "color": "down"},
                {"label": "고저 차", "value": "189.97p", "delta": "일중 3.82%", "color": "neutral"},
            ],
            "main_text": "오전에 다 밀렸다가\n오후에 다시 올라섰습니다",
            "sub_text": "코스피200도 799.52에서 767.09까지 왔다 갔습니다",
            "voice": "장 초반 삼 점 삼일 퍼센트까지 올랐다가 사천구백사십삼까지 밀렸고, 오후에 다시 올라섰습니다.",
            "character": "expr_surprise",
            "character_label": "",
        },
        {
            "badge": "거래대금 43% 증가",
            "keyword": "20조3,426억",
            "chalk_img": str(ART / "v1_scene3_volume_return.png"),
            "stats": [
                {"label": "코스피", "value": "20조3,426억", "delta": "전일 대비 +43.3%", "color": "up"},
                {"label": "전일", "value": "14조1,960억", "delta": "12년 6개월 최소였던 날", "color": "neutral"},
                {"label": "코스닥", "value": "5조5,167억", "delta": "넥스트레이드 7조2,638억", "color": "up"},
            ],
            "main_text": "어제 14조에서\n20조로 돌아왔습니다",
            "sub_text": "얇아졌던 시장에 하루 만에 사람이 들어왔습니다",
            "voice": "거래대금은 이십조 삼천사백이십육억. 어제 십사조에서 사십삼 퍼센트 늘었습니다.",
            "character": "pose_point",
            "character_label": "",
        },
        {
            "badge": "받아낸 건 기관",
            "keyword": "기관 +5,118억",
            "chalk_img": str(ART / "v1_scene4_institution_buy.png"),
            "stats": [
                {"label": "외국인", "value": "-3,338억", "delta": "4거래일 연속 매도", "color": "down"},
                {"label": "기관", "value": "+5,118억", "delta": "금융투자 +3,189억", "color": "up"},
                {"label": "기타법인", "value": "+4,600억", "delta": "개인 -6,380억", "color": "up"},
            ],
            "main_text": "외국인과 개인이 팔고\n기관과 기타법인이 받았습니다",
            "sub_text": "대형주 +2.15%, 중형주 +0.41%, 소형주 +0.15%",
            "voice": "외국인 삼천삼백삼십팔억, 개인 육천삼백팔십억을 팔았고, 기관 오천백십팔억과 기타법인 사천육백억이 받아냈습니다.",
            "character": "expr_explain",
            "character_label": "",
        },
        {
            "badge": "외국인은 아침에 샀다",
            "keyword": "991억 → -3,338억",
            "chalk_img": str(ART / "v1_scene5_semis_rebound.png"),
            "stats": [
                {"label": "09:05", "value": "+991억", "delta": "장 초반 순매수", "color": "up"},
                {"label": "15:22", "value": "-4,216억", "delta": "오후 최대 매도", "color": "down"},
                {"label": "종가", "value": "-3,338억", "delta": "878억 되사며 마감", "color": "down"},
            ],
            "main_text": "아침에 사고\n오후에 다 팔았습니다",
            "sub_text": "엔비디아 실적에 산 반도체를 정오부터 되팔았습니다",
            "voice": "외국인은 아침 구 시에 구백구십일억 순매수였는데, 정오에 돌아서서 종가에는 삼천삼백삼십팔억 매도로 끝났습니다.",
            "character": "expr_worried",
            "character_label": "",
        },
        {
            "badge": "종가는 선물도 팔았다",
            "keyword": "2,145 → -323계약",
            "chalk_img": str(ART / "v1_scene7_auction_handback.png"),
            "stats": [
                {"label": "장중 최대", "value": "+2,145계약", "delta": "14시 27분", "color": "up"},
                {"label": "15:25", "value": "+1,597계약", "delta": "동시호가 진입", "color": "up"},
                {"label": "종가", "value": "-323계약", "delta": "1,920계약 뒤집힘", "color": "down"},
            ],
            "main_text": "선물도 되팔았습니다\n확인은 내일입니다",
            "sub_text": "19일 위클리 만기와 앤트로픽 상장이 겹칩니다",
            "voice": "선물도 장중 이천백사십오 계약까지 샀는데, 마감 동시호가에 천백칠십 계약을 되팔았습니다. 내일 만기와 앤트로픽 상장이 확인 지점입니다.",
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


def _show(path: Path) -> str:
    """리포트 표기용 경로 (워크스페이스 기준 상대 경로)."""
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
        f"# {video['title']} — 유튜브 쇼츠 대본 (칠판 특강 · 3회차)",
        "",
        f"- 헤더: {video['header'][0]} / {video['header'][1]}",
        f"- 규격: 1080x1920 세로형 9:16, 25fps, 칠판 분필 드로잉 시장 특강 스타일, {len(video['scenes'])}개 씬",
        "- 음성: Edge-TTS ko-KR-InJoonNeural, 속도 +5% (차분한 남성 톤)",
        f"- 대본 분량: {chars}자",
        "- 수치 표기: 화면은 아라비아 숫자, 내레이션은 한글 발음(예: 이십조 삼천사백이십육억)",
        f"- 하단 고지: {DISCLAIMER}",
        "",
        "| 씬 | 배지 | 키워드 | 수치 카드 | 화면 문구 | 내레이션 | 겅태 |",
        "| :--- | :--- | :--- | :--- | :--- | :--- | :--- |",
    ]
    for i, s in enumerate(video["scenes"], 1):
        cards = " / ".join(f"{c['label']} {c['value']}" for c in s["stats"])
        main = s["main_text"].replace("\n", " ")
        lines.append(f"| {i} | {s['badge']} | {s['keyword']} | {cards} | {main} | {s['voice']} | {s['character']} |")
    lines += ["", "## 연출 메모", "- 겅태 감정 매핑: 회복 훅은 기쁨/놀람, 수급 설명은 가리키기·설명, 마무리는 인사.", ""]
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
