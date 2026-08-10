

# GetMediaPresignedUrl200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**uploadUrl** | **URI** | Presigned URL to PUT your file to (expires in 1 hour) |  [optional] |
|**publicUrl** | **URI** | Public URL where the file will be accessible after upload. Served from the temp/ prefix by default (expires 7 days after upload) or from media/ when permanent is true. |  [optional] |
|**key** | **String** | Storage key/path of the file. Prefixed temp/ by default, media/ when permanent is true. |  [optional] |
|**expiresIn** | **Integer** | Seconds until the presigned uploadUrl expires (always 3600) |  [optional] |



