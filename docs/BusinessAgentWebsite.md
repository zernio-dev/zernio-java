

# BusinessAgentWebsite


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**url** | **URI** |  |  |
|**includedSubDomains** | **List&lt;String&gt;** |  |  [optional] |
|**includedUrlPatterns** | **List&lt;String&gt;** | Only URLs containing one of these substrings are ingested. |  [optional] |
|**excludedSubDomains** | **List&lt;String&gt;** |  |  [optional] |
|**excludedUrlPatterns** | **List&lt;String&gt;** |  |  [optional] |
|**singleUrls** | **List&lt;URI&gt;** | Crawl only these exact pages instead of the whole site. |  [optional] |
|**id** | **String** |  |  |
|**crawlStatus** | **String** | not_started, pending, in_progress, completed, completed_no_data or failed (see crawl_error). |  [optional] |
|**crawlError** | **String** |  |  [optional] |
|**pagesCrawled** | **Integer** |  |  [optional] |
|**lastCrawledAt** | **Integer** | Unix seconds. |  [optional] |
|**createdAt** | **Integer** | Unix seconds. |  [optional] |



