---
name: goldie-design-system
description: >
  금골디 디자인 시스템 라이브러리. DS 토큰/컴포넌트/프로덕션 화면 레퍼런스를 제공한다.
  goldie-screen-builder 에이전트가 이 스킬의 references/를 참조하여 디자인을 생성한다.
  트리거: 디자인시스템, 스토리북, 스토리보드, 컴포넌트 생성, 토큰 추출,
  Figma 코드화, 화면정의서, 기능정의서, PRD 코드화, DS 동기화.
---

# Goldie Design System Library

## 참조 파일 구조 (필요한 것만 Read)

```
references/
├── tokens.md                     # DS 전체 토큰 + 컴포넌트 스펙
│   ├── Color (Atomic + Semantic)
│   ├── Typography (D1~Caption, 33 styles)
│   ├── Spacing (0~60px, 11 steps)
│   ├── Radius (0~999px, 7 steps)
│   ├── Divider (1/2/8px)
│   ├── Shadow (normal/strong/heavy)
│   ├── Opacity (dim/toast)
│   ├── Atomic Button (5 size × 4 variant)
│   ├── Text Field (2 size × 3 variant × 5 state)
│   ├── Popup/Basic + BottomSheet
│   ├── Toast (4 variant)
│   ├── Tooltip (6 position)
│   ├── Header (4 variant + header set)
│   ├── Bottom Navigation B2C/B2B
│   └── Tab + Category
│
├── env.md                        # Figma keys, 기술스택, 모노레포 구조
├── component-codegen.md          # CVA + Radix 코드 생성 패턴
├── screen-patterns.md            # 화면 코드 패턴 (tsx + Storybook)
│
└── screens/                      # 프로덕션 화면 레퍼런스
    ├── home.md                   # 홈 화면 구조
    └── my-vault.md               # MY금고 홈 구조
```

## 로드 규칙

| 작업 | 로드할 파일 |
|------|-----------|
| 화면 디자인 (Stitch) | env.md + tokens.md + screens/{관련}.md + ~/.goldie/stitch-ds-prompt.md |
| 컴포넌트 생성 | env.md + tokens.md + component-codegen.md |
| 코드 출력 | 위 + screen-patterns.md |
| 토큰 동기화 | env.md + tokens.md |

## Stitch MCP 연동 (화면 디자인 필수)

화면 디자인 작업 시 **반드시 Stitch MCP를 먼저 호출**하여 AI 디자인을 생성한다.
Stitch가 시각적 완성도(레이아웃, 비율, 여백감)를 잡고, DS 토큰으로 정밀 보정하는 2단계 워크플로우.

```
Stitch 프롬프트 = DS 스펙(~/.goldie/stitch-ds-prompt.md) + 기획서 요구사항
→ generate_screen_from_text → fetch_screen_image/code
→ Figma MCP로 DS 토큰 정밀 적용
```

## Figma MCP 연동

```yaml
ds_file_key: nb3vl6A5oOBjV5yW7XprRr
prod_file_key: EH0KGqF7rGyFIxwXETiXX5

# 텍스트 스타일 적용 (포크 플러그인 필요)
set_text_style_id(nodeId, styleKey)  # importStyleByKeyAsync로 라이브러리 스타일 import

# 컬러 변수 바인딩
apply_variable_to_node(nodeId, variableKey, "fills/0/color")  # importVariableByKeyAsync

# DS 컴포넌트 clone (통합 피그마에서)
clone_node(nodeId) → insert_child(parentId, childId)
```

## DS 라이브러리 핵심 원칙

1. **시맨틱 토큰만 사용** — atomic 색상 직접 사용 금지
2. **텍스트 스타일 바인딩** — 수동 fontSize/fontWeight 설정 금지
3. **4배수 간격** — spacing 토큰 외 값 사용 최소화
4. **컴포넌트 재사용** — 수동 프레임 생성 최소화, DS 컴포넌트 clone 우선

## 작업 프로세스

DS/Figma 변경 작업은 `memory/feedback_figma-design-rules.md` A섹션을 따른다.
- **A-1 계획 보고**: 생성 전 Before/After + 토큰 사용 계획 필수
- **A-2 완료 검증**: 하드코딩/토큰 동기화/컴포넌트 재사용 체크
- **A-3 금지**: 무단 컴포넌트 생성, 범위 밖 리팩토링, 토큰 없는 스타일링
