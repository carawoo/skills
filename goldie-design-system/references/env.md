# 환경 정보

## Figma 파일

```yaml
# 디자인 시스템 (토큰 + 컴포넌트 정의)
ds_file_key: nb3vl6A5oOBjV5yW7XprRr
ds_file_name: GOLDIE_Design System

# 통합 피그마 (실제 배포 화면 + 기획서)
prod_file_key: EH0KGqF7rGyFIxwXETiXX5
prod_file_name: GOLDIE_통합 피그마 (NEW)
prod_pages: "[사용자]"(B2C), "[사장님]"(B2B), "표지"
prod_status: 📌마스터(현행) > 🟢배포완료 > 🟡진행중 > 🟣진행예정
```

## Figma DS 페이지 구조

```
fileKey: nb3vl6A5oOBjV5yW7XprRr

┌─ Foundation ─────────────────────────────────┐
│  Typography   │ D1~Caption, Pretendard       │→ typography.css
│  Colors       │ color_atomic, color_semantic, │→ color.css
│               │ token (3프레임)               │
│  Radius·      │ Radius, Spacing, Divider     │→ radius.css
│  Spacing·     │ (3프레임)                     │
│  Divider      │                              │
├─ Resource ───────────────────────────────────┤
│  Logo         │ 로고 에셋                     │
│  Icon         │ ic/18, ic/24 등              │→ svgIcons/ds/
├─ Component ──────────────────────────────────┤
│  Popup        │ 팝업/다이얼로그               │→ BasicPopup
│  Text filed   │ 텍스트 입력                   │→ TextDesignField
│  Navigation   │ 내비게이션 헤더               │→ NavigationHeader
└──────────────────────────────────────────────┘

스타일: Text(D1~Caption), Effect(shadow), Variables(색상)
```

## 코드베이스

```yaml
repo: goldncompany/goldie_frontend
framework: Next.js 15 (App Router, Turbopack)
language: TypeScript 5
styling: Tailwind CSS v4 (@theme inline, @utility)
component_pattern: CVA + clsx + tailwind-merge (shadcn/ui 패턴)
ui_primitive: Radix UI (accordion, alert-dialog, dialog, select, switch, slot)
package_manager: pnpm 10
build_tool: Turborepo
storybook: v10.3 (React-Vite, 포트 6007)
font: Pretendard (300~700, woff2)
state: Zustand 5 + TanStack React Query 5
form: React Hook Form 7 + Zod 3
navigation: Stackflow (앱-like 화면 전환)
animation: Framer Motion 12 + Lottie React
test: Vitest 3 + Testing Library + Playwright
```

## 모노레포 구조

```
apps/goldie/              # B2C 웹앱
apps/goldie-partner/      # B2B 파트너 웹뷰
packages/design-system/   # @goldie/design-system
packages/theme/           # @goldie/theme (토큰 CSS)
packages/hooks/           # @goldie/hooks
packages/types/           # @goldie/types
packages/util/            # @goldie/util (cn 함수 등)
packages/config/          # @goldie/config
```

## 기존 DS 컴포넌트 (4개)

| 컴포넌트 | Variants | Props |
|----------|----------|-------|
| AtomicButton | variant 4종(primary/secondary/tertiary/quaternary), size 5종(xlarge~xsmall) | leftIcon, rightIcon, disabled, loading |
| BasicPopup | horizontal/vertical 레이아웃 | icon, title, description, primaryButton, secondaryButton, textLink |
| NavigationHeader | variant 4종(default/popup/modal/opacity) | leading, title, trailing, textAction 슬롯 |
| TextDesignField | fieldSize 2종 | tone 3종(default/negative/positive), label, guideText, clearButton, boxButton |

## 모션/아이콘/Lottie

- **DsMotion**: 프리셋명 래퍼 (fadeIn, fadeUp, scaleIn, slideFromBottom, sheetSnap 등 35종)
- **Stagger**: list, tight, grid, cascade
- **아이콘**: SVG 48종 (`packages/design-system/src/svgIcons/ds/`)
- **Lottie**: bonusBox, gameSuccess, identityVerification, paperLoading
