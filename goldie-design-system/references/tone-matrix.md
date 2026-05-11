# Goldie Tone Matrix — 콘텐츠 유형 → 톤 lookup

> **출처**: Anthropic frontend-design SKILL의 "의도적 미적 방향성 + 완전 커밋" 원칙을 흡수.
> **목적**: 메모리에 분산된 톤 규칙을 1개 lookup 표로 통합. 디자인 작업 *시작 전* 톤을 먼저 결정 → 사고/혼선 차단.
> **위치**: `~/.claude/skills/goldie-design-system/references/tone-matrix.md`
> **호출자**: `goldie-screen-builder` Phase 0, `goldie-marketer`(콘텐츠), `create-feed` 스킬, 위클리/시세/FAQ/광고 디자인 일체.

---

## 0. 사용 방법 (3 step)

1. **콘텐츠 유형 식별** — 이 작업은 어느 카테고리인가? (위클리, 시즌, FAQ, 일반 시세, 광고, 앱 화면)
2. **표에서 lookup** — 해당 행의 톤 슬롯(Mood / Cover / Card / Accent / Typography) 그대로 적용.
3. **금지 항목 확인** — 모든 톤 공통 금지 색 4종(아래 §5) 자동 적용.

이 3 step 안 지키면 위클리 시그니처 다크가 어버이날에 새거나, FAQ에 럭셔리 톤이 섞이는 사고 발생.

---

## 1. 톤 매트릭스 (콘텐츠 유형 × 슬롯)

