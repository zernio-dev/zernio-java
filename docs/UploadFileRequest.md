

# UploadFileRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  |
|**name** | **String** |  |  |
|**contentType** | **String** |  |  |
|**parentId** | **String** | Target folder; the root when omitted. |  [optional] |
|**url** | **URI** |  |  |
|**convertTo** | [**ConvertToEnum**](#ConvertToEnum) | Google Drive only: import the bytes as a Docs, Sheets or Slides file (a text or Office file becomes an editable document). OneDrive answers 400. |  [optional] |



## Enum: ConvertToEnum

| Name | Value |
|---- | -----|
| APPLICATION_VND_GOOGLE_APPS_DOCUMENT | &quot;application/vnd.google-apps.document&quot; |
| APPLICATION_VND_GOOGLE_APPS_SPREADSHEET | &quot;application/vnd.google-apps.spreadsheet&quot; |
| APPLICATION_VND_GOOGLE_APPS_PRESENTATION | &quot;application/vnd.google-apps.presentation&quot; |



