

# CreateWhatsAppFlowRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | WhatsApp social account ID |  |
|**name** | **String** | Flow display name |  |
|**categories** | [**List&lt;CategoriesEnum&gt;**](#List&lt;CategoriesEnum&gt;) | Flow categories |  |
|**cloneFlowId** | **String** | Optional: ID of an existing flow to clone the Flow JSON from |  [optional] |
|**asVersion** | **Boolean** | When cloning, true keeps the clone in cloneFlowId&#39;s version lineage (auto-numbered next version); false/absent creates an independent flow. Ignored without cloneFlowId. |  [optional] |



## Enum: List&lt;CategoriesEnum&gt;

| Name | Value |
|---- | -----|
| SIGN_UP | &quot;SIGN_UP&quot; |
| SIGN_IN | &quot;SIGN_IN&quot; |
| APPOINTMENT_BOOKING | &quot;APPOINTMENT_BOOKING&quot; |
| LEAD_GENERATION | &quot;LEAD_GENERATION&quot; |
| CONTACT_US | &quot;CONTACT_US&quot; |
| CUSTOMER_SUPPORT | &quot;CUSTOMER_SUPPORT&quot; |
| SURVEY | &quot;SURVEY&quot; |
| OTHER | &quot;OTHER&quot; |



