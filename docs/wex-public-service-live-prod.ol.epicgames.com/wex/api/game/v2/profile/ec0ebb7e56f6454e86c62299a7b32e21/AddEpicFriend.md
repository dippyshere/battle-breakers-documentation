# AddEpicFriend

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/AddEpicFriend?profileId=friends&rvn=9894*



___

## Request

```http request
POST /wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/AddEpicFriend?profileId=friends&rvn=9894 HTTP/1.1
```

### Query String

| Name | Value |
|---|---|
| profileId | friends |
| rvn | 9894 |




### Request Headers

| Name | Value |
|---|---|
| Host | wex-public-service-live-prod.ol.epicgames.com |
| Accept-Encoding | deflate, gzip |
| Accept | \*/\* |
| Content-Type | application/json |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":24008},{"profileId":"levels","clientCommandRevision":14476},{"profileId":"friends","clientCommandRevision":8262},{"profileId":"monsterpit","clientCommandRevision":1081},{"profileId":"multiplayer","clientCommandRevision":900}] |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-F3D9427349594725F517EF85DC3110D7 |
| User-Agent | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit |
| Authorization | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |
| Content-Length | 60 |


### Request Body

```json
{
  "friendAccountId": "47c782fa8b0144afb42e0f8d2f6ca41a"
}
```

___

## Response

#### Status: 200 OK




### Response Headers

| Name | Value |
|---|---|
| Date | Thu, 29 Dec 2022 05:43:42 GMT |
| Content-Type | application/json |
| Content-Length | 1473 |
| X-EpicGames-McpVersion | prod Release-1.88-1.88 build 107 cl 19310354 |
| X-EpicGames-ContentVersion | 1.88.244-r17036752 |
| X-EpicGames-MinBuild | 17036752 |
| X-EpicGames-Profile-Revision | 9894 |
| X-Epic-Device-ID | 68009daed09498667a8039cce09983ed |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-F3D9427349594725F517EF85DC3110D7 |
| Connection | keep-alive |


### Response Body

```json
{
  "profileRevision": 9895,
  "profileId": "friends",
  "profileChangesBaseRevision": 9894,
  "profileChanges": [
    {
      "changeType": "itemAdded",
      "itemId": "5bc8605d-0a90-4d08-b54f-06d79ab3d387",
      "item": {
        "templateId": "Friend:Instance",
        "attributes": {
          "lifetime_claimed": 0,
          "accountId": "47c782fa8b0144afb42e0f8d2f6ca41a",
          "canBeSparred": false,
          "snapshot_expires": "2022-12-29T08:43:42.688Z",
          "best_gift": 0,
          "lifetime_gifted": 0,
          "remoteFriendId": "f3e94437-6bce-4115-bf96-1309dbae6dbd",
          "snapshot": {
            "displayName": "Jenks73-",
            "avatarUrl": "wex-temp-avatar.png",
            "repHeroes": [
              {
                "itemId": "b8664898-3960-44ea-91ea-129a62301aa8",
                "templateId": "Character:DragonKnight_SR1_Water_DragonForm_T06",
                "bIsCommander": true,
                "level": 150,
                "skillLevel": 20,
                "upgrades": [
                  95,
                  95,
                  95,
                  95,
                  34,
                  150,
                  6,
                  125,
                  5
                ],
                "accountInfo": {
                  "level": 687,
                  "perks": [
                    12,
                    246,
                    284,
                    243,
                    14,
                    163,
                    27,
                    27
                  ]
                },
                "foilLevel": 1,
                "gearTemplateId": "Character:DragonKnight_SR1_Water_JumpStrike_T06"
              },
              {
                "itemId": "40cc06b8-bd44-46e0-ad79-4217d2e4ffc1",
                "templateId": "Character:Ninja_VR1_Light_CrystalDaggers_T06",
                "bIsCommander": true,
                "level": 150,
                "skillLevel": 20,
                "upgrades": [
                  95,
                  95,
                  95,
                  95,
                  34,
                  150,
                  6,
                  125,
                  5
                ],
                "accountInfo": {
                  "level": 687,
                  "perks": [
                    12,
                    246,
                    284,
                    243,
                    14,
                    163,
                    27,
                    27
                  ]
                },
                "foilLevel": 1,
                "gearTemplateId": ""
              }
            ],
            "lastPlayTime": "2022-12-29T05:39:01.003Z",
            "numLevelsCompleted": 996,
            "numTerritoriesClaimed": 84,
            "accountLevel": 687,
            "numRepHeroes": 2,
            "isPvPUnlocked": true
          },
          "status": "EpicFriend",
          "gifts": {}
        },
        "quantity": 1
      }
    }
  ],
  "profileCommandRevision": 8263,
  "serverTime": "2022-12-29T05:43:42.692Z",
  "responseVersion": 1
}
```

*Response body was encoded in base64*

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
