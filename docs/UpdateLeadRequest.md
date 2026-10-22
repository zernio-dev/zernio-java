

# UpdateLeadRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**value** | **BigDecimal** | Deal value; requires currency. |  [optional] |
|**currency** | **String** | ISO 4217 code. |  [optional] |
|**accountId** | **String** | Required when &#x60;{id}&#x60; is a Meta leadgenId: the facebook or metaads account that received the lead. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| NEW | &quot;new&quot; |
| CONTACTED | &quot;contacted&quot; |
| UNREACHABLE | &quot;unreachable&quot; |
| QUALIFIED | &quot;qualified&quot; |
| CONVERTED | &quot;converted&quot; |
| DISQUALIFIED | &quot;disqualified&quot; |



