# Select Hammer Chest

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/:accountId/SelectHammerChest?profileId=profile0&rvn=40451*

___

## Request

```http
POST /wex/api/game/v2/profile/:accountId/SelectHammerChest?profileId=profile0&rvn=40451 HTTP/1.1
```

### Path Parameters

| Name     | Value                             |
|----------|-----------------------------------|
| acountId | ec0ebb7e56f6454e86c62299a7b32e21  |

### Query String

| Name      | Value    |
|-----------|----------|
| profileId | profile0 |
| rvn       | 40451    |

### Request Headers

| Name                         | Value                                                                                                                                                                                                                                                                              |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Host                         | wex-public-service-live-prod.ol.epicgames.com                                                                                                                                                                                                                                      |
| Accept-Encoding              | deflate, gzip                                                                                                                                                                                                                                                                      |
| Accept                       | \*/\*                                                                                                                                                                                                                                                                              |
| Content-Type                 | application/json                                                                                                                                                                                                                                                                   |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":24138},{"profileId":"levels","clientCommandRevision":14478},{"profileId":"friends","clientCommandRevision":8264},{"profileId":"monsterpit","clientCommandRevision":1081},{"profileId":"multiplayer","clientCommandRevision":900}] |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-223C3D6D4299B088186FEE8AEC4C8F15                                                                                                                                                                             |
| User-Agent                   | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit                                                                                                                                                                                                                   |
| Authorization                | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md)                                                                                                                                                              |
| Content-Length               | 56                                                                                                                                                                                                                                                                                 |

### Request Body

```json
{
  "chestId": "128a407b-f755-42f1-9370-4f6e3beec0b7"
}
```

___

## Response

#### Status: 200 OK

### Response Headers

| Name                         | Value                                                                                                  |
|------------------------------|--------------------------------------------------------------------------------------------------------|
| Date                         | Thu, 29 Dec 2022 05:53:28 GMT                                                                          |
| Content-Type                 | application/json                                                                                       |
| Content-Length               | 453                                                                                                    |
| X-EpicGames-McpVersion       | prod Release-1.88-1.88 build 107 cl 19310354                                                           |
| X-EpicGames-ContentVersion   | 1.88.244-r17036752                                                                                     |
| X-EpicGames-MinBuild         | 17036752                                                                                               |
| X-EpicGames-Profile-Revision | 40451                                                                                                  |
| X-Epic-Device-ID             | 68009daed09498667a8039cce09983ed                                                                       |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-223C3D6D4299B088186FEE8AEC4C8F15 |
| Connection                   | keep-alive                                                                                             |

### Response Body

```json
{
  "profileRevision": 40452,
  "profileId": "profile0",
  "profileChangesBaseRevision": 40451,
  "profileChanges": [
    {
      "changeType": "statModified",
      "name": "active_hammer_chest",
      "value": "128a407b-f755-42f1-9370-4f6e3beec0b7"
    },
    {
      "changeType": "itemRemoved",
      "itemId": "360886d1-7a8d-4fdd-9a95-34b5303a5bb7"
    },
    {
      "changeType": "itemRemoved",
      "itemId": "542a5a1c-005b-413e-9f2d-326c31d70367"
    }
  ],
  "profileCommandRevision": 24139,
  "serverTime": "2022-12-29T05:53:28.960Z",
  "responseVersion": 1
}
```

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
