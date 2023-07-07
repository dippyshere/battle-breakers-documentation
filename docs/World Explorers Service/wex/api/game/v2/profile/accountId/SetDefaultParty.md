# Set Default Party

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/:accountId/SetDefaultParty?profileId=profile0&rvn=40454*

___

## Request

```http
POST /wex/api/game/v2/profile/:accountId/SetDefaultParty?profileId=profile0&rvn=40454 HTTP/1.1
```

### Path Parameters

| Name     | Value                             |
|----------|-----------------------------------|
| acountId | ec0ebb7e56f6454e86c62299a7b32e21  |

### Query String

| Name      | Value    |
|-----------|----------|
| profileId | profile0 |
| rvn       | 40454    |

### Request Headers

| Name                         | Value                                                                                                                                                                                                                                                                              |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Host                         | wex-public-service-live-prod.ol.epicgames.com                                                                                                                                                                                                                                      |
| Accept-Encoding              | deflate, gzip                                                                                                                                                                                                                                                                      |
| Accept                       | \*/\*                                                                                                                                                                                                                                                                              |
| Content-Type                 | application/json                                                                                                                                                                                                                                                                   |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":24141},{"profileId":"levels","clientCommandRevision":14478},{"profileId":"friends","clientCommandRevision":8264},{"profileId":"monsterpit","clientCommandRevision":1081},{"profileId":"multiplayer","clientCommandRevision":900}] |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-3DCE6A3847C4B8CE865202976E4FE5E3                                                                                                                                                                             |
| User-Agent                   | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit                                                                                                                                                                                                                   |
| Authorization                | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md)                                                                                                                                                              |
| Content-Length               | 77                                                                                                                                                                                                                                                                                 |

### Request Body

```json
{
  "partyId": "4edcc770-73c0-4c75-b07a-3f2600e3f765",
  "type": "PveFire"
}
```

___

## Response

#### Status: 200 OK

### Response Headers

| Name                         | Value                                                                                                  |
|------------------------------|--------------------------------------------------------------------------------------------------------|
| Date                         | Thu, 29 Dec 2022 05:54:05 GMT                                                                          |
| Content-Type                 | application/json                                                                                       |
| Content-Length               | 565                                                                                                    |
| X-EpicGames-Profile-Revision | 40454                                                                                                  |
| X-EpicGames-McpVersion       | prod Release-1.88-1.88 build 107 cl 19310354                                                           |
| X-EpicGames-ContentVersion   | 1.88.244-r17036752                                                                                     |
| X-EpicGames-MinBuild         | 17036752                                                                                               |
| X-Epic-Device-ID             | 68009daed09498667a8039cce09983ed                                                                       |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-3DCE6A3847C4B8CE865202976E4FE5E3 |
| Connection                   | keep-alive                                                                                             |

### Response Body

```json
{
  "profileRevision": 40455,
  "profileId": "profile0",
  "profileChangesBaseRevision": 40454,
  "profileChanges": [
    {
      "changeType": "statModified",
      "name": "default_parties",
      "value": {
        "PveLight": "5d951c35-442e-4e52-b614-02973632398d",
        "LastPvePartyUsed": "4edcc770-73c0-4c75-b07a-3f2600e3f765",
        "PveFire": "4edcc770-73c0-4c75-b07a-3f2600e3f765",
        "PveDark": "5d951c35-442e-4e52-b614-02973632398d",
        "PveNature": "5d951c35-442e-4e52-b614-02973632398d",
        "PveWater": "5d951c35-442e-4e52-b614-02973632398d"
      }
    }
  ],
  "profileCommandRevision": 24142,
  "serverTime": "2022-12-29T05:54:05.440Z",
  "responseVersion": 1
}
```

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
