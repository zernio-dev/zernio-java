

# CheckPhoneNumberAvailability200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**country** | **String** |  |  [optional] |
|**numberType** | **String** |  |  [optional] |
|**available** | **Boolean** | Whether deliverable voice inventory exists right now. |  [optional] |
|**addressConstraint** | [**AddressConstraintEnum**](#AddressConstraintEnum) |  |  [optional] |
|**areas** | **List&lt;String&gt;** | For &#x60;geo&#x60; only — the area(s) the registered address must be in. |  [optional] |
|**areaOptions** | [**List&lt;CheckPhoneNumberAvailability200ResponseAreaOptionsInner&gt;**](CheckPhoneNumberAvailability200ResponseAreaOptionsInner.md) | Live inventory grouped by area code, largest stock first. Empty when out of stock (or the area lookup failed). Pass a chosen &#x60;ndc&#x60; as &#x60;areaCode&#x60; on POST /v1/phone-numbers/purchase (or on the KYC submit for regulated countries) to require that area.  |  [optional] |



## Enum: AddressConstraintEnum

| Name | Value |
|---- | -----|
| GEO | &quot;geo&quot; |
| COUNTRY | &quot;country&quot; |
| NONE | &quot;none&quot; |



