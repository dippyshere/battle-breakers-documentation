# Add To Monster Pit

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/:accountId/AddToMonsterPit?profileId=monsterpit&rvn=6483*

___

## Request

```http
POST /wex/api/game/v2/profile/:accountId/AddToMonsterPit?profileId=monsterpit&rvn=6483 HTTP/1.1
```

### Path Parameters

| Name     | Value                             |
|----------|-----------------------------------|
| acountId | ec0ebb7e56f6454e86c62299a7b32e21  |

### Query String

| Name      | Value      |
|-----------|------------|
| profileId | monsterpit |
| rvn       | 6483       |

### Request Headers

| Name                         | Value                                                                                                                                                                                                                                                                              |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Host                         | wex-public-service-live-prod.ol.epicgames.com                                                                                                                                                                                                                                      |
| Accept-Encoding              | deflate, gzip                                                                                                                                                                                                                                                                      |
| Accept                       | \*/\*                                                                                                                                                                                                                                                                              |
| Content-Type                 | application/json                                                                                                                                                                                                                                                                   |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":23947},{"profileId":"levels","clientCommandRevision":14433},{"profileId":"friends","clientCommandRevision":8252},{"profileId":"monsterpit","clientCommandRevision":1078},{"profileId":"multiplayer","clientCommandRevision":900}] |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-BF5B64544412777DD4C71C8545BEAE11-A6F85CB74658ACDAA5A1A4A222410CE5                                                                                                                                                                             |
| User-Agent                   | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit                                                                                                                                                                                                                   |
| Authorization                | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md)                                                                                                                                                              |
| Content-Length               | 64                                                                                                                                                                                                                                                                                 |

### Request Body

```json
{
  "characterItemId": "0f400dd1-7b9a-4ed0-a6a0-905f90412dff"
}
```

___

## Response

#### Status: 200 OK

### Response Headers

| Name                         | Value                                                                                                  |
|------------------------------|--------------------------------------------------------------------------------------------------------|
| Date                         | Wed, 28 Dec 2022 12:09:20 GMT                                                                          |
| Content-Type                 | application/json                                                                                       |
| Content-Length               | 926                                                                                                    |
| X-EpicGames-Profile-Revision | 6483                                                                                                   |
| X-EpicGames-McpVersion       | prod Release-1.88-1.88 build 107 cl 19310354                                                           |
| X-EpicGames-ContentVersion   | 1.88.244-r17036752                                                                                     |
| X-EpicGames-MinBuild         | 17036752                                                                                               |
| X-Epic-Device-ID             | 68009daed09498667a8039cce09983ed                                                                       |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-BF5B64544412777DD4C71C8545BEAE11-A6F85CB74658ACDAA5A1A4A222410CE5 |
| Connection                   | keep-alive                                                                                             |

### Response Body

```json
{
  "profileRevision": 6485,
  "profileId": "monsterpit",
  "profileChangesBaseRevision": 6483,
  "profileChanges": [
    {
      "changeType": "itemAdded",
      "itemId": "0f400dd1-7b9a-4ed0-a6a0-905f90412dff",
      "item": {
        "templateId": "Character:TreasureHunter_VR2_Fire_AntiMaterialCharge_T04",
        "attributes": {
          "gear_weapon_item_id": "",
          "weapon_unlocked": false,
          "sidekick_template_id": "",
          "is_new": false,
          "level": 1,
          "num_sold": 0,
          "skill_level": 1,
          "sidekick_unlocked": false,
          "upgrades": [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0
          ],
          "used_as_sidekick": false,
          "gear_armor_item_id": "",
          "skill_xp": 0,
          "armor_unlocked": false,
          "foil_lvl": -1,
          "xp": 0,
          "rank": 0,
          "sidekick_item_id": ""
        },
        "quantity": 1
      }
    }
  ],
  "profileCommandRevision": 1079,
  "serverTime": "2022-12-28T12:09:20.091Z",
  "multiUpdate": [
    {
      "profileRevision": 40206,
      "profileId": "profile0",
      "profileChangesBaseRevision": 40204,
      "profileChanges": [
        {
          "changeType": "itemRemoved",
          "itemId": "0f400dd1-7b9a-4ed0-a6a0-905f90412dff"
        }
      ],
      "profileCommandRevision": 23948
    }
  ],
  "responseVersion": 1
}
```

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
