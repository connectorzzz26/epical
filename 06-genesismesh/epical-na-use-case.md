# Use Case: `epical-na` as a Genesis Mesh Network Authority

## Executive summary

`epical-na` is the deployed orchestrator for the Epical GDPR / DSAR agent pipeline. In the current repository it coordinates the work across ingest, index, analyse, redact, and produce agents.

The Genesis Mesh use case is to make `epical-na` more than an Azure AI Foundry orchestrator: it becomes Epical's treaty-recognized Network Authority for compliance work under the `MiraOS-NA` sovereign anchor. That gives the DSAR pipeline a verifiable trust boundary, signed agent enrollment, revocation, policy distribution, and controlled collaboration with services already demonstrated by the Genesis Mesh initial backers.

In plain terms:

- `epical-na` owns the compliance case trust domain.
- Stage agents are enrolled as trusted members, not just called by name.
- Evidence access is policy-bound and revocable.
- Initial-backer services can be consumed only through signed recognition treaties.
- Every cross-agent or cross-sovereign handoff can be explained later to counsel, security, or a regulator.

## Current Epical agent pipeline

The current agent roster is documented in `src/README.md`:

| Agent | Role | Current purpose |
| --- | --- | --- |
| `epical-na` | Orchestrator | Plans the DSAR work and delegates to stage agents. |
| `epical-ingest` | Ingest | Collect and normalise raw enterprise exports such as Microsoft 365 and Unit4. |
| `epical-index` | Index | Extract text, count identifiers, and build the inventory. |
| `epical-analyse` | Analyse | Map material to GDPR obligations and identify Article 15 gaps / over-disclosure. |
| `epical-redact` | Redact | Minimise evidence and mask third-party identifiers. |
| `epical-produce` | Produce | Draft legal-ready deliverables such as counsel summaries or regulator complaint drafts. |

Genesis Mesh adds the missing trust layer around that pipeline.

## Genesis Mesh role for `epical-na`

`epical-na` should be treated as Epical's recognized Network Authority for compliance automation, operating under a signed Genesis Mesh treaty with `MiraOS-NA`.

In this model, `MiraOS-NA` is the Genesis Mesh sovereign anchor. `EPICAL-NA` / `epical-na` is the Epical employee-GDPR authority that receives a bounded mandate from that anchor. It can enroll internal Epical agents and recognize selected downstream services only inside the treaty's role, purpose, data-class, and validity limits.

Its responsibilities would be:

1. Issue signed membership attestations for the Epical stage agents.
2. Enforce which agent may access which evidence class.
3. Publish signed policy for retention, redaction, and permitted tools.
4. Revoke an agent or capability when a case closes, credentials rotate, or a tool becomes unsafe.
5. Recognize selected external/backer sovereigns only when a signed treaty path exists from `MiraOS-NA` through `EPICAL-NA`.
6. Maintain an auditable Connectome showing which agents and services were trusted for a case.

The key value is defensibility. A DSAR response should not depend on informal prompts and opaque tool calls. It should show who handled the evidence, under which authority, and whether that authority was still valid.

## Use-case flow

```text
Raw exports / case material
        |
        v
  EPICAL-NA / epical-na employee-GDPR trust domain
        |
        +--> epical-ingest   -- signed access to source exports
        +--> epical-index    -- signed access to normalized evidence
        +--> epical-analyse  -- signed access to indexed facts and legal criteria
        +--> epical-redact   -- signed access to third-party / sensitive-data minimization tasks
        +--> epical-produce  -- signed access to redacted findings and deliverable templates
        |
        +--> recognized backer services through Genesis Mesh treaties
             for example USG-NB / USG-style gateway patterns
```

That is the processing flow. The Connectome graph should be drawn differently: `MiraOS-NA` is the center of the graph, with `EPICAL-NA` and any gateway/backer sovereigns connected to it as treaty edges.

