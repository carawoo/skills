---
name: goldie-design-system
description: >
  금골디 디자인 시스템 코드 생성기 & 스토리보드 자동화.
  Figma 디자인 시스템에서 토큰/컴포넌트를 추출하여 Storybook 기반 코드를 생성하고,
  PRD/기능정의서를 입력하면 디자인 시스템 컴포넌트 기반 스토리보드를 자동 생성한다.
  트리거: 디자인시스템, 스토리북, 스토리보드, 컴포넌트 생성, 토큰 추출,
  Figma 코드화, 화면정의서, 기능정의서, PRD 코드화, DS 동기화.
---

# Goldie Design System Skill

금골디 Figma 디자인 시스템 → 코드 자동 생성 + PRD → 스토리보드 변환 스킬.

## 모드

이 스킬은 **3가지 모드**로 동작한다:

### Mode A: `figma-sync` — Figma → 코드 동기화
Figma 디자인 시스템에서 토큰과 컴포넌트를 추출하여 코드로 변환

### Mode B: `component-gen` — 컴포넌트 코드 생성
Figma의 특정 컴포넌트를 코드 + Storybook 스토리로 변환

### Mode C: `storyboard` — PRD → 스토리보드 생성
PRD/기능정의서를 입력받아 디자인 시스템 컴포넌트 기반 스토리보드 코드 생성

---

## 환경 정보 (변경 금지)

```yaml
figma_file_key: nb3vl6A5oOBjV5yW7XprRr
figma_file_name: GOLDIE_Design System

# 모노레포 구조
monorepo: goldncompany/goldie_frontend
design_system_package: packages/design-system  # @goldie/design-system
theme_package: packages/theme                   # @goldie/theme

# 기술 스택
framework: Next.js 15 (App Router)
language: TypeScript 5
styling: Tailwind CSS v4 (@theme inline, @utility)
component_pattern: Radix UI + CVA + tailwind-merge (shadcn/ui 패턴)
package_manager: pnpm 10
build_tool: Turborepo
storybook: v10.3 (React-Vite)
font: Pretendard (300~700)
motion: Framer Motion 12 + Lottie React
icons: Lucide React + 커스텀 SVG 48종 (packages/design-system/src/svgIcons/ds/)

# 기존 토큰 파일
tokens:
  color: packages/theme/color.css        # Atomic(yellow/orange/red/purple/blue/green 50~900) + Semantic(fill/line/bg/text)
  typography: packages/theme/typography.css  # D1~D2, T1~T2, H1~H3, B1~B3, Caption
  radius: packages/theme/radius.css      # 0/2/4/8/16/20/999px
  spacing: 없음 (Tailwind 기본 사용)
  shadow: 없음

# 기존 컴포넌트 (4개)
existing_components:
  - AtomicButton     # CVA variant 4종, size 5종, icon 지원
  - BasicPopup       # horizontal/vertical, icon/title/description
  - NavigationHeader # variant 4종, leading/title/trailing 슬롯
  - TextDesignField  # fieldSize 2종, tone 3종, label/guideText

# 기존 Storybook 스토리 (7개)
existing_stories:
  - AtomicButton.stories.tsx
  - BasicPopup.stories.tsx
  - NavigationHeader.stories.tsx
  - TextDesignField.stories.tsx
  - IconsCatalog.stories.tsx
  - LottiePlayground.stories.tsx
  - MotionPlayground.stories.tsx
```

---

## Mode A: `figma-sync` — Figma → 코드 동기화

### 트리거 예시
- "디자인 시스템 동기화해줘"
- "Figma 토큰 추출해줘"
- "컬러 토큰 업데이트"

### 실행 절차

