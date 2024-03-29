# Catalog Items

#####

*https://catalog-public-service-prod06.ol.epicgames.com/catalog/api/shared/namespace/wex/bulk/items?includeDLCDetails=false&includeMainGameDetails=false&country=US&locale=en*

___

## Request

```http
POST /catalog/api/shared/namespace/wex/bulk/items?includeDLCDetails=false&includeMainGameDetails=false&country=US&locale=en HTTP/1.1
```

### Query String

| Name                   | Value |
|------------------------|-------|
| includeDLCDetails      | false |
| includeMainGameDetails | false |
| country                | US    |
| locale                 | en    |

### Request Headers

| Name                  | Value                                                                                                                 |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------|
| Host                  | catalog-public-service-prod06.ol.epicgames.com                                                                        |
| Accept                | \*/\*                                                                                                                 |
| Accept-Encoding       | deflate, gzip                                                                                                         |
| Content-Type          | application/x-www-form-urlencoded                                                                                     |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F0B5EE074C9D4C2448C00AA6A440E5E1-E6A735F0484126F47FBBC489FF7ADA3A                |
| User-Agent            | UELauncher/14.4.1-23462965+++Portal+Release-Live Windows/10.0.22621.1.256.64bit                                       |
| Authorization         | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |
| Content-Length        | 179                                                                                                                   |

### Request Body

| Name | Value                            |
|------|----------------------------------|
| id   | a53e821fbdc24181877243a8dbb63463 |
| id   | a1689ab49a0d41e1a0828505861d0bb9 |
| id   | 3d329b913b3c44cc8f4c5a2fc84e7cf4 |
| id   | d3ec04d33f674fd3a7054b6b6b92d6c9 |
| id   | e458e71024404176addca212860f9ef2 |

___

## Response

#### Status: 200 OK

### Response Headers

| Name                  | Value                                                                                                  |
|-----------------------|--------------------------------------------------------------------------------------------------------|
| Date                  | Thu, 29 Dec 2022 05:55:04 GMT                                                                          |
| Content-Type          | application/json                                                                                       |
| Transfer-Encoding     | chunked                                                                                                |
| Vary                  | Accept-Encoding                                                                                        |
| X-Epic-Device-ID      | 2f4c92e44a8a8420a867089329526852                                                                       |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F0B5EE074C9D4C2448C00AA6A440E5E1-E6A735F0484126F47FBBC489FF7ADA3A |
| Content-Encoding      | gzip                                                                                                   |
| Connection            | keep-alive                                                                                             |

### Response Body

