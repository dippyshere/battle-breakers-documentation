# SellHero

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/SellHero?profileId=profile0&rvn=39887*

___

## Request

```http request
POST /wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/SellHero?profileId=profile0&rvn=39887 HTTP/1.1
```

### Query String

| Name | Value |
|---|---|
| profileId | profile0 |
| rvn | 39887 |




### Request Headers

| Name | Value |
|---|---|
| Host | wex-public-service-live-prod.ol.epicgames.com |
| Accept-Encoding | deflate, gzip |
| Accept | \*/\* |
| Content-Type | application/json |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":23745},{"profileId":"levels","clientCommandRevision":14327},{"profileId":"friends","clientCommandRevision":8247},{"profileId":"monsterpit","clientCommandRevision":1073},{"profileId":"multiplayer","clientCommandRevision":847}] |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-BF5B64544412777DD4C71C8545BEAE11-29B013B34F84E0E1829BC8A1ED9C5979 |
| User-Agent | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit |
| Authorization | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |
| Content-Length | 80 |


### Request Body

```json
{
  "heroItemId": "e1c95163-4896-4747-8cce-7c8c61e2f96e",
  "bIsInPit": false
}
```

___

## Response

#### Status: 200 OK




### Response Headers

| Name | Value |
|---|---|
| Date | Wed, 28 Dec 2022 11:38:39 GMT |
| Content-Type | application/json |
| Content-Length | 957 |
| X-EpicGames-McpVersion | prod Release-1.88-1.88 build 107 cl 19310354 |
| X-EpicGames-ContentVersion | 1.88.244-r17036752 |
| X-EpicGames-MinBuild | 17036752 |
| X-EpicGames-Profile-Revision | 39887 |
| X-Epic-Device-ID | 68009daed09498667a8039cce09983ed |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-BF5B64544412777DD4C71C8545BEAE11-29B013B34F84E0E1829BC8A1ED9C5979 |
| Connection | keep-alive |


### Response Body

```json
{
  "profileRevision": 39889,
  "profileId": "profile0",
  "profileChangesBaseRevision": 39887,
  "profileChanges": [
    {
      "changeType": "itemRemoved",
      "itemId": "e1c95163-4896-4747-8cce-7c8c61e2f96e"
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "daa87593-4b4a-4ffa-a21d-8979d6eb38ed",
      "quantity": 560831956
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
      "quantity": 13009718
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "1b148e65-99c0-4eb8-a99d-7377f537276e",
      "quantity": 330
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "46366ac8-8b65-4af2-89bd-3dd1d175307b",
      "quantity": 258
    }
  ],
  "profileCommandRevision": 23746,
  "serverTime": "2022-12-28T11:38:39.532Z",
  "multiUpdate": [
    {
      "profileRevision": 6373,
      "profileId": "monsterpit",
      "profileChangesBaseRevision": 6371,
      "profileChanges": [
        {
          "changeType": "itemAttrChanged",
          "itemId": "d0eba98e-18b0-4d0f-96d6-8c8a55a1f2aa",
          "attributeName": "num_sold",
          "attributeValue": 6
        }
      ],
      "profileCommandRevision": 1074
    }
  ],
  "responseVersion": 1
}
```

*Response body was encoded in base64*

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
