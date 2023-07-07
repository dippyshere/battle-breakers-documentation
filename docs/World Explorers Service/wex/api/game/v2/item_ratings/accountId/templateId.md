# Item Rating

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/item_ratings/:accountId/:templateId*

___

## Request

```http
GET /wex/api/game/v2/item_ratings/:accountId/:templateId HTTP/1.1
```

### Path Parameters

| Name       | Value                                        |
|------------|----------------------------------------------|
| acountId   | ec0ebb7e56f6454e86c62299a7b32e21             |
| templateId | Character:Ninja_VR1_Light_CrystalDaggers_T05 |

### Request Headers

| Name                  | Value                                                                                                                 |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------|
| Host                  | wex-public-service-live-prod.ol.epicgames.com                                                                         |
| Accept                | \*/\*                                                                                                                 |
| Accept-Encoding       | deflate, gzip                                                                                                         |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-BF5B64544412777DD4C71C8545BEAE11-A6A9D5984661D1CE314A8E811AE0BB01                |
| User-Agent            | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit                                                      |
| Authorization         | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |
| Content-Length        | 0                                                                                                                     |

___

## Response

#### Status: 200 OK

### Response Headers

| Name                       | Value                                                                                                  |
|----------------------------|--------------------------------------------------------------------------------------------------------|
| Date                       | Wed, 28 Dec 2022 11:38:59 GMT                                                                          |
| Content-Type               | application/json                                                                                       |
| Content-Length             | 367                                                                                                    |
| X-EpicGames-McpVersion     | prod Release-1.88-1.88 build 107 cl 19310354                                                           |
| X-EpicGames-ContentVersion | 1.88.244-r17036752                                                                                     |
| X-EpicGames-MinBuild       | 17036752                                                                                               |
| X-Epic-Device-ID           | 68009daed09498667a8039cce09983ed                                                                       |
| X-Epic-Correlation-ID      | UE4-2f4c92e44a8a8420a867089329526852-BF5B64544412777DD4C71C8545BEAE11-A6A9D5984661D1CE314A8E811AE0BB01 |
| Connection                 | keep-alive                                                                                             |

### Response Body

```json
{
  "myRating": {
    "gameplayRating": 5,
    "appearanceRating": 4
  },
  "overallRatings": {
    "ratingsKey": "CD.Ninja.VR1.Light.CrystalDaggers.T03",
    "discussUrl": "",
    "ratings": [
      {
        "gameplayRating": 3,
        "appearanceRating": 2
      },
      {
        "gameplayRating": 1,
        "appearanceRating": 1
      },
      {
        "gameplayRating": 3,
        "appearanceRating": 3
      },
      {
        "gameplayRating": 10,
        "appearanceRating": 8
      },
      {
        "gameplayRating": 83,
        "appearanceRating": 87
      }
    ]
  }
}
```

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
