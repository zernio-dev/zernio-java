

# TrackingTagDiagnostic

One health check the platform runs on a tracking tag.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**key** | **String** | Platform check id (Meta: e.g. &#x60;pixel_missing_param_in_events&#x60;). |  |
|**title** | **String** |  |  |
|**description** | **String** |  |  [optional] |
|**result** | **String** | The platform verdict (Meta: &#x60;passed&#x60;, &#x60;failed&#x60;, &#x60;warning&#x60;). |  |
|**actionUrl** | **String** | Where to fix it in the platform UI (Meta: Events Manager). |  [optional] |
|**alwaysUseDefaultValue** | **Boolean** | Record &#x60;defaultValue&#x60; even when the conversion sends its own value. |  [optional] |
|**primary** | **Boolean** | Primary (counts toward bidding) or secondary (observation only). |  [optional] |
|**countingType** | [**CountingTypeEnum**](#CountingTypeEnum) | &#x60;one&#x60; &#x3D; one conversion per ad interaction, &#x60;every&#x60; &#x3D; each conversion. |  [optional] |



## Enum: CountingTypeEnum

| Name | Value |
|---- | -----|
| ONE | &quot;one&quot; |
| EVERY | &quot;every&quot; |



