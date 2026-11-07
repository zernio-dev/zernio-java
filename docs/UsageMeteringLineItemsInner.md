

# UsageMeteringLineItemsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  [optional] |
|**product** | [**ProductEnum**](#ProductEnum) |  |  [optional] |
|**totalUsd** | **BigDecimal** |  |  [optional] |
|**quantity** | **BigDecimal** |  |  [optional] |
|**paidFrom** | [**PaidFromEnum**](#PaidFromEnum) | Present only on pay-per-use paid from the prepaid balance (balance billing). That spend is included in &#x60;days&#x60; and &#x60;totals&#x60; but is not on the monthly invoice. |  [optional] |



## Enum: ProductEnum

| Name | Value |
|---- | -----|
| ACCOUNTS | &quot;accounts&quot; |
| NUMBERS | &quot;numbers&quot; |
| IMESSAGE | &quot;imessage&quot; |
| CALLS | &quot;calls&quot; |
| SMS | &quot;sms&quot; |
| MESSAGES | &quot;messages&quot; |
| VERIFY | &quot;verify&quot; |
| DLC | &quot;dlc&quot; |
| X_API | &quot;xApi&quot; |
| ADS | &quot;ads&quot; |
| CREDITS | &quot;credits&quot; |
| OTHER | &quot;other&quot; |



## Enum: PaidFromEnum

| Name | Value |
|---- | -----|
| BALANCE | &quot;balance&quot; |



