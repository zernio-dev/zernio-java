

# AutomationTemplateAutomation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**key** | **String** | Stable within the template, for example &#x60;automation1&#x60;. |  |
|**definition** | **Map&lt;String, Object&gt;** | A &#x60;POST /v1/automations&#x60; body without &#x60;status&#x60;, in which every value tied to one account is an input reference such as &#x60;{ \&quot;$input\&quot;: \&quot;adAccount\&quot; }&#x60;. Campaign ids, id filters, start and end dates and approval steps are not kept. |  |



