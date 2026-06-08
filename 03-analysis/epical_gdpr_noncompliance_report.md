# Epical GDPR case - evidence-backed non-compliance analysis

Scope reviewed: /mnt/c/Source/epical. Automated inventory indexed 5,838 extractable documents, including 5,571 text exports, 71 DOCX, 22 PDF, 17 XLSX, 14 PPTX, 78 ASPX, 56 HTML and 7 CSV files. This is not legal advice, but an evidence map for a GDPR complaint/legal review.

Executive conclusion: I found multiple strong apparent GDPR compliance failures. The strongest are over-disclosure / insecure handling of third-party employee data, BankID signature artifacts, broad HR/payroll/union spreadsheets, and a DSAR handling dossier that appears incomplete and relies on broad exclusions. These are not minor paperwork issues; they go to GDPR core principles: data minimisation, confidentiality/security, accountability, Article 15 completeness, and protection of third-party rights.


## F1. DSAR handling dossier shows incomplete inventory / pre-decided limitations

Severity: High

GDPR articles implicated: Articles 12(3), 12(4), 15(1), 15(3), 5(2)

Evidence: Internal DSAR dossier records request in mid-January 2026 and lists “Inventory of Data Sources (Pending IT/HR Input)”; in one version: “HR systems: Pending”, “Email systems: Pending”, “Teams/Collaboration: Pending”, “IT logs: Pending”. It also states broad exclusions such as no “entire email mailboxes or raw system exports” and delivery only by encrypted USB.

Why this is non-compliant / challengeable: A controller may redact third-party/business secrets, but it must still identify and provide the requester’s personal data and Article 15(1)(a–h) information. A dossier that still has pending source inventories near/after the statutory period supports an accountability and completeness challenge. Blanket categorical refusal of full threads/exports is not enough unless they extract or summarize the requester’s personal data and explain refusals under Article 12(4).

Files:
- 01-ingest/Sharepoint/Thaer_DSAR_Dossier_With_HR_Details.docx
- 01-ingest/Sharepoint/Thaer_DSAR_Dossier_Filled_Sections.docx
- 01-ingest/Sharepoint/Thaer_DSAR_Dossier_Updated_A.docx


## F2. Extension notice deadline problem / controller identity ambiguity

Severity: Medium-High

GDPR articles implicated: Articles 12(3), 15

Evidence: DSAR extension notice says request submitted 27.1.2026 and response no later than 27.4.2026. It is from “Nordcloud Hosting Sweden AB / Nordcloud group Legal/DPO,” not clearly Epical Group, while Epical DSAR dossier states the request was submitted in mid-January and handled internally by Lars Rosenquist.

Why this is non-compliant / challengeable: Article 12(3) allows a two-month extension only when necessary, considering complexity/number of requests, and the controller must inform the data subject within one month of receipt. If Epical’s request was mid-January, a 13 Feb notice may be within one month only depending exact date; if received before 13 Jan, it is late. The mismatch between Epical/Nordcloud controller naming and dates should be challenged: who is the controller, what exact receipt date, and what exact extension applies?

Files:
- 01-ingest/Teams/DSAR_Extension_Notice_2026-02-13_text.txt
- 01-ingest/Sharepoint/DSAR_Extension_Notice_2026-02-13.pdf
- 01-ingest/Sharepoint/Thaer_DSAR_Dossier_With_HR_Details.docx


## F3. Unit4 export contains excessive sensitive HR/payroll/family/health-related data

Severity: High

GDPR articles implicated: Articles 5(1)(c), 5(1)(f), 9, 15(1)(b), 32

Evidence: 01-ingest/Unit4/TS Unit4 Data for GDPR.xlsx contains: Resource ID, first/name, birthdate/personal identity number, gender, bank account and IBAN, employment terms, location, seniority, leave data, absence records including “Sick leave”, and next-of-kin record containing wife name, address and mobile number.

Why this is non-compliant / challengeable: This is highly sensitive employment/financial/family data. If provided as a DSAR extract, it supports that Epical processed this data and had to disclose categories, purposes, recipients, retention and safeguards. If stored in an unprotected working folder/SharePoint export, it raises data minimisation, confidentiality and security concerns. Sick-leave/health-related absence may be special category data or at least sensitive employment data requiring heightened protection.

