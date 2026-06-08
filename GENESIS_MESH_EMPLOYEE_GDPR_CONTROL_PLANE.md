# Genesis Mesh Employee GDPR Control Plane

## Executive summary

This repository is not only a working case file for one employee DSAR. It is the prototype for a governed employee GDPR compliance mesh.

The existing Epical pipeline already shows the practical flow:

```text
01-ingest -> 02-index -> 03-analysis -> 04-redacted-evidence -> 05-deliverables
```

Genesis Mesh adds the missing control plane around that flow:

- signed agent identity
- role-bound evidence access
- policy distribution
- revocation
- recognition treaties for external or backer services
- auditability of who processed what, under which authority, and why

The best-case Epical onboarding scenario is to make `MiraOS-NA` the Genesis Mesh sovereign anchor, recognize `EPICAL-NA` / `epical-na` as the Epical employee-GDPR Network Authority through a signed treaty, and use Thaer Saidi's case as the privacy-preserving baseline for proving the model.

## What this changes

Without Genesis Mesh, the repository demonstrates a strong but mostly linear compliance workflow: collect evidence, index it, analyse it, redact it, and produce legal deliverables.

With Genesis Mesh, the same workflow becomes a governed trust system:

```text
Employee GDPR request
        |
        v
+-------------------------------+
| epical-na                     |
| Genesis Mesh Network Authority|
+-------------------------------+
        |
        +--> signed ingest agent
        +--> signed index agent
        +--> signed analysis agent
        +--> signed redaction agent
        +--> signed production agent
        |
        +--> recognized backer services
             only by treaty, purpose, data class, and validity window
```

The repository then says something stronger:

> This is not just Thaer's DSAR case. This is the prototype for a governed employee GDPR compliance mesh.

## Why Thaer's case is the baseline

Thaer's case is a useful baseline because it crosses the hardest parts of employee GDPR compliance:

- Teams and internal collaboration messages
- SharePoint and document-library material
- HR, payroll, identity, and employment records
- project and customer/supplier context
- third-party personal data
- possible omission, over-disclosure, and minimisation problems
- informal internal narratives and feedback loops

That makes it a good control-test case for whether Epical can answer four questions:

1. Did we find the employee's personal data across the relevant systems?
2. Did we separate the employee's data from third-party data?
3. Did we distinguish evidence from interpretation?
4. Can we explain every agent, service, policy, and reviewer involved in the response?

The baseline must stay privacy-preserving:

- raw case material remains inside the Epical trust domain
- outside services receive no raw employee data unless explicitly approved
- backer services start with metadata, policy, trust-bundle, revocation, and coverage tasks
- any demo version uses redacted, minimized, or synthetic examples

## The `epical-na` authority model

`MiraOS-NA` should act as the Genesis Mesh sovereign anchor for this model. `EPICAL-NA` / `epical-na` should act as the recognized Network Authority for the employee GDPR compliance mesh under a signed treaty from that anchor.

It owns:

| Control | Meaning |
| --- | --- |
| Agent enrollment | Which internal agents are trusted for this case. |
| Role policy | What each agent may do. |
| Evidence boundaries | Which evidence classes each role may access. |
| Purpose limitation | Why the agent or service is allowed to process the material. |
| Backer recognition | Which external/backer sovereigns are trusted, for what purpose, and for how long. |
| Revocation | Which roles, services, or trust edges have been disabled. |
| Audit trail | How the case was processed and what changed over time. |

## Internal agent roles

| Agent | Mesh role | Boundary |
| --- | --- | --- |
| `epical-ingest` | Evidence intake | Can see raw exports for intake and normalization, but cannot make legal conclusions. |
| `epical-index` | Evidence indexing | Can structure and classify evidence, but cannot decide final disclosure. |
| `epical-analyse` | GDPR analysis | Maps indexed facts to obligations, omissions, and over-disclosure risks. |
| `epical-redact` | Data minimisation | Handles sensitive and third-party masking for a defined purpose only. |
| `epical-produce` | Response production | Builds employee/counsel/regulator deliverables from approved redacted findings. |

Each role should be signed, scoped, time-bound, and revocable.

The treaty chain should remain visible in every demo or proof bundle:

```text
MiraOS-NA
        |
        +--> treaty: EPICAL-NA employee-GDPR authority
                    |
                    +--> internal Epical agents
                    +--> treaty-bound gateways such as USG-NB / USG patterns
```

`USG-NB` or any similar gateway pattern should be treated as a recognized downstream service path, not as a default processor of Epical employee data.

## Initial-backer services

Initial Genesis Mesh backer services should be introduced carefully. They should not become broad processors of Epical employee data. Their best first use is to strengthen governance without expanding exposure.

