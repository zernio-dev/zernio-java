

# PostMetricSample


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**syncedAt** | **String** | When Zernio read the numbers from the platform. |  |
|**views** | **BigDecimal** |  |  |
|**likes** | **BigDecimal** |  |  |
|**comments** | **BigDecimal** |  |  |
|**shares** | **BigDecimal** | null on platforms that do not return the counter, unlike a real 0. |  |
|**saves** | **BigDecimal** | null on platforms that do not return the counter, unlike a real 0. |  |
|**watchSeconds** | **BigDecimal** | Average watch time; null when the platform gives no watch signal. |  |
|**completionRate** | **BigDecimal** | null when the platform gives no watch signal. |  |



