# Epical — GDPR Compliance Handling for Employee Enterprise Data

> A repeatable process (and the working case file) for handling a GDPR **Data Subject
> Access Request (DSAR)** and compliance review over **employee enterprise data** — email,
> chat, collaboration and HR systems — from raw export through to regulator-ready legal
> deliverables.

This repository is organised as a **pipeline**: it takes the messy enterprise data that an
employer holds about an employee (Microsoft 365 mailboxes, Teams, SharePoint, and the Unit4
HR system), **indexes** it, **analyses** it for personal data and GDPR non-compliance,
**redacts** it, and **produces the legal documents** needed to assert the data subject's
rights. The current contents are the live working file for the *Thaer Saidi v. Epical /
Nordcloud* DSAR matter, but the **folder structure and steps are intended to be reused for
any employee GDPR case.**

> [!WARNING]
> **This repository contains real, highly sensitive personal data** (Swedish personal
> identity numbers, BankID artifacts, salaries, home addresses, bank/IBAN details, health
> and next-of-kin information for many individuals). Treat it as confidential case material.
> See [Confidentiality & data-handling rules](#confidentiality--data-handling-rules) before
> sharing, copying or committing anything.

---

## The process at a glance

```
  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
  │ 1. INGEST    │ → │ 2. INDEX     │ → │ 3. ANALYSE   │ → │ 4. REDACT    │ → │ 5. PRODUCE   │
  │ raw exports  │   │ inventory &  │   │ find personal│   │ minimise to  │   │ legal output │
  │ (M365, HR)   │   │ classify     │   │ data + gaps  │   │ evidential   │   │ (letters,    │
  │              │   │              │   │              │   │ value        │   │ complaint)   │
  └──────────────┘   └──────────────┘   └──────────────┘   └──────────────┘   └──────────────┘
```

| Stage | What happens | Inputs | Outputs (in this repo) |
|------|--------------|--------|------------------------|
| **1. Ingest** | Collect the raw enterprise exports the employer holds about the data subject. | PST mailbox, Teams/SharePoint exports, Unit4 HR export | `*.pst`, `Items.1.001*.zip`, `Teams/`, `Sharepoint/`, `TS Unit4 Data for GDPR.xlsx` |
| **2. Index** | Extract text, count personal identifiers (personnummer, emails), classify by keyword, build a machine-readable inventory. | Extracted `*.txt`, Office/PDF files | `_analysis/inventory.json` |
| **3. Analyse** | Map the inventory to GDPR obligations; identify missing Article 15 elements and over-disclosure. | `inventory.json`, source files | `_analysis/epical_gdpr_noncompliance_report.md`, `gdpr/0X-*.md` |
| **4. Redact** | Reduce evidence to the minimum needed to prove each point; mask third-party identifiers. | Findings + source files | `_analysis/epical_gdpr_evidence_appendix_redacted.md` |
| **5. Produce** | Generate the formal legal deliverables from the evidence. | Redacted appendix + findings | `Letter_Before_Action_*.docx`, `Complaint_to_IMY_*.docx` |

---

## Repository layout

```
epical/
├── README.md                              ← you are here (the process)
│
│   ── Stage 1: INGEST (raw enterprise data — git-ignored, see .gitignore) ──
├── thaer.saidi@epicalgroup.com.001.pst    Outlook/Exchange mailbox export
├── Items.1.001.zip                        Full M365 case export (large)
├── Items.1.001.GDPR_Case_T.zip            Scoped "GDPR Case" export
├── Items.1.001.GDPR_Case_T/               …unzipped: Exchange/ + SharePoint/ (hr, allcompany, …)
├── TS Unit4 Data for GDPR.xlsx            Unit4 HR master-data export (payroll, IBAN, next-of-kin)
├── Teams/                                 5,500+ extracted Teams/email message text files
├── Sharepoint/                            144 SharePoint docs (docx/pdf/xlsx/pptx) + key exhibits
│
│   ── Stages 2–4: INDEX / ANALYSE / REDACT ──
├── _analysis/
│   ├── inventory.json                     Machine-readable index of every extractable file
│   ├── epical_gdpr_noncompliance_report.md   Evidence-backed findings F1–F8 (the analysis)
│   ├── epical_gdpr_evidence_appendix_redacted.md   Minimally-redacted exhibits A–G
│   ├── make_letter.py                     Generator for the letter before action
│   └── make_imy_complaint.py              Generator for the IMY complaint
│
├── gdpr/                                  Regulator-oriented evidence pack (one issue per file)
│   ├── README.md                          Index of the evidence pack
│   ├── 01-timeline.md                     … through …
│   └── 08-complaint-points.md             Complaint-ready allegations
│
│   ── Stage 5: PRODUCE (legal deliverables) ──
├── Letter_Before_Action_Thaer_Saidi.docx  Formal demand to Epical / Nordcloud
└── Complaint_to_IMY_Thaer_Saidi.docx      Article 77 complaint to the Swedish DPA (IMY)
```

---

## Data sources covered (employee enterprise data)

The process is built to handle the systems a typical employer uses to process employee data:

- **Microsoft 365 — Exchange / Outlook** (`*.pst`): mailbox content, where the employee is the
  subject of, or is referenced in, internal correspondence.
- **Microsoft 365 — Teams** (`Teams/*.txt`): chat and channel messages, often containing many
  third-party recipients and identifiers.
- **Microsoft 365 — SharePoint** (`Sharepoint/`, `Items.1.001.GDPR_Case_T/SharePoint/`): HR,
  all-company and service-desk document libraries.
- **Unit4 HR / payroll** (`TS Unit4 Data for GDPR.xlsx`): personnel master data — identity
  number, bank account/IBAN, employment terms, absence/leave, and next-of-kin records.
- **Identity / signature artifacts**: BankID completion records found within the exports.

---

## The GDPR framework applied (Stage 3)

The analysis benchmarks the data against the data subject's rights and the controller's
obligations under the EU GDPR (2016/679) and the Swedish Data Protection Act (lag (2018:218)):

| Theme | Articles | What the process checks |
|------|----------|--------------------------|
| **Right of access** | 12, 15 | Was a complete Article 15 response given on time, with the (a)–(h) information? |
| **Time limits** | 12(3) | Was any extension valid and notified within one month of the true receipt date? |
| **Reasons for refusal** | 12(4) | Were blanket exclusions justified with specific reasons? |
| **Data minimisation / confidentiality** | 5(1)(c), 5(1)(f) | Was excessive or third-party data processed or disclosed? |
| **Accountability** | 5(2) | Is the controller's identity and inventory clear and documented? |
| **Lawfulness** | 6 | Is there a lawful basis for each processing activity? |
| **Special categories** | 9 | Trade-union membership, health/sick-leave — handled with heightened protection? |
| **Security & by-design** | 25, 32 | Were appropriate technical/organisational measures in place? |
| **Breach duties** | 33, 34 | Does any over-disclosure trigger notification to IMY / data subjects? |
| **Remedies** | 77, 82, 83 | Complaint to IMY, compensation, and administrative fines. |

The findings are recorded as **F1–F8** in
[`_analysis/epical_gdpr_noncompliance_report.md`](_analysis/epical_gdpr_noncompliance_report.md)
and re-stated as a one-issue-per-file evidence pack under [`gdpr/`](gdpr/).

---

## Deliverables produced (Stage 5)

Both Word documents are generated from the redacted evidence by reproducible Python scripts:

| Deliverable | Generator | Purpose |
|-------------|-----------|---------|
| [`Letter_Before_Action_Thaer_Saidi.docx`](Letter_Before_Action_Thaer_Saidi.docx) | [`_analysis/make_letter.py`](_analysis/make_letter.py) | Formal demand to the controllers to comply with Article 15 and remedy the breaches, before escalation. |
| [`Complaint_to_IMY_Thaer_Saidi.docx`](Complaint_to_IMY_Thaer_Saidi.docx) | [`_analysis/make_imy_complaint.py`](_analysis/make_imy_complaint.py) | Article 77 complaint asking IMY to investigate, order compliance, and consider corrective measures. |

### Reproducing the documents

```powershell
# From the repository root
pip install python-docx
python _analysis/make_letter.py          # → Letter_Before_Action_Thaer_Saidi.docx
python _analysis/make_imy_complaint.py   # → Complaint_to_IMY_Thaer_Saidi.docx
```

Both documents contain `[ ]` placeholders (firm details, addresses, IDs, signatory) and a
drafting note listing the facts to verify before sending — see the bottom of each document.

---

## Using this process for a new employee GDPR case

1. **Ingest** the employer's exports for the data subject into the root (mailbox, Teams,
   SharePoint, HR export). Keep large/binary bundles out of git (see `.gitignore`).
