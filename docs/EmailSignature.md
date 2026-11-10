

# EmailSignature

A signature Zernio stores and appends itself, so it works on every provider.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**html** | **String** |  |  [optional] |
|**text** | **String** | Appended to plain-text bodies. When &#x60;null&#x60;, the html stripped to text is used. |  [optional] |
|**accountId** | **String** | &#x60;null&#x60; for a workspace-wide signature. |  [optional] |
|**defaultFor** | **List&lt;String&gt;** | Sending addresses this signature is the default for. Each address has one default per scope; an account signature wins over a workspace one. |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] |



