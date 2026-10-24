

# LinkedInMentionIssue

One LinkedIn mention that could not be resolved, listed under `details.mentions[]` of the error.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**input** | **String** | The mention exactly as written in the request, for example &#x60;@[https://www.linkedin.com/in/jane-doe]&#x60;. |  |
|**code** | [**CodeEnum**](#CodeEnum) | Why it failed. |  |
|**message** | **String** | Human-readable reason. |  |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| LINKEDIN_MENTION_UNRESOLVABLE | &quot;linkedin_mention_unresolvable&quot; |
| LINKEDIN_MENTION_REQUIRES_PAGE_ADMIN | &quot;linkedin_mention_requires_page_admin&quot; |
| LINKEDIN_MENTION_NAME_UNAVAILABLE | &quot;linkedin_mention_name_unavailable&quot; |
| LINKEDIN_MENTIONS_LIMIT_EXCEEDED | &quot;linkedin_mentions_limit_exceeded&quot; |
| RATE_LIMITED | &quot;rate_limited&quot; |
| RECONNECT_REQUIRED | &quot;reconnect_required&quot; |
| TEMPORARILY_UNAVAILABLE | &quot;temporarily_unavailable&quot; |



