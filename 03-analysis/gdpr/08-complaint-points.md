# Regulator-Ready Complaint Points

Use this as the basis for an IMY complaint or legal letter. The wording is intentionally factual rather than emotional.

## 1. Failure To Provide A Complete Article 15 Response

The controller received a clear Article 15 DSAR on 2026-01-27. The request covered HR records, email, internal communications, system logs, audit trails, access records, collaboration platforms, tickets, messaging tools, and structured/unstructured datasets.

The reviewed export contains no complete final Article 15 response setting out the required information under Article 15(1)(a)-(h), including purposes, categories, recipients, retention periods, source, rights, complaint route, or automated decision-making/profiling information.

Evidence:

- `Teams\Fw Strategic Assessment, GDPR Article 15 Request, and DataOps Growth Opportunity_text.txt:66-84,125`
- `gdpr\02-missing-article-15-response.md`

## 2. Incomplete Search And Missing Data Sources

The controller's own internal dossier says the data source inventory was pending and that IT logs were pending. This conflicts with the DSAR scope and with the extension notice, which acknowledged that specialist IT support was needed.

Evidence:

- `Sharepoint\Thaer_DSAR_Dossier_With_HR_Details.docx`, extracted lines 52-56.
- `Teams\DSAR_Extension_Notice_2026-02-13_text.txt:43-49`
- `gdpr\03-incomplete-search-and-omissions.md`

## 3. Omission Of Known HR And Legal Case Documents

The apparent DSAR case folder does not contain key HR/legal documents that the broader export proves existed, including HR case notes, dismissal notice, Unionen notice, and mutual separation agreement.

Evidence:

- `Sharepoint\Epical HR case notes TS.docx`
- `Teams\Epical HR case notes TS_text.txt`
- `Sharepoint\20260220 Epical - Intended summary dismissal _ termination due to personal reasons.pdf`
- `Teams\20260220 Epical - Intended summary dismissal _ termination due to personal reasons_text.txt`
- `Sharepoint\20260220 Varsel Unionen.pdf`
- `Teams\20260220 Varsel Unionen_text.txt`
- `Sharepoint\20260227 Epical Överenskommelse.docx.pdf`
- `Teams\20260227 Epical Överenskommelse.docx_text.txt`
- `gdpr\03-incomplete-search-and-omissions.md`

## 4. Overbroad Use Of Article 15(4)

The internal dossier excludes whole categories such as complete mailboxes, full email conversations, Teams threads, attachments, business information, and security logs. Article 15(4) requires protection of others' rights but does not justify blanket exclusion without assessing and disclosing the requester's personal data through redaction, extracts, or summaries where appropriate.

Evidence:

- `Sharepoint\Thaer_DSAR_Dossier_With_HR_Details.docx`, extracted lines 20-36.
- `gdpr\04-overbroad-exclusions.md`

## 5. Controller Identity Confusion

The extension notice says the personal data is processed by Nordcloud Hosting Sweden AB, while the employment documents identify Epical Sweden AB as employer and party to dismissal/separation documents. The reviewed materials do not explain which entity is the controller or the legal relationship between the entities.

Evidence:

- `Teams\DSAR_Extension_Notice_2026-02-13_text.txt:19-22`
- `Teams\20260220 Epical - Intended summary dismissal _ termination due to personal reasons_text.txt:27-35`
- `Teams\20260220 Varsel Unionen_text.txt:24-28`
- `Teams\20260227 Epical Överenskommelse.docx_text.txt:24-28`
- `gdpr\05-controller-identity-confusion.md`

## 6. Third-Party Data Over-Disclosure

The apparent DSAR package contains third-party HR-style payloads with birthdate, employment status, gender, termination date/reason, address, email, and collective-agreement context. This contradicts the internal dossier's stated rule that third-party personal data must be protected.

Evidence:

- `Items.1.001.GDPR_Case_T\Exchange\thaer.saidi@epicalgroup.com\TeamsMessagesData\Employee NCCUserID1001567NCCUse...html`
- `Sharepoint\Thaer_DSAR_Dossier_With_HR_Details.docx`, extracted lines 26-34.
- `gdpr\06-third-party-overdisclosure.md`

## 7. High-Risk Data Without Article 15 Explanation

The produced data includes national identity number, address, bank/IBAN information, sick leave, emergency contact and spouse data, HR investigation notes, dismissal data, and access revocation/security rationale. The reviewed materials do not include the required processing explanation for these categories.

Evidence:

- `TS Unit4 Data for GDPR.xlsx`
- `Teams\20260220 Epical - Intended summary dismissal _ termination due to personal reasons_text.txt:39-65`
- `Teams\Epical HR case notes TS_text.txt:13,33-47`
- `gdpr\07-sensitive-data-handling.md`

## 8. Separate PST Extraction Issue

The formal case extraction contains a 0-byte PST:

```text
Items.1.001.GDPR_Case_T\thaer.saidi@epicalgroup.com.001.pst
```

The root folder contains a large PST:

```text
thaer.saidi@epicalgroup.com.001.pst
```

This should be investigated because it may contain additional email evidence and responsive personal data not visible in the current extracted case folder.

## Requested Remedy

Ask IMY or the controller to require:

1. A complete Article 15(1)(a)-(h) response.
2. A source-by-source search record covering HR, email, Teams, SharePoint, access logs, audit logs, tickets, security systems, Unit4, Teamtailor, and legal/HR case files.
3. A withholding/redaction schedule identifying what was withheld and why.
4. Confirmation of the correct controller entity and legal basis for the Nordcloud/Epical identity change.
5. Remediation for any third-party over-disclosure.
6. Re-delivery of the DSAR response in a structured, intelligible, commonly used electronic format.

