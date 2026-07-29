# Codex × 법제처 MCP — 파산전문 변호사를 위한 2시간 토탈 솔루션

일요일 2시간 동안 변호사 친구에게 **AI 도구를 분업시켜 일하는 법**을 알려주고,  
**NotebookLM + Codex + 법제처(law.go.kr) MCP**를 연결해 개인파산/개인회생 업무용 루틴을 함께 만든다.

이 프로젝트는 낙초의 **OpenAI FDE 연습**이다.  
고객은 파산전문 변호사이고, 목표는 “AI 데모”가 아니라 실제 업무에 남는 토탈 솔루션이다.

🔗 **기획 페이지(GitHub Pages)**: `https://waterfirst.github.io/fde-codex-lawyer/`

## 2시간 목표

2시간 뒤 변호사가 직접 할 수 있어야 한다.

1. NotebookLM으로 익명 사건 문서를 읽고 핵심 사실·쟁점·출처를 뽑기
2. Codex에게 사건 자료 정리와 산출물 생성을 지시하기
3. 법제처 MCP로 법령 근거 확인하기
4. 개인파산/개인회생 사건 1건의 1차 검토 패킷 만들기
5. 누락자료·쟁점후보·변호사 확인질문 뽑기
6. 결과물을 GitHub/HTML로 남겨 다음 사건에 재사용하기

## 도구 분업

- **NotebookLM = 눈**
  - PDF 묶음을 읽고 핵심 사실, 쟁점 후보, 출처 위치를 뽑는다.
  - 비개발자 변호사에게 가장 빠른 첫 성공 경험을 준다.
- **Gemini = 긴 문서/스캔 보조**
  - 초장문 단일 문서, 이미지성 문서, 스캔 품질이 낮은 문서의 초벌 구조화에 쓴다.
- **Codex = 손**
  - 폴더, 파일, Markdown, CSV, HTML, GitHub Pages, 반복 루틴을 만든다.
- **법제처 MCP = 근거**
  - 법령 조문, 시행일, 개정 여부를 확인한다.
- **Claude/GPT = 오케스트레이터**
  - 업무분해, 위험표현 제거, 개인정보 안전선, 변호사 검토 질문을 정리한다.
- **변호사 = 최종 판단**
  - 법률 의견, 제출 문구, 대외 판단은 변호사가 확정한다.

## 무엇을 만드나 — 다섯 루틴

1. **법령 Q&A** (`routines/01_law_qa.md`)  
   질문 → 법제처 MCP 검색 → 조문 인용 + 쉬운 설명
2. **개정 모니터** (`routines/02_amendment_watch.md`)  
   관심 법령 변경 → 변경점 요약 리포트
3. **자문 메모 생성** (`routines/03_advisory_memo.md`)  
   사안 → 법령 근거 → 자문 메모 초안
4. **파산/회생 사건 Intake** (`prompts/01_case_intake_prompt.md`)  
   원본 자료 → 문서 인덱스·누락자료·기본 사실
5. **변호사 검토 패킷** (`SKILL.md`)  
   쟁점 후보 → 증빙표 → 질문 목록 → 최종 리뷰 패킷

## 준비물
- Codex CLI (설치·로그인 완료)
- law.go.kr 오픈API 인증키(`OC`) — [open.law.go.kr](https://open.law.go.kr)에서 발급
- `~/.codex/config.toml`에 `korean_law` MCP 등록 (아래)

```toml
[mcp_servers.korean_law]
command = "npx"
args = ["-y", "korean-law-mcp"]
env = { LAW_OC = "본인_인증키" }
startup_timeout_sec = 30
tool_timeout_sec = 180
enabled = true
```

연결 확인: Codex에서 `개인정보보호법 제15조 찾아줘` → 실제 조문이 나오면 성공.

## 2시간 흐름
| 시간 | 파트 | 내용 |
|---|---|---|
| 0:00–0:15 | 문제정의 | 월 12건 업무흐름, 병목, 금지범위 |
| 0:15–0:35 | 첫 성공 | NotebookLM으로 익명 샘플 문서 읽기 |
| 0:35–0:50 | 환경연결 | Codex·법제처 MCP 연결 확인 |
| 0:50–1:20 | 사건 루틴 | Codex로 개인파산/회생 Intake 루틴 실행 |
| 1:20–1:45 | 토탈 패킷 | 법제처 MCP 근거 + 요약·쟁점·증빙·질문 산출 |
| 1:45–2:00 | 핸드오프 | GitHub Pages, 다음 파일럿 1건 지정 |

## 안전 원칙
AI 출력은 **초안**이지 법률 자문이 아니다. 모든 결론은 인용된 조문·판례로 검증하고 변호사가 최종 책임진다.

특히 NotebookLM/Gemini는 외부 클라우드 서비스이므로, **실제 의뢰인 원문을 그대로 업로드하지 않는다.**

- 실습은 익명 샘플 사건만 사용
- 실무 적용 시 의뢰인명, 주민번호, 주소, 계좌번호, 민감 가족정보 제거
- 민감 사건은 엔터프라이즈/로컬 처리 검토
- 변호사-의뢰인 비밀유지와 개인정보보호법 리스크를 먼저 설명

## FDE 관점 성공 기준

- 고객 업무를 먼저 듣고 문제를 재정의했는가?
- 2시간 안에 돌아가는 최소 루틴을 만들었는가?
- 법령 근거와 개인정보 안전선을 지켰는가?
- 다음 사건에 재사용 가능한 문서/프롬프트/폴더 구조가 남았는가?
- 변호사가 “이거 다음 사건에도 써보겠다”고 느끼는가?

## 일요일에 열어놓을 파일

- `WORKSHOP_RUNBOOK.md` — 진행자 스크립트
- `CHECKLIST.md` — 준비/보안/시연 체크리스트
- `prompts/copy_paste.md` — 실습 중 바로 복붙할 프롬프트
- `prompts/04_full_orchestration_prompt.md` — 전체 사건 패킷 생성 프롬프트
- `cases/sample_001_personal_bankruptcy/` — 익명 샘플 사건

## 재실행법
1. `~/.codex/config.toml`의 `korean_law` MCP `enabled=true` 확인
2. Codex 실행 후 `AGENTS.md` → 원하는 루틴 파일을 읽히고 지시
3. 산출물(HTML/MD)은 프로젝트 폴더에 저장, 필요하면 GitHub push
