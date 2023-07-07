# Evolve Hero

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/:accountId/EvolveHero?profileId=profile0&rvn=40483*

___

## Request

```http
POST /wex/api/game/v2/profile/:accountId/EvolveHero?profileId=profile0&rvn=40483 HTTP/1.1
```

### Path Parameters

| Name     | Value                             |
|----------|-----------------------------------|
| acountId | ec0ebb7e56f6454e86c62299a7b32e21  |

### Query String

| Name      | Value    |
|-----------|----------|
| profileId | profile0 |
| rvn       | 40483    |

### Request Headers

| Name                         | Value                                                                                                                                                                                                                                                                              |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Host                         | wex-public-service-live-prod.ol.epicgames.com                                                                                                                                                                                                                                      |
| Accept-Encoding              | deflate, gzip                                                                                                                                                                                                                                                                      |
| Accept                       | \*/\*                                                                                                                                                                                                                                                                              |
| Content-Type                 | application/json                                                                                                                                                                                                                                                                   |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":24168},{"profileId":"levels","clientCommandRevision":14480},{"profileId":"friends","clientCommandRevision":8264},{"profileId":"monsterpit","clientCommandRevision":1081},{"profileId":"multiplayer","clientCommandRevision":900}] |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-305E691143513DA7A72C87B1826B0608                                                                                                                                                                             |
| User-Agent                   | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit                                                                                                                                                                                                                   |
| Authorization                | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md)                                                                                                                                                              |
| Content-Length               | 147                                                                                                                                                                                                                                                                                |

### Request Body

```json
{
  "heroItemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
  "bIsInPit": false,
  "evoPathName": "Recipe_MartialArtist_SR2_Fire_SeveringBlow_T06"
}
```

___

## Response

#### Status: 200 OK

### Response Headers

| Name                         | Value                                                                                                  |
|------------------------------|--------------------------------------------------------------------------------------------------------|
| Date                         | Thu, 29 Dec 2022 06:06:49 GMT                                                                          |
| Content-Type                 | application/json                                                                                       |
| Content-Length               | 1669                                                                                                   |
| X-EpicGames-Profile-Revision | 40483                                                                                                  |
| X-EpicGames-McpVersion       | prod Release-1.88-1.88 build 107 cl 19310354                                                           |
| X-EpicGames-ContentVersion   | 1.88.244-r17036752                                                                                     |
| X-EpicGames-MinBuild         | 17036752                                                                                               |
| X-Epic-Device-ID             | 68009daed09498667a8039cce09983ed                                                                       |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-305E691143513DA7A72C87B1826B0608 |
| Connection                   | keep-alive                                                                                             |

### Response Body

```json
{
  "profileRevision": 40484,
  "profileId": "profile0",
  "profileChangesBaseRevision": 40483,
  "profileChanges": [
    {
      "changeType": "itemQuantityChanged",
      "itemId": "daa87593-4b4a-4ffa-a21d-8979d6eb38ed",
      "quantity": 565490462
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "ff4b9833-ff77-458f-aca9-acfd817d9703",
      "quantity": 41410
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "d61fef89-f42b-40a2-9e5e-4a264714a7fd",
      "quantity": 362
    },
    {
      "changeType": "itemAdded",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "item": {
        "templateId": "Character:MartialArtist_SR2_Fire_SeveringBlow_T06",
        "attributes": {
          "gear_weapon_item_id": "",
          "weapon_unlocked": false,
          "sidekick_template_id": "",
          "level": 150,
          "is_new": false,
          "num_sold": 0,
          "skill_level": 1,
          "sidekick_unlocked": false,
          "upgrades": [
            25,
            1,
            25,
            1,
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
          "rank": 10,
          "sidekick_item_id": ""
        },
        "quantity": 1
      }
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
            "HeroEvolve": 1,
            "BaseBonus": 10,
            "EnergySpent": 8
          }
        },
        "standardGift": 10
      }
    }
  ],
  "notifications": [
    {
      "type": "WExpCharacterEvolution",
      "primary": true,
      "oldItemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "oldTemplateId": "Character:MartialArtist_SR2_Fire_SeveringBlow_T05",
      "newItemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d"
    }
  ],
  "profileCommandRevision": 24169,
  "serverTime": "2022-12-29T06:06:49.707Z",
  "responseVersion": 1
}
```

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
