

# CreateStandaloneAd201ResponseOneOf1

Multi-creative shape: N ads returned sharing platformCampaignId / platformAdSetId.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ads** | [**List&lt;Ad&gt;**](Ad.md) |  |  [optional] |
|**platformCampaignId** | **String** |  |  [optional] |
|**platformAdSetId** | **String** |  |  [optional] |
|**appliedDefaults** | [**AdAppliedDefaults**](AdAppliedDefaults.md) |  |  [optional] |
|**message** | **String** |  |  [optional] |
|**warnings** | **List&lt;String&gt;** | Meta only, present only when needed. An &#x60;activation_failed:&#x60; entry means Meta refused the final switch to ACTIVE for the ads it names (or for their ad set or campaign): the entry names what was kept PAUSED and what was switched ACTIVE, and quotes Meta&#39;s error and the status calls that switch the PAUSED ones on later. |  [optional] |



