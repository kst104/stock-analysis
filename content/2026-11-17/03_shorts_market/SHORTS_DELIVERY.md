# SHORTS DELIVERY — 11/17 장마감 시황 (2회차 · 시장 마감 편)

## 산출물
| 항목 | 경로 |
| --- | --- |
| 유튜브 쇼츠 MP4 | `downloads/Stock1_1117_장마감_시황_칠판드로잉_쇼츠.mp4` (저장소 사본 `content/2026-11-17/03_shorts_market/stock_chalkboard/chalkboard_shorts_video.mp4`) |
| 움직이는 미리보기 GIF | `downloads/Stock1_1117_미리보기.gif` (사본 `preview/moving_preview.gif`) |
| 씬 캡처 3장 | `downloads/Stock1_1117_scene_1~3.png` (사본 `preview/scene{1,2,3}_preview.png`) |
| 대본 | `content/2026-11-17/03_shorts_market/stock_chalkboard/shorts_script.md` |
| 생성 스크립트 | `scripts/generate_stock_1117_market_shorts.py` + `engine/stock_chalkboard_engine.py` |
| 칠판 드로잉 원본 7장 | `assets/chalkboard/stock1117/v1_scene1~7_*.png` |
| 검증 리포트 | `content/2026-11-17/03_shorts_market/stock_chalkboard/render_report.json` |

## 규격 (ffmpeg 검증)
- 1080x1920 (SAR 1:1, DAR 9:16 세로), H.264 High, **25.00 fps CFR (1,685프레임 = 67.40초)**
- 오디오 AAC LC 44.1kHz 모노, Edge-TTS `ko-KR-InJoonNeural` (+5%)
- 용량 4.32MB, mean_volume -20.9dB / max -3.6dB

## 구성 (7씬 · 67초)
| 씬 | 배지 | 노란 키워드 | 수치 카드 | 겅태 |
| --- | --- | --- | --- | --- |
| 1 | 11월 17일 장마감 | 5,000선 붕괴 | 코스피 4,968.48 / 2월 2일 이후 최저 / 나흘 -7.57% | 놀람 |
| 2 | 세 시장 동반 하락 | 코스닥 -2.34% | 코스닥 650.06 / 코스피200 770.74 / 시총 4,076조 | 걱정 |
| 3 | 12년 6개월 만에 가장 한산 | 거래대금 14조 | 거래대금 14조1,960억 / 거래량 1억8,309만주 / 예탁금 86조9,247억 | 설명 |
| 4 | 수급은 한 방향 | 개인은 29%만 | 외국인 -1조4,430억 / 기관 +5,436억 / 개인 +4,218억 | 가리키기 |
| 5 | 매도는 두 종목에 | 전체의 72% | 삼성전자 190,300 / SK하이닉스 1,098,000 / 기관 +3,241억 | 설명 |
| 6 | 하락의 무게는 반도체 밖 | 유틸리티 -4.84% | 유틸리티 -4.84% / 방산 -4.25% / 2차전지 -3.66% | 걱정 |
| 7 | 그런데 선물은 매수 | 사흘째 헷지 | 외국인 선물 +1,582계약 / 베이시스 괴리 -5.15pt / 8766 S=-60 | 인사 |

## 업로드 문구안
- 제목: 5,000선이 무너졌는데 외국인은 선물을 샀습니다 (11/17 코스피 마감)
- 설명 첫 줄: 코스피 4,968.48(-2.59%), 거래대금 14조. 외국인은 사흘째 현물을 팔고 선물은 샀습니다.
- 고지: 본 영상은 투자 권유가 아닌 시장 기록 및 정보 정리입니다.

## 고지
전 씬 하단 고정: "본 영상은 투자 권유가 아닌 시장 기록 및 정보 정리입니다."

## 출처
`content/2026-11-17/01_market_daily_insight.md` (한국거래소 집계 오후 3시 35분, 8766 KIS 누적, 18901 감마)
자매 저장소의 수급 심화 편: `kst104/stock-future` `content/2026-11-17/04_shorts_foreign_flow/`
