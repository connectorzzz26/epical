# Epical — Governed Employee GDPR Compliance Mesh

> A repeatable process, working case file, and Genesis Mesh control-plane prototype for
> handling a GDPR **Data Subject Access Request (DSAR)** and compliance review over
> **employee enterprise data** — email, chat, collaboration, HR, identity, and project
> systems — from raw export through to regulator-ready legal deliverables.

This repository is organised as a **pipeline with a governance overlay**. The pipeline takes
the messy enterprise data that an employer holds about an employee (Microsoft 365 mailboxes,
Teams, SharePoint, and the Unit4 HR system), **indexes** it, **analyses** it for personal data
and GDPR non-compliance, **redacts** it, and **produces the legal documents** needed to assert
the data subject's rights.

The Genesis Mesh overlay turns that same pipeline into a governed trust system: `MiraOS-NA`
acts as the Genesis Mesh sovereign anchor, `EPICAL-NA` / `epical-na` acts as Epical's
treaty-recognized Network Authority, internal agents become signed role-bound processors,
backer/external services are recognized only by treaty, and the case record can distinguish
evidence from interpretation, reviewer feedback, and influence loops.

The current contents are the live working file for the *Thaer Saidi v. Epical / Nordcloud*
DSAR matter, but the **folder structure and steps are intended to be reused for any employee
GDPR case**. In product terms, this is not just one DSAR case: it is the prototype for a
governed employee GDPR compliance mesh.

The pipeline is reflected directly in the **numbered top-level folders** (`01-ingest` →
`05-deliverables`): each folder is one stage, and Genesis Mesh is documented as the control
plane that governs the stages.

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
  │ 01-ingest    │   │ 02-index     │   │ 03-analysis  │   │ 04-redacted… │   │ 05-deliver…  │
  └──────────────┘   └──────────────┘   └──────────────┘   └──────────────┘   └──────────────┘
          ▲                  ▲                  ▲                  ▲                  ▲
          └──────────────────┴──────────────────┴──────────────────┴──────────────────┘
                  Genesis Mesh control plane: identity, policy, treaties, revocation,
                  evidence/influence separation, and auditable processing authority
```

| Stage | Folder | What happens | Outputs |
|------|--------|--------------|---------|
| **1. Ingest** | `01-ingest/` | Collect the raw enterprise exports the employer holds about the data subject. | Mailbox PST, Teams/SharePoint exports, Unit4 workbook, full case-export zips |
| **2. Index** | `02-index/` | Extract text, count personal identifiers (personnummer, emails), classify by keyword, build a machine-readable inventory. | `inventory.json` |
| **3. Analyse** | `03-analysis/` | Map the inventory to GDPR obligations; identify missing Article 15 elements and over-disclosure. | `epical_gdpr_noncompliance_report.md`, `gdpr/0X-*.md` |
| **4. Redact** | `04-redacted-evidence/` | Reduce evidence to the minimum needed to prove each point; mask third-party identifiers. | `epical_gdpr_evidence_appendix_redacted.md` |
| **5. Produce** | `05-deliverables/` | Generate the formal legal deliverables from the evidence. | `Letter_Before_Action_*.docx`, `Complaint_to_IMY_*.docx` |

---

## Genesis Mesh governance layer

The root strategic artifact is [`GENESIS_MESH_EMPLOYEE_GDPR_CONTROL_PLANE.md`](GENESIS_MESH_EMPLOYEE_GDPR_CONTROL_PLANE.md).
It reframes this repository as a governed employee GDPR compliance mesh prototype:

- `MiraOS-NA` is the Genesis Mesh sovereign anchor for the model.
- `EPICAL-NA` / `epical-na` is the treaty-recognized Network Authority for the case.
- Internal agents are treated as signed, scoped, revocable processors.
- Initial-backer or external services are recognized only through purpose-bound treaties.
- Thaer's case is the privacy-preserving baseline for proving the process.
- Nordcloud-style feedback-loop risk is modeled as an influence-control problem: evidence,
  interpretation, reviewer feedback, and legal conclusions must remain separate and auditable.

Detailed Genesis Mesh notes live under [`06-genesismesh/`](06-genesismesh/), and the post-POC operating-model artifacts live under [`06-governance/`](06-governance/).

---

## Repository layout

```
epical/
├── README.md                       ← root narrative: pipeline + Genesis Mesh governance layer
├── GENESIS_MESH_EMPLOYEE_GDPR_CONTROL_PLANE.md
│                                      root control-plane thesis for the employee GDPR mesh
├── POC_NEXT_STEPS.md                post-POC implementation path
├── .gitignore
│
├── 01-ingest/                      STAGE 1 — raw enterprise data, as exported
│   ├── Exchange/
│   │   └── thaer.saidi@epicalgroup.com.001.pst   Outlook/Exchange mailbox (git-ignored)
│   ├── Teams/                       5,563 extracted Teams/email message text files
│   ├── Sharepoint/                  144 SharePoint docs (docx/pdf/xlsx/pptx) + key exhibits
│   ├── Unit4/
│   │   └── TS Unit4 Data for GDPR.xlsx   HR master data (payroll, IBAN, next-of-kin)
│   └── case-exports/                Full M365 case exports
│       ├── Items.1.001.zip                       (git-ignored, large)
│       ├── Items.1.001.GDPR_Case_T.zip           (git-ignored)
│       └── Items.1.001.GDPR_Case_T/   …unzipped: Exchange/ + SharePoint/ (hr, allcompany, …)
│
├── 02-index/                       STAGE 2 — machine-readable inventory
│   └── inventory.json               Index of every extractable file (ids, keywords, snippets)
│
├── 03-analysis/                    STAGE 3 — findings mapped to GDPR
│   ├── epical_gdpr_noncompliance_report.md   Evidence-backed findings F1–F8
│   └── gdpr/                        Regulator-oriented evidence pack (one issue per file)
│       ├── README.md                Index of the evidence pack
│       ├── 01-timeline.md           … through …
│       └── 08-complaint-points.md   Complaint-ready allegations
│
├── 04-redacted-evidence/           STAGE 4 — minimised, third-party-masked exhibits
│   └── epical_gdpr_evidence_appendix_redacted.md   Exhibits A–G
│
├── 05-deliverables/                STAGE 5 — regulator-/court-ready legal output
│   ├── Letter_Before_Action_Thaer_Saidi.docx   Formal demand to Epical / Nordcloud
│   ├── Complaint_to_IMY_Thaer_Saidi.docx        Article 77 complaint to the Swedish DPA (IMY)
│   └── generators/                  Reproducible python-docx builders
│       ├── make_letter.py
│       └── make_imy_complaint.py
│
├── 06-genesismesh/                 Genesis Mesh control-plane notes and Connectome example
│   ├── README.md
│   ├── epical-na-use-case.md
│   ├── best-case-onboarding-feedback-loop.md
│   └── connectome.json
│
└── 06-governance/                  Post-POC operating-model artifacts
    ├── README.md
    ├── case-manifest.example.yaml
    ├── agent-roles.yaml
    ├── evidence-classes.yaml
    ├── influence-map.md
    ├── source-coverage-matrix.md
    └── ... treaty, revocation, redaction, regulator, metrics, roadmap docs
