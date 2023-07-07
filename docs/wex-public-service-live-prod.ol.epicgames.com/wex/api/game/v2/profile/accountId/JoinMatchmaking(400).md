# Join Matchmaking (Inelegible)

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/:accountId/JoinMatchmaking?profileId=multiplayer&rvn=1*

___

## Request

```http
POST /wex/api/game/v2/profile/:accountId/JoinMatchmaking?profileId=multiplayer&rvn=1 HTTP/1.1
```

### Path Parameters

| Name     | Value                             |
|----------|-----------------------------------|
| acountId | ec0ebb7e56f6454e86c62299a7b32e21  |

### Query String

| Name      | Value       |
|-----------|-------------|
| profileId | multiplayer |
| rvn       | 1           |

### Request Headers

| Name                         | Value                                                                                                                                                                                                                                                              |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Host                         | wex-public-service-live-prod.ol.epicgames.com                                                                                                                                                                                                                      |
| Accept-Encoding              | deflate, gzip                                                                                                                                                                                                                                                      |
| Accept                       | \*/\*                                                                                                                                                                                                                                                              |
| Content-Type                 | application/json                                                                                                                                                                                                                                                   |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":4},{"profileId":"levels","clientCommandRevision":1},{"profileId":"friends","clientCommandRevision":2},{"profileId":"monsterpit","clientCommandRevision":0},{"profileId":"multiplayer","clientCommandRevision":0}] |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-420FE66A4AACA5058BA3B193D82F56CE-AC245A2049FA3CE0DB8F4F8D6987E95C                                                                                                                                                             |
| User-Agent                   | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit                                                                                                                                                                                                   |
| Authorization                | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md)                                                                                                                                              |
| Content-Length               | 4                                                                                                                                                                                                                                                                  |

### Request Body

```json
{}
```

___

## Response

#### Status: 400 Bad Request

### Response Headers

| Name                         | Value                                                                                                  |
|------------------------------|--------------------------------------------------------------------------------------------------------|
| Date                         | Tue, 27 Dec 2022 06:01:30 GMT                                                                          |
| Content-Type                 | application/json;charset=UTF-8                                                                         |
| Content-Length               | 207                                                                                                    |
| X-Epic-Error-Code            | 92014                                                                                                  |
| X-Epic-Error-Name            | errors.com.epicgames.world_explorers.bad_request                                                       |
| X-EpicGames-McpVersion       | prod Release-1.88-1.88 build 107 cl 19310354                                                           |
| X-EpicGames-ContentVersion   | 1.88.244-r17036752                                                                                     |
| X-EpicGames-MinBuild         | 17036752                                                                                               |
| X-EpicGames-Profile-Revision | 1                                                                                                      |
| X-Epic-Device-ID             | 68009daed09498667a8039cce09983ed                                                                       |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-420FE66A4AACA5058BA3B193D82F56CE-AC245A2049FA3CE0DB8F4F8D6987E95C |
| Connection                   | keep-alive                                                                                             |

### Response Body

```json
{
  "errorCode": "errors.com.epicgames.world_explorers.bad_request",
  "errorMessage": "Does not meet meet minimum requirememts.",
  "messageVars": [],
  "numericErrorCode": 92014,
  "originatingService": "WEX",
  "intent": "prod"
}
```

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
