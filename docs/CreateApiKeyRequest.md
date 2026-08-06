

# CreateApiKeyRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  |
|**expiresIn** | **Integer** | Days until expiry |  [optional] |
|**scope** | [**ScopeEnum**](#ScopeEnum) | &#39;full&#39; grants access to all profiles (default), &#39;profiles&#39; restricts to specific profiles |  [optional] |
|**profileIds** | **List&lt;String&gt;** | Profile IDs this key can access. Required when scope is &#39;profiles&#39;. |  [optional] |
|**permission** | [**PermissionEnum**](#PermissionEnum) | &#39;read-write&#39; allows all operations (default), &#39;read&#39; restricts to GET requests only |  [optional] |
|**disabledResourceGroups** | [**List&lt;DisabledResourceGroupsEnum&gt;**](#List&lt;DisabledResourceGroupsEnum&gt;) | Resource groups to DISABLE on this key (opt-out denylist). Omit for a legacy full-access key. A key with any group disabled mints with the zrk_ prefix, gets 403 with code&#x3D;insufficient_permissions and required_group on operations in disabled groups (each operation&#39;s group is published as x-resource-group), and can never manage API keys, invites, or member identity. With &#39;messages&#39; disabled, the key cannot read or send private messages through any API surface and cannot create or edit a webhook subscription broader than itself. Subscriptions that already exist are governed by their own &#x60;disabledResourceGroups&#x60;, not by this key&#39;s. OAuth connector tokens resolve against the same registry, but their groups are not settable yet. |  [optional] |



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



