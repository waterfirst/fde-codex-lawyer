# 일요일 2시간 워크숍 진행자 스크립트

_Codex × 법제처 MCP × 파산전문 변호사 업무 자동화_

## 목표

변호사 친구에게 “AI에게 일 시키는 법”을 2시간 안에 체감시킨다.

핵심은 코딩 교육이 아니다.  
**문제정의 → NotebookLM 문서독해 → Codex 지시 → 법제처 MCP 근거확인 → 사건 검토 패킷 생성 → GitHub 핸드오프**를 경험시키는 것이다.

## 0:00–0:15 문제정의

### 낙초가 물어볼 질문

1. 월 12건 중 가장 시간이 오래 걸리는 단계는 어디인가?
2. 사건 접수 때 항상 빠지는 자료는 무엇인가?
3. 변호사가 반드시 직접 판단해야 하는 항목은 무엇인가?
4. AI가 해도 되는 반복작업은 무엇인가?
5. 최종 산출물이 Markdown, Word, HTML 중 무엇이면 편한가?

### 말할 멘트

> 오늘 목표는 법률판단을 AI에게 넘기는 게 아니다.  
> 반복 정리 업무를 줄이고, 변호사가 판단해야 할 포인트를 더 빨리 보게 만드는 것이다.

## 0:15–0:35 NotebookLM 첫 성공

### 목적

변호사 업무의 본질은 코딩보다 문서 독해다.  
첫 성공은 Codex CLI가 아니라 NotebookLM으로 잡는다.

### 사용할 자료

- `cases/sample_001_personal_bankruptcy/input/interview/interview_note.md`
- `cases/sample_001_personal_bankruptcy/input/metadata.json`

### NotebookLM 질문

```text
이 익명 개인파산 샘플 사건에서 핵심 사실, 누락자료, 쟁점 후보, 변호사가 확인해야 할 질문을 정리해줘.
각 항목은 가능한 경우 출처 위치를 함께 표시해줘.
법률 결론은 확정하지 말고 "검토 필요" 수준으로만 표현해줘.
```

### 변호사에게 설명할 말

> NotebookLM은 눈이다. 문서를 읽고 핵심을 뽑는다.  
> Codex는 손이다. 그 결과를 파일, 보고서, 루틴으로 만든다.

## 0:35–0:50 환경 연결

### 확인

- Codex CLI 로그인
- `~/.codex/config.toml`
- `korean_law` MCP enabled
- 법제처 OpenAPI 키

### 연결 테스트 프롬프트

```text
AGENTS.md 규칙을 따른다.
korean_law MCP를 사용해 "채무자 회생 및 파산에 관한 법률"에서 개인파산과 관련된 조문을 찾아라.
조문 번호, 핵심 문장, 쉬운 설명을 짧게 정리하라.
근거를 찾지 못하면 확인 불가라고 말하라.
```

## 0:50–1:20 사건 Intake 루틴

### 목적

NotebookLM이 뽑은 사실/쟁점 후보를 Codex가 표준 산출물로 바꾸는 것을 보여준다.

### 시연

1. `prompts/01_case_intake_prompt.md` 열기
2. 샘플 사건 폴더를 입력으로 지정
3. 문서 인덱스, 누락자료, 사건 요약 생성
4. 추정하지 않고 “자료 없음/추가 확인 필요”라고 쓰는지 확인

### 실패 시 대처

- MCP 연결 실패: 법령 검색 부분은 건너뛰고 로컬 루틴/출력 구조만 보여준다.
- API 키 문제: `LAW_OC` 값 확인, 다음에 재시도.
- 검색 결과 불충분: “확인 불가”라고 나오는 것도 성공으로 설명한다. 환각 방지이기 때문.

## 1:20–1:45 토탈 검토 패킷

### 사용할 샘플

`cases/sample_001_personal_bankruptcy/input/`

### 실행 프롬프트

`prompts/04_full_orchestration_prompt.md` 사용

### 변호사에게 보여줄 포인트

- 파일명 정리
- 누락자료 자동 발견
- 기본 사실 요약
- 추정하지 않고 `자료 없음` 처리

### 목표 산출물

- `output/01_case_summary.md`
- `output/02_issue_checklist.md`
- `output/03_draft_report.md`
- `output/04_evidence_table.csv`
- `output/05_questions_for_lawyer.md`
- `output/review_packet.html`

### 강조할 점

> AI가 결론을 내는 게 아니라, 변호사가 빨리 판단하도록 사건을 정리한다.

## 1:45–2:00 핸드오프

### 변호사에게 남길 것

1. GitHub Pages URL
2. README 재실행법
3. AGENTS.md 안전 규칙
4. SKILL.md 사건 처리 절차
5. prompts 복붙 파일
6. 다음 실제 파일럿 1건 선정

### 마무리 멘트

> 오늘 만든 건 완성품이 아니라 첫 번째 운영 루틴이다.  
> 다음 단계는 실제 익명 사건 1건으로 처리시간과 수정량을 재는 것이다.

## FDE 면접용 기록 포인트

- 고객: 파산전문 변호사
- 문제: 월 12건 문서 검토 반복업무
- 접근: 현업 인터뷰 → 업무분해 → MCP 근거 연결 → Codex 오케스트레이션
- 산출물: GitHub Pages, AGENTS, SKILL, prompts, 샘플 사건 구조
- 안전: 개인정보, 법률단정, 근거 없는 주장 차단
- 성공지표: 처리시간, 누락자료 발견률, 변호사 수정량, 재사용률
