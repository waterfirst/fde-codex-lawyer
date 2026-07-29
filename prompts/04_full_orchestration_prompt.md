# Prompt 04 — 전체 오케스트레이션 실행

```text
Goal:
개인파산/개인회생 익명 사건 1건을 변호사 검토용 1차 패킷으로 정리한다.

Input:
cases/sample_001_personal_bankruptcy/input/

Output:
cases/sample_001_personal_bankruptcy/output/
- 01_case_summary.md
- 02_issue_checklist.md
- 03_draft_report.md
- 04_evidence_table.csv
- 05_questions_for_lawyer.md
- review_packet.html

Constraints:
- AGENTS.md와 SKILL.md를 먼저 읽고 따른다.
- 법률 판단 확정 금지.
- 개인정보 원문 출력 금지.
- 법령 근거는 가능한 경우 korean_law MCP로 확인한다.
- 근거 없는 문장은 unsupported_claims.md에 분리한다.
- 원본 파일은 수정하지 않는다.
- 추정 금지. 자료가 없으면 "자료 없음" 또는 "추가 확인 필요"라고 쓴다.

Steps:
1. Intake Worker:
   - 입력 파일 목록을 만들고 문서 유형을 분류한다.
   - 누락자료를 표시한다.
2. Extraction Worker:
   - 상담 메모와 metadata에서 날짜, 금액, 채권자, 재산, 소득, 가족관계 후보를 뽑는다.
3. Screening Worker:
   - 가족 간 이체, 편파변제, 재산 처분, 보험, 차량, 부동산, 사업자산, 진술 불일치 후보를 탐지한다.
4. Legal Grounding Worker:
   - 관련 법령 근거를 korean_law MCP로 확인한다.
   - 조문을 못 찾으면 확인 불가라고 쓴다.
5. Draft Worker:
   - 사건 요약과 초안 보고서를 작성한다.
6. Evidence Worker:
   - 주요 문장마다 입력자료 근거를 연결한다.
   - 근거 부족은 audit/unsupported_claims.md에 분리한다.
7. Review Worker:
   - 개인정보 노출과 법률 단정 표현을 점검한다.
   - 변호사에게 물어볼 질문 5~10개를 만든다.

Stop condition:
- output 6개 파일이 존재한다.
- audit/run_log.md가 존재한다.
- 금지 표현이 없다.
- 변호사 질문 5개 이상이 있다.
- 마지막에 "본 내용은 초안이며 변호사의 검토·판단이 필요합니다"를 명시한다.
```

