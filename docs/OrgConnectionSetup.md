

# OrgConnectionSetup

What the administrator does. Google returns `dnsRecord`, `adminConsoleUrl`, `clientId`, `scopes` and `directoryScope`; Microsoft returns `adminConsentUrl` and `applicationPermissions`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |
|**dnsRecord** | [**OrgConnectionSetupDnsRecord**](OrgConnectionSetupDnsRecord.md) |  |  [optional] |
|**adminConsoleUrl** | **URI** |  |  [optional] |
|**clientId** | **String** |  |  [optional] |
|**scopes** | **List&lt;String&gt;** |  |  [optional] |
|**directoryScope** | **String** |  |  [optional] |
|**adminConsentUrl** | **URI** |  |  [optional] |
|**applicationPermissions** | **List&lt;String&gt;** |  |  [optional] |
|**steps** | **List&lt;String&gt;** |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| GOOGLE_DOMAIN_WIDE_DELEGATION | &quot;google_domain_wide_delegation&quot; |
| MICROSOFT_ADMIN_CONSENT | &quot;microsoft_admin_consent&quot; |