```text
                            USG-NB / USG gateway patterns
                                      |
                                      |
                                      v
EPICAL-NA / epical-na  <------>  MiraOS-NA  <------>  other recognized sovereigns
        |
        +--> epical-ingest
        +--> epical-index
        +--> epical-analyse
        +--> epical-redact
        +--> epical-produce
```

At runtime, `epical-na` can ask: "Is this agent, service, or external sovereign currently trusted for this case and role?" If not, the task is blocked or routed to a safer internal path.

## How `epical-na` benefits from initial-backer services

The initial Genesis Mesh backers already demonstrate a set of services and trust primitives that `epical-na` can use as a compliance mesh foundation. The exact public Genesis Mesh artifacts currently list verified sovereigns such as `MiraOS-NA`, `001-NA`, `anonymous-NA`, `AMINE-M6-NA`, `ONS-A-NA`, and `USG-NB`, with `MiraOS-NA` acting as the sovereign anchor for this Epical model and `USG-NB` showing a Connectome baseline of multiple active recognition edges and imported revocation material.

This Epical note treats those as available trust patterns and service classes, not as a claim that any named external organization is already serving Epical.

| Initial-backer capability | How `epical-na` benefits | DSAR / GDPR value |
| --- | --- | --- |
| Sovereign identity and signed genesis material | `epical-na` can recognize a service by cryptographic sovereign identity instead of a loose URL or prompt label. | Stronger auditability and less risk of sending evidence to the wrong endpoint. |
| Recognition treaties | `epical-na` can allow a backer service only for a defined role, purpose, and validity window. | Supports purpose limitation and least privilege. |
| Revocation feeds | If a service, agent, or attestation is revoked, `epical-na` can stop trusting it and record the reason. | Supports incident response and post-case defensibility. |
| Trust bundles | Backer services can publish portable trust material that `epical-na` can validate offline before use. | Reduces dependency on live systems when preparing legal or regulator evidence. |
| Connectome visibility | `epical-na` can show which internal agents and recognized services participated in a case. | Gives counsel a clear chain of processing and delegation. |
| Policy distribution | Policies such as allowed transports, allowed services, and maximum hops can be signed and enforced. | Helps prove controlled processing rather than uncontrolled AI automation. |
| Secure transport preferences | Existing Genesis Mesh policy material demonstrates controlled transports such as QUIC and WireGuard-style private routing. | Better fit for sensitive HR, identity, payroll, and legal material. |
| Collective / passthrough patterns | `USG-NB` demonstrates a collective-passthrough style recognition graph that can broker or aggregate multiple sovereigns. | Lets `epical-na` reach specialized services through a recognized trust spine instead of integrating every service directly. |

## Candidate backer-service integrations

These are practical service integrations that fit the Epical repository and the services implied by the initial-backer Genesis Mesh artifacts.

### 1. Evidence indexing service

A recognized backer service can help `epical-index` extract text, count identifiers, classify personal data, and build an evidence inventory.

Benefit:

- faster processing of large Teams, SharePoint, Exchange, and HR exports;
- reusable classification patterns across cases;
- signed proof that the indexing service was trusted only for inventory work.

Guardrail:

- the service receives only the minimum evidence slice required for indexing;
- third-party personal data is masked before broader sharing where possible.

### 2. Privacy and redaction service

A recognized backer service can help `epical-redact` identify personal identity numbers, addresses, health data, family data, third-party employee data, and credentials.

Benefit:

- better minimization before counsel or external review;
- consistent redaction policy across evidence appendices;
- revocation if the redaction service or its model version becomes unsafe.

Guardrail:

- no raw secrets or credential material should be sent externally;
- high-risk material stays inside `epical-na` unless a signed treaty explicitly allows the processing purpose.

### 3. GDPR analysis service

A recognized backer service can support `epical-analyse` by mapping indexed evidence to GDPR themes: Article 15 completeness, controller/processor boundaries, over-disclosure, sensitive-data handling, retention, and breach-assessment triggers.

Benefit:

