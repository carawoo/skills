# 토큰 체계

## Color

```yaml
atomic: yellow/orange/red/purple/blue/green (50~900, 10단계) + naturalGray/warmGray (50~900)
semantic:
  fill: primary(bright~dark 6단계), grayscale(14종), status(8종), accent(12종)
  line: default/secondary/tertiary
  bg: default/secondary/tertiary/quaternary/primary
  text: primary/secondary/tertiary/quaternary/on-primary/disabled 등 12종
```

## Typography

```yaml
font: Pretendard (300~700)
letter_spacing: -1% (공통)

| 스케일   | Size  | Weight               | Line Height |
|---------|-------|----------------------|-------------|
| D1      | 52pt  | B(700), R(400)       | 66          |
| D2      | 42pt  | B(700), R(400)       | 56          |
| T1      | 36pt  | B(700), R(400)       | 48          |
| T2      | 30pt  | B(700), S(600), R(400) | 42        |
| H1      | 24pt  | B(700), S(600), R(400) | 32        |
| H2      | 22pt  | B(700), S(600), R(400) | 30        |
| H3      | 20pt  | B(700), S(600), R(400) | 28        |
| B1      | 18pt  | B(700), S(600), R(400) | 26        |
| B2      | 16pt  | B(700), S(600), R(400) | 24        |
| B3      | 14pt  | B(700), S(600), R(400) | 22        |
| Caption | 12pt  | B(700), M(500), R(400) | 16        |

utility: text-{scale}-{weight} (예: text-h1-bold, text-b2-regular, text-caption-medium)
```

## Radius / Spacing / Shadow

```yaml
radius: 0 / 2 / 4 / 8 / 16 / 20 / 999 px → rounded-{값}
spacing: Tailwind 기본 (4px 단위)
shadow: effect style "shadow" 정의됨
```

## Tailwind 유틸리티 매핑 (자주 쓰는 것)

```
# 배경
bg-bg-default         # 기본 (white)
bg-bg-secondary       # 구분선/섹션 (gray)
bg-bg-primary         # 브랜드 (gold)
bg-fill-primary       # 주요 요소
bg-fill-grayscale-*   # 뉴트럴 (100~900)

# 텍스트
text-text-primary     # 본문
text-text-secondary   # 부제/설명
text-text-tertiary    # 보조
text-text-quaternary  # 힌트/placeholder

# 상태
text-status-positive  # 상승/성공 (green)
text-status-negative  # 하락/에러 (red)

# 테두리
border-line-default   # 기본 선
border-line-secondary # 연한 선

# 타이포
text-d1-bold ~ text-caption-regular

# 모서리
rounded-0/2/4/8/16/20/999
```

## 토큰 CSS 코드 생성 규칙

```css
/* ✅ Tailwind CSS v4 패턴 — packages/theme/ */
@theme inline {
  --color-fill-primary: #D4A843;
}

@utility text-h1-bold {
  font-family: var(--font-pretendard);
  font-size: 24px;
  font-weight: 700;
  line-height: 32px;
  letter-spacing: -0.01em;
}

/* ❌ 금지: CSS-in-JS export, .ts 토큰 파일, @apply, theme() 함수 */
```
