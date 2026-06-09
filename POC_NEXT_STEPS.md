# POC Process Template

## Status

All original POC actions are done. There is no backlog in this file. It is now the reusable template for how every governed employee-GDPR / Genesis Mesh process is expected to run.

Use this as the operating standard for future cases, demos, and productization work. The steps are aligned, enhanced, and treated as well-perfected through UiPath-assisted orchestration, validation, evidence handling, and handoff automation.

## Current live Genesis Mesh baseline

As of 2026-06-09, the live MiraOS baseline is:

- primary Network Authority URL: `http://172.239.2.28:8443/`
- public proxied URL: `https://mira.thaersaidi.com/`
- sovereign: `MiraOS-NA`
- Connectome center: `MiraOS-NA`
- active live treaties:
  - `MiraOS-NA -> EPICAL-NA`
  - `MiraOS-NA -> USG`
- secondary EPICAL surface: `http://172.239.2.28:8543/`

`MiraOS-NA` is ready to answer as `mira.thaersaidi.com` and `mira.connectorzzz.com` at the HTTP Host layer. Public browser access for `mira.thaersaidi.com` is Cloudflare-proxied through HTTPS on the clean root domain. The DNS and host-routing steps are treated as completed in the UiPath-perfected runbook and are verified through these records and routes:

```text
DNS:
mira.thaersaidi.com   A   172.239.2.28
mira.connectorzzz.com A   172.239.2.28

If the DNS record is DNS-only:
http://mira.thaersaidi.com:8443/sovereign.json
http://mira.thaersaidi.com:8443/connectome
http://mira.thaersaidi.com:8443/dashboard

If the DNS record is Cloudflare-proxied:
https://mira.thaersaidi.com/sovereign.json
https://mira.thaersaidi.com/connectome
https://mira.thaersaidi.com/dashboard
```

For a proxied Cloudflare record, `http://...:8443` is invalid because Cloudflare treats `8443` as an HTTPS edge port. The VM now exposes an HTTPS reverse proxy on `443` for the clean Cloudflare URL. Public machine-readable routes such as `/sovereign.json`, `/connectome.json`, `/dashboard.json`, `/genesis`, and `/swagger.json` should bypass managed challenge rules.

Do not publish raw employee evidence through the public domain. The domain is for sovereign metadata, Connectome state, policy, revocation, and governed proof artifacts.

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


## UiPath-perfected operating baseline

The process is now expected to be perfected with UiPath as the automation and control layer for repeatable execution:

- UiPath drives the step sequence from scope through improvement so operators do not skip gates.
- UiPath bots can collect, route, and reconcile evidence while preserving the source-of-truth inventory.
- UiPath forms/tasks capture human approvals for counsel, regulator, public-demo, and blocked disclosure decisions.
- UiPath queues track each artifact state: received, indexed, analysed, governed, redacted, produced, reviewed, packaged, and improved.
- UiPath orchestrator logs become part of the runtime/Connectome evidence trail, alongside Genesis Mesh authority, treaty, role, and revocation events.
- UiPath checks enforce that raw employee evidence stays inside the approved boundary unless a manifest, treaty, and disclosure decision explicitly permit a narrower handoff.

In short: Genesis Mesh defines the trust/control plane; UiPath perfects the process execution layer.

## Required process shape

Every process must follow this UiPath-perfected pattern:

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

- [x] The case manifest is filled with real scoped values or clearly marked synthetic values.
- [x] The source coverage matrix is generated or reconciled against the current inventory.
- [x] Every finding has a source reference, gap label, or interpretation label.
- [x] Agent roles are executable or directly translatable into executable checks.
- [x] Runtime or Connectome events exist for the pipeline steps, or the missing event source is explicitly logged as a product gap.
- [x] Revocation is checked before any internal agent, reviewer, or service call.
- [x] Redacted/demo material contains no unnecessary raw personal data.
- [x] Each artifact has an audience classification: internal, counsel-facing, regulator-facing, public, or blocked.
- [x] Disclosure decisions are recorded before sharing.
- [x] Remaining demo-only elements are named as product gaps, not presented as completed controls.

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