- improves consistency of legal issue spotting;
- separates factual extraction from legal-risk analysis;
- creates an auditable record of which analysis service influenced each finding.

Guardrail:

- the output remains review material, not final legal advice;
- counsel-facing claims must still be validated against source evidence.

### 4. Secure delivery / trust-bundle service

A recognized backer service can provide trust-bundle validation and safe transfer of redacted deliverables.

Benefit:

- counsel can receive a compact trust package: proof bundle, Connectome summary, redaction manifest, and deliverable draft;
- offline validation becomes possible even when live agent services are unavailable.

Guardrail:

- deliverables should include redacted evidence only;
- original raw evidence remains controlled by `epical-na` unless explicitly approved.

### 5. Collective backer gateway

A collective service such as the `USG-NB` pattern can act as a recognized gateway to several specialized sovereigns.

Benefit:

- `epical-na` signs one treaty with a gateway and then consumes a curated set of services through that gateway;
- useful when the DSAR case needs multiple service classes: indexing, redaction, validation, and delivery.

Guardrail:

- the gateway must expose which downstream sovereign actually performed each task;
- `epical-na` should reject anonymous passthrough for sensitive case data unless the downstream trust path is visible.

## Example operating model

1. `epical-na` initializes a case-specific trust domain, for example `EPICAL-DSAR-CASE-NA`.
2. It enrolls the internal stage agents with signed roles:
   - `role:ingest`
   - `role:index`
   - `role:analyse`
   - `role:redact`
   - `role:produce`
3. It imports or validates trust bundles from selected initial-backer services.
4. It creates recognition treaties for only the services needed by this case.
5. Each task request carries purpose, role, evidence scope, and expiry.
6. Revocation feeds are checked before every high-risk handoff.
7. At the end of the case, `epical-na` exports:
   - proof bundle;
   - Connectome snapshot;
   - redaction manifest;
   - deliverable trace;
   - list of revoked / expired access paths.

## Policy sketch

```json
{
  "sovereign": "epical-na",
  "connectome_center": "MiraOS-NA",
  "purpose": "employee-dsar-gdpr-review",
  "allowed_internal_agents": [
    "epical-ingest",
    "epical-index",
    "epical-analyse",
    "epical-redact",
    "epical-produce"
  ],
  "allowed_external_service_classes": [
    "evidence-indexing",
    "privacy-redaction",
    "gdpr-analysis-support",
    "trust-bundle-validation",
    "secure-redacted-delivery"
  ],
  "default_external_access": "deny",
  "raw_evidence_external_access": "deny-unless-case-approved",
  "revocation_check": "before-each-cross-sovereign-handoff",
  "artifact_export": [
    "proof-bundle.json",
    "connectome.json",
    "redaction-manifest.json",
    "deliverable-trace.json"
  ]
}
```

## Why this matters for Epical

This turns the current DSAR agent project into a stronger compliance product pattern:

- less dependence on informal agent orchestration;
- clearer evidence lineage;
- safer use of external or community-provided services;
- demonstrable access control and revocation;
- reusable architecture for future DSAR, HR, identity, and enterprise-data review cases;
- a better story for security, legal, and regulator scrutiny.

## Non-claims and guardrails

- This document does not claim Epical has adopted Genesis Mesh.
- This document does not claim any initial backer is processing Epical data today.
- Initial backers should be named as operators or providers only when public proof artifacts and a signed treaty exist.
- Raw HR, identity, payroll, health, family, credential, and legal material should not leave `epical-na` without explicit case approval.
- External outputs are review aids, not final legal conclusions.

## Next implementation steps

1. Create an `epical-na` Genesis Mesh config and signed genesis artifact.
2. Define the five internal stage-agent roles as Genesis Mesh roles.
3. Draft the first policy manifest for evidence access and redaction handling.
4. Create an offline proof-bundle / Connectome validation gate for any demo artifacts.
5. Add a redaction manifest format so every deliverable can trace what was removed and why.
6. Only then evaluate recognition treaties with initial-backer service classes.