2. **Index** them into `_analysis/inventory.json` (extract text; count personnummer and email
   identifiers; classify by keyword).
3. **Analyse** against the GDPR table above; write findings to `_analysis/` and a per-issue
   pack to `gdpr/`.
4. **Redact** the strongest evidence into a minimally-redacted appendix.
5. **Produce** the letter before action and, if needed, the IMY complaint from the templates
   in `_analysis/`.

---

## Confidentiality & data-handling rules

- **Do not commit raw evidence.** `.gitignore` already excludes `*.zip`, `*.pst` and `*.mp4`.
  Do **not** add the unredacted source files (Teams/SharePoint exports, the Unit4 workbook, or
  BankID artifacts) to version control or any shared remote.
- **Apply data minimisation to our own work product** — the same principle we hold the
  controller to. Only the *redacted* appendix is intended to circulate; mask third-party
  personnummer, contact details and signature blobs.
- **Restrict access** to those working the matter. Store on encrypted media; deliver disclosures
  by secure channel.
- **Third-party data is not ours to publish** — exhibits expose ~105 other employees. Keep
  unredacted originals for IMY/court production only, on a confidential basis.

---

## Disclaimer

This repository is **case-preparation material and a working process, not legal advice**, and
it was assembled with automated tooling. The `.docx` deliverables are drafts prepared on the
instructions and material provided; they must be reviewed and settled by a qualified Swedish
**advokat** before they are sent or filed. Dates, the controller's identity, and the exact
contents of any disclosure already made must be independently verified.
