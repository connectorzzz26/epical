# Risk Register

| Risk | Impact | Likelihood | Mitigation | Owner |
| --- | --- | --- | --- | --- |
| Raw evidence leak | Critical | Medium | Internal-only default; redaction policy; no raw backer transfer. | EPICAL-NA |
| Over-disclosure | High | High | Redaction policy and disclosure decision log. | epical-redact |
| Under-disclosure / omission | High | High | Source coverage matrix and employee challenge lane. | epical-index / legal |
| Hallucinated legal conclusion | High | Medium | Source-linked findings and legal review status. | epical-analyse |
| Hidden reviewer influence | High | Medium | Influence map and role-scoped feedback. | epical-na |
| Stale treaty | Medium | Medium | Validity windows and revocation log. | EPICAL-NA |
| Revoked service still trusted | High | Low/Medium | Revocation feed checks before service calls. | EPICAL-NA |
| Unclear controller identity | High | Medium | Processing register and regulator pack gap statement. | legal |
| Git/working-copy churn with sensitive exports | Medium | Medium | Avoid raw commits; keep longpaths/autocrlf controlled. | repo operator |
