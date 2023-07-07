# Level Up Hero

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/:accountId/LevelUpHero?profileId=profile0&rvn=40482*

___

## Request

```http
POST /wex/api/game/v2/profile/:accountId/LevelUpHero?profileId=profile0&rvn=40482 HTTP/1.1
```

### Path Parameters

| Name     | Value                             |
|----------|-----------------------------------|
| acountId | ec0ebb7e56f6454e86c62299a7b32e21  |

### Query String

| Name      | Value    |
|-----------|----------|
| profileId | profile0 |
| rvn       | 40482    |

### Request Headers

| Name                         | Value                                                                                                                                                                                                                                                                              |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Host                         | wex-public-service-live-prod.ol.epicgames.com                                                                                                                                                                                                                                      |
| Accept-Encoding              | deflate, gzip                                                                                                                                                                                                                                                                      |
| Accept                       | \*/\*                                                                                                                                                                                                                                                                              |
| Content-Type                 | application/json                                                                                                                                                                                                                                                                   |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":24167},{"profileId":"levels","clientCommandRevision":14480},{"profileId":"friends","clientCommandRevision":8264},{"profileId":"monsterpit","clientCommandRevision":1081},{"profileId":"multiplayer","clientCommandRevision":900}] |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-81837E1D44F953936B661D9E22E4DE20                                                                                                                                                                             |
| User-Agent                   | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit                                                                                                                                                                                                                   |
| Authorization                | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md)                                                                                                                                                              |
| Content-Length               | 122                                                                                                                                                                                                                                                                                |

### Request Body

```json
{
  "heroItemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
  "bIsInPit": false,
  "bMaxOut": false,
  "numLevelUps": 149
}
```

___

## Response

#### Status: 200 OK

### Response Headers

| Name                         | Value                                                                                                  |
|------------------------------|--------------------------------------------------------------------------------------------------------|
| Date                         | Thu, 29 Dec 2022 06:06:43 GMT                                                                          |
| Content-Type                 | application/json                                                                                       |
| Transfer-Encoding            | chunked                                                                                                |
| X-EpicGames-McpVersion       | prod Release-1.88-1.88 build 107 cl 19310354                                                           |
| X-EpicGames-ContentVersion   | 1.88.244-r17036752                                                                                     |
| X-EpicGames-MinBuild         | 17036752                                                                                               |
| X-EpicGames-Profile-Revision | 40482                                                                                                  |
| X-Epic-Device-ID             | 68009daed09498667a8039cce09983ed                                                                       |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-81837E1D44F953936B661D9E22E4DE20 |
| Connection                   | keep-alive                                                                                             |

### Response Body

