# Data

#####

*https://datarouter.ol.epicgames.com/datarouter/api/v1/public/data?SessionID=&AppID=WEX.LIVE&AppVersion=1.88.244-r17036752&UserID=2f4c92e44a8a8420a867089329526852%7Cec0ebb7e56f6454e86c62299a7b32e21%7C83e93ca4-71a9-4951-bdcc-fb1730ad7313%7C68009daed09498667a8039cce09983ed%7Cec0ebb7e56f6454e86c62299a7b32e21&AppEnvironment=datacollector-binary&UploadType=eteventstream*



___

## Request

```http request
POST /datarouter/api/v1/public/data?SessionID=&AppID=WEX.LIVE&AppVersion=1.88.244-r17036752&UserID=2f4c92e44a8a8420a867089329526852%7Cec0ebb7e56f6454e86c62299a7b32e21%7C83e93ca4-71a9-4951-bdcc-fb1730ad7313%7C68009daed09498667a8039cce09983ed%7Cec0ebb7e56f6454e86c62299a7b32e21&AppEnvironment=datacollector-binary&UploadType=eteventstream HTTP/1.1
```

### Query String

| Name | Value |
|---|---|
| SessionID |  |
| AppID | WEX.LIVE |
| AppVersion | 1.88.244-r17036752 |
| UserID | 2f4c92e44a8a8420a867089329526852\|ec0ebb7e56f6454e86c62299a7b32e21\|83e93ca4-71a9-4951-bdcc-fb1730ad7313\|68009daed09498667a8039cce09983ed\|ec0ebb7e56f6454e86c62299a7b32e21 |
| AppEnvironment | datacollector-binary |
| UploadType | eteventstream |




### Request Headers

| Name | Value |
|---|---|
| Host | datarouter.ol.epicgames.com |
| Accept | \*/\* |
| Accept-Encoding | deflate, gzip |
| Content-Type | application/json; charset=utf-8 |
| User-Agent | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit |
| Content-Length | 126 |


### Request Body

```json
{
  "Events": [
    {
      "EventName": "UI_StorefrontOpened",
      "DateOffset": "+00:00:35.649",
      "Platform": "Windows",
      "StorefrontName": "Featured"
    }
  ]
}
```

___

## Response

#### Status: 204 No Content




### Response Headers

| Name | Value |
|---|---|
| Date | Thu, 29 Dec 2022 06:11:17 GMT |
| Access-Control-Allow-Origin | \* |
| X-Epic-Correlation-ID | beaa754e-5671-4d98-842e-12e30107ae45 |
| Connection | keep-alive |



___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
