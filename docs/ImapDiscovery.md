

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
|**hostReplacements** | [**List&lt;ImapDiscoveryHostReplacementsInner&gt;**](ImapDiscoveryHostReplacementsInner.md) | Server names discovery swapped for the name the server certificate is issued for, as on shared hosting where mail.&lt;domain&gt; has no certificate of its own. Present on the imap route. |  [optional] |
|**reconnectCause** | **String** |  |  [optional] |
|**reason** | **String** |  |  [optional] |
|**unsupportedReason** | [**UnsupportedReasonEnum**](#UnsupportedReasonEnum) | Why an &#x60;unsupported&#x60; route cannot connect:  - &#x60;proton_requires_bridge&#x60;: Proton Mail only works through its local bridge. - &#x60;forwarding_only&#x60;: the domain forwards mail (Cloudflare Email Routing) and stores none, so connect the mailbox it forwards to. - &#x60;domain_typo&#x60;: the domain takes no mail and looks like a mistyped consumer domain. &#x60;suggestedEmail&#x60; has the likely address. - &#x60;no_mail_domain&#x60;: the domain has no MX and no address, so it cannot receive email.  |  [optional] |
|**suggestedEmail** | **String** | With unsupportedReason domain_typo: the address the user most likely meant, such as ana7275@gmail.com for ana@7275gmail.com. Run discovery again with it once the user confirms. |  [optional] |
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
| FORWARDING_ONLY | &quot;forwarding_only&quot; |
| DOMAIN_TYPO | &quot;domain_typo&quot; |
| NO_MAIL_DOMAIN | &quot;no_mail_domain&quot; |



