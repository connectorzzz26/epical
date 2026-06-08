# Sensitive And High-Risk Personal Data Handling

## Finding

The evidence contains high-risk personal data: personal identity number, address, bank/IBAN, sick leave, emergency contact, spouse/relationship data, HR investigation notes, access revocation, and employment termination data. The reviewed materials do not show a complete Article 15 explanation of purposes, recipients, retention, sources, or safeguards for these categories.

## Evidence: Unit4 Personal Data Export

Evidence file:

- `01-ingest/Unit4/TS Unit4 Data for GDPR.xlsx`

Observed workbook sheets:

```text
Parameters
TS Personal Data
Absences
Emergency contact
```

Observed fields in `TS Personal Data`:

```text
Resource ID
First name
Name
Date from / Date to
Status
Age
Birthdate
Gender
Language
NI Number
Bank account
IBAN
Probation period
Termination reason
Country
Location
Seniority date
Leaver
Leave date
Reason for leaving
Street address
Mobile / Telephone / E-mail
```

Observed `Absences` rows:

```text
Vacation/Annual leave
Sick leave: 2025-09-30 to 2025-10-03
Flexible hours, whole day leave
```

Observed `Emergency contact` row:

```text
Name: Ons Allouche
Birthdate: 1991-02-05
Relationship: Wife
Address: Evenemangsgatan 34 LGH 2903
Mobile number
Next of kin: True
```

## Evidence: Dismissal Notice Contains Swedish Personal Identity Number And Address

Evidence file:

- `Teams\20260220 Epical - Intended summary dismissal _ termination due to personal reasons_text.txt`

Extracted lines:

```text
39-45: Name, personal identity number, address.
49-65: intended summary dismissal / termination due to personal reasons.
```

## Evidence: HR Case Notes Include Sickness And Access Revocation

Evidence file:

- `Teams\Epical HR case notes TS_text.txt`

Extracted lines:

```text
13: Epical chose to revoke both internal and client access ...
33-36: revoked TS accesses ... internal investigation ... sick leave certificate.
39-47: employment could not continue ... broken trust ... Unionen ... paid leave and access remains revoked.
```

## Why This Is A Strong GDPR Point

This is not merely administrative data. It includes:

- national identity number;
- bank/IBAN data;
- sickness absence;
- next-of-kin data;
- employment investigation data;
- access revocation/security rationale;
- dismissal and union notification data.

For an Article 15 response, the controller should explain at least:

- why each category is processed;
- categories of recipients;
- retention periods;
- data sources;
- safeguards;
- rights and complaint route;
- any automated processing/profiling if applicable.

The reviewed export shows data values but not the legally required processing explanation.

## Complaint Wording

Epical/Nordcloud processed and disclosed high-risk employment and identity data without providing the required Article 15 processing information. The exported data includes national identity number, bank/IBAN information, sickness absence, emergency contact and spouse data, HR investigation data, and dismissal data, but the reviewed response materials do not explain purposes, recipients, retention, sources, safeguards, or rights.

