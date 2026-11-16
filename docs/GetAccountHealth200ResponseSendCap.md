

# GetAccountHealth200ResponseSendCap

Google and Microsoft only: today's outbound mail allowance for the mailbox.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**limit** | **Integer** | Today&#39;s cap: the base cap, doubled after 14 days of sending with no spam signal. |  [optional] |
|**baseLimit** | **Integer** | The cap before doubling. |  [optional] |
|**doubled** | **Boolean** |  |  [optional] |
|**doublesAt** | **OffsetDateTime** | When the cap doubles if the mailbox sends every day from now on and raises no spam signal. Null once doubled, with a manual limit, and on IMAP. |  [optional] |
|**used** | **Integer** |  |  [optional] |
|**resetsAt** | **OffsetDateTime** |  |  [optional] |



