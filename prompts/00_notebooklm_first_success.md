# 루틴⓪ Python 로컬 리더 우선 + NotebookLM 선택 옵션

목적: 변호사 업무의 핵심인 **문서 읽기와 핵심 파악**을 가장 먼저 성공시킨다.

기본 도구: Python local reader  
선택 도구: NotebookLM/Gemini  
사용 자료: 실제 사건은 변호사 노트북 안에서만 처리한다. NotebookLM/Gemini는 익명 샘플 또는 완전 마스킹 자료에만 쓴다.

## Python 로컬 리더 실행

```bash
python3 scripts/local_doc_intake.py \
  cases/sample_001_personal_bankruptcy/input \
  --out cases/sample_001_personal_bankruptcy/output/local_intake
```

생성물:

- `case_intake.json`
- `document_index.csv`
- `redacted_text.md`
- `README_FOR_CODEX.md`

## NotebookLM에 붙여넣을 질문

아래 질문은 **익명 샘플 또는 완전 마스킹 자료에만** 사용한다.

아래 사건 자료를 변호사 검토 보조 관점에서 정리해줘.

반드시 지켜라:
- 법률 결론을 확정하지 말 것
- 모르는 사실은 추정하지 말 것
- 답변마다 가능한 출처 문서/문단을 붙일 것
- 개인정보, 주민등록번호, 계좌번호, 주소 원문은 출력하지 말 것
- 이 결과는 변호사 검토용 초안임을 명시할 것

출력 형식:

1. 사건 한 줄 요약
2. 핵심 사실 10개
3. 금액·날짜·채권자·재산 관련 항목
4. 누락자료 목록
5. 개인파산/개인회생 쟁점 후보
6. 이상거래·재산누락·편파변제 의심 포인트
7. 변호사가 의뢰인에게 물어볼 질문 10개
8. 근거가 약하거나 추가 확인이 필요한 주장

## Codex로 넘길 때

Python 로컬 리더 결과 또는 NotebookLM 결과를 그대로 믿지 말고, Codex에게 다음처럼 지시한다.

```text
AGENTS.md와 SKILL.md를 먼저 읽어라.
Python 로컬 리더가 만든 local_intake 결과를 기준으로 하라.
NotebookLM/Gemini 결과가 있으면 참고만 하고, 확정 사실로 단정하지 마라.
cases/sample_001_personal_bankruptcy/input/ 자료와 대조하여
document_index.csv, missing_documents.md, 01_case_summary.md,
issues_for_lawyer.md 초안을 만들어라.
법률 판단 확정 금지, 개인정보 원문 출력 금지.
```
