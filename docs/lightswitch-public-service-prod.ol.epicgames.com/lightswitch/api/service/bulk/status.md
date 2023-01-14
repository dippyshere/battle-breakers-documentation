# Status

#####

*https://lightswitch-public-service-prod.ol.epicgames.com/lightswitch/api/service/bulk/status?serviceId=WorldExplorersLive*



___

## Request

```http request
GET /lightswitch/api/service/bulk/status?serviceId=WorldExplorersLive HTTP/1.1
```

### Query String

| Name | Value |
|---|---|
| serviceId | WorldExplorersLive |




### Request Headers

| Name | Value |
|---|---|
| Host | lightswitch-public-service-prod.ol.epicgames.com |
| Accept | \*/\* |
| Accept-Encoding | deflate, gzip |
| Content-Type | application/json |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-27A444314652A4B2519DBEA580BCAFE6 |
| User-Agent | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit |
| Authorization | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |
| Content-Length | 0 |



___

## Response

#### Status: 200 OK




### Response Headers

| Name | Value |
|---|---|
| Date | Thu, 29 Dec 2022 06:07:55 GMT |
| Content-Type | application/json |
| Content-Length | 348 |
| X-Epic-Device-ID | 68009daed09498667a8039cce09983ed |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-27A444314652A4B2519DBEA580BCAFE6 |
| Connection | keep-alive |


### Response Body

```json
[
  {
    "serviceInstanceId": "worldexplorerslive",
    "status": "UP",
    "message": "This is a default status.",
    "maintenanceUri": null,
    "overrideCatalogIds": [
      "ae402a2cb61b4c5fa199ce5311cca724"
    ],
    "allowedActions": [
      "PLAY",
      "DOWNLOAD"
    ],
    "banned": false,
    "launcherInfoDTO": {
      "appName": "WorldExplorersLive",
      "catalogItemId": "a53e821fbdc24181877243a8dbb63463",
      "namespace": "wex"
    }
  }
]
```

*Response body was encoded in base64*

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