| Backer-service class | Best first use | Data boundary |
| --- | --- | --- |
| Trust-bundle validation | Confirm service identity and recognition status. | No raw employee data. |
| Revocation feed | Stop trusting revoked agents, keys, or services. | No raw employee data. |
| Policy review | Check whether case policy matches GDPR handling rules. | Policy and metadata only. |
| Coverage checker | Detect likely missing source categories. | Source inventory only. |
| Redaction quality checker | Review minimisation consistency. | Redacted/minimized snippets first. |
| Secure delivery | Package approved deliverables. | Final approved artifacts only. |

This is the key Genesis Mesh rule:

> A service is not trusted because it is useful. A service is trusted only when `epical-na` recognizes it through a signed treaty for a specific purpose, data class, and validity window.

## Nordcloud-style influence and feedback-loop risk

The repository also needs to model an organizational risk, not only a technical one.

The Nordcloud lesson can be framed as a feedback-loop pattern:

1. Influential actors shape what gets noticed, ignored, escalated, or normalized.
2. Their feedback becomes part of the internal operating loop.
3. Later reviewers interpret new signals through that earlier narrative.
4. The organization can start treating influence as evidence.

For employee GDPR, that is dangerous. A DSAR response is not only about finding files. It is about proving that the response was not distorted by informal influence, hidden reviewer bias, or untraceable internal narratives.

Genesis Mesh helps by separating:

- direct evidence
- third-party claims
- reviewer comments
- inferred interpretations
- legal conclusions
- redaction decisions
- policy decisions

No stakeholder feedback should silently become case evidence. If feedback matters, it should have visible source, role, scope, timestamp, and review status.

## Best-case Epical outcome

In the best case, Epical can say:

> We do not use AI loosely on employee data. We operate a governed employee GDPR compliance mesh. Each agent has a signed role, each evidence class has a policy boundary, each external service is recognized by treaty, and each response can be audited from intake to delivery.

That gives Epical:

- safer employee-data handling
- fewer omissions
- less over-disclosure
- better legal defensibility
- stronger AI governance
- clearer separation between evidence and influence
- a repeatable process for future employee GDPR cases

## Repository structure after the Genesis Mesh overlay

```text
epical/
├── README.md
│   Root narrative: employee GDPR pipeline + Genesis Mesh governance layer.
│
├── GENESIS_MESH_EMPLOYEE_GDPR_CONTROL_PLANE.md
│   Root strategic/control-plane artifact: why this repo is a governed employee GDPR mesh prototype.
│
├── 01-ingest/
│   Raw employee-data exports and source material.
│
├── 02-index/
│   Machine-readable inventory and Genesis Mesh use-case notes.
│   └── 06-genesismesh/
│       ├── README.md
│       ├── epical-na-use-case.md
│       └── best-case-onboarding-feedback-loop.md
│
├── 03-analysis/
│   GDPR findings and issue-by-issue analysis.
│
├── 04-redacted-evidence/
│   Minimized evidence suitable for controlled circulation.
│
└── 05-deliverables/
    Employee/counsel/regulator-facing outputs.
```

## Demo shape

The strongest demo is not a chatbot. It is a governed case run.

### Panel 1: Employee data map

Shows systems searched, evidence classes, identifiers, source coverage, likely omissions, and third-party data density.

### Panel 2: Trust and influence map

Shows signed agents, recognized services, reviewer feedback, rejected influence, revocations, and trust edges.

### Panel 3: GDPR response pack

Shows the employee-facing response, redacted evidence appendix, counsel-ready risk memo, source coverage declaration, and unresolved gaps.

The demo moment:

> Epical can prove not only what it disclosed, but how the disclosure was governed.

## Links

- Root process: [`README.md`](README.md)
- Executive case summary: [`EXECUTIVE_SUMMARY.md`](EXECUTIVE_SUMMARY.md)
- Product-owner review: [`PRODUCT_OWNER_REVIEW_SUMMARY.md`](PRODUCT_OWNER_REVIEW_SUMMARY.md)
- Genesis Mesh index: [`02-index/06-genesismesh/README.md`](02-index/06-genesismesh/README.md)
- `epical-na` use case: [`02-index/06-genesismesh/epical-na-use-case.md`](02-index/06-genesismesh/epical-na-use-case.md)
- Best-case onboarding and feedback loop: [`02-index/06-genesismesh/best-case-onboarding-feedback-loop.md`](02-index/06-genesismesh/best-case-onboarding-feedback-loop.md)

## Guardrails

- Do not expose Thaer's raw private material to outside services without explicit approval.
- Do not treat Nordcloud-style influence as proven fact unless backed by evidence.
- Do not imply Epical has adopted Genesis Mesh unless that adoption becomes real.
- Do not let stakeholder feedback silently become case evidence.
- Do not collapse evidence, interpretation, legal conclusion, and influence into the same opaque output.
- Do not use AI-generated GDPR conclusions without traceable source references and review status.

## Product thesis

Employee GDPR compliance fails when evidence, influence, and interpretation collapse into the same opaque process.

Genesis Mesh fixes that by making trust, role, policy, feedback, and revocation explicit.
