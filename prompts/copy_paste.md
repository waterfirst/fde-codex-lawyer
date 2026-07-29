# 복붙용 프롬프트 (실습 중 바로 사용)

## 루틴⓪ NotebookLM 첫 성공
아래 익명 샘플 사건 자료를 읽고, 변호사 검토용으로 정리해줘.

주의:
- 법률 결론을 확정하지 말 것
- 모르는 내용은 추정하지 말 것
- 답변마다 가능한 출처 문서/문단을 붙일 것
- 실제 의뢰인 개인정보가 아니라 익명 샘플이라는 전제로만 처리할 것

출력:
1. 핵심 사실 10개
2. 누락자료 목록
3. 개인파산/개인회생 쟁점 후보
4. 이상거래·재산누락 의심 포인트
5. 변호사가 의뢰인에게 물어볼 질문 10개

## 연결 확인
개인정보보호법 제15조를 korean_law MCP로 찾아서 조문 원문과 쉬운 설명을 함께 보여줘.

## 루틴① 법령 Q&A
AGENTS.md 규칙을 따른다. 다음 질문에 korean_law MCP로 관련 법령을 검색해
결론 → 근거 조문(조·항·호) → 쉬운 설명 → 예외 → 면책 순으로 답하라.
질문: "____"

## 루틴② 개정 모니터
AGENTS.md를 따른다. korean_law MCP로 [개인정보보호법, 전자상거래법]의 최신 시행일·개정이력을 조회하고,
YYYY-MM-DD 이후 변경 조문을 '법령/조문/변경내용/실무영향'으로 요약해 amendment_report.md로 저장하라.

## 루틴③ 자문 메모
AGENTS.md를 따른다. 아래 익명 사안에 대해 관련 법령·판례를 korean_law MCP로 조회하고
자문 메모 초안을 advisory_memo.html로 작성하라(사실관계/쟁점/법령/판례/의견/면책).
사안: "____"

## 루틴④ 개인파산/개인회생 사건 Intake
AGENTS.md와 SKILL.md를 먼저 읽어라.
cases/sample_001_personal_bankruptcy/input/ 자료를 기준으로 사건 1건의 Intake를 수행하라.
원본 파일은 수정하지 말고, document_index.csv, missing_documents.md, 01_case_summary.md 초안을 만들어라.
개인정보와 법률 판단 확정 표현은 금지한다.

## 루틴⑤ 전체 오케스트레이션
AGENTS.md와 SKILL.md를 먼저 읽어라.
prompts/04_full_orchestration_prompt.md의 지시대로 cases/sample_001_personal_bankruptcy 사건을 처리하라.
목표는 변호사 검토용 1차 패킷이다.
법률 판단 확정 금지, 개인정보 원문 출력 금지, 근거 없는 문장은 unsupported_claims.md로 분리하라.
