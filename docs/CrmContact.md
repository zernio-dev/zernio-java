

# CrmContact

A person in the connected CRM, in the same shape for HubSpot and Salesforce.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The CRM&#39;s own id. |  |
|**objectType** | [**ObjectTypeEnum**](#ObjectTypeEnum) | &#x60;lead&#x60; only on Salesforce. |  |
|**firstName** | **String** |  |  |
|**lastName** | **String** |  |  |
|**email** | **String** |  |  |
|**phone** | **String** | The phone, else the mobile phone, as stored in the CRM. |  |
|**company** | **String** | HubSpot &#x60;company&#x60;; Salesforce Lead &#x60;Company&#x60; or Contact Account name. |  |
|**ownerId** | **String** |  |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**updatedAt** | **OffsetDateTime** |  |  |
|**url** | **URI** | Opens the record in the CRM. |  |
|**properties** | **Map&lt;String, Object&gt;** | The native fields asked for with &#x60;properties&#x60;, by name. |  |
|**raw** | **Map&lt;String, Object&gt;** | The CRM&#39;s own record, only with &#x60;includeRaw&#x3D;true&#x60;. |  [optional] |



## Enum: ObjectTypeEnum

| Name | Value |
|---- | -----|
| CONTACT | &quot;contact&quot; |
| LEAD | &quot;lead&quot; |



