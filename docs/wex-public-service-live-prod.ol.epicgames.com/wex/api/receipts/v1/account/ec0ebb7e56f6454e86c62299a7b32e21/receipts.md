# Receipts

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/receipts/v1/account/ec0ebb7e56f6454e86c62299a7b32e21/receipts*



___

## Request

```http request
GET /wex/api/receipts/v1/account/ec0ebb7e56f6454e86c62299a7b32e21/receipts HTTP/1.1
```





### Request Headers

| Name | Value |
|---|---|
| Host | wex-public-service-live-prod.ol.epicgames.com |
| Accept | \*/\* |
| Accept-Encoding | deflate, gzip |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-B35E65544831B97BA4FD83A743387CA3 |
| User-Agent | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit |
| Authorization | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |
| Content-Length | 0 |



___

## Response

#### Status: 200 OK




### Response Headers

| Name | Value |
|---|---|
| Date | Thu, 29 Dec 2022 05:43:13 GMT |
| Content-Type | application/json |
| Content-Length | 481 |
| X-EpicGames-McpVersion | prod Release-1.88-1.88 build 107 cl 19310354 |
| X-EpicGames-ContentVersion | 1.88.244-r17036752 |
| X-EpicGames-MinBuild | 17036752 |
| X-Epic-Device-ID | 68009daed09498667a8039cce09983ed |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-B35E65544831B97BA4FD83A743387CA3 |
| Connection | keep-alive |


### Response Body

```json
[
  {
    "appStore": "EpicPurchasingService",
    "appStoreId": "d3exxxxxxxxxxxxxxxxxxxxxxxxxx6c9",
    "receiptId": "c8dxxxxxxxxxxxxxxxxxxxxxxxxxx56b",
    "receiptInfo": "ENTITLEMENT"
  },
  {
    "appStore": "EpicPurchasingService",
    "appStoreId": "3d3xxxxxxxxxxxxxxxxxxxxxxxxxxcf4",
    "receiptId": "eb6xxxxxxxxxxxxxxxxxxxxxxxxxx330",
    "receiptInfo": "ENTITLEMENT"
  },
  {
    "appStore": "EpicPurchasingService",
    "appStoreId": "a16xxxxxxxxxxxxxxxxxxxxxxxxxxbb9",
    "receiptId": "2e0xxxxxxxxxxxxxxxxxxxxxxxxxx7c2",
    "receiptInfo": "ENTITLEMENT"
  }
]
```

*Response body was encoded in base64*

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
