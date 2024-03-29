# Catalog Offers

#####

*https://catalog-public-service-prod.ol.epicgames.com/catalog/api/shared/bulk/offers?id=b1c1372c9d0a428bacde8161117b1b2c&id=7d270c7e78d3439db8afe81bcd0b6b6a&id=9d517678254c4b27ab85f0d1d149784b&id=8e60722d2cd54953907351b5a94debc5&id=395a588577834f4089f14440868a3785&id=20621749aaa04a49b28a2e68049470cb&id=760156eb63ad49b68861a5b269b73b48&id=2be4ab85c1ae42bab895be28ab6cb99e&id=1bb845075f334ecaae7b55e421ab3dea&id=11b1aad3c22d4fe58c361b8c913477d6&returnItemDetails=false&country=AU&locale=en*

___

## Request

```http
GET /catalog/api/shared/bulk/offers?id=b1c1372c9d0a428bacde8161117b1b2c&id=7d270c7e78d3439db8afe81bcd0b6b6a&id=9d517678254c4b27ab85f0d1d149784b&id=8e60722d2cd54953907351b5a94debc5&id=395a588577834f4089f14440868a3785&id=20621749aaa04a49b28a2e68049470cb&id=760156eb63ad49b68861a5b269b73b48&id=2be4ab85c1ae42bab895be28ab6cb99e&id=1bb845075f334ecaae7b55e421ab3dea&id=11b1aad3c22d4fe58c361b8c913477d6&returnItemDetails=false&country=AU&locale=en HTTP/1.1
```

### Query String

| Name              | Value                            |
|-------------------|----------------------------------|
| id                | b1c1372c9d0a428bacde8161117b1b2c |
| id                | 7d270c7e78d3439db8afe81bcd0b6b6a |
| id                | 9d517678254c4b27ab85f0d1d149784b |
| id                | 8e60722d2cd54953907351b5a94debc5 |
| id                | 395a588577834f4089f14440868a3785 |
| id                | 20621749aaa04a49b28a2e68049470cb |
| id                | 760156eb63ad49b68861a5b269b73b48 |
| id                | 2be4ab85c1ae42bab895be28ab6cb99e |
| id                | 1bb845075f334ecaae7b55e421ab3dea |
| id                | 11b1aad3c22d4fe58c361b8c913477d6 |
| returnItemDetails | false                            |
| country           | AU                               |
| locale            | en                               |

### Request Headers

| Name                  | Value                                                                                                                 |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------|
| Host                  | catalog-public-service-prod.ol.epicgames.com                                                                          |
| Accept                | \*/\*                                                                                                                 |
| Accept-Encoding       | deflate, gzip                                                                                                         |
| Content-Type          | application/json                                                                                                      |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-2C9A20D3445C02CB961D53A0784930CD                |
| User-Agent            | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit                                                      |
| Authorization         | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |
| Content-Length        | 0                                                                                                                     |

___

## Response

#### Status: 200 OK

### Response Headers

| Name                  | Value                                                                                                  |
|-----------------------|--------------------------------------------------------------------------------------------------------|
| Date                  | Thu, 29 Dec 2022 05:43:11 GMT                                                                          |
| Content-Type          | application/json                                                                                       |
| Transfer-Encoding     | chunked                                                                                                |
| Vary                  | Accept-Encoding                                                                                        |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-2C9A20D3445C02CB961D53A0784930CD |
| Content-Encoding      | gzip                                                                                                   |
| Connection            | keep-alive                                                                                             |

### Response Body

