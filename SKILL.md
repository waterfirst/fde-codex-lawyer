# SKILL.md — 개인파산/개인회생 사건 1차 검토 패킷 생성

## 목적

익명화된 개인파산/개인회생 사건 자료를 받아 변호사 검토용 1차 패킷을 만든다.

AI는 법률 판단을 확정하지 않는다.  
반복 작업인 자료정리, 누락확인, 쟁점 후보, 초안, 증빙표, 질문 목록만 만든다.

## 입력

```text
cases/YYYY/YYYY-MM-NNN_case_slug/input/
├─ raw_pdfs/
├─ interview/
└─ metadata.json
```

## 출력

```text
output/
├─ 01_case_summary.md
├─ 02_issue_checklist.md
├─ 03_draft_report.md
├─ 04_evidence_table.csv
└─ 05_questions_for_lawyer.md

audit/
├─ run_log.md
├─ privacy_check.md
└─ unsupported_claims.md
```

## 루프

1. Intake
   - 파일 목록화
   - 문서 유형 분류
   - 누락자료 표시
2. Extraction
   - OCR/텍스트 추출
   - 날짜, 금액, 계좌, 재산, 소득, 가족관계 후보 구조화
3. Screening
   - 가족 간 이체
   - 편파변제 후보
   - 재산 처분 후보
   - 보험 환급금
   - 차량/부동산/사업자산
   - 진술 불일치
4. Legal Grounding
   - 법제처 MCP로 관련 법령 확인
   - 조문 없는 결론 금지
5. Draft
   - 사건 요약
   - 쟁점 후보
   - 추가 자료 요청
6. Evidence
   - 핵심 문장별 문서/페이지 연결
7. Review
   - 개인정보 노출 점검
   - 법률 단정 표현 제거

## 금지 표현

- 면책 가능 확정
- 면책불허가 확정
- 사기파산
- 법 위반 확정
- 판사가 반드시 이렇게 판단

## 허용 표현

- 검토 필요
- 쟁점 후보
- 추가 확인 필요
- 자료상 확인되는 범위
- 변호사 판단 필요
- 근거 추가 필요

## 종료조건

- 5개 표준 산출물 생성
- 개인정보 노출 점검 완료
- 법률 단정 표현 0개
- 근거 없는 문장은 `unsupported_claims.md`에 분리
- 변호사 질문 5~10개 생성

