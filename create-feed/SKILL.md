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

| 템플릿 | Figma ID | 사이즈 | 위치 |
|--------|----------|--------|------|
| wn-cover | 601:6581 | 1080x1440 | Section 8 |
| wn-02 (데이터) | 601:6692 | 1080x1440 | Section 8 |
| wn-03 (분석) | 601:6693 | 1080x1440 | Section 8 |
| wn-closing | 601:6584 | 1080x1440 | Section 8 |
| faq-cover | 640:788 | 1080x1440 | faq-피드발행완료 |
| faq-02~06 | 640:789~870 | 1080x1440 | faq-피드발행완료 |
| Cover (골드) | 846:838 | 1080x1440 | 페이지 루트 |
| close | 869:5288 | 1080x1440 | 페이지 루트 |

### 세트 구성

**피드형:** Cover → Content(wn/faq 혼합) x2~4 → Closing
**위클리:** wn-cover → wn-02 → wn-03 → wn-closing
**FAQ형:** faq-cover → faq-03/04/05 x2~3 → Closing

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

## 콘텐츠 프레임 구조 (Section 9 패턴) — 필수 준수

모든 콘텐츠 프레임(커버/클로징 제외)은 이 구조를 따른다:

```
최상위 프레임 (1080x1440, #FFFFFF)
└─ Inner Frame (1080x1440, #FEFAEE, radius 80)
   ├─ dim (하단 골드 그라디언트, 1080x680) ← z-index 0
   ├─ Title Section (1080x408, fill none, y=0) ← z-index front
   │  ├─ Pill Badge (#FCD15A, radius 50, auto layout HORIZONTAL, CENTER/CENTER, padding 20/20/40/40)
   │  │  └─ 카테고리 (Pretendard Variable ExtraBold 36px, #424242)
   │  ├─ Title (Pretendard Variable ExtraBold 64px, CENTER, #424242, width 840)
   │  └─ Tag (Pretendard Variable Medium 48px, CENTER, #424242, width 840)
   ├─ Cards Container (1080x~700, y=420)
   ├─ Footer (1080x128, fill none, y=1312)
   │  ├─ "Weekly" (Montserrat SemiBold 36px, #424242, opacity 0.2)
   │  ├─ Divider (2x34, #424242, opacity 0.2)
   │  └─ "금골디" (Montserrat Regular 36px, #424242, opacity 0.2)
   └─ CTA Bar (1078x136, #FFBE00, y=1304) ← 클로징 직전 프레임에만!
```

### Title Section 생성
- auto layout: VERTICAL, CENTER/CENTER, padding 112/40/120/120, gap 20
- Pill Badge: auto layout HORIZONTAL, CENTER/CENTER, padding 20/20/40/40
- **폰트 생성 후 반드시 `set_font_name`** — 기본 Inter 방지

### CTA Bar
- **클로징 직전 마지막 콘텐츠 프레임에만** 적용
- position: absolute, x=1, y=1304

---

## 디자인 절대 규칙

### Fill 규칙
- **fill 금지:** Title Section, Cards Container, Footer, Text Area
- **fill 허용:** 최상위(#FFFFFF), Inner Frame(#FEFAEE), Inner Gold Frame(#FCD564), Card(#FFFFFF), CTA Bar(#FFBE00), Pill Badge(#FCD15A), Badge(#FCD564/#DB6E00)

### Width 규칙
- Title Section, Cards Container, Footer: **1080px**
- Card: **920px**, radius 82px, stroke #FCD564 4px
- Step Card: radius 36px, stroke 없음

### Closing — 반드시 wn-closing(601:6584) 클론
- clone_node로 복제 — 직접 빌드 금지
- Closing Description: **Pretendard Regular 44px** (#222222)
- Component 2 SVG (171x258) 사이즈 변경 금지

### Cover Title
- Line 1: Pretendard Variable Regular 120px, #424242
- Line 2-3: Pretendard Variable ExtraBold 120px, 그라디언트 #424242→#FFBE00

### Badge
- 정원형 필수 (가로=세로), 생성 후 resize_node 호출
- Template B: 80x80, #FCD564
- Template E: 68x68, #DB6E00

### 색상 규칙
- 본문: #333333 (#111111 금지)
- 서브: #424242
- 하락: #3741F2 / 상승: #FA4444
- #000000 절대 금지

### 혼합 폰트 텍스트 교체
- `set_text_content` 전에 반드시 `set_font_name`으로 폰트 통일
- 헤드라인: Pretendard Variable ExtraBold
- 본문: Pretendard Regular
- 서브: Pretendard Variable Medium
- Footer: Montserrat SemiBold / Regular

### 프레임 생성 직후 체크
- [ ] Inner Frame (#FEFAEE, radius 80)
- [ ] Title Section (Pill + Title + Tag)
- [ ] Footer 하단 (y=1312)
- [ ] CTA Bar 클로징 직전에만
- [ ] Badge 정원형
- [ ] 폰트 Pretendard Variable (Inter 아닌지)
- [ ] width 1080

---

## 캡션 규칙 (goldie-marketer)

### SEO 최적화
- 첫 125자에 핵심 키워드 ("금시세", "금 1돈", "금골디")
- 해시태그 5개 이내
- 서비스명 "금골디" 캡션 내 2회 이상

### CTA
- 저장: "나중에 꺼내보실 수 있도록 저장해두세요"
- 공유: "금 갖고 계신 분들께 공유해드리면 도움이 될 거예요"

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

1. **Figma 프레임:** 커버 + 본문 2~4장 (wn+faq 혼합) + 클로징
2. **인스타 캡션:** SEO 최적화
3. **해시태그:** 5개
4. **Alt text:** 장별
5. **저장/공유 CTA:** 2종
