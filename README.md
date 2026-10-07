# Unire più PDF in un unico file (locale)

Script Python **offline** che unisce due o più PDF in un solo file con [`pypdf`](https://pypi.org/project/pypdf/), senza caricare documenti su siti web.

Allineato alla guida Lab di ai riparo:

**[Unire più PDF in un unico file senza usare siti web](https://airiparo.it/lab/unire-pdf-locale/)**

## Caratteristiche

- Unione locale: dopo l’installazione di `pypdf` nello script **non** apre connessioni di rete
- CLI ibrida: passa i file in ordine, oppure senza argomenti unisce tutti i `.pdf` della cartella (ordine alfabetico)
- Flag `-o` / `--output` per il nome del PDF risultante (default `documento_unito.pdf`)
- Gli originali non vengono modificati
- Licenza **MIT**

## Requisiti

- Python **3.9+** (testato con Python 3.12)
- Dipendenza: `pypdf` (nel `venv` del progetto)
- Windows, macOS o Linux

## Installazione

### Opzione 1 — Clona il repository

```bash
git clone https://github.com/lunoffice/unire-pdf-locale.git
cd unire-pdf-locale
python3 -m venv .venv
source .venv/bin/activate   # Windows: .\.venv\Scripts\activate.bat
python -m pip install pypdf
```

### Opzione 2 — Solo lo script

Scarica `unisci_pdf.py` dalla [release/pagina del repo](https://github.com/lunoffice/unire-pdf-locale) oppure dalla scheda download su ai riparo (stesso SHA-256):

[Download verificato su ai riparo](https://airiparo.it/lab/unire-pdf-locale/)

## Uso

Con due o più PDF nella cartella di lavoro:

```bash
# ordine esplicito (consigliato)
python unisci_pdf.py documento_a.pdf documento_b.pdf

# nome output personalizzato
python unisci_pdf.py documento_a.pdf documento_b.pdf -o fascicolo.pdf

# senza argomenti: tutti i .pdf in cwd (ordine alfabetico)
python unisci_pdf.py
```

Su macOS/Linux, se serve: `python3 unisci_pdf.py …`.

### Esempio di output

```text
Inizio unione di 2 file…
 -> Aggiunto: documento_a.pdf
 -> Aggiunto: documento_b.pdf

Successo: creato …/documento_unito.pdf
```

## Opzioni della CLI

| Flag | Effetto | Default |
| --- | --- | --- |
| `files` (posizionali) | PDF da unire, nell’ordine desiderato | se omessi → tutti i `.pdf` in cwd |
| `-o` / `--output` | Nome del PDF risultante | `documento_unito.pdf` |
| `-h` / `--help` | Aiuto nativo | — |

## Note di privacy e sicurezza

- Non caricare documenti d’identità, contratti o referti su merge PDF online gratuiti.
- I PDF protetti da password tipicamente **non** si uniscono finché non sono decifrati in chiaro; questo script non aggira cifratura.
- Unire ≠ rimuovere metadati. Per le foto vedi la guida EXIF su ai riparo.

## Checksum

Lo SHA-256 di `unisci_pdf.py` è pubblicato nella scheda download della guida Lab (deve coincidere con il file di questo repository).

## Licenza

MIT — Copyright (c) 2026 Alex Lunalbi (ai riparo)
