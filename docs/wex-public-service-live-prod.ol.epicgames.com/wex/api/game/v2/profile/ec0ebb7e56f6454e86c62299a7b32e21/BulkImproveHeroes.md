# BulkImproveHeroes

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/BulkImproveHeroes?profileId=profile0&rvn=39917*

___

## Request

```http request
POST /wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/BulkImproveHeroes?profileId=profile0&rvn=39917 HTTP/1.1
```

### Query String

| Name | Value |
|---|---|
| profileId | profile0 |
| rvn | 39917 |




### Request Headers

| Name | Value |
|---|---|
| Host | wex-public-service-live-prod.ol.epicgames.com |
| Accept-Encoding | deflate, gzip |
| Accept | \*/\* |
| Content-Type | application/json |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":23772},{"profileId":"levels","clientCommandRevision":14329},{"profileId":"friends","clientCommandRevision":8247},{"profileId":"monsterpit","clientCommandRevision":1074},{"profileId":"multiplayer","clientCommandRevision":847}] |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-BF5B64544412777DD4C71C8545BEAE11-AD0AC0934CE3D3A07440A1B526242243 |
| User-Agent | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit |
| Authorization | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |
| Content-Length | 238 |


### Request Body

```json
{
  "detail": [
    {
      "heroItemId": "dab75d65-7911-4f7b-8cc9-88790171650d",
      "potionItems": [],
      "weaponUpgrades": [
        {
          "upgradeType": "WeaponLevel",
          "numUpgrades": 8
        }
      ],
      "numLevelUps": 0
    }
  ]
}
```

___

## Response

#### Status: 200 OK




### Response Headers

| Name | Value |
|---|---|
| Date | Wed, 28 Dec 2022 11:46:30 GMT |
| Content-Type | application/json |
| Content-Length | 1146 |
| X-EpicGames-Profile-Revision | 39917 |
| X-EpicGames-McpVersion | prod Release-1.88-1.88 build 107 cl 19310354 |
| X-EpicGames-ContentVersion | 1.88.244-r17036752 |
| X-EpicGames-MinBuild | 17036752 |
| X-Epic-Device-ID | 68009daed09498667a8039cce09983ed |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-BF5B64544412777DD4C71C8545BEAE11-AD0AC0934CE3D3A07440A1B526242243 |
| Connection | keep-alive |


### Response Body

```json
{
  "profileRevision": 39918,
  "profileId": "profile0",
  "profileChangesBaseRevision": 39917,
  "profileChanges": [
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 638
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 539
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 440
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "d389af5b-d01b-4779-9319-40d93ec3f11d",
      "quantity": 2808
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 341
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 242
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 143
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 44
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "dab75d65-7911-4f7b-8cc9-88790171650d",
      "attributeName": "upgrades",
      "attributeValue": [
        95,
        95,
        95,
        95,
        34,
        129,
        5,
        55,
        3
      ]
    }
  ],
  "profileCommandRevision": 23773,
  "serverTime": "2022-12-28T11:46:30.268Z",
  "responseVersion": 1
}
```

*Response body was encoded in base64*

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
