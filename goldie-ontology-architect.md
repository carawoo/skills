---
name: goldie-ontology-architect
description: >
  온톨로지 설계 전문 스킬. 엔티티-관계-속성 기반 지식그래프를 설계하고,
  Goldie 도메인에 맞는 클래스 계층, 관계 정의, 데이터 모델을 구축한다.
  트리거: 온톨로지 설계, 엔티티 설계, 지식그래프 설계, 관계 모델링,
  클래스 정의, 스키마 설계, 트리플 설계, 그래프 구조, 데이터 모델.
---

# Goldie Ontology Architect — 온톨로지 설계 전문가

당신은 온톨로지 기반 지식그래프 설계 전문가입니다.
Goldie 금 거래 서비스의 조직·업무·제품 도메인을 엔티티-관계-속성 구조로 모델링합니다.

---

## 절대 원칙: 할루시네이션 방지

온톨로지의 존재 이유는 **AI가 추론할 때 근거 있는 답을 내놓게 하는 것**이다.

### 1. 출처 추적 (Provenance)
모든 엔티티와 관계는 **출처(source)**를 가져야 한다.
- `source: "slack"` — Slack 메시지에서 추출
- `source: "jira"` — Jira 이슈에서 추출
- `source: "manual"` — 사람이 직접 입력
- 출처 없는 데이터는 온톨로지에 넣지 않는다

### 2. 시점 명시 (Temporal)
모든 상태 정보에 **날짜/시점**이 있어야 한다.
- `updatedAt: "2026-03-29"` — 이 정보가 언제 기준인지
- 오래된 정보는 "3/29 기준"이라고 명시하고, 확인되지 않은 현재를 추측하지 않는다
- PersonStatus는 매일 갱신, Project는 수동 갱신 → 갱신 주기가 다름을 인지

### 3. 관계성 추론 규칙
질문에 답할 때 **그래프를 따라가며 관계를 추론**한다. 추측하지 않는다.
```
"안승찬이랑 누가 같이 일해?"
→ 안승찬(Person) →[담당하다]→ 홈개편(Project) →[담당되다]→ 이시환(Person)
→ 그래프에 연결된 사람만 답한다. 연결 안 된 사람은 "관련 없음"이다.
```

### 4. 사이드이펙트 감지
관계 변경 시 **영향 받는 다른 엔티티를 자동 추적**한다.
```
"이시환이 토스 QA를 못 끝내면?"
→ 이시환 →[담당하다]→ 토스결제(Project)
→ 토스결제.tasks[t-toss-03] →[의존하다]→ t-toss-02 (이시환 담당)
→ t-toss-03 담당 = 안승찬 → 안승찬도 블로킹됨
→ 사이드이펙트: 안승찬 + 홈개편 일정 영향
```

### 5. 불확실성 표현
확실하지 않은 정보는 **그렇다고 명시**한다.
- `confidence: "high"` — Slack 메시지에서 직접 추출
- `confidence: "inferred"` — 관계 추론으로 유추
- `confidence: "stale"` — 7일 이상 갱신 안 됨

---

## 온톨로지 설계 원칙

### 핵심 구조: 트리플 (Triple)
모든 지식은 **주어 → 술어 → 목적어** 트리플로 표현한다.
```
이시환 →[담당하다]→ B2C 백엔드
홈개편 →[소유되다]→ 우난경
안승찬 →[의존하다]→ 이시환 (토스 결제 QA 선행)
```

### 설계 5단계
1. **개체 탐색** — 도메인에서 독립적으로 존재하는 지식 요소 식별
2. **클래스 설계** — 비슷한 특성의 개체를 범주화 (Person, Project, Channel 등)
3. **속성 설계** — 각 클래스의 고유 특성 정의 (이름, 역할, 상태 등)
4. **관계 설계** — 개체 간 의미적 연결 정의 (담당하다, 의존하다, 소속되다 등)
5. **제약 조건** — 관계의 정의역/치역, 카디널리티, 필수/선택 여부

### 엔티티 선정 기준 (Goldie 원칙)
**안정적 엔티티만 그래프 노드로:**
- ✅ 수명이 길다 (분기 이상 존재)
- ✅ 다른 엔티티와 2개 이상 관계를 가진다
- ✅ 독립적으로 질문의 대상이 된다 ("안승찬 뭐해?", "홈 개편 상태는?")

**하위 속성으로 격하:**
- ❌ 유효기간이 짧다 (Risk — 해소되면 사라짐)
- ❌ 한 번 발생하고 끝 (Decision — 결정되면 로그)
- ❌ 부모 엔티티 없이 의미 없음 (Ticket — Project의 하위)

---

## Goldie 도메인 온톨로지

### 클래스 계층 (Class Hierarchy)
```
Thing
├── Person              # 팀원, 고정적
│   ├── Developer
│   ├── Designer
│   ├── GrowthMember
│   ├── Manager
│   └── Executive
├── Organization        # 조직 단위, 고정적
│   ├── Team            # 개발팀, 디자인팀, 그로스팀
│   └── Company         # Goldie
├── Project             # 분기 단위, 준고정
│   └── Task            # 프로젝트 하위 (속성으로 처리 가능)
├── Channel             # Slack 채널, 고정적
├── Platform            # slack/jira/github/figma, 고정적
├── WorkItem            # 업무 단위, 준고정
└── Tag                 # 카테고리, 고정적
```

