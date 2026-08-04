

# WhatsAppHeaderComponentExample


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**headerText** | **List&lt;String&gt;** | Sample values for header text variables |  [optional] |
|**headerTextNamedParams** | [**List&lt;WhatsAppNamedParamExample&gt;**](WhatsAppNamedParamExample.md) | Sample values for NAMED header variables (templates using {{customer_name}}-style tokens with parameter_format: NAMED). |  [optional] |
|**headerHandle** | **List&lt;URI&gt;** | When the header format is a media type (image, video, gif, document), provide a public URL here. Zernio will download and upload it to WhatsApp on your behalf, replacing it with the internal file handle before creating the template. |  [optional] |



