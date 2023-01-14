# UpgradeHero

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/UpgradeHero?profileId=profile0&rvn=40522*



___

## Request

```http request
POST /wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/UpgradeHero?profileId=profile0&rvn=40522 HTTP/1.1
```

### Query String

| Name | Value |
|---|---|
| profileId | profile0 |
| rvn | 40522 |




### Request Headers

| Name | Value |
|---|---|
| Host | wex-public-service-live-prod.ol.epicgames.com |
| Accept-Encoding | deflate, gzip |
| Accept | \*/\* |
| Content-Type | application/json |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":24201},{"profileId":"levels","clientCommandRevision":14486},{"profileId":"friends","clientCommandRevision":8264},{"profileId":"monsterpit","clientCommandRevision":1081},{"profileId":"multiplayer","clientCommandRevision":900}] |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-903FCDBD4CCE95EEF47CAC8D0514C3A9 |
| User-Agent | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit |
| Authorization | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |
| Content-Length | 194 |


### Request Body

```json
{
  "heroItemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
  "bIsInPit": false,
  "potionItems": [],
  "weaponUpgrades": [
    {
      "upgradeType": "WeaponLevel",
      "numUpgrades": 86
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
| Date | Thu, 29 Dec 2022 06:09:07 GMT |
| Content-Type | application/json |
| Transfer-Encoding | chunked |
| X-EpicGames-McpVersion | prod Release-1.88-1.88 build 107 cl 19310354 |
| X-EpicGames-ContentVersion | 1.88.244-r17036752 |
| X-EpicGames-MinBuild | 17036752 |
| X-EpicGames-Profile-Revision | 40522 |
| X-Epic-Device-ID | 68009daed09498667a8039cce09983ed |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-903FCDBD4CCE95EEF47CAC8D0514C3A9 |
| Connection | keep-alive |


### Response Body

```json
{
  "profileRevision": 40523,
  "profileId": "profile0",
  "profileChangesBaseRevision": 40522,
  "profileChanges": [
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 3497
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 3487
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 3477
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 3467
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 3457
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 3447
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 3437
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 3427
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 3417
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 3407
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 3397
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 3387
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 3377
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 3367
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 3357
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 3347
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 3337
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 3327
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 3317
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 3307
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 3297
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 3287
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 3277
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 3267
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "d389af5b-d01b-4779-9319-40d93ec3f11d",
      "quantity": 2179
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 3232
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 3197
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 3162
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 3127
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 3092
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 3057
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 3022
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 2987
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 2952
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 2917
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 2882
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 2847
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 2812
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 2777
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 2742
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 2707
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 2672
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 2637
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 2602
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 2567
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 2532
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 2497
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 2462
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 2427
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "d389af5b-d01b-4779-9319-40d93ec3f11d",
      "quantity": 2139
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 2367
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 2307
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 2247
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 2187
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 2127
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 2067
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 2007
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 1947
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 1887
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 1827
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 1767
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 1707
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 1647
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 1587
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 1527
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 1467
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 1407
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 1347
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 1287
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 1227
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 1167
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 1107
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 1047
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 987
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "d389af5b-d01b-4779-9319-40d93ec3f11d",
      "quantity": 2079
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 902
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 817
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 732
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 647
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 562
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 477
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 392
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 307
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 222
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 137
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
      "quantity": 52
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "upgrades",
      "attributeValue": [
        95,
        1,
        95,
        1,
        0,
        86,
        3,
        0,
        0
      ]
    }
  ],
  "profileCommandRevision": 24202,
  "serverTime": "2022-12-29T06:09:07.860Z",
  "responseVersion": 1
}
```

*Response body was encoded in base64*

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
