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

## 참조 파일 (필요한 것만 Read)

| 파일 | 내용 | 로드 시점 |
|------|------|----------|
| `references/env.md` | Figma keys, 기술스택, 기존 컴포넌트, 모노레포 구조 | 항상 |
| `references/tokens.md` | 토큰 체계 (color/typo/radius) + Tailwind 매핑 + CSS 생성 규칙 | Mode A, B, C |
| `references/component-codegen.md` | CVA 컴포넌트 + Storybook 스토리 코드 패턴 | Mode B |
| `references/screen-patterns.md` | 화면 레이아웃/상태/카드/리스트/바텀시트/스토리 패턴 | Mode C |

---

## Mode A: `figma-sync` — Figma → 코드 동기화

**트리거**: "디자인 시스템 동기화", "토큰 추출", "컬러 업데이트"

**로드**: `references/env.md` + `references/tokens.md`

**절차**:
1. Figma MCP(`get_design_context`, `get_variable_defs`)로 토큰 추출
2. `gh api`로 기존 `packages/theme/*.css` 읽기
3. 변경사항 비교 → 기존 파일 업데이트 (Tailwind v4 `@theme inline`, `@utility` 문법)
4. 결과 리포트 (추가/수정/신규 파일)

---

## Mode B: `component-gen` — 컴포넌트 코드 생성

**트리거**: "Button 만들어줘", "BottomSheet 코드화", "컴포넌트 Storybook"

**로드**: `references/env.md` + `references/tokens.md` + `references/component-codegen.md`

**절차**:
1. Figma MCP로 대상 컴포넌트 Variants/Props 추출
2. `gh api`로 기존 `AtomicButton.tsx` 패턴 확인 (1회)
3. CVA + Radix + tailwind-merge 패턴으로 코드 생성
4. Storybook 스토리 (autodocs, variant별, 상태별) 생성
5. 기존 export index에 추가

---

## Mode C: `storyboard` — PRD → 스토리보드 생성

**트리거**: "기획서 코드화", "PRD 스토리보드", "화면 만들어줘"

**로드**: `references/env.md` + `references/tokens.md` + `references/screen-patterns.md`

**절차**:
1. PRD에서 화면 단위 분해 (화면명, 기능, 플로우, 상태 분기)
2. DS 컴포넌트 매핑 (기존 우선, 없으면 Mode B 제안)
3. Figma 있으면 `get_design_context`로 레이아웃 참조
4. 화면 코드 + Storybook 스토리 + README 생성

**출력 구조**:
```
{feature}/
├── README.md              # 개요 + Mermaid 플로우 + API/상태관리/라우팅 가이드
├── screens/{Screen}.tsx   # 화면 (DS 조합, 상태별 분기)
├── screens/{Screen}.stories.tsx  # 스토리 (default/loading/error/empty)
├── components/            # 기능 전용 서브 컴포넌트
├── flow.stories.tsx       # 전체 플로우 스토리
├── types.ts + mocks.ts
```

---

## 공통 규칙

### Figma MCP 접근
```
fileKey: nb3vl6A5oOBjV5yW7XprRr (DS)
fileKey: EH0KGqF7rGyFIxwXETiXX5 (통합 피그마)

get_metadata → get_design_context → get_screenshot
get_variable_defs (토큰) / get_context_for_code_connect (컴포넌트)
search_design_system (에셋 검색)
```

### 기존 코드 참조
```bash
# 컴포넌트 패턴
gh api repos/goldncompany/goldie_frontend/contents/packages/design-system/src/components/AtomicButton/AtomicButton.tsx -H "Accept: application/vnd.github.raw+json"
# 토큰
gh api repos/goldncompany/goldie_frontend/contents/packages/theme/color.css -H "Accept: application/vnd.github.raw+json"
```

### 네이밍
- 컴포넌트/파일: PascalCase
- 스토리 타이틀: `"공통 컴포넌트/{Name}"` 또는 `"스토리보드/{Feature}/{Screen}"`
- CSS 변수: 케밥 (`--color-fill-primary`)
- CVA variants: camelCase

### 검증
- [ ] 기존 CVA+Tailwind+Radix 패턴 일관성
- [ ] TypeScript 타입 완전 정의
- [ ] Storybook autodocs + 모든 variant/상태 스토리
- [ ] Figma 원본과 토큰 값 일치
- [ ] 접근성 (aria-label, role)
