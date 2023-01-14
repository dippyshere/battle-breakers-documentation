# SendGiftPoints

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/SendGiftPoints?profileId=profile0&rvn=40315*



___

## Request

```http request
POST /wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/SendGiftPoints?profileId=profile0&rvn=40315 HTTP/1.1
```

### Query String

| Name | Value |
|---|---|
| profileId | profile0 |
| rvn | 40315 |




### Request Headers

| Name | Value |
|---|---|
| Host | wex-public-service-live-prod.ol.epicgames.com |
| Accept-Encoding | deflate, gzip |
| Accept | \*/\* |
| Content-Type | application/json |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":24007},{"profileId":"levels","clientCommandRevision":14476},{"profileId":"friends","clientCommandRevision":8262},{"profileId":"monsterpit","clientCommandRevision":1081},{"profileId":"multiplayer","clientCommandRevision":900}] |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-E1A66BD445CE08321E91B6A855926B5E |
| User-Agent | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit |
| Authorization | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |
| Content-Length | 4 |


### Request Body

```json
{}
```

___

## Response

#### Status: 200 OK




### Response Headers

| Name | Value |
|---|---|
| Date | Thu, 29 Dec 2022 05:43:35 GMT |
| Content-Type | application/json |
| Content-Length | 699 |
| X-EpicGames-McpVersion | prod Release-1.88-1.88 build 107 cl 19310354 |
| X-EpicGames-ContentVersion | 1.88.244-r17036752 |
| X-EpicGames-MinBuild | 17036752 |
| X-EpicGames-Profile-Revision | 40315 |
| X-Epic-Device-ID | 68009daed09498667a8039cce09983ed |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-E1A66BD445CE08321E91B6A855926B5E |
| Connection | keep-alive |


### Response Body

```json
{
  "profileRevision": 40317,
  "profileId": "profile0",
  "profileChangesBaseRevision": 40315,
  "profileChanges": [
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
            "BaseBonus": 10
          }
        },
        "standardGift": 10
      }
    }
  ],
  "profileCommandRevision": 24008,
  "serverTime": "2022-12-29T05:43:35.542Z",
  "multiUpdate": [
    {
      "profileRevision": 9894,
      "profileId": "friends",
      "profileChangesBaseRevision": 9892,
      "profileChanges": [],
      "profileCommandRevision": 8262
    }
  ],
  "responseVersion": 1
}
```

*Response body was encoded in base64*

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
