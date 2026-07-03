

# CreateInviteTokenRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**scope** | [**ScopeEnum**](#ScopeEnum) | &#39;all&#39; grants access to all profiles, &#39;profiles&#39; restricts to specific profiles |  |
|**profileIds** | **List&lt;String&gt;** | Required if scope is &#39;profiles&#39;. Array of profile IDs to grant access to. |  [optional] |
|**role** | [**RoleEnum**](#RoleEnum) | Org role granted to the invitee. Defaults to &#39;member&#39;. &#39;admin&#39; can manage the team (invite/remove members, change roles and access) and billing, but not ownership transfer or account deletion. &#39;billing_admin&#39; (displayed as Billing Manager) manages billing only. &#39;viewer&#39; creates a read-only member who can view everything in their profile scope but cannot perform any content mutation (publish, edit, delete, connect accounts). |  [optional] |
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