**Step 1: Figma 디자인 시스템 구조 파악**
```
fileKey: nb3vl6A5oOBjV5yW7XprRr

페이지 구조 (확인 완료):
┌─ Foundation ─────────────────────────────────────────┐
│  Typography        │ D1~Caption, Pretendard          │→ typography.css
│  Colors            │ color_atomic, color_semantic,    │→ color.css
│                    │ token (3개 프레임)               │
│  Radius·Spacing·   │ Radius, Spacing, Divider        │→ radius.css
│  Divider           │ (3개 프레임)                     │
├─ Resource ───────────────────────────────────────────┤
│  Logo              │ 로고 에셋                        │
│  Icon              │ 아이콘 세트 (ic/18, ic/24 등)    │→ svgIcons/ds/
├─ Component ──────────────────────────────────────────┤
│  Popup             │ 팝업/다이얼로그 컴포넌트          │→ BasicPopup
│  Text filed        │ 텍스트 입력 필드                  │→ TextDesignField
│  Navigation        │ 내비게이션 헤더                   │→ NavigationHeader
├─ 기타 ───────────────────────────────────────────────┤
│  as is - to be     │ 리디자인 비교 문서                │
│  표지               │ DS 표지                         │
└──────────────────────────────────────────────────────┘

스타일 정보 (파일 전역):
- Text styles: D1, D2, T1, T2, H1, H2, H3, B1, B2, B3, Caption
- Effect styles: shadow
- Variables: Figma Variables 컬렉션 (색상 토큰)
```

**Step 2: 토큰 추출 & 코드 생성**
```
1. get_design_context로 각 토큰 페이지의 상세 정보 추출
2. get_variable_defs로 Figma Variables(색상, 수치) 추출

3. 기존 토큰 파일과 비교:
   - packages/theme/color.css
   - packages/theme/typography.css
   - packages/theme/radius.css

4. 변경사항이 있으면 기존 파일 업데이트
   - 새 토큰 추가
   - 변경된 값 수정
   - Tailwind v4 @theme / @utility 문법 유지

5. 없는 토큰 파일 신규 생성:
   - spacing.css (필요시)
   - shadow.css (필요시)
```

**Step 3: 결과 리포트**
```
변경 사항 요약:
- 추가된 토큰: N개
- 수정된 토큰: N개
- 새 파일: [파일 목록]
```

### 코드 생성 규칙 (토큰)

```css
/* Tailwind CSS v4 토큰 패턴 — packages/theme/ */

/* ✅ 올바른 패턴 */
@theme inline {
  --color-fill-primary: #D4A843;
  --color-fill-primary-bright: #F5D680;
}

@utility text-h1-bold {
  font-family: var(--font-pretendard);
  font-size: 24px;
  font-weight: 700;
  line-height: 32px;
  letter-spacing: -0.01em;
}

/* ❌ 절대 금지 */
/* CSS-in-JS 형태 export, 별도 .ts 토큰 파일 생성 금지 */
/* 기존 color.css/typography.css/radius.css 구조를 반드시 따를 것 */
```

---

## Mode B: `component-gen` — 컴포넌트 코드 생성

### 트리거 예시
- "Button 컴포넌트 만들어줘"
- "Figma에서 BottomSheet 코드화해줘"
- "Toast 컴포넌트 Storybook으로"

### 실행 절차

**Step 1: Figma 컴포넌트 분석**
```
1. get_design_context로 대상 컴포넌트의 상세 정보 추출
   - Variants (상태, 사이즈, 타입 등)
   - Props 구조
   - 스크린샷

2. get_context_for_code_connect로 컴포넌트 메타데이터 추출
   - property definitions
   - variant options
   - descendant tree
```

**Step 2: 컴포넌트 코드 생성**

파일 구조:
```
packages/design-system/src/components/{ComponentName}/
├── {ComponentName}.tsx           # 컴포넌트 코드
├── {ComponentName}.stories.tsx   # Storybook 스토리
└── index.ts                      # re-export
```

**Step 3: 기존 패턴 준수 확인**
```
1. 기존 컴포넌트(AtomicButton 등) 코드를 Read로 읽어서 패턴 파악
2. 동일한 CVA + Tailwind + Radix 패턴 적용
3. 기존 export index에 새 컴포넌트 추가
```

### 코드 생성 규칙 (컴포넌트)

