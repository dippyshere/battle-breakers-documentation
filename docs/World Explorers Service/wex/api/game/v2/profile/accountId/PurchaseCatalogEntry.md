# Purchase Catalog Entry

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/:accountId/PurchaseCatalogEntry?profileId=profile0&rvn=40504*

___

## Request

```http
POST /wex/api/game/v2/profile/:accountId/PurchaseCatalogEntry?profileId=profile0&rvn=40504 HTTP/1.1
```

### Path Parameters

| Name     | Value                             |
|----------|-----------------------------------|
| acountId | ec0ebb7e56f6454e86c62299a7b32e21  |

### Query String

| Name      | Value    |
|-----------|----------|
| profileId | profile0 |
| rvn       | 40504    |

### Request Headers

| Name                         | Value                                                                                                                                                                                                                                                                              |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Host                         | wex-public-service-live-prod.ol.epicgames.com                                                                                                                                                                                                                                      |
| Accept-Encoding              | deflate, gzip                                                                                                                                                                                                                                                                      |
| Accept                       | \*/\*                                                                                                                                                                                                                                                                              |
| Content-Type                 | application/json                                                                                                                                                                                                                                                                   |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":24189},{"profileId":"levels","clientCommandRevision":14480},{"profileId":"friends","clientCommandRevision":8264},{"profileId":"monsterpit","clientCommandRevision":1081},{"profileId":"multiplayer","clientCommandRevision":900}] |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-98E0DD3B4D2B5E8C12ED9BA37B5447B6                                                                                                                                                                             |
| User-Agent                   | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit                                                                                                                                                                                                                   |
| Authorization                | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md)                                                                                                                                                              |
| Content-Length               | 180                                                                                                                                                                                                                                                                                |

### Request Body

```json
{
  "offerId": "BA24852247819DFDC572E0A0D5DA7563",
  "purchaseQuantity": 1,
  "currency": "MtxCurrency",
  "currencySubType": "",
  "expectedTotalPrice": 75,
  "gameContext": ""
}
```

___

## Response

#### Status: 200 OK

### Response Headers

| Name                         | Value                                                                                                  |
|------------------------------|--------------------------------------------------------------------------------------------------------|
| Date                         | Thu, 29 Dec 2022 06:08:06 GMT                                                                          |
| Content-Type                 | application/json                                                                                       |
| Content-Length               | 2840                                                                                                   |
| X-EpicGames-McpVersion       | prod Release-1.88-1.88 build 107 cl 19310354                                                           |
| X-EpicGames-ContentVersion   | 1.88.244-r17036752                                                                                     |
| X-EpicGames-MinBuild         | 17036752                                                                                               |
| X-EpicGames-Profile-Revision | 40504                                                                                                  |
| X-Epic-Device-ID             | 68009daed09498667a8039cce09983ed                                                                       |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-98E0DD3B4D2B5E8C12ED9BA37B5447B6 |
| Connection                   | keep-alive                                                                                             |

### Response Body

