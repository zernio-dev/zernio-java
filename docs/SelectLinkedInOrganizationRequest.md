

# SelectLinkedInOrganizationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**profileId** | **String** |  |  |
|**tempToken** | **String** |  |  |
|**userProfile** | **Object** |  |  |
|**accountType** | [**AccountTypeEnum**](#AccountTypeEnum) | Send this (with selectedOrganization for an organization) or selections, not both. |  [optional] |
|**selections** | [**List&lt;SelectLinkedInOrganizationRequestSelectionsInner&gt;**](SelectLinkedInOrganizationRequestSelectionsInner.md) | Several accounts to connect from one sign-in (yourself and/or organizations), each as its own account. With two or more entries the response lists &#x60;accounts&#x60; and &#x60;failed&#x60; instead of &#x60;account&#x60;, and the request is refused with 400 while a profile holds one LinkedIn account and on a reconnect or an ads connect. A single entry behaves exactly like accountType. |  [optional] |
|**selectedOrganization** | [**SelectLinkedInOrganizationRequestSelectedOrganization**](SelectLinkedInOrganizationRequestSelectedOrganization.md) |  |  [optional] |
|**redirectUrl** | **URI** |  |  [optional] |



## Enum: AccountTypeEnum

| Name | Value |
|---- | -----|
| PERSONAL | &quot;personal&quot; |
| ORGANIZATION | &quot;organization&quot; |