```tsx
// ✅ 컴포넌트 코드 패턴 (packages/design-system/src/components/)

import { cva, type VariantProps } from "class-variance-authority";
import { cn } from "@goldie/util";        // 또는 로컬 cn 유틸
import { forwardRef } from "react";

// 1. CVA variants 정의
const componentVariants = cva(
  // base 클래스 (Tailwind v4 유틸리티)
  "inline-flex items-center justify-center transition-colors",
  {
    variants: {
      variant: {
        primary: "bg-fill-primary text-text-on-primary",
        secondary: "bg-fill-grayscale-100 text-text-primary",
      },
      size: {
        large: "h-14 px-6 text-b1-semibold rounded-16",
        medium: "h-12 px-5 text-b2-semibold rounded-12",
        small: "h-10 px-4 text-b3-semibold rounded-8",
      },
    },
    defaultVariants: {
      variant: "primary",
      size: "medium",
    },
  }
);

// 2. Props 타입 (VariantProps + HTML 확장)
export interface ComponentNameProps
  extends React.HTMLAttributes<HTMLElement>,
    VariantProps<typeof componentVariants> {
  // 추가 Props
}

// 3. forwardRef 컴포넌트
const ComponentName = forwardRef<HTMLElement, ComponentNameProps>(
  ({ className, variant, size, ...props }, ref) => {
    return (
      <element
        ref={ref}
        className={cn(componentVariants({ variant, size }), className)}
        {...props}
      />
    );
  }
);
ComponentName.displayName = "ComponentName";

export { ComponentName, componentVariants };
```

```tsx
// ✅ Storybook 스토리 패턴

import type { Meta, StoryObj } from "@storybook/react";
import { ComponentName } from "./ComponentName";

const meta: Meta<typeof ComponentName> = {
  title: "공통 컴포넌트/ComponentName",
  component: ComponentName,
  tags: ["autodocs"],
  argTypes: {
    variant: {
      control: "select",
      options: ["primary", "secondary"],
      description: "컴포넌트 스타일 변형",
    },
    size: {
      control: "select",
      options: ["large", "medium", "small"],
      description: "컴포넌트 크기",
    },
  },
};

export default meta;
type Story = StoryObj<typeof ComponentName>;

// Default 스토리
export const Default: Story = {
  args: {
    children: "텍스트",
    variant: "primary",
    size: "medium",
  },
};

// Variant별 스토리
export const AllVariants: Story = {
  render: () => (
    <div className="flex flex-col gap-4">
      <ComponentName variant="primary">Primary</ComponentName>
      <ComponentName variant="secondary">Secondary</ComponentName>
    </div>
  ),
};

// Size별 스토리
export const AllSizes: Story = {
  render: () => (
    <div className="flex items-center gap-4">
      <ComponentName size="large">Large</ComponentName>
      <ComponentName size="medium">Medium</ComponentName>
      <ComponentName size="small">Small</ComponentName>
    </div>
  ),
};

// 상태별 스토리 (disabled, loading 등)
export const Disabled: Story = {
  args: {
    children: "비활성",
    disabled: true,
  },
};
```

### 금지 사항
- styled-components, emotion 등 CSS-in-JS 절대 사용 금지
- 별도 .css 모듈 파일 생성 금지 (Tailwind 유틸리티만 사용)
- 기존 4개 컴포넌트(AtomicButton, BasicPopup, NavigationHeader, TextDesignField) 수정 금지
- Radix UI 프리미티브가 이미 devDependency에 있으면 그걸 래핑할 것

---

## Mode C: `storyboard` — PRD → 스토리보드 생성

### 트리거 예시
- "이 PRD로 스토리보드 만들어줘"
- "기능정의서 기반 화면 코드화"
- "이 기획서 스토리보드로 변환"

### 입력
- PRD / 기능정의서 / 화면 기획서 (텍스트 또는 파일)
- 선택: Figma 프로토타입 URL

### 실행 절차

