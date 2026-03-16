---
name: create-feed
description: >
  금골디 인스타그램 카드뉴스 피드를 자동 생성한다.
  주제만 입력하면 리서치 → 디자인 → 캡션까지 한번에 완성.
  트리거: 인스타 피드, 카드뉴스, 피드 만들어, create-feed,
  인스타그램 콘텐츠, 금시세 뉴스, FAQ 콘텐츠.
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
  - 트렌드 분석, 경쟁사 콘텐츠 벤치마킹, 시장 데이터 수집에 활용
  - WebFetch로 Manus 세션 결과 참조 가능
- **인스타그램 SEO** 확인: 키워드 선정, 해시태그 5개

### Step 2: 디자인 생성 (Figma MCP)
- Figma 채널 `p8apycpv` 연결
- 템플릿 규칙에 따라 프레임 생성

### Step 3: 캡션 생성
- **goldie-marketer 에이전트** 실행: 캡션 + Alt text

---

## 템플릿 시스템

### 사용 가능한 템플릿

| 템플릿 | 용도 | 배경 |
|--------|------|------|
| A: Cover | 커버 | 골드 #FCD564, radius 80 |
| B: Card | 뉴스/퀴즈 | 크림 #FEFAEE |
| C: Closing | 마지막 장 (항상 포함) | 골드 #FCD564 |
| D: FAQ 콘텐츠 | 정보 리스트 카드 | 크림 #FEFAEE |
| E: FAQ 프로세스 | 스텝/과정 카드 | 크림 #FEFAEE |

### 기본 세트 구성

**뉴스형:** Cover(A) → Card(B) x2~3 → Closing(C)
**FAQ형:** Cover(A) → Process(E) x2~3 → Closing(C)
**퀴즈형:** Cover(A) → Quiz(B) → Answer(B, 오답 50%) → Closing(C)

---

## 디자인 절대 규칙 (위반 시 재작업)

### 1. Fill 규칙
- **fill 금지:** Header, Title Area, Cards Container, Footer Text Group, Row, Content, Text Area
- **fill 허용:** 최상위 프레임(#ffffff/#FEFAEE), Inner Gold Frame(#FCD564), Card(#FFFFFF), CTA Bar(#FFBE00), Badge(#FCD564/#DB6E00), Step Card(#FFFFFF)

### 2. Width 규칙
- Header, Title Area, Cards Container, Steps Section, Footer: **부모 width 1080px**
- Card (Template B): **920px** (1080 - 80*2)
- Step Card Row: **920px**, Step 1,2: **450px** (grow 1)

### 3. Header (Template B용)
```
Header (1080x200, fill none, horizontal, space-between, center, padding 60/80)
├─ Footer Text Group (fill none, horizontal, center, gap 28) ← 좌측 index 0
│  ├─ 카테고리 (Montserrat SemiBold 36px, #424242)
│  ├─ Line Divider (2x34, rgba(66,66,66,0.2))
│  └─ "금골디" (Montserrat Regular 36px, #424242)
└─ Logo Emblem (60x60 SVG, #FCD564/#EEB825) ← 우측
```

### 4. Cover Footer (Template A용)
```
Footer (1080x226, fill none, horizontal, space-between, center, padding 62/83/125)
├─ Footer Text Group (horizontal, gap 28)
│  ├─ "NEWS"/"WEEKLY REPORT" (Montserrat SemiBold 36px, #424242)
│  ├─ Line Divider (2x34, rgba(66,66,66,0.2))
│  └─ "금골디" (Montserrat Regular 36px, #424242)
└─ Logo Emblem (80x80 SVG, #595446 inner shadow)
```
- stroke top 1px rgba(66,66,66,0.15)

### 5. FAQ Footer (Template D/E용)
```
Footer (1080x128, fill none, horizontal, space-between, center, padding 30 40 / 80 80)
├─ Footer Text Group (opacity 0.2, horizontal, gap 28)
└─ Logo Emblem (48x48, #595446, opacity 0.5)
```

### 6. Card 규칙
- Template B: radius **82px**, stroke #FCD564 4px, width 920
- Step Card: radius **36px**, stroke 없음

### 7. Badge 규칙
- **정원형 필수** (가로 = 세로)
- Template B: 80x80, #FCD564, radius 80
- Template E: 68x68, #DB6E00, radius 34

### 8. Closing (항상 마지막)
- Inner Gold Frame (#FCD564, radius 80)
- Glow Circle (990x990, #FFBB1C 60%, blur 150)
- Content (1080x1440, fill none, vertical, space-between, center, padding **400**/120, gap auto)
- Component 2 SVG (171x258, #474747) — 사이즈 변경 금지
- Closing Title: LINEAR 그라디언트 #424242→#FFBE00 상→하
- "우리 집 숨은 금 찾기"

### 9. Cover Title
- Title Line 1: Pretendard Variable Regular 120px, **#424242 솔리드**
- Title Line 2-3: Pretendard Variable ExtraBold 120px, LINEAR 그라디언트 #424242→#FFBE00 상→하

### 10. Template E Title
- Pretendard Variable ExtraBold 64px, **#424242 솔리드**

### 11. Steps Section (Template E)
- drop shadow: X:0 Y:2 Blur:10 Spread:0 #AE8000 10%
- 3개(홀수): Row(2개 450x378) + 1개 풀와이드(920x340)
- 4개(짝수): 2x2 Wrap

### 12. 색상 규칙
- 본문: #333333 (기존 #111111 사용 금지)
- 서브: #424242
- 하락: #3741F2 (파랑)
- 상승: #FA4444 (빨강)
- #000000 절대 금지

### 13. 프레임 생성 직후 체크
- [ ] fill 제거했는지
- [ ] width 1080 맞췄는지
- [ ] Header 좌측이 텍스트 그룹인지
- [ ] Badge 정원형인지

---

## 캡션 규칙 (goldie-marketer)

### SEO 최적화
- 첫 125자에 핵심 키워드 집중 ("금시세", "금 1돈", "금골디")
- 해시태그 5개 이내
- Alt text 장별 작성 (키워드 포함)
- 서비스명 "금골디" 캡션 내 2회 이상

### CTA
- 저장 유도: "나중에 꺼내보실 수 있도록 저장해두세요"
- 공유 유도: "금 갖고 계신 분들께 공유해드리면 도움이 될 거예요"

### 브랜드 보이스
- 전문적이면서 친근한 톤
- 과장/공포/느낌표 남발 금지
- 출처 기반 수치만 사용

---

## 사용법

```
/create-feed 이번주 금시세 뉴스
/create-feed 한국은행 금 ETF 편입
/create-feed FAQ - 금 함량별 가격 차이
/create-feed 퀴즈 - 이번주 금 1돈 시세
```

## 산출물

1. **Figma 프레임:** 커버 + 본문 2~3장 + 클로징
2. **인스타 캡션:** SEO 최적화 (첫 125자 키워드)
3. **해시태그:** 5개
4. **Alt text:** 장별
5. **저장/공유 CTA:** 2종
