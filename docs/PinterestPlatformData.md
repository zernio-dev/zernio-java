

# PinterestPlatformData


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**title** | **String** | Pin title. Defaults to first line of content or \&quot;Pin\&quot;. Must be ≤ 100 characters. |  [optional] |
|**boardId** | **String** | Target Pinterest board ID. If omitted, the first available board is used. |  [optional] |
|**boardSectionId** | **String** | Target section inside the board. Optional; the pin lands on the board itself when omitted. Pinterest rejects the pin if the section does not belong to boardId, so send both together. |  [optional] |
|**link** | **URI** | Destination link (pin URL) |  [optional] |
|**coverImageUrl** | **URI** | Optional cover image for video pins |  [optional] |
|**coverImageKeyFrameTime** | **Integer** | Optional key frame time in seconds for derived video cover |  [optional] |
|**isAiGenerated** | **Boolean** | When true, the Pin is created with Pinterest&#39;s AI_MODIFIED disclosure (ai_disclosures), which shows an \&quot;AI modified\&quot; label. Applies to image and video Pins. Pinterest offers no \&quot;not AI\&quot; value, so false simply omits the disclosure. Pinterest may still label a Pin on its own detection. |  [optional] |



