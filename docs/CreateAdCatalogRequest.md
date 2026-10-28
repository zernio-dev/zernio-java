

# CreateAdCatalogRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | A facebook, instagram, metaads or whatsapp account ID |  |
|**catalogAccountId** | **String** | Account whose Meta login token performs the call (see GET) |  [optional] |
|**adAccountId** | **String** | Ad account whose owner business creates the catalog |  [optional] |
|**businessId** | **String** | Business portfolio that owns the catalog |  [optional] |
|**name** | **String** |  |  |
|**vertical** | [**VerticalEnum**](#VerticalEnum) | Meta catalog vertical. Use services for a professional services catalog (for example one linked to WhatsApp). local_service_business is a deprecated alias of local_service_businesses. The product endpoints under /v1/ads/catalogs/{catalogId}/products write commerce product items only. |  [optional] |



## Enum: VerticalEnum

| Name | Value |
|---- | -----|
| COMMERCE | &quot;commerce&quot; |
| ADOPTABLE_PETS | &quot;adoptable_pets&quot; |
| APPS_AND_SOFTWARE | &quot;apps_and_software&quot; |
| ARTICLES_AND_PUBLICATIONS | &quot;articles_and_publications&quot; |
| DESTINATIONS | &quot;destinations&quot; |
| FLIGHTS | &quot;flights&quot; |
| GENERIC | &quot;generic&quot; |
| HOME_LISTINGS | &quot;home_listings&quot; |
| HOTELS | &quot;hotels&quot; |
| LOCAL_SERVICE_BUSINESSES | &quot;local_service_businesses&quot; |
| MEDIA_TITLES | &quot;media_titles&quot; |
| OFFER_ITEMS | &quot;offer_items&quot; |
| OFFLINE_COMMERCE | &quot;offline_commerce&quot; |
| SERVICES | &quot;services&quot; |
| TRANSACTABLE_ITEMS | &quot;transactable_items&quot; |
| VEHICLES | &quot;vehicles&quot; |
| LOCAL_SERVICE_BUSINESS | &quot;local_service_business&quot; |



