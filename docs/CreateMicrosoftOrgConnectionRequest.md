

# CreateMicrosoftOrgConnectionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**profileId** | **String** |  |  |
|**scopes** | [**List&lt;ScopesEnum&gt;**](#List&lt;ScopesEnum&gt;) |  |  |
|**allowedEmails** | **List&lt;String&gt;** | Addresses or &#x60;@domain&#x60; entries mailboxes must match. Omit for every mailbox. |  [optional] |
|**redirectUrl** | **URI** | Where Microsoft sends the administrator after consent. |  [optional] |



## Enum: List&lt;ScopesEnum&gt;

| Name | Value |
|---- | -----|
| EMAIL | &quot;email&quot; |
| CALENDAR | &quot;calendar&quot; |
| FILES | &quot;files&quot; |
| CONTACTS | &quot;contacts&quot; |



