# RemoveFromMonsterPit

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/RemoveFromMonsterPit?profileId=monsterpit&rvn=6367*

___

## Request

```http request
POST /wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/RemoveFromMonsterPit?profileId=monsterpit&rvn=6367 HTTP/1.1
```

### Query String

| Name | Value |
|---|---|
| profileId | monsterpit |
| rvn | 6367 |




### Request Headers

| Name | Value |
|---|---|
| Host | wex-public-service-live-prod.ol.epicgames.com |
| Accept-Encoding | deflate, gzip |
| Accept | \*/\* |
| Content-Type | application/json |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":23686},{"profileId":"levels","clientCommandRevision":14325},{"profileId":"friends","clientCommandRevision":8246},{"profileId":"monsterpit","clientCommandRevision":1071},{"profileId":"multiplayer","clientCommandRevision":847}] |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-1154642548C092033C1B6F950A4EB35B-A2FA7D094E828552652F2ABE26A27C0E |
| User-Agent | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit |
| Authorization | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |
| Content-Length | 64 |


### Request Body

```json
{
  "characterItemId": "6d213240-1b55-4862-9fc1-021ef1f21f2c"
}
```

___

## Response

#### Status: 200 OK




### Response Headers

| Name | Value |
|---|---|
| Date | Tue, 27 Dec 2022 06:57:54 GMT |
| Content-Type | application/json |
| Content-Length | 1009 |
| X-EpicGames-McpVersion | prod Release-1.88-1.88 build 107 cl 19310354 |
| X-EpicGames-ContentVersion | 1.88.244-r17036752 |
| X-EpicGames-MinBuild | 17036752 |
| X-EpicGames-Profile-Revision | 6367 |
| X-Epic-Device-ID | 68009daed09498667a8039cce09983ed |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-1154642548C092033C1B6F950A4EB35B-A2FA7D094E828552652F2ABE26A27C0E |
| Connection | keep-alive |


### Response Body

```json
{
  "profileRevision": 6369,
  "profileId": "monsterpit",
  "profileChangesBaseRevision": 6367,
  "profileChanges": [
    {
      "changeType": "itemRemoved",
      "itemId": "6d213240-1b55-4862-9fc1-021ef1f21f2c"
    }
  ],
  "profileCommandRevision": 1072,
  "serverTime": "2022-12-27T06:57:54.464Z",
  "multiUpdate": [
    {
      "profileRevision": 39824,
      "profileId": "profile0",
      "profileChangesBaseRevision": 39822,
      "profileChanges": [
        {
          "changeType": "itemQuantityChanged",
          "itemId": "c384fe1c-cf33-48ab-868e-56125c6f9b88",
          "quantity": 43858
        },
        {
          "changeType": "itemAdded",
          "itemId": "6d213240-1b55-4862-9fc1-021ef1f21f2c",
          "item": {
            "templateId": "Character:Cleric_C1_Light_Pixie_T01",
            "attributes": {
              "gear_weapon_item_id": "",
              "weapon_unlocked": false,
              "sidekick_template_id": "",
              "level": 120,
              "is_new": false,
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
      "profileCommandRevision": 23687
    }
  ],
  "responseVersion": 1
}
```

*Response body was encoded in base64*

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
