

# CheckPhoneNumberAvailability200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**country** | **String** |  |  [optional] |
|**numberType** | **String** |  |  [optional] |
|**available** | **Boolean** | Whether deliverable voice inventory exists right now. |  [optional] |
|**preOrderable** | **Boolean** | Nothing deliverable now, but this pair can be pre-ordered: submit KYC as usual and we buy regular stock the moment it returns, otherwise the carrier sources the number (usually 2 to 4 weeks, never guaranteed). Only document tiers (3/4) qualify. |  [optional] |
|**addressConstraint** | [**AddressConstraintEnum**](#AddressConstraintEnum) |  |  [optional] |
|**areas** | **List&lt;String&gt;** | For &#x60;geo&#x60; only: the area(s) the registered address must be in. |  [optional] |
|**areaOptions** | [**List&lt;CheckPhoneNumberAvailability200ResponseAreaOptionsInner&gt;**](CheckPhoneNumberAvailability200ResponseAreaOptionsInner.md) | Live inventory grouped by area code. For US and CA this is the full country inventory (every area code with stock, recognizable metros listed first, then alphabetical); other countries are ordered largest stock first; they list the areas in the latest inventory page (up to 500 numbers, which for most countries is the entire pool). Empty when out of stock (or the area lookup failed). Pass a chosen &#x60;ndc&#x60; as &#x60;areaCode&#x60; on POST /v1/phone-numbers/purchase (or on the KYC submit for regulated countries) to require that area.  |  [optional] |
|**soldOutAreas** | [**List&lt;CheckPhoneNumberAvailability200ResponseSoldOutAreasInner&gt;**](CheckPhoneNumberAvailability200ResponseSoldOutAreasInner.md) | Areas that had stock in the last 90 days and have none now. Pass one as &#x60;areaCode&#x60; with &#x60;preOrder: true&#x60; on the KYC submit when &#x60;preOrderable&#x60; is true, or watch it with POST /v1/phone-numbers/stock-watches.  |  [optional] |



## Enum: AddressConstraintEnum

| Name | Value |
|---- | -----|
| GEO | &quot;geo&quot; |
| COUNTRY | &quot;country&quot; |
| NONE | &quot;none&quot; |