Files:
- 01-ingest/Unit4/TS Unit4 Data for GDPR.xlsx


## F4. Disclosure/retention of broad employee union/payroll list with 106 people

Severity: Very High

GDPR articles implicated: Articles 5(1)(c), 5(1)(e), 5(1)(f), 6, 32

Evidence: 01-ingest/Sharepoint/member-list (3).xlsx has 106 rows. Columns include Efternamn, Förnamn, Personnummer, Epost, Mobilnummer, Postadress, Arbetsställe, Klubb/Sektion, Fast lön, salary dates, employment dates and regional union affiliation. Examples include full Swedish personal identity numbers, private emails, private phone numbers, home addresses and monthly salary for many Epical Sweden employees.

Why this is non-compliant / challengeable: This is the strongest “big” issue found. A single spreadsheet exposes many non-requester employees’ personal identity numbers, private contact data, addresses, salaries, workplaces and union-related fields. If included in Thaer’s DSAR package or held in a broadly accessible SharePoint/Teams context, it is likely excessive and contrary to minimisation/confidentiality. Union affiliation can reveal trade-union membership, a special category under Article 9, unless carefully controlled. This could support a personal data breach / unauthorized disclosure argument.

Files:
- 01-ingest/Sharepoint/member-list (3).xlsx


## F5. BankID signature artifacts expose another person’s personal number, IP address, device identifier and full signature blob

Severity: Very High

GDPR articles implicated: Articles 5(1)(c), 5(1)(f), 6, 32

Evidence: 01-ingest/Sharepoint/BankIDSignatures.txt and 01-ingest/Teams/BankIDSignatures_text.txt include “SDO for Rudy Kyrönlahti” and “SDO for Thaer Saidi”; each record contains completionData.user.personalNumber, device.uhi, ipAddress, orderRef and a long XML signature/certificate payload.

Why this is non-compliant / challengeable: This is a major confidentiality/minimisation issue. BankID signature evidence is identity/security data. Including another individual’s personal number, IP/device identifier and signature material in a case/export unrelated to that person is difficult to justify. This is strong evidence of over-disclosure and weak handling of authentication/signature artifacts.

Files:
- 01-ingest/Sharepoint/BankIDSignatures.txt
- 01-ingest/Teams/BankIDSignatures_text.txt


## F6. Mass Teams/email exports include hundreds of people and personal identifiers

Severity: High

GDPR articles implicated: Articles 5(1)(c), 5(1)(f), 15(4), 32

Evidence: The scan indexed 5,838 extractable files; 5,571 are .txt extracted Teams/email-like files. 151 files contain personnummer-like values; 1,486 files contain 10+ unique email addresses. Large examples: 01-ingest/Teams/Apr 30 2025, 014231 PM - Epical People and Culture Sweden Sweden.PeopleAndCulture@epicalgroup.com;Ronny Karlsson ronny.karlsson@epicalgroup.com;Erik Håkansson erik.hakansson@epicalgroup.com;Abdul Bare abdul_text.txt (pnr-like=0, unique emails=186); 01-ingest/Teams/Apr 30 2025, 110123 AM - Ronny Karlsson ronny.karlsson@epicalgroup.com;Erik Håkansson erik.hakansson@epicalgroup.com;Abdul Bare abdul.bare@epicalgroup.com;Niklas Thulin niklas.thulin@epicalgroup_text.txt (pnr-like=0, unique emails=168); 01-ingest/Teams/Apr 30 2025, 110126 AM - Ronny Karlsson ronny.karlsson@epicalgroup.com;Erik Håkansson erik.hakansson@epicalgroup.com;Abdul Bare abdul.bare@epicalgroup.com;Niklas Thulin niklas.thulin@epicalgroup_text.txt (pnr-like=0, unique emails=168); 01-ingest/Teams/Apr 30 2025, 112109 AM - Epical People and Culture Sweden Sweden.PeopleAndCulture@epicalgroup.com;Ronny Karlsson ronny.karlsson@epicalgroup.com;Erik Håkansson erik.hakansson@epicalgroup.com;Abdul Bare abdul_text.txt (pnr-like=0, unique emails=184); 01-ingest/Teams/Apr 30 2025, 112212 AM - Epical People and Culture Sweden Sweden.PeopleAndCulture@epicalgroup.com;Ronny Karlsson ronny.karlsson@epicalgroup.com;Erik Håkansson erik.hakansson@epicalgroup.com;Abdul Bare abdul_text.txt (pnr-like=0, unique emails=185).

