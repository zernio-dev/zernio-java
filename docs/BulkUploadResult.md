

# BulkUploadResult

Result of a CSV bulk upload. The same shape is returned for `200` (all rows succeeded or all failed) and `207` (mixed). Per-row outcomes live in `results`; the row's success is `ok`, and failures carry machine-readable codes in `errors`. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**total** | **Integer** | Number of data rows processed from the CSV |  [optional] |
|**valid** | **Integer** | Count of rows that succeeded (results[].ok &#x3D;&#x3D;&#x3D; true) |  [optional] |
|**invalid** | **Integer** | Count of rows that failed (total - valid) |  [optional] |
|**results** | [**List&lt;BulkUploadResultResultsInner&gt;**](BulkUploadResultResultsInner.md) | One entry per CSV data row, in row order. |  [optional] |
|**warnings** | **List&lt;String&gt;** | Top-level advisory warnings, e.g. &#x60;rows_exceed_advisory_limit:500&#x60;, &#x60;unknown_columns:&lt;a,b,c&gt;&#x60; (comma-separated unrecognized CSV column names), or &#x60;not_added_to_caption:&lt;columns&gt;&#x60; (the &#x60;hashtags&#x60; and/or &#x60;mentions&#x60; column is filled: stored on the post, not added to the caption). Empty when none. |  [optional] |
|**rateLimitedAccounts** | [**List&lt;BulkUploadResultRateLimitedAccountsInner&gt;**](BulkUploadResultRateLimitedAccountsInner.md) | Present only when one or more rows targeted an account currently in cooldown. Lets callers map &#x60;rate_limited:*&#x60; row errors back to structured metadata without parsing the error strings.  |  [optional] |



