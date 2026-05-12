---
name: create-feed
description: >
  금골디 인스타그램 카드뉴스 피드를 자동 생성한다.
  주제만 입력하면 리서치 → 디자인 → 캡션까지 한번에 완성.
  트리거: 인스타 피드, 카드뉴스, 피드 만들어, create-feed,
  인스타그램 콘텐츠, 금시세 뉴스, FAQ 콘텐츠, 위클리 리포트.
---

# Create Feed — 금골디 인스타그램 카드뉴스 자동 생성

## 🚨 Step 0 — 콘텐츠 유형 분류 (모든 피드 작업의 최우선 선행)

> **회고 (2026-05-12 우난경 지시):** 직전 위클리 작업의 관성으로 인사이트 콘텐츠를 위클리 wn 표준에 강제로 끼워 맞춘 사례 발생. **다시는 콘텐츠 유형 분류를 건너뛰지 말 것.**

### 분류 1줄 명시 → 매핑 표 확인 → 템플릿 선택 (강제 순서)

피드 작업 시작 시 가장 먼저 콘텐츠 유형을 1줄로 명시한 뒤, 아래 표에서 표준을 확정한다. **유형 분류를 명시하지 않은 채 클론 시작 금지.**

### 🎯 콘텐츠 유형별 표준 포맷 매핑 (2026-05-12 확정)

| 콘텐츠 유형 | 발행 주기 | 표준 SECTION/Frame | 슬라이드 수 | 푸터 라벨 | 비고 |
|------------|----------|-------------------|------------|----------|------|
| **위클리** (지난 주 시세 보고) | **매주 월요일** | `1988:2249` (Featured) | **5장** (wn-01~05) | `WEEKLY NEWS` | 커버/그래프/분석/전망/다음주. 상승=화이트, 하락=다크. |
| **인사이트** (주제 해설·트렌드·정책) | 비정기 | `2000:2443` (GIFT GUIDE) | **3장** (gg01·gg02·gg03) | `INSIGHT` | 커버 + Featured 3카드 + Featured 2카드+골드 메시지 |
| **FAQ** (Q&A 가이드) | 비정기 | `640:788`+`640:789~` (faq) | **3~5장** | `FAQ` | Step 3카드 구조 |
| **금시세 뉴스** (당일/단발) | 비정기 | wn-02 + wn-03 (변형) | 2~3장 | `NEWS` | 시세 카드 + 분석 |
| **카드뉴스 (HOW TO)** | 비정기 | faq-03/05 | 3~5장 | `GUIDE` | 단계별 설명 |
| **비교형** | 비정기 | wn-02 (비교 카드) | 2~3장 | `COMPARE` | 좌우 비교 |
| **참여형** (퀴즈/투표) | 비정기 | wn-03 변형 | 2장 | `QUIZ` | 참여 유도 |

### Step 0 체크리스트 (작업 시작 시 강제 발화)
1. **유형 1줄 선언:** "이 콘텐츠는 [위클리 / 인사이트 / FAQ / 금시세 뉴스 / 카드뉴스 / 비교형 / 참여형] 유형이다."
2. **표준 SECTION/Frame ID 확정** (위 표 매핑)
3. **슬라이드 수 확정**
4. **푸터 라벨 결정**
5. 위 4개를 명시한 뒤에만 클론 시작

### 관성 방지 룰
- 직전 작업 표준을 다음 작업에 재사용하기 전 *반드시* 유형 분류 재확인
- "이전과 같은 표준 쓰면 되겠지" 같은 가정 금지
- 사용자가 카테고리를 명시(`/금테크/인사이트`)하면 그 유형 라벨에 반드시 매칭

### 위반 사례 (2026-05-12, 회고용)
- 인사이트 콘텐츠 "중앙은행이 금을 755톤 산 이유"를 위클리 wn 표준(시세 보고용 5장)에 강제로 적용 → wn-04 "다음 주가 더 중요해요" 슬롯에 인사이트 카피를 덮어쓰며 구조 미스매치 → 사용자 지적 후 GIFT GUIDE 3장으로 재작업
- 원인: 직전 위클리 작업의 관성 + `create-feed` 스킬의 매핑 표 미참조
- 재발 방지: Step 0 분류 1줄을 모든 피드 작업에 강제

---

