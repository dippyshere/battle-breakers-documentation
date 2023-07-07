# Claim Territory

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/:accountId/ClaimTerritory?profileId=levels&rvn=131*

___

## Request

```http
POST /wex/api/game/v2/profile/:accountId/ClaimTerritory?profileId=levels&rvn=131 HTTP/1.1
```

### Path Parameters

| Name     | Value                             |
|----------|-----------------------------------|
| acountId | ec0ebb7e56f6454e86c62299a7b32e21  |

### Query String

| Name      | Value  |
|-----------|--------|
| profileId | levels |
| rvn       | 131    |

### Request Headers

| Name                         | Value                                                                                                                                                                                                                                                                   |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Host                         | wex-public-service-live-prod.ol.epicgames.com                                                                                                                                                                                                                           |
| Accept-Encoding              | deflate, gzip                                                                                                                                                                                                                                                           |
| Accept                       | \*/\*                                                                                                                                                                                                                                                                   |
| Content-Type                 | application/json                                                                                                                                                                                                                                                        |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":134},{"profileId":"levels","clientCommandRevision":65},{"profileId":"friends","clientCommandRevision":11},{"profileId":"monsterpit","clientCommandRevision":18},{"profileId":"multiplayer","clientCommandRevision":5}] |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-420FE66A4AACA5058BA3B193D82F56CE-165E50BF440BDA4461B0B7908A78E8AA                                                                                                                                                                  |
| User-Agent                   | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit                                                                                                                                                                                                        |
| Authorization                | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md)                                                                                                                                                   |
| Content-Length               | 58                                                                                                                                                                                                                                                                      |

### Request Body

```json
{
  "territoryId": "Territory.ForestOfMixedEmotions.D1"
}
```

___

## Response

#### Status: 200 OK

### Response Headers

| Name                         | Value                                                                                                  |
|------------------------------|--------------------------------------------------------------------------------------------------------|
| Date                         | Tue, 27 Dec 2022 06:26:49 GMT                                                                          |
| Content-Type                 | application/json                                                                                       |
| Content-Length               | 1260                                                                                                   |
| X-EpicGames-Profile-Revision | 131                                                                                                    |
| X-EpicGames-McpVersion       | prod Release-1.88-1.88 build 107 cl 19310354                                                           |
| X-EpicGames-ContentVersion   | 1.88.244-r17036752                                                                                     |
| X-EpicGames-MinBuild         | 17036752                                                                                               |
| X-Epic-Device-ID             | 68009daed09498667a8039cce09983ed                                                                       |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-420FE66A4AACA5058BA3B193D82F56CE-165E50BF440BDA4461B0B7908A78E8AA |
| Connection                   | keep-alive                                                                                             |

### Response Body

```json
{
  "profileRevision": 133,
  "profileId": "levels",
  "profileChangesBaseRevision": 131,
  "profileChanges": [
    {
      "changeType": "itemAdded",
      "itemId": "251eaac8-fe8e-46b7-b100-f376d468bff5",
      "item": {
        "templateId": "WorldUnlock:Territory",
        "attributes": {
          "territoryId": "Territory.ForestOfMixedEmotions.D1"
        },
        "quantity": 1
      }
    }
  ],
  "notifications": [
    {
      "type": "WExpTerritoryClaim",
      "primary": true,
      "territoryId": "Territory.ForestOfMixedEmotions.D1",
      "lootResult": {
        "tierGroupName": "LTG.FC.Territory.Claim",
        "items": [
          {
            "itemType": "Currency:MtxGiveaway",
            "itemGuid": "43b9acd8-7b61-42ed-98ff-f5b938ce859b",
            "itemProfile": "profile0",
            "quantity": 100
          }
        ]
      }
    }
  ],
  "profileCommandRevision": 66,
  "serverTime": "2022-12-27T06:26:49.093Z",
  "multiUpdate": [
    {
      "profileRevision": 205,
      "profileId": "profile0",
      "profileChangesBaseRevision": 203,
      "profileChanges": [
        {
          "changeType": "statModified",
          "name": "num_territories_claimed",
          "value": 1
        },
        {
          "changeType": "itemQuantityChanged",
          "itemId": "43b9acd8-7b61-42ed-98ff-f5b938ce859b",
          "quantity": 600
        },
        {
          "changeType": "statModified",
          "name": "activity",
          "value": {
            "a": {
              "date": "2022-12-27T00:00:00.000Z",
              "claimed": false,
              "props": {
                "HeroAcquired": 32,
                "AccountLevelUp": 10,
                "BaseBonus": 10,
                "EnergySpent": 77,
                "TerritoryClaimed": 1,
                "BuildingUpgrade": 5
              }
            },
            "standardGift": 10
          }
        }
      ],
      "profileCommandRevision": 135
    }
  ],
  "responseVersion": 1
}
```

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
