

# CreateConversionActionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | SocialAccount ID. Must be a &#x60;googleads&#x60; account. |  |
|**adAccountId** | **String** | Platform ad account ID (Google customer ID, digits only). Resolved automatically when the connection has exactly one accessible customer. |  [optional] |
|**customerId** | **String** | Alias of adAccountId, kept for existing callers |  [optional] |
|**name** | **String** |  |  |
|**type** | [**TypeEnum**](#TypeEnum) | Only WEBPAGE is supported for creation today. |  |
|**defaultValue** | **BigDecimal** | Default conversion value used when an event doesn&#39;t carry its own value. |  [optional] |
|**alwaysUseDefaultValue** | **Boolean** | When true, always use defaultValue and ignore any value sent with the event. Defaults to true when defaultValue is set. |  [optional] |
|**category** | [**CategoryEnum**](#CategoryEnum) | conversion_action.category. Defaults to DEFAULT on create. |  [optional] |
|**countingType** | [**CountingTypeEnum**](#CountingTypeEnum) | ONE_PER_CLICK counts one conversion per ad click (leads); MANY_PER_CLICK counts every one (purchases). |  [optional] |
|**defaultCurrency** | **String** | ISO 4217 currency of defaultValue (value_settings.default_currency_code). |  [optional] |
|**clickThroughLookbackWindowDays** | **Integer** | Days after an ad click a conversion still counts. |  [optional] |
|**viewThroughLookbackWindowDays** | **Integer** | Days after an ad view a view-through conversion still counts. |  [optional] |
|**primaryForGoal** | **Boolean** | true &#x3D; primary (counts toward bidding when its goal is biddable), false &#x3D; secondary. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| WEBPAGE | &quot;WEBPAGE&quot; |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;DEFAULT&quot; |
| PAGE_VIEW | &quot;PAGE_VIEW&quot; |
| PURCHASE | &quot;PURCHASE&quot; |
| SIGNUP | &quot;SIGNUP&quot; |
| DOWNLOAD | &quot;DOWNLOAD&quot; |
| ADD_TO_CART | &quot;ADD_TO_CART&quot; |
| BEGIN_CHECKOUT | &quot;BEGIN_CHECKOUT&quot; |
| SUBSCRIBE_PAID | &quot;SUBSCRIBE_PAID&quot; |
| PHONE_CALL_LEAD | &quot;PHONE_CALL_LEAD&quot; |
| IMPORTED_LEAD | &quot;IMPORTED_LEAD&quot; |
| SUBMIT_LEAD_FORM | &quot;SUBMIT_LEAD_FORM&quot; |
| BOOK_APPOINTMENT | &quot;BOOK_APPOINTMENT&quot; |
| REQUEST_QUOTE | &quot;REQUEST_QUOTE&quot; |
| GET_DIRECTIONS | &quot;GET_DIRECTIONS&quot; |
| OUTBOUND_CLICK | &quot;OUTBOUND_CLICK&quot; |
| CONTACT | &quot;CONTACT&quot; |
| ENGAGEMENT | &quot;ENGAGEMENT&quot; |
| STORE_VISIT | &quot;STORE_VISIT&quot; |
| STORE_SALE | &quot;STORE_SALE&quot; |
| QUALIFIED_LEAD | &quot;QUALIFIED_LEAD&quot; |
| CONVERTED_LEAD | &quot;CONVERTED_LEAD&quot; |



## Enum: CountingTypeEnum

| Name | Value |
|---- | -----|
| ONE_PER_CLICK | &quot;ONE_PER_CLICK&quot; |
| MANY_PER_CLICK | &quot;MANY_PER_CLICK&quot; |



