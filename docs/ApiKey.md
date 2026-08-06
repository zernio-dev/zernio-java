

# ApiKey


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**keyPreview** | **String** |  |  [optional] |
|**expiresAt** | **OffsetDateTime** |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**key** | **String** | Returned only once, on creation |  [optional] |
|**scope** | [**ScopeEnum**](#ScopeEnum) | &#39;full&#39; grants access to all profiles, &#39;profiles&#39; restricts to specific profiles |  [optional] |
|**profileIds** | [**List&lt;ApiKeyProfileIdsInner&gt;**](ApiKeyProfileIdsInner.md) | Profiles this key can access (populated with name and color). Only present when scope is &#39;profiles&#39;. |  [optional] |
|**permission** | [**PermissionEnum**](#PermissionEnum) | &#39;read-write&#39; allows all operations, &#39;read&#39; restricts to GET requests only |  [optional] |
|**disabledResourceGroups** | [**List&lt;DisabledResourceGroupsEnum&gt;**](#List&lt;DisabledResourceGroupsEnum&gt;) | Resource groups this key can NOT access (opt-out denylist). Absent or empty means legacy full access. A key with any group disabled is a restricted key (zrk_ prefix) and can never manage API keys, invites, or member identity. Each operation&#39;s group is published as x-resource-group. With &#39;messages&#39; disabled, the key cannot read or send private messages through any API surface, and it cannot create or edit a webhook subscription broader than itself: it cannot subscribe to, test-fire, redeliver, or read delivery logs for message events. Subscriptions created earlier, from the dashboard, or with a full-access key keep delivering whatever their own &#x60;disabledResourceGroups&#x60; allows, so restricting an existing integration end to end means restricting the subscription too. OAuth connector tokens (AI assistants and MCP clients) resolve against the same registry, but their groups are not settable yet: treat an authorized connector as full access. |  [optional] |



## Enum: ScopeEnum

| Name | Value |
|---- | -----|
| FULL | &quot;full&quot; |
| PROFILES | &quot;profiles&quot; |



## Enum: PermissionEnum

| Name | Value |
|---- | -----|
| READ_WRITE | &quot;read-write&quot; |
| READ | &quot;read&quot; |



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



