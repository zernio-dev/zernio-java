

# ConversionEventUser

User identity fields. More signals mean higher match rates.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**email** | **String** | Plaintext email. Hashed server-side. |  [optional] |
|**phone** | **String** | Phone number, ideally E.164. Hashed server-side. |  [optional] |
|**firstName** | **String** | Plaintext first name. Hashed server-side. |  [optional] |
|**lastName** | **String** | Plaintext last name. Hashed server-side. |  [optional] |
|**externalId** | **String** | Stable customer identifier (e.g. CRM user ID). Hashed server-side for Meta and Google. Sent as plaintext to LinkedIn (LinkedIn&#39;s Conversions API spec requires the raw value). Maximum effective list size on LinkedIn is 1.  |  [optional] |
|**ipAddress** | **String** | Client IP address. Sent plaintext. |  [optional] |
|**userAgent** | **String** | Client user-agent string. Sent plaintext. |  [optional] |
|**country** | **String** | ISO 3166-1 alpha-2 country code, e.g. &#39;us&#39;. |  [optional] |
|**city** | **String** | Meta advanced matching (ct). Plaintext city; normalized + SHA-256 hashed server-side. Meta only. |  [optional] |
|**state** | **String** | Meta advanced matching (st). 2-letter ANSI for US; hashed server-side. Meta only. |  [optional] |
|**zip** | **String** | Meta advanced matching (zp). US uses first 5 digits; hashed server-side. Meta only. |  [optional] |
|**dob** | **String** | Meta advanced matching (db). YYYYMMDD; hashed server-side. Meta only. |  [optional] |
|**gender** | **String** | Meta advanced matching (ge). &#39;f&#39; or &#39;m&#39;; hashed server-side. Meta only. |  [optional] |
|**clickIds** | [**ConversionEventUserClickIds**](ConversionEventUserClickIds.md) |  |  [optional] |



