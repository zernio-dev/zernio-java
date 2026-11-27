

# BulkUpdateAdCampaignStatusRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**stage** | **Boolean** | Send true to store this write as a staged change instead of applying it. The response is &#x60;202&#x60; with the change, and POST /v1/ads/changes/{changeId}/confirm applies it later. Cannot be combined with &#x60;validateOnly&#x60;. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**campaigns** | [**List&lt;BulkUpdateAdCampaignStatusRequestCampaignsInner&gt;**](BulkUpdateAdCampaignStatusRequestCampaignsInner.md) |  |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| PAUSED | &quot;paused&quot; |



