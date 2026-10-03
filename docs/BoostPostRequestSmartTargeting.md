

# BoostPostRequestSmartTargeting

TikTok only (a 400 elsewhere). TikTok Smart Targeting on the ad group: `audience` is TikTok's `smart_audience_enabled`, `interestsBehaviors` its `smart_interest_behavior_enabled`. When on, TikTok may deliver beyond the selected audiences or interests. Available on Video views, Traffic, Lead generation, App install, Web conversion and Community interaction. Only the flags you send are written; an unwritten flag reads back null in `nativeSettings`, so send `false` explicitly to be able to verify it is off. Not available with smartPlus or when attaching to an existing ad set (adSetId). 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**audience** | **Boolean** | TikTok smart_audience_enabled. |  [optional] |
|**interestsBehaviors** | **Boolean** | TikTok smart_interest_behavior_enabled. |  [optional] |



