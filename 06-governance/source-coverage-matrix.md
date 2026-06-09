# Source Coverage Matrix

| Source | Expected | Received | Indexed | Analysed | Gaps | Risk |
| --- | --- | --- | --- | --- | --- | --- |
| Exchange / Outlook mailbox | Yes | Partial / to verify | To verify | To verify | PST/full mailbox coverage must be confirmed. | Omission risk. |
| Teams messages | Yes | Yes | Yes | Yes | Confirm all channels/chats and date ranges. | Over-disclosure + third-party data risk. |
| SharePoint documents | Yes | Yes | Yes | Yes | Confirm HR/all-company/service libraries. | Hidden HR/support pages may be missed. |
| Unit4 HR/payroll | Yes | Partial / to verify | To verify | To verify | Need final workbook/source-system confirmation. | Critical sensitive-data risk. |
| BankID / signature artifacts | Yes where present | Yes where present | To verify | To verify | Need artifact class and redaction policy. | Identity/security risk. |
| Customer/supplier/project context | Yes where referenced | Yes where present | Partial | Partial | Need confidentiality classification. | Third-party confidentiality risk. |
| Controller/processor inventory | Yes | Incomplete / to verify | No | Partial | Need final controller identity and recipient list. | Article 15 incompleteness risk. |
| Retention/deletion records | Yes | Not confirmed | No | No | Need retention policy and deletion evidence. | Accountability risk. |

## Post-POC success definition

The POC is considered successful when every expected source is marked either:

1. received, indexed, analysed, and included/excluded with rationale; or
2. missing, with an explicit gap statement and follow-up action.