```json
{
  "profileRevision": 40505,
  "profileId": "profile0",
  "profileChangesBaseRevision": 40504,
  "profileChanges": [
    {
      "changeType": "itemQuantityChanged",
      "itemId": "c384fe1c-cf33-48ab-868e-56125c6f9b88",
      "quantity": 47666
    },
    {
      "changeType": "statModified",
      "name": "in_app_purchases",
      "value": {
        "receipts": [
          "EPIC:eb665de87ac14ffab73aeb96bd333330",
          "EPIC:2e02135793fe4413aa1640498211d7c2",
          "EPIC:c8dd7751893344e99f46bb53f016c56b"
        ],
        "ignoredReceipts": [],
        "fulfillmentCounts": {
          "31F1E7B54BEE5543632BFEB482C4ACFA": 12,
          "186EC3E24BDAA76FCEFCA68DDC887D0F": 1,
          "732F6AA847F9E06DA6BC80BE7787239E": 5,
          "814943904E314407D9148283C9E2F844": 1,
          "CE1C43AA459C1ECEC8B18F9BA20D1097": 1,
          "CB216748458584AD3A77589F2DC76650": 2,
          "7261281843FAF9039E92E2A98FA92915": 14,
          "878728D44A2CA0901731C387D18FEED5": 1,
          "6392E0D84AF6F18DCDAAA48F5546D655": 6,
          "4C8EACD1407CB320A502B89DCDAC5E81": 208,
          "72C1755A4BD8E5ECAED50785FCF03FAD": 8,
          "233CFA5B48709E1D65BD5F8FA57EA5DA": 1,
          "F6A2E1ED4CB463E5C0E4D7B820DA4E58": 1,
          "A86A61834036C4E950E1F2A5B40B4AE5": 1,
          "38278D54469AA644404255919ABC67CF": 1,
          "DC714F7D45EEEC1D2756938E0FA3B582": 1,
          "52D56C1E4AEC429B0A7832829468C197": 1,
          "D474860B426A23965442C89B99BE10D8": 5,
          "E82EF78449C4B61A829BBBBE91EE9C7E": 1,
          "75CB97A24CA11057CC4C9DABB00815AA": 2,
          "E7EEA718452DEDED4574BD9D51CE23A1": 1,
          "61CD419C44CD138E0553CEA45150F1B8": 206,
          "48268FEC4038F934733109AFAE874A71": 1,
          "EBDAA0DC4684721269F4F29A5494519E": 1,
          "E378447A458FC88538561791FBC40E8D": 4,
          "E6D1A39447B70DD0DF3B1BB6A131048E": 1,
          "BC654DB043042EDBC9BE119B694B31FC": 1,
          "C8510E9E43D4A175E11A4D83477965AE": 2,
          "D278C0A74FF450148D6E7C8682581A30": 1,
          "B745870D4E6945E04A065E9A96CF5849": 1,
          "5D65EC654A3B7E261272F3997142AB23": 90,
          "173064B74940CE8DC97BD58D041C50FC": 1,
          "8550273E418A227A2CCFE7B8825472FF": 1,
          "079FD00344F68D68E5E775AD0E62EB2A": 1,
          "78518C6744B17181971E0FBDAC7AA2BC": 7,
          "8772B1374685F66D9F9B54A0A3C026B5": 1,
          "CF03EC6145560777C8E2D58CD8588386": 1,
          "D98E59024D2A05BB8E7773BD4951B36F": 1,
          "C17935C642A727E5C50C1BB47D5890AC": 1,
          "A80BEC12434F8B49089CC792CDB846F4": 12,
          "689616B946BB3263CDD4F99952A3A666": 1,
          "C426C022454E0C7359B90BA969FA466B": 3,
          "640638854F2169675F757CA9F211A0E3": 1,
          "103ED23440AAA7003FF8F18687922A23": 1,
          "83BCFEDA406B41DEAA2F7390CEFF8264": 2,
          "8299F3BC42C1058E5AFC2ABF92E17A31": 1,
          "B001F0CB45831A4AB6BF2BA950EF7FA9": 24,
          "1B469D454810E7E7FDED778538F84FB3": 1,
          "9514A1FF45D5609EC6AADBA5F3F4C11E": 1,
          "190D074344071F0E47351E9293C95AC0": 1,
          "E3069A27428C5C1D05892DA6244406B4": 1,
          "9CB6414546E5B8D84ACD149377E57579": 9,
          "C31635B946A2B1184D391FABFAE3656B": 5,
          "D578396A44620E4D15757BB62D82F65C": 1
        }
      }
    },
    {
      "changeType": "statModified",
      "name": "hero_limit",
      "value": 75
    },
    {
      "changeType": "statModified",
      "name": "store_level",
      "value": 65465
    }
  ],
  "notifications": [
    {
      "type": "CatalogPurchase",
      "primary": true,
      "lootResult": {
        "items": [
          {
            "itemType": "StandIn:InventoryUpgrade",
            "attributes": {
              "FakeQuantity": 5
            },
            "quantity": 0
          }
        ]
      }
    }
  ],
  "profileCommandRevision": 24190,
  "serverTime": "2022-12-29T06:08:06.723Z",
  "responseVersion": 1
}
```

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
