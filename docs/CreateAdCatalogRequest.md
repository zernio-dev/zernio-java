

# CreateAdCatalogRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | A facebook, instagram, metaads or whatsapp account ID |  |
|**catalogAccountId** | **String** | Account whose Meta login token performs the call (see GET) |  [optional] |
|**adAccountId** | **String** | Ad account whose owner business creates the catalog |  [optional] |
|**businessId** | **String** | Business portfolio that owns the catalog |  [optional] |
|**name** | **String** |  |  |
|**vertical** | [**VerticalEnum**](#VerticalEnum) |  |  [optional] |



## Enum: VerticalEnum

| Name | Value |
|---- | -----|
| COMMERCE | &quot;commerce&quot; |
| VEHICLES | &quot;vehicles&quot; |
| HOTELS | &quot;hotels&quot; |
| FLIGHTS | &quot;flights&quot; |
| DESTINATIONS | &quot;destinations&quot; |
| HOME_LISTINGS | &quot;home_listings&quot; |
| LOCAL_SERVICE_BUSINESS | &quot;local_service_business&quot; |
| OFFLINE_COMMERCE | &quot;offline_commerce&quot; |
| TICKETED_EXPERIENCES | &quot;ticketed_experiences&quot; |
| TRANSACTABLE_ITEMS | &quot;transactable_items&quot; |



