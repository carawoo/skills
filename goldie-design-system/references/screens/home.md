# 홈 화면 프로덕션 레퍼런스

## 구조 (360x1992, bg #FFF, overflow-y scroll)

### 상단 영역 (0~600px)
- bg: #F5F5F4 (warmGray-100) → 시세 섹션부터 #FFF (rounded:20 20 0 0)
- header set: logo(Slot) + ic/24/alarm_on(알림, 빨간점 #F53B32)
- 타이틀: H2/SB #000, y:127
- 2열 카드 (y:207, 320x230, gap:12)
  - 금팔기: 154x230, gradient #FFF9E3→#FFEFB1, shadow/normal, rounded:8
    - "금 팔기" B1/SB + "집에서 편하게\n금은방 시세 비교" B3/Reg
  - 우측 2단: 각 154x109, bg #FFF, shadow/normal, rounded:8
    - "AI 예상견적" B1/SB + B3/Reg #404040
    - "금 모으기" B1/SB + "NEW!" badge(bg #422C07, Caption/Bold #FFF)
- MY금고 바: 320x56, bg #FFF, shadow/normal, rounded:8, padding:16 12
  - ic/18/my_gold + "MY금고" B2/SB #404040 → "5,258,300원" B2/SB #000 + chevron

### 실시간 시세 (y:536)
- bg #FFF, rounded:20 20 0 0, padding:24 20
- "실시간 24K 순금 시세" B2/Reg #404040 + 기준시각 B3/Reg #A3A3A3
- "864,000원" H1/Bold #000
- "어제보다" B3/Reg #737373 + "+239,610원 (3.5%)" B3/Reg #F53B32
- 차트: 120x58, gradient #FFD664→#FFF, line #FFAA00
- CTA: button/atomic Quaternary 320x50

### 이달의 골디 (y:792)
- "이달의 금골디" H3/SB #000 + B2/Reg #404040
- 가로 스크롤: 148x148 카드, bg #FAFAF9, rounded:16
  - B3/SB #404040 (라벨) + B1/Bold #404040 (값) + gfx/60 아이콘

### 이번주 금 소식 (y:1076)
- H3/SB #000 + B2/Reg #404040
- 리스트: 78px, padding:0 24, gap:16
  - 번호 B3/SB #A3A3A3 + 카테고리 B3/SB #FFAA00 + 제목 B3/Reg #404040

### 고객센터 (y:1470)
- "도움이 필요하신가요?" B2/Bold #424242
- 카드: 320x96, border #F5F5F5, rounded:12
  - 문의하기/FAQ: ic/18 + B3/Reg #404040 + chevron #525252

### 푸터 (y:1650)
- bg #FAFAFA, padding:32 20 60
- "금골디 사업자 정보" B3/SB #737373 + dropdown
- 정보: Caption/Reg #A3A3A3

### 하단탭
- bottom navigation_B2C, 홈 active (#000, icon #FFAA00)
