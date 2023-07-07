# Query Profile (Multiplayer)

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/:accountId/QueryProfile?profileId=multiplayer&rvn=-1*

___

## Request

```http
POST /wex/api/game/v2/profile/:accountId/QueryProfile?profileId=multiplayer&rvn=-1 HTTP/1.1
```

### Path Parameters

| Name     | Value                             |
|----------|-----------------------------------|
| acountId | ec0ebb7e56f6454e86c62299a7b32e21  |

### Query String

| Name      | Value       |
|-----------|-------------|
| profileId | multiplayer |
| rvn       | -1          |

### Request Headers

| Name                         | Value                                                                                                                                                                                                                                                                   |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Host                         | wex-public-service-live-prod.ol.epicgames.com                                                                                                                                                                                                                           |
| Accept-Encoding              | deflate, gzip                                                                                                                                                                                                                                                           |
| Accept                       | \*/\*                                                                                                                                                                                                                                                                   |
| Content-Type                 | application/json                                                                                                                                                                                                                                                        |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":-1},{"profileId":"levels","clientCommandRevision":-1},{"profileId":"friends","clientCommandRevision":-1},{"profileId":"monsterpit","clientCommandRevision":-1},{"profileId":"multiplayer","clientCommandRevision":-1}] |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-0B7F237845879274156B60BDF32E84BB                                                                                                                                                                  |
| User-Agent                   | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit                                                                                                                                                                                                        |
| Authorization                | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md)                                                                                                                                                   |
| Content-Length               | 4                                                                                                                                                                                                                                                                       |

### Request Body

```json
{
  "profileRevision": 1,
  "profileId": "multiplayer",
  "profileChangesBaseRevision": 1,
  "profileChanges": [
    {
      "changeType": "fullProfileUpdate",
      "profile": {
        "_id": "14e9a5dd69be48d9a96fb49e440440b3",
        "created": "2022-12-24T00:43:34.604Z",
        "updated": "2022-12-24T00:43:34.604Z",
        "rvn": 1,
        "wipeNumber": 5,
        "accountId": "d330e65d299748e9ad8c06a4a1fc3d85",
        "profileId": "multiplayer",
        "version": "initial",
        "items": {
          "ae5869cd-ace5-4572-bb4f-b21b5d52072d": {
            "templateId": "MultiplayerMode:PvpDuel",
            "attributes": {
              "lifetime_wins": 0,
              "current_enemies_defeated": 0,
              "defense_rating": 0,
              "current_losses": 0,
              "attack_rating": 0,
              "match_roster": [],
              "lifetime_enemies_defeated": 0,
              "recent_matches": [],
              "pvp_match_count": 0,
              "match_refresh": {},
              "current_wins": 0,
              "recent_opponents": [],
              "lifetime_losses": 0
            },
            "quantity": 1
          }
        },
        "stats": {
          "attributes": {
            "daily_pvp_wins": 0,
            "last_refresh": "0021-12-01T21:12:00.000Z",
            "current_pvp_win_date": "0021-12-01T21:12:00.000Z",
            "pvp_taunt": "",
            "default_parties": {},
            "matchmaking_id": "",
            "daily_pvp_reward_limit": 25
          }
        },
        "commandRevision": 0
      }
    }
  ],
  "profileCommandRevision": 0,
  "serverTime": "2022-12-24T00:50:48.859Z",
  "responseVersion": 1
}
```

___

## Response

#### Status: 200 OK

### Response Headers

| Name                         | Value                                                                                                  |
|------------------------------|--------------------------------------------------------------------------------------------------------|
| Date                         | Thu, 29 Dec 2022 05:43:02 GMT                                                                          |
| Content-Type                 | application/json                                                                                       |
| Transfer-Encoding            | chunked                                                                                                |
| X-EpicGames-Profile-Revision | 1884                                                                                                   |
| X-EpicGames-McpVersion       | prod Release-1.88-1.88 build 107 cl 19310354                                                           |
| X-EpicGames-ContentVersion   | 1.88.244-r17036752                                                                                     |
| X-EpicGames-MinBuild         | 17036752                                                                                               |
| X-Epic-Device-ID             | 68009daed09498667a8039cce09983ed                                                                       |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-0B7F237845879274156B60BDF32E84BB |
| Connection                   | keep-alive                                                                                             |

### Response Body

```json

```

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
