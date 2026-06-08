# GDPR Evidence Pack - Epical / Nordcloud DSAR

This folder summarises the GDPR non-compliance evidence found in the local export at `c:\Source\epical`.

Scope reviewed:

- `Teams\*.txt`
- `Sharepoint\*.docx`, `*.pdf`, `*.xlsx`, `*.png`, `*.msg`
- `Items.1.001.GDPR_Case_T\...`
- `TS Unit4 Data for GDPR.xlsx`

Important limitation: the raw PST archives were not fully parsed because this environment does not have a PST reader. The extracted Teams/Exchange/SharePoint material was reviewed directly. Notably, `Items.1.001.GDPR_Case_T\thaer.saidi@epicalgroup.com.001.pst` is a 0-byte file, while the root `thaer.saidi@epicalgroup.com.001.pst` is large and needs separate PST extraction.

## Core Conclusion

The evidence supports a strong GDPR complaint on these grounds:

1. The Article 15 response appears incomplete or missing.
2. The search/inventory was incomplete, with key systems marked pending.
3. Epical/Nordcloud used overbroad exclusion language for email, Teams, attachments, and logs.
4. The controller identity is inconsistent: Nordcloud Hosting Sweden AB vs Epical Sweden AB.
5. The DSAR package appears to over-disclose third-party personal data.
6. Sensitive/special-category-adjacent employment data was handled without clear Article 15 explanation.
7. The DSAR package omits documents Epical clearly held in the broader export.

## Legal Benchmarks Used

- GDPR Article 12: response without undue delay and within one month, extendable by two months only when necessary and with reasons.
- GDPR Article 15: right of access includes the personal data and information about purposes, categories, recipients, retention, rights, source, and automated decision-making/profiling.
- GDPR Article 15(4): rights and freedoms of others may limit copies, but it is not a blanket exemption from access.
- GDPR Article 5(1)(c) and 5(1)(f): data minimisation, integrity, and confidentiality.
- EDPB Guidelines 01/2022 on data subject rights - right of access.
- IMY right to complain to the Swedish supervisory authority.

## Files In This Evidence Pack

- `01-timeline.md` - verified timeline.
- `02-missing-article-15-response.md` - missing mandatory Article 15 elements.
- `03-incomplete-search-and-omissions.md` - missing systems and documents.
- `04-overbroad-exclusions.md` - misuse of Article 15(4) and blanket exclusions.
- `05-controller-identity-confusion.md` - Nordcloud vs Epical controller issue.
- `06-third-party-overdisclosure.md` - third-party personal data in disclosure.
- `07-sensitive-data-handling.md` - sensitive HR, sick leave, ID, bank, and emergency contact data.
- `08-complaint-points.md` - regulator-ready complaint allegations.

