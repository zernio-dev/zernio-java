

# UpdateAdRequestTargeting

Meta + TikTok (demographics/interests), Google (keyword and device bid adjustment edits only), and LinkedIn (countries or regions required). Pinterest / X return 501. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**keywords** | [**List&lt;UpdateAdRequestTargetingKeywordsInner&gt;**](UpdateAdRequestTargetingKeywordsInner.md) | Google only. The FULL desired set of positive keywords for the entire ad group. Omit to leave positives unchanged; [] removes all positives. Negatives are independent. Entries are strings (BROAD) or { text, matchType } with matchType exact | phrase | broad; an omitted matchType also defaults to BROAD. Matching case-insensitive text AND match type retains the existing criterion ID, status, bid overrides, labels and history without a mutation. A changed text or match type uses remove/create, without transferring the old criterion&#39;s attributes or history. See Google keyword replacement above for an EXACT-to-BROAD example. Mirrored to GET /v1/ads/keywords immediately.  |  [optional] |
|**negativeKeywords** | [**List&lt;UpdateAdRequestTargetingKeywordsInner&gt;**](UpdateAdRequestTargetingKeywordsInner.md) | Google only. The FULL desired set of negative keywords for the entire ad group, independent of positives. Omit to leave negatives unchanged; [] removes all negatives. Uses the same text/match-type identity and preservation contract as keywords above. Strings and objects without matchType default to BROAD, so resending an EXACT or PHRASE negative as a bare string requests a different criterion. Campaign negatives are separate: use /v1/ads/campaigns/{campaignId}/negative-keywords to manage those.  |  [optional] |
|**devices** | [**List&lt;UpdateAdRequestTargetingDevicesInner&gt;**](UpdateAdRequestTargetingDevicesInner.md) | Google only. The FULL new set of device bid modifiers for the campaign. Entries are a device name alone (targeted, bid modifier reset to 1) or { device, bidModifier }. A supported device you leave out is switched off, written as a bid modifier of 0. Google never removes a device criterion, so an excluded device reads back as bidModifier 0 rather than disappearing, and a set that switches every device off returns 422. Which devices a campaign carries depends on its channel: Search campaigns have MOBILE, DESKTOP and TABLET, Display campaigns also have CONNECTED_TV, and sending a device the campaign does not carry returns 422. |  [optional] |
|**ageMin** | **Integer** |  |  [optional] |
|**ageMax** | **Integer** |  |  [optional] |
|**countries** | **List&lt;String&gt;** | ISO 3166-1 alpha-2 codes. On Google this is the FULL new country set for the campaign (same contract as &#x60;locations&#x60;); on LinkedIn it replaces the campaign&#39;s geo criteria. |  [optional] |
|**locations** | **Object** |  |  [optional] |
|**languages** | **List&lt;String&gt;** | Google only. The FULL new language set for the campaign, as Google language codes (ISO 639-1, plus variants such as &#x60;zh_CN&#x60;). An unknown code returns 400. |  [optional] |
|**interests** | [**List&lt;UpdateAdRequestTargetingInterestsInner&gt;**](UpdateAdRequestTargetingInterestsInner.md) | Interest objects from /v1/ads/interests. Each must include id and name. |  [optional] |
|**advantageAudience** | [**AdvantageAudienceEnum**](#AdvantageAudienceEnum) | Meta only. Omit to preserve the existing setting on update. 0 &#x3D; disabled, 1 &#x3D; enabled. |  [optional] |



## Enum: AdvantageAudienceEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |



