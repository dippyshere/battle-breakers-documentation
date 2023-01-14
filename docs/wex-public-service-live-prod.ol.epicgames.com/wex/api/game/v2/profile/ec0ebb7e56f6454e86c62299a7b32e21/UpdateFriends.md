# UpdateFriends

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/UpdateFriends?profileId=friends&rvn=9896*



___

## Request

```http request
POST /wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/UpdateFriends?profileId=friends&rvn=9896 HTTP/1.1
```

### Query String

| Name | Value |
|---|---|
| profileId | friends |
| rvn | 9896 |




### Request Headers

| Name | Value |
|---|---|
| Host | wex-public-service-live-prod.ol.epicgames.com |
| Accept-Encoding | deflate, gzip |
| Accept | \*/\* |
| Content-Type | application/json |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":24190},{"profileId":"levels","clientCommandRevision":14480},{"profileId":"friends","clientCommandRevision":8264},{"profileId":"monsterpit","clientCommandRevision":1081},{"profileId":"multiplayer","clientCommandRevision":900}] |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-5603C774453CFD129D9E13A417B671DE |
| User-Agent | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit |
| Authorization | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |
| Content-Length | 29 |


### Request Body

```json
{
  "friendInstanceId": ""
}
```

___

## Response

#### Status: 200 OK




### Response Headers

| Name | Value |
|---|---|
| Date | Thu, 29 Dec 2022 06:08:07 GMT |
| Content-Type | application/json |
| Content-Length | 190 |
| X-EpicGames-Profile-Revision | 9896 |
| X-EpicGames-McpVersion | prod Release-1.88-1.88 build 107 cl 19310354 |
| X-EpicGames-ContentVersion | 1.88.244-r17036752 |
| X-EpicGames-MinBuild | 17036752 |
| X-Epic-Device-ID | 68009daed09498667a8039cce09983ed |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-5603C774453CFD129D9E13A417B671DE |
| Connection | keep-alive |


### Response Body

```json
{
  "profileRevision": 9896,
  "profileId": "friends",
  "profileChangesBaseRevision": 9896,
  "profileChanges": [],
  "profileCommandRevision": 8264,
  "serverTime": "2022-12-29T06:08:07.664Z",
  "responseVersion": 1
}
```

*Response body was encoded in base64*

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
