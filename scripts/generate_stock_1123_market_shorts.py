#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-23 (월) 장마감 시황 쇼츠 생성기 (6회차 · 올.주.선.이 3단 레이아웃)
- 6씬 + 마지막 방향성 컷(오늘의 방향 / 내일의 예상, 우측 상단 11/23~ 집계 시작)
- 실행: STOCK_SHORTS_OUTPUT=/workspace/downloads python scripts/generate_stock_1123_market_shorts.py
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
ART = Path(os.environ.get("STOCK_CHALK_ART_DIR", str(REPO_ROOT / "assets" / "chalkboard" / "stock1123")))
ARCHIVE = REPO_ROOT / "content" / "2026-11-23" / "03_shorts_market" / "stock_chalkboard"

VIDEO = {
    "id": "Stock1_1123",
    "title": "11/23 장마감 시황 — 이틀에 8.36%, 장중 5.80% 밀렸다가 4,700선 사수",
    "out": DOWNLOADS / "Stock1_1123_장마감_시황_칠판드로잉_쇼츠.mp4",
    "scenes": [
        {
            "topic": "코스피 -3.31%",
            "caption": "코스피 4,708.54 · 161.42포인트 하락",
            "chalk_img": str(ART / "v1_scene1_index.png"),
            "voice": "이십삼일 코스피는 백육십일 포인트 내린 사천칠백팔 점 오사에 마감했습니다. 삼 점 삼일 퍼센트 하락입니다.",
        },
        {
            "topic": "장중 -5.80%",
            "caption": "시가 4,734.90 · 저가 4,586.80",
            "chalk_img": str(ART / "v1_scene2_rebound.png"),
            "voice": "사천칠백삼십사로 출발해 오전에 사천오백팔십육까지 밀렸습니다. 장중으로 오 점 팔 퍼센트 하락입니다.",
        },
        {
            "topic": "매도 사이드카",
            "caption": "11시 33분 발동 · 이틀 연속",
            "chalk_img": str(ART / "v1_scene3_sidecar.png"),
            "voice": "오전 열한 시 삼십삼 분, 이틀 연속 매도 사이드카가 걸렸습니다. 올해 서른두 번째입니다.",
        },
        {
            "topic": "기관만 순매수",
            "caption": "외국인 -2,472억 · 개인 -3,670억 · 기관 +1,872억",
            "chalk_img": str(ART / "v1_scene4_flows.png"),
            "voice": "외국인이 이천사백칠십억, 개인이 삼천육백칠십억을 팔았고, 기관만 천팔백칠십억을 샀습니다.",
        },
        {
            "topic": "반도체·건설 약세",
            "caption": "삼성전자 -3.06% · 건설 -6.91%",
            "chalk_img": str(ART / "v1_scene5_chips.png"),
            "voice": "삼성전자 삼 퍼센트, 에스케이하이닉스 이 점 오 퍼센트. 건설 업종은 칠 퍼센트 가까이 빠졌습니다.",
        },
        {
            "topic": "감마 플립 732.12",
            "caption": "총 감마 -9,238억 · 괴리 -5.32pt",
            "chalk_img": str(ART / "v1_scene6_gamma.png"),
            "voice": "감마는 마이너스 구간, 플립은 칠백삼십이 포인트 일입니다. 선물은 이론가보다 오 포인트 넘게 싸게 끝났습니다.",
        },
        {
            "type": "direction",
            "topic": "오늘·내일 방향",
            "today_label": "중간하방",
            "tomorrow_label": "약간 상방 또는 횡보",
            "accuracy_text": "11/23~ 집계 시작",
            "hold": 2.0,
            "voice": "오늘의 방향은 중간 하방이었습니다. 내일은 약간 상방 또는 횡보로 봅니다.",
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
        f"# {video['title']} — 유튜브 쇼츠 대본 (올.주.선.이 · 6회차)",
        "",
        f"- 상단 훅: {TOP_LINE} / 네이비 박스: 올.주.선.이 · <주제>",
        f"- 규격: 1080x1920 세로형 9:16, 25fps, 3단 레이아웃(상단 흰색·중단 칠판 1080x860·하단 흰색), {len(video['scenes'])}개 씬",
        "- 음성: Edge-TTS ko-KR-SunHiNeural, 속도 +5%",
        f"- 대본 분량: {chars}자",
        "- 시작 0.0~2.0초: '구독·알림·좋아요는 힘이 됩니다' 배지 오버레이",
        "- 마지막 컷: 오늘의 방향 / 내일의 예상 + 우측 상단 '11/23~ 집계 시작'",
        f"- 하단 안내문: {FOOTER}",
        "",
        "| 씬 | 주제 | 자막 | 내레이션 |",
        "| :--- | :--- | :--- | :--- |",
    ]
    for i, s in enumerate(video["scenes"], 1):
        cap = s.get("caption") or f"오늘의 방향: {s.get('today_label')} / 내일의 예상: {s.get('tomorrow_label')}"
        lines.append(f"| {i} | {s['topic']} | {cap} | {s['voice']} |")
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
    for idx, ts in enumerate([0.5, total * 0.30, total - 1.2], 1):
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
              "layout": "jaljab(올.주.선.이 3단)", "subscribe_badge": "0.0~2.0s",
              "direction_cut": "last scene (오늘의 방향 / 내일의 예상 / 11/23~ 집계 시작)"}
    (ARCHIVE / "render_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return report


if __name__ == "__main__":
    build(VIDEO)