## 워크플로우

사용자가 주제를 입력하면 Step 0(유형 분류)을 *반드시 먼저* 수행하고, 그 다음 아래 단계를 **병렬 실행**한다.

### Step 1: 데이터 수집 (병렬)
- **goldie-researcher 에이전트** 실행: 주제 관련 시장 데이터 교차검증
  - 공신력 있는 출처 2개 이상 교차검증 필수
  - 최근 한 달 이내 자료만 사용
  - 구체적 수치 + 출처 명시
- **Manus AI 리서치** (필요 시): https://manus.im/ 에서 심층 서칭
- **인스타그램 SEO** 확인: 키워드 선정, 해시태그 5개

### Step 1.5: 데이터 검증 (위클리/시세 콘텐츠 필수)
리서처 결과를 피그마에 반영하기 **전에** 반드시 아래를 검증한다:
- **국내 금 시세**: 한국표준금거래소 기준, 매도가(살 때)/매입가(팔 때) 구분 확인
- **국제 금 시세**: XAU/USD spot 뉴욕 마감가, 일별 데이터 확인
- **원/달러 환율**: 서울외환시장 종가 기준, 실시간 확인
- **등락률**: 계산식 포함, 매입/매도 기준 혼용 금지
- **미확인 데이터는 "미확인"으로 표기** — 추정치로 콘텐츠 제작 금지
- 검증 후 수치 불일치 시 피그마+캡션 모두 수정

### Step 2: 디자인 생성 (Figma MCP)
- Figma 파일: `GOLDIE_운영콘텐츠 디자인` (AnD7rIOMfUYblzfyc7cA8l)
- 페이지: "인스타그램 콘텐츠"
- 콘텐츠 유형별 wn/faq 템플릿 혼합 사용

### Step 3: 캡션 생성
- **goldie-marketer 에이전트** 실행: 캡션 + Alt text

### Step 4: 한글 검수 (필수, 발행 전 마지막 게이트)

> 피그마 텍스트 입력 직후 **반드시** 수행. 누락 시 발행 금지.

**4-A. 자동 스캔**
- 모든 슬라이드에 `scan_text_nodes` 실행 → 전체 텍스트 한 번에 출력
- 카피본을 줄 단위로 정렬하여 검토 가능한 형태로 추출

**4-B. 한글 맞춤법 4대 체크리스트**
1. **오탈자**: 한글 자소 위치 오류 (섮이면→섞이면, 갂인→각인, 잴주세요→재 주세요)
2. **띄어쓰기**: 보조용언, 의존명사, 합성어 검수 (재 주세요/확인해 보세요)
3. **동사 자연스러움**: 한자어+하다 조합 부자연 검출 (견적해요→감정해요/견적을 내요)
4. **의미불명 단어**: 컨텍스트 부적합 단어 (명세 매장→근처 매장)

