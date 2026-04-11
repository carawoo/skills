# 토큰 체계 (Figma DS + color.css 검증 완료)

## Color — Atomic

```
Yellow:  50:#FFF7D8  100:#FFEDB3  200:#FFE695  300:#FFD664  400:#FFBE19  500:#FFAA00  600:#CA8B04  700:#A16907  800:#624410  900:#422C07
Orange:  50:#FFF7ED  100:#FFEDD5  200:#FED7AA  300:#FB923C  400:#F97316  500:#EA580C  600:#C2410C  700:#9A3412  800:#7C2D12  900:#431407
Red:     50:#FEEBEB  100:#FFBFBC  200:#FF8E8E  300:#FF7070  400:#FB5656  500:#F53B32  600:#DF362E  700:#AE2A24  800:#87201C  900:#671915
Purple:  50:#F4F0FF  100:#E7DCFF  200:#AF90FD  300:#885FF7  400:#7B42FF  500:#6620DF  600:#44149F  700:#381881  800:#301C69  900:#26203A
Blue:    50:#EDF7FE  100:#DBEFFE  200:#BFE3FE  300:#93CCFD  400:#67B4FC  500:#3D7CF5  600:#2563EB  700:#1644C7  800:#043189  900:#082969
Green:   50:#EAFAEE  100:#CAF6D4  200:#9DE8AD  300:#70DD89  400:#4AD568  500:#13C33B  600:#0EAF32  700:#1D913A  800:#17702F  900:#115626
NaturalGray: 50:#FAFAFA  100:#F5F5F5  200:#E5E5E5  300:#D4D4D4  400:#A3A3A3  500:#737373  600:#525252  700:#404040  800:#171717  900:#0A0A0A
WarmGray:    50:#FAFAF9  100:#F5F5F4  200:#E7E5E4  300:#D6D3D1  400:#A8A29E  500:#78716C  600:#57534E  700:#44403C  800:#292524  900:#1C1917
Basic: white:#FFFFFF  black:#000000
```

## Color — Semantic (color.css 기준)

```yaml
fill:
  primary-bright:   yellow-50   #FFF7D8
  primary-light:    yellow-100  #FFEDB3
  primary-default:  yellow-300  #FFD664   ← 브랜드 메인!
  primary-strong:   yellow-400  #FFBE19
  primary-heavy:    yellow-500  #FFAA00
  primary-dark:     yellow-900  #422C07
  grayscale-black:  #000000
  grayscale-white:  #FFFFFF
  grayscale-gray900~50: naturalGray 스케일
  grayscale-warmGray100: #F5F5F4
  grayscale-warmGray50:  #FAFAF9
  status-lightRed:  red-50    #FEEBEB
  status-red:       red-500   #F53B32
  status-lightGreen: green-50 #EAFAEE
  status-green:     green-500 #13C33B
  status-lightBlue: blue-50   #EDF7FE
  status-blue:      blue-500  #3D7CF5
  status-lightOrange: orange-100 #FFEDD5
  status-orange:    orange-300 #FB923C

line:
  default:    naturalGray-300  #D4D4D4
  secondary:  naturalGray-200  #E5E5E5
  tertiary:   naturalGray-100  #F5F5F5

bg:
  default:    white      #FFFFFF
  secondary:  naturalGray-50  #FAFAFA
  tertiary:   naturalGray-100 #F5F5F5
  quaternary: warmGray-100    #F5F5F4
  primary:    yellow-300      #FFD664

text:
  default:      black         #000000
  white:        white         #FFFFFF
  black:        black         #000000
  secondary:    naturalGray-700  #404040
  tertiary:     naturalGray-500  #737373
  quaternary:   naturalGray-400  #A3A3A3
  disable:      naturalGray-300  #D4D4D4
  primary:      yellow-300       #FFD664  (브랜드 텍스트)
  deepPrimary:  yellow-500       #FFAA00
  red:          red-600          #DF362E
  green:        green-500        #13C33B
  blue:         blue-500         #3D7CF5
  orange:       orange-300       #FB923C

overlay:
  dim: rgba(0,0,0,0.4)
  heavy-dim: rgba(0,0,0,0.6)
```

## Typography (Figma DS CSS 기준)