**Step 1: PRD 분석**
```
1. PRD에서 화면(Screen) 단위 추출
   - 화면명, 목적, 주요 기능
   - 사용자 플로우 (화면 간 전환)
   - 상태별 분기 (로딩, 에러, 빈 상태, 성공)

2. 각 화면에 필요한 컴포넌트 매핑
   - 기존 DS 컴포넌트 재사용 우선
   - 없는 컴포넌트는 Mode B로 먼저 생성 제안

3. Figma 프로토타입이 있으면:
   - get_design_context로 레이아웃/컴포넌트 구조 파악
   - get_screenshot으로 시각 참조
```

**Step 2: 스토리보드 코드 생성**

파일 구조:
```
storyboard/{FeatureName}/
├── README.md                    # 기능 개요, 플로우 다이어그램
├── screens/
│   ├── {Screen1}.tsx            # 화면 컴포넌트 (DS 조합)
│   ├── {Screen1}.stories.tsx    # Storybook 스토리 (상태별)
│   ├── {Screen2}.tsx
│   └── {Screen2}.stories.tsx
├── flow.stories.tsx             # 전체 플로우 스토리 (화면 전환)
└── types.ts                     # 공유 타입
```

**Step 3: Storybook 플로우 스토리**
```tsx
// flow.stories.tsx — 화면 전환 플로우를 한눈에

import type { Meta, StoryObj } from "@storybook/react";

const meta: Meta = {
  title: "스토리보드/{FeatureName}/플로우",
  parameters: {
    layout: "fullscreen",
  },
};

export default meta;

// 각 화면을 순서대로 보여주는 스토리
export const Step1_진입: StoryObj = {
  render: () => <Screen1 />,
};

export const Step2_입력: StoryObj = {
  render: () => <Screen2 mockData={sampleData} />,
};

export const Step3_확인: StoryObj = {
  render: () => <Screen3 />,
};

// 상태별 분기
export const Error_네트워크: StoryObj = {
  render: () => <Screen2 error="network" />,
};

export const Empty_데이터없음: StoryObj = {
  render: () => <Screen2 data={[]} />,
};
```

**Step 4: README.md 자동 생성**
```markdown
# {FeatureName} 스토리보드

## 개요
{PRD에서 추출한 기능 설명}

## 화면 플로우
{Mermaid.js 플로우차트}

## 화면 목록
| # | 화면명 | 설명 | 상태 | 사용 컴포넌트 |
|---|--------|------|------|---------------|
| 1 | Screen1 | 진입 화면 | default, loading | NavigationHeader, AtomicButton |
| 2 | Screen2 | 입력 화면 | default, error, empty | TextDesignField, BasicPopup |

## 개발 가이드
- 필요 API: [엔드포인트 목록]
- 상태 관리: [Zustand store 구조 제안]
- 라우팅: [Stackflow 화면 전환 정의]
```

### 스토리보드 코드 규칙

```tsx
// ✅ 화면 컴포넌트 패턴

import { NavigationHeader } from "@goldie/design-system";
import { AtomicButton } from "@goldie/design-system";

interface Screen1Props {
  // 화면에 필요한 데이터
  data?: SomeType;
  // 상태 제어 (스토리보드용)
  isLoading?: boolean;
  error?: string;
}

/**
 * ## Screen1: {화면명}
 *
 * ### 기능
 * - {기능 1}
 * - {기능 2}
 *
 * ### 인터랙션
 * - {버튼} 탭 → Screen2로 이동
 * - 스와이프 다운 → 새로고침
 *
 * ### 상태
 * - default: 정상 데이터 표시
 * - loading: 스켈레톤 표시
 * - error: 에러 바텀시트
 * - empty: 빈 상태 일러스트
 */
export function Screen1({ data, isLoading, error }: Screen1Props) {
  if (isLoading) return <Screen1Skeleton />;
  if (error) return <Screen1Error error={error} />;
  if (!data) return <Screen1Empty />;

  return (
    <div className="flex flex-col min-h-screen bg-bg-default">
      <NavigationHeader variant="default" title="화면 제목" />

      <main className="flex-1 px-5 py-4">
        {/* 콘텐츠 영역 - DS 컴포넌트 조합 */}
      </main>

      <footer className="px-5 pb-8">
        <AtomicButton variant="primary" size="xlarge" className="w-full">
          다음
        </AtomicButton>
      </footer>
    </div>
  );
}
```

