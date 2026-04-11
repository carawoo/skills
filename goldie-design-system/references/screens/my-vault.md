# MY금고 홈 프로덕션 레퍼런스

## 구조 (360x1504, bg #FFF, overflow-y scroll)

### header set (y:0, 96px)
- StatusBar(48) + header_defalt(48)
- Slot: logo(골디 emblem) + ic/24/alarm_off(알림벨)
- Title: hidden

### 총 자산 (y:116, mx:20, 320px)
- "MY금고 총 자산" B2/SB #404040 + "오늘 17:25 기준" B3/Reg #A3A3A3
- "5,258,300원" T2/Bold #000
- "어제보다" B2/Reg #737373 + "+239,610원" B2/Reg #F53B32 + "(3.5%)" B2/Reg #F53B32

### 상단 박스 (bg #FAFAF9 warmGray-50, rounded:8, padding:20, gap:8)
- MY귀금속 B2/Reg #000 → 4,409,300원 B2/SB #000
- 골디캐시 → 837,000원
- 모은 금 → 837,000g

### MY귀금속 현황 (bg #F5F5F4 warmGray-100, rounded:20 20 0 0, padding:30 20 148)
- "MY귀금속 현황" B1/SB #000 + ic/18/info(#A3A3A3)

#### 보유량 2열 (154x148, bg #FFF, rounded:8, padding:16, gap:26)
- 금: ic/18/my_gold(#FFD664) + "금 보유량" B2/SB #404040
  - "총 24.152g" B3/Reg #404040
  - "4,125,500원" B1/SB #000
  - "+247,300원 (6.32%)" B3/Reg #F53B32
- 은: ic/18/my_silver(#BFE3FE) + 동일 구조
  - 하락: #2563EB (text/blue)

#### 귀금속 리스트 (bg #FFF, rounded:8, padding:16 20 20)
- "총 3개" B2/SB #404040
- 아이템: 64x64 이미지(rounded:12) + gap:12
  - "18K 반지 | 5.2g" B3/SB #737373 (함량|중량, separator: 1px #D4D4D4 rotated)
  - "1,167,300원" B1/SB #000
  - "+124,900원 (6.32%)" B3/Reg #F53B32
  - ic/18/allow_line chevron #A3A3A3
- CTA: "추가하기"(bg #FFF7D8) + "판매하기"(bg #FFD664) 각 136x50 rounded:8 B2/SB #000

### MY자산 (gap:16)
- "MY자산" B1/SB #000
- 골디캐시 박스 (bg #FFF, rounded:8, padding:16 20)
  - ic/18/cash + "골디캐시" B2/SB #404040
  - "837,000원" B1/SB #000 + 출금/내역 버튼(bg #F5F5F5, rounded:8, B3/SB #000)
- 모은금 박스 (bg #FFF, rounded:8, padding:16 20 20)
  - ic/18/gold + "모은 금" B2/SB #404040 + chevron
  - 모은 금 B3/Reg #737373 → "0.007579g" B1/SB #000
  - 환산 금액 B3/Reg #737373 → "약 6,557원" B1/SB #000

### bottom navigation_B2C (MY금고 active)
- 5탭 + 중앙 FAB(금모으기)
