# Cash Out Workshop

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/:accountId/CashOutWorkshop?profileId=profile0&rvn=40353*

___

## Request

```http
POST /wex/api/game/v2/profile/:accountId/CashOutWorkshop?profileId=profile0&rvn=40353 HTTP/1.1
```

### Path Parameters

| Name     | Value                             |
|----------|-----------------------------------|
| acountId | ec0ebb7e56f6454e86c62299a7b32e21  |

### Query String

| Name      | Value    |
|-----------|----------|
| profileId | profile0 |
| rvn       | 40353    |

### Request Headers

| Name                         | Value                                                                                                                                                                                                                                                                              |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Host                         | wex-public-service-live-prod.ol.epicgames.com                                                                                                                                                                                                                                      |
| Accept-Encoding              | deflate, gzip                                                                                                                                                                                                                                                                      |
| Accept                       | \*/\*                                                                                                                                                                                                                                                                              |
| Content-Type                 | application/json                                                                                                                                                                                                                                                                   |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":24043},{"profileId":"levels","clientCommandRevision":14476},{"profileId":"friends","clientCommandRevision":8263},{"profileId":"monsterpit","clientCommandRevision":1081},{"profileId":"multiplayer","clientCommandRevision":900}] |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-AD48DDB740D06C50E3886F8DB45B2561                                                                                                                                                                             |
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
| Date                         | Thu, 29 Dec 2022 05:45:28 GMT                                                                          |
| Content-Type                 | application/json                                                                                       |
| Content-Length               | 567                                                                                                    |
| X-EpicGames-McpVersion       | prod Release-1.88-1.88 build 107 cl 19310354                                                           |
| X-EpicGames-ContentVersion   | 1.88.244-r17036752                                                                                     |
| X-EpicGames-MinBuild         | 17036752                                                                                               |
| X-EpicGames-Profile-Revision | 40353                                                                                                  |
| X-Epic-Device-ID             | 68009daed09498667a8039cce09983ed                                                                       |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-AD48DDB740D06C50E3886F8DB45B2561 |
| Connection                   | keep-alive                                                                                             |

### Response Body

```json
{
  "profileRevision": 40355,
  "profileId": "profile0",
  "profileChangesBaseRevision": 40353,
  "profileChanges": [
    {
      "changeType": "statModified",
      "name": "labor_force",
      "value": {
        "lastInterval": "2022-12-29T00:00:00.000Z",
        "laborUsed": 936
      }
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "daa87593-4b4a-4ffa-a21d-8979d6eb38ed",
      "quantity": 564819337
    }
  ],
  "profileCommandRevision": 24044,
  "serverTime": "2022-12-29T05:45:28.729Z",
  "multiUpdate": [
    {
      "profileRevision": 29639,
      "profileId": "levels",
      "profileChangesBaseRevision": 29637,
      "profileChanges": [],
      "profileCommandRevision": 14476
    }
  ],
  "responseVersion": 1
}
```

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
