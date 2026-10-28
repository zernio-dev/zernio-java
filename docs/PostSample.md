

# PostSample


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**syncedAt** | **OffsetDateTime** | When Zernio fetched this reading from the platform |  |
|**views** | **Integer** |  |  |
|**likes** | **Integer** |  |  |
|**comments** | **Integer** |  |  |
|**shares** | **Integer** | Null on platforms that do not return shares |  |
|**saves** | **Integer** | Null on platforms that do not return saves |  |
|**watchSeconds** | **BigDecimal** | Average watch time in seconds. Null when the platform gives none. |  |
|**completionRate** | **BigDecimal** | Share of viewers who watched to the end, 0 to 1. Null when the platform gives none. |  |



