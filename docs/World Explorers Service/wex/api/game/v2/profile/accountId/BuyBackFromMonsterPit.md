# Buy Back From Monster Pit

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/:accountId/BuyBackFromMonsterPit?profileId=monsterpit&rvn=6363*

___

## Request

```http
POST /wex/api/game/v2/profile/:accountId/BuyBackFromMonsterPit?profileId=monsterpit&rvn=6363 HTTP/1.1
```

### Path Parameters

| Name     | Value                             |
|----------|-----------------------------------|
| acountId | ec0ebb7e56f6454e86c62299a7b32e21  |

### Query String

| Name      | Value      |
|-----------|------------|
| profileId | monsterpit |
| rvn       | 6363       |

### Request Headers

| Name                         | Value                                                                                                                                                                                                                                                                              |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Host                         | wex-public-service-live-prod.ol.epicgames.com                                                                                                                                                                                                                                      |
| Accept-Encoding              | deflate, gzip                                                                                                                                                                                                                                                                      |
| Accept                       | \*/\*                                                                                                                                                                                                                                                                              |
| Content-Type                 | application/json                                                                                                                                                                                                                                                                   |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":23683},{"profileId":"levels","clientCommandRevision":14325},{"profileId":"friends","clientCommandRevision":8246},{"profileId":"monsterpit","clientCommandRevision":1069},{"profileId":"multiplayer","clientCommandRevision":847}] |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-1154642548C092033C1B6F950A4EB35B-70B4279C4C6C1CD8EA5CF5AFF9E56F78                                                                                                                                                                             |
| User-Agent                   | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit                                                                                                                                                                                                                   |
| Authorization                | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md)                                                                                                                                                              |
| Content-Length               | 67                                                                                                                                                                                                                                                                                 |

### Request Body

```json
{
  "characterTemplateId": "Character:Cleric_C1_Light_Pixie_T01"
}
```

___

## Response

#### Status: 200 OK

### Response Headers

| Name                         | Value                                                                                                  |
|------------------------------|--------------------------------------------------------------------------------------------------------|
| Date                         | Tue, 27 Dec 2022 06:57:33 GMT                                                                          |
| Content-Type                 | application/json                                                                                       |
| Content-Length               | 1365                                                                                                   |
| X-EpicGames-Profile-Revision | 6363                                                                                                   |
| X-EpicGames-McpVersion       | prod Release-1.88-1.88 build 107 cl 19310354                                                           |
| X-EpicGames-ContentVersion   | 1.88.244-r17036752                                                                                     |
| X-EpicGames-MinBuild         | 17036752                                                                                               |
| X-Epic-Device-ID             | 68009daed09498667a8039cce09983ed                                                                       |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-1154642548C092033C1B6F950A4EB35B-70B4279C4C6C1CD8EA5CF5AFF9E56F78 |
| Connection                   | keep-alive                                                                                             |

### Response Body

```json
{
  "profileRevision": 6365,
  "profileId": "monsterpit",
  "profileChangesBaseRevision": 6363,
  "profileChanges": [
    {
      "changeType": "itemAttrChanged",
      "itemId": "7e2c681a-95d8-4a8f-a245-be2de39e94e8",
      "attributeName": "num_sold",
      "attributeValue": 0
    }
  ],
  "profileCommandRevision": 1070,
  "serverTime": "2022-12-27T06:57:33.649Z",
  "multiUpdate": [
    {
      "profileRevision": 39819,
      "profileId": "profile0",
      "profileChangesBaseRevision": 39817,
      "profileChanges": [
        {
          "changeType": "itemQuantityChanged",
          "itemId": "daa87593-4b4a-4ffa-a21d-8979d6eb38ed",
          "quantity": 557069923
        },
        {
          "changeType": "itemQuantityChanged",
          "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
          "quantity": 12950053
        },
        {
          "changeType": "itemQuantityChanged",
          "itemId": "1b148e65-99c0-4eb8-a99d-7377f537276e",
          "quantity": 328
        },
        {
          "changeType": "itemQuantityChanged",
          "itemId": "46366ac8-8b65-4af2-89bd-3dd1d175307b",
          "quantity": 248
        },
        {
          "changeType": "itemAdded",
          "itemId": "05c96b3f-c931-4754-83ad-5134c3373e40",
          "item": {
            "templateId": "Character:Cleric_C1_Light_Pixie_T01",
            "attributes": {
              "gear_weapon_item_id": "",
              "weapon_unlocked": false,
              "sidekick_template_id": "",
              "level": 1,
              "is_new": true,
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
      "profileCommandRevision": 23684
    }
  ],
  "responseVersion": 1
}
```

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
