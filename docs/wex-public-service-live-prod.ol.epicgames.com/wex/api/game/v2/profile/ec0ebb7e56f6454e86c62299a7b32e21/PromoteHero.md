# PromoteHero

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/PromoteHero?profileId=profile0&rvn=40481*



___

## Request

```http request
POST /wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/PromoteHero?profileId=profile0&rvn=40481 HTTP/1.1
```

### Query String

| Name | Value |
|---|---|
| profileId | profile0 |
| rvn | 40481 |




### Request Headers

| Name | Value |
|---|---|
| Host | wex-public-service-live-prod.ol.epicgames.com |
| Accept-Encoding | deflate, gzip |
| Accept | \*/\* |
| Content-Type | application/json |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":24166},{"profileId":"levels","clientCommandRevision":14480},{"profileId":"friends","clientCommandRevision":8264},{"profileId":"monsterpit","clientCommandRevision":1081},{"profileId":"multiplayer","clientCommandRevision":900}] |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-A2B17BEF430FEBE00DD3B6A9B7CC54E5 |
| User-Agent | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit |
| Authorization | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |
| Content-Length | 108 |


### Request Body

```json
{
  "heroItemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
  "bIsInPit": false,
  "prestigePromote": false
}
```

___

## Response

#### Status: 200 OK




### Response Headers

| Name | Value |
|---|---|
| Date | Thu, 29 Dec 2022 06:06:34 GMT |
| Content-Type | application/json |
| Content-Length | 1036 |
| X-EpicGames-Profile-Revision | 40481 |
| X-EpicGames-McpVersion | prod Release-1.88-1.88 build 107 cl 19310354 |
| X-EpicGames-ContentVersion | 1.88.244-r17036752 |
| X-EpicGames-MinBuild | 17036752 |
| X-Epic-Device-ID | 68009daed09498667a8039cce09983ed |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-A2B17BEF430FEBE00DD3B6A9B7CC54E5 |
| Connection | keep-alive |


### Response Body

```json
{
  "profileRevision": 40482,
  "profileId": "profile0",
  "profileChangesBaseRevision": 40481,
  "profileChanges": [
    {
      "changeType": "itemQuantityChanged",
      "itemId": "daa87593-4b4a-4ffa-a21d-8979d6eb38ed",
      "quantity": 565740462
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "ff4b9833-ff77-458f-aca9-acfd817d9703",
      "quantity": 41710
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "d61fef89-f42b-40a2-9e5e-4a264714a7fd",
      "quantity": 376
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "rank",
      "attributeValue": 10
    },
    {
      "changeType": "statModified",
      "name": "activity",
      "value": {
        "a": {
          "date": "2022-12-28T00:00:00.000Z",
          "claimed": true,
          "props": {
            "HeroAcquired": 137,
            "HeroPromote": 1,
            "HeroEvolve": 1,
            "MonsterPitLevelUp": 1,
            "HeroFoil": 1,
            "AccountLevelUp": 2,
            "BaseBonus": 10,
            "EnergySpent": 187
          }
        },
        "b": {
          "date": "2022-12-29T00:00:00.000Z",
          "claimed": false,
          "props": {
            "HeroAcquired": 200,
            "HeroPromote": 10,
            "BaseBonus": 10,
            "EnergySpent": 8
          }
        },
        "standardGift": 10
      }
    }
  ],
  "profileCommandRevision": 24167,
  "serverTime": "2022-12-29T06:06:34.066Z",
  "responseVersion": 1
}
```

*Response body was encoded in base64*

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
