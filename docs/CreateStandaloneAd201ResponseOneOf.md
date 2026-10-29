

# CreateStandaloneAd201ResponseOneOf

Legacy + attach shapes: one ad returned.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ad** | [**Ad**](Ad.md) |  |  [optional] |
|**appliedDefaults** | [**AdAppliedDefaults**](AdAppliedDefaults.md) |  |  [optional] |
|**message** | **String** |  |  [optional] |
|**warnings** | **List&lt;String&gt;** | Meta only, present only when needed.  An &#x60;activation_failed:&#x60; entry means Meta refused the final switch to ACTIVE. The entry names what was kept PAUSED (the ad, plus its ad set or campaign when Meta refused those) and what was switched ACTIVE, and quotes Meta&#39;s error and the status calls that switch the PAUSED ones on later.  |  [optional] |



