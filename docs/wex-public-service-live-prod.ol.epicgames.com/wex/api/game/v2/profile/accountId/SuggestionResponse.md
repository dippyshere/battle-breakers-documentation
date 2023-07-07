# Suggestion Response

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/:accountId/SuggestionResponse?profileId=friends&rvn=21*

___

## Request

```http
POST /wex/api/game/v2/profile/:accountId/SuggestionResponse?profileId=friends&rvn=21 HTTP/1.1
```

### Path Parameters

| Name     | Value                             |
|----------|-----------------------------------|
| acountId | ec0ebb7e56f6454e86c62299a7b32e21  |

### Query String

| Name      | Value   |
|-----------|---------|
| profileId | friends |
| rvn       | 21      |

### Request Headers

| Name                         | Value                                                                                                                                                                                                                                                                   |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Host                         | wex-public-service-live-prod.ol.epicgames.com                                                                                                                                                                                                                           |
| Accept-Encoding              | deflate, gzip                                                                                                                                                                                                                                                           |
| Accept                       | \*/\*                                                                                                                                                                                                                                                                   |
| Content-Type                 | application/json                                                                                                                                                                                                                                                        |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":153},{"profileId":"levels","clientCommandRevision":70},{"profileId":"friends","clientCommandRevision":12},{"profileId":"monsterpit","clientCommandRevision":19},{"profileId":"multiplayer","clientCommandRevision":5}] |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-420FE66A4AACA5058BA3B193D82F56CE-85708C274B808F69EE5558ABAF552296                                                                                                                                                                  |
| User-Agent                   | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit                                                                                                                                                                                                        |
| Authorization                | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md)                                                                                                                                                   |
| Content-Length               | 117                                                                                                                                                                                                                                                                     |

### Request Body

```json
{
  "invitedFriendInstanceIds": [
    "d60b39d7-8e2e-4bef-a7e5-ef890b282b74"
  ],
  "rejectedFriendInstanceIds": []
}
```

___

## Response

#### Status: 200 OK

### Response Headers

| Name                         | Value                                                                                                  |
|------------------------------|--------------------------------------------------------------------------------------------------------|
| Date                         | Tue, 27 Dec 2022 06:28:12 GMT                                                                          |
| Content-Type                 | application/json                                                                                       |
| Content-Length               | 260                                                                                                    |
| X-EpicGames-Profile-Revision | 21                                                                                                     |
| X-EpicGames-McpVersion       | prod Release-1.88-1.88 build 107 cl 19310354                                                           |
| X-EpicGames-ContentVersion   | 1.88.244-r17036752                                                                                     |
| X-EpicGames-MinBuild         | 17036752                                                                                               |
| X-Epic-Device-ID             | 68009daed09498667a8039cce09983ed                                                                       |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-420FE66A4AACA5058BA3B193D82F56CE-85708C274B808F69EE5558ABAF552296 |
| Connection                   | keep-alive                                                                                             |

### Response Body

```json
{
  "profileRevision": 23,
  "profileId": "friends",
  "profileChangesBaseRevision": 21,
  "profileChanges": [
    {
      "changeType": "itemRemoved",
      "itemId": "d60b39d7-8e2e-4bef-a7e5-ef890b282b74"
    }
  ],
  "profileCommandRevision": 13,
  "serverTime": "2022-12-27T06:28:12.816Z",
  "responseVersion": 1
}
```

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