```json
{
  "760156eb63ad49b68861a5b269b73b48": {
    "id": "760156eb63ad49b68861a5b269b73b48",
    "title": "Unwavering Guardian Collection",
    "description": "Rep hero bonuses and more!",
    "longDescription": "Rep hero bonuses and more!",
    "keyImages": [
      {
        "type": "Thumbnail",
        "url": "https://cdn1.epicgames.com/wex/offer/BB_InGame_StoreArt_Collection-512x512-03916083c870df5d62bad565313b36db.jpg",
        "md5": "03916083c870df5d62bad565313b36db",
        "width": 512,
        "height": 512,
        "size": 315373,
        "uploadedDate": "2019-11-12T19:17:21.244Z"
      }
    ],
    "categories": [
      {
        "path": "account_upgrades"
      }
    ],
    "namespace": "wex",
    "status": "SUNSET",
    "creationDate": "2018-07-31T19:34:56.992Z",
    "lastModifiedDate": "2022-12-14T15:55:34.739Z",
    "internalName": "Unwavering Guardian Collection",
    "recurrence": "ONCE",
    "items": [
      {
        "id": "2570dc2fefcf4611a3ab9419f216fed5",
        "keyImages": [],
        "categories": [],
        "namespace": "wex",
        "unsearchable": false
      }
    ],
    "currencyCode": "AUD",
    "currentPrice": 2195,
    "price": 2195,
    "basePrice": 1499,
    "basePriceCurrencyCode": "USD",
    "recurringPrice": 0,
    "freeDays": 0,
    "maxBillingCycles": 0,
    "seller": {
      "id": "o-aa83a0a9bc45e98c80c1b1c9d92e9e",
      "name": "Epic Games"
    },
    "viewableDate": "2019-11-11T17:00:00.000Z",
    "effectiveDate": "2019-11-11T17:00:00.000Z",
    "expiryDate": "2022-12-14T16:00:00.000Z",
    "vatIncluded": true,
    "isCodeRedemptionOnly": false,
    "isFeatured": false,
    "taxSkuId": "FR_Game",
    "merchantGroup": "WEX_MKT",
    "priceTier": "prod-wex_USD_1499",
    "urlSlug": "vip-level-release-04",
    "roleNamesToGrant": [],
    "tags": [],
    "ignoreOrder": false,
    "fulfillToGroup": false,
    "fraudItemType": "RMT_Offer",
    "shareRevenue": false,
    "offerType": "OTHERS",
    "unsearchable": false,
    "releaseOffer": "",
    "title4Sort": "Unwavering Guardian Collection",
    "refundType": "NON_REFUNDABLE",
    "visibilityType": "IS_LISTED",
    "currencyDecimals": 2,
    "allowPurchaseForPartialOwned": true,
    "shareRevenueWithUnderageAffiliates": false,
    "partialItemPrerequisiteCheck": false
  },
  "395a588577834f4089f14440868a3785": {
    "id": "395a588577834f4089f14440868a3785",
    "title": "Underworld Trader Collection",
    "description": "Free secret shop access!",
    "longDescription": "Free secret shop access!",
    "keyImages": [
      {
        "type": "Thumbnail",
        "url": "https://cdn1.epicgames.com/wex/offer/BB_InGame_StoreArt_Collection-512x512-03916083c870df5d62bad565313b36db.jpg",
        "md5": "03916083c870df5d62bad565313b36db",
        "width": 512,
        "height": 512,
        "size": 315373,
        "uploadedDate": "2019-11-12T19:16:41.860Z"
      }
    ],
    "categories": [
      {
        "path": "account_upgrades"
      }
    ],
    "namespace": "wex",
    "status": "SUNSET",
    "creationDate": "2018-07-31T19:28:00.619Z",
    "lastModifiedDate": "2022-12-14T15:55:35.492Z",
    "internalName": "Underworld Trader Collection",
    "recurrence": "ONCE",
    "items": [
      {
        "id": "a01482d5718d42ad8eb51f868b02a555",
        "keyImages": [],
        "categories": [],
        "namespace": "wex",
        "unsearchable": false
      }
    ],
    "currencyCode": "AUD",
    "currentPrice": 2195,
    "price": 2195,
    "basePrice": 1499,
    "basePriceCurrencyCode": "USD",
    "recurringPrice": 0,
    "freeDays": 0,
    "maxBillingCycles": 0,
    "seller": {
      "id": "o-aa83a0a9bc45e98c80c1b1c9d92e9e",
      "name": "Epic Games"
    },
    "viewableDate": "2019-11-11T17:00:00.000Z",
    "effectiveDate": "2019-11-11T17:00:00.000Z",
    "expiryDate": "2022-12-14T16:00:00.000Z",
    "vatIncluded": true,
    "isCodeRedemptionOnly": false,
    "isFeatured": false,
    "taxSkuId": "FR_Game",
    "merchantGroup": "WEX_MKT",
    "priceTier": "prod-wex_USD_1499",
    "urlSlug": "vip-level-release-03",
    "roleNamesToGrant": [],
    "tags": [],
    "ignoreOrder": false,
    "fulfillToGroup": false,
    "fraudItemType": "RMT_Offer",
    "shareRevenue": false,
    "offerType": "OTHERS",
    "unsearchable": false,
    "releaseOffer": "",
    "title4Sort": "Underworld Trader Collection",
    "refundType": "NON_REFUNDABLE",
    "visibilityType": "IS_LISTED",
    "currencyDecimals": 2,
    "allowPurchaseForPartialOwned": true,
    "shareRevenueWithUnderageAffiliates": false,
    "partialItemPrerequisiteCheck": false
  },
  "7d270c7e78d3439db8afe81bcd0b6b6a": {
    "id": "7d270c7e78d3439db8afe81bcd0b6b6a",
    "title": "Castle Treasury",
    "description": "Gems and items",
    "longDescription": "Gems and items",
    "keyImages": [
      {
        "type": "Thumbnail",
        "url": "https://cdn1.epicgames.com/wex/offer/StoreBannerCastletreasuryCAT-512x512-2fac1319851701d50590de9c9441e585.jpg",
        "md5": "2fac1319851701d50590de9c9441e585",
        "width": 512,
        "height": 512,
        "size": 1691892,
        "uploadedDate": "2019-10-31T18:57:56.006Z"
      }
    ],
    "categories": [
      {
        "path": "mtx packages"
      }
    ],
    "namespace": "wex",
    "status": "SUNSET",
    "creationDate": "2018-07-31T20:30:36.098Z",
    "lastModifiedDate": "2022-12-14T15:55:31.994Z",
    "internalName": "Castle Treasury",
    "recurrence": "ONCE",
    "items": [
      {
        "id": "7aaaad1ac33346c698678fba3e15109b",
        "keyImages": [],
        "categories": [],
        "namespace": "wex",
        "unsearchable": false
      }
    ],
    "currencyCode": "AUD",
    "currentPrice": 4495,
    "price": 4495,
    "basePrice": 2999,
    "basePriceCurrencyCode": "USD",
    "recurringPrice": 0,
    "freeDays": 0,
    "maxBillingCycles": 0,
    "seller": {
      "id": "o-aa83a0a9bc45e98c80c1b1c9d92e9e",
      "name": "Epic Games"
    },
    "viewableDate": "2019-11-11T17:00:00.000Z",
    "effectiveDate": "2019-11-11T17:00:00.000Z",
    "expiryDate": "2022-12-14T16:00:00.000Z",
    "vatIncluded": true,
    "isCodeRedemptionOnly": false,
    "isFeatured": false,
    "taxSkuId": "FR_Game",
    "merchantGroup": "WEX_MKT",
    "priceTier": "prod-wex_USD_2999",
    "urlSlug": "release-castle-treasury",
    "roleNamesToGrant": [],
    "tags": [],
    "ignoreOrder": false,
    "fulfillToGroup": false,
    "fraudItemType": "RMT_Offer",
    "shareRevenue": false,
    "offerType": "OTHERS",
    "unsearchable": false,
    "releaseOffer": "",
    "title4Sort": "Castle Treasury",
    "refundType": "NON_REFUNDABLE",
    "visibilityType": "IS_LISTED",
    "currencyDecimals": 2,
    "allowPurchaseForPartialOwned": true,
    "shareRevenueWithUnderageAffiliates": false,
    "partialItemPrerequisiteCheck": false
  },
  "b1c1372c9d0a428bacde8161117b1b2c": {
    "id": "b1c1372c9d0a428bacde8161117b1b2c",
    "title": "Bag of Gems",
    "description": "Gems and items",
    "longDescription": "Gems and items",
    "keyImages": [
      {
        "type": "Thumbnail",
        "url": "https://cdn1.epicgames.com/wex/offer/StoreBannerpouchbagofgemsCAT-512x512-897e4920698db21010a5b2a1c751e9a1.jpg",
        "md5": "897e4920698db21010a5b2a1c751e9a1",
        "width": 512,
        "height": 512,
        "size": 1669161,
        "uploadedDate": "2019-10-31T19:00:15.088Z"
      }
    ],
    "categories": [
      {
        "path": "mtx packages"
      }
    ],
    "namespace": "wex",
    "status": "SUNSET",
    "creationDate": "2018-07-31T20:12:21.759Z",
    "lastModifiedDate": "2022-12-14T15:55:40.042Z",
    "internalName": "Bag of Gems",
    "recurrence": "ONCE",
    "items": [
      {
        "id": "af98a3729dc6444893fc2c34f002dd5a",
        "keyImages": [],
        "categories": [],
        "namespace": "wex",
        "unsearchable": false
      }
    ],
    "currencyCode": "AUD",
    "currentPrice": 1495,
    "price": 1495,
    "basePrice": 999,
    "basePriceCurrencyCode": "USD",
    "recurringPrice": 0,
    "freeDays": 0,
    "maxBillingCycles": 0,
    "seller": {
      "id": "o-aa83a0a9bc45e98c80c1b1c9d92e9e",
      "name": "Epic Games"
    },
    "viewableDate": "2019-11-11T17:00:00.000Z",
    "effectiveDate": "2019-11-11T17:00:00.000Z",
    "expiryDate": "2022-12-14T16:00:00.000Z",
    "vatIncluded": true,
    "isCodeRedemptionOnly": false,
    "isFeatured": false,
    "taxSkuId": "FR_Game",
    "merchantGroup": "WEX_MKT",
    "priceTier": "prod-wex_USD_1000",
    "urlSlug": "release-bag-of-gems",
    "roleNamesToGrant": [],
    "tags": [],
    "ignoreOrder": false,
    "fulfillToGroup": false,
    "fraudItemType": "RMT_Offer",
    "shareRevenue": false,
    "offerType": "OTHERS",
    "unsearchable": false,
    "releaseOffer": "",
    "title4Sort": "Bag of Gems",
    "refundType": "NON_REFUNDABLE",
    "visibilityType": "IS_LISTED",
    "currencyDecimals": 2,
    "allowPurchaseForPartialOwned": true,
    "shareRevenueWithUnderageAffiliates": false,
    "partialItemPrerequisiteCheck": false
  },
  "1bb845075f334ecaae7b55e421ab3dea": {
    "id": "1bb845075f334ecaae7b55e421ab3dea",
    "title": "Battle Pass",
    "description": "Unlocks premium Battle Pass rewards",
    "longDescription": "Unlocks premium Battle Pass rewards",
    "keyImages": [
      {
        "type": "Thumbnail",
        "url": "https://cdn1.epicgames.com/wex/offer/BP_3_BB-512x512-bee05de1924c0ee5e788b26338f16240.png",
        "md5": "bee05de1924c0ee5e788b26338f16240",
        "width": 512,
        "height": 512,
        "size": 385400,
        "uploadedDate": "2019-12-07T01:28:07.239Z"
      }
    ],
    "categories": [
      {
        "path": "recurring"
      }
    ],
    "namespace": "wex",
    "status": "SUNSET",
    "creationDate": "2018-06-11T20:07:55.881Z",
    "lastModifiedDate": "2022-12-14T15:55:35.914Z",
    "internalName": "Battle Pass",
    "recurrence": "ONCE",
    "items": [
      {
        "id": "0b7991b5075e491abadd836b3155fb18",
        "keyImages": [],
        "categories": [],
        "namespace": "wex",
        "unsearchable": false
      }
    ],
    "currencyCode": "AUD",
    "currentPrice": 755,
    "price": 755,
    "basePrice": 499,
    "basePriceCurrencyCode": "USD",
    "recurringPrice": 0,
    "freeDays": 0,
    "maxBillingCycles": 0,
    "seller": {
      "id": "o-aa83a0a9bc45e98c80c1b1c9d92e9e",
      "name": "Epic Games"
    },
    "viewableDate": "2019-11-11T17:00:00.000Z",
    "effectiveDate": "2019-11-11T17:00:00.000Z",
    "expiryDate": "2022-12-14T16:00:00.000Z",
    "vatIncluded": true,
    "isCodeRedemptionOnly": false,
    "isFeatured": false,
    "taxSkuId": "FR_Game",
    "merchantGroup": "WEX_MKT",
    "priceTier": "prod-wex_USD_499",
    "urlSlug": "battle-pass",
    "roleNamesToGrant": [],
    "tags": [],
    "purchaseLimit": -1,
    "ignoreOrder": false,
    "fulfillToGroup": false,
    "fraudItemType": "RMT_Offer",
    "shareRevenue": false,
    "offerType": "OTHERS",
    "unsearchable": false,
    "releaseOffer": "",
    "title4Sort": "Battle Pass",
    "refundType": "NON_REFUNDABLE",
    "visibilityType": "IS_LISTED",
    "currencyDecimals": 2,
    "allowPurchaseForPartialOwned": true,
    "shareRevenueWithUnderageAffiliates": false,
    "partialItemPrerequisiteCheck": false
  },
  "11b1aad3c22d4fe58c361b8c913477d6": {
    "id": "11b1aad3c22d4fe58c361b8c913477d6",
    "title": "Battle Breaker Collection",
    "description": "A pet and free daily chests!",
    "longDescription": "A pet and free daily chests!",
    "keyImages": [
      {
        "type": "Thumbnail",
        "url": "https://cdn1.epicgames.com/wex/offer/BB_InGame_StoreArt_Collection-512x512-03916083c870df5d62bad565313b36db.jpg",
        "md5": "03916083c870df5d62bad565313b36db",
        "width": 512,
        "height": 512,
        "size": 315373,
        "uploadedDate": "2019-11-12T19:02:31.375Z"
      }
    ],
    "categories": [
      {
        "path": "account_upgrades"
      }
    ],
    "namespace": "wex",
    "status": "SUNSET",
    "creationDate": "2018-07-30T23:02:57.245Z",
    "lastModifiedDate": "2022-12-14T15:55:28.852Z",
    "internalName": "Battle Breaker Collection",
    "recurrence": "ONCE",
    "items": [
      {
        "id": "91551bc9f3574ce28bf6207b72d766c9",
        "keyImages": [],
        "categories": [],
        "namespace": "wex",
        "unsearchable": false
      }
    ],
    "currencyCode": "AUD",
    "currentPrice": 2195,
    "price": 2195,
    "basePrice": 1499,
    "basePriceCurrencyCode": "USD",
    "recurringPrice": 0,
    "freeDays": 0,
    "maxBillingCycles": 0,
    "seller": {
      "id": "o-aa83a0a9bc45e98c80c1b1c9d92e9e",
      "name": "Epic Games"
    },
    "viewableDate": "2019-11-11T17:00:00.000Z",
    "effectiveDate": "2019-11-11T17:00:00.000Z",
    "expiryDate": "2022-12-14T16:00:00.000Z",
    "vatIncluded": true,
    "isCodeRedemptionOnly": false,
    "isFeatured": false,
    "taxSkuId": "FR_Game",
    "merchantGroup": "WEX_MKT",
    "priceTier": "prod-wex_USD_1499",
    "urlSlug": "vip-level-release",
    "roleNamesToGrant": [],
    "tags": [],
    "ignoreOrder": false,
    "fulfillToGroup": false,
    "fraudItemType": "RMT_Offer",
    "shareRevenue": false,
    "offerType": "OTHERS",
    "unsearchable": false,
    "releaseOffer": "",
    "title4Sort": "Battle Breaker Collection",
    "refundType": "NON_REFUNDABLE",
    "visibilityType": "IS_LISTED",
    "currencyDecimals": 2,
    "allowPurchaseForPartialOwned": true,
    "shareRevenueWithUnderageAffiliates": false,
    "partialItemPrerequisiteCheck": false
  },
  "2be4ab85c1ae42bab895be28ab6cb99e": {
    "id": "2be4ab85c1ae42bab895be28ab6cb99e",
    "title": "Master of the Hoard",
    "description": "A unique pet and more!",
    "longDescription": "A unique pet and more!",
    "keyImages": [
      {
        "type": "Thumbnail",
        "url": "https://cdn1.epicgames.com/wex/offer/BB_InGame_StoreArt_Collection-512x512-03916083c870df5d62bad565313b36db.jpg",
        "md5": "03916083c870df5d62bad565313b36db",
        "width": 512,
        "height": 512,
        "size": 315373,
        "uploadedDate": "2019-11-12T19:18:21.054Z"
      }
    ],
    "categories": [
      {
        "path": "account_upgrades"
      }
    ],
    "namespace": "wex",
    "status": "SUNSET",
    "creationDate": "2018-07-31T19:39:56.257Z",
    "lastModifiedDate": "2022-12-14T15:55:40.852Z",
    "internalName": "Master of the Hoard",
    "recurrence": "ONCE",
    "items": [
      {
        "id": "15cd3d5ce3c14b11904bc1c8a07d4081",
        "keyImages": [],
        "categories": [],
        "namespace": "wex",
        "unsearchable": false
      }
    ],
    "currencyCode": "AUD",
    "currentPrice": 2195,
    "price": 2195,
    "basePrice": 1499,
    "basePriceCurrencyCode": "USD",
    "recurringPrice": 0,
    "freeDays": 0,
    "maxBillingCycles": 0,
    "seller": {
      "id": "o-aa83a0a9bc45e98c80c1b1c9d92e9e",
      "name": "Epic Games"
    },
    "viewableDate": "2019-11-11T17:00:00.000Z",
    "effectiveDate": "2019-11-11T17:00:00.000Z",
    "expiryDate": "2022-12-14T16:00:00.000Z",
    "vatIncluded": true,
    "isCodeRedemptionOnly": false,
    "isFeatured": false,
    "taxSkuId": "FR_Game",
    "merchantGroup": "WEX_MKT",
    "priceTier": "prod-wex_USD_1499",
    "urlSlug": "vip-level-release-02",
    "roleNamesToGrant": [],
    "tags": [],
    "ignoreOrder": false,
    "fulfillToGroup": false,
    "fraudItemType": "RMT_Offer",
    "shareRevenue": false,
    "offerType": "OTHERS",
    "unsearchable": false,
    "releaseOffer": "",
    "title4Sort": "Master of the Hoard",
    "refundType": "NON_REFUNDABLE",
    "visibilityType": "IS_LISTED",
    "currencyDecimals": 2,
    "allowPurchaseForPartialOwned": true,
    "shareRevenueWithUnderageAffiliates": false,
    "partialItemPrerequisiteCheck": false
  },
  "20621749aaa04a49b28a2e68049470cb": {
    "id": "20621749aaa04a49b28a2e68049470cb",
    "title": "Treasure Hunter Collection",
    "description": "Daily treasures and more!",
    "longDescription": "Daily treasures and more!",
    "keyImages": [
      {
        "type": "Thumbnail",
        "url": "https://cdn1.epicgames.com/wex/offer/BB_InGame_StoreArt_Collection-512x512-03916083c870df5d62bad565313b36db.jpg",
        "md5": "03916083c870df5d62bad565313b36db",
        "width": 512,
        "height": 512,
        "size": 315373,
        "uploadedDate": "2019-11-12T19:15:46.581Z"
      }
    ],
    "categories": [
      {
        "path": "account_upgrades"
      }
    ],
    "namespace": "wex",
    "status": "SUNSET",
    "creationDate": "2018-07-31T19:14:17.585Z",
    "lastModifiedDate": "2022-12-14T15:55:37.939Z",
    "internalName": "Treasure Hunter Collection",
    "recurrence": "ONCE",
    "items": [
      {
        "id": "47127e95642443508f03f5334a7ff4bb",
        "keyImages": [],
        "categories": [],
        "namespace": "wex",
        "unsearchable": false
      }
    ],
    "currencyCode": "AUD",
    "currentPrice": 2195,
    "price": 2195,
    "basePrice": 1499,
    "basePriceCurrencyCode": "USD",
    "recurringPrice": 0,
    "freeDays": 0,
    "maxBillingCycles": 0,
    "seller": {
      "id": "o-aa83a0a9bc45e98c80c1b1c9d92e9e",
      "name": "Epic Games"
    },
    "viewableDate": "2019-11-11T17:00:00.000Z",
    "effectiveDate": "2019-11-11T17:00:00.000Z",
    "expiryDate": "2022-12-14T16:00:00.000Z",
    "vatIncluded": true,
    "isCodeRedemptionOnly": false,
    "isFeatured": false,
    "taxSkuId": "FR_Game",
    "merchantGroup": "WEX_MKT",
    "priceTier": "prod-wex_USD_1499",
    "urlSlug": "vip-level-release-01",
    "roleNamesToGrant": [],
    "tags": [],
    "ignoreOrder": false,
    "fulfillToGroup": false,
    "fraudItemType": "RMT_Offer",
    "shareRevenue": false,
    "offerType": "OTHERS",
    "unsearchable": false,
    "releaseOffer": "",
    "title4Sort": "Treasure Hunter Collection",
    "refundType": "NON_REFUNDABLE",
    "visibilityType": "IS_LISTED",
    "currencyDecimals": 2,
    "allowPurchaseForPartialOwned": true,
    "shareRevenueWithUnderageAffiliates": false,
    "partialItemPrerequisiteCheck": false
  },
  "9d517678254c4b27ab85f0d1d149784b": {
    "id": "9d517678254c4b27ab85f0d1d149784b",
    "title": "Swiftslayer Kale's Starter Pack",
    "description": "A nutritious ninja and upgrade items",
    "longDescription": "Deftly maneuver your way through each level and their perils with the help of Hero Swiftslayer Kale and these crafty upgrade items:\n\n-300 Gems\n-300,000 Gold\n-50,000 Hero XP\n-25 Nature Essence\n-25 Major Strength Elixirs\n-25 Major Health Elixirs",
    "keyImages": [
      {
        "type": "Thumbnail",
        "url": "https://cdn1.epicgames.com/wex/offer/spkale-512x512-cb1472b6cef1be5627ff37de9dc1ec6b.jpg",
        "md5": "cb1472b6cef1be5627ff37de9dc1ec6b",
        "width": 512,
        "height": 512,
        "size": 72105,
        "uploadedDate": "2020-01-23T19:39:29.008Z"
      }
    ],
    "categories": [
      {
        "path": "starter_packs"
      }
    ],
    "namespace": "wex",
    "status": "SUNSET",
    "creationDate": "2016-09-12T15:16:00.459Z",
    "lastModifiedDate": "2022-12-14T15:55:38.355Z",
    "internalName": "Swiftslayer Kale's Starter Pack",
    "recurrence": "ONCE",
    "items": [
      {
        "id": "e78d1268471745e7835e6c18218574d6",
        "keyImages": [],
        "categories": [],
        "namespace": "wex",
        "unsearchable": false
      }
    ],
    "currencyCode": "AUD",
    "currentPrice": 395,
    "price": 395,
    "basePrice": 299,
    "basePriceCurrencyCode": "USD",
    "recurringPrice": 0,
    "freeDays": 0,
    "maxBillingCycles": 0,
    "seller": {
      "id": "o-aa83a0a9bc45e98c80c1b1c9d92e9e",
      "name": "Epic Games"
    },
    "viewableDate": "2020-02-04T17:00:00.000Z",
    "effectiveDate": "2016-09-12T11:13:00.000Z",
    "expiryDate": "2022-12-14T16:00:00.000Z",
    "vatIncluded": true,
    "isCodeRedemptionOnly": false,
    "isFeatured": false,
    "taxSkuId": "FR_Game",
    "merchantGroup": "WEX_MKT",
    "priceTier": "prod-wex_USD_99",
    "urlSlug": "starter-pack",
    "roleNamesToGrant": [],
    "purchaseLimit": 1,
    "ignoreOrder": false,
    "fulfillToGroup": false,
    "fraudItemType": "RMT_Offer",
    "shareRevenue": false,
    "offerType": "IN_GAME_PURCHASE",
    "unsearchable": true,
    "releaseOffer": "",
    "title4Sort": "Swiftslayer Kale's Starter Pack",
    "refundType": "NON_REFUNDABLE",
    "visibilityType": "IS_LISTED",
    "currencyDecimals": 2,
    "allowPurchaseForPartialOwned": true,
    "shareRevenueWithUnderageAffiliates": false,
    "partialItemPrerequisiteCheck": false
  },
  "8e60722d2cd54953907351b5a94debc5": {
    "id": "8e60722d2cd54953907351b5a94debc5",
    "title": "Level-Up Pack",
    "description": "Rewards as you level up",
    "longDescription": "Rewards as you level up",
    "keyImages": [
      {
        "type": "Thumbnail",
        "url": "https://cdn1.epicgames.com/wex/offer/BB_InGame_StoreArt_Collection-512x512-03916083c870df5d62bad565313b36db.jpg",
        "md5": "03916083c870df5d62bad565313b36db",
        "width": 512,
        "height": 512,
        "size": 315373,
        "uploadedDate": "2019-11-12T19:19:32.271Z"
      }
    ],
    "categories": [
      {
        "path": "starter_packs"
      }
    ],
    "namespace": "wex",
    "status": "SUNSET",
    "creationDate": "2018-07-31T20:36:40.734Z",
    "lastModifiedDate": "2022-12-14T15:55:41.205Z",
    "internalName": "Level-Up Pack",
    "recurrence": "ONCE",
    "items": [
      {
        "id": "3db4fd77eaed4a9a9275257cfb71ba6c",
        "keyImages": [],
        "categories": [],
        "namespace": "wex",
        "unsearchable": false
      }
    ],
    "currencyCode": "AUD",
    "currentPrice": 2995,
    "price": 2995,
    "basePrice": 1999,
    "basePriceCurrencyCode": "USD",
    "recurringPrice": 0,
    "freeDays": 0,
    "maxBillingCycles": 0,
    "seller": {
      "id": "o-aa83a0a9bc45e98c80c1b1c9d92e9e",
      "name": "Epic Games"
    },
    "viewableDate": "2019-11-11T17:00:00.000Z",
    "effectiveDate": "2019-11-11T17:00:00.000Z",
    "expiryDate": "2022-12-14T16:00:00.000Z",
    "vatIncluded": true,
    "isCodeRedemptionOnly": false,
    "isFeatured": false,
    "taxSkuId": "FR_Game",
    "merchantGroup": "WEX_MKT",
    "priceTier": "prod-wex_USD_1999",
    "urlSlug": "release-level-up-pack",
    "roleNamesToGrant": [],
    "tags": [],
    "ignoreOrder": false,
    "fulfillToGroup": false,
    "fraudItemType": "RMT_Offer",
    "shareRevenue": false,
    "offerType": "OTHERS",
    "unsearchable": false,
    "releaseOffer": "",
    "title4Sort": "Level-Up Pack",
    "refundType": "NON_REFUNDABLE",
    "visibilityType": "IS_LISTED",
    "currencyDecimals": 2,
    "allowPurchaseForPartialOwned": true,
    "shareRevenueWithUnderageAffiliates": false,
    "partialItemPrerequisiteCheck": false
  }
}
```

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
