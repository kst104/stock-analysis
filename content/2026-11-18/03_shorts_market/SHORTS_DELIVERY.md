# SHORTS DELIVERY — 11/18 장마감 시황 (3회차 · 시장 마감 편)

## 산출물
| 항목 | 경로 |
| --- | --- |
| 유튜브 쇼츠 MP4 | `downloads/Stock1_1118_장마감_시황_칠판드로잉_쇼츠.mp4` (저장소 사본 `content/2026-11-18/03_shorts_market/stock_chalkboard/chalkboard_shorts_video.mp4`) |
| 움직이는 미리보기 GIF | `downloads/Stock1_1118_미리보기.gif` (사본 `preview/moving_preview.gif`) |
| 씬 캡처 3장 | `downloads/Stock1_1118_scene_1~3.png` (사본 `preview/scene{1,2,3}_preview.png`) |
| 대본 | `content/2026-11-18/03_shorts_market/stock_chalkboard/shorts_script.md` |
| 생성 스크립트 | `scripts/generate_stock_1118_market_shorts.py` + `engine/stock_chalkboard_engine.py` |
| 칠판 드로잉 원본 7장 | `assets/chalkboard/stock1118/v1_scene1~7_*.png` |
| 검증 리포트 | `content/2026-11-18/03_shorts_market/stock_chalkboard/render_report.json` |

## 규격 (ffmpeg 검증)
- 1080x1920 (SAR 1:1, DAR 9:16 세로), H.264 High, **25.00 fps CFR (57.43초)**
- 오디오 AAC LC 44.1kHz 모노, Edge-TTS `ko-KR-InJoonNeural` (+5%)
- 용량 3.34MB, mean_volume -20.5dB / max -3.6dB

## 구성 (6씬 · 57초)
| 씬 | 배지 | 노란 키워드 | 수치 카드 | 겅태 |
| --- | --- | --- | --- | --- |
| 1 | 11월 18일 장마감 | 5,000선 회복 | 코스피 5,067.44 / 코스피200 787.71 / 코스닥 662.81 | 기쁨 |
| 2 | 하루에 190포인트 | 일중 3.82% | 고가 5,133.14 / 저가 4,943.17 / 고저 차 189.97p | 놀람 |
| 3 | 거래대금 43% 증가 | 20조3,426억 | 코스피 20조3,426억 / 전일 14조1,960억 / 코스닥 5조5,167억 | 가리키기 |
| 4 | 받아낸 건 기관 | 기관 +5,118억 | 외국인 -3,338억 / 기관 +5,118억 / 기타법인 +4,600억 | 설명 |
| 5 | 외국인은 아침에 샀다 | 991억 → -3,338억 | 09:05 +991억 / 15:22 -4,216억 / 종가 -3,338억 | 걱정 |
| 6 | 종가는 선물도 팔았다 | 2,145 → -323계약 | 장중 +2,145계약 / 15:25 +1,597계약 / 종가 -323계약 | 인사 |

## 업로드 문구안
- 제목: 5,000선은 돌아왔는데 외국인은 아침에 산 걸 다 팔았습니다 (11/18 코스피 마감)
- 설명 첫 줄: 코스피 5,067.44(+1.99%), 하루에 190포인트를 오갔습니다. 외국인은 991억 순매수로 시작해 3,338억 매도로 끝났습니다.
- 고지: 본 영상은 투자 권유가 아닌 시장 기록 및 정보 정리입니다.

## 고지
전 씬 하단 고정: "본 영상은 투자 권유가 아닌 시장 기록 및 정보 정리입니다."

## 출처
`content/2026-11-18/01_market_daily_insight.md` (한국거래소 마감 집계, 8766 KIS 누적, 18901 감마)
자매 저장소의 수급 심화 편: `kst104/stock-future` `content/2026-11-18/04_shorts_foreign_flow/`
