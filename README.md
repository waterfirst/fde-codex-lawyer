# Codex × 법제처 MCP — 변호사를 위한 2시간 토탈 솔루션 (FDE 실습)

비개발자 변호사가 **Codex CLI + 법제처(law.go.kr) MCP**로 실무 어시스턴트를 만드는 2시간 핸즈온.
FDE(Forward Deployed Engineer) 연습: 고객(변호사)의 실제 업무에 들어가 돌아가는 솔루션을 함께 만든다.

🔗 **기획 페이지(GitHub Pages)**: `https://waterfirst.github.io/fde-codex-lawyer/`

## 무엇을 만드나 — 세 루틴
1. **법령 Q&A** (`routines/01_law_qa.md`) — 질문 → 법령 검색 → 조문 인용 + 쉬운 설명
2. **개정 모니터** (`routines/02_amendment_watch.md`) — 관심 법령 변경 → 변경점 요약 리포트
3. **자문 메모 생성** (`routines/03_advisory_memo.md`) — 사안 → 법령·판례 근거 → 자문 메모 초안(HTML)

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
| 0:00–0:15 | 환경 준비 | Codex·MCP 연결, `AGENTS.md` |
| 0:15–0:40 | 첫 성공 | 법령 하나 검색·요약 |
| 0:40–1:15 | 루틴 만들기 | 루틴① 법령 Q&A |
| 1:15–1:45 | 토탈 솔루션 | 루틴②/③ 조립 → HTML 리포트 |
| 1:45–2:00 | 핸드오프 | README·GitHub·다음 과제 |

## 안전 원칙
AI 출력은 **초안**이지 법률 자문이 아니다. 모든 결론은 인용된 조문·판례로 검증하고 변호사가 최종 책임진다.
의뢰인 실명·민감정보는 입력하지 않는다.

## 재실행법
1. `~/.codex/config.toml`의 `korean_law` MCP `enabled=true` 확인
2. Codex 실행 후 `AGENTS.md` → 원하는 루틴 파일을 읽히고 지시
3. 산출물(HTML/MD)은 프로젝트 폴더에 저장, 필요하면 GitHub push