```
font-family: Pretendard
letter-spacing: -0.01em (전 스케일 공통)
color: #171717 (DS 기본 텍스트 색)

| Style         | Size | Weight      | Line Height |
|---------------|------|-------------|-------------|
| D1/Bold       | 52px | 700 (Bold)  | 66px        |
| D1/Regular    | 52px | 400 (Reg)   | 66px        |
| D2/Bold       | 42px | 700         | 56px        |
| D2/Regular    | 42px | 400         | 56px        |
| T1/Bold       | 36px | 700         | 48px        |
| T1/Regular    | 36px | 400         | 48px        |
| T2/Bold       | 30px | 700         | 42px        |
| T2/SemiBold   | 30px | 600         | 42px        |
| T2/Regular    | 30px | 400         | 42px        |
| H1/Bold       | 24px | 700         | 32px        |
| H1/SemiBold   | 24px | 600         | 32px        |
| H1/Regular    | 24px | 400         | 32px        |
| H2/Bold       | 22px | 700         | 30px        |
| H2/SemiBold   | 22px | 600         | 30px        |
| H2/Regular    | 22px | 400         | 30px        |
| H3/Bold       | 20px | 700         | 28px        |
| H3/SemiBold   | 20px | 600         | 28px        |
| H3/Regular    | 20px | 400         | 28px        |
| B1/Bold       | 18px | 700         | 26px        |
| B1/SemiBold   | 18px | 600         | 26px        |
| B1/Regular    | 18px | 400         | 26px        |
| B2/Bold       | 16px | 700         | 24px        |
| B2/SemiBold   | 16px | 600         | 24px        |
| B2/Regular    | 16px | 400         | 24px        |
| B3/Bold       | 14px | 700         | 22px        |
| B3/SemiBold   | 14px | 600         | 22px        |
| B3/Regular    | 14px | 400         | 22px        |
| Caption/Bold  | 12px | 700         | 16px        |
| Caption/Med   | 12px | 500 (Med)   | 16px        |
| Caption/Reg   | 12px | 400         | 16px        |

Tailwind utility: text-{scale}-{weight} (예: text-h1-bold, text-b2-regular, text-caption-medium)
```

## Radius

```
0 / 2 / 4 / 8 / 16 / 20 / 999 px
Tailwind: rounded-{값}
Figma DS에서 border-radius: 20px (컴포넌트), 999px (pill)
```

## Shadow (Effect Styles)

```
shadow/nomal, shadow/strong, shadow/heavy — 3단계
```

## Figma → CSS 매핑 주의사항

- 브랜드 gold = **#FFD664** (yellow-300), NOT #D4A843
- text-default = **#000000**, NOT #1f1f1f (Figma preview의 #171717은 gray-800)
- text-secondary = **#404040** (gray-700)
- text-tertiary = **#737373** (gray-500)  
- text-quaternary = **#A3A3A3** (gray-400)
- line-default = **#D4D4D4** (gray-300), NOT #E8E8E8
- bg-secondary = **#FAFAFA** (gray-50), NOT #F5F5F5
- status-positive = **#13C33B** (green-500)
- status-negative = **#F53B32** (red-500) / text-red = #DF362E (red-600)

## DS 컴포넌트 스펙

### Atomic Button

| Size | Height | Padding | Text Style | Icon Size | Radius |
|------|--------|---------|-----------|----------|--------|
| LARGE | 50px | 0 20px | B2/SB 16px #000 | 18x18 | 8px |
| MEDIUM | 44px | 0 20px | B3/SB 14px #000 | 16x16 | 8px |
| SMALL | 36px (min-w:60) | 0 12px | B3/SB 14px #000 | 16x16 | 8px |
| XSMALL | 32px (min-w:54) | 0 12px | B3/SB 14px #000 | 16x16 | 8px |
| XXSMALL | 24px | 4px 8px | Caption/Med 12px #000 | 16x16 | 999px |

Variants:
- Primary: bg #FFD664 / disabled bg #E5E5E5 text #FFF
- Secondary: bg #FFF7D8 / disabled text #D4D4D4
- Tertiary: bg #F5F5F5 / disabled text #D4D4D4
- Quaternary: bg #FFF border #E5E5E5 / disabled text #D4D4D4

### Text Field

| Size | Input Height | Placeholder | Label | Guide |
|------|-------------|-------------|-------|-------|
| large | 50px | B2/Reg 16px | B3/Reg 14px #737373 | Caption/Reg 12px |
| xlarge | 58px | B1/Reg 18px | B2/Reg 16px #737373 | B3/Reg 14px |

States:
- Inactive: border #E5E5E5
- Focus: border #000000 + cursor
- Typing: border #000000 + value #000
- Finished: border #E5E5E5 + value #000
- Disabled: border #E5E5E5, bg #F5F5F5, btn bg #E5E5E5 text #FFF

