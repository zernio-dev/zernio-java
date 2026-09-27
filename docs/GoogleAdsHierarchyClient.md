

# GoogleAdsHierarchyClient

A Google Ads account inside a manager tree.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customerId** | **String** | Native Google Ads customer id, digits only. |  [optional] |
|**name** | **String** | Null for a pending invitation. |  [optional] |
|**currency** | **String** |  |  [optional] |
|**timeZone** | **String** |  |  [optional] |
|**manager** | **Boolean** | True for a sub-manager account. |  [optional] |
|**testAccount** | **Boolean** |  |  [optional] |
|**hidden** | **Boolean** | Hidden in the manager&#39;s Google Ads UI. |  [optional] |
|**level** | **Integer** | Distance from the root (1 &#x3D; direct client of the root). |  [optional] |
|**status** | **String** | Google customer status: ENABLED, CANCELED, SUSPENDED or CLOSED. Null for a pending invitation. |  [optional] |
|**parentCustomerId** | **String** | Direct manager of this account. Null only when more than 50 managers under the root were skipped. |  [optional] |
|**managerLinkId** | **String** | Id of the link to the parent, used by PATCH /v1/ads/accounts/manager-links. |  [optional] |
|**linkStatus** | [**LinkStatusEnum**](#LinkStatusEnum) |  |  [optional] |



## Enum: LinkStatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;ACTIVE&quot; |
| PENDING | &quot;PENDING&quot; |



