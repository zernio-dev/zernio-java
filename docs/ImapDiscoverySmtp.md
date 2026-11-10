

# ImapDiscoverySmtp


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**host** | **String** |  |  [optional] |
|**port** | **Integer** |  |  [optional] |
|**security** | [**SecurityEnum**](#SecurityEnum) | tls from the first byte (993, 465) or STARTTLS on a plain port (143, 587). |  [optional] |



## Enum: SecurityEnum

| Name | Value |
|---- | -----|
| TLS | &quot;tls&quot; |
| STARTTLS | &quot;starttls&quot; |



