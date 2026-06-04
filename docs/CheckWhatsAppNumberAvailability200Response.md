

# CheckWhatsAppNumberAvailability200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**country** | **String** |  |  [optional] |
|**numberType** | **String** |  |  [optional] |
|**available** | **Boolean** | Whether deliverable voice inventory exists right now. |  [optional] |
|**addressConstraint** | [**AddressConstraintEnum**](#AddressConstraintEnum) |  |  [optional] |
|**areas** | **List&lt;String&gt;** | For &#x60;geo&#x60; only — the area(s) the registered address must be in. |  [optional] |



## Enum: AddressConstraintEnum

| Name | Value |
|---- | -----|
| GEO | &quot;geo&quot; |
| COUNTRY | &quot;country&quot; |
| NONE | &quot;none&quot; |



