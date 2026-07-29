# Prompt 03 — 변호사 검토 패킷 생성

```text
Goal: 변호사가 10분 안에 사건 상태를 파악할 수 있는 검토 패킷을 만든다.

Input:
- output/01_case_summary.md
- output/02_issue_checklist.md
- output/legal_basis.md
- output/04_evidence_table.csv
- audit/unsupported_claims.md

Output:
- output/05_questions_for_lawyer.md
- output/review_packet.html

Constraints:
- 법률 판단 확정 금지
- 개인정보 원문 노출 금지
- 근거 없는 주장은 따로 표시
- 변호사 결정 필요 항목을 맨 위에 배치

Steps:
1. 사건 요약 5줄
2. 핵심 쟁점 후보 5개 이하
3. 누락자료 목록
4. 근거 부족 문장 목록
5. 변호사에게 물어볼 질문 5~10개
6. 다음 액션 제안

Stop condition:
- 변호사 질문 5~10개 존재
- review_packet.html 존재
- 금지 표현 없음
```

