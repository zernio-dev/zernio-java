

# GetTikTokSmartPlusMaterialReport200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adAccountId** | **String** |  |  [optional] |
|**level** | [**LevelEnum**](#LevelEnum) |  |  [optional] |
|**startDate** | **String** |  |  [optional] |
|**endDate** | **String** |  |  [optional] |
|**page** | **Integer** |  |  [optional] |
|**pageSize** | **Integer** |  |  [optional] |
|**totalRows** | **Integer** |  |  [optional] |
|**totalPages** | **Integer** |  |  [optional] |
|**missingRows** | **Integer** | Rows TikTok declared that a read and its retry could not return. 0 when the result is complete. |  [optional] |
|**rows** | [**List&lt;GetTikTokSmartPlusMaterialReport200ResponseRowsInner&gt;**](GetTikTokSmartPlusMaterialReport200ResponseRowsInner.md) |  |  [optional] |



## Enum: LevelEnum

| Name | Value |
|---- | -----|
| AD | &quot;ad&quot; |
| AD_GROUP | &quot;adGroup&quot; |



