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
