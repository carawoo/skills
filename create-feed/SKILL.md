---
name: create-feed
description: >
  금골디 인스타그램 카드뉴스 피드를 자동 생성한다.
  주제만 입력하면 리서치 → 디자인 → 캡션까지 한번에 완성.
  트리거: 인스타 피드, 카드뉴스, 피드 만들어, create-feed,
  인스타그램 콘텐츠, 금시세 뉴스, FAQ 콘텐츠, 위클리 리포트.
---

# Create Feed — 금골디 인스타그램 카드뉴스 자동 생성

## 워크플로우

사용자가 주제를 입력하면 아래 3단계를 **병렬 실행**한다.

### Step 1: 데이터 수집 (병렬)
- **goldie-researcher 에이전트** 실행: 주제 관련 시장 데이터 교차검증
  - 공신력 있는 출처 2개 이상 교차검증 필수
  - 최근 한 달 이내 자료만 사용
  - 구체적 수치 + 출처 명시
- **Manus AI 리서치** (필요 시): https://manus.im/ 에서 심층 서칭
- **인스타그램 SEO** 확인: 키워드 선정, 해시태그 5개

### Step 2: 디자인 생성 (Figma MCP)
- Figma 파일: `GOLDIE_운영콘텐츠 디자인` (AnD7rIOMfUYblzfyc7cA8l)
- 페이지: "인스타그램 콘텐츠"
- 콘텐츠 유형별 wn/faq 템플릿 혼합 사용

### Step 3: 캡션 생성
- **goldie-marketer 에이전트** 실행: 캡션 + Alt text

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

### 520→1080 스케일 규칙
- 클론 후 반드시 1080x1440으로 resize (비율 2.077x)
- 코너 래디어스: 40→**80**, 18→**37**, 30→**62**
- 폰트: 32→**66**, 22→**46**, 18→**38**, 15→**31**, 40→**83**, 16→**33**
- Footer: POST3_cover(846:838) 기준 — 1080x226, 텍스트 x=125, 로고 x=875, 80x80

### 세트 구성

**위클리:** wn-00(커버) → wn-01(그래프) → wn-02~04(카드 2~3장) → wn-05(전문가전망)
**피드형:** Cover → Content(wn/faq 혼합) x2~4
**FAQ형:** faq-cover → faq-03/04/05 x2~3

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

### 콘텐츠 유형별 매핑

| 유형 | 템플릿 | Pill 카테고리 |
|------|--------|-------------|
| 금시세 뉴스 | wn-02 + wn-03 | 시세, 분석 |
| 카드뉴스 | faq-03/05 | STEP, HOW TO |
| 기능 소개 | wn-03 변형 | 기능소개 |
| 비교형 | wn-02 변형 | 비교 |
| 리뷰/전망 | wn-03 + wn-02 | 리뷰, 전망 |
| 참여형 | wn-03 변형 | 투표 |

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
└─ Inner Frame (1080x1440, #FEFAEE, radius 80)
   ├─ dim (하단 골드 그라디언트, 1080x680) ← z-index 0
   ├─ Title Section (1080x408, fill none, y=0) ← z-index front
   │  ├─ Pill Badge (#FCD15A, radius 50, auto layout HORIZONTAL, CENTER/CENTER, padding 20/20/40/40)
   │  │  └─ 카테고리 (Pretendard Variable ExtraBold 36px, #424242)
   │  ├─ Title (Pretendard Variable ExtraBold 64px, CENTER, #424242, width 840)
   │  ├─ Tag (Pretendard Variable Medium 46px, CENTER, #424242, width 840)
   │  └─ Subtitle (Pretendard Variable Regular 44px, #333333, width 920) ← wn 템플릿
   ├─ Cards Container (1080x~926, y=335, padding 0/60, gap 28, VERTICAL CENTER)
   │  │  shadow: drop-shadow(0 8 20 rgba(237,146,43,0.2))
   │  ├─ Card (fill parent, bg rgba(255,255,255,0.92), radius 60, padding 50/60, gap 16, VERTICAL CENTER, stroke 없음)
   │  │  ├─ Label (Pretendard Bold 34px, #424242)
   │  │  ├─ Value (Pretendard Bold 48px, #333333)
   │  │  └─ Desc (Pretendard Regular 38px, #676767, CENTER)
   │  └─ ... (Card 2, Card 3 동일 구조)
   ├─ Footer (1080x128, y=1312) ← 표준 Footer 참조
   └─ CTA Bar (1078x136, #FFBE00, y=1304) ← 마지막 카드에만!
```

### Title Section 생성 (Frame 1261157357)
- auto layout: VERTICAL, CENTER/CENTER, padding **80**/30/60/60, gap 20
- **상단 패딩 80px** — 1080 기준 통일
- **위클리 헤더 타이틀: 80px** (1080x1440 프레임 전체 통일, 66px 금지)
- **point/뱃지 내 텍스트: Pretendard Variable Medium 48px** (1080 기준, 38px/Bold 금지)
- **point 박스: W, H 모두 Hug** (auto layout HORIZONTAL, CENTER/CENTER)
- Pill Badge: auto layout HORIZONTAL, CENTER/CENTER, padding 20/20/40/40
- **폰트 생성 후 반드시 `set_font_name`** — 기본 Inter 방지

### 콘텐츠 컨테이너 좌우 패딩 규칙
- **모든 콘텐츠 컨테이너 좌우 패딩: 40px**
- 그래프 컨테이너 (Frame 1261157381): paddingLeft 40, paddingRight 40
- 전문가 카드 컨테이너 (Frame 1261157364 / center-contents): paddingLeft 40, paddingRight 40

### 커버 Footer (wn-00 전용)
커버 프레임에만 적용되는 별도 Footer. 일반 콘텐츠 Footer와 다름.
```
Footer (1080x226, position absolute, y=1214)
├─ auto layout: HORIZONTAL, SPACE_BETWEEN, CENTER
├─ padding: 62px 125px 83px
├─ border-top: 1px solid rgba(255,255,255,0.15)
├─ Footer Text Group (442x36, gap 28)
│  ├─ "WEEKLY REPORT" (Montserrat SemiBold 36px, #FFFFFF)
│  ├─ Divider (2x34, rgba(255,255,255,0.2))
│  └─ "금골디" (Montserrat Regular 36px, #FFFFFF)
└─ Logo Emblem (80x80)
   └─ emblem vectors: 골드 (#FCD564, #EEB825)
```
- 다크 커버(하락)에서도 동일 (텍스트 #FFFFFF, 로고 골드)

### 표준 Footer (1080x1440 프레임 공통)
모든 1080x1440 콘텐츠 프레임에 동일하게 적용한다.
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
