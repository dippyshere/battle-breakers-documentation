# Windows

#####

*https://launcher-public-service-prod06.ol.epicgames.com/launcher/api/public/assets/Windows?label=Live*



___

## Request

```http request
GET /launcher/api/public/assets/Windows?label=Live HTTP/1.1
```

### Query String

| Name | Value |
|---|---|
| label | Live |




### Request Headers

| Name | Value |
|---|---|
| Host | launcher-public-service-prod06.ol.epicgames.com |
| Accept | \*/\* |
| Accept-Encoding | deflate, gzip |
| Content-Type | application/json |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F0B5EE074C9D4C2448C00AA6A440E5E1-071DE5AC4F5D9009AD571BB5FBDF04FB |
| User-Agent | UELauncher/14.4.1-23462965+++Portal+Release-Live Windows/10.0.22621.1.256.64bit |
| Authorization | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |
| Content-Length | 0 |



___

## Response

#### Status: 200 OK




### Response Headers

| Name | Value |
|---|---|
| Content-Type | application/json |
| Transfer-Encoding | chunked |
| Date | Thu, 29 Dec 2022 06:06:18 GMT |
| X-Epic-MaxPageSize | 100 |
| X-Epic-Device-ID | 2f4c92e44a8a8420a867089329526852 |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F0B5EE074C9D4C2448C00AA6A440E5E1-071DE5AC4F5D9009AD571BB5FBDF04FB |
| X-Cache | Miss from cloudfront |
| Via | 1.1 3fb6aad2d0d4eb57ef667ceeeeca901a.cloudfront.net (CloudFront) |
| X-Amz-Cf-Pop | SYD62-P2 |
| X-Amz-Cf-Id | ZYTQiH4q-s6iR4m8uXrSw9VpvXcHy8-7aBpygBJrwrvQNnGFa3IP9g== |
| Connection | keep-alive |


### Response Body

```json
[
  {
    "appName": "WorldExplorersLive",
    "labelName": "Live-Windows",
    "buildVersion": "1.88.244-r17036752-Windows",
    "catalogItemId": "a53e821fbdc24181877243a8dbb63463",
    "namespace": "wex",
    "assetId": "WorldExplorersLive"
  }
]
```

*Response body was encoded in base64*

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
