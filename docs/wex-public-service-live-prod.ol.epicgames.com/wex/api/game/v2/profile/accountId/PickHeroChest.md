# Pick Hero Chest

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/:accountId/PickHeroChest?profileId=profile0&rvn=39990*

___

## Request

```http
POST /wex/api/game/v2/profile/:accountId/PickHeroChest?profileId=profile0&rvn=39990 HTTP/1.1
```

### Path Parameters

| Name     | Value                             |
|----------|-----------------------------------|
| acountId | ec0ebb7e56f6454e86c62299a7b32e21  |

### Query String

| Name      | Value    |
|-----------|----------|
| profileId | profile0 |
| rvn       | 39990    |

### Request Headers

| Name                         | Value                                                                                                                                                                                                                                                                              |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Host                         | wex-public-service-live-prod.ol.epicgames.com                                                                                                                                                                                                                                      |
| Accept-Encoding              | deflate, gzip                                                                                                                                                                                                                                                                      |
| Accept                       | \*/\*                                                                                                                                                                                                                                                                              |
| Content-Type                 | application/json                                                                                                                                                                                                                                                                   |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":23817},{"profileId":"levels","clientCommandRevision":14357},{"profileId":"friends","clientCommandRevision":8252},{"profileId":"monsterpit","clientCommandRevision":1074},{"profileId":"multiplayer","clientCommandRevision":847}] |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-BF5B64544412777DD4C71C8545BEAE11-2C39865447688B9B6B2856B6DBE7108D                                                                                                                                                                             |
| User-Agent                   | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit                                                                                                                                                                                                                   |
| Authorization                | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md)                                                                                                                                                              |
| Content-Length               | 116                                                                                                                                                                                                                                                                                |

### Request Body

```json
{
  "towerId": "c983aa2d-f59c-4b43-a471-78d74ff05ea5",
  "heroTrackId": "CoreBronze",
  "heroChestType": "Normal"
}
```

___

## Response

#### Status: 200 OK

### Response Headers

| Name                         | Value                                                                                                  |
|------------------------------|--------------------------------------------------------------------------------------------------------|
| Date                         | Wed, 28 Dec 2022 11:58:58 GMT                                                                          |
| Content-Type                 | application/json                                                                                       |
| Content-Length               | 594                                                                                                    |
| X-EpicGames-McpVersion       | prod Release-1.88-1.88 build 107 cl 19310354                                                           |
| X-EpicGames-ContentVersion   | 1.88.244-r17036752                                                                                     |
| X-EpicGames-MinBuild         | 17036752                                                                                               |
| X-EpicGames-Profile-Revision | 39990                                                                                                  |
| X-Epic-Device-ID             | 68009daed09498667a8039cce09983ed                                                                       |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-BF5B64544412777DD4C71C8545BEAE11-2C39865447688B9B6B2856B6DBE7108D |
| Connection                   | keep-alive                                                                                             |

### Response Body

```json
{
  "profileRevision": 39991,
  "profileId": "profile0",
  "profileChangesBaseRevision": 39990,
  "profileChanges": [
    {
      "changeType": "itemAttrChanged",
      "itemId": "c983aa2d-f59c-4b43-a471-78d74ff05ea5",
      "attributeName": "active_chest",
      "attributeValue": {
        "heroChoicesDeprecated": [
          "Character:MartialArtist_UC1_Fire_ChargedFist_T03",
          "Character:Mage_UC1_Nature_ElementalPhantom_T03",
          "Character:Warrior_UC1_Water_Pummel_T03"
        ],
        "itemChoices": [],
        "itemQuantities": [],
        "heroTrackId": "CoreBronze",
        "heroChestType": "Normal",
        "foilLevel": 0
      }
    }
  ],
  "profileCommandRevision": 23818,
  "serverTime": "2022-12-28T11:58:58.258Z",
  "responseVersion": 1
}
```

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
