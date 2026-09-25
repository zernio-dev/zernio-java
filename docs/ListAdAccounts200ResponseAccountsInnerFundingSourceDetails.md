

# ListAdAccounts200ResponseAccountsInnerFundingSourceDetails

Meta only. Meta's `funding_source_details` object, forwarded unchanged. ABSENT under exactly the same conditions as `fundingSource`, never sent as null or as an empty object. Read `billingStatus` for what the absence means. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Meta&#39;s ID for the funding instrument. Matches &#x60;fundingSource&#x60;. |  [optional] |
|**displayString** | **String** | Meta&#39;s own human-readable label for the funding instrument, e.g. &#39;Available Balance (EUR)&#39; or a masked card. Meta composes this string; do not parse it. |  [optional] |
|**type** | **Integer** | Meta&#39;s raw numeric funding-source type, forwarded unchanged. Meta publishes no mapping from these numbers to payment-method kinds, so none is documented here and none should be inferred. |  [optional] |



