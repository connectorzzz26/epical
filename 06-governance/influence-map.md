# Influence Map

## Purpose

This map keeps evidence, interpretation, feedback, and influence separate. It is designed for the Nordcloud-style feedback-loop risk pattern: informal influence must not silently become case evidence.

## Classification lanes

| Lane | Meaning | Can support final finding? | Required controls |
| --- | --- | --- | --- |
| Direct evidence | Source file, message, HR record, timestamped export, or system artifact. | Yes | Source path, timestamp, evidence class. |
| Third-party claim | A person's statement about events or another person. | Only with corroboration | Speaker, role, scope, confidence. |
| Reviewer feedback | HR/legal/security/stakeholder review. | Not by itself | Reviewer role, conflict check, review status. |
| Inferred interpretation | Analysis derived from multiple evidence items. | Yes, if traceable | Source references and rationale. |
| Disputed narrative | Claim challenged by employee or contradicted by evidence. | No until resolved | Challenge note and unresolved status. |
| Legal conclusion | Counsel/regulator-facing conclusion. | Yes, after review | Evidence references and legal reviewer status. |
| Rejected influence | Feedback considered out-of-scope, unsupported, biased, or conflicted. | No | Rejection reason and authority. |

## Baseline post-POC state

| Item | Lane | Status | Control decision |
| --- | --- | --- | --- |
| Raw Teams/SharePoint/HR exports | Direct evidence | Controlled | Internal-only processing under EPICAL-NA. |
| Source coverage gaps | Inferred interpretation | Active | Must be listed in source coverage matrix. |
| Nordcloud-style influence pattern | Risk pattern | Active | Discuss as governance risk, not unproven fact. |
| HR or stakeholder commentary | Reviewer feedback | Controlled | Cannot become evidence without source/corroboration. |
| Employee challenge points | Disputed narrative / challenge signal | Active | Must remain visible in regulator pack. |

## Rule

No feedback becomes evidence unless `epical-na` records who said it, why they were authorized to say it, what evidence supports it, and whether the employee can challenge it.
