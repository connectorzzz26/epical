# Epical / Nordcloud DSAR Matter — Lawyer Readiness Findings

Date: 2026-06-08  
Subject: Thaer Saidi DSAR / GDPR compliance position  
Scope: Internal case assessment based on the current deliverables and evidence structure in this repository.

> Working note: This document is a structured findings summary for case preparation. It is not legal advice by itself and should be reviewed by counsel before being sent externally or relied upon in proceedings.

---

## Executive summary

Based on the current deliverables, Epical / Nordcloud appear to be in a weak handling position if Thaer Saidi appoints a lawyer to pursue the DSAR and GDPR issues formally.

The matter is stronger than a simple late-response complaint. The current case file combines several pressure points:

1. a potentially missed Article 15 GDPR response deadline;
2. uncertainty over the correct controller entity;
3. evidence that key DSAR source inventories remained pending;
4. broad exclusions of mailboxes, Teams threads and attachments;
5. alleged exposure or insecure handling of highly sensitive third-party data;
6. BankID identity/signature artifacts in the material;
7. possible Article 33/34 personal data breach assessment obligations.

If the factual exhibits are accurate and can be proven, the risk for Epical / Nordcloud is not only that the DSAR was delayed. The larger risk is that the matter may be framed as a wider failure of data minimisation, confidentiality, security, accountability and breach handling.

---

## Key findings

### 1. Article 15 deadline risk

The deliverables state that the controller invoked an extension and committed to respond by 27 April 2026. The draft position is that no compliant Article 15 response was provided by that date.

This is one of the cleanest points for a lawyer to press because it is simple:

- request made;
- extension invoked;
- final deadline identified;
- compliant response allegedly not delivered.

This supports potential allegations under Articles 12(3), 15(1) and 15(3) GDPR.

### 2. Controller identity is unclear

The case material suggests a mismatch between the entity handling the request and the entity issuing the extension notice:

- the request was submitted to / handled internally by Epical;
- the extension notice was issued by Nordcloud Hosting Sweden AB / Nordcloud Group Legal / DPO;
- the extension notice referred to Nordcloud and IBM systems.

This creates an accountability issue. A data subject must know which legal entity is responsible for processing and responding. If Epical and Nordcloud cannot clearly explain their roles as controller, joint controller or processor, this weakens their position.

Relevant GDPR framing:

- Article 5(2) accountability;
- Articles 12, 13 and 14 transparency;
- Article 15 right of access.

### 3. Pending source inventory weakens the DSAR defence

The draft deliverables refer to an internal DSAR dossier where source areas were still marked as pending, including:

- HR systems;
- email systems;
- Teams / collaboration;
- IT logs.

If accurate, this is important because a controller cannot easily defend a completed Article 15 response while its own source inventory remains incomplete. This supports the argument that the DSAR was not properly completed within the statutory period.

### 4. Blanket exclusions may not be enough

The draft findings state that Epical / Nordcloud excluded broad categories such as:

- entire email mailboxes or raw system exports;
- full email conversations or Teams threads;
- attachments or documents.

A controller may redact third-party data, confidential business material or irrelevant material. However, it still needs to identify and provide the data subject's own personal data, or provide intelligible extracts / summaries where full documents cannot be disclosed.

The strongest legal point is not that they had to disclose everything. The strongest point is that they could not rely on broad category exclusions without:

- extracting the data subject's own personal data;
- explaining what was withheld;
- giving specific reasons under Article 12(4).

### 5. Sensitive third-party data is the highest-risk part

The most serious risk area is the alleged presence of sensitive third-party personal data in the case material, especially:

- a spreadsheet listing 105 employees;
- Swedish personal identity numbers;
- private contact details;
- home addresses;
- salaries;
- trade-union club / section affiliation.

Trade-union affiliation can be special-category data under Article 9 GDPR. If this material was disclosed to Thaer Saidi, placed in a broad export, or made available internally without strict need-to-know controls, this creates significant exposure.

This could support allegations under:

- Article 5(1)(c) data minimisation;
- Article 5(1)(f) integrity and confidentiality;
- Article 6 lawful basis;
- Article 9 special-category data;
- Article 32 security of processing.

### 6. BankID artifacts create a serious security narrative

The deliverables describe BankID SDO / signature completion records containing:

- signer names;
- personal identity numbers;
- device identifiers;
- IP addresses;
- order references;
- XML signature / certificate payloads.

If BankID artifacts for Thaer Saidi and at least one unrelated third party are present in the material, this strengthens the security and confidentiality argument. It also makes the matter easier for a regulator to understand because BankID data is highly sensitive in the Swedish context.

