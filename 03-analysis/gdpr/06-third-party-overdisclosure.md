# Third-Party Personal Data Over-Disclosure

## Finding

The apparent DSAR package includes Teams/Exchange HTML exports containing personal data about other people, including HR-style payloads for non-Thaer individuals. This creates a strong Article 5(1)(c), Article 5(1)(f), and Article 15(4) issue.

## Evidence: Internal Dossier Recognises Third-Party Data Must Be Protected

Evidence file:

- `Sharepoint\Thaer_DSAR_Dossier_With_HR_Details.docx`

Extracted lines:

```text
26: Third-Party Personal Data
27: Information containing personal data about other individuals cannot be disclosed unless it is possible to separate or redact their data without affecting the meaning.
28-30: employees; customers; external partners ...
31-34: business confidentiality and security data must be summarised or withheld where necessary.
```

## Evidence: Apparent DSAR Package Contains Third-Party HR Payloads

Evidence file:

- `Items.1.001.GDPR_Case_T\Exchange\thaer.saidi@epicalgroup.com\TeamsMessagesData\Employee NCCUserID1001567NCCUse...html`

Observed extracted content includes another employee-style record:

```text
businessobjectid: 10000997
globalbusinessobjectid: 1001567
BirthDate: 1986-07-30
EmployeeStatus: Terminated
Gender: Male
LastDateWorked: 2025-09-10
TerminationDate: 2025-09-10
EmploymentTerminationReason: Agreement
EmploymentType: Probation (SWE)
PhysicalAddress: Address Line 1, postal code, postal location, home address type
LogicalAddress: email address
UnionCollectiveAgreement: Tjanstemannaavtalet
```

Why this matters:

- This appears to be personal data about another employee or test employee, not the data subject.
- It includes employment status, termination details, address details, gender, email, and union/collective-agreement context.
- If disclosed to the DSAR requester without redaction, this contradicts the controller's own stated limitation rules.

## Evidence: Large Recipient Lists Contain Many Third Parties

Evidence examples:

- `Teams\Dec 18 2025, 073024 AM - Epical People and Culture Finland ..._text.txt`
- `Teams\Dec 18 2025, 080134 AM - Epical People and Culture Finland ..._text.txt`

Observed:

- Very large lists of employee names and email addresses are present.
- These may be relevant if the data subject was a recipient, but the controller still had to minimise and assess third-party data.

## Why This Is A Strong GDPR Point

This creates a two-sided non-compliance problem:

1. If Epical withheld your personal data too broadly, Article 15 was not fulfilled.
2. If Epical disclosed unrelated third-party HR data, Article 5 and Article 15(4) were breached.

Both can be true at the same time.

## Complaint Wording

Epical/Nordcloud failed to apply consistent redaction and data minimisation. The internal dossier states that third-party personal data must be protected, yet the apparent DSAR package contains third-party HR-style payloads including birthdate, gender, termination status, address data, email data, and collective-agreement context. This indicates inadequate review and over-disclosure of personal data unrelated to the requester.

