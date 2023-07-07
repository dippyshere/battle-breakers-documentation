# UnlockWeaponGear

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/:accountId/UnlockWeaponGear?profileId=profile0&rvn=40523*

___

## Request

```http
POST /wex/api/game/v2/profile/:accountId/UnlockWeaponGear?profileId=profile0&rvn=40523 HTTP/1.1
```

### Path Parameters

| Name     | Value                             |
|----------|-----------------------------------|
| acountId | ec0ebb7e56f6454e86c62299a7b32e21  |

### Query String

| Name      | Value    |
|-----------|----------|
| profileId | profile0 |
| rvn       | 40523    |

### Request Headers

| Name                         | Value                                                                                                                                                                                                                                                                              |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Host                         | wex-public-service-live-prod.ol.epicgames.com                                                                                                                                                                                                                                      |
| Accept-Encoding              | deflate, gzip                                                                                                                                                                                                                                                                      |
| Accept                       | \*/\*                                                                                                                                                                                                                                                                              |
| Content-Type                 | application/json                                                                                                                                                                                                                                                                   |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":24202},{"profileId":"levels","clientCommandRevision":14486},{"profileId":"friends","clientCommandRevision":8264},{"profileId":"monsterpit","clientCommandRevision":1081},{"profileId":"multiplayer","clientCommandRevision":900}] |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-E914FCB448FF7043D6DD33B0B35D8F3F                                                                                                                                                                             |
| User-Agent                   | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit                                                                                                                                                                                                                   |
| Authorization                | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md)                                                                                                                                                              |
| Content-Length               | 59                                                                                                                                                                                                                                                                                 |

### Request Body

```json
{
  "heroItemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d"
}
```

___

## Response

#### Status: 200 OK

### Response Headers

| Name                         | Value                                                                                                  |
|------------------------------|--------------------------------------------------------------------------------------------------------|
| Date                         | Thu, 29 Dec 2022 06:09:10 GMT                                                                          |
| Content-Type                 | application/json                                                                                       |
| Content-Length               | 628                                                                                                    |
| X-EpicGames-McpVersion       | prod Release-1.88-1.88 build 107 cl 19310354                                                           |
| X-EpicGames-ContentVersion   | 1.88.244-r17036752                                                                                     |
| X-EpicGames-MinBuild         | 17036752                                                                                               |
| X-EpicGames-Profile-Revision | 40523                                                                                                  |
| X-Epic-Device-ID             | 68009daed09498667a8039cce09983ed                                                                       |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-E914FCB448FF7043D6DD33B0B35D8F3F |
| Connection                   | keep-alive                                                                                             |

### Response Body

```json
{
  "profileRevision": 40524,
  "profileId": "profile0",
  "profileChangesBaseRevision": 40523,
  "profileChanges": [
    {
      "changeType": "itemQuantityChanged",
      "itemId": "1e403f80-6fc6-4eb5-b1fe-8b5be9066958",
      "quantity": 154
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "710aa558-c165-4e6a-bdda-5baec9a2ed65",
      "quantity": 21
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "034d9087-3678-498b-bb42-5c168b900821",
      "quantity": 18
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "weapon_unlocked",
      "attributeValue": true
    }
  ],
  "profileCommandRevision": 24203,
  "serverTime": "2022-12-29T06:09:10.655Z",
  "responseVersion": 1
}
```

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
