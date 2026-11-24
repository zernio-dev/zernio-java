

# ConnectCustomDomain


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**hostname** | **String** | The subdomain, such as &#x60;connect.yourbrand.com&#x60;. |  |
|**zone** | **String** | The registered domain the records live in, such as &#x60;yourbrand.com&#x60;. |  |
|**status** | [**StatusEnum**](#StatusEnum) | &#x60;pending&#x60; until the TXT record is found and the certificate is issued, &#x60;active&#x60; once the domain serves the connect screens, &#x60;failed&#x60; when it stopped pointing at Zernio (remove it and add it again). |  |
|**connectEnabled** | **Boolean** | Whether new connect links open on this domain while it is active. |  |
|**ownershipVerified** | **Boolean** | True once the TXT record was found. |  |
|**records** | [**List&lt;ConnectCustomDomainRecordsInner&gt;**](ConnectCustomDomainRecordsInner.md) | The DNS records to add at your DNS provider. |  |
|**activatedAt** | **OffsetDateTime** |  |  |
|**createdAt** | **OffsetDateTime** |  |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| ACTIVE | &quot;active&quot; |
| FAILED | &quot;failed&quot; |