### 금지 사항
- 실제 API 호출 코드 작성 금지 (mock 데이터로 대체)
- 비즈니스 로직 구현 금지 (UI 구조만)
- 상태 관리 코드 구현 금지 (구조만 제안)
- 라우팅 코드 구현 금지 (화면 전환은 스토리로만 표현)

---

## 공통 규칙

### Figma MCP 접근 방법
```
1. get_metadata: 노드 구조 파악 (nodeId, 레이어명, 위치, 크기)
2. get_design_context: 상세 디자인 정보 + 스크린샷 + 참조 코드
3. get_screenshot: 시각적 확인용 스크린샷
4. get_variable_defs: Figma Variables (색상, 수치 토큰)
5. get_context_for_code_connect: 컴포넌트 Props/Variants 메타데이터
6. search_design_system: 디자인 시스템 에셋 검색

항상 fileKey: nb3vl6A5oOBjV5yW7XprRr 사용
```

### 기존 코드 읽기 필수
```
컴포넌트 생성 전 반드시:
1. gh api로 기존 컴포넌트 코드 확인 (패턴 파악)
   - gh api repos/goldncompany/goldie_frontend/contents/packages/design-system/src/components
2. 기존 Storybook 설정 확인
   - gh api repos/goldncompany/goldie_frontend/contents/packages/design-system/.storybook
3. 기존 theme 토큰 확인
   - gh api repos/goldncompany/goldie_frontend/contents/packages/theme

기존 패턴과 100% 일관성 유지
```

### Tailwind CSS v4 필수 규칙
```css
/* ✅ v4 문법 사용 */
@theme inline { ... }
@utility text-h1-bold { ... }

/* ❌ v3 문법 금지 */
/* @apply, theme() 함수, tailwind.config.js 방식 금지 */
```

### 네이밍 규칙
```
- 컴포넌트: PascalCase (AtomicButton, BasicPopup)
- 파일: PascalCase.tsx
- 스토리 타이틀: "공통 컴포넌트/{ComponentName}" (기존 패턴)
- 스토리보드 타이틀: "스토리보드/{FeatureName}/{ScreenName}"
- CSS 변수: --color-fill-primary, --font-size-h1 (케밥)
- CVA variants: camelCase (variant, size, tone)
```

### 검증 체크리스트
```
[ ] 기존 패턴(CVA + Tailwind + Radix)과 일관성
[ ] TypeScript 타입 완전 정의
[ ] Storybook autodocs 태그 포함
[ ] 모든 variant/size 조합 스토리 포함
[ ] 상태별 스토리 (default, disabled, loading, error) 포함
[ ] 접근성 (aria-label, role 등) 적용
[ ] Figma 원본과 토큰 값 일치
[ ] 기존 export index에 추가
```

---

## 사용 예시

### 예시 1: 전체 디자인 시스템 동기화
```
사용자: "디자인 시스템 Figma 동기화해줘"
→ Mode A 실행
→ Figma 토큰 추출 → 기존 코드 비교 → 변경사항 적용
```

### 예시 2: 특정 컴포넌트 생성
```
사용자: "BottomSheet 컴포넌트 만들어줘"
→ Mode B 실행
→ Figma에서 BottomSheet 컴포넌트 찾기
→ Variants/Props 분석
→ 코드 + 스토리 생성
```

### 예시 3: PRD → 스토리보드
```
사용자: "이 기획서로 스토리보드 만들어줘" + PRD 첨부
→ Mode C 실행
→ 화면 단위 분해
→ DS 컴포넌트 매핑
→ 화면 코드 + 플로우 스토리 + README 생성
→ 개발자가 바로 작업 가능한 수준
```

### 예시 4: Figma 화면을 코드로
```
사용자: "이 Figma 화면 코드화해줘" + Figma URL
→ Mode C 실행 (Figma 참조)
→ get_design_context로 화면 구조 파악
→ DS 컴포넌트 조합으로 코드 생성
→ 상태별 Storybook 스토리
```