```json
{
  "a1689ab49a0d41e1a0828505861d0bb9": {
    "id": "a1689ab49a0d41e1a0828505861d0bb9",
    "title": "FN Kyle",
    "description": "FN Kyle",
    "keyImages": [],
    "categories": [
      {
        "path": "cross_promo"
      }
    ],
    "namespace": "wex",
    "status": "ACTIVE",
    "creationDate": "2019-09-11T15:22:58.646Z",
    "lastModifiedDate": "2019-11-20T18:15:25.453Z",
    "entitlementName": "FN_BB_Kyle",
    "entitlementType": "ENTITLEMENT",
    "itemType": "DURABLE",
    "releaseInfo": [],
    "developer": "Epic Games",
    "developerId": "o-aa83a0a9bc45e98c80c1b1c9d92e9e",
    "eulaIds": [],
    "endOfSupport": false,
    "unsearchable": false
  },
  "3d329b913b3c44cc8f4c5a2fc84e7cf4": {
    "id": "3d329b913b3c44cc8f4c5a2fc84e7cf4",
    "title": "FN Jess",
    "description": "FN Jess",
    "keyImages": [],
    "categories": [
      {
        "path": "cross_promo"
      }
    ],
    "namespace": "wex",
    "status": "ACTIVE",
    "creationDate": "2019-09-11T16:00:56.443Z",
    "lastModifiedDate": "2019-11-20T18:15:25.452Z",
    "entitlementName": "FN_BB_Jess",
    "entitlementType": "ENTITLEMENT",
    "itemType": "DURABLE",
    "releaseInfo": [],
    "developer": "Epic Games",
    "developerId": "o-aa83a0a9bc45e98c80c1b1c9d92e9e",
    "eulaIds": [],
    "endOfSupport": false,
    "unsearchable": false
  },
  "d3ec04d33f674fd3a7054b6b6b92d6c9": {
    "id": "d3ec04d33f674fd3a7054b6b6b92d6c9",
    "title": "FN Ramirez",
    "description": "Ramirez Hero (Fortnite Cross-Promotion)",
    "keyImages": [],
    "categories": [
      {
        "path": "cross_promo"
      }
    ],
    "namespace": "wex",
    "status": "ACTIVE",
    "creationDate": "2019-09-09T21:09:32.805Z",
    "lastModifiedDate": "2019-11-20T18:15:25.453Z",
    "entitlementName": "d3ec04d33f674fd3a7054b6b6b92d6c9",
    "entitlementType": "ENTITLEMENT",
    "itemType": "DURABLE",
    "releaseInfo": [],
    "developer": "Epic Games",
    "developerId": "o-aa83a0a9bc45e98c80c1b1c9d92e9e",
    "eulaIds": [],
    "endOfSupport": false,
    "unsearchable": false
  },
  "a53e821fbdc24181877243a8dbb63463": {
    "id": "a53e821fbdc24181877243a8dbb63463",
    "title": "Battle Breakers",
    "description": "Battle Breakers",
    "keyImages": [
      {
        "type": "Featured",
        "url": "https://cdn1.epicgames.com/wex/item/BB_AndroidLauncher_Keyart-800x800-f83d14d91266a550f50475984ec11bf8.jpg",
        "md5": "f83d14d91266a550f50475984ec11bf8",
        "width": 800,
        "height": 800,
        "size": 758378,
        "uploadedDate": "2020-07-21T16:09:53.602Z"
      },
      {
        "type": "DieselGameBox",
        "url": "https://cdn1.epicgames.com/wex/item/BB_AndroidLauncher_Keyart-800x800-f83d14d91266a550f50475984ec11bf8.jpg",
        "md5": "f83d14d91266a550f50475984ec11bf8",
        "width": 800,
        "height": 800,
        "size": 758378,
        "uploadedDate": "2020-07-21T19:06:39.190Z"
      },
      {
        "type": "DieselGameBoxTall",
        "url": "https://cdn1.epicgames.com/wex/item/BB_AndroidLauncher_Keyart-800x800-f83d14d91266a550f50475984ec11bf8.jpg",
        "md5": "f83d14d91266a550f50475984ec11bf8",
        "width": 800,
        "height": 800,
        "size": 758378,
        "uploadedDate": "2020-07-21T19:07:13.144Z"
      }
    ],
    "categories": [
      {
        "path": "games"
      },
      {
        "path": "applications"
      }
    ],
    "namespace": "wex",
    "status": "ACTIVE",
    "creationDate": "2016-08-10T17:22:25.371Z",
    "lastModifiedDate": "2022-02-14T19:52:45.988Z",
    "customAttributes": {
      "CanSkipKoreanIdVerification": {
        "type": "STRING",
        "value": "true"
      },
      "FolderName": {
        "type": "STRING",
        "value": "BattleBreakers"
      }
    },
    "entitlementName": "WorldExplorersLive",
    "entitlementType": "EXECUTABLE",
    "itemType": "DURABLE",
    "releaseInfo": [
      {
        "id": "f9a36cd1681a41d1872c7037ec8d8c60",
        "appId": "WorldExplorersLive",
        "compatibleApps": [],
        "platform": [
          "Windows"
        ],
        "dateAdded": "2016-08-10T00:00:00.000Z"
      }
    ],
    "developer": "Epic Games",
    "developerId": "o-aa83a0a9bc45e98c80c1b1c9d92e9e",
    "eulaIds": [
      "egstore"
    ],
    "installModes": [],
    "endOfSupport": false,
    "ageGatings": {},
    "applicationId": "",
    "unsearchable": true
  },
  "e458e71024404176addca212860f9ef2": {
    "id": "e458e71024404176addca212860f9ef2",
    "title": "Battle Breakers free audience access item",
    "description": "Battle Breakers free audience access item",
    "keyImages": [
      {
        "type": "DieselGameBox",
        "url": "https://cdn1.epicgames.com/wex/item/EG_Store_BattleBreakers_Blade_Desktop_Vertical-400x530-afdd15049ad2c0e79dc21d4235551daa.jpg",
        "md5": "afdd15049ad2c0e79dc21d4235551daa",
        "width": 400,
        "height": 530,
        "size": 314602,
        "uploadedDate": "2019-11-04T18:08:09.176Z"
      },
      {
        "type": "DieselGameBoxLogo",
        "url": "https://cdn1.epicgames.com/wex/item/BB_EGS_LauncherLogo-600x600-a6461213c7f9dee740bb19879f69f218.png",
        "md5": "a6461213c7f9dee740bb19879f69f218",
        "width": 600,
        "height": 600,
        "size": 198270,
        "uploadedDate": "2019-11-04T18:08:44.444Z"
      },
      {
        "type": "ESRB",
        "url": "https://cdn1.epicgames.com/wex/item/ESRB_BB-842x485-bdb4735b95d04022de302870571f199d.jpg",
        "md5": "bdb4735b95d04022de302870571f199d",
        "width": 842,
        "height": 485,
        "size": 109062,
        "uploadedDate": "2020-01-07T15:37:05.749Z"
      }
    ],
    "categories": [
      {
        "path": "accesscontrol"
      }
    ],
    "namespace": "wex",
    "status": "ACTIVE",
    "creationDate": "2019-10-11T13:37:54.714Z",
    "lastModifiedDate": "2020-01-07T15:37:11.076Z",
    "entitlementName": "WorldExplorers_Free",
    "entitlementType": "AUDIENCE",
    "itemType": "DURABLE",
    "releaseInfo": [],
    "developer": "Epic Games",
    "developerId": "o-aa83a0a9bc45e98c80c1b1c9d92e9e",
    "eulaIds": [],
    "endOfSupport": false,
    "esrbGameRatingValue": "TEEN",
    "unsearchable": false
  }
}
```

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
