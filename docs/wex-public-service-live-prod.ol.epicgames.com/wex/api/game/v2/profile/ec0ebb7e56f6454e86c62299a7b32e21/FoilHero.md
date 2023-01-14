# FoilHero

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/FoilHero?profileId=profile0&rvn=39893*

___

## Request

```http request
POST /wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/FoilHero?profileId=profile0&rvn=39893 HTTP/1.1
```

### Query String

| Name | Value |
|---|---|
| profileId | profile0 |
| rvn | 39893 |




### Request Headers

| Name | Value |
|---|---|
| Host | wex-public-service-live-prod.ol.epicgames.com |
| Accept-Encoding | deflate, gzip |
| Accept | \*/\* |
| Content-Type | application/json |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":23750},{"profileId":"levels","clientCommandRevision":14327},{"profileId":"friends","clientCommandRevision":8247},{"profileId":"monsterpit","clientCommandRevision":1074},{"profileId":"multiplayer","clientCommandRevision":847}] |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-BF5B64544412777DD4C71C8545BEAE11-86FE9DDC438AA91AA385A6B06B37A7E9 |
| User-Agent | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit |
| Authorization | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |
| Content-Length | 80 |


### Request Body

```json
{
  "heroItemId": "2dbc336a-554b-449c-ae84-b4697bb00119",
  "bIsInPit": false
}
```

___

## Response

#### Status: 200 OK




### Response Headers

| Name | Value |
|---|---|
| Date | Wed, 28 Dec 2022 11:41:31 GMT |
| Content-Type | application/json |
| Content-Length | 703 |
| X-EpicGames-Profile-Revision | 39893 |
| X-EpicGames-McpVersion | prod Release-1.88-1.88 build 107 cl 19310354 |
| X-EpicGames-ContentVersion | 1.88.244-r17036752 |
| X-EpicGames-MinBuild | 17036752 |
| X-Epic-Device-ID | 68009daed09498667a8039cce09983ed |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-BF5B64544412777DD4C71C8545BEAE11-86FE9DDC438AA91AA385A6B06B37A7E9 |
| Connection | keep-alive |


### Response Body

```json
{
  "profileRevision": 39894,
  "profileId": "profile0",
  "profileChangesBaseRevision": 39893,
  "profileChanges": [
    {
      "changeType": "itemQuantityChanged",
      "itemId": "39f1336e-1af6-466d-91a6-f59ee85efedc",
      "quantity": 982
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "2dbc336a-554b-449c-ae84-b4697bb00119",
      "attributeName": "foil_lvl",
      "attributeValue": 1
    },
    {
      "changeType": "statModified",
      "name": "activity",
      "value": {
        "a": {
          "date": "2022-12-28T00:00:00.000Z",
          "claimed": false,
          "props": {
            "HeroAcquired": 1,
            "HeroFoil": 1,
            "BaseBonus": 10
          }
        },
        "b": {
          "date": "2022-12-27T00:00:00.000Z",
          "claimed": true,
          "props": {
            "BaseBonus": 10,
            "EnergySpent": 3
          }
        },
        "standardGift": 10
      }
    }
  ],
  "profileCommandRevision": 23751,
  "serverTime": "2022-12-28T11:41:31.330Z",
  "responseVersion": 1
}
```

*Response body was encoded in base64*

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
