# Set Rep Hero

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/:accountId/SetRepHero?profileId=profile0&rvn=39278*

___

## Request

```http
POST /wex/api/game/v2/profile/:accountId/SetRepHero?profileId=profile0&rvn=39278 HTTP/1.1
```

### Path Parameters

| Name     | Value                             |
|----------|-----------------------------------|
| acountId | ec0ebb7e56f6454e86c62299a7b32e21  |

### Query String

| Name      | Value    |
|-----------|----------|
| profileId | profile0 |
| rvn       | 39278    |

### Request Headers

| Name                         | Value                                                                                                                                                                                                                                                                              |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Host                         | wex-public-service-live-prod.ol.epicgames.com                                                                                                                                                                                                                                      |
| Accept-Encoding              | deflate, gzip                                                                                                                                                                                                                                                                      |
| Accept                       | \*/\*                                                                                                                                                                                                                                                                              |
| Content-Type                 | application/json                                                                                                                                                                                                                                                                   |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":23271},{"profileId":"levels","clientCommandRevision":14240},{"profileId":"friends","clientCommandRevision":8236},{"profileId":"monsterpit","clientCommandRevision":1038},{"profileId":"multiplayer","clientCommandRevision":835}] |
| X-Epic-Correlation-ID        | UE4-550659054c6fbbba966be789c8ecf002-D77C844B4D0785D0053F3CBFB86C4B7D-B96C5420404ADE4138A4278FA8EBEBF7                                                                                                                                                                             |
| User-Agent                   | WorldExplorers/1.88.244-r17036752 Windows/10.0.25267.1.256.64bit                                                                                                                                                                                                                   |
| Authorization                | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md)                                                                                                                                                              |
| Content-Length               | 71                                                                                                                                                                                                                                                                                 |

### Request Body

```json
{
  "heroId": "6ee61d5c-1c59-4a5b-aae4-347a85ed14c0",
  "slotIdx": 0
}
```

___

## Response

#### Status: 200 OK

### Response Headers

| Name                         | Value                                                                                                  |
|------------------------------|--------------------------------------------------------------------------------------------------------|
| Date                         | Sat, 17 Dec 2022 13:36:42 GMT                                                                          |
| Content-Type                 | application/json                                                                                       |
| Content-Length               | 294                                                                                                    |
| X-EpicGames-Profile-Revision | 39278                                                                                                  |
| X-EpicGames-McpVersion       | prod Release-1.88-1.88 build 107 cl 19310354                                                           |
| X-EpicGames-ContentVersion   | 1.88.244-r17036752                                                                                     |
| X-EpicGames-MinBuild         | 17036752                                                                                               |
| X-Epic-Device-ID             | 7b6449837a601db90694fa85168cb856                                                                       |
| X-Epic-Correlation-ID        | UE4-550659054c6fbbba966be789c8ecf002-D77C844B4D0785D0053F3CBFB86C4B7D-B96C5420404ADE4138A4278FA8EBEBF7 |
| Connection                   | keep-alive                                                                                             |

### Response Body

```json
{
  "profileRevision": 39279,
  "profileId": "profile0",
  "profileChangesBaseRevision": 39278,
  "profileChanges": [
    {
      "changeType": "statModified",
      "name": "rep_hero_ids",
      "value": [
        "6ee61d5c-1c59-4a5b-aae4-347a85ed14c0"
      ]
    }
  ],
  "profileCommandRevision": 23272,
  "serverTime": "2022-12-17T13:36:42.603Z",
  "responseVersion": 1
}
```

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
