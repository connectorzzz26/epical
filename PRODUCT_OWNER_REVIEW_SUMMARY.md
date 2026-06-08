# Product Owner Review Summary

Date: 2026-06-08  
Repository: `thaersaidi/epical`  
Subject: DSAR / GDPR evidence pipeline and deliverables review

---

## Purpose

This repository contains a structured DSAR and GDPR case-handling solution for employee enterprise data.

The goal is to take raw exported data from employer systems, index it, analyse it, reduce it to relevant evidence, and produce formal legal deliverables such as:

- a Letter Before Action;
- a complaint to IMY, the Swedish data protection authority;
- redacted evidence summaries;
- reusable scripts for generating the final documents.

The solution is designed around the matter concerning Thaer Saidi and Epical / Nordcloud, but the structure can also be reused for similar employee DSAR cases.

---

## What the solution does

The repository is organised as a five-stage pipeline:

1. **Ingest**  
   Collect raw exports from Microsoft 365, Teams, SharePoint, Exchange and HR systems.

2. **Index**  
   Build an inventory of files, extracted text, personal identifiers and relevant keywords.

3. **Analyse**  
   Map the discovered material against GDPR obligations and identify potential compliance gaps.

4. **Redact**  
   Reduce the material to the minimum evidence needed and mask third-party identifiers where possible.

5. **Produce**  
   Generate formal deliverables, including a Letter Before Action and an IMY complaint.

---

## Main review areas for the Product Owner

The Product Owner should review the solution from three angles:

1. **Functional completeness**  
   Does the pipeline cover the expected DSAR handling steps from raw data to final deliverables?

2. **Evidence quality**  
   Are the findings traceable to source files, exhibits and documented analysis?

3. **Governance and risk**  
   Is sensitive data handled carefully enough, especially third-party personal data, BankID artifacts, HR data and payroll information?

---

## Key findings currently captured

The case analysis currently highlights several potential GDPR issues:

- unclear controller responsibility between Epical / Nordcloud;
- possible missed Article 15 DSAR deadline;
- incomplete source inventory at the time of the response deadline;
- broad exclusions of email, Teams threads and attachments;
- handling of sensitive third-party employee data;
- BankID identity and signature artifacts in the material;
- HR, payroll, absence and next-of-kin data in Unit4 exports;
- third-party health or sick-leave information in broad exports;
- operational credentials and Azure role information appearing alongside personal data;
- possible need for personal data breach assessment under GDPR Articles 33 and 34.

These points should be treated as review findings until validated against the source evidence.

---

## Deliverables to review

The main generated deliverables are:

- `05-deliverables/Letter_Before_Action_Thaer_Saidi.docx`
- `05-deliverables/Complaint_to_IMY_Thaer_Saidi.docx`

The generator scripts are:

- `05-deliverables/generators/make_letter.py`
- `05-deliverables/generators/make_imy_complaint.py`

Additional internal assessment:

- `05-deliverables/findings_epical_lawyer_readiness.md`

---

## Product Owner validation checklist

The Product Owner should verify the following before approving the solution:

### Case facts

- Confirm the exact DSAR submission date.
- Confirm the exact extension notice date.
- Confirm whether the final deadline was 27 April 2026.
- Confirm whether a compliant Article 15 response was delivered.
- Confirm which entity is the correct controller: Epical, Nordcloud, both, or another group entity.

### Evidence

- Confirm that every major finding is linked to a source file or exhibit.
- Confirm that sensitive third-party data is redacted before external sharing.
- Confirm that BankID artifacts are handled with extra care.
- Confirm that payroll, IBAN, family and health data are not unnecessarily exposed.
- Confirm that the evidence pack is complete enough for counsel or IMY review.

### Legal deliverables

- Complete all placeholders in the DOCX outputs.
- Add correct company registration numbers and addresses.
- Add correct law firm / counsel details if a lawyer is sending the letter.
- Review whether the IMY complaint should be translated or filed in Swedish.
- Ensure the final text is reviewed by counsel before external use.

### Repository governance

- Review whether this repository should remain public.
- Review whether sensitive evidence should be removed, encrypted or moved to a private evidence store.
- Confirm that `.gitignore` protects large and sensitive raw exports.
- Confirm that no raw personal data is accidentally exposed in generated files.
- Confirm that future users understand the confidentiality rules.

---

## Risks requiring Product Owner attention

### 1. Sensitive data exposure risk

The repository may contain or reference highly sensitive personal data. This includes personal identity numbers, salary data, HR records, BankID artifacts, family information and health-related data.

The Product Owner should treat data minimisation and access control as priority review items.

### 2. Public repository risk

If the repository is public, this creates a serious governance issue. Even if some raw files are git-ignored, extracted text, summaries or metadata may still reveal personal data.

The Product Owner should decide whether the repository should be made private or split into:

- a public reusable framework; and
- a private confidential evidence repository.

### 3. Legal wording risk

The deliverables are strong but should not be sent without legal review. The wording must remain factual, evidence-based and proportionate.

### 4. Evidence traceability risk

Any claim in the Letter Before Action or IMY complaint should be traceable to a specific exhibit. Findings that cannot be proven should be softened or removed.

---

## Suggested Product Owner decision points

The Product Owner should decide:

1. Is the current pipeline structure approved?
2. Are the deliverables fit for counsel review?
3. Should the repository be made private?
4. Should raw evidence be separated from generated documents?
5. Are additional redaction controls needed?
6. Should a Swedish version of the IMY complaint be produced?
7. Should the solution include a formal evidence register?
8. Should the generated DOCX files include exhibit cross-references?
9. Should the pipeline include automated checks for personal identity numbers, IBANs and BankID artifacts?
10. Should there be a final sign-off checklist before any external delivery?

---

## Recommended next steps

1. Freeze the current evidence snapshot.
2. Verify all factual claims against source files.
3. Move sensitive material to a controlled private location if not already done.
4. Complete all placeholders in the deliverables.
5. Ask counsel to review the Letter Before Action and IMY complaint.
6. Add an evidence register with source path, description, GDPR issue and redaction status.
7. Add automated checks for sensitive identifiers before commit.
8. Decide whether the repository should be public, private or split into public/private parts.

---

## Bottom line

The solution is useful and structured, but it handles sensitive legal and personal-data material. The Product Owner review should focus less on document formatting and more on evidence quality, confidentiality, redaction, traceability and safe external use.

The deliverables are suitable as drafts for counsel review, not as final external submissions without validation.