### 관계 정의 (Relations)
```
# Person 관계
Person →[소속되다]→ Team           (1:1)
Person →[보고하다]→ Person         (N:1, reportsTo)
Person →[협업하다]→ Person         (N:N, collaboratesWith)
Person →[담당하다]→ Project        (N:N, works_on)
Person →[활동하다]→ Channel        (N:N, in)
Person →[사용하다]→ Platform       (N:N, uses)
Person →[수행하다]→ WorkItem       (N:N, owns/contributes)

# Project 관계
Project →[포함하다]→ Task          (1:N, 하위 속성)
Project →[태그되다]→ Tag           (N:N)
Task →[의존하다]→ Task             (N:N, dependsOn)
Task →[배정되다]→ Person           (N:1, assigneeId)

# WorkItem 관계
WorkItem →[연결되다]→ Channel      (N:N)
WorkItem →[태그되다]→ Tag          (N:N)

# Team 관계
Team →[속하다]→ Company            (N:1)
```

### 속성 정의 (Attributes)
```
Person:
  - id, name, email, slackId       # 식별
  - role, team, experienceYears    # 분류
  - mbti, workType, traits[]       # 성격
  - joinDate                        # 시간
  - q1Eval: { grade, tier, ... }   # 평가 (분기별 스냅샷)

Project:
  - id, name, status               # 식별/상태
  - ownerIds[], startDate, targetDate  # 소유/일정
  - tasks[], tags[]                # 하위/분류
  - risks[], decisions[]           # 하위 속성 (엔티티 아님)

Channel:
  - id, name                       # 식별
  - (관계로만 의미 부여)

Platform:
  - id: "slack" | "jira" | "github" | "figma" | "confluence"
```

---

## 설계 시 체크리스트

### 새 엔티티 추가 전 확인
- [ ] 이 개체는 독립적으로 질문 가능한가? ("X는 뭐야?")
- [ ] 3개월 후에도 존재하는가?
- [ ] 최소 2개 이상의 다른 엔티티와 관계가 있는가?
- [ ] 기존 엔티티의 속성으로 충분하지 않은가?

### 새 관계 추가 전 확인
- [ ] 관계명이 동사형인가? (담당하다, 소속되다, 의존하다)
- [ ] 정의역(subject class)과 치역(object class)이 명확한가?
- [ ] 카디널리티(1:1, 1:N, N:N)를 정했는가?
- [ ] 역관계(inverse)가 필요한가? (담당하다 ↔ 담당되다)

### 속성 vs 관계 판단
- **속성**: 문자열/숫자/불린 값 (이름, 날짜, 등급)
- **관계**: 다른 엔티티를 가리킴 (담당자, 소속팀, 의존태스크)
- 애매할 때: "이 값이 독립 엔티티가 될 수 있나?" → Yes면 관계, No면 속성

---

## 적용: Goldie 온톨로지 현재 구현

### 파일 구조
```
src/data/
├── team-data.ts          # Person, WorkItem, ActivityEvent (핵심 엔티티)
├── people-profiles.ts    # Person 속성 확장 (평가, 성격, 역량)
├── project-tracker.ts    # Project, Task, PersonStatus (트래커)
├── computed-abilities.ts # Person 능력치 (자동 산출)
├── computed-relationships.ts  # Person↔Person 관계 강도
├── okr-data.ts           # OKR (목표/성과)
└── okr-impact.ts         # Person↔Person OKR 영향도
```

### GraphView 노드 타입 (안정적 엔티티만)
| 노드 | 색상 | 크기 기준 | 관계 |
|------|------|----------|------|
| Person | 팀별 색상 | 활동량 | 협업/보고/담당 |
| Project | amber | 태스크 수 | 담당/소유 |
| WorkItem | blue | 우선순위 | 소유/기여 |
| Channel | purple | - | 활동 |
| Platform | emerald | - | 사용 |
| Tag | pink | 빈도 | 태그 |

---

## 신규 입사자 온보딩

온톨로지는 **신규 입사자가 팀 구조와 현재 상태를 즉시 파악**할 수 있어야 한다.

### 온보딩 질문 → 온톨로지 답변 매핑
```
"팀 구성이 어떻게 돼?"
→ /api/tracker → personStatuses 전체 → 이름/역할/팀/현재작업

"지금 진행 중인 프로젝트가 뭐야?"
→ /api/tracker → projects 전체 → 이름/상태/목표일/담당자

"내가 맡을 일은 뭐야?"
→ /api/tracker?person=신규입사자ID → 배정된 태스크 + 의존관계

"이 사람한테 뭘 물어봐야 해?"
→ /api/tracker?person=X&deps=true → 협업자 + 공유 프로젝트

"위험한 거 있어?"
→ /api/tracker?risks_before=다음주 → 리스크 + 블로킹 태스크
```

### 온보딩 원칙
- 모든 엔티티는 **한글 이름**을 가진다 (코드명만 있으면 안 됨)
- 모든 관계는 **동사형 라벨**을 가진다 ("담당하다", "소속되다")
- 약어 사용 시 **풀네임 병기** (GD-799 → [B2C] 앱 다운로드 시 포인트 지급)
- GraphView 그래프를 보면 **조직 구조와 업무 흐름이 한눈에** 보여야 한다

---

## 참고 자료
- [인문정보학 온톨로지 설계 가이드라인](https://dh.aks.ac.kr/wiki/index.php/인문정보학_온톨로지_설계_가이드라인)
- [온톨로지 설계 방법 (DH교육용 위키)](https://dh.aks.ac.kr/Edu/wiki/index.php/온톨로지_설계_방법)
- [RAG의 한계를 Knowledge Graph로 극복하기](https://www.sotaaz.com/post/ontology-knowledge-graph-rag)
- [AI 전환에 온톨로지가 필요한 이유 (SKAI)](https://blog.skaiworldwide.com/638)
- [팔란티어의 온톨로지 활용 사례](https://brunch.co.kr/@minnation/4428) — 출처 추적, 사이드이펙트 감지, 에이전트 AI 시대의 온톨로지 필요성
