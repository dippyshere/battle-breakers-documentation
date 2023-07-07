# Claim Notification Opt In Reward

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/:accountId/ClaimNotificationOptInReward?profileId=profile0&rvn=7*

___

## Request

```http
POST /wex/api/game/v2/profile/:accountId/ClaimNotificationOptInReward?profileId=profile0&rvn=7 HTTP/1.1
```

### Path Parameters

| Name     | Value                             |
|----------|-----------------------------------|
| acountId | ec0ebb7e56f6454e86c62299a7b32e21  |

### Query String

| Name      | Value    |
|-----------|----------|
| profileId | profile0 |
| rvn       | 7        |

### Request Headers

| Name                         | Value                                                                                                                                                                                                                                                              |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Host                         | wex-public-service-live-prod.ol.epicgames.com                                                                                                                                                                                                                      |
| Accept-Encoding              | deflate, gzip                                                                                                                                                                                                                                                      |
| Accept                       | \*/\*                                                                                                                                                                                                                                                              |
| Content-Type                 | application/json                                                                                                                                                                                                                                                   |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":5},{"profileId":"levels","clientCommandRevision":2},{"profileId":"friends","clientCommandRevision":2},{"profileId":"monsterpit","clientCommandRevision":0},{"profileId":"multiplayer","clientCommandRevision":0}] |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-420FE66A4AACA5058BA3B193D82F56CE-3ECAD9F04AE73301F0D5E6AC6C2A9C6B                                                                                                                                                             |
| User-Agent                   | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit                                                                                                                                                                                                   |
| Authorization                | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md)                                                                                                                                              |
| Content-Length               | 4                                                                                                                                                                                                                                                                  |

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
| Date                         | Tue, 27 Dec 2022 06:02:06 GMT                                                                          |
| Content-Type                 | application/json                                                                                       |
| Content-Length               | 471                                                                                                    |
| X-EpicGames-Profile-Revision | 7                                                                                                      |
| X-EpicGames-McpVersion       | prod Release-1.88-1.88 build 107 cl 19310354                                                           |
| X-EpicGames-ContentVersion   | 1.88.244-r17036752                                                                                     |
| X-EpicGames-MinBuild         | 17036752                                                                                               |
| X-Epic-Device-ID             | 68009daed09498667a8039cce09983ed                                                                       |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-420FE66A4AACA5058BA3B193D82F56CE-3ECAD9F04AE73301F0D5E6AC6C2A9C6B |
| Connection                   | keep-alive                                                                                             |

### Response Body

```json
{
  "profileRevision": 8,
  "profileId": "profile0",
  "profileChangesBaseRevision": 7,
  "profileChanges": [
    {
      "changeType": "itemAdded",
      "itemId": "047dac3e-eb0e-4608-8a5e-471722d5bc57",
      "item": {
        "templateId": "Giftbox:GB_NotificationOptInReward",
        "attributes": {
          "sealed_days": 0,
          "params": {},
          "min_level": 1
        },
        "quantity": 1
      }
    },
    {
      "changeType": "statModified",
      "name": "notification_optin_reward_claimed",
      "value": true
    }
  ],
  "profileCommandRevision": 6,
  "serverTime": "2022-12-27T06:02:06.110Z",
  "responseVersion": 1
}
```

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
