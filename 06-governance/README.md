# 06 - Governance

This folder is the post-POC operating model for the Genesis Mesh employee GDPR compliance mesh.

It assumes the initial proof of concept succeeded:

- the existing DSAR pipeline ran end-to-end;
- `MiraOS-NA` was modeled as the Genesis Mesh sovereign anchor;
- `EPICAL-NA` / `epical-na` was modeled as the employee-GDPR Network Authority;
- internal stage agents were mapped to signed, scoped, revocable roles;
- Thaer's case was used as a privacy-preserving baseline, not as public demo data;
- Nordcloud-style influence / feedback-loop risk was separated from direct evidence;
- backer-service participation was constrained by treaty, purpose, data class, and validity window.

The purpose of this folder is to make that success operational. These files turn the narrative into reusable governance artifacts for future employee GDPR cases.

## Reading order

1. [`../GENESIS_MESH_EMPLOYEE_GDPR_CONTROL_PLANE.md`](../GENESIS_MESH_EMPLOYEE_GDPR_CONTROL_PLANE.md) — root control-plane thesis.
2. [`case-manifest.example.yaml`](case-manifest.example.yaml) — one governed case constitution.
3. [`agent-roles.yaml`](agent-roles.yaml) — signed internal and reviewer roles.
4. [`evidence-classes.yaml`](evidence-classes.yaml) — data classes and handling boundaries.
5. [`influence-map.md`](influence-map.md) — evidence vs interpretation vs feedback-loop controls.
6. [`source-coverage-matrix.md`](source-coverage-matrix.md) — what was expected, received, indexed, and still missing.
7. [`regulator-pack-index.md`](regulator-pack-index.md) — how the governed case can be explained externally.

## Non-claim

These files are filled as the target operating model after a successful POC. They do not claim that Epical, Nordcloud, or any named third party has formally adopted Genesis Mesh unless that adoption is separately evidenced.
