

# DuplicateAdCampaign200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**copiedCampaignId** | **String** | Platform ID of the new campaign |  [optional] |
|**discovery** | [**DiscoveryEnum**](#DiscoveryEnum) |  |  [optional] |
|**raw** | **Object** | Platform-native response from the copy endpoint (Meta includes ad_object_ids for child copies) |  [optional] |



## Enum: DiscoveryEnum

| Name | Value |
|---- | -----|
| TRIGGERED | &quot;triggered&quot; |
| SKIPPED | &quot;skipped&quot; |
| FAILED | &quot;failed&quot; |



