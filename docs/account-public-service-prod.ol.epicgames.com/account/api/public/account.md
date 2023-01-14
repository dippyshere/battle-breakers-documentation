# Account

#####

*https://account-public-service-prod.ol.epicgames.com/account/api/public/account?accountId=b476b9e794ef40b49a1f070c69c4d7eb&accountId=7c029e5b93714af7b5a02d1789bb692b*



___

## Request

```http request
GET /account/api/public/account?accountId=b476b9e794ef40b49a1f070c69c4d7eb&accountId=7c029e5b93714af7b5a02d1789bb692b HTTP/1.1
```

### Query String

| Name | Value |
|---|---|
| accountId | b476b9e794ef40b49a1f070c69c4d7eb |
| accountId | 7c029e5b93714af7b5a02d1789bb692b |




### Request Headers

| Name | Value |
|---|---|
| Host | account-public-service-prod.ol.epicgames.com |
| Accept | \*/\* |
| Accept-Encoding | deflate, gzip |
| Content-Type | application/json |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-6F9474B34AC91F86FEB2378E0F7246DE |
| User-Agent | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit |
| Authorization | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |
| Content-Length | 0 |



___

## Response

#### Status: 200 OK




### Response Headers

| Name | Value |
|---|---|
| Date | Thu, 29 Dec 2022 05:43:02 GMT |
| Content-Type | application/json |
| Content-Length | 4865 |
| Cache-Control | no-cache, no-store, no-transform |
| X-Epic-Device-ID | 68009daed09498667a8039cce09983ed |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-6F9474B34AC91F86FEB2378E0F7246DE |
| Connection | keep-alive |


### Response Body

```json
[
  {
    "id": "b476b9e794ef40b49a1f070c69c4d7eb",
    "displayName": "EpicName1",
    "externalAuths": {
      "xbl": {
        "accountId": "b476b9e794ef40b49a1f070c69c4d7eb",
        "type": "xbl",
        "externalAuthIdType": "xuid",
        "externalDisplayName": "XboxName1",
        "authIds": []
      },
      "nintendo": {
        "accountId": "b476b9e794ef40b49a1f070c69c4d7eb",
        "type": "nintendo",
        "externalAuthId": "lp1_a6904xxxxxxxxeea",
        "externalAuthIdType": "nsa_id",
        "authIds": [
          {
            "id": "lp1_a6904xxxxxxxxeea",
            "type": "nsa_id"
          }
        ]
      },
      "psn": {
        "accountId": "b476b9e794ef40b49a1f070c69c4d7eb",
        "type": "psn",
        "externalAuthId": "809xxxxxxxxxxxxx633",
        "externalAuthIdType": "psn_user_id",
        "externalDisplayName": "PSNName1",
        "authIds": [
          {
            "id": "809xxxxxxxxxxxxx633",
            "type": "psn_user_id"
          }
        ]
      }
    }
  },
  {
    "id": "7c029e5b93714af7b5a02d1789bb692b",
    "displayName": "EpicName2",
    "externalAuths": {}
  }
]
```

*Response body was encoded in base64*

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