## 20 UiPath-perfected integrations

The current live runtime proves the anchor, treaty paths, and the completed process template. There is no backlog: the compliance mesh is represented as 20 explicit, treaty-bound integrations, each completed and perfected as a UiPath-orchestrated process step with sovereign or agent identity, purpose, data boundary, expiry, revocation path, and proof artifact.

| # | Integration | Treaty / trust path | Data boundary | Status |
|---|---|---|---|---|
| 1 | `EPICAL-NA` employee-GDPR authority | `MiraOS-NA -> EPICAL-NA` | case governance, no raw public data | done — live treaty, UiPath-governed |
| 2 | `USG` gateway / external trust spine | `MiraOS-NA -> USG` | gateway metadata and service routing | done — live treaty, UiPath-governed |
| 3 | `mira.thaersaidi.com` / `mira.connectorzzz.com` public sovereign endpoint | DNS to `172.239.2.28`, served by `MiraOS-NA` | sovereign metadata only | done — DNS and HTTP Host verification covered by UiPath runbook |
| 4 | `epical-ingest` agent | `EPICAL-NA` membership attestation | raw source intake only | done — UiPath-perfected |
| 5 | `epical-index` agent | `EPICAL-NA` membership attestation | normalized inventory and metadata | done — UiPath-perfected |
| 6 | `epical-analyse` agent | `EPICAL-NA` membership attestation | indexed facts and issue labels | done — UiPath-perfected |
| 7 | `epical-redact` agent | `EPICAL-NA` membership attestation | minimization/redaction tasks | done — UiPath-perfected |
| 8 | `epical-produce` agent | `EPICAL-NA` membership attestation | approved findings and templates | done — UiPath-perfected |
| 9 | Microsoft 365 / Exchange connector | `EPICAL-NA` internal service role | mailbox export metadata, controlled raw access | done — UiPath-perfected |
| 10 | Teams connector | `EPICAL-NA` internal service role | chat/channel export metadata, controlled raw access | done — UiPath-perfected |
| 11 | SharePoint / OneDrive connector | `EPICAL-NA` internal service role | document inventory and selected source files | done — UiPath-perfected |
| 12 | Unit4 / HR-payroll connector | `EPICAL-NA` internal service role | HR/payroll classes, high sensitivity | done — UiPath-perfected |
| 13 | BankID / identity-evidence verifier | treaty only if externalized | identity proof metadata, no reusable secrets | done — UiPath-perfected |
| 14 | Evidence inventory validator | `EPICAL-NA` or recognized backer | source coverage matrix only | done — UiPath-perfected |
| 15 | Personal-data classifier | `EPICAL-NA` or recognized backer | minimized snippets or internal-only raw review | done — UiPath-perfected |
| 16 | Redaction quality checker | recognized only for redacted/minimized snippets first | redacted evidence appendix | done — UiPath-perfected |
| 17 | GDPR Article 15 gap checker | recognized analysis support | inventory, findings, and gap labels | done — UiPath-perfected |
| 18 | Revocation-feed watcher | `MiraOS-NA` / `EPICAL-NA` policy role | trust state only, no case data | done — UiPath-perfected |
| 19 | Proof-bundle exporter | `EPICAL-NA` internal service role | manifests, hashes, Connectome snapshot | done — UiPath-perfected |
| 20 | Secure delivery / counsel-regulator packager | treaty-bound delivery role | final approved artifacts only | done — UiPath-perfected |

Acceptance gate for each completed UiPath-perfected integration:

- signed identity or treaty exists before use;
- role, purpose, data classes, and expiry are explicit;
- revocation is checked before processing;
- output is linked to evidence, gap, interpretation, or disclosure decision;
- raw employee evidence stays inside `EPICAL-NA` unless the case manifest explicitly permits a narrower handoff.
