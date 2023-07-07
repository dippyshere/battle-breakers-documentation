# Unlock Region

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/:accountId/UnlockRegion?profileId=levels&rvn=3*

___

## Request

```http
POST /wex/api/game/v2/profile/:accountId/UnlockRegion?profileId=levels&rvn=3 HTTP/1.1
```

### Query String

| Name | Value |
|---|---|
| profileId | levels |
| rvn | 3 |

### Request Headers

| Name | Value |
|---|---|
| Host | wex-public-service-live-prod.ol.epicgames.com |
| Accept-Encoding | deflate, gzip |
| Accept | \*/\* |
| Content-Type | application/json |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":5},{"profileId":"levels","clientCommandRevision":1},{"profileId":"friends","clientCommandRevision":2},{"profileId":"monsterpit","clientCommandRevision":0},{"profileId":"multiplayer","clientCommandRevision":0}] |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-420FE66A4AACA5058BA3B193D82F56CE-1A7FE73A443A0342C554DAB13E041684 |
| User-Agent | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit |
| Authorization | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |
| Content-Length | 49 |

### Request Body

```json
{
  "regionId": "Region.ForestOfMixedEmotions"
}
```

___

## Response

#### Status: 200 OK

### Response Headers

| Name | Value |
|---|---|
| Date | Tue, 27 Dec 2022 06:01:38 GMT |
| Content-Type | application/json |
| Content-Length | 367 |
| X-EpicGames-Profile-Revision | 3 |
| X-EpicGames-McpVersion | prod Release-1.88-1.88 build 107 cl 19310354 |
| X-EpicGames-ContentVersion | 1.88.244-r17036752 |
| X-EpicGames-MinBuild | 17036752 |
| X-Epic-Device-ID | 68009daed09498667a8039cce09983ed |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-420FE66A4AACA5058BA3B193D82F56CE-1A7FE73A443A0342C554DAB13E041684 |
| Connection | keep-alive |

### Response Body

```json
{
  "profileRevision": 4,
  "profileId": "levels",
  "profileChangesBaseRevision": 3,
  "profileChanges": [
    {
      "changeType": "itemAdded",
      "itemId": "715f1dbb-a8df-478f-b8f2-557b145b1dbd",
      "item": {
        "templateId": "WorldUnlock:Region",
        "attributes": {
          "regionId": "Region.ForestOfMixedEmotions"
        },
        "quantity": 1
      }
    }
  ],
  "profileCommandRevision": 2,
  "serverTime": "2022-12-27T06:01:38.311Z",
  "responseVersion": 1
}
```

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