| 콘텐츠 유형 | Mood | Cover | Card BG | Accent | 비고 |
|------------|------|-------|---------|--------|------|
| **위클리 - 하락 주간** | 시그니처 다크 / 경보 | `1985:2066` (다크 #383838, 1080×1440) / `1989:2280` 스토리 | `#FFFFFF` Featured + `#FEFAEE` 외곽 | `#FFBE00` 골드 + `#F53B32` 빨강(상승) / `#2563EB` 파랑(하락) | 다크 커버 **유일 허용 케이스** |
| **위클리 - 상승 주간** | 골드 시그니처 | `846:838` 골드 #FCD564 커버 | `#FFFFFF` Featured + `#FEFAEE` 외곽 | `#FFBE00` + `#F53B32`(상승) | 다크 커버 금지 |
| **시즌 (어버이날·어린이날·스승의날·발렌타인 등)** | 따뜻 / 가족 | `846:838` 골드 커버 (`#FCD564`) | `#FFFFFF` Featured + `#FEFAEE` 외곽 | `#FFBE00`, `#8A6A00`(다크 골드) | 다크 커버 절대 금지 |
| **FAQ / 가이드 / 체크리스트** | 안내 / 신뢰 | `640:788` faq-cover (크림 톤) | `#FFFFFF` 카드 + `#FEFAEE` 외곽 | `#FFBE00` | step-card `[C] Featured` 표준 적용 (1080×1440) |
| **일간/월간 시세 카드뉴스** | 정보 / 데이터 | `846:838` 골드 커버 | `#FFFFFF` 카드 + `#FEFAEE` 외곽 | `#FFBE00` + 상승/하락색 | tabular-nums 필수 |
| **광고 소재 (메타/네이버)** | 럭셔리 / 신뢰 | (별도 광고 템플릿) | `#FFFFFF` + 골드 그라데이션 | `#FFD664` 골드 + `#1A1A1A` 다크 포인트 | CTA만 다크 허용 |
| **앱 화면 - 일반** | 깨끗 / 모던 | — | `#FFFFFF` | `#FFD664` Primary | shadow-card + radius 16, 회색 bg 금지 |
| **앱 화면 - 강조 (히어로 / 안내 배너 / 견적)** | 포인트 강조 | — | `--gd-cream-100` (#FFFAEB) / `--gd-cream-200` (#FFF7D8) | `#FFD664` | 크림은 *포인트만*, 전체 깔지 말 것 |
| **앱 화면 - AI 배너 / Apple 로그인 / 활성 필터** | 다크 포인트 | — | `--gd-ink-900` (#1A1A1A) | `#FFD664` 골드 텍스트 | #000 절대 금지 |

---

## 2. 의도 명시 (Anthropic SKILL 차용)

각 톤은 **왜 존재하는가**가 명시되어야 함. 디자인 작업 시작 시 1줄 의도 선언:

- 다크 커버 = "이 주는 하락 주간이라 사용자가 즉시 알아채야 한다"
- 골드 커버 = "신뢰·고급감 + 브랜드 시그니처"
- 크림 톤 = "정보 안내 + 부드러움 (FAQ·가이드)"
- 다크 포인트 = "CTA·강조 (AI/로그인)"

의도 선언 없이 톤을 임의로 섞지 말 것. **절충 회피, 완전 커밋.**

---

## 3. 톤 결정 자동 체크 (screen-builder Phase 0)

`goldie-screen-builder`가 작업 시작 전 자동으로 묻고 답하는 3개 질문:

```
Q1. 이 콘텐츠는 위클리 보고서인가? (Yes → Q1-a / No → Q2)
  Q1-a. 하락 주간인가? (Yes → 다크 커버 `1985:2066` / No → 골드 커버 `846:838`)
Q2. 시즌·FAQ·시세 카드뉴스 중 어디인가? → 표에서 lookup
Q3. 앱 화면인가? → Mood 슬롯 (일반/강조/다크 포인트) 중 선택
```

3개 질문 답 + 표 lookup 결과를 작업 시작 보고에 명시:

```
[톤 결정]
- 콘텐츠 유형: 위클리 (상승 주간)
- Cover: 846:838 골드
- Card BG: #FFFFFF
- Accent: #FFBE00 + #F53B32 (상승색)
- 의도: "이번 주는 상승 → 브랜드 시그니처 골드로 긍정 신호"
```

이 보고 없이 디자인 진행 시 PM(우난경) 컨펌 받기 전 *재정정 비용 발생*.

---

## 4. 폰트·간격 표준 (모든 톤 공통)

- 한글: **Pretendard Variable** (CDN: jsdelivr orioncactus)
- 영문/숫자: **Montserrat** (Footer Label, Featured Num)
- step-card 1080×1440: Pill Bold 34px / Title ExtraBold 68px / Subtitle Medium 44px / Featured Num ExtraBold 36px / Featured Title ExtraBold 52px / Featured Desc Regular 40px
- 간격: **4 배수만** 사용 (spacing token 외 값 금지)
- 숫자: `font-variant-numeric: tabular-nums` 필수

---

## 5. 절대 금지 색 (모든 톤 공통)

| 금지 | 대체 | 출처 |
|------|------|------|
| `#000000`/`#000` 순수 검정 (배경) | `#1A1A1A` (`--gd-ink-900`) | `feedback_no-pure-black.md` |
| `#000000`/`#000` 순수 검정 (텍스트) | `#222222` (`--gd-ink-800`) | 동상 |
| `#F5F5F5`/`#F0F0F0`/`#EEE`/`#DDD` 무채색 회색 bg | `#FFFFFF` + shadow-card / `--gd-line` (#F5EFDF) | `feedback_no-gray-bg.md` |
| 카드 border 1px #EEE | shadow-card + radius 16 (border 제거) | 동상 |
| 다크 커버 (위클리 하락 외) | 골드 `846:838` 또는 크림 faq-cover `640:788` | `feedback_dark-cover-weekly-only.md` |

**유지 OK**: `#999999` placeholder, `#666666` 보조 텍스트, 플랫폼 브랜드색(#FEE500 카카오, #03C75A 네이버, #FFD664 골드).

---

## 6. 원본 메모리 (단일 진실 출처 — 본 매트릭스가 인용)

이 파일은 **인덱스 + lookup** 역할. 상세 룰은 아래 메모리가 원본:

- `~/.claude/projects/-Users-goldie-growth/memory/feedback_dark-cover-weekly-only.md` — 다크 커버 시그니처
- `~/.claude/projects/-Users-goldie-growth/memory/feedback_no-pure-black.md` — #000 배제
- `~/.claude/projects/-Users-goldie-growth/memory/feedback_no-gray-bg.md` — 회색 bg 배제 + 카드 스타일
- `~/.claude/projects/-Users-goldie-growth/memory/reference_step-card-design.md` — step-card 1080×1440 표준 [C] Featured
- `~/.claude/projects/-Users-goldie-growth/memory/reference_figma-templates.md` — Cover/Card/Closing 템플릿

룰 충돌 시 **원본 메모리 우선**, 본 매트릭스가 미반영이면 갱신 필요.

---

## 7. 위반 시 처리

- 다크 커버를 시즌 콘텐츠에 사용 → 즉시 `delete_node` + 골드 커버로 교체
- #000 사용 → `#1A1A1A`/`#222222`로 일괄 치환
- 회색 bg 사용 → `#FFFFFF` + shadow-card로 교체
- 톤 결정 보고 누락 → 작업 중단 + Phase 0 재실행

위반 1회 = 우난경 PM에 즉시 보고 + 본 매트릭스 갱신.
