

# CreateInviteTokenRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**scope** | [**ScopeEnum**](#ScopeEnum) | &#39;all&#39; grants access to all profiles, &#39;profiles&#39; restricts to specific profiles |  |
|**profileIds** | **List&lt;String&gt;** | Required if scope is &#39;profiles&#39;. Array of profile IDs to grant access to. |  [optional] |
|**role** | [**RoleEnum**](#RoleEnum) | Org role granted to the invitee. Defaults to &#39;member&#39;. &#39;admin&#39; can manage the team (invite/remove members, change roles and access) and billing, but not ownership transfer or account deletion. &#39;billing_admin&#39; (displayed as Billing Manager) manages billing only. &#39;viewer&#39; creates a read-only member who can view everything in their profile scope but cannot perform any content mutation (publish, edit, delete, connect accounts). |  [optional] |
|**disabledResourceGroups** | [**List&lt;DisabledResourceGroupsEnum&gt;**](#List&lt;DisabledResourceGroupsEnum&gt;) | Resource groups the invitee may not use once they join (the same groups as restricted API keys). Their dashboard hides those sections and every API request into a disabled group, with any credential they hold, is refused with 403. Omitted or empty means full access. Groups the caller lacks themselves are always added. |  [optional] |
|**readOnly** | **Boolean** | Deprecated. Use role &#39;viewer&#39; instead. When true, the invite is created with role &#39;viewer&#39;. Cannot be combined with role &#39;billing_admin&#39; or &#39;admin&#39;. |  [optional] |



## Enum: ScopeEnum

| Name | Value |
|---- | -----|
| ALL | &quot;all&quot; |
| PROFILES | &quot;profiles&quot; |



## Enum: RoleEnum

| Name | Value |
|---- | -----|
| ADMIN | &quot;admin&quot; |
| MEMBER | &quot;member&quot; |
| BILLING_ADMIN | &quot;billing_admin&quot; |
| VIEWER | &quot;viewer&quot; |



## Enum: List&lt;DisabledResourceGroupsEnum&gt;

| Name | Value |
|---- | -----|
| PUBLISHING | &quot;publishing&quot; |
| ENGAGEMENT | &quot;engagement&quot; |
| MESSAGES | &quot;messages&quot; |
| CONTACTS | &quot;contacts&quot; |
| ANALYTICS | &quot;analytics&quot; |
| ADS | &quot;ads&quot; |
| TELEPHONY | &quot;telephony&quot; |
| ACCOUNTS | &quot;accounts&quot; |
| BILLING | &quot;billing&quot; |
| WEBHOOKS | &quot;webhooks&quot; |
| COMMERCE | &quot;commerce&quot; |



