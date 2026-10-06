

# GetInstagramOnlineFollowers200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**success** | **Boolean** |  |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  [optional] |
|**metric** | [**MetricEnum**](#MetricEnum) |  |  [optional] |
|**days** | [**List&lt;GetInstagramOnlineFollowers200ResponseDaysInner&gt;**](GetInstagramOnlineFollowers200ResponseDaysInner.md) | Oldest first, as Meta returns them. Days Meta still reports as empty are left out. |  [optional] |
|**note** | **String** |  |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| INSTAGRAM | &quot;instagram&quot; |



## Enum: MetricEnum

| Name | Value |
|---- | -----|
| ONLINE_FOLLOWERS | &quot;online_followers&quot; |



