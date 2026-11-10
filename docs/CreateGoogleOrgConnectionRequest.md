

# CreateGoogleOrgConnectionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**profileId** | **String** |  |  |
|**domain** | **String** | The Workspace domain the admin delegates. |  |
|**scopes** | [**List&lt;ScopesEnum&gt;**](#List&lt;ScopesEnum&gt;) | Areas the mailboxes get, the same as a user connect. |  |
|**adminEmail** | **String** | A super admin, used to list the domain&#39;s users. |  [optional] |
|**allowedEmails** | **List&lt;String&gt;** | Addresses or &#x60;@domain&#x60; entries mailboxes must match. Omit for every mailbox. |  [optional] |



## Enum: List&lt;ScopesEnum&gt;

| Name | Value |
|---- | -----|
| EMAIL | &quot;email&quot; |
| CALENDAR | &quot;calendar&quot; |
| FILES | &quot;files&quot; |
| CONTACTS | &quot;contacts&quot; |



