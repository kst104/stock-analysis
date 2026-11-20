# SHORTS DELIVERY — 11/20 장마감 시황 (5회차 · 시장 마감 편 · 올.주.선.이 3단 레이아웃)

## 산출물
| 항목 | 경로 |
| --- | --- |
| 유튜브 쇼츠 MP4 | `downloads/Stock1_1120_장마감_시황_칠판드로잉_쇼츠.mp4` (저장소 사본 `content/2026-11-20/03_shorts_market/stock_chalkboard/chalkboard_shorts_video.mp4`) |
| 움직이는 미리보기 GIF | `downloads/Stock1_1120_미리보기.gif` (사본 `preview/moving_preview.gif`) |
| 씬 캡처 3장 | `downloads/Stock1_1120_scene_1~3.png` (사본 `preview/scene{1,2,3}_preview.png`) |
| 대본 | `content/2026-11-20/03_shorts_market/stock_chalkboard/shorts_script.md` |
| 생성 스크립트 | `scripts/generate_stock_1120_market_shorts.py` + `engine/stock_jaljab_engine.py` |
| 칠판 드로잉 원본 6장 | `assets/chalkboard/stock1120/v1_scene1~6_*.png` |
| 검증 리포트 | `content/2026-11-20/03_shorts_market/stock_chalkboard/render_report.json` |

## 규격 (ffmpeg 검증)
- 1080x1920 (세로 9:16), H.264, 25.00 fps, 66.08초, 4.48MB
- 오디오 AAC 44.1kHz, Edge-TTS `ko-KR-InJoonNeural` (+5%)
- 상단 0~540px 흰 배경: `올바른 주식·선물 이해하기` + 네이비(#1E3A8A) 박스 `올.주.선.이 · <주제>`
- 중단 540~1400px: 칠판 아트 1080x860, 하단 중앙 한 줄 자막(흰 글씨·검정 외곽선)
- 하단 1400~1920px 흰 배경: y=1422 `올.주.선.이 · 투자 참고용 정보 정리`
- 시작 0.0~2.0초 `구독·알림·좋아요는 힘이 됩니다` 배지(2초 직전 0.45초 페이드 아웃)

## 구성 (6씬 · 66초)
| 씬 | 주제 | 자막 |
| --- | --- | --- |
| 1 | 코스피 -5.21% | 코스피 4,869.96 · 5.21% 급락 |
| 2 | 개장부터 -4% | 시가 4,928.51 · 장중 4,831.69 |
| 3 | 매도 사이드카 | 오전 11시 54분 · 오후 1시 28분 |
| 4 | 외국인 1조1,420억 매도 | 개인 1조5,955억이 받아냈다 |
| 5 | 반도체 급락 | 삼성전자 -7.01% · SK하이닉스 -5.92% |
| 6 | 감마 플립 764.55 | 종가 755.34 · 플립 아래 1.20% |

## 업로드 문구안
- 제목: 코스피 -5.21% (11/20 마감), 4,869.96
- 설명 첫 줄: 코스피 4,869.96(-5.21%). 개장부터 4% 빠지고 장중 4,831.69까지 밀렸습니다. 외국인 1조1,420억 매도, 개인 1조5,955억 매수.
- 고지: 본 영상은 투자 권유가 아닌 시장 기록 및 정보 정리입니다.

## 출처
`content/2026-11-20/01_market_daily_insight.md` (한국거래소 마감 집계, 8766 KIS, 18901 감마)
자매 저장소의 수급 심화 편: `kst104/stock-future` `content/2026-11-20/04_shorts_foreign_flow/`
