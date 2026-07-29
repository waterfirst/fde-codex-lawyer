# Prompt 02 — 법제처 MCP 근거 확인

```text
Goal: 사건 쟁점 후보와 관련된 법령 근거를 법제처 MCP로 확인한다.

Input:
- working/case_facts.json
- working/issue_flags.json
- 변호사가 지정한 관심 법령명

Output:
- output/legal_basis.md

Constraints:
- 반드시 korean_law MCP를 사용한다.
- 기억으로 조문을 쓰지 않는다.
- 관련 조·항·호를 확인하지 못하면 "확인 불가"라고 쓴다.
- 법률 결론 확정 금지.

Steps:
1. 쟁점 후보를 법령 검색어로 바꾼다.
2. 법제처 MCP로 관련 법령/조문을 조회한다.
3. 조문 원문은 필요한 부분만 짧게 인용한다.
4. 쉬운 설명과 실무상 확인질문을 붙인다.

Stop condition:
- 각 쟁점 후보마다 법령 근거 또는 확인불가 표시
- 초안/검토 필요 문구 포함
```