**4-C. 검수 도구 활용**
- `design:ux-writing` 스킬 호출 가능: UX 카피 톤·정확성 검수
- `goldie-marketer` 에이전트 재검수 요청 가능: 브랜드 보이스 + 한글 어색함 동시 확인
- 외부 검수 시 [네이버 맞춤법 검사기](https://search.naver.com/search.naver?query=맞춤법+검사기) 또는 부산대 맞춤법 검사기 활용

**4-D. 발행 전 최종 셀프체크**
- [ ] 슬라이드별 전체 텍스트를 처음부터 끝까지 한 번 더 음독
- [ ] 1돈=3.75g 같은 핵심 수치 재확인
- [ ] 서비스명 "금골디" 표기 통일 ("골디" 단독 금지)
- [ ] 캐럿 표기 통일 ("카라트" 금지)
- [ ] 느낌표 남발/공포/과장 표현 없음

> ⚠️ 사용자 피드백으로 오탈자 발견 시 → 해당 케이스를 4-B 체크리스트에 추가하여 재발 방지.

---

## Figma 소스 템플릿 (클론 전용)

| 템플릿 | Figma ID | 사이즈 | 위치 | 용도 |
|--------|----------|--------|------|------|
| wn-00 (커버 상승) | 444:911 | 520x675→1080x1440 | 위클리(601:6894) | 주간 상승 시 |
| wn-00 (커버 하락) | 444:1057 | 520x675→1080x1440 | 위클리(601:6894) | 주간 하락 시 (다크 #383838) |
| wn-01 (그래프) | 590:4094 | 520x675→1080x1440 | 위클리(601:6894) | 주간 시세 차트 |
| wn-02~04 (카드) | 590:4151~4265 | 520x675→1080x1440 | 위클리(601:6894) | 데이터/뉴스 카드 |
| wn-05 (전문가) | 591:4547 | 520x675→1080x1440 | 위클리(601:6894) | 기관 전망 (다크 #383632) |
| wn-06 (다음주) | 590:4321 | 520x675→1080x1440 | 위클리(601:6894) | 다음 주 관전포인트 |
| wn-07 (클로징) | 590:4377 | 520x675→1080x1440 | 위클리(601:6894) | 클로징 |
| Cover (골드) | 846:838 | 1080x1440 | 페이지 루트 | faq/일반 커버 |
| close | 869:5288 | 1080x1440 | 페이지 루트 | 일반 클로징 |
| faq-cover | 640:788 | 1080x1440 | faq-피드발행완료 | FAQ 커버 |
| faq-02~06 | 640:789~870 | 1080x1440 | faq-피드발행완료 | FAQ 본문 |
| **위클리 Featured 세트** | **1988:2249** | 1080x1440 × 5장 | — | **위클리 표준 (시세 보고용)** — wn-01~05 |
| **인사이트 GIFT GUIDE 세트** | **2000:2443** (`260506`) | 1080x1440 × 3장 | — | **인사이트 표준** — gg01 커버 + gg02 본문1 + gg03 본문2+골드 메시지 |
| gg01 (인사이트 커버) | 1997:2418 / 2001:2504 | 1080x1440 | 2000:2443 안 | Inner Gold + Title Line 1·2-3 + 골드바 이미지 |
| gg02 (인사이트 본문 1) | 1997:2360 / 2001:2475 | 1080x1440 | 2000:2443 안 | Pill + Title + Subtitle + Featured 3카드 |
| gg03 (인사이트 본문 2) | 1997:2389 / 2001:2446 | 1080x1440 | 2000:2443 안 | Pill + Title + Subtitle + Featured 2카드 + 골드 메시지 카드 |

### 520→1080 스케일 규칙
- 클론 후 반드시 1080x1440으로 resize (비율 2.077x)
- 코너 래디어스: 40→**80**, 18→**37**, 30→**62**
- 폰트: 32→**66**, 22→**46**, 18→**38**, 15→**31**, 40→**83**, 16→**33**
- Footer: POST3_cover(846:838) 기준 — 1080x226, 텍스트 x=125, 로고 x=875, 80x80

### 세트 구성

**위클리 (시세 보고, 매주 월요일):** 1988:2249 (Featured 5장) — wn-01 커버 → wn-02 그래프 → wn-03 분석 → wn-04 전망 → wn-05 다음주
**인사이트 (주제 해설):** 2000:2443 (GIFT GUIDE 3장) — gg01 커버 → gg02 본문1 (Featured 3카드) → gg03 본문2 (Featured 2카드 + 골드 메시지)
**FAQ (Q&A 가이드):** faq-cover (640:788) → faq-02~05 (Step 3카드 구조)
**피드형 (기타):** Cover → Content(wn/faq 혼합) ×2~4

> **클로징은 자동 생성하지 않는다.** 디자이너가 직접 추가.

### 위클리 커버 분기
- **주간 상승:** wn-00 상승 (444:911) — 흰 배경 #FFFFFF
- **주간 하락:** wn-00 하락 (444:1057) — 다크 배경 #383838, 빨간 글로우

### 전문가 전망 프레임 (wn-05)
- 기관 전망/전문가 의견이 포함될 때 반드시 사용
- 다크 배경 #383632, innerframe radius 80, clip content ON
```
center-contents (1080x850, padding 10/10/40/40, gap 30)
├─ drop-shadow(0 2 10 rgba(174,128,0,0.1))
├─ primaryAxis: CENTER, counterAxis: CENTER
└─ Frame 1261157392 (fill width, gap 20)
   ├─ cards row (fill width, HORIZONTAL CENTER, gap 20)
   │  ├─ card (flex-grow 1, rgba(255,255,255,0.1), radius 37)
   │  │  ├─ padding: 26/26/24/24, gap 30
   │  │  ├─ primaryAxis: CENTER, counterAxis: CENTER
   │  │  ├─ 은행명 (Pretendard Variable Bold 46px, #FFFFFF, line-height 100%)
   │  │  ├─ divider (fill width, 1px #FFFFFF op 0.2)
   │  │  └─ price area (fill width, VERTICAL CENTER, gap 20)
   │  │     ├─ 가격 (Montserrat ExtraBold 83px, gradient #FFBE00→#FEFAEE, line-height 100%)
   │  │     └─ 라벨 (Pretendard Variable Regular 31px, #FFFFFF op 0.8, line-height 100%)
   │  └─ card (동일 구조)
   └─ cards row (동일 구조)
```

### 콘텐츠 유형별 매핑 (Step 0 분류 결과를 여기서 재확인)

| 유형 | 표준 SECTION/Frame | Pill 카테고리 | 슬라이드 수 |
|------|-------------------|-------------|------------|
| **위클리** (지난 주 시세 보고) | **1988:2249** (wn 5장) | 시세, 분석, 전망 | 5장 |
| **인사이트** (주제 해설) | **2000:2443** (gg 3장) | 이유, 추이·국가, 인사이트 | 3장 |
| **FAQ** (Q&A) | 640:788 + 640:789~ | 체크 1·2·3 / 4·5 | 3~5장 |
| 금시세 뉴스 (단발) | wn-02 + wn-03 변형 | 시세, 분석 | 2~3장 |
| 카드뉴스 (HOW TO) | faq-03/05 | STEP, HOW TO | 3~5장 |
| 기능 소개 | wn-03 변형 | 기능소개 | 2장 |
| 비교형 | wn-02 변형 | 비교 | 2~3장 |
| 리뷰/전망 | wn-03 + wn-02 | 리뷰, 전망 | 2~3장 |
| 참여형 | wn-03 변형 | 투표, 퀴즈 | 2장 |

---

## 프레임 구조 — 필수 준수

### 커버 프레임 구조 (faq-cover / wn-cover / Cover(골드))

> **Inner Gold Frame은 커버의 핵심 요소. 절대 빠뜨리지 말 것.**

```
최상위 프레임 (1080x1440, #FFFFFF)
└─ Inner Gold Frame (1080x1440, #FCD564, radius 80) ← 필수!
   ├─ Glow Circle (861x861, #FFBB1C, opacity 0.6)
   ├─ Title Group (850x~264, CENTER)
   │  ├─ Title Line 1 (Pretendard Variable Regular 90px, #424242)
   │  └─ Title Line 2-3 (Pretendard Variable ExtraBold 100px, #424242)
   ├─ Footer (1080x226)
   │  └─ Footer Text Group ("FAQ | 금골디" 또는 "Weekly | 금골디")
   └─ 이미지 (하단 제품 이미지)
```

**커버 생성 시 반드시 clone_node 사용** — 직접 빌드 시 Inner Gold Frame 누락 위험.

### 커버 이미지 제안 (산출물에 포함)
- 피드 생성 시 커버에 어울리는 이미지를 **한 줄 텍스트**로 제안
- 주제·톤에 맞는 구체적 이미지 키워드 (예: "금반지 클로즈업, 따뜻한 조명", "골드바 스택, 미니멀 배경")
- 디자이너가 바로 소싱할 수 있는 수준으로 작성

### 콘텐츠 프레임 구조 (커버/클로징 제외)

```
최상위 프레임 (1080x1440, #FFFFFF)
├─ Inner Frame (1080x1440, #FEFAEE, radius 80)
│  ├─ dim (하단 골드 그라디언트, 1080x680) ← z-index 0
│  ├─ Title Section (1080x408, fill none, y=0) ← z-index front
│  │  ├─ Pill Badge (#FCD15A, radius 50, auto layout HORIZONTAL, CENTER/CENTER, padding 20/20/40/40)
│  │  │  └─ 카테고리 (Pretendard Variable ExtraBold 36px, #424242)
│  │  ├─ Title (Pretendard Variable ExtraBold 64px, CENTER, #424242, width 840)
│  │  ├─ Tag (Pretendard Variable Medium 46px, CENTER, #424242, width 840)
│  │  └─ Subtitle (Pretendard Variable Regular 44px, #333333, width 920) ← wn 템플릿
│  ├─ Steps Section (1080x918, y=382, VERTICAL CENTER, padding 90/80, gap 20)
│  │  │  shadow: drop-shadow(0 2 10 rgba(174,128,0,0.1))
│  │  ├─ Row (920x378, HORIZONTAL, gap 20)
│  │  │  ├─ Step Card (450x378, #FFFFFF, radius 36, padding 50/40, gap 24, VERTICAL CENTER)
│  │  │  │  ├─ Badge (68x68, #DB6E00, radius 34, VERTICAL CENTER)
│  │  │  │  │  └─ 번호 (Pretendard Bold 38px, #FFFFFF)
│  │  │  │  ├─ Step Title (Pretendard Bold 40px, #222222, CENTER)
│  │  │  │  └─ Step Desc (Pretendard Regular 32px, #333333, CENTER)
│  │  │  └─ Step Card (동일 구조)
│  │  └─ Step Card (920x340, full width, 동일 내부 구조)
│  │
│  │  **비교형 카드 컨테이너** (Frame 1261157364):
│  │  - VERTICAL CENTER, padding **120**/120/20/20, gap **30**
│  │  - W 1080, drop-shadow(0 2 10 rgba(174,128,0,0.1))
│  │  ├─ Card Row (1000x460, HORIZONTAL, gap 20)
│  │  │  ├─ Card (480x420, bg rgba(255,255,255,0.72), radius **37**, padding **80**/80/24/24, gap 20, VERTICAL SPACE_BETWEEN)
│  │  │  │  ├─ Label (Pretendard Variable Bold 46px, #222222, CENTER)
│  │  │  │  ├─ Divider (fill width, 1px solid #575757, opacity 0.2)
│  │  │  │  └─ Value Area (fill width, VERTICAL CENTER, gap 6)
│  │  │  │     ├─ Value (Montserrat ExtraBold 83px, #DF0000, CENTER)
│  │  │  │     └─ Desc (Pretendard Variable Regular 31px, #222222, opacity 0.5, CENTER)
│  │  │  └─ Card (동일 구조)
│  │  └─ Bottom Text (Pretendard Variable Medium 33px, #424242, opacity 0.5)
│  └─ CTA Bar (1078x136, #FFBE00, y=1304) ← 마지막 카드에만!
└─ **Footer (1080x128, y=1312, fill 없음)** ← 최상위 프레임 직속! Inner Frame 밖!
```

> **Footer 배치 절대 규칙:**
> - Footer는 반드시 **최상위 프레임의 직속 자식**으로 배치 (Inner Frame 안에 넣지 않는다)
> - Inner Frame의 auto layout/clip content에 의해 잘리는 것을 방지하기 위함
> - fill: **없음** (투명), W: **1080**, H: **128**, absolute y=**1312**
> - 모든 콘텐츠 프레임에 **반드시** Footer를 생성한다 (생략 금지)

### Title Section 생성 (Frame 1261157357)
- auto layout: VERTICAL, CENTER/CENTER, padding **112**/40/120/120, gap 20
- **상단 패딩 112px, 좌우 120px, 하단 40px**
- **Title Text Group (Frame 1261157363):** VERTICAL, CENTER, gap **20** (10px 금지)
- **위클리 헤더 타이틀: 80px** (1080x1440 프레임 전체 통일, 66px 금지)
- **point/뱃지 내 텍스트: Pretendard Variable Medium 48px** (1080 기준, 38px/Bold 금지)
- **point 박스: W, H 모두 Hug** (auto layout HORIZONTAL, CENTER/CENTER)
- Pill Badge: auto layout HORIZONTAL, CENTER/CENTER, padding 20/20/40/40
- **폰트 생성 후 반드시 `set_font_name`** — 기본 Inter 방지

### 콘텐츠 컨테이너 좌우 패딩 규칙
- **모든 콘텐츠 컨테이너 좌우 패딩: 40px**
- 그래프 컨테이너 (Frame 1261157381): paddingLeft 40, paddingRight 40
- 전문가 카드 컨테이너 (Frame 1261157364 / center-contents): paddingLeft 40, paddingRight 40

### Step 1·Step 2 카드 높이 = "H fill" (Fill container, vertical stretch) — 필수
- Row 컨테이너 안의 Step 1·Step 2 카드는 **항상 height = Fill container** (Figma `layoutSizingVertical = STRETCH`, CSS `align-self: stretch`)
- 이유: Row 높이가 변해도 두 카드가 같은 높이로 늘어나도록 보장. 텍스트 길이 차이로 카드 높이 어긋남 방지.
- Row container: `display: flex; flex-direction: row; align-items: stretch; gap: 20; width: 920; height: 378` (height는 콘텐츠 따라 변할 수 있음)
- Step 1·2 card: `align-self: stretch; flex: none; padding: 50/40; gap: 24; width: 450; background: #FFFFFF; radius: 36`
- Step 3 card (full-width 단일): `width: 920; padding: 50/40; gap: 20; background: #FFFFFF; radius: 36`
- 적용 방법: Figma에서 카드 선택 → 우측 패널 Auto layout → Resizing → height **Fill container** 선택

### 커버 Footer (wn-00 전용)
커버 프레임에만 적용되는 별도 Footer. 일반 콘텐츠 Footer와 다름.
```
Footer (1080x226, position absolute, y=1214)
├─ auto layout: HORIZONTAL, SPACE_BETWEEN, CENTER
├─ padding: 62px 125px 83px
├─ border-top: 1px solid rgba(255,255,255,0.15)
├─ Footer Text Group (442x36, gap 28)
│  ├─ "WEEKLY NEWS" (Montserrat SemiBold 36px, #FFFFFF)
│  ├─ Divider (2x34, rgba(255,255,255,0.2))
│  └─ "금골디" (Montserrat Regular 36px, #FFFFFF)
└─ Logo Emblem (80x80)
   └─ emblem vectors: 골드 (#FCD564, #EEB825)
```
- 다크 커버(하락)에서도 동일 (텍스트 #FFFFFF, 로고 골드)

### 표준 Footer (1080x1440 프레임 공통) — 필수 생성
모든 1080x1440 콘텐츠 프레임에 **반드시** 동일하게 적용한다.
**배치:** 최상위 프레임 직속 자식 (Inner Frame 밖), fill 없음, absolute.
```
Footer (1080x128, position absolute, y=1312)
├─ auto layout: HORIZONTAL, SPACE_BETWEEN, CENTER
├─ padding: 30px 80px 40px
├─ Footer Text Group (442x36, opacity 0.2, gap 28)
│  ├─ "WEEKLY NEWS" (Montserrat SemiBold 36px, #424242)
│  ├─ Divider (2x34, rgba(66,66,66,0.2))
│  └─ "금골디" (Montserrat Regular 36px, #424242)
└─ Logo Emblem (48x48, opacity 0.5)
   └─ emblem vectors: #595446
```
- 다크 배경(wn-00 하락, wn-05 전문가) 프레임에서는 텍스트 #FFFFFF, divider #FFFFFF

### 관전포인트 리스트 (wn-06)
```
Frame 1261157395 (1080x870, bg #FFFFFF)
├─ auto layout: VERTICAL, SPACE_BETWEEN
├─ padding: 70px 0px
├─ 리스트 아이템 (1080x181, padding 36px 0, gap 10, CENTER)
│  ├─ 제목 (Pretendard Variable Bold 46px, #222222, line-height 100%)
│  └─ 설명 (Pretendard Regular 38px, #111111, line-height 140%)
├─ Divider (1080x0, 1px solid #575757, opacity 0.2)
├─ 리스트 아이템 (동일)
├─ Divider
└─ 리스트 아이템 (마지막 — 제목 ExtraBold #DB6E00)
```

### CTA Bar
- **마지막 콘텐츠 프레임에만** 적용
- position: absolute, x=1, y=1304

---

## 인사이트 GIFT GUIDE 3장 표준 (2026-05-12 도입)

> 인사이트 콘텐츠는 위클리 wn 표준이 아닌 **GIFT GUIDE 3장 세트**(`2000:2443`)를 사용한다. 위클리는 시세 보고용 5장이라 인사이트에 맞지 않음.

### 슬라이드 구성 (3장 고정)

**gg01 (커버, 1080x1440 · Inner Gold)**
- 노드 ID: `1997:2418` (또는 `2001:2504`)
- Title Line 1 (Pretendard Variable Regular 120px, #424242) — 1줄 라벨
- Title Line 2-3 (Pretendard Variable ExtraBold 120px, 그라디언트 #424242→#FFBE00) — 2줄 핵심 메시지
- 하단 골드바·선물 이미지 (변경 가능)
- Footer (1080x226): `INSIGHT | 금골디`

**gg02 (본문 1, 1080x1440 · #FEFAEE)**
- 노드 ID: `1997:2360` (또는 `2001:2475`)
- 구조: C_Header(Pill+Title+Subtitle) + Featured 3카드 + C_Footer
- Pill: 카테고리 라벨 (예: `이유 1·2·3`)
- Title (Pretendard Variable ExtraBold 68px, #222222)
- Subtitle (Pretendard Variable Medium 44px, #8A6A00)
- Featured 카드 (3개, #FFFFFF 배경, radius 32, 920×298):
  - C_Featured_Num (Montserrat ExtraBold 36px, #FFBE00) — 01/02/03
  - C_Featured_Title (Pretendard Variable ExtraBold 52px, #222222)
  - C_Featured_Desc (Pretendard Variable Regular 40px, #424242)

**gg03 (본문 2, 1080x1440 · #FEFAEE)**
- 노드 ID: `1997:2389` (또는 `2001:2446`)
- 구조: C_Header + Featured 2카드 + **골드 메시지 카드** (#FCD15A) + C_Footer
- Featured 2카드 (04/05) — gg02와 동일 구조
- 골드 메시지 카드 (마지막, #FCD15A 배경, radius 32):
  - Title (Pretendard Variable ExtraBold 52px, 2줄) — 핵심 메시지 (예: "우리도 흐름을 따라가 봐요")
  - Desc (Pretendard Variable Regular 34px) — 행동 유도 (금골디 자연 노출)
  - 우측 작은 이미지 (선택)

### 인사이트 텍스트 노드 ID 패턴 (gg02·gg03 동일)
원본 1997 base 기준:
- `+3` C_Pill_Text
- `+4` C_Title
- `+5` C_Subtitle
- `+8/+12/+16` C_Featured_Num (01/02/03 또는 04/05)
- `+9/+13/+17` C_Featured_Title
- `+10/+14/+18` C_Featured_Desc
- gg03 마지막 골드 카드: `+17` Title / `+18` Desc
- `+21` C_Footer_Label / `+23` C_Footer_Brand

### 인사이트 Pill·Footer 라벨 권장값
- Pill: `이유 1·2·3` / `추이·국가` / `데이터 1·2·3` 등 (콘텐츠에 맞게)
- Footer Label: `INSIGHT` (또는 `INSIGHT REPORT`)

---

## 기본 프레임 규격 — 1080x1440 통일

> **모든 피드 프레임은 1080x1440을 기본 베이스로 생성한다.**
> 기존 소형 프레임 템플릿(640x, 750x 등)은 사용하지 않는다.
> 클론 후에도 반드시 1080x1440 기준으로 폰트·위치·코너 래디어스를 통일한다.

### 1080 기준 통일 체크리스트
- [ ] 프레임: 1080x1440
- [ ] Inner Frame / Inner Gold Frame: 1080x1440, radius **80**
- [ ] Card: fill parent (960px), radius **60**, stroke 없음
- [ ] Step Card: radius **36** (또는 50)
- [ ] Pill Badge: radius **50**
- [ ] Title: **64px** / Tag: **46px** / Step Title: **45px**
- [ ] Desc: **38px** / Label: **34px**
- [ ] Footer: y=1312, 1080px
- [ ] CTA Bar: y=1304, 1078px

---

## 디자인 절대 규칙

### Fill 규칙
- **fill 금지:** Title Section, Cards Container, Footer, Text Area
- **fill 허용:** 최상위(#FFFFFF), Inner Frame(#FEFAEE), Inner Gold Frame(#FCD564), Card(#FFFFFF), CTA Bar(#FFBE00), Pill Badge(#FCD15A), Badge(#FCD564/#DB6E00)

### Width 규칙
- Title Section, Cards Container, Footer: **1080px**
- Card (비교/데이터형): **fill parent (960px)**, radius **60px**, bg rgba(255,255,255,0.92), padding 50/60, gap 16, stroke 없음
- Card (faq/step형): **fill parent (960px)**, radius 60px, stroke 없음, bg #FFFFFF
- Step Card: radius 36px, stroke 없음

### Desc 색상 규칙
- 비교형 카드 Desc: **#676767** (연한 회색)
- 일반 카드 Desc: #333333 또는 #3741F2 (강조)

### Closing — 자동 생성 안 함
- 클로징은 디자이너가 직접 추가 (자동 클론/빌드 금지)

### Cover Title
- Line 1: Pretendard Variable Regular **90px**, #424242
- Line 2-3: Pretendard Variable ExtraBold **100px**, 그라디언트 #424242→#FFBE00

### Badge
- 정원형 필수 (가로=세로), 생성 후 resize_node 호출
- Template B: 80x80, #FCD564
- Template E: 68x68, #DB6E00

### 색상 규칙
- 본문: #333333 (#111111 금지)
- 서브: #424242
- 하락: #3741F2 / 상승: #FA4444
- #000000 절대 금지

### 행간 규칙
- **모든 텍스트 line-height: 140%** 통일 (AUTO/고정px 금지)

### 폰트 사이즈 규칙 (1080x1440 프레임)
- **Step Desc / Card Desc (설명 텍스트): 38px** (28px/32px 금지 — 모바일에서 너무 작음)
- **Label: Pretendard Bold 34px** (Regular 금지, 28px 금지)
- **Step Title: 45px** (40px 금지)
- Card Title (Value): **44px** (Pretendard Variable Bold, 통일)
- **Tag: 46px** (48px 금지)
- Title: 64px

### 혼합 폰트 텍스트 교체
- `set_text_content` 전에 반드시 `set_font_name`으로 폰트 통일
- 헤드라인: Pretendard Variable ExtraBold
- 본문: Pretendard Regular 38px
- 서브: Pretendard Variable Medium
- Footer: Montserrat SemiBold / Regular

### 프레임 생성 직후 체크
- [ ] **커버: Inner Gold Frame (#FCD564, radius 80) 존재 확인** ← 최우선
- [ ] 콘텐츠: Inner Frame (#FEFAEE, radius 80)
- [ ] Title Section (Pill + Title + Tag)
- [ ] Footer 하단 (y=1312)
- [ ] CTA Bar 마지막 카드에만
- [ ] Badge 정원형
- [ ] 폰트 Pretendard Variable (Inter 아닌지)
- [ ] width 1080
- [ ] 줄바꿈: `\n` 사용 금지 → 실제 엔터로 줄바꿈

---

## 캡션 규칙 (goldie-marketer)

### SEO 최적화
- 첫 125자에 핵심 키워드 ("금시세", "금 1돈", "금골디")
- 해시태그 5개 이내
- 서비스명 "금골디" 캡션 내 2회 이상

### CTA
- 저장: "나중에 꺼내보실 수 있도록 저장해두세요"
- 공유: "금 갖고 계신 분들께 공유해드리면 도움이 될 거예요"

### 카피 작성 원칙
- **한 줄 핵심:** 모든 텍스트는 최대한 짧게, 핵심만 눈에 들어오게
- **Tag:** 반드시 1줄 (2줄 넘어가면 줄이기)
- **Step Desc / Card Desc:** 1~2줄 이내, 정보 나열 금지
- **고객 혜택 중심:** "무엇을 하는지" 대신 "고객이 뭘 얻는지" 강조
- **행동 유도:** 수동적 설명 → 능동적 행동/결과로 전환

### 브랜드 보이스
- 전문적이면서 친근한 톤
- 과장/공포/느낌표 남발 금지
- 출처 기반 수치만 사용

---

## 사용법

```
/create-feed 이번주 금시세 뉴스
/create-feed FAQ - 금 함량별 가격 차이
/create-feed 퀴즈 - 이번주 금 1돈 시세
```

## 산출물

1. **Figma 프레임:** 커버 + 본문 2~4장 (wn+faq 혼합) — 클로징 제외
2. **커버 이미지 제안:** 한 줄 키워드 (디자이너 소싱용)
3. **인스타 캡션:** SEO 최적화
4. **해시태그:** 5개
5. **Alt text:** 장별
6. **저장/공유 CTA:** 2종
