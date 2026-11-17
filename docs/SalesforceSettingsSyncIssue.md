

# SalesforceSettingsSyncIssue

Set while the org refuses Zernio's writes for a reason only its admin can fix (field-level security, a validation rule, a duplicate rule); cleared by the next accepted write. The account's health shows it too.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | The Salesforce error code, such as &#x60;FIELD_CUSTOM_VALIDATION_EXCEPTION&#x60;. |  |
|**message** | **String** |  |  |
|**at** | **OffsetDateTime** |  |  |



