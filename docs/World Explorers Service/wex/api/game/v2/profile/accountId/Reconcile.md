# Reconcile

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/:accountId/Reconcile?profileId=friends&rvn=9896*

___

## Request

```http
POST /wex/api/game/v2/profile/:accountId/Reconcile?profileId=friends&rvn=9896 HTTP/1.1
```

### Path Parameters

| Name     | Value                             |
|----------|-----------------------------------|
| acountId | ec0ebb7e56f6454e86c62299a7b32e21  |

### Query String

| Name      | Value   |
|-----------|---------|
| profileId | friends |
| rvn       | 9896    |

### Request Headers

| Name                         | Value                                                                                                                                                                                                                                                                              |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Host                         | wex-public-service-live-prod.ol.epicgames.com                                                                                                                                                                                                                                      |
| Accept-Encoding              | deflate, gzip                                                                                                                                                                                                                                                                      |
| Accept                       | \*/\*                                                                                                                                                                                                                                                                              |
| Content-Type                 | application/json                                                                                                                                                                                                                                                                   |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":24190},{"profileId":"levels","clientCommandRevision":14480},{"profileId":"friends","clientCommandRevision":8264},{"profileId":"monsterpit","clientCommandRevision":1081},{"profileId":"multiplayer","clientCommandRevision":900}] |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-94801B3043BE6683A17343909730CE9C                                                                                                                                                                             |
| User-Agent                   | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit                                                                                                                                                                                                                   |
| Authorization                | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md)                                                                                                                                                              |
| Content-Length               | 10176                                                                                                                                                                                                                                                                              |

### Request Body

```json
{
  "friendIdList": [
    "15512b25e6c44acaa5b3f993d93e257b",
    "e5434d7005d54ed18ae726f91f6c2ccb",
    "c2a0f61cd40941ff9e3aec3f2754184b"
  ],
  "outgoingIdList": [],
  "incomingIdList": []
}
```

___

## Response

#### Status: 200 OK

### Response Headers

| Name                         | Value                                                                                                  |
|------------------------------|--------------------------------------------------------------------------------------------------------|
| Date                         | Thu, 29 Dec 2022 06:08:07 GMT                                                                          |
| Content-Type                 | application/json                                                                                       |
| Transfer-Encoding            | chunked                                                                                                |
| X-EpicGames-McpVersion       | prod Release-1.88-1.88 build 107 cl 19310354                                                           |
| X-EpicGames-ContentVersion   | 1.88.244-r17036752                                                                                     |
| X-EpicGames-MinBuild         | 17036752                                                                                               |
| X-EpicGames-Profile-Revision | 9896                                                                                                   |
| X-Epic-Device-ID             | 68009daed09498667a8039cce09983ed                                                                       |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-94801B3043BE6683A17343909730CE9C |
| Connection                   | keep-alive                                                                                             |

### Response Body

```json
{
  "profileRevision": 9896,
  "profileId": "friends",
  "profileChangesBaseRevision": 9896,
  "profileChanges": [],
  "notifications": [
    {
      "type": "WExpReconcileNotification",
      "primary": true,
      "results": {
        "15512b25e6c44acaa5b3f993d93e257b": true,
        "e5434d7005d54ed18ae726f91f6c2ccb": false,
        "c2a0f61cd40941ff9e3aec3f2754184b": true
      }
    }
  ],
  "profileCommandRevision": 8264,
  "serverTime": "2022-12-29T06:08:07.244Z",
  "responseVersion": 1
}
```

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
