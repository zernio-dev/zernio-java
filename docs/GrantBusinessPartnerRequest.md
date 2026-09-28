

# GrantBusinessPartnerRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**businessId** | **String** | Meta business portfolio id of the partner (numeric string). |  |
|**permittedTasks** | [**List&lt;PermittedTasksEnum&gt;**](#List&lt;PermittedTasksEnum&gt;) | Tasks granted on the Page, Meta&#39;s permitted_tasks vocabulary. Defaults to ADVERTISE and ANALYZE. The bare names are what Business Settings shows; the PROFILE_PLUS_ names are the New Pages Experience tasks and the only way to grant FACEBOOK_ACCESS or REVENUE. Granting MANAGE also yields MANAGE_LEADS. |  [optional] |



## Enum: List&lt;PermittedTasksEnum&gt;

| Name | Value |
|---- | -----|
| MANAGE | &quot;MANAGE&quot; |
| CREATE_CONTENT | &quot;CREATE_CONTENT&quot; |
| MODERATE | &quot;MODERATE&quot; |
| MESSAGING | &quot;MESSAGING&quot; |
| ADVERTISE | &quot;ADVERTISE&quot; |
| ANALYZE | &quot;ANALYZE&quot; |
| MODERATE_COMMUNITY | &quot;MODERATE_COMMUNITY&quot; |
| MANAGE_JOBS | &quot;MANAGE_JOBS&quot; |
| PAGES_MESSAGING | &quot;PAGES_MESSAGING&quot; |
| PAGES_MESSAGING_SUBSCRIPTIONS | &quot;PAGES_MESSAGING_SUBSCRIPTIONS&quot; |
| READ_PAGE_MAILBOXES | &quot;READ_PAGE_MAILBOXES&quot; |
| VIEW_MONETIZATION_INSIGHTS | &quot;VIEW_MONETIZATION_INSIGHTS&quot; |
| MANAGE_LEADS | &quot;MANAGE_LEADS&quot; |
| CASHIER_ROLE | &quot;CASHIER_ROLE&quot; |
| GLOBAL_STRUCTURE_MANAGEMENT | &quot;GLOBAL_STRUCTURE_MANAGEMENT&quot; |
| PROFILE_PLUS_FULL_CONTROL | &quot;PROFILE_PLUS_FULL_CONTROL&quot; |
| PROFILE_PLUS_MANAGE | &quot;PROFILE_PLUS_MANAGE&quot; |
| PROFILE_PLUS_FACEBOOK_ACCESS | &quot;PROFILE_PLUS_FACEBOOK_ACCESS&quot; |
| PROFILE_PLUS_CREATE_CONTENT | &quot;PROFILE_PLUS_CREATE_CONTENT&quot; |
| PROFILE_PLUS_MODERATE | &quot;PROFILE_PLUS_MODERATE&quot; |
| PROFILE_PLUS_MODERATE_DELEGATE_COMMUNITY | &quot;PROFILE_PLUS_MODERATE_DELEGATE_COMMUNITY&quot; |
| PROFILE_PLUS_MESSAGING | &quot;PROFILE_PLUS_MESSAGING&quot; |
| PROFILE_PLUS_ADVERTISE | &quot;PROFILE_PLUS_ADVERTISE&quot; |
| PROFILE_PLUS_ANALYZE | &quot;PROFILE_PLUS_ANALYZE&quot; |
| PROFILE_PLUS_REVENUE | &quot;PROFILE_PLUS_REVENUE&quot; |
| PROFILE_PLUS_MANAGE_LEADS | &quot;PROFILE_PLUS_MANAGE_LEADS&quot; |
| PROFILE_PLUS_CREATIVE_MANAGEMENT | &quot;PROFILE_PLUS_CREATIVE_MANAGEMENT&quot; |
| PROFILE_PLUS_CREATOR_MANAGEMENT | &quot;PROFILE_PLUS_CREATOR_MANAGEMENT&quot; |
| PROFILE_PLUS_GLOBAL_STRUCTURE_MANAGEMENT | &quot;PROFILE_PLUS_GLOBAL_STRUCTURE_MANAGEMENT&quot; |



