#!/usr/bin/env python3
"""Local-only document intake for bankruptcy/rehab case folders.

This script is intentionally conservative:
- Reads files from a local folder only.
- Redacts common Korean PII patterns before writing outputs.
- Produces structured artifacts for Codex to review.
- Does not send data to external services.

Supported directly: .txt, .md, .json, .csv
PDF support: optional if `pypdf` is installed.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


SUPPORTED_TEXT = {".txt", ".md", ".json", ".csv"}


PII_PATTERNS = [
    (re.compile(r"\b\d{6}-\d{7}\b"), "[REDACTED_RRN]"),
    (re.compile(r"\b01[016789]-?\d{3,4}-?\d{4}\b"), "[REDACTED_PHONE]"),
    (re.compile(r"\b\d{2,6}-\d{2,6}-\d{2,8}\b"), "[REDACTED_ACCOUNT]"),
    (re.compile(r"([가-힣]{2,4})\s*(?:씨|님)"), "[REDACTED_NAME]"),
]

DATE_RE = re.compile(r"\b(?:20\d{2}[.-]\d{1,2}[.-]\d{1,2}|20\d{2}년\s*\d{1,2}월\s*\d{1,2}일)\b")
MONEY_RE = re.compile(r"(?:\d{1,3}(?:,\d{3})+|\d+)\s*(?:원|만원|억원)")
KEYWORD_RE = re.compile(r"(채권자|채무|소득|급여|재산|보험|차량|부동산|계좌|이체|대출|카드|압류|연체|가족|배우자|자녀)")


@dataclass
class DocRecord:
    path: str
    suffix: str
    bytes: int
    chars: int
    dates: list[str]
    money: list[str]
    keywords: list[str]
    status: str


def redact(text: str) -> str:
    redacted = text
    for pattern, replacement in PII_PATTERNS:
        redacted = pattern.sub(replacement, redacted)
    return redacted


def read_pdf(path: Path) -> str:
    try:
        from pypdf import PdfReader  # type: ignore
    except Exception:
        return "[PDF_TEXT_UNAVAILABLE: install pypdf to extract local PDF text]"
    try:
        reader = PdfReader(str(path))
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    except Exception as exc:
        return f"[PDF_READ_ERROR: {exc}]"


def read_file(path: Path) -> str:
    if path.suffix.lower() in SUPPORTED_TEXT:
        return path.read_text(encoding="utf-8", errors="ignore")
    if path.suffix.lower() == ".pdf":
        return read_pdf(path)
    return ""


def iter_files(root: Path) -> Iterable[Path]:
    for p in sorted(root.rglob("*")):
        if p.is_file() and not any(part.startswith(".") for part in p.parts):
            yield p


def unique_matches(pattern: re.Pattern[str], text: str, limit: int = 20) -> list[str]:
    seen: list[str] = []
    for m in pattern.findall(text):
        value = m if isinstance(m, str) else " ".join(m)
        if value not in seen:
            seen.append(value)
        if len(seen) >= limit:
            break
    return seen


def main() -> int:
    parser = argparse.ArgumentParser(description="Local-only case document intake")
    parser.add_argument("input_dir", help="case input directory")
    parser.add_argument("--out", default=None, help="output directory")
    args = parser.parse_args()

    input_dir = Path(args.input_dir).resolve()
    if not input_dir.exists() or not input_dir.is_dir():
        raise SystemExit(f"input_dir not found: {input_dir}")

    out_dir = Path(args.out).resolve() if args.out else input_dir.parent / "output" / "local_intake"
    out_dir.mkdir(parents=True, exist_ok=True)

    records: list[DocRecord] = []
    redacted_chunks: list[str] = []

    for path in iter_files(input_dir):
        raw = read_file(path)
        rel = path.relative_to(input_dir).as_posix()
        redacted = redact(raw)
        status = "ok" if raw else "unsupported_or_empty"
        records.append(
            DocRecord(
                path=rel,
                suffix=path.suffix.lower(),
                bytes=path.stat().st_size,
                chars=len(redacted),
                dates=unique_matches(DATE_RE, redacted),
                money=unique_matches(MONEY_RE, redacted),
                keywords=unique_matches(KEYWORD_RE, redacted),
                status=status,
            )
        )
        if redacted.strip():
            redacted_chunks.append(f"\n\n## FILE: {rel}\n\n{redacted[:8000]}")

    with (out_dir / "case_intake.json").open("w", encoding="utf-8") as f:
        json.dump([asdict(r) for r in records], f, ensure_ascii=False, indent=2)

    with (out_dir / "document_index.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(asdict(records[0]).keys()) if records else ["path"])
        writer.writeheader()
        for r in records:
            row = asdict(r)
            row["dates"] = "; ".join(row["dates"])
            row["money"] = "; ".join(row["money"])
            row["keywords"] = "; ".join(row["keywords"])
            writer.writerow(row)

    (out_dir / "redacted_text.md").write_text(
        "# Redacted Local Text\n\n"
        "원문은 외부로 보내지 않는다. 이 파일은 로컬 마스킹 결과이며 Codex 검토 입력으로 사용한다.\n"
        + "".join(redacted_chunks),
        encoding="utf-8",
    )

    (out_dir / "README_FOR_CODEX.md").write_text(
        "# Codex 지시\n\n"
        "AGENTS.md와 SKILL.md를 먼저 읽어라.\n"
        "이 폴더의 `case_intake.json`, `document_index.csv`, `redacted_text.md`만 보고 사건 1차 검토 패킷을 만들어라.\n"
        "원문 추정 금지, 개인정보 복원 금지, 법률판단 확정 금지.\n",
        encoding="utf-8",
    )

    print(json.dumps({"status": "ok", "input": str(input_dir), "out": str(out_dir), "files": len(records)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
