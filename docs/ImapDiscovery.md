

# ImapDiscovery


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**email** | **String** |  |  [optional] |
|**route** | [**RouteEnum**](#RouteEnum) |  |  [optional] |
|**provider** | [**ImapDiscoveryProvider**](ImapDiscoveryProvider.md) |  |  [optional] |
|**source** | [**SourceEnum**](#SourceEnum) |  |  [optional] |
|**confidence** | [**ConfidenceEnum**](#ConfidenceEnum) | low when only a probe answered: show the settings for the user to check. |  [optional] |
|**imap** | [**ImapDiscoveryImap**](ImapDiscoveryImap.md) |  |  [optional] |
|**smtp** | [**ImapDiscoverySmtp**](ImapDiscoverySmtp.md) |  |  [optional] |
|**auth** | [**ImapDiscoveryAuth**](ImapDiscoveryAuth.md) |  |  [optional] |
|**preflight** | [**List&lt;ImapDiscoveryPreflightInner&gt;**](ImapDiscoveryPreflightInner.md) | What to switch on at the provider first, such as IMAP access on GMX or Yandex. |  [optional] |
|**reconnectCause** | **String** |  |  [optional] |
|**reason** | **String** |  |  [optional] |
|**unsupportedReason** | [**UnsupportedReasonEnum**](#UnsupportedReasonEnum) |  |  [optional] |
|**appPasswordFallback** | **Object** | Google only: Gmail over IMAP with an app password, for accounts whose admin blocks Google sign-in for other apps. |  [optional] |



## Enum: RouteEnum

| Name | Value |
|---- | -----|
| IMAP | &quot;imap&quot; |
| GOOGLE_OAUTH | &quot;google_oauth&quot; |
| MICROSOFT_OAUTH | &quot;microsoft_oauth&quot; |
| UNSUPPORTED | &quot;unsupported&quot; |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| PRESET | &quot;preset&quot; |
| MX | &quot;mx&quot; |
| AUTOCONFIG | &quot;autoconfig&quot; |
| ISPDB | &quot;ispdb&quot; |
| SRV | &quot;srv&quot; |
| PROBE | &quot;probe&quot; |
| NONE | &quot;none&quot; |



## Enum: ConfidenceEnum

| Name | Value |
|---- | -----|
| HIGH | &quot;high&quot; |
| MEDIUM | &quot;medium&quot; |
| LOW | &quot;low&quot; |



## Enum: UnsupportedReasonEnum

| Name | Value |
|---- | -----|
| PROTON_REQUIRES_BRIDGE | &quot;proton_requires_bridge&quot; |