Variants:
- default: guide #737373
- negative (line_color=red): border #F53B32, guide #F53B32
- negative (line_color=gray): border #000/#E5E5E5, guide #F53B32
- positive: guide #13C33B

Inner button: 60x36 bg #FFD664 rounded:8, B3/SB 14px #000
Required marker: * B3/Reg #F53B32

### MCP 연동 가이드 (Button_MCP)
공통 네이밍: Variant → 그대로 props 매핑
- Atomic 버튼: size/variant/state/leftIcon/rightIcon/BTN
- Bottom 버튼: Atomic 버튼 조합, gradient bg, padding 20px
- Select Box: variant/state/size + Boolean
- Stepper: variant/size

### Popup/Basic
layout: horizontal(320px, rounded:16, 2열 버튼) / vertical(320px, rounded:16, 세로 버튼)
- icon: 80x80 slot
- title: H3/SB #000, center
- subtitle: B2/Reg #737373, center
- CTA: Secondary(#FFF7D8) + Primary(#FFD664), 각 136x50
- textLink: B3/SB #A3A3A3 underline

### Popup/BottomSheet
- dim: rgba(0,0,0,0.4)
- container: rounded:20 20 0 0, bg #FFF
- header: header_defalt + ic/24/close
- CTA: button/bottom (gradient bg, padding 20px, Atomic LARGE)

### Toast
- height:40, rounded:999, bg rgba(0,0,0,0.6), backdrop-filter blur(5px)
- text: B3/SB #FFF, icon 24x24
- variants: default/positive(#13C33B)/negative(#F53B32)/cautionary(#FFBE19)

### Tooltip
- bg: rgba(0,0,0,0.6), rounded:10, B3/Reg #FFF
- positions: top/bottom × left/middle/right
- close: ic/18/close #A3A3A3
- arrow: 16x8 triangle same bg

### Header (header_defalt)
- 360x48, bg #FFF
- variants: Default(Slot+Title+Frame), Popup(Title+close), Modal(Title+close), Opacity(transparent bg, white icons)
- Title: B2/SB #000, center
- Slot: 24x24 (ic/24/back, ic/24/blank)
- Frame: text btn(B3/SB #A3A3A3) + ic/24 slots

### header set
- Status Safe Area(48) + header_defalt(48) = 96px total
- StatusBar: light(#212121 icons) / dark(#FFF icons)

### Bottom Navigation B2C
- 360x72, bg #FFF, border-top #F5F5F5, shadow heavy, rounded:16 16 0 0
- 5 tabs: 홈/MY금고/금모으기/내역/메뉴 (each 56x72)
- active: icon filled #FFAA00, text #000 Caption/Med
- inactive: icon stroke #737373, text #737373 Caption/Med
- center FAB: 56x56 gradient gold, border 3px #FFF, shadow

### Bottom Navigation B2B
- 360x82, 3 tabs: 홈/채팅/MY스토어
- text: B3/SB, active #000, inactive #737373

### Tab
- line underline: active #FFD664 4px, B2/SB #000 / inactive B2/Reg #A3A3A3
- new dot: 4x4 #FF0000

### Category
- pill: selected(bg #000, B3/SB #FFF) / default(bg #FFF border #E5E5E5, B3/SB #737373)
- height:38, rounded:999, padding 8 16

## Spacing (DS CSS 검증 완료)

4배수 기준, 예외적 값 최소화

| Token | Value |
|-------|-------|
| spacing-0 | 0px |
| spacing-20 | 2px |
| spacing-40 | 4px |
| spacing-80 | 8px |
| spacing-120 | 12px |
| spacing-160 | 16px |
| spacing-200 | 20px |
| spacing-240 | 24px |
| spacing-320 | 32px |
| spacing-400 | 40px |
| spacing-600 | 60px |

## Divider

콘텐츠 간 구분선. 리스트/카드/섹션 구분에 사용.

| Token | Height | Color Token | HEX |
|-------|--------|------------|-----|
| divider-1 | 1px | line-default(#D4D4D4) / line-secondary(#E5E5E5) / line-tertiary(#F5F5F5) | 선택 |
| divider-2 | 2px | line-tertiary | #F5F5F5 |
| divider-8 | 8px | line-tertiary | #F5F5F5 |

용도:
- divider-1: 리스트 아이템 사이 (1px solid)
- divider-2: 가벼운 섹션 구분
- divider-8: 주요 섹션 구분 (MY금고 홈 등)