```

---

## Data sources covered (employee enterprise data)

The process is built to handle the systems a typical employer uses to process employee data:

- **Microsoft 365 — Exchange / Outlook** (`01-ingest/Exchange/*.pst`): mailbox content, where
  the employee is the subject of, or is referenced in, internal correspondence.
- **Microsoft 365 — Teams** (`01-ingest/Teams/*.txt`): chat and channel messages, often
  containing many third-party recipients and identifiers.
- **Microsoft 365 — SharePoint** (`01-ingest/Sharepoint/`, and
  `01-ingest/case-exports/Items.1.001.GDPR_Case_T/SharePoint/`): HR, all-company and
  service-desk document libraries.
- **Unit4 HR / payroll** (`01-ingest/Unit4/TS Unit4 Data for GDPR.xlsx`): personnel master
  data — identity number, bank account/IBAN, employment terms, absence/leave, next-of-kin.
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
[`03-analysis/epical_gdpr_noncompliance_report.md`](03-analysis/epical_gdpr_noncompliance_report.md)
and re-stated as a one-issue-per-file evidence pack under
[`03-analysis/gdpr/`](03-analysis/gdpr/).

---

## Deliverables produced (Stage 5)

Both Word documents are generated from the redacted evidence by reproducible Python scripts:

| Deliverable | Generator | Purpose |
|-------------|-----------|---------|
| [`Letter_Before_Action_Thaer_Saidi.docx`](05-deliverables/Letter_Before_Action_Thaer_Saidi.docx) | [`generators/make_letter.py`](05-deliverables/generators/make_letter.py) | Formal demand to the controllers to comply with Article 15 and remedy the breaches, before escalation. |
| [`Complaint_to_IMY_Thaer_Saidi.docx`](05-deliverables/Complaint_to_IMY_Thaer_Saidi.docx) | [`generators/make_imy_complaint.py`](05-deliverables/generators/make_imy_complaint.py) | Article 77 complaint asking IMY to investigate, order compliance, and consider corrective measures. |

### Reproducing the documents

```powershell
# From the repository root
pip install python-docx
python 05-deliverables/generators/make_letter.py          # → 05-deliverables/Letter_Before_Action_Thaer_Saidi.docx
python 05-deliverables/generators/make_imy_complaint.py   # → 05-deliverables/Complaint_to_IMY_Thaer_Saidi.docx
```

Each script writes its `.docx` into `05-deliverables/` (the path is resolved relative to the
script, so it works from any working directory). Both documents contain `[ ]` placeholders
(firm details, addresses, IDs, signatory) and a drafting note listing the facts to verify
before sending — see the bottom of each document.

---

## Using this process for a new employee GDPR case

1. **Ingest** the employer's exports for the data subject into `01-ingest/` (mailbox →
   `Exchange/`, chat → `Teams/`, documents → `Sharepoint/`, HR → `Unit4/`, full bundles →
   `case-exports/`). Keep large/binary bundles out of git (see `.gitignore`).
2. **Index** them into `02-index/inventory.json` (extract text; count personnummer and email
   identifiers; classify by keyword).
3. **Analyse** against the GDPR table above; write findings to `03-analysis/` and a per-issue
   pack to `03-analysis/gdpr/`.
4. **Redact** the strongest evidence into a minimally-redacted appendix in
   `04-redacted-evidence/`.
5. **Produce** the letter before action and, if needed, the IMY complaint using the generators
   in `05-deliverables/generators/`.

---

## Confidentiality & data-handling rules

- **Do not commit raw evidence.** `.gitignore` already excludes `*.zip`, `*.pst` and `*.mp4`.
  Do **not** add the unredacted source files (the `01-ingest/Teams` and `01-ingest/Sharepoint`
  exports, the Unit4 workbook, or BankID artifacts) to version control or any shared remote.
- **Apply data minimisation to our own work product** — the same principle we hold the
  controller to. Only the *redacted* appendix (`04-redacted-evidence/`) is intended to
  circulate; mask third-party personnummer, contact details and signature blobs.
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
