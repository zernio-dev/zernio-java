

# CancelCommerceOrderRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Connected store SocialAccount id. |  |
|**reason** | [**ReasonEnum**](#ReasonEnum) |  |  |
|**refund** | **Boolean** | Refund the payments to the original methods. Authorized payments are voided either way. |  [optional] |
|**restock** | **Boolean** |  |  [optional] |
|**notifyCustomer** | **Boolean** |  |  [optional] |
|**staffNote** | **String** | Visible to staff only. |  [optional] |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| CUSTOMER | &quot;customer&quot; |
| DECLINED | &quot;declined&quot; |
| FRAUD | &quot;fraud&quot; |
| INVENTORY | &quot;inventory&quot; |
| STAFF | &quot;staff&quot; |
| OTHER | &quot;other&quot; |



