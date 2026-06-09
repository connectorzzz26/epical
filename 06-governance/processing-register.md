# Processing Register

Mini Article 30-style register for the governed employee GDPR baseline case.

| Processing activity | Purpose | Data categories | Roles/recipients | Lawful basis / GDPR hook | Controls |
| --- | --- | --- | --- | --- | --- |
| Evidence intake | Build DSAR source inventory | Raw exports, messages, documents, HR records | `epical-ingest`, `epical-na` | Article 15 response preparation; accountability | Internal-only, chain of custody. |
| Evidence indexing | Create searchable inventory | Text extracts, identifiers, metadata | `epical-index` | Article 15 completeness | Identifier minimisation, source refs. |
| GDPR analysis | Identify gaps/over-disclosure | Derived analysis, selected evidence | `epical-analyse`, legal reviewer | Articles 12, 15, 5, 25, 32 | Source-linked findings. |
| Redaction | Minimise disclosure | Third-party and sensitive data | `epical-redact` | Articles 5(1)(c), 5(1)(f) | Redaction log and policy. |
| Deliverable production | Prepare response/complaint packs | Approved redacted findings | `epical-produce`, counsel | Articles 15, 77, 82 | Review before sending. |
| Backer policy/coverage support | Validate governance controls | Metadata, policy, source inventory | treaty-bound service only | Accountability/security by design | No raw data by default. |

## Transfer status

Default: no international or external transfer of raw employee data. Any external/backer transfer must be treaty-bound and explicitly approved by data class.
