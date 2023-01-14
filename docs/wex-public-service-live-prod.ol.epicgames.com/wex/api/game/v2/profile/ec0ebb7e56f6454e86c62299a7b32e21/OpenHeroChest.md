# OpenHeroChest

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/OpenHeroChest?profileId=profile0&rvn=39991*

___

## Request

```http request
POST /wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/OpenHeroChest?profileId=profile0&rvn=39991 HTTP/1.1
```

### Query String

| Name | Value |
|---|---|
| profileId | profile0 |
| rvn | 39991 |




### Request Headers

| Name | Value |
|---|---|
| Host | wex-public-service-live-prod.ol.epicgames.com |
| Accept-Encoding | deflate, gzip |
| Accept | \*/\* |
| Content-Type | application/json |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":23818},{"profileId":"levels","clientCommandRevision":14357},{"profileId":"friends","clientCommandRevision":8252},{"profileId":"monsterpit","clientCommandRevision":1074},{"profileId":"multiplayer","clientCommandRevision":847}] |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-BF5B64544412777DD4C71C8545BEAE11-1F8A82814B85415C5B1E609062337990 |
| User-Agent | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit |
| Authorization | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |
| Content-Length | 147 |


### Request Body

```json
{
  "towerId": "c983aa2d-f59c-4b43-a471-78d74ff05ea5",
  "itemTemplateId": "Character:Mage_UC1_Nature_ElementalPhantom_T03",
  "itemQuantity": 1
}
```

___

## Response

#### Status: 200 OK




### Response Headers

| Name | Value |
|---|---|
| Date | Wed, 28 Dec 2022 11:59:01 GMT |
| Content-Type | application/json |
| Content-Length | 1851 |
| X-EpicGames-Profile-Revision | 39991 |
| X-EpicGames-McpVersion | prod Release-1.88-1.88 build 107 cl 19310354 |
| X-EpicGames-ContentVersion | 1.88.244-r17036752 |
| X-EpicGames-MinBuild | 17036752 |
| X-Epic-Device-ID | 68009daed09498667a8039cce09983ed |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-BF5B64544412777DD4C71C8545BEAE11-1F8A82814B85415C5B1E609062337990 |
| Connection | keep-alive |


### Response Body

```json
{
  "profileRevision": 39992,
  "profileId": "profile0",
  "profileChangesBaseRevision": 39991,
  "profileChanges": [
    {
      "changeType": "itemRemoved",
      "itemId": "729f561f-2162-4209-aa5e-cf69697e0c4b"
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "c983aa2d-f59c-4b43-a471-78d74ff05ea5",
      "attributeName": "CoreBronze_progress",
      "attributeValue": 293
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "c983aa2d-f59c-4b43-a471-78d74ff05ea5",
      "attributeName": "level",
      "attributeValue": 293
    },
    {
      "changeType": "itemAdded",
      "itemId": "d744db3a-2e42-4834-86d8-36c6931b4f21",
      "item": {
        "templateId": "Character:Mage_UC1_Nature_ElementalPhantom_T03",
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
    },
    {
      "changeType": "statModified",
      "name": "activity",
      "value": {
        "a": {
          "date": "2022-12-28T00:00:00.000Z",
          "claimed": false,
          "props": {
            "HeroAcquired": 2,
            "HeroEvolve": 1,
            "HeroFoil": 1,
            "AccountLevelUp": 1,
            "BaseBonus": 10,
            "EnergySpent": 94
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
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "c983aa2d-f59c-4b43-a471-78d74ff05ea5",
      "attributeName": "active_chest"
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "c983aa2d-f59c-4b43-a471-78d74ff05ea5",
      "attributeName": "chest_options",
      "attributeValue": [
        {
          "heroChoicesDeprecated": [
            "Character:Warrior_Starter_Light_RoboGuy_T02",
            "Character:Mage_Basic_Water_EnergyBlast_T02",
            "Character:Archer_Basic_Dark_AimedShot_T02"
          ],
          "itemChoices": [],
          "itemQuantities": [],
          "heroTrackId": "CoreBronze",
          "foilLevel": 0
        }
      ]
    }
  ],
  "profileCommandRevision": 23819,
  "serverTime": "2022-12-28T11:59:01.214Z",
  "responseVersion": 1
}
```

*Response body was encoded in base64*

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