Potential framing:

- excessive processing;
- insecure retention;
- insufficient redaction;
- poor access control;
- possible breach assessment duty.

### 7. Unit4 HR / payroll / family data adds personal impact

The material also describes a Unit4 HR export containing Thaer Saidi's:

- personal identity number;
- bank account / IBAN;
- employment terms;
- absence records;
- next-of-kin details for spouse.

This helps show personal impact and sensitivity. It also supports the argument that any DSAR response must be accompanied by Article 15 metadata, including purpose, categories, recipients, retention periods, source and safeguards.

### 8. Third-party health data and credentials increase regulatory concern

The drafts refer to:

- a message disclosing a named person's heart attack and sick leave;
- SFTP credentials for Basware;
- Azure role assignment exports.

These points are important because they show the issue is not only HR data. They suggest possible weak separation between personal data, health data and operational security material.

This supports the wider argument around Articles 25 and 32 GDPR: data protection by design and security of processing.

---

## Why a lawyer would have leverage

A lawyer could put pressure on Epical / Nordcloud by asking direct, hard-to-avoid questions:

1. Who exactly is the controller?
2. When exactly was the DSAR received?
3. Was the Article 12(3) extension validly notified within one month of receipt?
4. Was a complete Article 15 response delivered by 27 April 2026?
5. Why were HR, email, Teams and IT log inventories still marked as pending?
6. What personal data was withheld and why?
7. Why were whole categories excluded instead of extracting or summarising the data subject's personal data?
8. Was the 105-person employee spreadsheet disclosed or broadly accessible?
9. Were BankID artifacts disclosed, retained or broadly accessible?
10. Was a personal data breach assessment performed?
11. Was IMY notified under Article 33?
12. Were affected data subjects notified under Article 34?
13. What preservation steps have been taken to prevent deletion or alteration of evidence?

These questions shift the discussion from general disagreement to evidence, accountability and compliance proof.

---

## Practical risk rating

### DSAR deadline risk: High

If no compliant Article 15 response was delivered by 27 April 2026, this is a straightforward compliance weakness.

### Controller identity risk: Medium to High

The Epical / Nordcloud split creates confusion. If they cannot explain roles clearly, accountability risk increases.

### Data minimisation / third-party data risk: High

The 105-person list, trade-union information, BankID artifacts and health data are the strongest regulatory points.

### Security-of-processing risk: High

BankID material, SFTP credentials and Azure role exports support a broader Article 32 narrative.

### Breach-notification risk: Medium to High

This depends on whether the sensitive third-party material was actually disclosed externally or made broadly accessible internally. If yes, Articles 33 and 34 become much more important.

### Litigation / compensation risk: Medium

The compensation angle depends on proof of material or non-material damage. The better immediate leverage is likely compliance, disclosure, preservation and regulator escalation.

---

## Recommended legal posture

The strongest posture is disciplined and evidence-based:

- do not attack Epical personally;
- do not use emotional language;
- do not publish sensitive third-party material;
- keep the focus on GDPR rights, controller accountability and evidence preservation;
- let a lawyer send the letter if possible;
- preserve all source evidence and metadata;
- redact third-party personal data in any working copy sent outside counsel / IMY.

The message should be:

> Please comply with Article 15 GDPR, clarify controller responsibility, explain the handling of sensitive personal data, perform any required breach assessment, and preserve all evidence.

This is stronger than threatening language because it gives Epical / Nordcloud a clear compliance problem to answer.

---

## Counsel review checklist

Before sending the Letter Before Action or filing with IMY, counsel should verify:

- exact DSAR submission date;
- exact extension notice date;
- exact response deadline;
- whether any response was received after 27 April 2026;
- controller identity and company registration numbers;
- whether Epical Sweden AB, Epical Group AB and Nordcloud Hosting Sweden AB are all correctly named;
- whether IBM should be mentioned only as a system environment or also as a relevant entity;
- proof that the inventory was still pending;
- proof of the 105-person spreadsheet;
- proof of BankID artifacts;
- proof of Unit4 HR export contents;
- proof of third-party health data;
- proof of SFTP credential / Azure role material;
- redaction quality before external disclosure;
- impact statement from Thaer Saidi;
- preservation demand wording;
- whether the complaint should be filed in Swedish.

---

## Bottom line

If the evidence is accurate, Epical / Nordcloud are not in a comfortable position. The case has credible leverage because it combines a missed DSAR deadline with sensitive-data handling concerns.

The strongest route is to proceed through counsel with a clean Letter Before Action first, then escalate to IMY if they do not respond properly.
