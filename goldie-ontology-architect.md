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

## 참고 자료
- [인문정보학 온톨로지 설계 가이드라인](https://dh.aks.ac.kr/wiki/index.php/인문정보학_온톨로지_설계_가이드라인)
- [온톨로지 설계 방법 (DH교육용 위키)](https://dh.aks.ac.kr/Edu/wiki/index.php/온톨로지_설계_방법)
- [RAG의 한계를 Knowledge Graph로 극복하기](https://www.sotaaz.com/post/ontology-knowledge-graph-rag)
- [AI 전환에 온톨로지가 필요한 이유 (SKAI)](https://blog.skaiworldwide.com/638)
