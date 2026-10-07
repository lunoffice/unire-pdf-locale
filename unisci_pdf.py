#!/usr/bin/env python3
"""
Unisci più PDF in un unico file — solo locale, nessuna rete.

Uso:
  python unisci_pdf.py a.pdf b.pdf
  python unisci_pdf.py a.pdf b.pdf -o fascicolo.pdf
  python unisci_pdf.py
      (senza argomenti: unisce tutti i .pdf della cartella corrente,
       in ordine alfabetico, escludendo il file di output)

Dipendenza: pypdf (installala nel venv del progetto).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from pypdf import PdfWriter


DEFAULT_OUTPUT = "documento_unito.pdf"


def raccolta_input(paths: list[str], output_name: str) -> list[Path]:
    """Restituisce i PDF da unire: argomenti CLI oppure tutti i .pdf in cwd."""
    out = Path(output_name).resolve()

    if paths:
        candidati = [Path(p) for p in paths]
    else:
        candidati = sorted(
            p for p in Path.cwd().glob("*.pdf") if p.resolve() != out
        )

    validi: list[Path] = []
    for p in candidati:
        if not p.is_file():
            print(f"Attenzione: '{p}' non esiste — saltato.", file=sys.stderr)
            continue
        if p.suffix.lower() != ".pdf":
            print(f"Attenzione: '{p}' non è un .pdf — saltato.", file=sys.stderr)
            continue
        if p.resolve() == out:
            print(
                f"Attenzione: '{p}' è il file di output — saltato.",
                file=sys.stderr,
            )
            continue
        validi.append(p)

    return validi


def unisci_pdf(file_input: list[Path], nome_output: str) -> Path:
    if len(file_input) < 2:
        print(
            "Errore: servono almeno 2 file PDF validi.",
            file=sys.stderr,
        )
        sys.exit(1)

    destinazione = Path(nome_output)
    print(f"Inizio unione di {len(file_input)} file…")
    writer = PdfWriter()

    try:
        for pdf in file_input:
            writer.append(str(pdf))
            print(f" -> Aggiunto: {pdf.name}")

        with destinazione.open("wb") as fh:
            writer.write(fh)
    except Exception as exc:  # noqa: BLE001 — messaggio chiaro per l'utente
        print(f"Errore durante l'unione: {exc}", file=sys.stderr)
        sys.exit(1)
    finally:
        writer.close()

    print(f"\nSuccesso: creato {destinazione.resolve()}")
    return destinazione


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Unisci più PDF in un unico file (solo locale).",
    )
    parser.add_argument(
        "files",
        nargs="*",
        help="PDF da unire, nell'ordine desiderato. Se omessi: tutti i .pdf in cwd.",
    )
    parser.add_argument(
        "-o",
        "--output",
        default=DEFAULT_OUTPUT,
        help=f"Nome del PDF risultante (default: {DEFAULT_OUTPUT})",
    )
    args = parser.parse_args()

    validi = raccolta_input(args.files, args.output)
    if not args.files:
        if not validi:
            print(
                "Nessun PDF trovato nella cartella corrente. "
                "Passa i file: python unisci_pdf.py a.pdf b.pdf",
                file=sys.stderr,
            )
            sys.exit(1)
        print("Nessun argomento: unisco i PDF della cartella (ordine alfabetico).")
        for p in validi:
            print(f"  - {p.name}")

    unisci_pdf(validi, args.output)


if __name__ == "__main__":
    main()
