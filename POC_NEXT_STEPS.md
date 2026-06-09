# POC Process Template

## Status

The original POC next steps are now treated as done. This file is no longer a backlog. It is the reusable template for how every governed employee-GDPR / Genesis Mesh process is expected to run.

Use this as the operating standard for future cases, demos, and productization work.

## Purpose

A POC is complete only when it proves the process, not just the narrative. The expected outcome is a governed case run that can show:

- what was received;
- what was searched;
- what was missing;
- who or what processed each evidence class;
- which findings are evidence-backed, gap-backed, interpreted, disputed, or rejected;
- which services were trusted, constrained, expired, or revoked;
- what was redacted, disclosed, withheld, or escalated;
- why every external-facing artifact is safe to share.

## Required process shape

Every process must follow this pattern:

```text
1. Scope
   -> define the case, subject, purpose, lawful boundary, forbidden processing, and success criteria

2. Ingest
   -> collect the raw exports or inputs without changing evidential originals

3. Index
   -> inventory every source, classify it, and record searchable metadata

4. Analyse
   -> attach every finding to evidence references, source gaps, or explicit interpretation labels

5. Govern
   -> bind agents, reviewers, services, and authority decisions to signed roles and revocation checks

6. Redact
   -> minimise the evidence into the safest version that can still prove the point

7. Produce
   -> generate counsel-facing, regulator-facing, internal, or public artifacts from the governed record

8. Review
   -> decide what is accepted, disputed, rejected, private, privileged, or safe to disclose

9. Package
   -> produce the final pack with index, manifest, source coverage, decision log, and disclosure log

10. Improve
    -> feed reusable lessons back into templates, metrics, risks, and roadmap without leaking case data
```

## Folder template

Use this repository layout as the reference template:

```text
<case-or-process>/
├── README.md
├── GENESIS_MESH_EMPLOYEE_GDPR_CONTROL_PLANE.md
├── POC_NEXT_STEPS.md                         # this template / process standard
│
├── 01-ingest/                                # raw inputs; do not publish or commit sensitive originals
│   ├── Exchange/
│   ├── Teams/
│   ├── Sharepoint/
│   ├── Unit4/
│   └── case-exports/
│
├── 02-index/                                 # machine-readable source inventory
│   └── inventory.json
│
├── 03-analysis/                              # evidence-backed findings and legal/compliance analysis
│   ├── <case>_noncompliance_report.md
│   └── gdpr/
│       ├── README.md
│       └── 0X-<issue>.md
│
├── 04-redacted-evidence/                     # minimised exhibits safe enough for controlled review
│   └── <case>_evidence_appendix_redacted.md
│
├── 05-deliverables/                          # generated letters, complaints, packs, or reports
│   ├── generators/
│   └── <deliverable>.docx
│
├── 06-genesismesh/                           # control-plane notes and Connectome/runtime evidence
│   ├── README.md
│   ├── epical-na-use-case.md
│   ├── best-case-onboarding-feedback-loop.md
│   └── connectome.json
│
└── 06-governance/                            # reusable operating model
    ├── README.md
    ├── case-manifest.example.yaml
    ├── agent-roles.yaml
    ├── evidence-classes.yaml
    ├── source-coverage-matrix.md
    ├── influence-map.md
    ├── processing-register.md
    ├── redaction-policy.md
    ├── disclosure-decision-log.md
    ├── regulator-pack-index.md
    ├── metrics.md
    └── productization-roadmap.md
```

## Artifact acceptance criteria

A process artifact is not accepted unless it satisfies the relevant gate below.

| Artifact | Must prove | Not accepted if |
|---|---|---|
| Case manifest | case purpose, authority, evidence boundaries, forbidden processing, success criteria | it contains placeholder values that decide real scope |
| Inventory / source coverage | every expected source is received, missing, excluded, or disputed | gaps are hidden or described only in prose |
| Finding | evidence reference, gap label, or interpretation label | it states a conclusion without provenance |
| Agent role | purpose, permissions, data classes, expiry, revocation path | the role can process everything by default |
| Treaty / service boundary | counterparty, purpose, data classes, validity window, revocation | a backer/external service receives data by implication |
| Connectome / runtime log | who did what, when, under which authority, with which inputs/outputs | it is hand-written as a demo-only substitute for runtime events |
| Redacted evidence | minimum data necessary to prove the point | third-party or sensitive data remains without necessity |
| Disclosure log | audience, artifact, legal basis, redaction level, decision owner | sharing happens before the decision is recorded |
| Regulator/counsel pack | index, findings, evidence, gaps, redactions, decision history | it cannot be reconstructed by an external reviewer |

## Evidence and influence rules

Keep these categories separate in every file:

- Evidence: source-backed fact from the case material.
- Gap: expected source or Article 15 element that is absent, incomplete, withheld, or disputed.
- Interpretation: analysis based on evidence or gaps.
- Feedback: reviewer, counsel, operator, or backer input.
- Influence risk: anything that could shape the process without being part of the evidence.
- Legal conclusion: counsel-ready conclusion, never mixed with raw evidence.

No finding should collapse these categories into one paragraph without labels.

## Privacy and disclosure rules

These classes stay private by default:

- raw HR, payroll, identity, health, BankID, salary, bank, next-of-kin, or address material;
- unredacted Teams, Exchange, SharePoint, or case-export files;
- third-party personal data;
- customer, supplier, or employer confidential data;
- legal strategy drafts unless approved for sharing;
- any artifact whose intended audience has not been recorded in the disclosure decision log.

Sharing defaults:

| Audience | Default material |
|---|---|
| Internal operator | governed working set, least-privilege access |
| Counsel | redacted pack plus confidential originals only when required |
| Regulator | regulator pack, source coverage, findings, evidence appendix, decision logs |
| Public demo | synthetic or heavily redacted material only |
| Backer / external service | no case data unless treaty, purpose, data class, validity window, and revocation are explicit |

## Definition of done

A POC/process is done when all of the following are true:

- [ ] The case manifest is filled with real scoped values or clearly marked synthetic values.
- [ ] The source coverage matrix is generated or reconciled against the current inventory.
- [ ] Every finding has a source reference, gap label, or interpretation label.
- [ ] Agent roles are executable or directly translatable into executable checks.
- [ ] Runtime or Connectome events exist for the pipeline steps, or the missing event source is explicitly logged as a product gap.
- [ ] Revocation is checked before any internal agent, reviewer, or service call.
- [ ] Redacted/demo material contains no unnecessary raw personal data.
- [ ] Each artifact has an audience classification: internal, counsel-facing, regulator-facing, public, or blocked.
- [ ] Disclosure decisions are recorded before sharing.
- [ ] Remaining demo-only elements are named as product gaps, not presented as completed controls.

## Product proof

The product proof is not more text. It is a repeatable governed run where a future operator can inspect the repository and understand:

- the case boundary;
- the sources and gaps;
- the processing authority;
- the evidence chain;
- the influence controls;
- the revocation status;
- the redaction decisions;
- the disclosure decisions;
- the final accountable output.

That is the expected template for all processes: a governed operating model that can be reused, audited, demonstrated safely, and productized.
