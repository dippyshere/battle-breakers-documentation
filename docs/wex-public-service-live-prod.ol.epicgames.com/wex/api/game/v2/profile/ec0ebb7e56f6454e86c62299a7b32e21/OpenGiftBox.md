# OpenGiftBox

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/OpenGiftBox?profileId=profile0&rvn=40349*



___

## Request

```http request
POST /wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/OpenGiftBox?profileId=profile0&rvn=40349 HTTP/1.1
```

### Query String

| Name | Value |
|---|---|
| profileId | profile0 |
| rvn | 40349 |




### Request Headers

| Name | Value |
|---|---|
| Host | wex-public-service-live-prod.ol.epicgames.com |
| Accept-Encoding | deflate, gzip |
| Accept | \*/\* |
| Content-Type | application/json |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":24040},{"profileId":"levels","clientCommandRevision":14476},{"profileId":"friends","clientCommandRevision":8263},{"profileId":"monsterpit","clientCommandRevision":1081},{"profileId":"multiplayer","clientCommandRevision":900}] |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-70CD84EF49F09C9EAF2537AB6EB99F61 |
| User-Agent | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit |
| Authorization | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |
| Content-Length | 55 |


### Request Body

```json
{
  "itemId": "f25baf81-2fc3-4e2d-940b-b50453ade9c0"
}
```

___

## Response

#### Status: 200 OK




### Response Headers

| Name | Value |
|---|---|
| Date | Thu, 29 Dec 2022 05:44:25 GMT |
| Content-Type | application/json |
| Content-Length | 1026 |
| X-EpicGames-McpVersion | prod Release-1.88-1.88 build 107 cl 19310354 |
| X-EpicGames-ContentVersion | 1.88.244-r17036752 |
| X-EpicGames-MinBuild | 17036752 |
| X-EpicGames-Profile-Revision | 40349 |
| X-Epic-Device-ID | 68009daed09498667a8039cce09983ed |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-70CD84EF49F09C9EAF2537AB6EB99F61 |
| Connection | keep-alive |


### Response Body

```json
{
  "profileRevision": 40350,
  "profileId": "profile0",
  "profileChangesBaseRevision": 40349,
  "profileChanges": [
    {
      "changeType": "itemRemoved",
      "itemId": "f25baf81-2fc3-4e2d-940b-b50453ade9c0"
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "c384fe1c-cf33-48ab-868e-56125c6f9b88",
      "quantity": 47769
    },
    {
      "changeType": "itemAdded",
      "itemId": "a1c51a9c-8685-49d2-a513-4e2c3d1831c2",
      "item": {
        "templateId": "Giftbox:GB_DailyGems_Laundry23",
        "attributes": {
          "sealed_days": 1,
          "params": {},
          "min_level": 1
        },
        "quantity": 1
      }
    }
  ],
  "notifications": [
    {
      "type": "WExpGiftBoxOpened",
      "primary": true,
      "giftBoxTemplateId": "Giftbox:GB_DailyGems_Laundry22",
      "lootResult": {
        "tierGroupName": "f25baf81-2fc3-4e2d-940b-b50453ade9c0",
        "items": [
          {
            "itemType": "Currency:MtxGiveaway",
            "itemGuid": "c384fe1c-cf33-48ab-868e-56125c6f9b88",
            "itemProfile": "profile0",
            "quantity": 50
          },
          {
            "itemType": "Giftbox:GB_DailyGems_Laundry23",
            "itemGuid": "a1c51a9c-8685-49d2-a513-4e2c3d1831c2",
            "itemProfile": "profile0",
            "quantity": 1
          }
        ]
      }
    }
  ],
  "profileCommandRevision": 24041,
  "serverTime": "2022-12-29T05:44:25.027Z",
  "responseVersion": 1
}
```

*Response body was encoded in base64*

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
