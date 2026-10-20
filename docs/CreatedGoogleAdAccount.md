

# CreatedGoogleAdAccount


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  |
|**adAccountId** | **String** | New Google Ads customer id for subsequent ads calls. |  |
|**managerCustomerId** | **String** | Manager the account was created under. |  |
|**connectionUpdated** | **Boolean** | Whether the customer was added to the connection and discovery was scheduled. When false the account exists: reconnect Google Ads instead of creating it again. |  |
|**warnings** | **List&lt;String&gt;** | Recovery instructions if the account could not be attached to the connection. |  |
|**paymentMethodRequired** | **Boolean** | Always true. The account has no billing until it is set up in Google Ads. |  |
|**nextSteps** | **String** | Billing setup instructions for the user. |  |
|**validateOnly** | **Boolean** | Always false on a 201. |  |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| GOOGLE | &quot;google&quot; |



