# Update Party

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/:accountId/UpdateParty?profileId=profile0&rvn=40529*

___

## Request

```http
POST /wex/api/game/v2/profile/:accountId/UpdateParty?profileId=profile0&rvn=40529 HTTP/1.1
```

### Path Parameters

| Name     | Value                             |
|----------|-----------------------------------|
| acountId | ec0ebb7e56f6454e86c62299a7b32e21  |

### Query String

| Name      | Value    |
|-----------|----------|
| profileId | profile0 |
| rvn       | 40529    |

### Request Headers

| Name                         | Value                                                                                                                                                                                                                                                                              |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Host                         | wex-public-service-live-prod.ol.epicgames.com                                                                                                                                                                                                                                      |
| Accept-Encoding              | deflate, gzip                                                                                                                                                                                                                                                                      |
| Accept                       | \*/\*                                                                                                                                                                                                                                                                              |
| Content-Type                 | application/json                                                                                                                                                                                                                                                                   |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":24208},{"profileId":"levels","clientCommandRevision":14486},{"profileId":"friends","clientCommandRevision":8264},{"profileId":"monsterpit","clientCommandRevision":1081},{"profileId":"multiplayer","clientCommandRevision":900}] |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-572152AA40302EB33DBEF2B014047D53                                                                                                                                                                             |
| User-Agent                   | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit                                                                                                                                                                                                                   |
| Authorization                | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md)                                                                                                                                                              |
| Content-Length               | 456                                                                                                                                                                                                                                                                                |

### Request Body

```json
{
  "partyItemId": "4edcc770-73c0-4c75-b07a-3f2600e3f765",
  "partyInstance": {
    "character_ids": [
      "73bc3aeb-a61e-4a87-8c47-93190c8cf727",
      "",
      "dab75d65-7911-4f7b-8cc9-88790171650d",
      "2dbc336a-554b-449c-ae84-b4697bb00119",
      "6f578f8e-2a2c-4eb9-81ab-6f2799202822",
      "f01dfe95-6a2c-4a18-a3d9-19709c5f7de1"
    ],
    "friend_index": 1,
    "commander_index": 0,
    "date_created": "2019.11.13-07.11.54",
    "party_icon": "None"
  }
}
```

___

## Response

#### Status: 200 OK

### Response Headers

| Name                         | Value                                                                                                  |
|------------------------------|--------------------------------------------------------------------------------------------------------|
| Date                         | Thu, 29 Dec 2022 06:09:34 GMT                                                                          |
| Content-Type                 | application/json                                                                                       |
| Content-Length               | 523                                                                                                    |
| X-EpicGames-Profile-Revision | 40529                                                                                                  |
| X-EpicGames-McpVersion       | prod Release-1.88-1.88 build 107 cl 19310354                                                           |
| X-EpicGames-ContentVersion   | 1.88.244-r17036752                                                                                     |
| X-EpicGames-MinBuild         | 17036752                                                                                               |
| X-Epic-Device-ID             | 68009daed09498667a8039cce09983ed                                                                       |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-572152AA40302EB33DBEF2B014047D53 |
| Connection                   | keep-alive                                                                                             |

### Response Body

```json
{
  "profileRevision": 40530,
  "profileId": "profile0",
  "profileChangesBaseRevision": 40529,
  "profileChanges": [
    {
      "changeType": "itemAttrChanged",
      "itemId": "4edcc770-73c0-4c75-b07a-3f2600e3f765",
      "attributeName": "character_ids",
      "attributeValue": [
        "73bc3aeb-a61e-4a87-8c47-93190c8cf727",
        "",
        "dab75d65-7911-4f7b-8cc9-88790171650d",
        "2dbc336a-554b-449c-ae84-b4697bb00119",
        "6f578f8e-2a2c-4eb9-81ab-6f2799202822",
        "f01dfe95-6a2c-4a18-a3d9-19709c5f7de1"
      ]
    }
  ],
  "profileCommandRevision": 24209,
  "serverTime": "2022-12-29T06:09:34.507Z",
  "responseVersion": 1
}
```

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
