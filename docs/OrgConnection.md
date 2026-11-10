

# OrgConnection

A Google Workspace domain or Microsoft 365 tenant whose administrator granted Zernio access to its mailboxes once.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**provider** | [**ProviderEnum**](#ProviderEnum) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**profileId** | **String** |  |  [optional] |
|**areas** | [**List&lt;AreasEnum&gt;**](#List&lt;AreasEnum&gt;) |  |  [optional] |
|**domain** | **String** |  |  [optional] |
|**tenantId** | **String** |  |  [optional] |
|**adminEmail** | **String** |  |  [optional] |
|**allowedEmails** | **List&lt;String&gt;** |  |  [optional] |
|**lastError** | **String** |  |  [optional] |
|**verifiedAt** | **OffsetDateTime** |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**setup** | [**OrgConnectionSetup**](OrgConnectionSetup.md) |  |  [optional] |



## Enum: ProviderEnum

| Name | Value |
|---- | -----|
| GOOGLE | &quot;google&quot; |
| MICROSOFT | &quot;microsoft&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| ACTIVE | &quot;active&quot; |
| REVOKED | &quot;revoked&quot; |



## Enum: List&lt;AreasEnum&gt;

| Name | Value |
|---- | -----|
| EMAIL | &quot;email&quot; |
| CALENDAR | &quot;calendar&quot; |
| FILES | &quot;files&quot; |
| CONTACTS | &quot;contacts&quot; |