Why this is non-compliant / challengeable: The DSAR response appears to contain or be mixed with broad communication exports rather than narrowly extracted personal data about the requester. Article 15(4) protects rights/freedoms of others. Dumping large threads/distributions with many recipients, identifiers and third-party personal data is a likely minimisation/confidentiality failure unless all non-relevant personal data was redacted and access tightly controlled.

Files:
- 02-index/inventory.json
- 01-ingest/Teams/*.txt


## F7. Health/sick leave information about third parties appears in Teams exports

Severity: High

GDPR articles implicated: Articles 9, 5(1)(c), 5(1)(f), 32

Evidence: 01-ingest/Teams/Aug 18 2025... text states a named individual “had a minor heartattack last week so he will be on sick leave for the coming 2 week.” 01-ingest/Unit4/TS Unit4 Data for GDPR.xlsx also contains Thaer absence row “Sick leave”.

Why this is non-compliant / challengeable: Health and sick-leave information requires heightened confidentiality. Its presence in broad Teams exports strengthens an argument that Epical/Nordcloud needed careful redaction and access controls before processing/disclosing DSAR materials.

Files:
- 01-ingest/Teams/Aug 18 2025, 080744 AM - Henrik Wallenberg henrik.wallenberg@epicalgroup.com;Björn Hackberg Bjorn.Hackberg@epicalgroup.com;Mats Jönsson mats.jonsson@epicalgroup.com;Elisabeth Blom elisabeth.blom@epicalgroup_text.txt
- 01-ingest/Unit4/TS Unit4 Data for GDPR.xlsx


## F8. Security credentials and infrastructure access information present in exports

Severity: High

GDPR articles implicated: Articles 5(1)(f), 25, 32

Evidence: Search found Teams HTML containing “I just forwarded you the SFTP credentials for basware on the ncc email”; AzureRoleAssignments_02022026_text.txt exposes role assignments including Key Vault Secrets User, Service Bus Data Receiver/Sender and storage permissions across dev/test resources.

Why this is non-compliant / challengeable: Although some of this is business/security rather than personal data, GDPR Article 32 requires appropriate security of processing. Mixing identity, HR and access-control exports with credentials/access-role information raises breach impact and security-by-design concerns. It also shows why simple raw exports are unsafe and should have been reviewed/redacted.

Files:
- 01-ingest/case-exports/Items.1.001.GDPR_Case_T/.../I just forwarded you the SFTP credential...html
- 01-ingest/Teams/AzureRoleAssignments_02022026_text.txt


## Complaint framing

1. Ask IMY / relevant supervisory authority to investigate whether Epical/Nordcloud had a lawful basis and adequate safeguards for retaining and exporting third-party employee payroll, identity, address, union-related and BankID data in the DSAR case material.

2. Ask for an order requiring a complete Article 15 response: purposes, categories, recipients/categories of recipients, retention periods, source of data, safeguards for transfers, and meaningful copies/summaries of personal data from email/01-ingest/Teams/logs rather than blanket exclusions.

3. Ask whether the employee/member list and BankIDSignatures files constitute a personal data breach under Articles 33/34, especially if they were disclosed to the requester or broadly accessible internally.

4. Ask Epical to explain access controls, redaction process, data source inventory, exact DSAR receipt date, exact controller identity, and why third-party special-category/financial/identity data was present.


## Immediate strongest exhibits

- 01-ingest/Sharepoint/member-list (3).xlsx: 106 employees with personnummer, private contact details, address, salary, union/section field.

- 01-ingest/Sharepoint/BankIDSignatures.txt and 01-ingest/Teams/BankIDSignatures_text.txt: BankID completion data for Thaer and another person, including personal numbers, IP/device identifiers and full signature blobs.

- 01-ingest/Unit4/TS Unit4 Data for GDPR.xlsx: Thaer HR/payroll/IBAN/absence/next-of-kin export including sick leave and family contact details.

- 01-ingest/Sharepoint/Thaer_DSAR_Dossier_With_HR_Details.docx: internal DSAR analysis and pending inventory language.

- 01-ingest/Teams/DSAR_Extension_Notice_2026-02-13_text.txt: extension rationale/date/controller evidence.
