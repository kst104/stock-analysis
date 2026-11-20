#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-20 (금) 장마감 시황 쇼츠 생성기 (5회차 · 올.주.선.이 3단 레이아웃)
- 1편: 검은 금요일, 코스피 4,869.96(-5.21%), 매도 사이드카, 반도체 급락, 감마 플립 764.55
- 실행: STOCK_SHORTS_OUTPUT=/workspace/downloads python scripts/generate_stock_1120_market_shorts.py
"""

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
REPO_ROOT = BASE_DIR.parent
sys.path.insert(0, str(REPO_ROOT))

from engine.stock_jaljab_engine import render_shorts, FFMPEG_PATH, FOOTER, TOP_LINE

DOWNLOADS = Path(os.environ.get("STOCK_SHORTS_OUTPUT", str(REPO_ROOT / "output")))
DOWNLOADS.mkdir(parents=True, exist_ok=True)
ART = Path(os.environ.get("STOCK_CHALK_ART_DIR", str(REPO_ROOT / "assets" / "chalkboard" / "stock1120")))
ARCHIVE = REPO_ROOT / "content" / "2026-11-20" / "03_shorts_market" / "stock_chalkboard"

VIDEO = {
    "id": "Stock1_1120",
    "title": "11/20 검은 금요일 — 코스피 5.21% 급락, 마지막 5분에 외국인이 숏을 되샀다",
    "out": DOWNLOADS / "Stock1_1120_장마감_시황_칠판드로잉_쇼츠.mp4",
    "scenes": [
        {
            "topic": "코스피 -5.21%",
            "caption": "코스피 4,869.96 · 5.21% 급락",
            "chalk_img": str(ART / "v1_scene1_crash.png"),
            "voice": "십일월 이십일 코스피는 이백육십칠 포인트 내린 사천팔백육십구 포인트 구육에 마감했습니다. 오 퍼센트대 급락입니다.",
        },
        {
            "topic": "개장부터 -4%",
            "caption": "시가 4,928.51 · 장중 4,831.69",
            "chalk_img": str(ART / "v1_scene2_gap_down.png"),
            "voice": "시초가부터 사 퍼센트가 빠졌고 장중에는 육 퍼센트 가까이 밀렸습니다. 열 달 만에 가장 낮은 자리입니다.",
        },
        {
            "topic": "매도 사이드카",
            "caption": "오전 11시 54분 · 오후 1시 28분",
            "chalk_img": str(ART / "v1_scene3_sidecar.png"),
            "voice": "오전 열한 시 오십사 분 코스피에, 오후 한 시 이십팔 분 코스닥에 매도 사이드카가 발동했습니다. 프로그램 매도호가가 오 분간 멈췄습니다.",
        },
        {
            "topic": "외국인 1조1,420억 매도",
            "caption": "개인 1조5,955억이 받아냈다",
            "chalk_img": str(ART / "v1_scene4_flows.png"),
            "voice": "외국인이 일조 천사백이십억, 기관이 구천오백십억을 팔았습니다. 개인은 일조 오천구백오십오억을 사서 받아냈습니다.",
        },
        {
            "topic": "반도체 급락",
            "caption": "삼성전자 -7.01% · SK하이닉스 -5.92%",
            "chalk_img": str(ART / "v1_scene5_chips.png"),
            "voice": "삼성전자가 칠 퍼센트, 에스케이하이닉스가 육 퍼센트 빠졌습니다. 삼성전기는 열두 퍼센트 넘게 밀렸습니다.",
        },
        {
            "topic": "감마 플립 764.55",
            "caption": "종가 755.34 · 플립 아래 1.20%",
            "chalk_img": str(ART / "v1_scene6_gamma.png"),
            "voice": "감마는 마이너스 사백삼십오억으로 돌아섰습니다. 플립은 칠백육십사 포인트 오, 종가는 그 아래입니다. 다음 주는 이 선이 기준입니다.",
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
            wh = _re.search(r"(\d{2,5})x(\d{2,5})", line)
            fp = _re.search(r"([\d.]+)\s*fps", line)
            info["streams"].append({"type": "video", "w": int(wh.group(1)) if wh else None,
                                    "h": int(wh.group(2)) if wh else None, "fps": fp.group(1) if fp else None})
        if "Stream" in line and "Audio:" in line:
            info["streams"].append({"type": "audio"})
    return info


def _show(p: Path) -> str:
    try:
        return str(p.resolve().relative_to(Path("/workspace")))
    except Exception:
        try:
            return str(p.resolve().relative_to(REPO_ROOT))
        except Exception:
            return str(p)


def write_script(video: dict):
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    chars = sum(len(s["voice"]) for s in video["scenes"])
    lines = [
        f"# {video['title']} — 유튜브 쇼츠 대본 (올.주.선.이 · 5회차)",
        "",
        f"- 상단 훅: {TOP_LINE} / 네이비 박스: 올.주.선.이 · <주제>",
        f"- 규격: 1080x1920 세로형 9:16, 25fps, 3단 레이아웃(상단 흰색·중단 칠판 1080x860·하단 흰색), {len(video['scenes'])}개 씬",
        "- 음성: Edge-TTS ko-KR-InJoonNeural, 속도 +5%",
        f"- 대본 분량: {chars}자",
        "- 시작 0.0~2.0초: '구독·알림·좋아요는 힘이 됩니다' 배지 오버레이",
        "- 수치 표기: 화면은 아라비아 숫자, 내레이션은 한글 발음",
        f"- 하단 안내문: {FOOTER}",
        "",
        "| 씬 | 주제 | 자막 | 내레이션 |",
        "| :--- | :--- | :--- | :--- |",
    ]
    for i, s in enumerate(video["scenes"], 1):
        lines.append(f"| {i} | {s['topic']} | {s['caption']} | {s['voice']} |")
    lines.append("")
    (ARCHIVE / "shorts_script.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"✅ 대본 저장 ({chars}자)")


def make_preview(video: dict):
    src = video["out"]
    gif = DOWNLOADS / f"{video['id']}_미리보기.gif"
    total = ffprobe_meta(src)["duration"]
    subprocess.run([FFMPEG_PATH, "-y", "-i", str(src), "-vf",
                    "fps=1.6,scale=420:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=192[p];[s1][p]paletteuse=dither=bayer",
                    "-loop", "0", str(gif)], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    caps = []
    for idx, ts in enumerate([0.5, total * 0.30, total * 0.62], 1):
        cap = DOWNLOADS / f"{video['id']}_scene_{idx}.png"
        subprocess.run([FFMPEG_PATH, "-y", "-ss", f"{ts:.2f}", "-i", str(src),
                        "-frames:v", "1", str(cap)], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        caps.append(cap)
    return gif, caps


def build(video: dict):
    write_script(video)
    render_shorts(video["scenes"], str(video["out"]), temp_dir=f"/tmp/{video['id']}_build")
    shutil.copy(video["out"], ARCHIVE / "chalkboard_shorts_video.mp4")
    gif, caps = make_preview(video)
    pdir = ARCHIVE / "preview"
    pdir.mkdir(parents=True, exist_ok=True)
    shutil.copy(gif, pdir / "moving_preview.gif")
    for i, c in enumerate(caps, 1):
        shutil.copy(c, pdir / f"scene{i}_preview.png")
    meta = ffprobe_meta(video["out"])
    report = {"file": _show(video["out"]), "duration": round(meta["duration"], 2),
              "size_mb": round(meta["size"] / 1024 / 1024, 2), "streams": meta["streams"],
              "gif": _show(gif), "captures": [_show(c) for c in caps],
              "layout": "jaljab(올.주.선.이 3단)", "subscribe_badge": "0.0~2.0s"}
    (ARCHIVE / "render_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return report


if __name__ == "__main__":
    build(VIDEO)