```json
{
  "profileRevision": 40483,
  "profileId": "profile0",
  "profileChangesBaseRevision": 40482,
  "profileChanges": [
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14761027
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 2
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14760827
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 3
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14760527
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 4
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14760127
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 5
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14759627
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 6
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14759027
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 7
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14758327
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 8
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14757527
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 9
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14756627
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 10
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14755627
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 11
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14754527
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 12
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14753327
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 13
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14752027
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 14
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14750627
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 15
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14749127
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 16
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14747527
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 17
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14745827
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 18
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14744027
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 19
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14742127
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 20
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14740127
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 21
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14738027
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 22
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14735827
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 23
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14733527
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 24
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14731127
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 25
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14728627
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 26
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14726027
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 27
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14723327
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 28
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14720527
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 29
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14717627
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 30
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14714627
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 31
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14711527
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 32
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14708327
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 33
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14705027
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 34
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14701627
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 35
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14698127
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 36
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14694527
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 37
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14690827
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 38
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14687027
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 39
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14683127
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 40
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14679127
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 41
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14675027
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 42
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14670827
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 43
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14666527
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 44
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14662127
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 45
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14657627
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 46
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14653027
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 47
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14648327
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 48
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14643527
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 49
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14638627
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 50
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14633627
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 51
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14628527
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 52
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14623327
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 53
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14618027
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 54
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14612627
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 55
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14607127
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 56
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14601527
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 57
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14595827
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 58
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14590027
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 59
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14584127
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 60
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14578127
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 61
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14572027
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 62
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14565827
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 63
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14559527
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 64
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14553127
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 65
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14546627
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 66
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14540027
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 67
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14533327
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 68
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14526527
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 69
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14519627
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 70
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14512627
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 71
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14505527
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 72
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14498327
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 73
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14491027
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 74
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14483627
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 75
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14476127
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 76
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14468527
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 77
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14460827
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 78
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14453027
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 79
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14445127
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 80
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14437127
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 81
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14429027
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 82
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14420827
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 83
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14412527
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 84
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14404127
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 85
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14395627
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 86
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14387027
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 87
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14378327
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 88
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14369527
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 89
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14360627
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 90
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14351627
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 91
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14342527
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 92
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14333327
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 93
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14324027
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 94
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14314627
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 95
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14305127
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 96
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14295527
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 97
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14285827
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 98
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14276027
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 99
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14266127
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 100
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14256127
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 101
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14246027
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 102
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14235827
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 103
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14225527
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 104
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14215127
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 105
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14204627
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 106
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14194027
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 107
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14183327
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 108
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14172527
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 109
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14161627
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 110
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14150627
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 111
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14139527
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 112
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14128327
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 113
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14117027
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 114
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14105627
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 115
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14094127
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 116
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14082527
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 117
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14070827
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 118
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14059027
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 119
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14047127
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 120
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 14023127
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 121
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 13998927
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 122
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 13974527
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 123
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 13949927
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 124
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 13925127
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 125
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 13900127
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 126
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 13874927
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 127
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 13849527
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 128
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 13823927
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 129
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 13798127
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 130
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 13772127
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 131
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 13745927
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 132
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 13719527
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 133
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 13692927
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 134
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 13666127
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 135
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 13639127
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 136
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 13611927
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 137
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 13584527
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 138
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 13556927
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 139
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 13529127
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 140
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 13501127
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 141
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 13472927
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 142
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 13444527
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 143
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 13415927
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 144
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 13387127
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 145
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 13358127
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 146
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 13328927
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 147
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 13299527
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 148
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 13269927
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 149
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 13240127
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "level",
      "attributeValue": 150
    }
  ],
  "notifications": [
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 2
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 3
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 4
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 5
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 6
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 7
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 8
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 9
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 10
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 11
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 12
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 13
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 14
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 15
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 16
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 17
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 18
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 19
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 20
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 21
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 22
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 23
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 24
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 25
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 26
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 27
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 28
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 29
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 30
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 31
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 32
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 33
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 34
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 35
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 36
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 37
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 38
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 39
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 40
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 41
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 42
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 43
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 44
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 45
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 46
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 47
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 48
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 49
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 50
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 51
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 52
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 53
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 54
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 55
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 56
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 57
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 58
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 59
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 60
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 61
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 62
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 63
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 64
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 65
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 66
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 67
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 68
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 69
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 70
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 71
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 72
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 73
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 74
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 75
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 76
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 77
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 78
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 79
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 80
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 81
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 82
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 83
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 84
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 85
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 86
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 87
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 88
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 89
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 90
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 91
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 92
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 93
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 94
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 95
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 96
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 97
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 98
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 99
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 100
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 101
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 102
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 103
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 104
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 105
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 106
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 107
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 108
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 109
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 110
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 111
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 112
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 113
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 114
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 115
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 116
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 117
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 118
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 119
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 120
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 121
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 122
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 123
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 124
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 125
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 126
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 127
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 128
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 129
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 130
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 131
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 132
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 133
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 134
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 135
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 136
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 137
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 138
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 139
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 140
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 141
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 142
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 143
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 144
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 145
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 146
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 147
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 148
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 149
    },
    {
      "type": "CharacterLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 150
    }
  ],
  "profileCommandRevision": 24168,
  "serverTime": "2022-12-29T06:06:43.775Z",
  "responseVersion": 1
}
```

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
