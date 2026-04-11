# 화면 코드 패턴

## 표준 레이아웃 (모바일 퍼스트)

```tsx
export function ScreenName({ data, isLoading, error }: ScreenNameProps) {
  if (isLoading) return <ScreenNameSkeleton />;
  if (error) return <ScreenNameError error={error} onRetry={refetch} />;
  if (!data || data.length === 0) return <ScreenNameEmpty />;

  return (
    <div className="flex flex-col min-h-dvh bg-bg-default">
      <NavigationHeader variant="default" title="화면 제목"
        trailing={<IconButton icon={<SettingsIcon />} />} />

      <main className="flex-1 overflow-y-auto">
        <section className="px-5 py-4">
          <h2 className="text-h2-bold text-text-primary mb-3">섹션 제목</h2>
        </section>
        <div className="h-2 bg-bg-secondary" />  {/* 구분선 */}
        <section className="px-5 py-4">{/* ... */}</section>
      </main>

      <footer className="sticky bottom-0 px-5 pb-8 pt-3 bg-bg-default border-t border-line-default">
        <AtomicButton variant="primary" size="xlarge" className="w-full">다음</AtomicButton>
      </footer>
    </div>
  );
}
```

## 상태 컴포넌트

```tsx
// 스켈레톤
function ScreenNameSkeleton() {
  return (
    <div className="flex flex-col min-h-dvh bg-bg-default">
      <NavigationHeader variant="default" title="" />
      <main className="flex-1 px-5 py-4 space-y-4">
        <div className="h-6 w-32 bg-fill-grayscale-100 rounded-8 animate-pulse" />
        <div className="h-24 bg-fill-grayscale-100 rounded-16 animate-pulse" />
      </main>
    </div>
  );
}

// 에러
function ScreenNameError({ error, onRetry }: { error: string; onRetry: () => void }) {
  return (
    <div className="flex flex-col min-h-dvh bg-bg-default">
      <NavigationHeader variant="default" title="오류" />
      <main className="flex-1 flex flex-col items-center justify-center px-5">
        <DsIcon name="cautionary" size={48} className="text-text-tertiary mb-4" />
        <p className="text-b1-regular text-text-secondary text-center mb-6">{error}</p>
        <AtomicButton variant="secondary" size="medium" onClick={onRetry}>다시 시도</AtomicButton>
      </main>
    </div>
  );
}

// 빈 상태
function ScreenNameEmpty() {
  return (
    <div className="flex flex-col min-h-dvh bg-bg-default">
      <NavigationHeader variant="default" title="화면 제목" />
      <main className="flex-1 flex flex-col items-center justify-center px-5">
        <DsIcon name="empty" size={64} className="text-text-quaternary mb-4" />
        <p className="text-b1-regular text-text-tertiary text-center">아직 데이터가 없어요</p>
      </main>
    </div>
  );
}
```

## 카드

```tsx
function InfoCard({ title, value, unit, trend }: InfoCardProps) {
  return (
    <div className="p-4 bg-bg-default rounded-16 border border-line-default">
      <p className="text-caption-medium text-text-tertiary mb-1">{title}</p>
      <div className="flex items-baseline gap-1">
        <span className="text-h1-bold text-text-primary">{value}</span>
        <span className="text-b3-regular text-text-secondary">{unit}</span>
      </div>
      {trend && (
        <p className={cn("text-caption-medium mt-1",
          trend > 0 ? "text-status-positive" : "text-status-negative")}>
          {trend > 0 ? "+" : ""}{trend}%
        </p>
      )}
    </div>
  );
}
```

## 리스트 아이템

```tsx
function ListItem({ title, subtitle, trailing, onClick }: ListItemProps) {
  return (
    <button className="flex items-center w-full px-5 py-3.5 gap-3 active:bg-bg-secondary transition-colors"
      onClick={onClick}>
      <div className="flex-1 min-w-0">
        <p className="text-b2-semibold text-text-primary truncate">{title}</p>
        {subtitle && <p className="text-caption-regular text-text-tertiary mt-0.5">{subtitle}</p>}
      </div>
      {trailing ?? <DsIcon name="allow" size={18} className="text-text-quaternary" />}
    </button>
  );
}
```

## 바텀시트

```tsx
function BottomSheet({ isOpen, onClose, title, children }: BottomSheetProps) {
  return (
    <DsMotion preset="sheetSnap">
      {isOpen && (
        <>
          <div className="fixed inset-0 bg-black/40 z-40" onClick={onClose} />
          <div className="fixed bottom-0 inset-x-0 bg-bg-default rounded-t-20 z-50 max-h-[80vh]">
            <div className="flex justify-center pt-2 pb-4">
              <div className="w-9 h-1 bg-fill-grayscale-200 rounded-999" />
            </div>
            {title && <div className="px-5 pb-4"><h3 className="text-h2-bold text-text-primary">{title}</h3></div>}
            <div className="overflow-y-auto px-5 pb-8">{children}</div>
          </div>
        </>
      )}
    </DsMotion>
  );
}
```

## Storybook 화면 스토리

```tsx
import type { Meta, StoryObj } from "@storybook/react";
import { ScreenName } from "./ScreenName";
import { mockData, emptyData } from "../mocks";

const meta: Meta<typeof ScreenName> = {
  title: "스토리보드/{FeatureName}/{ScreenName}",
  component: ScreenName,
  parameters: { layout: "fullscreen", viewport: { defaultViewport: "mobile1" } },
};
export default meta;
type Story = StoryObj<typeof ScreenName>;

export const Default: Story = { args: { data: mockData } };
export const Loading: Story = { args: { isLoading: true } };
export const Error: Story = { args: { error: "네트워크 연결을 확인해주세요" } };
export const Empty: Story = { args: { data: emptyData } };
```

## 금지

- min-h-screen → min-h-dvh (iOS safe area)
- 하드코딩 색상(#hex)/폰트(px) → 토큰 유틸리티
- API 호출 코드 → mock 데이터 대체
- 비즈니스 로직 → UI 구조만
