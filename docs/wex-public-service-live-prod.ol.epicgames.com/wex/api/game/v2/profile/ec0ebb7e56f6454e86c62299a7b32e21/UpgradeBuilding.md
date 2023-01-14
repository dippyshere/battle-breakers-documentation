# UpgradeBuilding

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/UpgradeBuilding?profileId=profile0&rvn=39270*

___

## Request

```http request
POST /wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/UpgradeBuilding?profileId=profile0&rvn=39270 HTTP/1.1
```

### Query String

| Name | Value |
|---|---|
| profileId | profile0 |
| rvn | 39270 |




### Request Headers

| Name | Value |
|---|---|
| Host | wex-public-service-live-prod.ol.epicgames.com |
| Accept-Encoding | deflate, gzip |
| Accept | \*/\* |
| Content-Type | application/json |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":23264},{"profileId":"levels","clientCommandRevision":14240},{"profileId":"friends","clientCommandRevision":8236},{"profileId":"monsterpit","clientCommandRevision":1037},{"profileId":"multiplayer","clientCommandRevision":835}] |
| X-Epic-Correlation-ID | UE4-550659054c6fbbba966be789c8ecf002-D77C844B4D0785D0053F3CBFB86C4B7D-3179D0D14CACFBB46366D0A8EBC215B0 |
| User-Agent | WorldExplorers/1.88.244-r17036752 Windows/10.0.25267.1.256.64bit |
| Authorization | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |
| Content-Length | 63 |


### Request Body

```json
{
  "buildingItemId": "15d78b45-2fc2-45d1-b465-0d6f3ea18178"
}
```

___

## Response

#### Status: 200 OK




### Response Headers

| Name | Value |
|---|---|
| Date | Sat, 17 Dec 2022 13:33:14 GMT |
| Content-Type | application/json |
| Content-Length | 834 |
| X-EpicGames-Profile-Revision | 39270 |
| X-EpicGames-McpVersion | prod Release-1.88-1.88 build 107 cl 19310354 |
| X-EpicGames-ContentVersion | 1.88.244-r17036752 |
| X-EpicGames-MinBuild | 17036752 |
| X-Epic-Device-ID | 7b6449837a601db90694fa85168cb856 |
| X-Epic-Correlation-ID | UE4-550659054c6fbbba966be789c8ecf002-D77C844B4D0785D0053F3CBFB86C4B7D-3179D0D14CACFBB46366D0A8EBC215B0 |
| Connection | keep-alive |


### Response Body

```json
{
  "profileRevision": 39271,
  "profileId": "profile0",
  "profileChangesBaseRevision": 39270,
  "profileChanges": [
    {
      "changeType": "itemQuantityChanged",
      "itemId": "daa87593-4b4a-4ffa-a21d-8979d6eb38ed",
      "quantity": 550049973
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "fd806af6-8b9e-400f-a2a3-2dda292ea0e5",
      "quantity": 35
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "15d78b45-2fc2-45d1-b465-0d6f3ea18178",
      "attributeName": "level",
      "attributeValue": 24
    },
    {
      "changeType": "statModified",
      "name": "activity",
      "value": {
        "a": {
          "date": "2022-12-17T00:00:00.000Z",
          "claimed": false,
          "props": {
            "HeroAcquired": 2,
            "AccountLevelUp": 1,
            "BaseBonus": 10,
            "EnergySpent": 23,
            "BuildingUpgrade": 1
          }
        },
        "b": {
          "date": "2022-12-15T00:00:00.000Z",
          "claimed": false,
          "props": {
            "BaseBonus": 10
          }
        },
        "standardGift": 10
      }
    }
  ],
  "profileCommandRevision": 23265,
  "serverTime": "2022-12-17T13:33:14.619Z",
  "responseVersion": 1
}
```

*Response body was encoded in base64*

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
