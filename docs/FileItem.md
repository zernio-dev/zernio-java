

# FileItem

A file or folder in a connected Google Drive or OneDrive. Ids are the provider's own.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**accountId** | **String** |  |  |
|**provider** | [**ProviderEnum**](#ProviderEnum) |  |  |
|**name** | **String** |  |  |
|**kind** | [**KindEnum**](#KindEnum) |  |  |
|**mimeType** | **String** |  |  |
|**size** | **Integer** | Bytes; null for folders and Google editors files. |  |
|**parentId** | **String** |  |  |
|**webUrl** | **String** | The provider&#39;s own link to open the item. |  |
|**downloadable** | **Boolean** | False for folders and for Drive files whose owner disabled downloading. |  |
|**exportMimeType** | **String** | Google Docs, Slides and Drawings download as PDF/PNG and Sheets as XLSX; this is the type the download carries. |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  |
|**modifiedAt** | **OffsetDateTime** |  |  |
|**trashed** | **Boolean** |  |  |



## Enum: ProviderEnum

| Name | Value |
|---- | -----|
| GOOGLE | &quot;google&quot; |
| MICROSOFT | &quot;microsoft&quot; |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| FILE | &quot;file&quot; |
| FOLDER | &quot;folder&quot; |



