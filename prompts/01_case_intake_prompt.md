# Prompt 01 — 사건 Intake

```text
Goal: 개인파산/개인회생 사건 1건의 입력자료를 정리한다.

Input:
- cases/YYYY/YYYY-MM-NNN_case_slug/input/raw_pdfs/
- cases/YYYY/YYYY-MM-NNN_case_slug/input/interview/
- cases/YYYY/YYYY-MM-NNN_case_slug/input/metadata.json

Output:
- working/document_index.csv
- output/01_case_summary.md 초안
- output/missing_documents.md
- audit/run_log.md

Constraints:
- 개인정보 전체 출력 금지
- 원본 파일 수정 금지
- 추정 금지, 자료 없으면 "자료 없음"
- 법률 판단 금지

Steps:
1. 파일 목록을 만든다.
2. 문서 유형을 분류한다.
3. 필수자료 누락 여부를 표시한다.
4. 사건 기본정보를 익명화해 요약한다.
5. 다음 루프에서 확인할 질문을 만든다.

Stop condition:
- document_index.csv 존재
- missing_documents.md 존재
- 개인정보 직접 노출 없음
```

