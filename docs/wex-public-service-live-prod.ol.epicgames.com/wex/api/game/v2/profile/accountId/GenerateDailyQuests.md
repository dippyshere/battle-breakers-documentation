# Generate Daily Quests

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/:accountId/GenerateDailyQuests?profileId=profile0&rvn=40313*

___

## Request

```http
POST /wex/api/game/v2/profile/:accountId/GenerateDailyQuests?profileId=profile0&rvn=40313 HTTP/1.1
```

### Path Parameters

| Name     | Value                             |
|----------|-----------------------------------|
| acountId | ec0ebb7e56f6454e86c62299a7b32e21  |

### Query String

| Name      | Value    |
|-----------|----------|
| profileId | profile0 |
| rvn       | 40313    |

### Request Headers

| Name                         | Value                                                                                                                                                                                                                                                                              |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Host                         | wex-public-service-live-prod.ol.epicgames.com                                                                                                                                                                                                                                      |
| Accept-Encoding              | deflate, gzip                                                                                                                                                                                                                                                                      |
| Accept                       | \*/\*                                                                                                                                                                                                                                                                              |
| Content-Type                 | application/json                                                                                                                                                                                                                                                                   |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":24005},{"profileId":"levels","clientCommandRevision":14476},{"profileId":"friends","clientCommandRevision":8261},{"profileId":"monsterpit","clientCommandRevision":1081},{"profileId":"multiplayer","clientCommandRevision":900}] |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-C2E117824B3D28799C5B27B246A65437                                                                                                                                                                             |
| User-Agent                   | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit                                                                                                                                                                                                                   |
| Authorization                | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md)                                                                                                                                                              |
| Content-Length               | 4                                                                                                                                                                                                                                                                                  |

### Request Body

```json
{}
```

___

## Response

#### Status: 200 OK

### Response Headers

| Name                         | Value                                                                                                  |
|------------------------------|--------------------------------------------------------------------------------------------------------|
| Date                         | Thu, 29 Dec 2022 05:43:19 GMT                                                                          |
| Content-Type                 | application/json                                                                                       |
| Content-Length               | 1133                                                                                                   |
| X-EpicGames-McpVersion       | prod Release-1.88-1.88 build 107 cl 19310354                                                           |
| X-EpicGames-ContentVersion   | 1.88.244-r17036752                                                                                     |
| X-EpicGames-MinBuild         | 17036752                                                                                               |
| X-EpicGames-Profile-Revision | 40313                                                                                                  |
| X-Epic-Device-ID             | 68009daed09498667a8039cce09983ed                                                                       |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-C2E117824B3D28799C5B27B246A65437 |
| Connection                   | keep-alive                                                                                             |

### Response Body

```json
{
  "profileRevision": 40314,
  "profileId": "profile0",
  "profileChangesBaseRevision": 40313,
  "profileChanges": [
    {
      "changeType": "itemAdded",
      "itemId": "a2bce9c2-fd38-44eb-a830-b270b5743a03",
      "item": {
        "templateId": "Quest:DefeatBosses2",
        "attributes": {
          "score": 0,
          "requirements": {
            "type": "Basic",
            "required": 16
          },
          "bIsCompleted": false,
          "questObjective": "DefeatBosses",
          "rewards": [
            {
              "templateId": "Currency:Hammer",
              "quantity": 1
            },
            {
              "templateId": "StandIn:AccountXp",
              "quantity": 63354
            }
          ]
        },
        "quantity": 1
      }
    },
    {
      "changeType": "itemAdded",
      "itemId": "2866efb0-7f20-463d-9b24-0bf2d437b9b9",
      "item": {
        "templateId": "Quest:DefeatEnemies2",
        "attributes": {
          "score": 0,
          "requirements": {
            "type": "Basic",
            "required": 360
          },
          "bIsCompleted": false,
          "questObjective": "DefeatEnemies",
          "rewards": [
            {
              "templateId": "Currency:Hammer",
              "quantity": 2
            },
            {
              "templateId": "StandIn:AccountXp",
              "quantity": 63354
            }
          ]
        },
        "quantity": 1
      }
    },
    {
      "changeType": "statModified",
      "name": "daily_quest_last_refresh",
      "value": "2022-12-29T05:43:19.931Z"
    }
  ],
  "notifications": [
    {
      "type": "WExpGiftPointReward",
      "primary": true,
      "totalPoints": 0,
      "lootResult": {
        "items": []
      }
    }
  ],
  "profileCommandRevision": 24006,
  "serverTime": "2022-12-29T05:43:19.934Z",
  "responseVersion": 1
}
```

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
