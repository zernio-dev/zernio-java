

# CreateFilePickerSessionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | A Google account connected with &#x60;scopes&#x3D;files&#x60;. |  |
|**redirectUrl** | **URI** | Where the browser goes when the user finishes. Absolute &#x60;http(s)&#x60; URL or a custom app scheme (&#x60;myapp://...&#x60;); relative, protocol-relative and script URLs are refused. Optional when you rely on the &#x60;file.picked&#x60; webhook. |  [optional] |
|**fileIds** | **List&lt;String&gt;** | Drive file ids to show the user first (Google Picker &#x60;DocsView.setFileIds&#x60;), for example to ask for access to files your app already knows about. Pre-navigation only: the user still has to pick them. |  [optional] |
|**mimeTypes** | **List&lt;String&gt;** | Only show files of these exact media types. |  [optional] |
|**multiselect** | **Boolean** | false limits the pick to one file. |  [optional] |



