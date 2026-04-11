# 컴포넌트 코드 생성 규칙

## CVA 컴포넌트 패턴

```tsx
import { cva, type VariantProps } from "class-variance-authority";
import { cn } from "@goldie/util";
import { forwardRef } from "react";

const componentVariants = cva(
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
    defaultVariants: { variant: "primary", size: "medium" },
  }
);

export interface ComponentNameProps
  extends React.HTMLAttributes<HTMLElement>,
    VariantProps<typeof componentVariants> {}

const ComponentName = forwardRef<HTMLElement, ComponentNameProps>(
  ({ className, variant, size, ...props }, ref) => (
    <element
      ref={ref}
      className={cn(componentVariants({ variant, size }), className)}
      {...props}
    />
  )
);
ComponentName.displayName = "ComponentName";
export { ComponentName, componentVariants };
```

## Storybook 스토리 패턴

```tsx
import type { Meta, StoryObj } from "@storybook/react";
import { ComponentName } from "./ComponentName";

const meta: Meta<typeof ComponentName> = {
  title: "공통 컴포넌트/ComponentName",
  component: ComponentName,
  tags: ["autodocs"],
  argTypes: {
    variant: { control: "select", options: ["primary", "secondary"] },
    size: { control: "select", options: ["large", "medium", "small"] },
  },
};
export default meta;
type Story = StoryObj<typeof ComponentName>;

export const Default: Story = { args: { children: "텍스트" } };

export const AllVariants: Story = {
  render: () => (
    <div className="flex flex-col gap-4">
      <ComponentName variant="primary">Primary</ComponentName>
      <ComponentName variant="secondary">Secondary</ComponentName>
    </div>
  ),
};
```

## 파일 구조

```
packages/design-system/src/components/{Name}/
├── {Name}.tsx            # 컴포넌트
├── {Name}.stories.tsx    # 스토리
└── index.ts              # re-export
```

## Figma → 컴포넌트 분석 절차

```
1. get_design_context → Variants/Props/스크린샷 추출
2. get_context_for_code_connect → property definitions, variant options
3. 기존 AtomicButton.tsx를 gh api로 Read → 패턴 일치 확인
4. CVA variants 매핑 → 코드 생성
```

## 금지

- CSS-in-JS, CSS Modules 사용 금지
- 기존 4개 컴포넌트 수정 금지
- Radix UI 프리미티브가 devDependency에 있으면 래핑할 것
