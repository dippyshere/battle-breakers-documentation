# Catalog

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/storefront/v2/catalog*

___

## Request

```http
GET /wex/api/storefront/v2/catalog HTTP/1.1
```

### Request Headers

| Name                  | Value                                                                                                                 |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------|
| Host                  | wex-public-service-live-prod.ol.epicgames.com                                                                         |
| Accept                | \*/\*                                                                                                                 |
| Accept-Encoding       | deflate, gzip                                                                                                         |
| X-EpicGames-Language  | en                                                                                                                    |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-E2B1B7EB42DD8FFC885BA985C350EAE0                |
| User-Agent            | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit                                                      |
| Authorization         | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |
| Content-Length        | 0                                                                                                                     |

___

## Response

#### Status: 200 OK

### Response Headers

| Name                       | Value                                                                                                  |
|----------------------------|--------------------------------------------------------------------------------------------------------|
| Date                       | Thu, 29 Dec 2022 05:43:08 GMT                                                                          |
| Content-Type               | application/json                                                                                       |
| Transfer-Encoding          | chunked                                                                                                |
| ETag                       | "B5F133E64D8591C71054B2B901114A26\|2022-12-29T00:00:00.000Z"                                           |
| X-EpicGames-McpVersion     | prod Release-1.88-1.88 build 107 cl 19310354                                                           |
| X-EpicGames-ContentVersion | 1.88.244-r17036752                                                                                     |
| X-EpicGames-MinBuild       | 17036752                                                                                               |
| X-Epic-Device-ID           | 68009daed09498667a8039cce09983ed                                                                       |
| X-Epic-Correlation-ID      | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-E2B1B7EB42DD8FFC885BA985C350EAE0 |
| Connection                 | keep-alive                                                                                             |

### Response Body

```json
{
  "refreshIntervalHrs": 12,
  "dailyPurchaseHrs": 12,
  "expiration": "2022-12-29T12:00:00.000Z",
  "storefronts": [
    {
      "name": "SecretShopPage3",
      "catalogEntries": [
        {
          "offerId": "01A480B175DE4C0DB99401D86666176A",
          "devName": "SecretShop.Page03.Reagent.39",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 300000,
              "dynamicRegularPrice": -1,
              "finalPrice": 255000,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 255000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Light",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "8C91A991717542BD88443E1F7716FFF2",
          "devName": "SecretShop.Page03.Reagent.35",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 300000,
              "dynamicRegularPrice": -1,
              "finalPrice": 255000,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 255000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Dark",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "7ABB7112D4BE4840B7B4384F22C186AF",
          "devName": "SecretShop.Page03.UnderworldTrader.38",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 25000000,
              "dynamicRegularPrice": -1,
              "finalPrice": 17500000,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 17500000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "VipLevelMin",
              "value": "3"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Voucher:Voucher_HeroGold",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "7BF89D7E6B6C4535867A0D46837E4AB4",
          "devName": "SecretShop.Page03.Misc.20",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 50000,
              "dynamicRegularPrice": -1,
              "finalPrice": 50000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 50000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_RXT_Parts_Small",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "BD2928EF77C8426B94A9B6D1B6111EB2",
          "devName": "SecretShop.Page03.Free.23",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 20000,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 14,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "TreasureMap:TM_MapResource",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "0EA59EE901364F008A2FF012BD2C3661",
          "devName": "SecretShop.Page03.TreasureMap.17",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 200,
              "dynamicRegularPrice": -1,
              "finalPrice": 200,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 200
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "TreasureMap:TM_Special_EasterEggDesert",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "9A4615BC36F04DC58BF42E06686F34C6",
          "devName": "SecretShop.Page03.CharShard.17",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 7500000,
              "dynamicRegularPrice": -1,
              "finalPrice": 7500000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 7500000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Voucher:Voucher_Chest_Gold",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "24D10F44ABF141ABB8551959E4716C14",
          "devName": "SecretShop.Page03.Elixir.13",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 400000,
              "dynamicRegularPrice": -1,
              "finalPrice": 340000,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 340000
            }
          ],
          "categories": [],
          "dailyLimit": 2,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "DC18D15274E643BDA2028A87D13A7D28",
          "devName": "SecretShop.Page03.Misc.17",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 200,
              "dynamicRegularPrice": -1,
              "finalPrice": 170,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 170
            }
          ],
          "categories": [],
          "dailyLimit": 5000,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "+100 ",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Currency:HeroXp_Basic",
              "quantity": 100
            }
          ]
        },
        {
          "offerId": "F7A58E0D17844A7CA8584F58B426A3D0",
          "devName": "SecretShop.Page03.Free.24",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 10000,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 2,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Currency:Hammer",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "1270FFDB3C6243C19C43BB3908458C4B",
          "devName": "SecretShop.Page03.UnderworldTrader.41",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 200,
              "dynamicRegularPrice": -1,
              "finalPrice": 140,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 140
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "VipLevelMin",
              "value": "3"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Fire",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "D8654A64B37B4A84B9EB8AC40B5EBD74",
          "devName": "SecretShop.Page03.UnderworldTrader.42",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 200,
              "dynamicRegularPrice": -1,
              "finalPrice": 140,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 140
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "VipLevelMin",
              "value": "3"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Light",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "1CE00BD101944F1F8FFB6CE8A86D83C6",
          "devName": "SecretShop.Page03.UnderworldTrader.31",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 10,
              "dynamicRegularPrice": -1,
              "finalPrice": 7,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 7
            }
          ],
          "categories": [],
          "dailyLimit": 20,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "VipLevelMin",
              "value": "3"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Ore:Ore_Magicite",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "E92D1AE46A554266AB5EFD0DB4C6D828",
          "devName": "SecretShop.Page03.Elixir.18",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 100,
              "dynamicRegularPrice": -1,
              "finalPrice": 85,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 85
            }
          ],
          "categories": [],
          "dailyLimit": 2,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "F081F10753F94B39AA88A0609AC0971F",
          "devName": "SecretShop.Page03.Shard.15",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 300000,
              "dynamicRegularPrice": -1,
              "finalPrice": 255000,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 255000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Water",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "611267C0B7174C4499804DCEBF51E2F5",
          "devName": "SecretShop.Page03.TreasureMap.13",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 10,
              "dynamicRegularPrice": -1,
              "finalPrice": 10,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 10
            }
          ],
          "categories": [],
          "dailyLimit": 10,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "TreasureMap:TM_MapResource",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "CD0B8DDB5FEE40F9B4E33CF973654B48",
          "devName": "SecretShop.Page03.UnderworldTraderGold.07",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 50000,
              "dynamicRegularPrice": -1,
              "finalPrice": 35000,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 35000
            }
          ],
          "categories": [],
          "dailyLimit": 6,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "VipLevelMin",
              "value": "3"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "273F7DB343AB4DC78BE0AAA50BB64760",
          "devName": "SecretShop.Page03.Reagent.56",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 200,
              "dynamicRegularPrice": -1,
              "finalPrice": 170,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 170
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Dark",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "13E9A5022CD0413396B7C45272B5F511",
          "devName": "SecretShop.Page03.Ore.03",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 25000,
              "dynamicRegularPrice": -1,
              "finalPrice": 21250,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 21250
            }
          ],
          "categories": [],
          "dailyLimit": 3,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Ore:Ore_Magicite",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "3E25EF1A1BF6491794A6E2A9E29C05B8",
          "devName": "SecretShop.Page03.Reagent.43",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 300000,
              "dynamicRegularPrice": -1,
              "finalPrice": 255000,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 255000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Fire",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "1D3216FA38B1449E83BD6CE25FE1AA1F",
          "devName": "SecretShop.Page03.Elixir.14",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 50000,
              "dynamicRegularPrice": -1,
              "finalPrice": 42500,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 42500
            }
          ],
          "categories": [],
          "dailyLimit": 5,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "2203013F57E74ED0B62D93BBA795FFE7",
          "devName": "SecretShop.Page03.UnderworldTrader.48",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 200,
              "dynamicRegularPrice": -1,
              "finalPrice": 170,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 170
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "VipLevelMin",
              "value": "3"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Water",
              "quantity": 1
            }
          ]
        }
      ]
    },
    {
      "name": "SecretShopPage4",
      "catalogEntries": [
        {
          "offerId": "9C09FF121A51434FBE35E60EF9B5734C",
          "devName": "SecretShop.Page04.CharShard.18",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 7500000,
              "dynamicRegularPrice": -1,
              "finalPrice": 7500000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 7500000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Voucher:Voucher_Chest_Gold",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "4401C298A06B4B64893906A83AC723EF",
          "devName": "SecretShop.Page04.Free.41",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 10000,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 4,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Currency:Hammer",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "C493ACD1C9BD4DD989AFBF505586190A",
          "devName": "SecretShop.Page04.Elixir.26",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 25,
              "dynamicRegularPrice": -1,
              "finalPrice": 25,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 25
            }
          ],
          "categories": [],
          "dailyLimit": 10,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "9809E345CEB0419A8D123E475CEB63AA",
          "devName": "SecretShop.Page04.Reagent.65",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 300000,
              "dynamicRegularPrice": -1,
              "finalPrice": 255000,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 255000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Water",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "E5FF8D0E66F54FD9BFEACE2398A2A348",
          "devName": "SecretShop.Page04.UnderworldTrader.85",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 10,
              "dynamicRegularPrice": -1,
              "finalPrice": 7,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 7
            }
          ],
          "categories": [],
          "dailyLimit": 20,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "VipLevelMin",
              "value": "3"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Ore:Ore_Magicite",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "4A1F7D6FF55445D9BEE60072F14EBE16",
          "devName": "SecretShop.Page04.Misc.32",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 200,
              "dynamicRegularPrice": -1,
              "finalPrice": 170,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 170
            }
          ],
          "categories": [],
          "dailyLimit": 5000,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "+100 ",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Currency:HeroXp_Basic",
              "quantity": 100
            }
          ]
        },
        {
          "offerId": "945007F9F5734A37BED76E8FB912E00C",
          "devName": "SecretShop.Page04.TreasureMap.24",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 40000,
              "dynamicRegularPrice": -1,
              "finalPrice": 34000,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 34000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "TreasureMap:TM_Special_BridgeOfLight",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "6FFB1D1C34AD4C27B58937CA148FE401",
          "devName": "SecretShop.Page04.Elixir.21",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 50000,
              "dynamicRegularPrice": -1,
              "finalPrice": 42500,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 42500
            }
          ],
          "categories": [],
          "dailyLimit": 10,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "7926EEB0E67F4264A66DD4AEF1608EB2",
          "devName": "SecretShop.Page04.TreasureMap.26",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 200000,
              "dynamicRegularPrice": -1,
              "finalPrice": 170000,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 170000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "TreasureMap:TM_Special_EasterEggDesert",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "42C688E164FB4334A4EDB33B8B0A6192",
          "devName": "SecretShop.Page04.Reagent.70",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 300000,
              "dynamicRegularPrice": -1,
              "finalPrice": 255000,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 255000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Light",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "891D127985CE4280A50D8C04AD795BC2",
          "devName": "SecretShop.Page04.UnderworldTrader.74",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 200,
              "dynamicRegularPrice": -1,
              "finalPrice": 140,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 140
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "VipLevelMin",
              "value": "3"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Water",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "9012C3D9001C4963A50B4E5B5E62DBDC",
          "devName": "SecretShop.Page04.Free.49",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 200,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 2,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Nature",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "E93E35DC403E4165A8A056B96E4033DB",
          "devName": "SecretShop.Page04.UnderworldTrader.73",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": 40,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "VipLevelMin",
              "value": "3"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shared_T02",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "9D8BA6C6A4DD49C18DFA25A934387627",
          "devName": "SecretShop.Page04.Shard.22",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 300000,
              "dynamicRegularPrice": -1,
              "finalPrice": 255000,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 255000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Fire",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "034652FBA49641339A13BDBD71E3BD03",
          "devName": "SecretShop.Page04.Misc.35",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 50000,
              "dynamicRegularPrice": -1,
              "finalPrice": 50000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 50000
            }
          ],
          "categories": [],
          "dailyLimit": 2,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_RXT_Parts_Small",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "4B01C5CB45874FB795DB426C6B782D3D",
          "devName": "SecretShop.Page04.Ore.05",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 25000,
              "dynamicRegularPrice": -1,
              "finalPrice": 21250,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 21250
            }
          ],
          "categories": [],
          "dailyLimit": 3,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Ore:Ore_Magicite",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "CF797C9843024F7A88375E17B26FCF76",
          "devName": "SecretShop.Page04.UnderworldTrader.68",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 200,
              "dynamicRegularPrice": -1,
              "finalPrice": 170,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 170
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "VipLevelMin",
              "value": "3"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Dark",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "44EF4424C5AF4E928E3CA99FAA2E6365",
          "devName": "SecretShop.Page04.Reagent.74",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 300000,
              "dynamicRegularPrice": -1,
              "finalPrice": 255000,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 255000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Fire",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "0604A5DB0B6A452CBC0B6E9DEDA843FF",
          "devName": "SecretShop.Page04.UnderworldTrader.81",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 400,
              "dynamicRegularPrice": -1,
              "finalPrice": 280,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 280
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "VipLevelMin",
              "value": "3"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "TreasureMap:TM_Special_PlanetCore",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "4B5C894ED917427BBD6B1DBAD94EABB7",
          "devName": "SecretShop.Page04.Reagent.68",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 300000,
              "dynamicRegularPrice": -1,
              "finalPrice": 255000,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 255000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Fire",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "0FF150C7D9C6411B9DB11FDB798C2155",
          "devName": "SecretShop.Page04.Elixir.24",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 50000,
              "dynamicRegularPrice": -1,
              "finalPrice": 42500,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 42500
            }
          ],
          "categories": [],
          "dailyLimit": 10,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "6BBFC4FB2AEE49AD9C6E288A52B2DFB9",
          "devName": "SecretShop.Page04.UnderworldTraderGold.11",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 2500,
              "dynamicRegularPrice": -1,
              "finalPrice": 1500,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1500
            }
          ],
          "categories": [],
          "dailyLimit": 30,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "VipLevelMin",
              "value": "3"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shared_T02",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "67068C10964040F2A70750221CCFE85E",
          "devName": "SecretShop.Page04.UnderworldTraderGold.13",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 4000,
              "dynamicRegularPrice": -1,
              "finalPrice": 2800,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 2800
            }
          ],
          "categories": [],
          "dailyLimit": 15,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "VipLevelMin",
              "value": "3"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "UpgradePotion:UpgradeHealthMinor",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "BA0AA33CB91B4031A769CFF25734131F",
          "devName": "SecretShop.Page04.UnderworldTrader.70",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 200,
              "dynamicRegularPrice": -1,
              "finalPrice": 170,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 170
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "VipLevelMin",
              "value": "3"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Light",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "685FBC83F8354595B12F8FC3014BAA3E",
          "devName": "SecretShop.Page04.Shard.29",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 200,
              "dynamicRegularPrice": -1,
              "finalPrice": 170,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 170
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Nature",
              "quantity": 1
            }
          ]
        }
      ]
    },
    {
      "name": "GemStore",
      "catalogEntries": [
        {
          "offerId": "2A5A0D104128328EDC4A27B5617FD200",
          "devName": "Bag of Gems",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "RealMoney",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "b1c1372c9d0a428bacde8161117b1b2c",
            "bb_bagofgems_release",
            "",
            "bb_bagofgems_release",
            "",
            "GEM1250000000000",
            "43484e39-3038-3030-c05a-3957434a2100",
            "",
            "sam_bagofgems_release"
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "bShowInGemStore",
              "value": "true"
            }
          ],
          "catalogGroup": "BagOfGems",
          "catalogGroupPriority": 0,
          "sortPriority": -3,
          "title": "Bag of Gems",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "/Game/UMG/Textures/Store/btn_StoreGemBag.btn_StoreGemBag",
          "itemGrants": [
            {
              "templateId": "Currency:MtxPurchased",
              "quantity": 1000
            },
            {
              "templateId": "Currency:MtxPurchaseBonus",
              "quantity": 250
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 30
            },
            {
              "templateId": "Reagent:Reagent_SupplyPoints_Elite",
              "quantity": 100
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 20
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 20
            }
          ]
        },
        {
          "offerId": "2D1D3AD847EABB6E86064997D9787928",
          "devName": "Castle Treasury",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "RealMoney",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "7d270c7e78d3439db8afe81bcd0b6b6a",
            "bb_castletreasury_release",
            "",
            "bb_castletreasury_release",
            "",
            "GEM4200000000000",
            "355a4d39-434e-3031-c047-3734384d0e00",
            "",
            "sam_castletreasury_release"
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "bShowInGemStore",
              "value": "true"
            }
          ],
          "catalogGroup": "CastleTreasury",
          "catalogGroupPriority": 0,
          "sortPriority": -6,
          "title": "Castle Treasury",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "/Game/UMG/Textures/Store/btn_StoreGemCastleTreasury.btn_StoreGemCastleTreasury",
          "itemGrants": [
            {
              "templateId": "Currency:MtxPurchased",
              "quantity": 3000
            },
            {
              "templateId": "Currency:MtxPurchaseBonus",
              "quantity": 1200
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 100
            },
            {
              "templateId": "Reagent:Reagent_SupplyPoints_Elite",
              "quantity": 300
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 75
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 75
            }
          ]
        }
      ]
    },
    {
      "name": "SecretShopPage2",
      "catalogEntries": [
        {
          "offerId": "CF8D4C453F0E4A75B3132B738A849923",
          "devName": "SecretShop.Page02.Misc.05",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 200,
              "dynamicRegularPrice": -1,
              "finalPrice": 170,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 170
            }
          ],
          "categories": [],
          "dailyLimit": 1000,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "+100 ",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Currency:HeroXp_Basic",
              "quantity": 100
            }
          ]
        },
        {
          "offerId": "B0BD3890216C42D28285B77FC750051F",
          "devName": "SecretShop.Page02.UnderworldTrader.01",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 10,
              "dynamicRegularPrice": -1,
              "finalPrice": 7,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 7
            }
          ],
          "categories": [],
          "dailyLimit": 20,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "VipLevelMin",
              "value": "3"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Ore:Ore_Magicite",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "3B8ED787C720461BBD404DE378D26A8F",
          "devName": "SecretShop.Page02.Reagent.25",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 200,
              "dynamicRegularPrice": -1,
              "finalPrice": 170,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 170
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Nature",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "155F8F1C420F4E6497F7811F5A6A4E0E",
          "devName": "SecretShop.Page02.Elixir.08",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 100,
              "dynamicRegularPrice": -1,
              "finalPrice": 85,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 85
            }
          ],
          "categories": [],
          "dailyLimit": 2,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "72E3AD399EE34F6EA5C61BDA4FD8E99C",
          "devName": "SecretShop.Page02.CharShard.13",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 1000000,
              "dynamicRegularPrice": -1,
              "finalPrice": 1000000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1000000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Misc_CeremonialSword",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "737D98FEB7A6407AA5C23590B232F374",
          "devName": "SecretShop.Page02.TreasureMap.04",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 150,
              "dynamicRegularPrice": -1,
              "finalPrice": 150,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 150
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "TreasureMap:TM_Special_Cloud5",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "C67B485F976443EFBB757F01987490DC",
          "devName": "SecretShop.Page02.Misc.03",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 1000000,
              "dynamicRegularPrice": -1,
              "finalPrice": 1000000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1000000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Misc_CeremonialSword",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "A50A59860E2F475CB46C776EA16A9250",
          "devName": "SecretShop.Page02.Reagent.08",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 300000,
              "dynamicRegularPrice": -1,
              "finalPrice": 255000,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 255000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Light",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "76CBD78B01034CCFBDC0A86F87A8203A",
          "devName": "SecretShop.Page02.Reagent.11",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 300000,
              "dynamicRegularPrice": -1,
              "finalPrice": 255000,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 255000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Dark",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "0034B9FAC6B940D787AC0B309C551AA3",
          "devName": "SecretShop.Page02.Elixir.06",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 25,
              "dynamicRegularPrice": -1,
              "finalPrice": 25,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 25
            }
          ],
          "categories": [],
          "dailyLimit": 5,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "1C180861BD96443BBBC51351FB655EE8",
          "devName": "SecretShop.Page02.Elixir.03",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 400000,
              "dynamicRegularPrice": -1,
              "finalPrice": 340000,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 340000
            }
          ],
          "categories": [],
          "dailyLimit": 2,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "BA66F5FA024E47ABA1B1DE2898AFAB3A",
          "devName": "SecretShop.Page02.Free.04",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 20000,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 10,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "TreasureMap:TM_MapResource",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "92C100EEB06F451D82094FEC7F292AE9",
          "devName": "SecretShop.Page02.Reagent.10",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 300000,
              "dynamicRegularPrice": -1,
              "finalPrice": 255000,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 255000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Nature",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "8B8FE8A9518C49099287DD050EE9060C",
          "devName": "SecretShop.Page02.Ore.01",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 25000,
              "dynamicRegularPrice": -1,
              "finalPrice": 21250,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 21250
            }
          ],
          "categories": [],
          "dailyLimit": 3,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Ore:Ore_Magicite",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "2A3419700FA94A819F6D2527ACD21B45",
          "devName": "SecretShop.Page02.Shard.08",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 200,
              "dynamicRegularPrice": -1,
              "finalPrice": 170,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 170
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Light",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "1A85EEF6D7D547129815F8EEA509C2EC",
          "devName": "SecretShop.Page02.UnderworldTraderGold.01",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 2500,
              "dynamicRegularPrice": -1,
              "finalPrice": 1500,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1500
            }
          ],
          "categories": [],
          "dailyLimit": 30,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "VipLevelMin",
              "value": "3"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shared_T02",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "1D2AA266C8044755985B24C5969205D8",
          "devName": "SecretShop.Page02.UnderworldTrader.16",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 200,
              "dynamicRegularPrice": -1,
              "finalPrice": 170,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 170
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "VipLevelMin",
              "value": "3"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Light",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "3677B9EA1CB3452EB8C230AB8805CD69",
          "devName": "SecretShop.Page02.UnderworldTrader.15",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 200,
              "dynamicRegularPrice": -1,
              "finalPrice": 170,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 170
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "VipLevelMin",
              "value": "3"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Fire",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "DDCEB10173F8441B99603CED9EEBCB6E",
          "devName": "SecretShop.Page02.UnderworldTrader.19",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": 40,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "VipLevelMin",
              "value": "3"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shared_T02",
              "quantity": 1
            }
          ]
        }
      ]
    },
    {
      "name": "WeeklyChallenge",
      "catalogEntries": [
        {
          "offerId": "9D1888E891BD43AB9DA003D288880200",
          "devName": "WeeklyChallenge.WCStore.12",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:WCCoins",
              "regularPrice": 5,
              "dynamicRegularPrice": -1,
              "finalPrice": 5,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": 5,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 99,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_WC_Hero_TripleCombo",
              "quantity": 4
            }
          ]
        },
        {
          "offerId": "373A66DDC30E4CDE8E9554C596654D41",
          "devName": "WeeklyChallenge.WCStore.10",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:WCCoins",
              "regularPrice": 40,
              "dynamicRegularPrice": -1,
              "finalPrice": 40,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 40
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": 3,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 40,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 100
            }
          ]
        },
        {
          "offerId": "0E116A56E39E435799ED39B090E21676",
          "devName": "WeeklyChallenge.WCStore.13",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:WCCoins",
              "regularPrice": 5,
              "dynamicRegularPrice": -1,
              "finalPrice": 5,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": 12,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 100,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Token:TK_Voucher_HeroBattle",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "C4C98274DEB14C21B56C5D3C13CEEC0C",
          "devName": "WeeklyChallenge.WCStore.04",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:WCCoins",
              "regularPrice": 5,
              "dynamicRegularPrice": -1,
              "finalPrice": 5,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": 5,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 10,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Nature",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "58A2382E60FF4D3991084DF21FA1483B",
          "devName": "WeeklyChallenge.WCStore.02",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:WCCoins",
              "regularPrice": 5,
              "dynamicRegularPrice": -1,
              "finalPrice": 2,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 2
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": 20,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 75,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Currency:SkillXP",
              "quantity": 100
            }
          ]
        },
        {
          "offerId": "F8489AEE810640B9A35538FA4F09C70D",
          "devName": "WeeklyChallenge.WCStore.09",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:WCCoins",
              "regularPrice": 5,
              "dynamicRegularPrice": -1,
              "finalPrice": 5,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": 15,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 50,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Ore:Ore_Magicite",
              "quantity": 10
            }
          ]
        },
        {
          "offerId": "398723C11EFD41B3A0BDC06CF004DFFD",
          "devName": "WeeklyChallenge.WCStore.05",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:WCCoins",
              "regularPrice": 5,
              "dynamicRegularPrice": -1,
              "finalPrice": 5,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": 5,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 10,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Water",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "10DA3DE368464C318176A75C2C3E7E93",
          "devName": "WeeklyChallenge.WCStore.08",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:WCCoins",
              "regularPrice": 50,
              "dynamicRegularPrice": -1,
              "finalPrice": 50,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 50
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": 1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 101,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Currency:MtxGiveaway",
              "quantity": 200
            }
          ]
        },
        {
          "offerId": "87ED883B16D642DD9BA19ACE31FC3948",
          "devName": "WeeklyChallenge.WCStore.07",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:WCCoins",
              "regularPrice": 5,
              "dynamicRegularPrice": -1,
              "finalPrice": 5,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": 5,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 10,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Dark",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "47296335F3D34052AED9B0B767C23687",
          "devName": "WeeklyChallenge.WCStore.03",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:WCCoins",
              "regularPrice": 5,
              "dynamicRegularPrice": -1,
              "finalPrice": 5,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": 5,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 10,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Fire",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "4E70CCEAF17741D7ABFF418EE6CBEFE9",
          "devName": "WeeklyChallenge.WCStore.06",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:WCCoins",
              "regularPrice": 5,
              "dynamicRegularPrice": -1,
              "finalPrice": 5,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": 5,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 10,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Light",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "F574035687484FD8BFEE2D967605F9E3",
          "devName": "WeeklyChallenge.WCStore.01",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:WCCoins",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": 100,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 75,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shared_T02",
              "quantity": 5
            }
          ]
        },
        {
          "offerId": "5AB9FCAC16A84AA8B48196DEF5B939D8",
          "devName": "WeeklyChallenge.WCStore.11",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:WCCoins",
              "regularPrice": 5,
              "dynamicRegularPrice": -1,
              "finalPrice": 5,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": 10,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 60,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Misc_CeremonialSword",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "45EC4E0C917949938D50E24F19870EB9",
          "devName": "WeeklyChallenge.WCStore.14",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:WCCoins",
              "regularPrice": 20,
              "dynamicRegularPrice": -1,
              "finalPrice": 20,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 20
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": 1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "48268FEC4038F934733109AFAE874A71",
              "minQuantity": 1
            }
          ],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 41,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "/Game/Characters/Classes/Assassin/Multi_Slasher/CD_Assassin_R2_Nature_Slasher_T03.CD_Assassin_R2_Nature_Slasher_T03",
          "itemGrants": [
            {
              "templateId": "Character:Assassin_R2_Nature_Slasher_T03",
              "quantity": 1
            }
          ]
        }
      ]
    },
    {
      "name": "HeroStore",
      "catalogEntries": [
        {
          "devName": "[VIRTUAL]1 x Night Hunter Lana for 2000 GameItem : Reagent:Reagent_Hero_Event",
          "offerId": "virtual:/1i158746eh4k7p47okhaog3c91[0]1#0",
          "fulfillmentIds": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": 2,
          "categories": [],
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Hero_Event",
              "regularPrice": 2000,
              "dynamicRegularPrice": 2000,
              "finalPrice": 2000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 2000
            }
          ],
          "meta": {
            "bIsNewHero": "FALSE",
            "bIsSpecialHero": "FALSE"
          },
          "matchFilter": "",
          "filterWeight": 0.0,
          "appStoreId": [],
          "requirements": [],
          "offerType": "StaticPrice",
          "refundable": false,
          "metaInfo": [
            {
              "key": "bIsNewHero",
              "value": "FALSE"
            },
            {
              "key": "bIsSpecialHero",
              "value": "FALSE"
            }
          ],
          "itemGrants": [
            {
              "templateId": "Character:Blademaster_VR2_Water_SilverWhip_T04",
              "quantity": 1
            }
          ],
          "additionalGrants": [],
          "sortPriority": 120,
          "catalogGroupPriority": 0
        },
        {
          "devName": "[VIRTUAL]1 x Arte Plein for 100 GameItem : Reagent:Reagent_SupplyPoints_Elite",
          "offerId": "virtual:/1i158746eh4k7p47okhaog3c91[0]1#1",
          "fulfillmentIds": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": 2,
          "categories": [],
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_SupplyPoints_Elite",
              "regularPrice": 100,
              "dynamicRegularPrice": 100,
              "finalPrice": 100,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 100
            }
          ],
          "meta": {
            "bIsNewHero": "FALSE",
            "bIsSpecialHero": "FALSE"
          },
          "matchFilter": "",
          "filterWeight": 0.0,
          "appStoreId": [],
          "requirements": [],
          "offerType": "StaticPrice",
          "refundable": false,
          "metaInfo": [
            {
              "key": "bIsNewHero",
              "value": "FALSE"
            },
            {
              "key": "bIsSpecialHero",
              "value": "FALSE"
            }
          ],
          "itemGrants": [
            {
              "templateId": "Character:Pet_VR2_FlyByNight_Light_T04",
              "quantity": 1
            }
          ],
          "additionalGrants": [],
          "sortPriority": 20,
          "catalogGroupPriority": 0
        },
        {
          "offerId": "FC9F55324B665622C6E85D987C5DE358",
          "devName": "Fire Cloudpuff 2",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_SupplyPoints_Elite",
              "regularPrice": 800,
              "dynamicRegularPrice": -1,
              "finalPrice": 800,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 800
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "F15984F442336A13D30447B2C57DD7AA",
              "minQuantity": 2
            },
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "E3069A27428C5C1D05892DA6244406B4",
              "minQuantity": 2
            }
          ],
          "metaInfo": [
            {
              "key": "AccountLevelMin",
              "value": "200"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 31,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Character:Pet_SR1_Cloudpuff_Fire_T05",
              "quantity": 1
            }
          ]
        },
        {
          "devName": "[VIRTUAL]1 x Flame the Raccoon for -1 GameItem : Reagent:Reagent_SupplyPoints_Elite",
          "offerId": "virtual:/00ig9fpo66b4605vafo7jvidec[0]191#12",
          "fulfillmentIds": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": 2,
          "categories": [],
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_SupplyPoints_Elite",
              "regularPrice": 100,
              "dynamicRegularPrice": 100,
              "finalPrice": 100,
              "saleType": "Strikethrough",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 100
            }
          ],
          "meta": {},
          "matchFilter": "",
          "filterWeight": 0.0,
          "appStoreId": [],
          "requirements": [],
          "offerType": "StaticPrice",
          "refundable": false,
          "itemGrants": [
            {
              "templateId": "Character:Pet_SR1_Fire_InfernoRacoon_T05",
              "quantity": 1
            }
          ],
          "additionalGrants": [],
          "sortPriority": 30,
          "catalogGroupPriority": 0
        },
        {
          "devName": "[VIRTUAL]1 x Painguin for -1 GameItem : Reagent:Reagent_SupplyPoints_Elite",
          "offerId": "virtual:/00ig9fpo66b4605vafo7jvidec[0]191#13",
          "fulfillmentIds": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": 2,
          "categories": [],
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_SupplyPoints_Elite",
              "regularPrice": 50,
              "dynamicRegularPrice": 50,
              "finalPrice": 50,
              "saleType": "Strikethrough",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 50
            }
          ],
          "meta": {},
          "matchFilter": "",
          "filterWeight": 0.0,
          "appStoreId": [],
          "requirements": [],
          "offerType": "StaticPrice",
          "refundable": false,
          "itemGrants": [
            {
              "templateId": "Character:Pet_UC1_Painguin_Water_T03",
              "quantity": 1
            }
          ],
          "additionalGrants": [],
          "sortPriority": 20,
          "catalogGroupPriority": 0
        },
        {
          "devName": "[VIRTUAL]1 x Commander Shorty for -1 GameItem : Reagent:Reagent_SupplyPoints_Elite",
          "offerId": "virtual:/00ig9fpo66b4605vafo7jvidec[0]191#10",
          "fulfillmentIds": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": 2,
          "categories": [],
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_SupplyPoints_Elite",
              "regularPrice": 100,
              "dynamicRegularPrice": 100,
              "finalPrice": 100,
              "saleType": "Strikethrough",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 100
            }
          ],
          "meta": {},
          "matchFilter": "",
          "filterWeight": 0.0,
          "appStoreId": [],
          "requirements": [],
          "offerType": "StaticPrice",
          "refundable": false,
          "itemGrants": [
            {
              "templateId": "Character:Pet_SR2_Fire_Corgi_T05",
              "quantity": 1
            }
          ],
          "additionalGrants": [],
          "sortPriority": 30,
          "catalogGroupPriority": 0
        },
        {
          "devName": "[VIRTUAL]1 x Rain Deer for -1 GameItem : Reagent:Reagent_SupplyPoints_Elite",
          "offerId": "virtual:/00ig9fpo66b4605vafo7jvidec[0]191#11",
          "fulfillmentIds": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": 2,
          "categories": [],
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_SupplyPoints_Elite",
              "regularPrice": 100,
              "dynamicRegularPrice": 100,
              "finalPrice": 100,
              "saleType": "Strikethrough",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 100
            }
          ],
          "meta": {},
          "matchFilter": "",
          "filterWeight": 0.0,
          "appStoreId": [],
          "requirements": [],
          "offerType": "StaticPrice",
          "refundable": false,
          "itemGrants": [
            {
              "templateId": "Character:Pet_VR2_Reindeer_Water_T04",
              "quantity": 1
            }
          ],
          "additionalGrants": [],
          "sortPriority": 30,
          "catalogGroupPriority": 0
        },
        {
          "devName": "[VIRTUAL]1 x Kurohomura for -1 GameItem : Reagent:Reagent_Hero_Event",
          "offerId": "virtual:/00ig9fpo66b4605vafo7jvidec[0]191#0",
          "fulfillmentIds": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": 2,
          "categories": [],
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Hero_Event",
              "regularPrice": 5000,
              "dynamicRegularPrice": 5000,
              "finalPrice": 5000,
              "saleType": "Strikethrough",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5000
            }
          ],
          "meta": {},
          "matchFilter": "",
          "filterWeight": 0.0,
          "appStoreId": [],
          "requirements": [],
          "offerType": "StaticPrice",
          "refundable": false,
          "itemGrants": [
            {
              "templateId": "Character:MartialArtist_SR2_Fire_SeveringBlow_T05",
              "quantity": 1
            }
          ],
          "additionalGrants": [],
          "sortPriority": 120,
          "catalogGroupPriority": 0
        },
        {
          "offerId": "90106DE84F9DD0698624BDA0B515F7B6",
          "devName": "Dark Cloudpuff 1",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_SupplyPoints_Elite",
              "regularPrice": 800,
              "dynamicRegularPrice": -1,
              "finalPrice": 800,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 800
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "BD6B06874A8AEA8FD6EF89A3F43F489F",
              "minQuantity": 1
            },
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "C4A82E024E03977BE786D09365878807",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "AccountLevelMin",
              "value": "200"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 31,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Character:Pet_SR1_Cloudpuff_Dark_T05",
              "quantity": 1
            }
          ]
        },
        {
          "devName": "[VIRTUAL]1 x Noble Ward Mirra for -1 GameItem : Reagent:Reagent_Hero_Event",
          "offerId": "virtual:/00ig9fpo66b4605vafo7jvidec[0]191#3",
          "fulfillmentIds": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": 2,
          "categories": [],
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Hero_Event",
              "regularPrice": 2000,
              "dynamicRegularPrice": 2000,
              "finalPrice": 2000,
              "saleType": "Strikethrough",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 2000
            }
          ],
          "meta": {},
          "matchFilter": "",
          "filterWeight": 0.0,
          "appStoreId": [],
          "requirements": [],
          "offerType": "StaticPrice",
          "refundable": false,
          "itemGrants": [
            {
              "templateId": "Character:Warrior_VR1_Light_Deflect_T04",
              "quantity": 1
            }
          ],
          "additionalGrants": [],
          "sortPriority": 110,
          "catalogGroupPriority": 0
        },
        {
          "devName": "[VIRTUAL]1 x Beastman Champion for -1 GameItem : Reagent:Reagent_Hero_Event",
          "offerId": "virtual:/00ig9fpo66b4605vafo7jvidec[0]191#4",
          "fulfillmentIds": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": 2,
          "categories": [],
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Hero_Event",
              "regularPrice": 2000,
              "dynamicRegularPrice": 2000,
              "finalPrice": 2000,
              "saleType": "Strikethrough",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 2000
            }
          ],
          "meta": {},
          "matchFilter": "",
          "filterWeight": 0.0,
          "appStoreId": [],
          "requirements": [],
          "offerType": "StaticPrice",
          "refundable": false,
          "itemGrants": [
            {
              "templateId": "Character:Warrior_VR2_Dark_Rampage_T04",
              "quantity": 1
            }
          ],
          "additionalGrants": [],
          "sortPriority": 110,
          "catalogGroupPriority": 0
        },
        {
          "devName": "[VIRTUAL]1 x Kumiho the Fox for -1 GameItem : Reagent:Reagent_Hero_Event",
          "offerId": "virtual:/00ig9fpo66b4605vafo7jvidec[0]191#1",
          "fulfillmentIds": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": 2,
          "categories": [],
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Hero_Event",
              "regularPrice": 2000,
              "dynamicRegularPrice": 2000,
              "finalPrice": 2000,
              "saleType": "Strikethrough",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 2000
            }
          ],
          "meta": {},
          "matchFilter": "",
          "filterWeight": 0.0,
          "appStoreId": [],
          "requirements": [],
          "offerType": "StaticPrice",
          "refundable": false,
          "itemGrants": [
            {
              "templateId": "Character:Assassin_VR1_Fire_HiddenStrike_T04",
              "quantity": 1
            }
          ],
          "additionalGrants": [],
          "sortPriority": 110,
          "catalogGroupPriority": 0
        },
        {
          "offerId": "E02009F74D1498D74D16B3B8B5E0D21C",
          "devName": "Nature Cloudpuff 1",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_SupplyPoints_Elite",
              "regularPrice": 800,
              "dynamicRegularPrice": -1,
              "finalPrice": 800,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 800
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "8772B1374685F66D9F9B54A0A3C026B5",
              "minQuantity": 1
            }
          ],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 31,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Character:Pet_SR1_Cloudpuff_Nature_T05",
              "quantity": 1
            }
          ]
        },
        {
          "devName": "[VIRTUAL]1 x Jarellia the Feral for -1 GameItem : Reagent:Reagent_Hero_Event",
          "offerId": "virtual:/00ig9fpo66b4605vafo7jvidec[0]191#2",
          "fulfillmentIds": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": 2,
          "categories": [],
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Hero_Event",
              "regularPrice": 2000,
              "dynamicRegularPrice": 2000,
              "finalPrice": 2000,
              "saleType": "Strikethrough",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 2000
            }
          ],
          "meta": {},
          "matchFilter": "",
          "filterWeight": 0.0,
          "appStoreId": [],
          "requirements": [],
          "offerType": "StaticPrice",
          "refundable": false,
          "itemGrants": [
            {
              "templateId": "Character:Cleric_VR2_Nature_FeralStrike_T04",
              "quantity": 1
            }
          ],
          "additionalGrants": [],
          "sortPriority": 110,
          "catalogGroupPriority": 0
        },
        {
          "devName": "[VIRTUAL]1 x Heavenguard Kaleb for -1 GameItem : Reagent:Reagent_Hero_Event",
          "offerId": "virtual:/00ig9fpo66b4605vafo7jvidec[0]191#7",
          "fulfillmentIds": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": 2,
          "categories": [],
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Hero_Event",
              "regularPrice": 800,
              "dynamicRegularPrice": 800,
              "finalPrice": 800,
              "saleType": "Strikethrough",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 800
            }
          ],
          "meta": {},
          "matchFilter": "",
          "filterWeight": 0.0,
          "appStoreId": [],
          "requirements": [],
          "offerType": "StaticPrice",
          "refundable": false,
          "itemGrants": [
            {
              "templateId": "Character:HolyKnight_R1_Light_Resurrect_T03",
              "quantity": 1
            }
          ],
          "additionalGrants": [],
          "sortPriority": 100,
          "catalogGroupPriority": 0
        },
        {
          "devName": "[VIRTUAL]1 x Mechshade Dagen for -1 GameItem : Reagent:Reagent_Hero_Event",
          "offerId": "virtual:/00ig9fpo66b4605vafo7jvidec[0]191#8",
          "fulfillmentIds": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": 2,
          "categories": [],
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Hero_Event",
              "regularPrice": 800,
              "dynamicRegularPrice": 800,
              "finalPrice": 800,
              "saleType": "Strikethrough",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 800
            }
          ],
          "meta": {},
          "matchFilter": "",
          "filterWeight": 0.0,
          "appStoreId": [],
          "requirements": [],
          "offerType": "StaticPrice",
          "refundable": false,
          "itemGrants": [
            {
              "templateId": "Character:Ninja_UC1_Fire_SwiftStrike_T03",
              "quantity": 1
            }
          ],
          "additionalGrants": [],
          "sortPriority": 100,
          "catalogGroupPriority": 0
        },
        {
          "offerId": "BFF081A44C9D7D7EDA18269F1ACC2CFD",
          "devName": "Dark Cloudpuff 2",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_SupplyPoints_Elite",
              "regularPrice": 800,
              "dynamicRegularPrice": -1,
              "finalPrice": 800,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 800
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "BD6B06874A8AEA8FD6EF89A3F43F489F",
              "minQuantity": 2
            },
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "C4A82E024E03977BE786D09365878807",
              "minQuantity": 2
            }
          ],
          "metaInfo": [
            {
              "key": "AccountLevelMin",
              "value": "200"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 31,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Character:Pet_SR1_Cloudpuff_Dark_T05",
              "quantity": 1
            }
          ]
        },
        {
          "devName": "[VIRTUAL]1 x Ejo The Messenger for -1 GameItem : Reagent:Reagent_Hero_Event",
          "offerId": "virtual:/00ig9fpo66b4605vafo7jvidec[0]191#5",
          "fulfillmentIds": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": 2,
          "categories": [],
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Hero_Event",
              "regularPrice": 2000,
              "dynamicRegularPrice": 2000,
              "finalPrice": 2000,
              "saleType": "Strikethrough",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 2000
            }
          ],
          "meta": {},
          "matchFilter": "",
          "filterWeight": 0.0,
          "appStoreId": [],
          "requirements": [],
          "offerType": "StaticPrice",
          "refundable": false,
          "itemGrants": [
            {
              "templateId": "Character:SpiritWarrior_VR2_Light_KindFist_T04",
              "quantity": 1
            }
          ],
          "additionalGrants": [],
          "sortPriority": 110,
          "catalogGroupPriority": 0
        },
        {
          "devName": "[VIRTUAL]1 x Kunoichi Melina for -1 GameItem : Reagent:Reagent_Hero_Event",
          "offerId": "virtual:/00ig9fpo66b4605vafo7jvidec[0]191#6",
          "fulfillmentIds": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": 2,
          "categories": [],
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Hero_Event",
              "regularPrice": 800,
              "dynamicRegularPrice": 800,
              "finalPrice": 800,
              "saleType": "Strikethrough",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 800
            }
          ],
          "meta": {},
          "matchFilter": "",
          "filterWeight": 0.0,
          "appStoreId": [],
          "requirements": [],
          "offerType": "StaticPrice",
          "refundable": false,
          "itemGrants": [
            {
              "templateId": "Character:Ninja_R2_Water_TripleStab_T03",
              "quantity": 1
            }
          ],
          "additionalGrants": [],
          "sortPriority": 100,
          "catalogGroupPriority": 0
        },
        {
          "offerId": "F74CDC054D2A0F40EC89B6915936EF8E",
          "devName": "Fire Cloudpuff 1",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_SupplyPoints_Elite",
              "regularPrice": 800,
              "dynamicRegularPrice": -1,
              "finalPrice": 800,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 800
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "F15984F442336A13D30447B2C57DD7AA",
              "minQuantity": 1
            },
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "E3069A27428C5C1D05892DA6244406B4",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "AccountLevelMin",
              "value": "100"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 31,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Character:Pet_SR1_Cloudpuff_Fire_T05",
              "quantity": 1
            }
          ]
        },
        {
          "devName": "[VIRTUAL]1 x Ancient Pact Palgrus for -1 GameItem : Reagent:Reagent_SupplyPoints_Elite",
          "offerId": "virtual:/00ig9fpo66b4605vafo7jvidec[0]191#9",
          "fulfillmentIds": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": 2,
          "categories": [],
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_SupplyPoints_Elite",
              "regularPrice": 200,
              "dynamicRegularPrice": 200,
              "finalPrice": 200,
              "saleType": "Strikethrough",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 200
            }
          ],
          "meta": {},
          "matchFilter": "",
          "filterWeight": 0.0,
          "appStoreId": [],
          "requirements": [],
          "offerType": "StaticPrice",
          "refundable": false,
          "itemGrants": [
            {
              "templateId": "Character:Pet_SR1_Palgrus_Light_T05",
              "quantity": 1
            }
          ],
          "additionalGrants": [],
          "sortPriority": 40,
          "catalogGroupPriority": 0
        },
        {
          "offerId": "839D87504767FFC769757B978FE78604",
          "devName": "Nature Cloudpuff 2",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_SupplyPoints_Elite",
              "regularPrice": 800,
              "dynamicRegularPrice": -1,
              "finalPrice": 800,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 800
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "8772B1374685F66D9F9B54A0A3C026B5",
              "minQuantity": 2
            },
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "BD6B06874A8AEA8FD6EF89A3F43F489F",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "AccountLevelMin",
              "value": "200"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 31,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Character:Pet_SR1_Cloudpuff_Nature_T05",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "3CC5B90E4322D33C641808A14CF2A6CE",
          "devName": "Light Cloudpuff 1",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_SupplyPoints_Elite",
              "regularPrice": 800,
              "dynamicRegularPrice": -1,
              "finalPrice": 800,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 800
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "E3069A27428C5C1D05892DA6244406B4",
              "minQuantity": 1
            },
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "8772B1374685F66D9F9B54A0A3C026B5",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "AccountLevelMin",
              "value": "50"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 31,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Character:Pet_SR1_Cloudpuff_Light_T05",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "C1C466504D2FE8078ACBD99E3C086AED",
          "devName": "Water Cloudpuff 2",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_SupplyPoints_Elite",
              "regularPrice": 800,
              "dynamicRegularPrice": -1,
              "finalPrice": 800,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 800
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "C4A82E024E03977BE786D09365878807",
              "minQuantity": 2
            },
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "F15984F442336A13D30447B2C57DD7AA",
              "minQuantity": 2
            }
          ],
          "metaInfo": [
            {
              "key": "AccountLevelMin",
              "value": "200"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 31,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Character:Pet_SR1_Cloudpuff_Water_T05",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "77BE70724F1603F9475694ADCA777E6A",
          "devName": "Water Cloudpuff 1",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_SupplyPoints_Elite",
              "regularPrice": 800,
              "dynamicRegularPrice": -1,
              "finalPrice": 800,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 800
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "C4A82E024E03977BE786D09365878807",
              "minQuantity": 1
            },
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "F15984F442336A13D30447B2C57DD7AA",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "AccountLevelMin",
              "value": "150"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 31,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Character:Pet_SR1_Cloudpuff_Water_T05",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "93CD385542C69DD7E6760D9D7E726CFA",
          "devName": "Light Cloudpuff 2",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_SupplyPoints_Elite",
              "regularPrice": 800,
              "dynamicRegularPrice": -1,
              "finalPrice": 800,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 800
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "E3069A27428C5C1D05892DA6244406B4",
              "minQuantity": 2
            },
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "8772B1374685F66D9F9B54A0A3C026B5",
              "minQuantity": 2
            }
          ],
          "metaInfo": [
            {
              "key": "AccountLevelMin",
              "value": "200"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 31,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Character:Pet_SR1_Cloudpuff_Light_T05",
              "quantity": 1
            }
          ]
        }
      ]
    },
    {
      "name": "Featured",
      "catalogEntries": [
        {
          "offerId": "DB5F94D05FA24D208D3A449C39EEA5EA",
          "devName": "StorefrontStacked.Page01.ElementalHeroes.445",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 500,
              "dynamicRegularPrice": -1,
              "finalPrice": 500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 500
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "Type",
              "value": "ElementalHero"
            },
            {
              "key": "HideQuantityRemaining",
              "value": "True"
            }
          ],
          "catalogGroup": "ElementalHeroes",
          "catalogGroupPriority": 445,
          "sortPriority": 72,
          "title": "Elemental Heroes",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 140
            },
            {
              "templateId": "Currency:Hammer",
              "quantity": 4
            },
            {
              "templateId": "TreasureMap:TM_MapResource",
              "quantity": 40
            },
            {
              "templateId": "TreasureMap:TM_Special_BridgeOfLight",
              "quantity": 1
            },
            {
              "templateId": "Reagent:Reagent_Shard_Fire",
              "quantity": 1
            },
            {
              "templateId": "Reagent:Reagent_Shared_T02",
              "quantity": 35
            }
          ]
        },
        {
          "offerId": "DE6872CA4BA847BFA6FF8625D48EA5C2",
          "devName": "StorefrontStacked.Page01.ElementalHeroes.366",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 500,
              "dynamicRegularPrice": -1,
              "finalPrice": 500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 500
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "Type",
              "value": "ElementalHero"
            },
            {
              "key": "HideQuantityRemaining",
              "value": "True"
            }
          ],
          "catalogGroup": "ElementalHeroes",
          "catalogGroupPriority": 366,
          "sortPriority": 72,
          "title": "Elemental Heroes",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 140
            },
            {
              "templateId": "Currency:Hammer",
              "quantity": 4
            },
            {
              "templateId": "TreasureMap:TM_OvergrownCastle_Map8",
              "quantity": 1
            },
            {
              "templateId": "Reagent:Reagent_Shared_T02",
              "quantity": 35
            },
            {
              "templateId": "Currency:SkillXP",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 15
            }
          ]
        },
        {
          "offerId": "308A41F23E4A4AC79AD9C9ADEF517D0A",
          "devName": "StorefrontMtx.L370000.MtxGift.36",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "44BB81AA4D528D13F5B64F857A30D41A",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "CD425F9A4614451770592D976A9CB72A",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "370000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 48",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "BE0A976B8D4A43DF83B18EEC0C5D6888",
          "devName": "StorefrontMtx.L440000.MtxGift.44",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "621ED4A24CF22364662C8B86D5681DBB",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "15B714264A35B80083536D821A2C9203",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "440000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 55",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "4EF045C2E40C4E228D0BA34B69520227",
          "devName": "StorefrontMtx.L980000.MtxGift.110",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "FB4E32F849408CFC50038494DF0B371C",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "8F30DCC84E3D5ACB54275796E2D75E5B",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "980000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 109",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "0E4C27E5A11F4C00BD402FCBEC94DB96",
          "devName": "StorefrontMtx.L950000.MtxGift.107",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "4C16D22849A940EFD2805FA3770F4289",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "9D90D9D043CA0596F6266EB2C3DC9C64",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "950000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 106",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "C23FF150D2AF4E2CABE0BC052E8FAFF0",
          "devName": "StorefrontLevel.L550000.LevelUpChest.27",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 5000,
              "dynamicRegularPrice": -1,
              "finalPrice": 5000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "92077EB243071AD9F0E7A2B5F2F71D7F",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "8A2CF2B442B4177565F52196364A120F",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "StoreLevelMin",
              "value": "550000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 60,
          "title": "Super Magic Chest",
          "shortDescription": "",
          "description": "A Diamond Hero Crystal, 5000 Magic Tickets and 8 items!",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 5000
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 100
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_SupplyPoints_Elite",
              "quantity": 200
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 10
            }
          ]
        },
        {
          "offerId": "FA23253B9D024B658F57FF2CA2548EA1",
          "devName": "StorefrontMtx.L60000.MtxGift.64",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "E83060694EC9CA80654B84AF64340D5D",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "014262EC477B66DE83109CA381FED5AD",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "60000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 13",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "BC59DAB14818A2910F892BBBEB77772F",
          "devName": "Kailani (Light)",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Voucher:Voucher_Hero_Blademaster_Light_Bladestorm",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "AffordOnly",
              "value": "true"
            },
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Hero.B_StoreButton_Hero'"
            },
            {
              "key": "type",
              "value": "Random"
            },
            {
              "key": "AutoRedeem",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 9999,
          "title": "Kailani",
          "shortDescription": "",
          "description": "Free Kailani from her crystal!",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Character:Blademaster_VR1_Light_BladeStorm_T04",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "DA4FAC9829FD4E3197E2E46E33EADBF7",
          "devName": "StorefrontMtx.L5000.MtxGift.51",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "0C425A7840E80B644949B2AD5291BD98",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "1E024004419DCE5D80EBC9B0A07D5957",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "5000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 2",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "AEDFBC344E6D551E9F25728FFD343012",
          "devName": "Elemental Hero Resources",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 500,
              "dynamicRegularPrice": -1,
              "finalPrice": 500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 500
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "type",
              "value": "ElementalHero"
            }
          ],
          "catalogGroup": "ElementalHeroes",
          "catalogGroupPriority": 0,
          "sortPriority": 72,
          "title": "Elemental Heroes",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 140
            },
            {
              "templateId": "Currency:Hammer",
              "quantity": 4
            },
            {
              "templateId": "Reagent:Reagent_Misc_CeremonialSword",
              "quantity": 2
            },
            {
              "templateId": "Currency:Gold",
              "quantity": 100000
            },
            {
              "templateId": "TreasureMap:TM_MapResource",
              "quantity": 10
            },
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "38BC8BF259A743158704262464691EC2",
          "devName": "StorefrontMtx.L520000.MtxGift.55",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "06EED93D416CC285D8F887BA31411157",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "131F08B046089B1F82D8B5AF558E8742",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "520000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 63",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "30F1E03644EF73FDE0776CB66B3AA586",
          "devName": "12HR Basic Chest (Silver) - 25",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 100,
              "dynamicRegularPrice": -1,
              "finalPrice": 25,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 25
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "DAILYCHEST",
              "value": "true"
            },
            {
              "key": "type",
              "value": "dailylootbox"
            },
            {
              "key": "AccountLevelMin",
              "value": "4"
            },
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles_Small.B_StoreButton_Bundles_Small'"
            }
          ],
          "catalogGroup": "Silver Chest",
          "catalogGroupPriority": 3,
          "sortPriority": 115,
          "title": "12hr Basic Chest",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 100
            },
            {
              "templateId": "Currency:Hammer",
              "quantity": 4
            }
          ]
        },
        {
          "offerId": "895D55BC580D48C9A5F72BD615057E6B",
          "devName": "StorefrontStacked.Page01.ElementalHeroes.447",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 500,
              "dynamicRegularPrice": -1,
              "finalPrice": 500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 500
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "Type",
              "value": "ElementalHero"
            },
            {
              "key": "HideQuantityRemaining",
              "value": "True"
            }
          ],
          "catalogGroup": "ElementalHeroes",
          "catalogGroupPriority": 447,
          "sortPriority": 72,
          "title": "Elemental Heroes",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 140
            },
            {
              "templateId": "Currency:Hammer",
              "quantity": 4
            },
            {
              "templateId": "Currency:Hammer",
              "quantity": 7
            },
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 100
            },
            {
              "templateId": "TreasureMap:TM_MapResource",
              "quantity": 10
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 2
            }
          ]
        },
        {
          "offerId": "D654B24038F54728B460219036D8F180",
          "devName": "StorefrontLevel.L370000.LevelUpChest.17",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 5000,
              "dynamicRegularPrice": -1,
              "finalPrice": 5000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "9599934D4B2CFBC377CB67AB131F6B6B",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "4685928D450EBBA5B93598A2F37CFFF6",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "StoreLevelMin",
              "value": "370000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 60,
          "title": "Super Magic Chest",
          "shortDescription": "",
          "description": "A Diamond Hero Crystal, 5000 Magic Tickets and 8 items!",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 5000
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 100
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_SupplyPoints_Elite",
              "quantity": 200
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 10
            }
          ]
        },
        {
          "offerId": "F002805939174124BF0C0F6AF5D2ED67",
          "devName": "StorefrontMtx.L290000.MtxGift.26",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "267A66044012B4293233CDB9199F91B2",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "F121FD584020B3BB4215BFB6C2723B63",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "290000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 40",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "F69DDAA3D24F4ED394D8E8EEDE7C7E67",
          "devName": "StorefrontMtx.L310000.MtxGift.29",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "24422CC946D4BBEF26BD38B1E8D4F1AB",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "4EB892244CC62635C6631D97E8A4DDAD",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "310000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 42",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "E5D2E934D62A436884C0A92D4168CD50",
          "devName": "StorefrontStacked.Page01.ElementalHeroes.369",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 500,
              "dynamicRegularPrice": -1,
              "finalPrice": 500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 500
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "Type",
              "value": "ElementalHero"
            },
            {
              "key": "HideQuantityRemaining",
              "value": "True"
            }
          ],
          "catalogGroup": "ElementalHeroes",
          "catalogGroupPriority": 369,
          "sortPriority": 72,
          "title": "Elemental Heroes",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 140
            },
            {
              "templateId": "Currency:Hammer",
              "quantity": 4
            },
            {
              "templateId": "Reagent:Reagent_Shard_Nature",
              "quantity": 5
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 4
            },
            {
              "templateId": "Currency:Gold",
              "quantity": 100000
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 3
            }
          ]
        },
        {
          "offerId": "0381F2F8D4CE42A788BFC3A203E6D722",
          "devName": "StorefrontStacked.Page01.ElementalHeroes.241",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 500,
              "dynamicRegularPrice": -1,
              "finalPrice": 500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 500
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "Type",
              "value": "ElementalHero"
            },
            {
              "key": "HideQuantityRemaining",
              "value": "True"
            }
          ],
          "catalogGroup": "ElementalHeroes",
          "catalogGroupPriority": 241,
          "sortPriority": 72,
          "title": "Elemental Heroes",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 140
            },
            {
              "templateId": "Currency:Hammer",
              "quantity": 4
            },
            {
              "templateId": "Ore:Ore_Magicite",
              "quantity": 25
            },
            {
              "templateId": "Reagent:Reagent_Shard_Water",
              "quantity": 1
            },
            {
              "templateId": "TreasureMap:TM_WaterfallValley_Map7",
              "quantity": 1
            },
            {
              "templateId": "Reagent:WCCoins",
              "quantity": 5
            }
          ]
        },
        {
          "offerId": "8B935496EDA84D2C8E1FDF67A11563D5",
          "devName": "StorefrontMtx.L340000.MtxGift.32",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "68F61AF9403A19EE7CB6B38B33A64EFE",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "4A66472743F146E7160266946FD8A5D2",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "340000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 45",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "C53D402C9561495AB8EF51A566FD3281",
          "devName": "StorefrontMtx.L470000.MtxGift.48",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "45A93AE643E53808914DC59CCE641783",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "DA4EB1D64213B51C77AE75B0DFC453EF",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "470000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 58",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "958CE71D7A0B49D38B2685A4E0DF41FD",
          "devName": "RandomNonRMTSale.EvoBundleNature.04",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 750,
              "dynamicRegularPrice": -1,
              "finalPrice": 600,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 600
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "RotatingSale",
              "value": "True"
            },
            {
              "key": "AccountLevelMin",
              "value": "10"
            },
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles_Small.B_StoreButton_Bundles_Small'"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 74,
          "title": "Nature Evo Bundle",
          "shortDescription": "A stack of evolution materials!",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 750
            },
            {
              "templateId": "Reagent:Reagent_Shared_T02",
              "quantity": 100
            },
            {
              "templateId": "Reagent:Reagent_Shard_Nature",
              "quantity": 8
            }
          ]
        },
        {
          "offerId": "E29FF6EAD94B47C2AE55CCFF782D23FA",
          "devName": "StorefrontMtx.L160000.MtxGift.11",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "85CCBB5D4A8BFFD46A252F8401CC2BBC",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "E9A7C0524017B2C6740E14849A88DAA2",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "160000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 27",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "7A984F384AD542F4A3461EB525323DE5",
          "devName": "StorefrontLevel.L20000.LevelUpChest.07",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 5000,
              "dynamicRegularPrice": -1,
              "finalPrice": 5000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "70FF4DEA4EAAAFFC1CB40FAFC63DB495",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "StoreLevelMin",
              "value": "20000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 60,
          "title": "Super Magic Chest",
          "shortDescription": "",
          "description": "A Diamond Hero Crystal, 5000 Magic Tickets and 8 items!",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 5000
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 100
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_SupplyPoints_Elite",
              "quantity": 200
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 10
            }
          ]
        },
        {
          "offerId": "2E10853B4E8B01964C2863B64D6250C9",
          "devName": "Mega Magic Chest (Weekly)",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 2000,
              "dynamicRegularPrice": -1,
              "finalPrice": 2000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 2000
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": 1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "CHEST",
              "value": "true"
            },
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "IsGold",
              "value": "true"
            },
            {
              "key": "StoreLevelMin",
              "value": "10000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 65,
          "title": "Mega Magic Chest",
          "shortDescription": "",
          "description": "A Gold Hero Crystal, 2000 Magic Tickets and 8 items! Available weekly.",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 1000
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 20
            },
            {
              "templateId": "Reagent:Reagent_Shared_MysteryGoo",
              "quantity": 1
            },
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 2000
            },
            {
              "templateId": "Currency:SkillXP",
              "quantity": 1000
            },
            {
              "templateId": "Currency:SkillXP",
              "quantity": 1000
            },
            {
              "templateId": "Reagent:Reagent_Foil",
              "quantity": 35
            }
          ]
        },
        {
          "offerId": "FFB78A3B3ED44432B894798F85DBF271",
          "devName": "StorefrontMtx.L880000.MtxGift.98",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "3BB881624BB8EB2F2D8B36A69F151905",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "08B7254D4901A7E821940F840BC24CC7",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "880000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 99",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "05DC736E7C594B08B0D2DAE3E4AE3FA2",
          "devName": "StorefrontStacked.Page01.ElementalHeroes.103",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 500,
              "dynamicRegularPrice": -1,
              "finalPrice": 500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 500
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "Type",
              "value": "ElementalHero"
            },
            {
              "key": "HideQuantityRemaining",
              "value": "True"
            }
          ],
          "catalogGroup": "ElementalHeroes",
          "catalogGroupPriority": 103,
          "sortPriority": 72,
          "title": "Elemental Heroes",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 140
            },
            {
              "templateId": "Currency:Hammer",
              "quantity": 4
            },
            {
              "templateId": "TreasureMap:TM_Special_UnderwaterTunnel",
              "quantity": 1
            },
            {
              "templateId": "Reagent:Reagent_Foil",
              "quantity": 10
            },
            {
              "templateId": "Currency:Gold",
              "quantity": 100000
            },
            {
              "templateId": "Reagent:Reagent_Shard_Light",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "677D766C44F2213FD71B8D88EA623E4F",
          "devName": "Diamond Hero",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Voucher:Voucher_HeroDiamond",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "AffordOnly",
              "value": "true"
            },
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Hero.B_StoreButton_Hero'"
            },
            {
              "key": "type",
              "value": "diamond"
            },
            {
              "key": "AutoRedeem",
              "value": "false"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 107,
          "title": "Diamond Hero",
          "shortDescription": "",
          "description": "Add a powerful super rare hero to your team!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "7B41B217FD8B43A087021D1DCED6A3E4",
          "devName": "StorefrontMtx.L970000.MtxGift.109",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "2502E968436E5D2DF78BB1A266AA3C5B",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "FB4E32F849408CFC50038494DF0B371C",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "970000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 108",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "DBE0AB3035D24330A8D2CCE57F2FAD53",
          "devName": "StorefrontMtx.L890000.MtxGift.99",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "08B7254D4901A7E821940F840BC24CC7",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "B0DE74BB4B8CE1FE2370A5B60FBBA4EF",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "890000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 100",
          "shortDescription": "",
          "description": "Can we have your autograph?",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "14F0BCD6DA8648CF81A7F967206B956B",
          "devName": "StorefrontMtx.L530000.MtxGift.56",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "131F08B046089B1F82D8B5AF558E8742",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "75A4D216442030897C9954A407FF0D5E",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "530000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 64",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "AC273E28438624F50FF33AAE8D95480A",
          "devName": "Starter Pack (S1)",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "RealMoney",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "9d517678254c4b27ab85f0d1d149784b",
            "bb_StarterPack1_C",
            "",
            "bb_starterpack1",
            "",
            "",
            "",
            "",
            "sam_kalestarter"
          ],
          "requirements": [
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "78314B1A48C50D547BBCC79EE27F767F",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_AccountUpgrade.B_StoreButton_AccountUpgrade'"
            },
            {
              "key": "type",
              "value": "starterpack"
            },
            {
              "key": "bUseBannerForDetails",
              "value": "true"
            }
          ],
          "catalogGroup": "StarterPacks",
          "catalogGroupPriority": 3,
          "sortPriority": 74,
          "title": "Starter Pack",
          "shortDescription": "A poison Ninja, gems, and resources to help you get started! ",
          "description": "<RT.CapsGreen>Recruit the poison ninja, Swiftslayer Kale!</>\r\n\r\n<RT.CapsGold>Includes resources to upgrade Kale.</>",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Currency:MtxPurchased",
              "quantity": 300
            },
            {
              "templateId": "Character:Ninja_VR2_Nature_ThrowSword_T04",
              "quantity": 1
            },
            {
              "templateId": "Currency:Gold",
              "quantity": 300000
            },
            {
              "templateId": "Currency:HeroXp_Basic",
              "quantity": 50000
            },
            {
              "templateId": "Reagent:Reagent_Shard_Nature",
              "quantity": 25
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 25
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 25
            }
          ]
        },
        {
          "offerId": "BA3E1D74569F40BFA48961037B3B618D",
          "devName": "StorefrontLevel.L470000.LevelUpChest.22",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 5000,
              "dynamicRegularPrice": -1,
              "finalPrice": 5000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "7363B7F84E1B0550EA36748DEFE29C23",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "CC1A5B204B3FDB3CBAF3AFA3211D4307",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "StoreLevelMin",
              "value": "470000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 60,
          "title": "Super Magic Chest",
          "shortDescription": "",
          "description": "A Diamond Hero Crystal, 5000 Magic Tickets and 8 items!",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 5000
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 100
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_SupplyPoints_Elite",
              "quantity": 200
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 10
            }
          ]
        },
        {
          "offerId": "FC5C9E5F0CFF4C1D8C023E5BE2E4EBF0",
          "devName": "StorefrontLevel.L250000.LevelUpChest.10",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 5000,
              "dynamicRegularPrice": -1,
              "finalPrice": 5000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "33BA8DE54E81E8CFBEE108AC31F3E454",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "BD992F7F42063F197AB4EC921CD0BC16",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "StoreLevelMin",
              "value": "250000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 60,
          "title": "Super Magic Chest",
          "shortDescription": "",
          "description": "A Diamond Hero Crystal, 5000 Magic Tickets and 8 items!",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 5000
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 100
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_SupplyPoints_Elite",
              "quantity": 200
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 10
            }
          ]
        },
        {
          "offerId": "97B98203D02A4F7D9182D248E505F5D5",
          "devName": "StorefrontMtx.L550000.MtxGift.59",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "9527715345720336DC2B3C88C4A56130",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "59D7755A4258A764FA399CA8C384A3A1",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "550000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 66",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "704A4ECEC4B048A39F8A50A10D53F486",
          "devName": "StorefrontMtx.L35000.MtxGift.33",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "C5F31BC54E89D885DEA27695C7F8AF3E",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "319E25444D07F24B97FF6FA1552EDBD7",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "35000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 8",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "BDC1D23B131B420EBCA6E7DCA26A7AD9",
          "devName": "StorefrontMtx.L620000.MtxGift.67",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "4A6141634D3AC5AC701DD0B2F0AD8F9E",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "C4306C5E41B21FEE9C5192B7617A362E",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "620000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 73",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "52B546C54328062C50FE80BCB60E3ABA",
          "devName": "Account Level Up Package - Basic (Release)",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "RealMoney",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "8e60722d2cd54953907351b5a94debc5",
            "bb_levelup_release",
            "",
            "bb_levelup_release",
            "",
            "",
            "",
            "",
            "sam_levelup_release"
          ],
          "requirements": [
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "59F5930D4800D4810BE9DDBBBD694FA6",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "8383C7924A5B37A8C656A69987543CF4",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "type",
              "value": "accountlevelup"
            },
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_AccountUpgrade.B_StoreButton_AccountUpgrade'"
            },
            {
              "key": "AccountLevelMin",
              "value": "35"
            },
            {
              "key": "AccountLevelMax",
              "value": "250"
            },
            {
              "key": "MtxLevelMin",
              "value": "100"
            },
            {
              "key": "PreviewFulfillmentClassPath",
              "value": "CatalogFulfillment'/Game/Catalog/Fulfillments/Bundles/Sale/Release_LevelUpPackage_Basic.Release_LevelUpPackage_Basic'"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 29,
          "title": "Level-Up Pack",
          "shortDescription": "Rewards every 10 levels up to level 150, including Legendary Hero Traces!",
          "description": "<RT.CapsGreen>Complete Skybreaker Quests as you level!</>\r\n<RT.BasicMed>Receive a Level Up Package every 10 levels from 10 to 150</>\r\n<RT.BasicMed>Packages are retroactive</>  \r\n\r\n<RT.CapsGold>Level Up Package Contents</> \r\n  <RT.BasicMed>1000 Core Hero Traces</>\r\n  <RT.BasicMed>100k Gold</>\r\n\r\n<RT.BasicMed>The final package contains 100 Legendary Hero Traces!</>",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Giftbox:GB_LevelUpPackage_Basic01",
              "quantity": 1
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 1000
            }
          ]
        },
        {
          "offerId": "83A8B57EDDDF4D7BA4A8D189A6672346",
          "devName": "StorefrontMtx.L930000.MtxGift.104",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "3EEBE6C44ADC45AAD484B19A00BD9134",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "2468A46347C548FE8C4702A77B29CE07",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "930000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 104",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "07A6E16C3E344E0F9D6AE9B175F7F1F4",
          "devName": "StorefrontMtx.L350000.MtxGift.34",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "4A66472743F146E7160266946FD8A5D2",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "2AE410184EAB8943E57EABACB2480680",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "350000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 46",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "DD6ECF854F2BE5BF7A98C69581050EFB",
          "devName": "Light Hero",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Voucher:Voucher_HeroSilver_Light",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "AffordOnly",
              "value": "true"
            },
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Hero.B_StoreButton_Hero'"
            },
            {
              "key": "type",
              "value": "light"
            },
            {
              "key": "AutoRedeem",
              "value": "false"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 101,
          "title": "Light Hero",
          "shortDescription": "",
          "description": "Summon a hero to join your team!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "1A76391606AE492B98511ABC9661D985",
          "devName": "Storefront.HeroBundle.07",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 4500,
              "dynamicRegularPrice": -1,
              "finalPrice": 4500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 4500
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": 1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_AccountUpgrade.B_StoreButton_AccountUpgrade'"
            },
            {
              "key": "HideQuantityRemaining",
              "value": "True"
            },
            {
              "key": "Type",
              "value": "herobundle"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 74,
          "title": "HeroBundle",
          "shortDescription": "",
          "description": "<RT.CapsGreen>A hero and upgrade resources!</>",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Character:SpiritWarrior_SR2_Fire_IronMonkey_T04",
              "quantity": 1
            },
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 2500
            },
            {
              "templateId": "Currency:Gold",
              "quantity": 2113000
            },
            {
              "templateId": "Currency:HeroXp_Basic",
              "quantity": 1260000
            },
            {
              "templateId": "Currency:SkillXP",
              "quantity": 9100
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMinor",
              "quantity": 74
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 74
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMinor",
              "quantity": 74
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 74
            },
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 25
            },
            {
              "templateId": "Ore:Ore_Iron",
              "quantity": 4024
            },
            {
              "templateId": "Ore:Ore_Silver",
              "quantity": 4024
            },
            {
              "templateId": "Ore:Ore_Magicite",
              "quantity": 270
            },
            {
              "templateId": "Reagent:Reagent_Shared_T02",
              "quantity": 450
            },
            {
              "templateId": "Reagent:Reagent_Shard_Fire",
              "quantity": 69
            }
          ]
        },
        {
          "offerId": "C18C7668C17F4F7CBA6574DA321F0214",
          "devName": "StorefrontLevel.L530000.LevelUpChest.26",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 5000,
              "dynamicRegularPrice": -1,
              "finalPrice": 5000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "2505AD4D4B9A19FBB46D0B9EBC1EA56C",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "92077EB243071AD9F0E7A2B5F2F71D7F",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "StoreLevelMin",
              "value": "530000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 60,
          "title": "Super Magic Chest",
          "shortDescription": "",
          "description": "A Diamond Hero Crystal, 5000 Magic Tickets and 8 items!",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 5000
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 100
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_SupplyPoints_Elite",
              "quantity": 200
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 10
            }
          ]
        },
        {
          "offerId": "4744940B4BF99738ACA115A616EC8C4E",
          "devName": "Underworld Trader (T3)",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "RealMoney",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "395a588577834f4089f14440868a3785",
            "bb_viptier3_release",
            "",
            "bb_viptier3_release",
            "",
            "",
            "",
            "",
            "sam_viptier3_release"
          ],
          "requirements": [
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "BE8A7A4F48546D69D0F8DF873120B3E6",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "VipLevelMin",
              "value": "2"
            },
            {
              "key": "AccountLevelMin",
              "value": "50"
            },
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_AccountUpgrade.B_StoreButton_AccountUpgrade'"
            },
            {
              "key": "VipLevelMax",
              "value": "2"
            },
            {
              "key": "type",
              "value": "accountupgrade"
            },
            {
              "key": "InspectItem",
              "value": "Character:Pet_SR1_Cloudpuff_Fire_T05"
            },
            {
              "key": "PreviewFulfillmentClassPath",
              "value": "CatalogFulfillment'/Game/Catalog/Fulfillments/AccountUpgrades/Release_VIP_Tier3.Release_VIP_Tier3'"
            },
            {
              "key": "bShowInGemStore",
              "value": "true"
            }
          ],
          "catalogGroup": "AccountUpgrades",
          "catalogGroupPriority": 0,
          "sortPriority": 40,
          "title": "Underworld Trader Collection",
          "shortDescription": "A unique pet, free secret shop entry, quests, gems, a hero and more!",
          "description": "<RT.CapsGreen>Fierce Cloudpuff</> <RT.BasicMed>- a pet that greatly reduces enemy DEF!</>\r\n\r\n<RT.CapsBlue>Includes Permanent Account Upgrades</>",
          "displayAssetPath": "/Game/UMG/Textures/Store/btn_StoreGemGoldenChest.btn_StoreGemGoldenChest",
          "itemGrants": [
            {
              "templateId": "Character:Pet_SR1_Cloudpuff_Fire_T05",
              "quantity": 1
            },
            {
              "templateId": "StandIn:FreeSecretShopItem",
              "quantity": 1
            },
            {
              "templateId": "StandIn:QuestLimit",
              "quantity": 1
            },
            {
              "templateId": "Currency:MtxPurchased",
              "quantity": 1500
            },
            {
              "templateId": "Currency:MtxPurchaseBonus",
              "quantity": 1000
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_Shard_Dark",
              "quantity": 15
            },
            {
              "templateId": "Reagent:Reagent_Shard_Fire",
              "quantity": 15
            },
            {
              "templateId": "Reagent:Reagent_Shard_Light",
              "quantity": 15
            },
            {
              "templateId": "Reagent:Reagent_Shard_Nature",
              "quantity": 15
            },
            {
              "templateId": "Reagent:Reagent_Shard_Water",
              "quantity": 15
            }
          ]
        },
        {
          "offerId": "6F897EF24E6F4DA3B73E3AE752FAE63E",
          "devName": "StorefrontMtx.L390000.MtxGift.38",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "4FF613E04A689AD396C48C814D9A8E2C",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "B5A4BF784C406402BF3D8CBD24A7CF39",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "390000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 50",
          "shortDescription": "",
          "description": "You help make the game a reality!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "67519B03CC6C4378AEDAF416942FF857",
          "devName": "StorefrontMtx.L770000.MtxGift.85",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "F3D83DC94DA0E904C3C56DB7D5961108",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "C64C6E59441A5349F9AE91A876893321",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "770000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 88",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "EF80BD4FE3BD41728165D99E9709B7FF",
          "devName": "StorefrontMtx.L450000.MtxGift.46",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "15B714264A35B80083536D821A2C9203",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "38DB359C4DE88053A370F78B24A69908",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "450000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 56",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "FA390CC7ABF14CD98B9D1AB5224D16C4",
          "devName": "StorefrontMtx.L460000.MtxGift.47",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "38DB359C4DE88053A370F78B24A69908",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "45A93AE643E53808914DC59CCE641783",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "460000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 57",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "4F588386C6704F6DBA808F99D46DCB28",
          "devName": "StorefrontLevel.L310000.LevelUpChest.13",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 5000,
              "dynamicRegularPrice": -1,
              "finalPrice": 5000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "3B8A9D74477DAF56B37DDE84F453A9E5",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "E65689DC44393C8ED32C3EA98549786A",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "StoreLevelMin",
              "value": "310000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 60,
          "title": "Super Magic Chest",
          "shortDescription": "",
          "description": "A Diamond Hero Crystal, 5000 Magic Tickets and 8 items!",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 5000
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 100
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_SupplyPoints_Elite",
              "quantity": 200
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 10
            }
          ]
        },
        {
          "offerId": "DC6CB1284AF36F773B0B6BA18DD64B25",
          "devName": "Treasure Hunter (T2)",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "RealMoney",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "20621749aaa04a49b28a2e68049470cb",
            "bb_viptier2_release",
            "",
            "bb_viptier2_release",
            "",
            "",
            "",
            "",
            "sam_viptier2_release"
          ],
          "requirements": [
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "BE8A7A4F48546D69D0F8DF873120B3E6",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "VipLevelMin",
              "value": "1"
            },
            {
              "key": "AccountLevelMin",
              "value": "25"
            },
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_AccountUpgrade.B_StoreButton_AccountUpgrade'"
            },
            {
              "key": "VipLevelMax",
              "value": "1"
            },
            {
              "key": "type",
              "value": "accountupgrade"
            },
            {
              "key": "InspectItem",
              "value": "Character:Pet_SR1_Cloudpuff_Light_T05"
            },
            {
              "key": "PreviewFulfillmentClassPath",
              "value": "CatalogFulfillment'/Game/Catalog/Fulfillments/AccountUpgrades/Release_VIP_Tier2.Release_VIP_Tier2'"
            },
            {
              "key": "bShowInGemStore",
              "value": "true"
            }
          ],
          "catalogGroup": "AccountUpgrades",
          "catalogGroupPriority": 0,
          "sortPriority": 40,
          "title": "Treasure Hunter Collection",
          "shortDescription": "A unique pet, free daily treasure maps, more teams, quests, gems, a hero and more!",
          "description": "<RT.CapsGreen>Cuddly Cloudpuff</> <RT.BasicMed> - a pet that resurrects and heals!</>\r\n\r\n<RT.CapsBlue>Includes Permanent Account Upgrades</>\r\n\r\n<RT.BasicMed>Treasure Hunts grant 5 Lockpicks and a daily bonus resource</>",
          "displayAssetPath": "/Game/UMG/Textures/Store/btn_StoreGemGoldenChest.btn_StoreGemGoldenChest",
          "itemGrants": [
            {
              "templateId": "Party:Instance",
              "quantity": 5
            },
            {
              "templateId": "Character:Pet_SR1_Cloudpuff_Light_T05",
              "quantity": 1
            },
            {
              "templateId": "StandIn:DailyTreasureHuntChest",
              "quantity": 1
            },
            {
              "templateId": "StandIn:TeamSlotsUpgrade",
              "quantity": 1,
              "attributes": {
                "FakeQuantity": 5
              }
            },
            {
              "templateId": "StandIn:InventoryUpgrade",
              "quantity": 1,
              "attributes": {
                "FakeQuantity": 25
              }
            },
            {
              "templateId": "StandIn:QuestLimit",
              "quantity": 1,
              "attributes": {
                "FakeQuantity": 1
              }
            },
            {
              "templateId": "Currency:MtxPurchased",
              "quantity": 1500
            },
            {
              "templateId": "Currency:MtxPurchaseBonus",
              "quantity": 750
            },
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 5000
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 500
            },
            {
              "templateId": "Ore:Ore_Magicite",
              "quantity": 100
            },
            {
              "templateId": "Ore:Ore_Silver",
              "quantity": 1000
            },
            {
              "templateId": "Ore:Ore_Iron",
              "quantity": 1000
            }
          ]
        },
        {
          "offerId": "AAB70BA93409477483295CDBDE2C6A50",
          "devName": "StorefrontMtx.L380000.MtxGift.37",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "CD425F9A4614451770592D976A9CB72A",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "4FF613E04A689AD396C48C814D9A8E2C",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "380000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 49",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "033EBDA10C7D4244ABFD45B9D74C22AA",
          "devName": "StorefrontStacked.Page01.ElementalHeroes.87",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 500,
              "dynamicRegularPrice": -1,
              "finalPrice": 500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 500
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "Type",
              "value": "ElementalHero"
            },
            {
              "key": "HideQuantityRemaining",
              "value": "True"
            }
          ],
          "catalogGroup": "ElementalHeroes",
          "catalogGroupPriority": 87,
          "sortPriority": 72,
          "title": "Elemental Heroes",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 140
            },
            {
              "templateId": "Currency:Hammer",
              "quantity": 4
            },
            {
              "templateId": "TreasureMap:TM_Special_Cloud5",
              "quantity": 1
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 25
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 2
            },
            {
              "templateId": "Currency:SkillXP",
              "quantity": 250
            }
          ]
        },
        {
          "offerId": "C988BA4B4BACFC5FE4C7389B7C594249",
          "devName": "Unwavering Guardian (T4)",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "RealMoney",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "760156eb63ad49b68861a5b269b73b48",
            "bb_viptier4_release",
            "",
            "bb_viptier4_release",
            "",
            "",
            "",
            "",
            "sam_viptier4_release"
          ],
          "requirements": [
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "BE8A7A4F48546D69D0F8DF873120B3E6",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "VipLevelMin",
              "value": "3"
            },
            {
              "key": "AccountLevelMin",
              "value": "75"
            },
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_AccountUpgrade.B_StoreButton_AccountUpgrade'"
            },
            {
              "key": "VipLevelMax",
              "value": "3"
            },
            {
              "key": "type",
              "value": "accountupgrade"
            },
            {
              "key": "InspectItem",
              "value": "Character:Pet_SR1_Cloudpuff_Water_T05"
            },
            {
              "key": "PreviewFulfillmentClassPath",
              "value": "CatalogFulfillment'/Game/Catalog/Fulfillments/AccountUpgrades/Release_VIP_Tier4.Release_VIP_Tier4'"
            },
            {
              "key": "bShowInGemStore",
              "value": "true"
            }
          ],
          "catalogGroup": "AccountUpgrades",
          "catalogGroupPriority": 0,
          "sortPriority": 40,
          "title": "Unwavering Guardian Collection",
          "shortDescription": "A unique pet, additional Rep Hero, use friends twice per day, quests, gems, a hero and more!",
          "description": "<RT.CapsGreen>Olympian Cloudpuff</> <RT.BasicMed>- a pet that heals mana and prevents debuffs!</>\r\n\r\n<RT.CapsBlue>Includes Permanent Account Upgrades</>",
          "displayAssetPath": "/Game/UMG/Textures/Store/btn_StoreGemGoldenChest.btn_StoreGemGoldenChest",
          "itemGrants": [
            {
              "templateId": "Character:Pet_SR1_Cloudpuff_Water_T05",
              "quantity": 1
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 100
            },
            {
              "templateId": "StandIn:AdditionalRepHero",
              "quantity": 1
            },
            {
              "templateId": "StandIn:AdditionalDailyFriendHeroUse",
              "quantity": 2
            },
            {
              "templateId": "StandIn:AdditionalDailyGiftPoints",
              "quantity": 1,
              "attributes": {
                "FakeQuantity": 80
              }
            },
            {
              "templateId": "StandIn:QuestLimit",
              "quantity": 1
            },
            {
              "templateId": "Currency:MtxPurchased",
              "quantity": 1500
            },
            {
              "templateId": "Currency:MtxPurchaseBonus",
              "quantity": 1500
            },
            {
              "templateId": "Currency:Hammer",
              "quantity": 100
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 500
            }
          ]
        },
        {
          "offerId": "1B6973A9D3614272B05A4E2C04279938",
          "devName": "StorefrontMtx.L280000.MtxGift.25",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "6EC4CB2241CDD5FFA61D059F0266A988",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "267A66044012B4293233CDB9199F91B2",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "280000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 39",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "2B004E8E91C74873954573F401C495A7",
          "devName": "StorefrontMtx.L130000.MtxGift.07",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "A21C10754CF2A279F3E72E959D1D7A6C",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "9E833A024D8FD5EAD1C4AD83D739AD24",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "130000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 24",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "8E37E79715ED430D9E983BE445E3E33E",
          "devName": "StorefrontLevel.L115000.LevelUpChest.02",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 5000,
              "dynamicRegularPrice": -1,
              "finalPrice": 5000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "5E0F227449A65CEEA0E5A9BBC01329CF",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "62A30DED4F2E3F8863CE0DB8B97125D5",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "StoreLevelMin",
              "value": "115000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 60,
          "title": "Super Magic Chest",
          "shortDescription": "",
          "description": "A Diamond Hero Crystal, 5000 Magic Tickets and 8 items!",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 5000
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 100
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_SupplyPoints_Elite",
              "quantity": 200
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 10
            }
          ]
        },
        {
          "offerId": "7ACC9E3E4AD65D51D44D11A63EF00EA7",
          "devName": "Water Hero",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Voucher:Voucher_HeroSilver_Water",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "AffordOnly",
              "value": "true"
            },
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Hero.B_StoreButton_Hero'"
            },
            {
              "key": "type",
              "value": "water"
            },
            {
              "key": "AutoRedeem",
              "value": "false"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 101,
          "title": "Water Hero",
          "shortDescription": "",
          "description": "Summon a hero to join your team!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "2C88F53240C5132C629A23B0E569E7D1",
          "devName": "PowerEfflux Nature",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Voucher:Voucher_Hero_TreasureHunter_Nature_PowerEfflux",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "AffordOnly",
              "value": "true"
            },
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Hero.B_StoreButton_Hero'"
            },
            {
              "key": "type",
              "value": "Random"
            },
            {
              "key": "AutoRedeem",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 9999,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Character:TreasureHunter_R2_Nature_PowerEfflux_T03",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "2481B2EBB97E488F9748AF775F45386F",
          "devName": "StorefrontStacked.Page01.ElementalHeroes.291",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 500,
              "dynamicRegularPrice": -1,
              "finalPrice": 500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 500
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "Type",
              "value": "ElementalHero"
            },
            {
              "key": "HideQuantityRemaining",
              "value": "True"
            }
          ],
          "catalogGroup": "ElementalHeroes",
          "catalogGroupPriority": 291,
          "sortPriority": 72,
          "title": "Elemental Heroes",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 140
            },
            {
              "templateId": "Currency:Hammer",
              "quantity": 4
            },
            {
              "templateId": "Reagent:Reagent_Shard_Fire",
              "quantity": 5
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMinor",
              "quantity": 7
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 20
            },
            {
              "templateId": "Reagent:Reagent_Shard_Light",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "4FADFAEED7004CD39245418BA1A6CC9A",
          "devName": "StorefrontMtx.L90000.MtxGift.100",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "E462EAA14B27F738FAC2B6B8428DD2FA",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "740E811445C06D5E4FD71E84F559593C",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "90000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 19",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "07456E4C4BA447FDA5CD1D13F10A314E",
          "devName": "StorefrontStacked.Page01.ElementalHeroes.65",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 500,
              "dynamicRegularPrice": -1,
              "finalPrice": 500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 500
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "Type",
              "value": "ElementalHero"
            },
            {
              "key": "HideQuantityRemaining",
              "value": "True"
            }
          ],
          "catalogGroup": "ElementalHeroes",
          "catalogGroupPriority": 65,
          "sortPriority": 72,
          "title": "Elemental Heroes",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 140
            },
            {
              "templateId": "Currency:Hammer",
              "quantity": 4
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 10
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMinor",
              "quantity": 10
            },
            {
              "templateId": "Currency:Gold",
              "quantity": 100000
            },
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "20127E956D94499FA2183DD86B048897",
          "devName": "StorefrontMtx.L800000.MtxGift.89",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "F0B52CD74EB72783AE8286BC75F1BEF1",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "26D8C467410A6F8B2D0216B98EC18F0B",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "800000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 91",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "AC5A697455F3455BBC4A0979994C89E7",
          "devName": "StorefrontMtx.L760000.MtxGift.84",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "95D438054A0CFA5ECC5EF582961AD9FC",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "F3D83DC94DA0E904C3C56DB7D5961108",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "760000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 87",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "B8751CE54CF5526D9E11E8BF4533FDC9",
          "devName": "12HR Basic Chest (Silver) (Battle Breaker)",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 100,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "DAILYCHEST",
              "value": "true"
            },
            {
              "key": "VipLevelMin",
              "value": "1"
            },
            {
              "key": "type",
              "value": "dailylootboxbb"
            },
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles_Small.B_StoreButton_Bundles_Small'"
            }
          ],
          "catalogGroup": "Silver Chest",
          "catalogGroupPriority": 4,
          "sortPriority": 115,
          "title": "12hr Basic Chest",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 100
            },
            {
              "templateId": "Currency:Hammer",
              "quantity": 4
            }
          ]
        },
        {
          "offerId": "56718B3E46FF8E47EA366CB62B14A85C",
          "devName": "Rare Meeg Crystal",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Voucher:Voucher_HeroMeegRare",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "AffordOnly",
              "value": "true"
            },
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Hero.B_StoreButton_Hero'"
            },
            {
              "key": "type",
              "value": "meeg"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 104,
          "title": "Rare Meeg Crystal",
          "shortDescription": "",
          "description": "Crack it open to find something special!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "76DF2F7323A04D68903405C18C9A1993",
          "devName": "StorefrontLevel.L350000.LevelUpChest.16",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 5000,
              "dynamicRegularPrice": -1,
              "finalPrice": 5000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "2F18BCC44E753971B12564A1449C37B5",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "9599934D4B2CFBC377CB67AB131F6B6B",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "StoreLevelMin",
              "value": "350000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 60,
          "title": "Super Magic Chest",
          "shortDescription": "",
          "description": "A Diamond Hero Crystal, 5000 Magic Tickets and 8 items!",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 5000
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 100
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_SupplyPoints_Elite",
              "quantity": 200
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 10
            }
          ]
        },
        {
          "offerId": "0B1AAB036CC3463D8729174EC77253B1",
          "devName": "StorefrontStacked.Page01.ElementalHeroes.313",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 500,
              "dynamicRegularPrice": -1,
              "finalPrice": 500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 500
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "Type",
              "value": "ElementalHero"
            },
            {
              "key": "HideQuantityRemaining",
              "value": "True"
            }
          ],
          "catalogGroup": "ElementalHeroes",
          "catalogGroupPriority": 313,
          "sortPriority": 72,
          "title": "Elemental Heroes",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 140
            },
            {
              "templateId": "Currency:Hammer",
              "quantity": 4
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 15
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 5
            },
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 100
            },
            {
              "templateId": "Currency:SkillXP",
              "quantity": 250
            }
          ]
        },
        {
          "offerId": "2F209D68B0B049D794ED16C9B9D7B0D5",
          "devName": "StorefrontStacked.Page01.ElementalHeroes.85",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 500,
              "dynamicRegularPrice": -1,
              "finalPrice": 500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 500
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "Type",
              "value": "ElementalHero"
            },
            {
              "key": "HideQuantityRemaining",
              "value": "True"
            }
          ],
          "catalogGroup": "ElementalHeroes",
          "catalogGroupPriority": 85,
          "sortPriority": 72,
          "title": "Elemental Heroes",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 140
            },
            {
              "templateId": "Currency:Hammer",
              "quantity": 4
            },
            {
              "templateId": "Currency:SkillXP",
              "quantity": 500
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMinor",
              "quantity": 7
            },
            {
              "templateId": "Reagent:Reagent_Shared_T02",
              "quantity": 50
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 20
            }
          ]
        },
        {
          "offerId": "D09C2DE994A040E08A3B556A24EF7D35",
          "devName": "StorefrontLevel.L150000.LevelUpChest.04",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 5000,
              "dynamicRegularPrice": -1,
              "finalPrice": 5000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "FE6C666D41BCDBA0704ED29B8A1FD492",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "4E0DF6CB4D36D1EF2CC5CBAA87EE65B1",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "StoreLevelMin",
              "value": "150000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 60,
          "title": "Super Magic Chest",
          "shortDescription": "",
          "description": "A Diamond Hero Crystal, 5000 Magic Tickets and 8 items!",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 5000
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 100
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_SupplyPoints_Elite",
              "quantity": 200
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 10
            }
          ]
        },
        {
          "offerId": "C989E0D7E21E4299937EB5FB452074A5",
          "devName": "StorefrontStacked.Page01.ElementalHeroes.117",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 500,
              "dynamicRegularPrice": -1,
              "finalPrice": 500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 500
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "Type",
              "value": "ElementalHero"
            },
            {
              "key": "HideQuantityRemaining",
              "value": "True"
            }
          ],
          "catalogGroup": "ElementalHeroes",
          "catalogGroupPriority": 117,
          "sortPriority": 72,
          "title": "Elemental Heroes",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 140
            },
            {
              "templateId": "Currency:Hammer",
              "quantity": 4
            },
            {
              "templateId": "Currency:SkillXP",
              "quantity": 2000
            },
            {
              "templateId": "Reagent:Reagent_Shard_Dark",
              "quantity": 1
            },
            {
              "templateId": "Reagent:Reagent_SupplyPoints_Elite",
              "quantity": 10
            },
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 100
            }
          ]
        },
        {
          "offerId": "9D811D35983A4EB284B7F7B8A008C7DE",
          "devName": "StorefrontMtx.L590000.MtxGift.63",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "9632B0144E806B1508858E8526C8C7D2",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "670D0A5340ABB9757D737B96CA72AD20",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "590000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 70",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "D92B6BD03F754DED9FA649FBF4A135F8",
          "devName": "StorefrontMtx.L400000.MtxGift.40",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "B5A4BF784C406402BF3D8CBD24A7CF39",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "5D2606E94E550BB7A3BDE59294A9A6E9",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "400000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 51",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "3AA4AB3F4AF719A69F444792ABE587C6",
          "devName": "Elemental Hero Resources (Master of the Hoard)",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 500,
              "dynamicRegularPrice": -1,
              "finalPrice": 350,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 350
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "VipLevelMin",
              "value": "5"
            },
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "type",
              "value": "ElementalHero"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 72,
          "title": "12hr Elemental Heroes",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 140
            },
            {
              "templateId": "Currency:Hammer",
              "quantity": 4
            },
            {
              "templateId": "Reagent:Reagent_SupplyPoints_Elite",
              "quantity": 5
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 60
            },
            {
              "templateId": "Reagent:Reagent_Foil",
              "quantity": 10
            },
            {
              "templateId": "Currency:SkillXP",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 10
            },
            {
              "templateId": "Reagent:WCCoins",
              "quantity": 2
            },
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 200
            }
          ]
        },
        {
          "offerId": "1D9B7236AA01476EA8FCFC7EA41B7DBB",
          "devName": "StorefrontLevel.L35000.LevelUpChest.15",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 5000,
              "dynamicRegularPrice": -1,
              "finalPrice": 5000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "70FF4DEA4EAAAFFC1CB40FAFC63DB495",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "BD7EBC794C6B9B123BFCDBA223F68A0E",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "StoreLevelMin",
              "value": "35000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 60,
          "title": "Super Magic Chest",
          "shortDescription": "",
          "description": "A Diamond Hero Crystal, 5000 Magic Tickets and 8 items!",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 5000
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 100
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_SupplyPoints_Elite",
              "quantity": 200
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 10
            }
          ]
        },
        {
          "offerId": "0FD29E0C4216F082922E1494F5349D1B",
          "devName": "PowerEfflux Fire",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Voucher:Voucher_Hero_TreasureHunter_Fire_PowerEfflux",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "AffordOnly",
              "value": "true"
            },
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Hero.B_StoreButton_Hero'"
            },
            {
              "key": "type",
              "value": "Random"
            },
            {
              "key": "AutoRedeem",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 9999,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Character:TreasureHunter_R2_Fire_PowerEfflux_T03",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "829B782A46AF980800255085B160AA45",
          "devName": "PowerEfflux Water",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Voucher:Voucher_Hero_TreasureHunter_Water_PowerEfflux",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "AffordOnly",
              "value": "true"
            },
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Hero.B_StoreButton_Hero'"
            },
            {
              "key": "type",
              "value": "Random"
            },
            {
              "key": "AutoRedeem",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 9999,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Character:TreasureHunter_R2_Water_PowerEfflux_T03",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "A654319C5EE0461BA572B0C9782B5CBD",
          "devName": "StorefrontLevel.L570000.LevelUpChest.28",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 5000,
              "dynamicRegularPrice": -1,
              "finalPrice": 5000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "8A2CF2B442B4177565F52196364A120F",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "BD23EFDD4B93572E335B939B59627F0F",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "StoreLevelMin",
              "value": "570000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 60,
          "title": "Super Magic Chest",
          "shortDescription": "",
          "description": "A Diamond Hero Crystal, 5000 Magic Tickets and 8 items!",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 5000
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 100
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_SupplyPoints_Elite",
              "quantity": 200
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 10
            }
          ]
        },
        {
          "offerId": "1BEE99CB4CEFE7BF2518CBAF5CA81023",
          "devName": "Meeg Crystal",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Voucher:Voucher_HeroMeeg",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "AffordOnly",
              "value": "true"
            },
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Hero.B_StoreButton_Hero'"
            },
            {
              "key": "type",
              "value": "meeg"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 103,
          "title": "Meeg Crystal",
          "shortDescription": "",
          "description": "Crack it open to find something special!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "3C9A2002402C57AFCEE6D6843AB1F283",
          "devName": "Mining Crystal",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Voucher:Voucher_Hero_Mine",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "AffordOnly",
              "value": "true"
            },
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Hero.B_StoreButton_Hero'"
            },
            {
              "key": "type",
              "value": "Random"
            },
            {
              "key": "AutoRedeem",
              "value": "false"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 102,
          "title": "Mining Crystal",
          "shortDescription": "",
          "description": "Crack it open to find something special!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "FB62DDCE8FFE4C74B06BCADE173F1CB0",
          "devName": "StorefrontMtx.L110000.MtxGift.05",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "7696BED040A499C469CBB9BA6A24F830",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "1369D9784B1B9096135B08BD23386E2D",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "110000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 22",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "71DAB8E8505D41F4B4D99CCD00B9B499",
          "devName": "StorefrontLevel.L50000.LevelUpChest.24",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 5000,
              "dynamicRegularPrice": -1,
              "finalPrice": 5000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "BD7EBC794C6B9B123BFCDBA223F68A0E",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "FC8853B24429F824CE4837B1A3C5B58A",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "StoreLevelMin",
              "value": "50000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 60,
          "title": "Super Magic Chest",
          "shortDescription": "",
          "description": "A Diamond Hero Crystal, 5000 Magic Tickets and 8 items!",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 5000
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 100
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_SupplyPoints_Elite",
              "quantity": 200
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 10
            }
          ]
        },
        {
          "offerId": "94115A059B484EB1A600E070F9D9102D",
          "devName": "StorefrontLevel.L450000.LevelUpChest.21",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 5000,
              "dynamicRegularPrice": -1,
              "finalPrice": 5000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "B949A38F4F1AFF040AF09EA67355F09B",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "7363B7F84E1B0550EA36748DEFE29C23",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "StoreLevelMin",
              "value": "450000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 60,
          "title": "Super Magic Chest",
          "shortDescription": "",
          "description": "A Diamond Hero Crystal, 5000 Magic Tickets and 8 items!",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 5000
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 100
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_SupplyPoints_Elite",
              "quantity": 200
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 10
            }
          ]
        },
        {
          "offerId": "51B8402D754E4FC3838D8F4B98A94CF4",
          "devName": "StorefrontLevel.L100000.LevelUpChest.01",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 5000,
              "dynamicRegularPrice": -1,
              "finalPrice": 5000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "1CE9D551409C5DF76678DBBD81B4FDB9",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "5E0F227449A65CEEA0E5A9BBC01329CF",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "StoreLevelMin",
              "value": "100000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 60,
          "title": "Super Magic Chest",
          "shortDescription": "",
          "description": "A Diamond Hero Crystal, 5000 Magic Tickets and 8 items!",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 5000
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 100
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_SupplyPoints_Elite",
              "quantity": 200
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 10
            }
          ]
        },
        {
          "offerId": "950669FD059D457881B7E91872EBFA2B",
          "devName": "StorefrontMtx.L730000.MtxGift.80",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "6C731B18416AC27CC6F29CBD0FC2CB8A",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "28A9A2AE472680E9279EAAAC80FE133B",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "730000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 84",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "013BF4ADEA4248BDA5F988DC4B975C01",
          "devName": "StorefrontMtx.L600000.MtxGift.65",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "670D0A5340ABB9757D737B96CA72AD20",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "99C4CD6341895994F96C418162800C4B",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "600000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 71",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "EE7D33624F974A0C8E3422CA8624EC6F",
          "devName": "StorefrontMtx.L95000.MtxGift.106",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "740E811445C06D5E4FD71E84F559593C",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "FF31B86842EFA7A884529E90768AE3D3",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "95000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 20",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "B93CAA874C45B7BA06BD2CAD25531475",
          "devName": "Battle Pass (Free)",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 1000,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleType": "Strikethrough",
              "saleExpiration": "9999-01-01T12:00:00.000Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": 1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "BE8A7A4F48546D69D0F8DF873120B3E6",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "BonusOverride",
              "value": "3000"
            },
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Battlepass.B_StoreButton_Battlepass'"
            }
          ],
          "catalogGroup": "BattlePass",
          "catalogGroupPriority": 2,
          "sortPriority": 500,
          "title": "Battle Pass",
          "shortDescription": "",
          "description": "100 Gems every day for 30 days\r\nUnlocks premium Battle Pass rewards",
          "displayAssetPath": "/Game/UMG/Textures/Store/btn_StoreGemBag.btn_StoreGemBag",
          "itemGrants": []
        },
        {
          "offerId": "D824D5FD9D0B4FBABD4D2E46E7A46808",
          "devName": "StorefrontMtx.L500000.MtxGift.53",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "105F8AFD4D3AF0210CFBDEBD62E6DCF8",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "2BFCE5B9460735E737669585D1895444",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "500000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 61",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "9E81909035A74E51979A66A3A0C7A246",
          "devName": "StorefrontMtx.L830000.MtxGift.92",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "AE3B458F433DE9BEF76CFFAFA6E5824B",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "EBB0863F49BB7043079813B5FCC2D915",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "830000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 94",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "A2278665382A4A389D9244FBBAC8354C",
          "devName": "StorefrontMtx.L700000.MtxGift.77",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "B133B6DC440D5686E38D49BBE35CD861",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "47201DAA4E39ECA176CD35AA4CF9A699",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "700000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 81",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "5AF2C9FC073D45D3AB409505BE6D7AE1",
          "devName": "StorefrontMtx.L40000.MtxGift.39",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "319E25444D07F24B97FF6FA1552EDBD7",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "10EF29A04E418C8E417CF7A40892E612",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "40000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 9",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "B2971E9916EC449ABF1D616E9910F68A",
          "devName": "StorefrontMtx.L870000.MtxGift.97",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "04AB19D44110BECA0DE37CAF7632195A",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "3BB881624BB8EB2F2D8B36A69F151905",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "870000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 98",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "192802C3DF17413BBA249D240FC7232C",
          "devName": "StorefrontMtx.L840000.MtxGift.93",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "EBB0863F49BB7043079813B5FCC2D915",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "594167794856DBCA4304328EDC133E15",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "840000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 95",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "DC4CC6470406467CAD3351C2C0C200FE",
          "devName": "StorefrontMtx.L20000.MtxGift.15",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "C92799DE44F0657A1C85C5BF6A1CC2B0",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "1DA1BAEC49524F730C07AA9D285CDDB3",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "20000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 5",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "BB705E9BC71545A99E81673915D9A376",
          "devName": "StorefrontMtx.L45000.MtxGift.45",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "10EF29A04E418C8E417CF7A40892E612",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "8352FBF848AB462C24BEEFABE6E373C0",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "45000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 10",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "8ED348DB4F6A6FA2A9AE28BCEA46D27B",
          "devName": "Silver Hero",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Voucher:Voucher_HeroSilver",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "AffordOnly",
              "value": "true"
            },
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Hero.B_StoreButton_Hero'"
            },
            {
              "key": "type",
              "value": "silver"
            },
            {
              "key": "AutoRedeem",
              "value": "false"
            }
          ],
          "catalogGroup": "Silver Hero",
          "catalogGroupPriority": 0,
          "sortPriority": 100,
          "title": "Silver Hero",
          "shortDescription": "",
          "description": "Summon a hero to join your team!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "ABBC1B5E4378416FAE163D70C9C9E491",
          "devName": "StorefrontMtx.L790000.MtxGift.87",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "6CBE11F4473C198CA22818827EF10200",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "F0B52CD74EB72783AE8286BC75F1BEF1",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "790000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 90",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "28634F6497D74ABABBF37FFD65613D5A",
          "devName": "StorefrontMtx.L910000.MtxGift.102",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "163B90B54347AA6F1BA40AA087DADF38",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "AA2F5806432BBFC19852F78A885B0659",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "910000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 102",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "EB904E19F7224C3A965A54FD4763BDA6",
          "devName": "StorefrontLevel.L410000.LevelUpChest.19",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 5000,
              "dynamicRegularPrice": -1,
              "finalPrice": 5000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "C1580AC74C42EEC07C38AB84A73A3A70",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "D0A62F8540F76D50B172988D31FF1B47",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "StoreLevelMin",
              "value": "410000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 60,
          "title": "Super Magic Chest",
          "shortDescription": "",
          "description": "A Diamond Hero Crystal, 5000 Magic Tickets and 8 items!",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 5000
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 100
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_SupplyPoints_Elite",
              "quantity": 200
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 10
            }
          ]
        },
        {
          "offerId": "027A52624DAEE845BA4669A1DB5BD41E",
          "devName": "Magic Chest (Voucher)",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Voucher:Voucher_Chest_Gold",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "CHEST",
              "value": "true"
            },
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Chest.B_StoreButton_Chest'"
            },
            {
              "key": "IsGold",
              "value": "true"
            },
            {
              "key": "AffordOnly",
              "value": "true"
            }
          ],
          "catalogGroup": "Gold Chest",
          "catalogGroupPriority": 10,
          "sortPriority": 72,
          "title": "Magic Chest",
          "shortDescription": "",
          "description": "Core Hero Shards, Magic Tickets and other valuable items",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "A505E68607D146F386B78A517839ED81",
          "devName": "StorefrontMtx.L65000.MtxGift.70",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "014262EC477B66DE83109CA381FED5AD",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "CC60997C47B1FCD9384468BAC133D076",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "65000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 14",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "8989143BA8024C2BBA89391E83BB99D6",
          "devName": "StorefrontMtx.L230000.MtxGift.19",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "1110F75F4FC800DF80F5C4969C7A7E79",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "3D7C6B744A5C5B729A984FA0EF7E8350",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "230000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 34",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "5CF426ED68EE4063A8DFB3BA8CD27281",
          "devName": "StorefrontMtx.L70000.MtxGift.76",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "CC60997C47B1FCD9384468BAC133D076",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "BEAC240147D696F03A55E796BF77ACD7",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "70000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 15",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "7D98BDEAF8A544399D11788935E8F24E",
          "devName": "StorefrontMtx.L990000.MtxGift.111",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "8F30DCC84E3D5ACB54275796E2D75E5B",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "2056F0AF47450E7F5739F6988E4CE902",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "990000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 110",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "8A679D4D1B174E3C8913C5B9F67C91EB",
          "devName": "StorefrontMtx.L430000.MtxGift.43",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "217EAEFF478385E11EA0EC8451C8F2BF",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "621ED4A24CF22364662C8B86D5681DBB",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "430000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 54",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "93A5A8228241406787A04E0DAD49CA70",
          "devName": "StorefrontStacked.Page01.ElementalHeroes.259",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 500,
              "dynamicRegularPrice": -1,
              "finalPrice": 500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 500
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "Type",
              "value": "ElementalHero"
            },
            {
              "key": "HideQuantityRemaining",
              "value": "True"
            }
          ],
          "catalogGroup": "ElementalHeroes",
          "catalogGroupPriority": 259,
          "sortPriority": 72,
          "title": "Elemental Heroes",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 140
            },
            {
              "templateId": "Currency:Hammer",
              "quantity": 4
            },
            {
              "templateId": "Currency:MtxGiveaway",
              "quantity": 100
            },
            {
              "templateId": "Currency:MtxGiveaway",
              "quantity": 100
            },
            {
              "templateId": "Currency:MtxGiveaway",
              "quantity": 100
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 50
            }
          ]
        },
        {
          "offerId": "91208574988D40589F260EE1E473DC9C",
          "devName": "StorefrontMtx.L860000.MtxGift.96",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "983F329B4E8428567D4563A2B427F174",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "04AB19D44110BECA0DE37CAF7632195A",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "860000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 97",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "54B67FB8A7EA4116B23BEF1CB0843919",
          "devName": "StorefrontLevel.L65000.LevelUpChest.29",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 5000,
              "dynamicRegularPrice": -1,
              "finalPrice": 5000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "FC8853B24429F824CE4837B1A3C5B58A",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "2CFBBA1041E1576AD0A0B4AC3CDD4DB8",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "StoreLevelMin",
              "value": "65000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 60,
          "title": "Super Magic Chest",
          "shortDescription": "",
          "description": "A Diamond Hero Crystal, 5000 Magic Tickets and 8 items!",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 5000
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 100
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_SupplyPoints_Elite",
              "quantity": 200
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 10
            }
          ]
        },
        {
          "offerId": "A3F4E0E64EF86C6926881799A0A2306B",
          "devName": "12hr Treasure Hunt",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "VipLevelMin",
              "value": "2"
            },
            {
              "key": "HideWhenEmpty",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 1,
          "sortPriority": 116,
          "title": "12hr Treasure Hunt",
          "shortDescription": "",
          "description": "5 Free Lockpicks, and Random Items for Treasure Hunters!",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "TreasureMap:TM_MapResource",
              "quantity": 5
            }
          ]
        },
        {
          "offerId": "00C859D3544B4A068DD98BA905453CDF",
          "devName": "StorefrontMtx.L180000.MtxGift.13",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "18A5EC98493012C7A7AF869D43CDEE69",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "933C99554A70D66D804FA98829541A99",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "180000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 29",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "3ABB1F431B0642EF963404AAEEA06F0B",
          "devName": "StorefrontStacked.Page01.ElementalHeroes.311",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 500,
              "dynamicRegularPrice": -1,
              "finalPrice": 500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 500
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "Type",
              "value": "ElementalHero"
            },
            {
              "key": "HideQuantityRemaining",
              "value": "True"
            }
          ],
          "catalogGroup": "ElementalHeroes",
          "catalogGroupPriority": 311,
          "sortPriority": 72,
          "title": "Elemental Heroes",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 140
            },
            {
              "templateId": "Currency:Hammer",
              "quantity": 4
            },
            {
              "templateId": "Ore:Ore_Magicite",
              "quantity": 25
            },
            {
              "templateId": "Reagent:Reagent_Shard_Water",
              "quantity": 1
            },
            {
              "templateId": "TreasureMap:TM_WaterfallValley_Map7",
              "quantity": 1
            },
            {
              "templateId": "Reagent:WCCoins",
              "quantity": 5
            }
          ]
        },
        {
          "offerId": "6BDBD627913D4D29B3F964519108DFF3",
          "devName": "StorefrontMtx.L15000.MtxGift.09",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "5796DC4E4A30D4075B12D1A809D1B1CC",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "C92799DE44F0657A1C85C5BF6A1CC2B0",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "15000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 4",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "BB92D0ACAF394753AD5E63DBC16446B9",
          "devName": "StorefrontMtx.L75000.MtxGift.82",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "BEAC240147D696F03A55E796BF77ACD7",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "2F90E8A14D3676B9182AD8B21C227F80",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "75000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 16",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "5237BDCFC050424A8BD2259DD4D8B9DC",
          "devName": "StorefrontMtx.L330000.MtxGift.31",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "7B06B6394E50D13C7248F0947280C2DE",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "68F61AF9403A19EE7CB6B38B33A64EFE",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "330000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 44",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "ECFD8517354946DCA6FA22718F1A9D34",
          "devName": "StorefrontMtx.L30000.MtxGift.27",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "D9467EB349B5955D042B6DB98B0BF2CA",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "C5F31BC54E89D885DEA27695C7F8AF3E",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "30000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 7",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "2A7965024E8D465BA6FEC553DF3B9111",
          "devName": "StorefrontLevel.L230000.LevelUpChest.09",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 5000,
              "dynamicRegularPrice": -1,
              "finalPrice": 5000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "735551394081781279D60F858635BC84",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "33BA8DE54E81E8CFBEE108AC31F3E454",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "StoreLevelMin",
              "value": "230000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 60,
          "title": "Super Magic Chest",
          "shortDescription": "",
          "description": "A Diamond Hero Crystal, 5000 Magic Tickets and 8 items!",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 5000
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 100
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_SupplyPoints_Elite",
              "quantity": 200
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 10
            }
          ]
        },
        {
          "offerId": "C6476F994723A27C298B289058A918EF",
          "devName": "Dark Hero",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Voucher:Voucher_HeroSilver_Dark",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "AffordOnly",
              "value": "true"
            },
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Hero.B_StoreButton_Hero'"
            },
            {
              "key": "type",
              "value": "dark"
            },
            {
              "key": "AutoRedeem",
              "value": "false"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 101,
          "title": "Dark Hero",
          "shortDescription": "",
          "description": "Summon a hero to join your team!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "6E7A466943619D1EE062BC8A09843F5F",
          "devName": "Nature Hero",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Voucher:Voucher_HeroSilver_Nature",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "AffordOnly",
              "value": "true"
            },
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Hero.B_StoreButton_Hero'"
            },
            {
              "key": "type",
              "value": "nature"
            },
            {
              "key": "AutoRedeem",
              "value": "false"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 101,
          "title": "Nature Hero",
          "shortDescription": "",
          "description": "Summon a hero to join your team!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "BA24852247819DFDC572E0A0D5DA7563",
          "devName": "Hero Inventory",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 75,
              "dynamicRegularPrice": -1,
              "finalPrice": 75,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 75
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ServiceName",
              "value": "InventoryUpgrade"
            },
            {
              "key": "type",
              "value": "heroinventory"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 20,
          "title": "+5 Hero Inventory",
          "shortDescription": "",
          "description": "Increases your maximum hero inventory size",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "StandIn:InventoryUpgrade",
              "quantity": 5,
              "attributes": {
                "FakeQuantity": 5
              }
            }
          ]
        },
        {
          "offerId": "755141BDB10248D0B71FF1899D4BF672",
          "devName": "StorefrontMtx.L560000.MtxGift.60",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "59D7755A4258A764FA399CA8C384A3A1",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "A33BE83644AFCC2B562D7EBDF37EC3BC",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "560000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 67",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "1A3A6DF349882AE8D962699646D832EB",
          "devName": "Master of the Hoard (T5)",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "RealMoney",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "2be4ab85c1ae42bab895be28ab6cb99e",
            "bb_viptier5_release",
            "",
            "bb_viptier5_release",
            "",
            "",
            "",
            "",
            "sam_viptier5_release"
          ],
          "requirements": [
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "BE8A7A4F48546D69D0F8DF873120B3E6",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "VipLevelMin",
              "value": "4"
            },
            {
              "key": "AccountLevelMin",
              "value": "100"
            },
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_AccountUpgrade.B_StoreButton_AccountUpgrade'"
            },
            {
              "key": "VipLevelMax",
              "value": "4"
            },
            {
              "key": "type",
              "value": "accountupgrade"
            },
            {
              "key": "InspectItem",
              "value": "Character:Pet_SR1_Cloudpuff_Dark_T05"
            },
            {
              "key": "PreviewFulfillmentClassPath",
              "value": "CatalogFulfillment'/Game/Catalog/Fulfillments/AccountUpgrades/Release_VIP_Tier5.Release_VIP_Tier5'"
            },
            {
              "key": "bShowInGemStore",
              "value": "true"
            }
          ],
          "catalogGroup": "AccountUpgrades",
          "catalogGroupPriority": 0,
          "sortPriority": 40,
          "title": "Master of the Hoard",
          "shortDescription": "A unique pet, extra pets for your Monster Pit, quests, gems, a hero and more!",
          "description": "<RT.CapsGreen>Dreadlord Cloudpuff</> <RT.BasicMed>- a pet that DEVOURS EVERYTHING!</>\r\n\r\n<RT.CapsBlue>Includes Permanent Account Upgrades</>\r\n\r\n<RT.BasicMed>Extra of each Cloudpuff pet for your Monster Pit!</>",
          "displayAssetPath": "/Game/UMG/Textures/Store/btn_StoreGemCastleTreasury.btn_StoreGemCastleTreasury",
          "itemGrants": [
            {
              "templateId": "Character:Pet_SR1_Cloudpuff_Dark_T05",
              "quantity": 2
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 100
            },
            {
              "templateId": "StandIn:ExtraFreeMarketplaceItem",
              "quantity": 1
            },
            {
              "templateId": "StandIn:DailydiscountonMagicChests",
              "quantity": 1
            },
            {
              "templateId": "StandIn:InventoryUpgrade",
              "quantity": 1,
              "attributes": {
                "FakeQuantity": 50
              }
            },
            {
              "templateId": "StandIn:QuestLimit",
              "quantity": 1
            },
            {
              "templateId": "Currency:MtxPurchased",
              "quantity": 1500
            },
            {
              "templateId": "Currency:MtxPurchaseBonus",
              "quantity": 3000
            },
            {
              "templateId": "Character:Pet_SR1_Cloudpuff_Fire_T05",
              "quantity": 1
            },
            {
              "templateId": "Character:Pet_SR1_Cloudpuff_Light_T05",
              "quantity": 1
            },
            {
              "templateId": "Character:Pet_SR1_Cloudpuff_Nature_T05",
              "quantity": 1
            },
            {
              "templateId": "Character:Pet_SR1_Cloudpuff_Water_T05",
              "quantity": 1
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_Shared_MysteryGoo",
              "quantity": 5
            }
          ]
        },
        {
          "offerId": "2813E8EAD8024D068BDFCDAF56D1D0ED",
          "devName": "StorefrontMtx.L410000.MtxGift.41",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "5D2606E94E550BB7A3BDE59294A9A6E9",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "7B18E62F43F3DCDEBF31738AB90E4919",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "410000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 52",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "4EF029313A9D40FBA5AE920512BB1959",
          "devName": "StorefrontMtx.L200000.MtxGift.16",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "23D6690D45EBBE60E00EFE9563C24B89",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "6FC6A72A456C12719AA6488176878E18",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "200000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 31",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "44A778063A9E4114AF436FED6A7F4AF1",
          "devName": "StorefrontMtx.L300000.MtxGift.28",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "F121FD584020B3BB4215BFB6C2723B63",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "24422CC946D4BBEF26BD38B1E8D4F1AB",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "300000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 41",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "FB3DBC14861F449B8F39F020E039E3DD",
          "devName": "StorefrontStacked.Page01.ElementalHeroes.262",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 500,
              "dynamicRegularPrice": -1,
              "finalPrice": 500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 500
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "Type",
              "value": "ElementalHero"
            },
            {
              "key": "HideQuantityRemaining",
              "value": "True"
            }
          ],
          "catalogGroup": "ElementalHeroes",
          "catalogGroupPriority": 262,
          "sortPriority": 72,
          "title": "Elemental Heroes",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 140
            },
            {
              "templateId": "Reagent:Reagent_Shard_Light",
              "quantity": 1
            },
            {
              "templateId": "Reagent:Reagent_Shard_Water",
              "quantity": 1
            },
            {
              "templateId": "Reagent:Reagent_Shard_Dark",
              "quantity": 1
            },
            {
              "templateId": "Reagent:Reagent_Shard_Fire",
              "quantity": 1
            },
            {
              "templateId": "Reagent:Reagent_Shard_Nature",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "1C8A7645673446BBAFE6B8FC20E73024",
          "devName": "StorefrontMtx.L360000.MtxGift.35",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "2AE410184EAB8943E57EABACB2480680",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "44BB81AA4D528D13F5B64F857A30D41A",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "360000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 47",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "16CF01D794EA43A09A86D59BD1A4C0B5",
          "devName": "StorefrontStacked.Page01.ElementalHeroes.434",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 500,
              "dynamicRegularPrice": -1,
              "finalPrice": 500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 500
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "Type",
              "value": "ElementalHero"
            },
            {
              "key": "HideQuantityRemaining",
              "value": "True"
            }
          ],
          "catalogGroup": "ElementalHeroes",
          "catalogGroupPriority": 434,
          "sortPriority": 72,
          "title": "Elemental Heroes",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 140
            },
            {
              "templateId": "Currency:Hammer",
              "quantity": 4
            },
            {
              "templateId": "Reagent:Reagent_Shard_Dark",
              "quantity": 3
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMinor",
              "quantity": 8
            },
            {
              "templateId": "Reagent:Reagent_Shard_Water",
              "quantity": 1
            },
            {
              "templateId": "Reagent:Reagent_Shard_Nature",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "78CE7FF1DC4C43048E0CBE6087F0832F",
          "devName": "StorefrontMtx.L10000.MtxGift.02",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "1E024004419DCE5D80EBC9B0A07D5957",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "5796DC4E4A30D4075B12D1A809D1B1CC",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "10000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 3",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "B95EDE8ACC1048D6A103A8014D741EFA",
          "devName": "StorefrontMtx.L780000.MtxGift.86",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "C64C6E59441A5349F9AE91A876893321",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "6CBE11F4473C198CA22818827EF10200",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "780000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 89",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "58EA7D322B8B4899B7661864BE961B93",
          "devName": "StorefrontMtx.L630000.MtxGift.68",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "C4306C5E41B21FEE9C5192B7617A362E",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "81A9C0044109547F2FC6A285D37B5A8F",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "630000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 74",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "0E8DC9AB6426424EBCF9344ABD01C2FA",
          "devName": "StorefrontMtx.L490000.MtxGift.50",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "03F40DBD424A80428272648B6B6FDA5B",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "105F8AFD4D3AF0210CFBDEBD62E6DCF8",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "490000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 60",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "2BE20BABD3604E69A847695432EBFC51",
          "devName": "StorefrontMtx.L740000.MtxGift.81",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "28A9A2AE472680E9279EAAAC80FE133B",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "5F6B767A47A95247E35E80AE9A702A6E",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "740000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 85",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "E258A1838CA645B287B60F558B43D28D",
          "devName": "StorefrontLevel.L290000.LevelUpChest.12",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 5000,
              "dynamicRegularPrice": -1,
              "finalPrice": 5000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "AB17757F431499E83A7550A80E1A66BC",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "3B8A9D74477DAF56B37DDE84F453A9E5",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "StoreLevelMin",
              "value": "290000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 60,
          "title": "Super Magic Chest",
          "shortDescription": "",
          "description": "A Diamond Hero Crystal, 5000 Magic Tickets and 8 items!",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 5000
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 100
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_SupplyPoints_Elite",
              "quantity": 200
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 10
            }
          ]
        },
        {
          "offerId": "D27930BFF58E46DE91E47576770BAB02",
          "devName": "StorefrontMtx.L240000.MtxGift.20",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "3D7C6B744A5C5B729A984FA0EF7E8350",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "DABF7ABF421751F780FC11BBDFD39273",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "240000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 35",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "C95A3A6C7FB843F7BCB7AE050543CDE8",
          "devName": "StorefrontMtx.L220000.MtxGift.18",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "7E46090E45019AAB5F8BCEBD6BCB33F8",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "1110F75F4FC800DF80F5C4969C7A7E79",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "220000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 33",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "BC6B9262EFD24623ABFE28A145A39191",
          "devName": "StorefrontMtx.L150000.MtxGift.10",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "B3EC21C9458D51BEB1BA22999A375658",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "85CCBB5D4A8BFFD46A252F8401CC2BBC",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "150000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 26",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "AC14388926684BD8BEF7981099996B34",
          "devName": "StorefrontLevel.L390000.LevelUpChest.18",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 5000,
              "dynamicRegularPrice": -1,
              "finalPrice": 5000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "4685928D450EBBA5B93598A2F37CFFF6",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "C1580AC74C42EEC07C38AB84A73A3A70",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "StoreLevelMin",
              "value": "390000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 60,
          "title": "Super Magic Chest",
          "shortDescription": "",
          "description": "A Diamond Hero Crystal, 5000 Magic Tickets and 8 items!",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 5000
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 100
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_SupplyPoints_Elite",
              "quantity": 200
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 10
            }
          ]
        },
        {
          "offerId": "9F5D14DBF6A346CB95C7FDC036469CF3",
          "devName": "StorefrontMtx.L570000.MtxGift.61",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "A33BE83644AFCC2B562D7EBDF37EC3BC",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "B1BF9CB842881A9E2E5D4CABB1F932F5",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "570000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 68",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "E2CA822D40AEA5AB943DAB975B3038CB",
          "devName": "Gold Hero",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Voucher:Voucher_HeroGold",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "AffordOnly",
              "value": "true"
            },
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Hero.B_StoreButton_Hero'"
            },
            {
              "key": "type",
              "value": "gold"
            },
            {
              "key": "AutoRedeem",
              "value": "false"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 102,
          "title": "Gold Hero",
          "shortDescription": "",
          "description": "Add a powerful very rare or higher hero to your team!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "F576C3C4BC21415E8CE3146BE68C6C6F",
          "devName": "StorefrontMtx.L170000.MtxGift.12",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "E9A7C0524017B2C6740E14849A88DAA2",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "18A5EC98493012C7A7AF869D43CDEE69",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "170000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 28",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "A1EDCFBAEC4B4A7DB26CAFD1A40DFA71",
          "devName": "StorefrontMtx.L670000.MtxGift.73",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "9CBA0101494E26B58A5408872F3C4353",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "E053B31F4111B3AF758685885D5CBED9",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "670000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 78",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "BB46761F58ED4260811483F3E2AA544D",
          "devName": "StorefrontStacked.Page01.ElementalHeroes.166",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 500,
              "dynamicRegularPrice": -1,
              "finalPrice": 500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 500
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "Type",
              "value": "ElementalHero"
            },
            {
              "key": "HideQuantityRemaining",
              "value": "True"
            }
          ],
          "catalogGroup": "ElementalHeroes",
          "catalogGroupPriority": 166,
          "sortPriority": 72,
          "title": "Elemental Heroes",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 140
            },
            {
              "templateId": "Currency:Hammer",
              "quantity": 4
            },
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 200
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 5
            },
            {
              "templateId": "Reagent:Reagent_Shared_T02",
              "quantity": 50
            },
            {
              "templateId": "Reagent:Reagent_Shard_Water",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "2397FE674EA1F134D3C8B2A21B53F131",
          "devName": "Drake",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Voucher:Voucher_Hero_Mage_Fire_BurningSword",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "AffordOnly",
              "value": "true"
            },
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Hero.B_StoreButton_Hero'"
            },
            {
              "key": "type",
              "value": "Random"
            },
            {
              "key": "AutoRedeem",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 9999,
          "title": "Drake",
          "shortDescription": "",
          "description": "Free Drake from his crystal!",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Character:Mage_Starter_Fire_BurningSwordCombo_T03",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "F2BACD7BABA64833B4563E71D778B516",
          "devName": "StorefrontMtx.L120000.MtxGift.06",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "1369D9784B1B9096135B08BD23386E2D",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "A21C10754CF2A279F3E72E959D1D7A6C",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "120000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 23",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "2B3B76515F044F84A2AB7A8EF16CBF17",
          "devName": "StorefrontMtx.L320000.MtxGift.30",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "4EB892244CC62635C6631D97E8A4DDAD",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "7B06B6394E50D13C7248F0947280C2DE",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "320000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 43",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "D7A61CEE232947F2A381B0B215928C2F",
          "devName": "StorefrontMtx.L540000.MtxGift.57",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "75A4D216442030897C9954A407FF0D5E",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "9527715345720336DC2B3C88C4A56130",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "540000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 65",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "ECA4EAF1D6F743C1B1E52724871501ED",
          "devName": "StorefrontMtx.L1000.MtxGift.01",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "0C425A7840E80B644949B2AD5291BD98",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "1000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 1",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "514EE1B2422FB17AB8F8618B385F66FA",
          "devName": "Basic Chest (Silver)",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 100,
              "dynamicRegularPrice": -1,
              "finalPrice": 100,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 100
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "DAILYCHEST",
              "value": "true"
            },
            {
              "key": "type",
              "value": "dailylootbox"
            },
            {
              "key": "AccountLevelMin",
              "value": "4"
            },
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles_Small.B_StoreButton_Bundles_Small'"
            }
          ],
          "catalogGroup": "Silver Chest",
          "catalogGroupPriority": 0,
          "sortPriority": 115,
          "title": "Basic Chest",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 100
            },
            {
              "templateId": "Currency:Hammer",
              "quantity": 4
            }
          ]
        },
        {
          "offerId": "FBA88017C7ED4E24AD29A55FF2A8AFEC",
          "devName": "StorefrontLevel.L490000.LevelUpChest.23",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 5000,
              "dynamicRegularPrice": -1,
              "finalPrice": 5000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "CC1A5B204B3FDB3CBAF3AFA3211D4307",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "90C2A42E4DD0334F1E67DEA8D228B8F0",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "StoreLevelMin",
              "value": "490000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 60,
          "title": "Super Magic Chest",
          "shortDescription": "",
          "description": "A Diamond Hero Crystal, 5000 Magic Tickets and 8 items!",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 5000
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 100
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_SupplyPoints_Elite",
              "quantity": 200
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 10
            }
          ]
        },
        {
          "offerId": "6DF17286032D4A818AAF86C100B06AB1",
          "devName": "StorefrontMtx.L80000.MtxGift.88",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "2F90E8A14D3676B9182AD8B21C227F80",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "A53DFF334DBCB6079E9D1A9AB22F902C",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "80000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 17",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "6E0A0982102E4273B8B9348EC2FC1B56",
          "devName": "StorefrontLevel.L270000.LevelUpChest.11",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 5000,
              "dynamicRegularPrice": -1,
              "finalPrice": 5000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "BD992F7F42063F197AB4EC921CD0BC16",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "AB17757F431499E83A7550A80E1A66BC",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "StoreLevelMin",
              "value": "270000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 60,
          "title": "Super Magic Chest",
          "shortDescription": "",
          "description": "A Diamond Hero Crystal, 5000 Magic Tickets and 8 items!",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 5000
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 100
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_SupplyPoints_Elite",
              "quantity": 200
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 10
            }
          ]
        },
        {
          "offerId": "8D62CBA909BC49C4BBFC1D3A26043E27",
          "devName": "StorefrontStacked.Page01.ElementalHeroes.102",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 500,
              "dynamicRegularPrice": -1,
              "finalPrice": 500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 500
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "Type",
              "value": "ElementalHero"
            },
            {
              "key": "HideQuantityRemaining",
              "value": "True"
            }
          ],
          "catalogGroup": "ElementalHeroes",
          "catalogGroupPriority": 102,
          "sortPriority": 72,
          "title": "Elemental Heroes",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 140
            },
            {
              "templateId": "Currency:Hammer",
              "quantity": 4
            },
            {
              "templateId": "Ore:Ore_Magicite",
              "quantity": 35
            },
            {
              "templateId": "Reagent:Reagent_RXT_Parts_Small",
              "quantity": 5
            },
            {
              "templateId": "Currency:Gold",
              "quantity": 100000
            },
            {
              "templateId": "Currency:Hammer",
              "quantity": 3
            }
          ]
        },
        {
          "offerId": "E50D5FCCC2C44C4681BE63FDE8A5C731",
          "devName": "StorefrontMtx.L920000.MtxGift.103",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "AA2F5806432BBFC19852F78A885B0659",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "3EEBE6C44ADC45AAD484B19A00BD9134",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "920000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 103",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "C554B16748E84873B5953ADB1C502025",
          "devName": "StorefrontLevel.L210000.LevelUpChest.08",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 5000,
              "dynamicRegularPrice": -1,
              "finalPrice": 5000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "D3E0B11D45BF46F1353F309ABC413135",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "735551394081781279D60F858635BC84",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "StoreLevelMin",
              "value": "210000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 60,
          "title": "Super Magic Chest",
          "shortDescription": "",
          "description": "A Diamond Hero Crystal, 5000 Magic Tickets and 8 items!",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 5000
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 100
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_SupplyPoints_Elite",
              "quantity": 200
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 10
            }
          ]
        },
        {
          "offerId": "68C82ED49FA34AEF8D2B8A3F9C0DF0DF",
          "devName": "StorefrontMtx.L640000.MtxGift.69",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "81A9C0044109547F2FC6A285D37B5A8F",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "75C7E43249236441B9002F8B752C6117",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "640000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 75",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "5A8C3360408F40E3839FDAE5DF2380DD",
          "devName": "StorefrontMtx.L850000.MtxGift.95",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "594167794856DBCA4304328EDC133E15",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "983F329B4E8428567D4563A2B427F174",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "850000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 96",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "9A2BE5888F4D4BFE874D0CCB292DA9B4",
          "devName": "StorefrontLevel.L170000.LevelUpChest.05",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 5000,
              "dynamicRegularPrice": -1,
              "finalPrice": 5000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "4E0DF6CB4D36D1EF2CC5CBAA87EE65B1",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "96AF5DA3462C0C7D5C35CD9104F4527B",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "StoreLevelMin",
              "value": "170000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 60,
          "title": "Super Magic Chest",
          "shortDescription": "",
          "description": "A Diamond Hero Crystal, 5000 Magic Tickets and 8 items!",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 5000
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 100
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_SupplyPoints_Elite",
              "quantity": 200
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 10
            }
          ]
        },
        {
          "offerId": "590CF0040E92446A844487CB525E6670",
          "devName": "StorefrontMtx.L960000.MtxGift.108",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "9D90D9D043CA0596F6266EB2C3DC9C64",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "2502E968436E5D2DF78BB1A266AA3C5B",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "960000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 107",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "0CF30DAE0AAD4F5C84E77B4CE11CC8C3",
          "devName": "StorefrontLevel.L130000.LevelUpChest.03",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 5000,
              "dynamicRegularPrice": -1,
              "finalPrice": 5000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "62A30DED4F2E3F8863CE0DB8B97125D5",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "FE6C666D41BCDBA0704ED29B8A1FD492",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "StoreLevelMin",
              "value": "130000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 60,
          "title": "Super Magic Chest",
          "shortDescription": "",
          "description": "A Diamond Hero Crystal, 5000 Magic Tickets and 8 items!",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 5000
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 100
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_SupplyPoints_Elite",
              "quantity": 200
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 10
            }
          ]
        },
        {
          "offerId": "3335B52DB36C420E9C895A68B3BD022B",
          "devName": "StorefrontMtx.L680000.MtxGift.74",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "E053B31F4111B3AF758685885D5CBED9",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "156018564EE5F273B9CED8AA57AEDC62",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "680000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 79",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "D2D01CE41D784BEC9D290052AAEBE0F4",
          "devName": "StorefrontMtx.L750000.MtxGift.83",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "5F6B767A47A95247E35E80AE9A702A6E",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "95D438054A0CFA5ECC5EF582961AD9FC",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "750000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 86",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "FB6B59AF4C220FECC40AB191117F097E",
          "devName": "Fire Hero",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Voucher:Voucher_HeroSilver_Fire",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "AffordOnly",
              "value": "true"
            },
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Hero.B_StoreButton_Hero'"
            },
            {
              "key": "type",
              "value": "fire"
            },
            {
              "key": "AutoRedeem",
              "value": "false"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 101,
          "title": "Fire Hero",
          "shortDescription": "",
          "description": "Summon a hero to join your team!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "39F07E3E516543E0BCBC9A859AC9702A",
          "devName": "StorefrontMtx.L480000.MtxGift.49",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "DA4EB1D64213B51C77AE75B0DFC453EF",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "03F40DBD424A80428272648B6B6FDA5B",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "480000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 59",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "1F0A4B5E9692404FBE92F2782061477C",
          "devName": "StorefrontMtx.L25000.MtxGift.21",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "1DA1BAEC49524F730C07AA9D285CDDB3",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "D9467EB349B5955D042B6DB98B0BF2CA",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "25000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 6",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "D1F92D5C4225429DBC2EE8F02136C6E1",
          "devName": "StorefrontMtx.L820000.MtxGift.91",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "82A8D4B544A9DC38C604F0A54305097C",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "AE3B458F433DE9BEF76CFFAFA6E5824B",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "820000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 93",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "C18AE9179A5547F7BCFEBECE59DD3CE2",
          "devName": "StorefrontMtx.L510000.MtxGift.54",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "2BFCE5B9460735E737669585D1895444",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "06EED93D416CC285D8F887BA31411157",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "510000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 62",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "32277ADF4C9D4C1FA8D9A7334A9AE5A7",
          "devName": "StorefrontLevel.L510000.LevelUpChest.25",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 5000,
              "dynamicRegularPrice": -1,
              "finalPrice": 5000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "90C2A42E4DD0334F1E67DEA8D228B8F0",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "2505AD4D4B9A19FBB46D0B9EBC1EA56C",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "StoreLevelMin",
              "value": "510000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 60,
          "title": "Super Magic Chest",
          "shortDescription": "",
          "description": "A Diamond Hero Crystal, 5000 Magic Tickets and 8 items!",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 5000
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 100
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_SupplyPoints_Elite",
              "quantity": 200
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 10
            }
          ]
        },
        {
          "offerId": "6443EFAC8C5F487F8B0783D62C2CB7F1",
          "devName": "StorefrontLevel.L80000.LevelUpChest.30",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 5000,
              "dynamicRegularPrice": -1,
              "finalPrice": 5000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "2CFBBA1041E1576AD0A0B4AC3CDD4DB8",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "1CE9D551409C5DF76678DBBD81B4FDB9",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "StoreLevelMin",
              "value": "80000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 60,
          "title": "Super Magic Chest",
          "shortDescription": "",
          "description": "A Diamond Hero Crystal, 5000 Magic Tickets and 8 items!",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 5000
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 100
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_SupplyPoints_Elite",
              "quantity": 200
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 10
            }
          ]
        },
        {
          "offerId": "E7C8F4A5BEF346569914B0911F685243",
          "devName": "StorefrontMtx.L900000.MtxGift.101",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "B0DE74BB4B8CE1FE2370A5B60FBBA4EF",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "163B90B54347AA6F1BA40AA087DADF38",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "900000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 101",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "8B48FD5A28A84BF6ACBF802869C885AA",
          "devName": "StorefrontMtx.L55000.MtxGift.58",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "713EA5E949A65138904884983F430D2F",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "E83060694EC9CA80654B84AF64340D5D",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "55000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 12",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "13086EDC4986EA7550441BB6DDEBC650",
          "devName": "12HR Basic Chest (Silver) - 75",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 100,
              "dynamicRegularPrice": -1,
              "finalPrice": 75,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 75
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "DAILYCHEST",
              "value": "true"
            },
            {
              "key": "type",
              "value": "dailylootbox"
            },
            {
              "key": "AccountLevelMin",
              "value": "4"
            },
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles_Small.B_StoreButton_Bundles_Small'"
            }
          ],
          "catalogGroup": "Silver Chest",
          "catalogGroupPriority": 1,
          "sortPriority": 115,
          "title": "12hr Basic Chest",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 100
            },
            {
              "templateId": "Currency:Hammer",
              "quantity": 4
            }
          ]
        },
        {
          "offerId": "CB55B1898B9E4C49A5280C544489EDFF",
          "devName": "StorefrontMtx.L420000.MtxGift.42",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "7B18E62F43F3DCDEBF31738AB90E4919",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "217EAEFF478385E11EA0EC8451C8F2BF",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "420000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 53",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "0F327F384EB8476EBBBA585D6C29851A",
          "devName": "StorefrontStacked.Page01.ElementalHeroes.131",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 500,
              "dynamicRegularPrice": -1,
              "finalPrice": 500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 500
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "Type",
              "value": "ElementalHero"
            },
            {
              "key": "HideQuantityRemaining",
              "value": "True"
            }
          ],
          "catalogGroup": "ElementalHeroes",
          "catalogGroupPriority": 131,
          "sortPriority": 72,
          "title": "Elemental Heroes",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 140
            },
            {
              "templateId": "Currency:Hammer",
              "quantity": 4
            },
            {
              "templateId": "TreasureMap:TM_MapResource",
              "quantity": 15
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMinor",
              "quantity": 10
            },
            {
              "templateId": "Currency:Hammer",
              "quantity": 3
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMinor",
              "quantity": 5
            }
          ]
        },
        {
          "offerId": "E6B8C4BC6E2C419B99A40B122846041D",
          "devName": "StorefrontMtx.L580000.MtxGift.62",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "B1BF9CB842881A9E2E5D4CABB1F932F5",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "9632B0144E806B1508858E8526C8C7D2",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "580000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 69",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "F2CA40651937441F89CD9159E79CAE4C",
          "devName": "StorefrontStacked.Page01.ElementalHeroes.361",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 500,
              "dynamicRegularPrice": -1,
              "finalPrice": 500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 500
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "Type",
              "value": "ElementalHero"
            },
            {
              "key": "HideQuantityRemaining",
              "value": "True"
            }
          ],
          "catalogGroup": "ElementalHeroes",
          "catalogGroupPriority": 361,
          "sortPriority": 72,
          "title": "Elemental Heroes",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 140
            },
            {
              "templateId": "Currency:Hammer",
              "quantity": 4
            },
            {
              "templateId": "TreasureMap:TM_Special_UnderwaterForest",
              "quantity": 1
            },
            {
              "templateId": "Reagent:Reagent_Misc_CeremonialSword",
              "quantity": 1
            },
            {
              "templateId": "Reagent:Reagent_Shared_T02",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 2
            }
          ]
        },
        {
          "offerId": "84D0111E4E03D3ABF723AAA9E2070047",
          "devName": "Team Slot",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 150,
              "dynamicRegularPrice": -1,
              "finalPrice": 150,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 150
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "233CFA5B48709E1D65BD5F8FA57EA5DA",
              "minQuantity": 5
            }
          ],
          "metaInfo": [
            {
              "key": "ServiceName",
              "value": "InventoryUpgrade"
            },
            {
              "key": "type",
              "value": "teamslot"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 19,
          "title": "+1 Team Slot",
          "shortDescription": "",
          "description": "Increases your maximum number of teams by 1 and maximum hero inventory by 5",
          "displayAssetPath": "/Game/UMG/Textures/Icons/AccountUpgradeItems/T_Team_Slots.T_Team_Slots",
          "itemGrants": [
            {
              "templateId": "Party:Instance",
              "quantity": 1
            },
            {
              "templateId": "StandIn:TeamSlotsUpgrade",
              "quantity": 1,
              "attributes": {
                "FakeQuantity": 1
              }
            },
            {
              "templateId": "StandIn:InventoryUpgrade",
              "quantity": 1,
              "attributes": {
                "FakeQuantity": 5
              }
            }
          ]
        },
        {
          "offerId": "4AAFA1673E3141ABB0F2AF09714F27E2",
          "devName": "StorefrontMtx.L610000.MtxGift.66",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "99C4CD6341895994F96C418162800C4B",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "4A6141634D3AC5AC701DD0B2F0AD8F9E",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "610000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 72",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "960FC988A26E413784BC2C14B9B9476C",
          "devName": "StorefrontMtx.L190000.MtxGift.14",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "933C99554A70D66D804FA98829541A99",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "23D6690D45EBBE60E00EFE9563C24B89",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "190000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 30",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "6FA8142C85A247DC9FC72F31B50640D1",
          "devName": "StorefrontMtx.L660000.MtxGift.72",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "FFAE4C824BC126932854A6A3199B1EB8",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "9CBA0101494E26B58A5408872F3C4353",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "660000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 77",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "C432DBE71C6144D98FBB849D1BE01BAF",
          "devName": "StorefrontStacked.Page01.ElementalHeroes.174",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 500,
              "dynamicRegularPrice": -1,
              "finalPrice": 500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 500
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "Type",
              "value": "ElementalHero"
            },
            {
              "key": "HideQuantityRemaining",
              "value": "True"
            }
          ],
          "catalogGroup": "ElementalHeroes",
          "catalogGroupPriority": 174,
          "sortPriority": 72,
          "title": "Elemental Heroes",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 140
            },
            {
              "templateId": "Currency:Hammer",
              "quantity": 4
            },
            {
              "templateId": "Reagent:Reagent_Shared_MysteryGoo",
              "quantity": 1
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMinor",
              "quantity": 5
            },
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 1
            },
            {
              "templateId": "Reagent:Reagent_Shared_T02",
              "quantity": 35
            }
          ]
        },
        {
          "offerId": "AD01C48577C34BACAC8F5F8BA932A9FB",
          "devName": "StorefrontMtx.L940000.MtxGift.105",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "2468A46347C548FE8C4702A77B29CE07",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "4C16D22849A940EFD2805FA3770F4289",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "940000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 105",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "FEB439F03D9345099C012D82E36875A9",
          "devName": "StorefrontMtx.L260000.MtxGift.23",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "82C167B44E347F8BD9E219832900351C",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "30919EB548919E3CF1BAB6B4BD4819A6",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "260000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 37",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "8588ED0351984C47943B6C15740E2785",
          "devName": "StorefrontMtx.L1000000.MtxGift.04",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "2056F0AF47450E7F5739F6988E4CE902",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "5BCAA5BA43680543482B429D3A2558B5",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "1000000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 111",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "912DCAF2533047178E59CAAA87474695",
          "devName": "StorefrontMtx.L650000.MtxGift.71",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "75C7E43249236441B9002F8B752C6117",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "FFAE4C824BC126932854A6A3199B1EB8",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "650000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 76",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "BA34F0F54407C1A6C6DE75AEF04555C9",
          "devName": "12HR Basic Chest (Silver) - 50",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 100,
              "dynamicRegularPrice": -1,
              "finalPrice": 50,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 50
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "DAILYCHEST",
              "value": "true"
            },
            {
              "key": "type",
              "value": "dailylootbox"
            },
            {
              "key": "AccountLevelMin",
              "value": "4"
            },
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles_Small.B_StoreButton_Bundles_Small'"
            }
          ],
          "catalogGroup": "Silver Chest",
          "catalogGroupPriority": 2,
          "sortPriority": 115,
          "title": "12hr Basic Chest",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 100
            },
            {
              "templateId": "Currency:Hammer",
              "quantity": 4
            }
          ]
        },
        {
          "offerId": "12F2000A4BE70D0E848622A2AB0B4784",
          "devName": "Battle Hero",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Voucher:Voucher_HeroBattle",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "AffordOnly",
              "value": "true"
            },
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Hero.B_StoreButton_Hero'"
            },
            {
              "key": "type",
              "value": "battle"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 108,
          "title": "Battle Hero",
          "shortDescription": "",
          "description": "Add a powerful hero to your team!",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Character:SpiritWarrior_SR2_Fire_IronMonkey_T04",
              "quantity": 1
            },
            {
              "templateId": "Character:HolyKnight_SR2_Light_Seraph_T05",
              "quantity": 1
            },
            {
              "templateId": "Character:Warrior_SR2_Nature_Behemoth_T05",
              "quantity": 1
            },
            {
              "templateId": "Character:Spellsword_SR2_Dark_DarkGale_T05",
              "quantity": 1
            },
            {
              "templateId": "Character:Ninja_SR2_Fire_DeathBlossom_T05",
              "quantity": 1
            },
            {
              "templateId": "Character:DragonKnight_SR1_Water_DragonForm_T05",
              "quantity": 1
            },
            {
              "templateId": "Character:Mage_SR2_Water_Blizzard_T05",
              "quantity": 1
            },
            {
              "templateId": "Character:Assassin_SR2_Dark_PhantomDash_T05",
              "quantity": 1
            },
            {
              "templateId": "Character:Blademaster_SR2_Water_SpinningEdge_T05",
              "quantity": 1
            },
            {
              "templateId": "Character:Shadowknight_SR2_Fire_Reaver_T05",
              "quantity": 1
            },
            {
              "templateId": "Character:Mage_SR2_Light_Anubis_T04",
              "quantity": 1
            },
            {
              "templateId": "Character:Warmage_SR2_Nature_Earthquake_T05",
              "quantity": 1
            },
            {
              "templateId": "Character:Ninja_SR2_Dark_Zed_T05",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "2A9FE2864271324688238A93EA48350F",
          "devName": "Battle Pass (Recurring)",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "RealMoney",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": 1,
          "refundable": false,
          "appStoreId": [
            "",
            "1bb845075f334ecaae7b55e421ab3dea",
            "bb_battlepass",
            "",
            "bb_battlepass",
            "",
            "",
            "",
            "",
            "sam_battlepass"
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "BonusOverride",
              "value": "3000"
            },
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Battlepass.B_StoreButton_Battlepass'"
            }
          ],
          "catalogGroup": "BattlePass",
          "catalogGroupPriority": 1,
          "sortPriority": 500,
          "title": "Battle Pass",
          "shortDescription": "",
          "description": "100 Gems every day for 30 days\r\nUnlocks premium Battle Pass rewards",
          "displayAssetPath": "/Game/UMG/Textures/Store/btn_StoreGemBag.btn_StoreGemBag",
          "itemGrants": []
        },
        {
          "offerId": "4F06CD5B4A764BDAE79A6FA00F4CB161",
          "devName": "Battle Breaker (T1)",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "RealMoney",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "11b1aad3c22d4fe58c361b8c913477d6",
            "bb_viptier1_release",
            "",
            "bb_viptier1_release",
            "",
            "",
            "",
            "",
            "sam_viptier1_release"
          ],
          "requirements": [
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "BE8A7A4F48546D69D0F8DF873120B3E6",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "VipLevelMin",
              "value": "0"
            },
            {
              "key": "AccountLevelMin",
              "value": "0"
            },
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_AccountUpgrade.B_StoreButton_AccountUpgrade'"
            },
            {
              "key": "VipLevelMax",
              "value": "0"
            },
            {
              "key": "type",
              "value": "accountupgrade"
            },
            {
              "key": "InspectItem",
              "value": "Character:Pet_SR1_Cloudpuff_Nature_T05"
            },
            {
              "key": "PreviewFulfillmentClassPath",
              "value": "CatalogFulfillment'/Game/Catalog/Fulfillments/AccountUpgrades/Release_VIP_Tier1.Release_VIP_Tier1'"
            },
            {
              "key": "bShowInGemStore",
              "value": "true"
            }
          ],
          "catalogGroup": "AccountUpgrades",
          "catalogGroupPriority": 0,
          "sortPriority": 40,
          "title": "Battle Breaker Collection",
          "shortDescription": "A unique pet, free daily chests, more teams, quests, gems, a hero and more!",
          "description": "<RT.CapsGreen>Chocolate Cloudpuff</> <RT.BasicMed> - A pet that attacks all enemies!</>\r\n\r\n<RT.CapsBlue>Includes Permanent Account Upgrades</>\r\n\r\n<RT.BasicMed>Free Basic Chests contain 4 Hammers and 100 Magic Tickets</>",
          "displayAssetPath": "/Game/UMG/Textures/Store/btn_StoreGemGoldenChest.btn_StoreGemGoldenChest",
          "itemGrants": [
            {
              "templateId": "Party:Instance",
              "quantity": 3
            },
            {
              "templateId": "Character:Pet_SR1_Cloudpuff_Nature_T05",
              "quantity": 1
            },
            {
              "templateId": "StandIn:FreeTwiceDailyLootBox",
              "quantity": 1
            },
            {
              "templateId": "StandIn:TeamSlotsUpgrade",
              "quantity": 1,
              "attributes": {
                "FakeQuantity": 3
              }
            },
            {
              "templateId": "StandIn:InventoryUpgrade",
              "quantity": 1,
              "attributes": {
                "FakeQuantity": 15
              }
            },
            {
              "templateId": "StandIn:QuestLimit",
              "quantity": 1,
              "attributes": {
                "FakeQuantity": 1
              }
            },
            {
              "templateId": "Currency:MtxPurchased",
              "quantity": 1500
            },
            {
              "templateId": "Currency:MtxPurchaseBonus",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 500
            }
          ]
        },
        {
          "offerId": "DD47D093977147099DBDCD8880D6690F",
          "devName": "StorefrontMtx.L140000.MtxGift.08",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "9E833A024D8FD5EAD1C4AD83D739AD24",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "B3EC21C9458D51BEB1BA22999A375658",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "140000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 25",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "0C7081BD42D0497891D134ACF1F121E3",
          "devName": "StorefrontMtx.L270000.MtxGift.24",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "30919EB548919E3CF1BAB6B4BD4819A6",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "6EC4CB2241CDD5FFA61D059F0266A988",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "270000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 38",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "4D80E4E8AC384F49A12F10A08E139A31",
          "devName": "StorefrontLevel.L430000.LevelUpChest.20",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 5000,
              "dynamicRegularPrice": -1,
              "finalPrice": 5000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "D0A62F8540F76D50B172988D31FF1B47",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "B949A38F4F1AFF040AF09EA67355F09B",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "StoreLevelMin",
              "value": "430000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 60,
          "title": "Super Magic Chest",
          "shortDescription": "",
          "description": "A Diamond Hero Crystal, 5000 Magic Tickets and 8 items!",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 5000
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 100
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_SupplyPoints_Elite",
              "quantity": 200
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 10
            }
          ]
        },
        {
          "offerId": "BA86647B407D2BFA34518093A26CB26B",
          "devName": "Heroic Chest (Monthly)",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 1500,
              "dynamicRegularPrice": -1,
              "finalPrice": 1500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1500
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": 1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "CHEST",
              "value": "true"
            },
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "IsGold",
              "value": "true"
            },
            {
              "key": "StoreLevelMin",
              "value": "1000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 66,
          "title": "Heroic Chest",
          "shortDescription": "",
          "description": "Contains at least 10 hero crystals, including at least 5 silver or better! Available monthly.",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 1500
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 10
            },
            {
              "templateId": "Currency:SkillXP",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_Shard_Dark",
              "quantity": 10
            },
            {
              "templateId": "Reagent:Reagent_Shard_Fire",
              "quantity": 10
            },
            {
              "templateId": "Reagent:Reagent_Shard_Light",
              "quantity": 10
            },
            {
              "templateId": "Reagent:Reagent_Shard_Nature",
              "quantity": 10
            },
            {
              "templateId": "Reagent:Reagent_Shard_Water",
              "quantity": 10
            },
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 1500
            }
          ]
        },
        {
          "offerId": "D2AA14F471D940B3B886850283CFB3D5",
          "devName": "StorefrontMtx.L100000.MtxGift.03",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "FF31B86842EFA7A884529E90768AE3D3",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "7696BED040A499C469CBB9BA6A24F830",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "100000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 21",
          "shortDescription": "",
          "description": "Holy Wukong, you're amazing!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "4AD5A49787A24EB381BC2704CFF45D23",
          "devName": "StorefrontMtx.L690000.MtxGift.75",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "156018564EE5F273B9CED8AA57AEDC62",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "B133B6DC440D5686E38D49BBE35CD861",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "690000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 80",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "4115479349B94BE7AB11135FF8542A04",
          "devName": "StorefrontLevel.L190000.LevelUpChest.06",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 5000,
              "dynamicRegularPrice": -1,
              "finalPrice": 5000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "96AF5DA3462C0C7D5C35CD9104F4527B",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "D3E0B11D45BF46F1353F309ABC413135",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "StoreLevelMin",
              "value": "190000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 60,
          "title": "Super Magic Chest",
          "shortDescription": "",
          "description": "A Diamond Hero Crystal, 5000 Magic Tickets and 8 items!",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 5000
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 100
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_SupplyPoints_Elite",
              "quantity": 200
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 10
            }
          ]
        },
        {
          "offerId": "738EDDCB487527431B5F4EAF8910BDC6",
          "devName": "Forgotten Crystal",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Voucher:Voucher_Hero_Custom_Interceptor",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "AffordOnly",
              "value": "true"
            },
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Hero.B_StoreButton_Hero'"
            },
            {
              "key": "type",
              "value": "Random"
            },
            {
              "key": "AutoRedeem",
              "value": ""
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 109,
          "title": "Forgotten Crystal",
          "shortDescription": "",
          "description": "Crack it open to find something special!",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Character:Knight_VR2_Dark_Interceptor_T04",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "948A70086E534831A04D844F6BA480FD",
          "devName": "StorefrontMtx.L50000.MtxGift.52",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "8352FBF848AB462C24BEEFABE6E373C0",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "713EA5E949A65138904884983F430D2F",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "50000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 11",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "4F9CA9E2D6754B9882A9373921421099",
          "devName": "StorefrontMtx.L210000.MtxGift.17",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "6FC6A72A456C12719AA6488176878E18",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "7E46090E45019AAB5F8BCEBD6BCB33F8",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "210000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 32",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "211FAECFED4E4D9D9D784A7EC675CD5B",
          "devName": "StorefrontLevel.L330000.LevelUpChest.14",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 5000,
              "dynamicRegularPrice": -1,
              "finalPrice": 5000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "E65689DC44393C8ED32C3EA98549786A",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "2F18BCC44E753971B12564A1449C37B5",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "StoreLevelMin",
              "value": "330000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 60,
          "title": "Super Magic Chest",
          "shortDescription": "",
          "description": "A Diamond Hero Crystal, 5000 Magic Tickets and 8 items!",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 5000
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 100
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_SupplyPoints_Elite",
              "quantity": 200
            },
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 50
            },
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 10
            }
          ]
        },
        {
          "offerId": "2DD7DF340036421CA48D4094A5F67BEE",
          "devName": "StorefrontStacked.Page01.ElementalHeroes.148",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 500,
              "dynamicRegularPrice": -1,
              "finalPrice": 500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 500
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "Type",
              "value": "ElementalHero"
            },
            {
              "key": "HideQuantityRemaining",
              "value": "True"
            }
          ],
          "catalogGroup": "ElementalHeroes",
          "catalogGroupPriority": 148,
          "sortPriority": 72,
          "title": "Elemental Heroes",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 140
            },
            {
              "templateId": "Currency:Hammer",
              "quantity": 4
            },
            {
              "templateId": "Reagent:Reagent_Shard_Nature",
              "quantity": 3
            },
            {
              "templateId": "Reagent:Reagent_Foil",
              "quantity": 15
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMinor",
              "quantity": 5
            },
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 100
            }
          ]
        },
        {
          "offerId": "BACD1EBF30054A51BE04F6C4836E8387",
          "devName": "StorefrontStacked.Page01.ElementalHeroes.89",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 500,
              "dynamicRegularPrice": -1,
              "finalPrice": 500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 500
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "Type",
              "value": "ElementalHero"
            },
            {
              "key": "HideQuantityRemaining",
              "value": "True"
            }
          ],
          "catalogGroup": "ElementalHeroes",
          "catalogGroupPriority": 89,
          "sortPriority": 72,
          "title": "Elemental Heroes",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 140
            },
            {
              "templateId": "Currency:Hammer",
              "quantity": 4
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 150
            },
            {
              "templateId": "Reagent:Reagent_Foil",
              "quantity": 15
            },
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 1
            },
            {
              "templateId": "Reagent:Reagent_Shard_Light",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "B022D1E267054BFF9DCF24818AD903EC",
          "devName": "StorefrontMtx.L85000.MtxGift.94",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "A53DFF334DBCB6079E9D1A9AB22F902C",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "E462EAA14B27F738FAC2B6B8428DD2FA",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "85000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 18",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "70355DD2040E4BA28092B4CAD3845F42",
          "devName": "StorefrontMtx.L710000.MtxGift.78",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "47201DAA4E39ECA176CD35AA4CF9A699",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "4F5DC10D401646573926DCA4714C2832",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "710000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 82",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "ADABB65340E1355361F29B95C23C808A",
          "devName": "Magic Tickets (Weekly)",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 600,
              "dynamicRegularPrice": -1,
              "finalPrice": 600,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 600
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": 1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "CHEST",
              "value": "true"
            },
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "IsGold",
              "value": "true"
            },
            {
              "key": "StoreLevelMin",
              "value": "10000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 64,
          "title": "Weekly Tickets",
          "shortDescription": "",
          "description": "Magic Tickets available weekly.",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 2000
            },
            {
              "templateId": "Currency:SkillXP",
              "quantity": 1000
            },
            {
              "templateId": "Reagent:Reagent_Shard_Dark",
              "quantity": 3
            },
            {
              "templateId": "Reagent:Reagent_Shard_Fire",
              "quantity": 3
            },
            {
              "templateId": "Reagent:Reagent_Shard_Light",
              "quantity": 3
            },
            {
              "templateId": "Reagent:Reagent_Shard_Nature",
              "quantity": 3
            },
            {
              "templateId": "Reagent:Reagent_Shard_Water",
              "quantity": 3
            }
          ]
        },
        {
          "offerId": "A6DBCA724BBEAB05DACF89AA9069BAAF",
          "devName": "Factory Crystal",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Voucher:Voucher_Hero_Workshop",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "AffordOnly",
              "value": "true"
            },
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Hero.B_StoreButton_Hero'"
            },
            {
              "key": "type",
              "value": "bronze"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 99,
          "title": "Factory Crystal",
          "shortDescription": "",
          "description": "Summon a hero to join your team!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "21A1EB7D8107434B9CFC565C272CB81C",
          "devName": "StorefrontMtx.L720000.MtxGift.79",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "4F5DC10D401646573926DCA4714C2832",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "6C731B18416AC27CC6F29CBD0FC2CB8A",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "720000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 83",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "DB541806BB6C472E8752D4736615F32B",
          "devName": "StorefrontMtx.L810000.MtxGift.90",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "26D8C467410A6F8B2D0216B98EC18F0B",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "82A8D4B544A9DC38C604F0A54305097C",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "810000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 92",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "FAB7BC4AE1E24118BD1F1159D82427E4",
          "devName": "StorefrontStacked.Page01.ElementalHeroes.01",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 500,
              "dynamicRegularPrice": -1,
              "finalPrice": 500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 500
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "Type",
              "value": "ElementalHero"
            },
            {
              "key": "HideQuantityRemaining",
              "value": "True"
            }
          ],
          "catalogGroup": "ElementalHeroes",
          "catalogGroupPriority": 1,
          "sortPriority": 72,
          "title": "Elemental Heroes",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 140
            },
            {
              "templateId": "Currency:Hammer",
              "quantity": 4
            },
            {
              "templateId": "Reagent:Reagent_Misc_CeremonialSword",
              "quantity": 2
            },
            {
              "templateId": "Currency:Gold",
              "quantity": 100000
            },
            {
              "templateId": "TreasureMap:TM_MapResource",
              "quantity": 10
            },
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "0B78AE2326EE49E1833C0E808660DE46",
          "devName": "StorefrontMtx.L250000.MtxGift.22",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "DABF7ABF421751F780FC11BBDFD39273",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "82C167B44E347F8BD9E219832900351C",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "MtxLevelMin",
              "value": "250000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "Support Gift 36",
          "shortDescription": "",
          "description": "Thank you for your support!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "13A12247C92C4D15B2EB4AF0A81240AC",
          "devName": "StorefrontStacked.Page01.ElementalHeroes.113",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 500,
              "dynamicRegularPrice": -1,
              "finalPrice": 500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 500
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ButtonClassPath",
              "value": "WidgetBlueprint'/Game/UMG/Store/B_StoreButton_Bundles.B_StoreButton_Bundles'"
            },
            {
              "key": "Type",
              "value": "ElementalHero"
            },
            {
              "key": "HideQuantityRemaining",
              "value": "True"
            }
          ],
          "catalogGroup": "ElementalHeroes",
          "catalogGroupPriority": 113,
          "sortPriority": 72,
          "title": "Elemental Heroes",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 500
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 140
            },
            {
              "templateId": "Currency:Hammer",
              "quantity": 4
            },
            {
              "templateId": "Ore:Ore_Magicite",
              "quantity": 15
            },
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 15
            },
            {
              "templateId": "TreasureMap:TM_ForestOfMixedEmotions_Map8",
              "quantity": 1
            },
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 2
            }
          ]
        }
      ]
    },
    {
      "name": "SecretShop",
      "catalogEntries": []
    },
    {
      "name": "MagicTicket",
      "catalogEntries": []
    },
    {
      "name": "Services",
      "catalogEntries": [
        {
          "offerId": "17E5A9AD45B206FE96CCCC9412334C52",
          "devName": "EnergyRefill 2",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 50,
              "dynamicRegularPrice": -1,
              "finalPrice": 50,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 50
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ServiceName",
              "value": "EnergyRefill"
            }
          ],
          "catalogGroup": "EnergyRefill",
          "catalogGroupPriority": 5,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "99F1C1E54A13B8C6B89E8D98E65676FF",
          "devName": "FriendLimitIncrease",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 100,
              "dynamicRegularPrice": -1,
              "finalPrice": 100,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 100
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ServiceName",
              "value": "FriendsListIncrease"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "F827239E4C5947CBF1F1C1ADDE3C7AE1",
          "devName": "Respec Account Reward Perks Monthly Discount",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 25,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": 1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ServiceName",
              "value": "PerkReset"
            }
          ],
          "catalogGroup": "Respec",
          "catalogGroupPriority": 999,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "7458C6424BE7E47690D51296E48779F8",
          "devName": "EnergyRefill 5",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 150,
              "dynamicRegularPrice": -1,
              "finalPrice": 150,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 150
            }
          ],
          "categories": [],
          "dailyLimit": 5,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ServiceName",
              "value": "EnergyRefill"
            }
          ],
          "catalogGroup": "EnergyRefill",
          "catalogGroupPriority": 2,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "63C49DB84063166931C697BEE8B9B760",
          "devName": "Market Page 2",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 50,
              "dynamicRegularPrice": -1,
              "finalPrice": 50,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 50
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ServiceName",
              "value": "MarketRefresh:0"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "2774D5334FCAEDB2D1FF0AA795B90335",
          "devName": "EnergyRefill 4",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 100,
              "dynamicRegularPrice": -1,
              "finalPrice": 100,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 100
            }
          ],
          "categories": [],
          "dailyLimit": 5,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ServiceName",
              "value": "EnergyRefill"
            }
          ],
          "catalogGroup": "EnergyRefill",
          "catalogGroupPriority": 3,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "0AC74A144F231B56B2CD149D688A3B60",
          "devName": "SecretShop Page 2",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 100,
              "dynamicRegularPrice": -1,
              "finalPrice": 100,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 100
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ServiceName",
              "value": "SecretShopRefresh:1"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "2ED72F49457A0AF78377308A8086F63C",
          "devName": "SecretShop Page 1 - FREE",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ServiceName",
              "value": "SecretShopRefresh:0"
            },
            {
              "key": "VipLevelMin",
              "value": "3"
            }
          ],
          "catalogGroup": "SecretShopP1",
          "catalogGroupPriority": 10,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "0A36979A4B20A28E20ACEC8924F9724D",
          "devName": "SecretShop Page 1",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 100,
              "dynamicRegularPrice": -1,
              "finalPrice": 100,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 100
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ServiceName",
              "value": "SecretShopRefresh:0"
            }
          ],
          "catalogGroup": "SecretShopP1",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "150BAC374E7A2C4635F41F850FEBB9E2",
          "devName": "EnergyRefill 3",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 75,
              "dynamicRegularPrice": -1,
              "finalPrice": 75,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 75
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ServiceName",
              "value": "EnergyRefill"
            }
          ],
          "catalogGroup": "EnergyRefill",
          "catalogGroupPriority": 4,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "F1DEEED84A1577DB97EA8C8D0E55D3E0",
          "devName": "EnergyRefill 6",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 200,
              "dynamicRegularPrice": -1,
              "finalPrice": 200,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 200
            }
          ],
          "categories": [],
          "dailyLimit": 7,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ServiceName",
              "value": "EnergyRefill"
            }
          ],
          "catalogGroup": "EnergyRefill",
          "catalogGroupPriority": 1,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "DAAF98114D3B28BFAD4E4D9D73B8070D",
          "devName": "SecretShop Page 3",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 200,
              "dynamicRegularPrice": -1,
              "finalPrice": 200,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 200
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ServiceName",
              "value": "SecretShopRefresh:2"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "942F8072452726BC0EADC0BB4F9127B9",
          "devName": "GameContinue",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 40,
              "dynamicRegularPrice": -1,
              "finalPrice": 40,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 40
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ServiceName",
              "value": "GameContinue"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "13DA45224BB94323B35251AF8DC1CFE7",
          "devName": "EnergyRefill 1",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 0,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ServiceName",
              "value": "EnergyRefill"
            }
          ],
          "catalogGroup": "EnergyRefill",
          "catalogGroupPriority": 6,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "CB2A2D9B42605E706C93F69EB9CBB079",
          "devName": "Market Page 3",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 100,
              "dynamicRegularPrice": -1,
              "finalPrice": 100,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 100
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ServiceName",
              "value": "MarketRefresh:1"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "A8D2354E4AE98209AEF8B5B26F0E8FE1",
          "devName": "Respec Account Reward Perks Unrestricted",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 25,
              "dynamicRegularPrice": -1,
              "finalPrice": 25,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 25
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ServiceName",
              "value": "PerkReset"
            }
          ],
          "catalogGroup": "Respec",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "AF44DAA04EFE95AFFFF49BBDC767BFBC",
          "devName": "ResetLaborPool",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 100,
              "dynamicRegularPrice": -1,
              "finalPrice": 100,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 100
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "ServiceName",
              "value": "ResetLaborPool"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": []
        }
      ]
    },
    {
      "name": "Marketplace",
      "catalogEntries": [
        {
          "offerId": "EABB0649D0784B589A3936CAD9394E90",
          "devName": "Marketplace.L05.Page01.PowerSource.01",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 2500,
              "dynamicRegularPrice": -1,
              "finalPrice": 2500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 2500
            }
          ],
          "categories": [],
          "dailyLimit": 10,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "5"
            },
            {
              "key": "MaxMarketLevel",
              "value": "9"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shared_T02",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "5C869FEC2EF6493FBFA719BC6D8D6E7F",
          "devName": "Marketplace.L07.Page01.MapFragments.04",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 20000,
              "dynamicRegularPrice": -1,
              "finalPrice": 20000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 20000
            }
          ],
          "categories": [],
          "dailyLimit": 5,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "7"
            },
            {
              "key": "MaxMarketLevel",
              "value": "10"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "TreasureMap:TM_MapResource",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "7F8361221A0949958939D3CEF503D89D",
          "devName": "Marketplace.L01.Page01.Free.02",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 4000,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 10,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "1"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "UpgradePotion:UpgradeHealthMinor",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "F55CF5E14C4B4B1EA0971EBC021399AC",
          "devName": "Marketplace.L10.Page01.PowerSource.04",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 2500,
              "dynamicRegularPrice": -1,
              "finalPrice": 2500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 2500
            }
          ],
          "categories": [],
          "dailyLimit": 15,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "10"
            },
            {
              "key": "MaxMarketLevel",
              "value": "14"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shared_T02",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "6D346178B1B34E90BCD700D0FD31FF10",
          "devName": "Marketplace.L20.Page01.Free.57",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 20000,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 3,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "20"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "TreasureMap:TM_MapResource",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "1AEEA8721EAA4675BD0C27E0E5D0B671",
          "devName": "Marketplace.L03.Page01.MapFragments.01",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 20000,
              "dynamicRegularPrice": -1,
              "finalPrice": 20000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 20000
            }
          ],
          "categories": [],
          "dailyLimit": 3,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "3"
            },
            {
              "key": "MaxMarketLevel",
              "value": "6"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "TreasureMap:TM_MapResource",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "0B9C665BD55F4AE5A312130D6D033C2F",
          "devName": "Marketplace.L19.Page01.Misc.16",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 50000,
              "dynamicRegularPrice": -1,
              "finalPrice": 50000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 50000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "19"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_RXT_Parts_Small",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "3E2FFAD6D96B43CFA4D0953D1A8A187F",
          "devName": "Marketplace.L12.Page01.Reagent.03",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 300000,
              "dynamicRegularPrice": -1,
              "finalPrice": 300000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 300000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "12"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Light",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "47B2E8BB7DED4769AA1F9D6DD83F3037",
          "devName": "Marketplace.L08.Page01.Free.42",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 300000,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "8"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Light",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "FFDF84C8D20040D9A621BBAD1905E512",
          "devName": "Marketplace.L11.Page01.TreasureMap.01",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 20000,
              "dynamicRegularPrice": -1,
              "finalPrice": 20000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 20000
            }
          ],
          "categories": [],
          "dailyLimit": 7,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "11"
            },
            {
              "key": "MaxMarketLevel",
              "value": "15"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "TreasureMap:TM_MapResource",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "AF93D694E58543EF98B468964274E872",
          "devName": "Marketplace.L06.Page01.Token.04",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 35000,
              "dynamicRegularPrice": -1,
              "finalPrice": 35000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 35000
            }
          ],
          "categories": [],
          "dailyLimit": 5,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "6"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "6239684CD2BE41B2B0F1B8C6D7D20161",
          "devName": "Marketplace.L16.Page01.TreasureMap.04",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 20000,
              "dynamicRegularPrice": -1,
              "finalPrice": 20000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 20000
            }
          ],
          "categories": [],
          "dailyLimit": 10,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "16"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "TreasureMap:TM_MapResource",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "39BD7B473E32484DA911B4FB7457E641",
          "devName": "Marketplace.L04.Page01.MinorElixir.02",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 4000,
              "dynamicRegularPrice": -1,
              "finalPrice": 4000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 4000
            }
          ],
          "categories": [],
          "dailyLimit": 8,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "4"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "UpgradePotion:UpgradeHealthMinor",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "031D3E0D1EB445BC99596DB45581C692",
          "devName": "Marketplace.L13.Page01.MapsMisc.03",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 10000,
              "dynamicRegularPrice": -1,
              "finalPrice": 10000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 10000
            }
          ],
          "categories": [],
          "dailyLimit": 2,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "13"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Currency:SkillXP",
              "quantity": 100
            }
          ]
        },
        {
          "offerId": "794EB898A3524A79ABA1EAEF20617014",
          "devName": "Marketplace.L01.Page1.VIP5.FreeBonus.04",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 20000,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 4,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "1"
            },
            {
              "key": "VipLevelMin",
              "value": "5"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "TreasureMap:TM_MapResource",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "EE1F612AAF12423796D37664C6112810",
          "devName": "Marketplace.L18.Page01.Hero.01",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 300000,
              "dynamicRegularPrice": -1,
              "finalPrice": 300000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 300000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "18"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_HeroMap_Bronze",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "6E0FC91CCB2F45C78D66AF2ACA1A2166",
          "devName": "Marketplace.L15.Page01.PowerSource.07",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 2500,
              "dynamicRegularPrice": -1,
              "finalPrice": 2500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 2500
            }
          ],
          "categories": [],
          "dailyLimit": 20,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "15"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shared_T02",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "0F8591634D9742168B7DEDC93BEA50EC",
          "devName": "Marketplace.L02.Page01.XP.01",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 200,
              "dynamicRegularPrice": -1,
              "finalPrice": 200,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 200
            }
          ],
          "categories": [],
          "dailyLimit": 100000,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "2"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "+100 ",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Currency:HeroXp_Basic",
              "quantity": 100
            }
          ]
        },
        {
          "offerId": "907B61B3FE024F15A63065697EC6679D",
          "devName": "Marketplace.L14.Page01.ElixirAll.04",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 50000,
              "dynamicRegularPrice": -1,
              "finalPrice": 50000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 50000
            }
          ],
          "categories": [],
          "dailyLimit": 3,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "14"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "2C78C3AE58DF4AB39F7922702D5DBD56",
          "devName": "Marketplace.L09.Page01.MajorElixir.03",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 50000,
              "dynamicRegularPrice": -1,
              "finalPrice": 50000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 50000
            }
          ],
          "categories": [],
          "dailyLimit": 4,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "9"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "3F2E0A69C89E4074963310741C3B7716",
          "devName": "Marketplace.L17.Page01.Shard.06",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 300000,
              "dynamicRegularPrice": -1,
              "finalPrice": 300000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 300000
            }
          ],
          "categories": [],
          "dailyLimit": 2,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "17"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Dark",
              "quantity": 1
            }
          ]
        }
      ]
    },
    {
      "name": "MarketplacePage3",
      "catalogEntries": [
        {
          "offerId": "B078B74487B843CBA1CA78BF47D11663",
          "devName": "Marketplace.L02.Page03.XP.03",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 200,
              "dynamicRegularPrice": -1,
              "finalPrice": 200,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 200
            }
          ],
          "categories": [],
          "dailyLimit": 100000,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "2"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "+100 ",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Currency:HeroXp_Basic",
              "quantity": 100
            }
          ]
        },
        {
          "offerId": "3A3C486F14E5478B826BE2D8C98FB03E",
          "devName": "Marketplace.L09.Page03.MajorElixir.09",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 50000,
              "dynamicRegularPrice": -1,
              "finalPrice": 50000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 50000
            }
          ],
          "categories": [],
          "dailyLimit": 4,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "9"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "3A430ADD0F1F4287991EA55F6154E1D5",
          "devName": "Marketplace.L13.Page03.MapsMisc.31",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 10000,
              "dynamicRegularPrice": -1,
              "finalPrice": 10000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 10000
            }
          ],
          "categories": [],
          "dailyLimit": 2,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "13"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Currency:SkillXP",
              "quantity": 100
            }
          ]
        },
        {
          "offerId": "F9EBEC41A0CB4D7CBA4DF497C1F350DC",
          "devName": "Marketplace.L05.Page03.PowerSource.03",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 2500,
              "dynamicRegularPrice": -1,
              "finalPrice": 2500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 2500
            }
          ],
          "categories": [],
          "dailyLimit": 10,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "5"
            },
            {
              "key": "MaxMarketLevel",
              "value": "9"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shared_T02",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "2AEFDF81DAAF449DA3B6114547C5FD4B",
          "devName": "Marketplace.L15.Page03.PowerSource.09",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 2500,
              "dynamicRegularPrice": -1,
              "finalPrice": 2500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 2500
            }
          ],
          "categories": [],
          "dailyLimit": 20,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "15"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shared_T02",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "B6B8AF20474E43679B8A397660ACD4F4",
          "devName": "Marketplace.L03.Page03.MapFragments.03",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 20000,
              "dynamicRegularPrice": -1,
              "finalPrice": 20000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 20000
            }
          ],
          "categories": [],
          "dailyLimit": 3,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "3"
            },
            {
              "key": "MaxMarketLevel",
              "value": "6"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "TreasureMap:TM_MapResource",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "F455EF7B234345FF98B736965E9323C0",
          "devName": "Marketplace.L01.Page03.Free.10",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 4000,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 10,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "1"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "UpgradePotion:UpgradeHealthMinor",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "EE166D45A88E4C81B8980CBD0E271880",
          "devName": "Marketplace.L08.Page03.Free.39",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 20000,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 5,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "8"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "TreasureMap:TM_MapResource",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "0DF8DDAA584C446FAC782412957C1317",
          "devName": "Marketplace.L10.Page03.PowerSource.06",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 2500,
              "dynamicRegularPrice": -1,
              "finalPrice": 2500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 2500
            }
          ],
          "categories": [],
          "dailyLimit": 15,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "10"
            },
            {
              "key": "MaxMarketLevel",
              "value": "14"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shared_T02",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "88DBD19D68224430AB91B46BE5A152C4",
          "devName": "Marketplace.L07.Page03.MapFragments.08",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 20000,
              "dynamicRegularPrice": -1,
              "finalPrice": 20000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 20000
            }
          ],
          "categories": [],
          "dailyLimit": 5,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "7"
            },
            {
              "key": "MaxMarketLevel",
              "value": "10"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "TreasureMap:TM_MapResource",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "314372D38DAF4F84908DE02DCC53083E",
          "devName": "Marketplace.L06.Page03.Token.21",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 100000,
              "dynamicRegularPrice": -1,
              "finalPrice": 100000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 100000
            }
          ],
          "categories": [],
          "dailyLimit": 2,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "6"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_SupplyPoints_Elite",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "A66B3964E34440CC95D808376AA43571",
          "devName": "Marketplace.L18.Page03.Hero.09",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 300000,
              "dynamicRegularPrice": -1,
              "finalPrice": 300000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 300000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "18"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_HeroMap_Bronze",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "E9AF740B9D2948C8BA8E8F81EE86E851",
          "devName": "Marketplace.L14.Page03.ElixirAll.11",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 50000,
              "dynamicRegularPrice": -1,
              "finalPrice": 50000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 50000
            }
          ],
          "categories": [],
          "dailyLimit": 3,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "14"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "60C210C52AB040ECBAF22556626C3891",
          "devName": "Marketplace.L04.Page03.MinorElixir.11",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 4000,
              "dynamicRegularPrice": -1,
              "finalPrice": 4000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 4000
            }
          ],
          "categories": [],
          "dailyLimit": 4,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "4"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "UpgradePotion:UpgradeStrengthMinor",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "CD4F67A9437B4DA5AF5E347A1B70DF99",
          "devName": "Marketplace.L12.Page03.Reagent.30",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 200,
              "dynamicRegularPrice": -1,
              "finalPrice": 200,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 200
            }
          ],
          "categories": [],
          "dailyLimit": 2,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "12"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Water",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "8A20EC4E951F459C945A7C33EC708400",
          "devName": "Marketplace.L16.Page03.TreasureMap.06",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 20000,
              "dynamicRegularPrice": -1,
              "finalPrice": 20000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 20000
            }
          ],
          "categories": [],
          "dailyLimit": 10,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "16"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "TreasureMap:TM_MapResource",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "398001206387426FB6DC56034CF2B869",
          "devName": "Marketplace.L01.Page3.VIP5.FreeBonus.74",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 50000,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "1"
            },
            {
              "key": "VipLevelMin",
              "value": "5"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "TreasureMap:TM_ForestOfMixedEmotions_Map8",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "CB01AB66A92C496BA829D424144C61A6",
          "devName": "Marketplace.L20.Page03.Free.120",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 2500,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 15,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "20"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shared_T02",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "5098EC09AE1240E0B258B909443E5944",
          "devName": "Marketplace.L11.Page03.TreasureMap.03",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 20000,
              "dynamicRegularPrice": -1,
              "finalPrice": 20000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 20000
            }
          ],
          "categories": [],
          "dailyLimit": 7,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "11"
            },
            {
              "key": "MaxMarketLevel",
              "value": "15"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "TreasureMap:TM_MapResource",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "588718B32FDE4B819C48779918FC0D96",
          "devName": "Marketplace.L17.Page03.Shard.28",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 300000,
              "dynamicRegularPrice": -1,
              "finalPrice": 300000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 300000
            }
          ],
          "categories": [],
          "dailyLimit": 2,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "17"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Water",
              "quantity": 1
            }
          ]
        }
      ]
    },
    {
      "name": "MarketplacePage2",
      "catalogEntries": [
        {
          "offerId": "58798C7B134441AAA0D371FBF2CF817B",
          "devName": "Marketplace.L10.Page02.PowerSource.05",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 2500,
              "dynamicRegularPrice": -1,
              "finalPrice": 2500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 2500
            }
          ],
          "categories": [],
          "dailyLimit": 15,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "10"
            },
            {
              "key": "MaxMarketLevel",
              "value": "14"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shared_T02",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "519B321DE41C46039A8FE1FE7ABA266A",
          "devName": "Marketplace.L16.Page02.TreasureMap.05",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 20000,
              "dynamicRegularPrice": -1,
              "finalPrice": 20000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 20000
            }
          ],
          "categories": [],
          "dailyLimit": 10,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "16"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "TreasureMap:TM_MapResource",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "C367DEFB69DE465ABECFC163901ECE1D",
          "devName": "Marketplace.L20.Page02.Free.92",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 50000,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "20"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "TreasureMap:TM_ForestOfMixedEmotions_Map8",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "898A5A6B4DBB4848A806ACC4C7449EC4",
          "devName": "Marketplace.L13.Page02.MapsMisc.16",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 10000,
              "dynamicRegularPrice": -1,
              "finalPrice": 10000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 10000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "13"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Currency:SkillXP",
              "quantity": 100
            }
          ]
        },
        {
          "offerId": "CD210A110E574F989D7CE973DA061EAB",
          "devName": "Marketplace.L08.Page02.Free.29",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 50000,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 6,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "8"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "113EF382B3B24B139FE8A4C00C038FFF",
          "devName": "Marketplace.L09.Page02.MajorElixir.05",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 50000,
              "dynamicRegularPrice": -1,
              "finalPrice": 50000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 50000
            }
          ],
          "categories": [],
          "dailyLimit": 4,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "9"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "C76133B32D794B2ABFB30192DC65C61D",
          "devName": "Marketplace.L07.Page02.MapFragments.07",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "MtxCurrency",
              "currencySubType": "",
              "regularPrice": 10,
              "dynamicRegularPrice": -1,
              "finalPrice": 10,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 10
            }
          ],
          "categories": [],
          "dailyLimit": 7,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "7"
            },
            {
              "key": "MaxMarketLevel",
              "value": "10"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "TreasureMap:TM_MapResource",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "5D6CCF79A7804AE4ABAD7089C5E4F6DE",
          "devName": "Marketplace.L15.Page02.PowerSource.08",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 2500,
              "dynamicRegularPrice": -1,
              "finalPrice": 2500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 2500
            }
          ],
          "categories": [],
          "dailyLimit": 20,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "15"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shared_T02",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "7FA05AFC2E6D47408CECED87FE65885A",
          "devName": "Marketplace.L11.Page02.TreasureMap.02",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 20000,
              "dynamicRegularPrice": -1,
              "finalPrice": 20000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 20000
            }
          ],
          "categories": [],
          "dailyLimit": 7,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "11"
            },
            {
              "key": "MaxMarketLevel",
              "value": "15"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "TreasureMap:TM_MapResource",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "941D2080864C413E82C475BDE3AB9D4B",
          "devName": "Marketplace.L18.Page02.Hero.05",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 300000,
              "dynamicRegularPrice": -1,
              "finalPrice": 300000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 300000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "18"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_HeroMap_Bronze",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "A6DBC56D94404CAFAA3029F60C91278C",
          "devName": "Marketplace.L03.Page02.MapFragments.02",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 20000,
              "dynamicRegularPrice": -1,
              "finalPrice": 20000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 20000
            }
          ],
          "categories": [],
          "dailyLimit": 3,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "3"
            },
            {
              "key": "MaxMarketLevel",
              "value": "6"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "TreasureMap:TM_MapResource",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "49CB7EDCCB824D14A3985616EB4F2AD6",
          "devName": "Marketplace.L04.Page02.MinorElixir.07",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 4000,
              "dynamicRegularPrice": -1,
              "finalPrice": 4000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 4000
            }
          ],
          "categories": [],
          "dailyLimit": 4,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "4"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "UpgradePotion:UpgradeStrengthMinor",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "0608273CDC4949DF9A95897C4948B764",
          "devName": "Marketplace.L01.Page2.VIP5.FreeBonus.34",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 300000,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "1"
            },
            {
              "key": "VipLevelMin",
              "value": "5"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Nature",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "C0622CF3FAFA4BB683164CC3D04C6C90",
          "devName": "Marketplace.L06.Page02.Token.11",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 35000,
              "dynamicRegularPrice": -1,
              "finalPrice": 35000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 35000
            }
          ],
          "categories": [],
          "dailyLimit": 5,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "6"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "53A087C7CE634462A70A9C57F0AD4116",
          "devName": "Marketplace.L14.Page02.ElixirAll.09",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 50000,
              "dynamicRegularPrice": -1,
              "finalPrice": 50000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 50000
            }
          ],
          "categories": [],
          "dailyLimit": 3,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "14"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "13E48B0A90C940E897AC31872BD41459",
          "devName": "Marketplace.L17.Page02.Shard.20",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 300000,
              "dynamicRegularPrice": -1,
              "finalPrice": 300000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 300000
            }
          ],
          "categories": [],
          "dailyLimit": 2,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "17"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Water",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "F50A32B0120C45CBB873AD8380DBC4D0",
          "devName": "Marketplace.L01.Page02.Free.07",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 4000,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 5,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "1"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "UpgradePotion:UpgradeStrengthMinor",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "A0B2F31FF9CB49168673201F9D47DD6F",
          "devName": "Marketplace.L05.Page02.PowerSource.02",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 2500,
              "dynamicRegularPrice": -1,
              "finalPrice": 2500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 2500
            }
          ],
          "categories": [],
          "dailyLimit": 10,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "5"
            },
            {
              "key": "MaxMarketLevel",
              "value": "9"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shared_T02",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "57E7ABFEFD81485D82627A837A6C04BC",
          "devName": "Marketplace.L02.Page02.XP.02",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 200,
              "dynamicRegularPrice": -1,
              "finalPrice": 200,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 200
            }
          ],
          "categories": [],
          "dailyLimit": 100000,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "2"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "+100 ",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Currency:HeroXp_Basic",
              "quantity": 100
            }
          ]
        },
        {
          "offerId": "FBD6D8ADEB094548ABF0B7AF0297A21A",
          "devName": "Marketplace.L12.Page02.Reagent.13",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Currency:Gold",
              "regularPrice": 300000,
              "dynamicRegularPrice": -1,
              "finalPrice": 300000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 300000
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "MarketLevel",
              "value": "12"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Light",
              "quantity": 1
            }
          ]
        }
      ]
    },
    {
      "name": "Events",
      "catalogEntries": [
        {
          "offerId": "118F973449C241E0A3AE5D90BAE43A9B",
          "devName": "Event.Evergreen5.25",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Event_Evergreen5",
              "regularPrice": 1500,
              "dynamicRegularPrice": -1,
              "finalPrice": 1500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1500
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "EventLimit",
              "value": "5"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 203,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Voucher:Voucher_HeroSilver_Fire",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "2AA18AB9BBCC45D7A38271FC1335C528",
          "devName": "Event.Evergreen5.17",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Event_Evergreen5",
              "regularPrice": 20,
              "dynamicRegularPrice": -1,
              "finalPrice": 20,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 20
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "EventLimit",
              "value": "50"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 186,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "UpgradePotion:UpgradeHealthMinor",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "5BA1F2A8139C47B2B2482C2E0971789A",
          "devName": "Event.Evergreen5.09",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Event_Evergreen5",
              "regularPrice": 3750,
              "dynamicRegularPrice": -1,
              "finalPrice": 3750,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 3750
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "EventLimit",
              "value": "10"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 194,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Misc_CeremonialSword",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "F60BF3D2F8514F83B75C24D7ED1DBB7F",
          "devName": "Event.Evergreen5.05",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Event_Evergreen5",
              "regularPrice": 1000,
              "dynamicRegularPrice": -1,
              "finalPrice": 1000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1000
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "EventLimit",
              "value": "1"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 198,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Currency:Hammer",
              "quantity": 35
            }
          ]
        },
        {
          "offerId": "BCD54AA28F954A26A81D1ACF425B731B",
          "devName": "Event.Evergreen5.21",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Event_Evergreen5",
              "regularPrice": 500,
              "dynamicRegularPrice": -1,
              "finalPrice": 500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 500
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "EventLimit",
              "value": "10"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 182,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 5
            }
          ]
        },
        {
          "offerId": "70105EB742C14099B8209AECC629A419",
          "devName": "Event.Evergreen5.30",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Event_Evergreen5",
              "regularPrice": 20000,
              "dynamicRegularPrice": -1,
              "finalPrice": 20000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 20000
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "EventLimit",
              "value": "2"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 179,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Hero_Event",
              "quantity": 500
            }
          ]
        },
        {
          "offerId": "4671AC9243F04158BA0A671C47E40357",
          "devName": "Event.Evergreen5.02",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Event_Evergreen5",
              "regularPrice": 80,
              "dynamicRegularPrice": -1,
              "finalPrice": 80,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 80
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "EventLimit",
              "value": "500"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 200,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Currency:MtxGiveaway",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "8A5705927EA848D6BC18BA6024DB082F",
          "devName": "Event.Evergreen5.07",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Event_Evergreen5",
              "regularPrice": 1000,
              "dynamicRegularPrice": -1,
              "finalPrice": 1000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1000
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "EventLimit",
              "value": "600"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 196,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_SupplyPoints_Elite",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "19826B8037F14BCD92D05E86AD38BAA7",
          "devName": "Event.Evergreen5.15",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Event_Evergreen5",
              "regularPrice": 2250,
              "dynamicRegularPrice": -1,
              "finalPrice": 2250,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 2250
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "EventLimit",
              "value": "50"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 188,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Fire",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "03476EA74FE84B2D8869B794E9AB13B1",
          "devName": "Event.Evergreen5.23",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Event_Evergreen5",
              "regularPrice": 1500,
              "dynamicRegularPrice": -1,
              "finalPrice": 1500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1500
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "EventLimit",
              "value": "5"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 201,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Voucher:Voucher_HeroSilver_Water",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "44E4A75E182F44499560B44AC2045E3F",
          "devName": "Event.Evergreen5.29",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Event_Evergreen5",
              "regularPrice": 375,
              "dynamicRegularPrice": -1,
              "finalPrice": 375,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 375
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "EventLimit",
              "value": "5"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 180,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_RXT_Parts_Small",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "B9D624B3EA8B4E65AB8C8D345EBD4160",
          "devName": "Event.Evergreen5.10",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Event_Evergreen5",
              "regularPrice": 10000,
              "dynamicRegularPrice": -1,
              "finalPrice": 10000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 10000
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "EventLimit",
              "value": "5"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 193,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Misc_CeremonialShield",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "AC3AED5C0D4A45679C717A8291FF3035",
          "devName": "Event.Evergreen5.14",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Event_Evergreen5",
              "regularPrice": 2250,
              "dynamicRegularPrice": -1,
              "finalPrice": 2250,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 2250
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "EventLimit",
              "value": "50"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 189,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Light",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "21F36F0179DF492AA516F2AEF866FF93",
          "devName": "Event.Evergreen5.28",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Event_Evergreen5",
              "regularPrice": 20000,
              "dynamicRegularPrice": -1,
              "finalPrice": 20000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 20000
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "EventLimit",
              "value": "10"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 175,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shared_MysteryGoo",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "2248DBFC177047ED81102FCC05B7E443",
          "devName": "Event.Evergreen5.19",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Event_Evergreen5",
              "regularPrice": 250,
              "dynamicRegularPrice": -1,
              "finalPrice": 250,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 250
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "EventLimit",
              "value": "50"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 184,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "UpgradePotion:UpgradeHealthMajor",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "47100E5C59E34A41965723ED4279D169",
          "devName": "Event.Evergreen5.27",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Event_Evergreen5",
              "regularPrice": 1500,
              "dynamicRegularPrice": -1,
              "finalPrice": 1500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1500
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "EventLimit",
              "value": "5"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 205,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Voucher:Voucher_HeroSilver_Nature",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "2B1912598BDA405398B9BE602DDBAADB",
          "devName": "Event.Evergreen5.18",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Event_Evergreen5",
              "regularPrice": 20,
              "dynamicRegularPrice": -1,
              "finalPrice": 20,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 20
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "EventLimit",
              "value": "50"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 185,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "UpgradePotion:UpgradeStrengthMinor",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "694DF940A0B64A57B307C96A8AD01625",
          "devName": "Event.Evergreen5.20",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Event_Evergreen5",
              "regularPrice": 250,
              "dynamicRegularPrice": -1,
              "finalPrice": 250,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 250
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "EventLimit",
              "value": "50"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 183,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "UpgradePotion:UpgradeStrengthMajor",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "17D499D6924D457A97D1CCF9D288B560",
          "devName": "Event.Evergreen5.01",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Event_Battlepass4",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "EventLimit",
              "value": "-1"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 1000,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Currency:Gold",
              "quantity": 50
            }
          ]
        },
        {
          "offerId": "3447B3D6A72C45808DCBDFAA40D419F2",
          "devName": "Event.Evergreen5.06",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Event_Evergreen5",
              "regularPrice": 500,
              "dynamicRegularPrice": -1,
              "finalPrice": 500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 500
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "EventLimit",
              "value": "2"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 197,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Currency:Hammer",
              "quantity": 15
            }
          ]
        },
        {
          "offerId": "A03EEC2CF7F84562BB5C8DFC590E9A8B",
          "devName": "Event.Evergreen5.32",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Event_Evergreen5",
              "regularPrice": 5300,
              "dynamicRegularPrice": -1,
              "finalPrice": 5300,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5300
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "EventLimit",
              "value": "2"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 177,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 100
            }
          ]
        },
        {
          "offerId": "971D7E24B79346A0BD438C56FFE96EF4",
          "devName": "Event.Evergreen5.26",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Event_Evergreen5",
              "regularPrice": 1500,
              "dynamicRegularPrice": -1,
              "finalPrice": 1500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1500
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "EventLimit",
              "value": "5"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 204,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Voucher:Voucher_HeroSilver_Light",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "BBC5CF7F162B4A0CAB62E4178FAA5AE4",
          "devName": "Event.Evergreen5.33",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Event_Evergreen5",
              "regularPrice": 500,
              "dynamicRegularPrice": -1,
              "finalPrice": 500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 500
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "EventLimit",
              "value": "1"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 176,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Ore:Ore_Magicite",
              "quantity": 150
            }
          ]
        },
        {
          "offerId": "97D41A20AAA44322B668D34E94C5FD80",
          "devName": "Event.Evergreen5.16",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Event_Evergreen5",
              "regularPrice": 2250,
              "dynamicRegularPrice": -1,
              "finalPrice": 2250,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 2250
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "EventLimit",
              "value": "50"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 187,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Nature",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "506B6EEDC04049E582A78BDAA3325957",
          "devName": "Event.Evergreen5.12",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Event_Evergreen5",
              "regularPrice": 2250,
              "dynamicRegularPrice": -1,
              "finalPrice": 2250,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 2250
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "EventLimit",
              "value": "50"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 191,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Water",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "6DEA55F7D6B341B2ADCBEEEF00928B51",
          "devName": "Event.Evergreen5.34",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Event_Evergreen5",
              "regularPrice": 6000,
              "dynamicRegularPrice": -1,
              "finalPrice": 6000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 6000
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "EventLimit",
              "value": "5"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 175,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Gear",
              "quantity": 2
            }
          ]
        },
        {
          "offerId": "A64379243F464023BC51B53FFE544B33",
          "devName": "Event.Evergreen5.22",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Event_Evergreen5",
              "regularPrice": 1000,
              "dynamicRegularPrice": -1,
              "finalPrice": 1000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1000
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "EventLimit",
              "value": "6"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 181,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Foil",
              "quantity": 50
            }
          ]
        },
        {
          "offerId": "5971DB99866D42138724247D2A8BBF42",
          "devName": "Event.Evergreen5.13",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Event_Evergreen5",
              "regularPrice": 2250,
              "dynamicRegularPrice": -1,
              "finalPrice": 2250,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 2250
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "EventLimit",
              "value": "50"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 190,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Dark",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "F3EA4EAF49284D23927F04EA03CF6EF0",
          "devName": "Event.Evergreen5.11",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Event_Evergreen5",
              "regularPrice": 22500,
              "dynamicRegularPrice": -1,
              "finalPrice": 22500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 22500
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "EventLimit",
              "value": "1"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 192,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Misc_CeremonialArmor",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "BFD783F78FAA4E30B48E1922E4889C90",
          "devName": "Event.Evergreen5.03",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Event_Evergreen5",
              "regularPrice": 500,
              "dynamicRegularPrice": -1,
              "finalPrice": 500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 500
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "EventLimit",
              "value": "1"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 200,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Currency:MtxGiveaway",
              "quantity": 250
            }
          ]
        },
        {
          "offerId": "E29E9E4FE1DA4D799EDA4FA2726D7D9B",
          "devName": "Event.Evergreen5.04",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Event_Evergreen5",
              "regularPrice": 4,
              "dynamicRegularPrice": -1,
              "finalPrice": 4,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 4
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "EventLimit",
              "value": "20000"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 199,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Currency:SkillXP",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "7597B2B7C7524125BAFA7E6D875B79BC",
          "devName": "Event.Evergreen5.31",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Event_Evergreen5",
              "regularPrice": 15,
              "dynamicRegularPrice": -1,
              "finalPrice": 15,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 15
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "EventLimit",
              "value": "300"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 178,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shared_T02",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "E630784D7E3345FF958A4AEC3D121315",
          "devName": "Event.Evergreen5.24",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Event_Evergreen5",
              "regularPrice": 1500,
              "dynamicRegularPrice": -1,
              "finalPrice": 1500,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1500
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "EventLimit",
              "value": "5"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 202,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Voucher:Voucher_HeroSilver_Dark",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "96898B4CC1C84B3886E7AAF22C772BD4",
          "devName": "Event.Evergreen5.08",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Event_Evergreen5",
              "regularPrice": 50000,
              "dynamicRegularPrice": -1,
              "finalPrice": 50000,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 50000
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "EventLimit",
              "value": "2"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 195,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Currency:HeroXp_Basic",
              "quantity": 500000
            }
          ]
        }
      ]
    },
    {
      "name": "Workshop",
      "catalogEntries": [
        {
          "offerId": "45916F474E404CCBB616CB74F1894575",
          "devName": "Workshop.Page01.ClassTraining.31",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Misc_ShadowEssence",
              "regularPrice": 5,
              "dynamicRegularPrice": -1,
              "finalPrice": 5,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "38278D54469AA644404255919ABC67CF",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "E7EEA718452DEDED4574BD9D51CE23A1",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "0"
            },
            {
              "key": "ForceShowFirstItemInGrant",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "/Game/Loot/AccountItems/Reagents/Reagent_ClassTraining_Strength.Reagent_ClassTraining_Strength",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_ClassTraining_Strength",
              "quantity": 1
            },
            {
              "templateId": "Currency:Gold",
              "quantity": 10000
            }
          ]
        },
        {
          "offerId": "4495EE859818440992EA8CE752EB7CCB",
          "devName": "Workshop.L01.Page01.BuildRockbeast.04",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Pet_Rockbeast",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "1"
            },
            {
              "key": "AffordOnly",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 3,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Character:Pet_R1_Rockbeast_Nature_T03",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "31258E3431B24968A9BAD843C4B38E0F",
          "devName": "Workshop.L07.Page01.BuildingMaterials.01",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "Other",
              "currencySubType": "LaborPoints",
              "regularPrice": 200,
              "dynamicRegularPrice": -1,
              "finalPrice": 200,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 200
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "7"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 7,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_SupplyPoints_BuildingUpgrade",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "E5A0AEC7C763489B91669EFB5B53078A",
          "devName": "Workshop.L01.Page01.BuildRxT.02",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_RXT_Parts_Small",
              "regularPrice": 100,
              "dynamicRegularPrice": -1,
              "finalPrice": 100,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 100
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "1"
            },
            {
              "key": "AffordOnly",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 5,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Character:Warrior_SR2_Fire_RoboGuy_T05",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "650F4214FB8F415DAA935EACF4893AAB",
          "devName": "Workshop.L01.Page01.BuildRandomGear.06",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Shard_Gear",
              "regularPrice": 20,
              "dynamicRegularPrice": -1,
              "finalPrice": 20,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 20
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "1"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 8,
          "title": "Build Random Armor  (VeryRare)",
          "shortDescription": "",
          "description": "Construct a random Very Rare armor!",
          "displayAssetPath": "/Game/UMG/Textures/HeroGear/T_Gear_Armor_Random_03_VeryRare.T_Gear_Armor_Random_03_VeryRare",
          "itemGrants": []
        },
        {
          "offerId": "B22688D6EA8B4BC1A990F6B904B145C8",
          "devName": "Workshop.L24.Page01.BuildingMaterials.10",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "Other",
              "currencySubType": "LaborPoints",
              "regularPrice": 200,
              "dynamicRegularPrice": -1,
              "finalPrice": 100,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 100
            }
          ],
          "categories": [],
          "dailyLimit": 8,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "24"
            },
            {
              "key": "MaxWorkshopLevel",
              "value": "25"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 14,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_SupplyPoints_BuildingUpgrade",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "5158AE01433D1424F81668A8BA65EFE3",
          "devName": "Rocket Fuel (Ancient Factory)",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "Other",
              "currencySubType": "LaborPoints",
              "regularPrice": 50,
              "dynamicRegularPrice": -1,
              "finalPrice": 50,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 50
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "6A5DCF444886DF11888AD192153B3FD1",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "9E41C3CA4B15890914C587ABBEBC8E76",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "878728D44A2CA0901731C387D18FEED5",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "3"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 4,
          "title": "Rocket Fuel",
          "shortDescription": "",
          "description": "Supercharged gameplay speed!\r\n\r\nNew speed is set automatically, but can be changed in Gameplay Settings.",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "StandIn:RocketFuel",
              "quantity": 1,
              "attributes": {
                "FakeQuantity": 1
              }
            }
          ]
        },
        {
          "offerId": "931EA8A6B50F4BE6AF48413864DD1378",
          "devName": "Workshop.Page01.ClassTraining.17",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Misc_ShadowEssence",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "8550273E418A227A2CCFE7B8825472FF",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "0"
            },
            {
              "key": "AffordOnly",
              "value": "true"
            },
            {
              "key": "ForceShowFirstItemInGrant",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 19,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "/Game/Loot/AccountItems/Reagents/Reagent_ClassTraining_Insight.Reagent_ClassTraining_Insight",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_ClassTraining_Insight",
              "quantity": 1
            },
            {
              "templateId": "Currency:Gold",
              "quantity": 10000
            }
          ]
        },
        {
          "offerId": "365906993CE0432388FCA98F20FD6A0A",
          "devName": "Workshop.Page01.ClassTraining.24",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Misc_ShadowEssence",
              "regularPrice": 5,
              "dynamicRegularPrice": -1,
              "finalPrice": 5,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "E7EEA718452DEDED4574BD9D51CE23A1",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "EBDAA0DC4684721269F4F29A5494519E",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "0"
            },
            {
              "key": "ForceShowFirstItemInGrant",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "/Game/Loot/AccountItems/Reagents/Reagent_ClassTraining_Insight.Reagent_ClassTraining_Insight",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_ClassTraining_Insight",
              "quantity": 1
            },
            {
              "templateId": "Currency:Gold",
              "quantity": 10000
            }
          ]
        },
        {
          "offerId": "999B0F083D8B46EDB4E0B786E36E0165",
          "devName": "Workshop.L16.Page01.BuildingMaterials.07",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "Other",
              "currencySubType": "LaborPoints",
              "regularPrice": 200,
              "dynamicRegularPrice": -1,
              "finalPrice": 100,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 100
            }
          ],
          "categories": [],
          "dailyLimit": 5,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "16"
            },
            {
              "key": "MaxWorkshopLevel",
              "value": "19"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 14,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_SupplyPoints_BuildingUpgrade",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "0FFCA8E24D464BECB885EC09B65E45E8",
          "devName": "Workshop.L08.Page01.BuildingMaterials.04",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "Other",
              "currencySubType": "LaborPoints",
              "regularPrice": 200,
              "dynamicRegularPrice": -1,
              "finalPrice": 100,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 100
            }
          ],
          "categories": [],
          "dailyLimit": 2,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "8"
            },
            {
              "key": "MaxWorkshopLevel",
              "value": "9"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 14,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_SupplyPoints_BuildingUpgrade",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "7D36124B1CC549FF8D0232CE8DABA132",
          "devName": "Workshop.L10.Page01.BuildingMaterials.05",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "Other",
              "currencySubType": "LaborPoints",
              "regularPrice": 200,
              "dynamicRegularPrice": -1,
              "finalPrice": 100,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 100
            }
          ],
          "categories": [],
          "dailyLimit": 3,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "10"
            },
            {
              "key": "MaxWorkshopLevel",
              "value": "11"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 14,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_SupplyPoints_BuildingUpgrade",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "CD1D13838980415E9FEAFC4FCE51ABB3",
          "devName": "Workshop.Page01.ClassTraining.11",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Misc_ShadowEssence",
              "regularPrice": 3,
              "dynamicRegularPrice": -1,
              "finalPrice": 3,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 3
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "689616B946BB3263CDD4F99952A3A666",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "814943904E314407D9148283C9E2F844",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "0"
            },
            {
              "key": "ForceShowFirstItemInGrant",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "/Game/Loot/AccountItems/Reagents/Reagent_ClassTraining_Endurance.Reagent_ClassTraining_Endurance",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_ClassTraining_Endurance",
              "quantity": 1
            },
            {
              "templateId": "Currency:Gold",
              "quantity": 10000
            }
          ]
        },
        {
          "offerId": "1DC95D1B125242FF8BA3627A833468CF",
          "devName": "Workshop.Page01.ClassTraining.29",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Misc_ShadowEssence",
              "regularPrice": 4,
              "dynamicRegularPrice": -1,
              "finalPrice": 4,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 4
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "D98E59024D2A05BB8E7773BD4951B36F",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "CF03EC6145560777C8E2D58CD8588386",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "0"
            },
            {
              "key": "ForceShowFirstItemInGrant",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "/Game/Loot/AccountItems/Reagents/Reagent_ClassTraining_Strength.Reagent_ClassTraining_Strength",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_ClassTraining_Strength",
              "quantity": 1
            },
            {
              "templateId": "Currency:Gold",
              "quantity": 10000
            }
          ]
        },
        {
          "offerId": "D52DE0B0CCB74BA0BBA4A5F8866B9CA1",
          "devName": "Workshop.L22.Page01.BuildRandomItem.11",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "Other",
              "currencySubType": "LaborPoints",
              "regularPrice": 50,
              "dynamicRegularPrice": -1,
              "finalPrice": 50,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 50
            }
          ],
          "categories": [],
          "dailyLimit": 10,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "22"
            },
            {
              "key": "MaxWorkshopLevel",
              "value": "23"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 20,
          "title": "Build Random Item",
          "shortDescription": "",
          "description": "Construct a random item, with a chance to get a hero!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "B57C78F0A96E47C895E5B5B1085AE4FC",
          "devName": "Workshop.Page01.ClassTraining.05",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Misc_ShadowEssence",
              "regularPrice": 4,
              "dynamicRegularPrice": -1,
              "finalPrice": 4,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 4
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "D98E59024D2A05BB8E7773BD4951B36F",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "CF03EC6145560777C8E2D58CD8588386",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "0"
            },
            {
              "key": "ForceShowFirstItemInGrant",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "/Game/Loot/AccountItems/Reagents/Reagent_ClassTraining_Agility.Reagent_ClassTraining_Agility",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_ClassTraining_Agility",
              "quantity": 1
            },
            {
              "templateId": "Currency:Gold",
              "quantity": 10000
            }
          ]
        },
        {
          "offerId": "3E2101505C1C4109A84C065202C734E9",
          "devName": "Workshop.Page01.ClassTraining.12",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Misc_ShadowEssence",
              "regularPrice": 4,
              "dynamicRegularPrice": -1,
              "finalPrice": 4,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 4
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "814943904E314407D9148283C9E2F844",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "D98E59024D2A05BB8E7773BD4951B36F",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "0"
            },
            {
              "key": "ForceShowFirstItemInGrant",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "/Game/Loot/AccountItems/Reagents/Reagent_ClassTraining_Endurance.Reagent_ClassTraining_Endurance",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_ClassTraining_Endurance",
              "quantity": 1
            },
            {
              "templateId": "Currency:Gold",
              "quantity": 10000
            }
          ]
        },
        {
          "offerId": "360F091A509142E7A55A1ED2F051104F",
          "devName": "Workshop.L01.Page01.BuildRandomGear.01",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Shard_Gear",
              "regularPrice": 4,
              "dynamicRegularPrice": -1,
              "finalPrice": 4,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 4
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "1"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 13,
          "title": "Build Random Weapon  (Uncommon)",
          "shortDescription": "",
          "description": "Construct a random Uncommon weapon!",
          "displayAssetPath": "/Game/UMG/Textures/HeroGear/T_Gear_Weapon_Random_01_Uncommon.T_Gear_Weapon_Random_01_Uncommon",
          "itemGrants": []
        },
        {
          "offerId": "998A2925D6294C8EAF0B0A1791936B0F",
          "devName": "Workshop.L12.Page01.BuildingMaterials.06",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "Other",
              "currencySubType": "LaborPoints",
              "regularPrice": 200,
              "dynamicRegularPrice": -1,
              "finalPrice": 100,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 100
            }
          ],
          "categories": [],
          "dailyLimit": 4,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "12"
            },
            {
              "key": "MaxWorkshopLevel",
              "value": "15"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 14,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_SupplyPoints_BuildingUpgrade",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "9CE722D5F83F487BA1024EF1C7B4827F",
          "devName": "Workshop.Page01.ClassTraining.30",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Misc_ShadowEssence",
              "regularPrice": 4,
              "dynamicRegularPrice": -1,
              "finalPrice": 4,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 4
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "CF03EC6145560777C8E2D58CD8588386",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "38278D54469AA644404255919ABC67CF",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "0"
            },
            {
              "key": "ForceShowFirstItemInGrant",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "/Game/Loot/AccountItems/Reagents/Reagent_ClassTraining_Strength.Reagent_ClassTraining_Strength",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_ClassTraining_Strength",
              "quantity": 1
            },
            {
              "templateId": "Currency:Gold",
              "quantity": 10000
            }
          ]
        },
        {
          "offerId": "AB831651BD0C42E7A7D38C2D4EF67F93",
          "devName": "Workshop.Page01.ClassTraining.08",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Misc_ShadowEssence",
              "regularPrice": 5,
              "dynamicRegularPrice": -1,
              "finalPrice": 5,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "E7EEA718452DEDED4574BD9D51CE23A1",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "EBDAA0DC4684721269F4F29A5494519E",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "0"
            },
            {
              "key": "ForceShowFirstItemInGrant",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "/Game/Loot/AccountItems/Reagents/Reagent_ClassTraining_Agility.Reagent_ClassTraining_Agility",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_ClassTraining_Agility",
              "quantity": 1
            },
            {
              "templateId": "Currency:Gold",
              "quantity": 10000
            }
          ]
        },
        {
          "offerId": "A72A10C090554E3FAFFAAC7E509A0A39",
          "devName": "Workshop.L20.Page01.BuildRandomItem.10",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "Other",
              "currencySubType": "LaborPoints",
              "regularPrice": 50,
              "dynamicRegularPrice": -1,
              "finalPrice": 50,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 50
            }
          ],
          "categories": [],
          "dailyLimit": 9,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "20"
            },
            {
              "key": "MaxWorkshopLevel",
              "value": "21"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 20,
          "title": "Build Random Item",
          "shortDescription": "",
          "description": "Construct a random item, with a chance to get a hero!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "EECEA07EAB504F7280ED968778C29E84",
          "devName": "Workshop.L03.Page01.BuildRandomItem.02",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "Other",
              "currencySubType": "LaborPoints",
              "regularPrice": 50,
              "dynamicRegularPrice": -1,
              "finalPrice": 50,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 50
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "3"
            },
            {
              "key": "MaxWorkshopLevel",
              "value": "4"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 20,
          "title": "Build Random Item",
          "shortDescription": "",
          "description": "Construct a random item, with a chance to get a hero!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "C0BDD96231EC43C48A6BC4CA5CE2ED3F",
          "devName": "Workshop.L26.Page01.BuildingMaterials.11",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "Other",
              "currencySubType": "LaborPoints",
              "regularPrice": 200,
              "dynamicRegularPrice": -1,
              "finalPrice": 100,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 100
            }
          ],
          "categories": [],
          "dailyLimit": 9,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "26"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 14,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_SupplyPoints_BuildingUpgrade",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "C2C29029295349C8A43165B228D1E15B",
          "devName": "Workshop.L01.Page01.BuildRxT.01",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_RXT_Parts_Small",
              "regularPrice": 100,
              "dynamicRegularPrice": -1,
              "finalPrice": 100,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 100
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "1"
            },
            {
              "key": "AffordOnly",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 5,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Character:Warrior_SR2_Dark_RoboGuy_T05",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "0CDCCE77C1B94CA18F4A969520953C8C",
          "devName": "Workshop.Page01.ClassTraining.03",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Misc_ShadowEssence",
              "regularPrice": 3,
              "dynamicRegularPrice": -1,
              "finalPrice": 3,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 3
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "689616B946BB3263CDD4F99952A3A666",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "814943904E314407D9148283C9E2F844",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "0"
            },
            {
              "key": "ForceShowFirstItemInGrant",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "/Game/Loot/AccountItems/Reagents/Reagent_ClassTraining_Agility.Reagent_ClassTraining_Agility",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_ClassTraining_Agility",
              "quantity": 1
            },
            {
              "templateId": "Currency:Gold",
              "quantity": 10000
            }
          ]
        },
        {
          "offerId": "3C03DFB85A5C4A43B2CEA594466A74B9",
          "devName": "Workshop.L18.Page01.BuildRandomItem.09",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "Other",
              "currencySubType": "LaborPoints",
              "regularPrice": 50,
              "dynamicRegularPrice": -1,
              "finalPrice": 50,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 50
            }
          ],
          "categories": [],
          "dailyLimit": 8,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "18"
            },
            {
              "key": "MaxWorkshopLevel",
              "value": "19"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 20,
          "title": "Build Random Item",
          "shortDescription": "",
          "description": "Construct a random item, with a chance to get a hero!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "D9FD18151FFE4B2DBE2467572A8584DB",
          "devName": "Workshop.Page01.ClassTraining.07",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Misc_ShadowEssence",
              "regularPrice": 5,
              "dynamicRegularPrice": -1,
              "finalPrice": 5,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "38278D54469AA644404255919ABC67CF",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "E7EEA718452DEDED4574BD9D51CE23A1",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "0"
            },
            {
              "key": "ForceShowFirstItemInGrant",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "/Game/Loot/AccountItems/Reagents/Reagent_ClassTraining_Agility.Reagent_ClassTraining_Agility",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_ClassTraining_Agility",
              "quantity": 1
            },
            {
              "templateId": "Currency:Gold",
              "quantity": 10000
            }
          ]
        },
        {
          "offerId": "595DAC9B5C734AEA88D8C5140D81AE8F",
          "devName": "Workshop.L01.Page01.BuildRockbeast.05",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Pet_Rockbeast",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "1"
            },
            {
              "key": "AffordOnly",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 3,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Character:Pet_R1_Rockbeast_Water_T03",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "592665652C524356A87F92B9778695DE",
          "devName": "Workshop.L01.Page01.BuildRandomGear.05",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Shard_Gear",
              "regularPrice": 10,
              "dynamicRegularPrice": -1,
              "finalPrice": 10,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 10
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "1"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 9,
          "title": "Build Random Armor  (Rare)",
          "shortDescription": "",
          "description": "Construct a random Rare armor!",
          "displayAssetPath": "/Game/UMG/Textures/HeroGear/T_Gear_Armor_Random_02_Rare.T_Gear_Armor_Random_02_Rare",
          "itemGrants": []
        },
        {
          "offerId": "AEADDA2C0873472FB05E03C6BD9B3B1B",
          "devName": "Workshop.L01.Page01.BuildRockbeast.01",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Pet_Rockbeast",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "1"
            },
            {
              "key": "AffordOnly",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 3,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Character:Pet_R1_Rockbeast_Dark_T03",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "FA483E537A324DFF8B544B5144123E82",
          "devName": "Workshop.Page01.ClassTraining.20",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Misc_ShadowEssence",
              "regularPrice": 4,
              "dynamicRegularPrice": -1,
              "finalPrice": 4,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 4
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "814943904E314407D9148283C9E2F844",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "D98E59024D2A05BB8E7773BD4951B36F",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "0"
            },
            {
              "key": "ForceShowFirstItemInGrant",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "/Game/Loot/AccountItems/Reagents/Reagent_ClassTraining_Insight.Reagent_ClassTraining_Insight",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_ClassTraining_Insight",
              "quantity": 1
            },
            {
              "templateId": "Currency:Gold",
              "quantity": 10000
            }
          ]
        },
        {
          "offerId": "3EA0E03038C84C80B11F63C4CE1DC3E5",
          "devName": "Workshop.L01.Page01.BuildRxT.04",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_RXT_Parts_Small",
              "regularPrice": 100,
              "dynamicRegularPrice": -1,
              "finalPrice": 100,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 100
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "1"
            },
            {
              "key": "AffordOnly",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 5,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Character:Warrior_SR2_Nature_RoboGuy_T05",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "EA1E69D4A20245E39FB900BB30DCD4FC",
          "devName": "Workshop.Page01.ClassTraining.04",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Misc_ShadowEssence",
              "regularPrice": 4,
              "dynamicRegularPrice": -1,
              "finalPrice": 4,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 4
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "814943904E314407D9148283C9E2F844",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "D98E59024D2A05BB8E7773BD4951B36F",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "0"
            },
            {
              "key": "ForceShowFirstItemInGrant",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "/Game/Loot/AccountItems/Reagents/Reagent_ClassTraining_Agility.Reagent_ClassTraining_Agility",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_ClassTraining_Agility",
              "quantity": 1
            },
            {
              "templateId": "Currency:Gold",
              "quantity": 10000
            }
          ]
        },
        {
          "offerId": "7B08EFFB6BE04482A0779C1E1B50A6BF",
          "devName": "Workshop.Page01.ClassTraining.10",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Misc_ShadowEssence",
              "regularPrice": 2,
              "dynamicRegularPrice": -1,
              "finalPrice": 2,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 2
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "8550273E418A227A2CCFE7B8825472FF",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "689616B946BB3263CDD4F99952A3A666",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "0"
            },
            {
              "key": "ForceShowFirstItemInGrant",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "/Game/Loot/AccountItems/Reagents/Reagent_ClassTraining_Endurance.Reagent_ClassTraining_Endurance",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_ClassTraining_Endurance",
              "quantity": 1
            },
            {
              "templateId": "Currency:Gold",
              "quantity": 10000
            }
          ]
        },
        {
          "offerId": "A42A8112B2B14853962A04F428248A15",
          "devName": "Workshop.Page01.ClassTraining.25",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Misc_ShadowEssence",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "8550273E418A227A2CCFE7B8825472FF",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "0"
            },
            {
              "key": "AffordOnly",
              "value": "true"
            },
            {
              "key": "ForceShowFirstItemInGrant",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 19,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "/Game/Loot/AccountItems/Reagents/Reagent_ClassTraining_Strength.Reagent_ClassTraining_Strength",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_ClassTraining_Strength",
              "quantity": 1
            },
            {
              "templateId": "Currency:Gold",
              "quantity": 10000
            }
          ]
        },
        {
          "offerId": "660D4B073413491D97DEAA063B1DE063",
          "devName": "Workshop.L01.Page01.BuildRxT.05",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_RXT_Parts_Small",
              "regularPrice": 100,
              "dynamicRegularPrice": -1,
              "finalPrice": 100,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 100
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "1"
            },
            {
              "key": "AffordOnly",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 5,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Character:Warrior_SR2_Water_RoboGuy_T05",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "FAA4E77185704DCC9484B5F26808AFF4",
          "devName": "Workshop.Page01.ClassTraining.16",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Misc_ShadowEssence",
              "regularPrice": 5,
              "dynamicRegularPrice": -1,
              "finalPrice": 5,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "E7EEA718452DEDED4574BD9D51CE23A1",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "EBDAA0DC4684721269F4F29A5494519E",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "0"
            },
            {
              "key": "ForceShowFirstItemInGrant",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "/Game/Loot/AccountItems/Reagents/Reagent_ClassTraining_Endurance.Reagent_ClassTraining_Endurance",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_ClassTraining_Endurance",
              "quantity": 1
            },
            {
              "templateId": "Currency:Gold",
              "quantity": 10000
            }
          ]
        },
        {
          "offerId": "8837ABE8704D4ACB92188D3067B323F1",
          "devName": "Workshop.L12.Page01.BuildRandomItem.06",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "Other",
              "currencySubType": "LaborPoints",
              "regularPrice": 50,
              "dynamicRegularPrice": -1,
              "finalPrice": 50,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 50
            }
          ],
          "categories": [],
          "dailyLimit": 5,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "12"
            },
            {
              "key": "MaxWorkshopLevel",
              "value": "13"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 20,
          "title": "Build Random Item",
          "shortDescription": "",
          "description": "Construct a random item, with a chance to get a hero!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "EE26D473FA3847BA9FFADACDF05F8E77",
          "devName": "Workshop.L01.Page01.BuildRockbeast.02",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Pet_Rockbeast",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "1"
            },
            {
              "key": "AffordOnly",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 3,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Character:Pet_R1_Rockbeast_Fire_T03",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "A444DDB665B34F7E9B9B244038418DAE",
          "devName": "Workshop.L01.Page01.BuildRandomItem.01",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "Other",
              "currencySubType": "LaborPoints",
              "regularPrice": 50,
              "dynamicRegularPrice": -1,
              "finalPrice": 0,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 0
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "1"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 21,
          "title": "Build Random Item",
          "shortDescription": "",
          "description": "Construct a random item, with a chance to get a hero!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "7BAF4F0929C042888CE8F7548BC895FB",
          "devName": "Workshop.L05.Page01.BuildRandomItem.03",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "Other",
              "currencySubType": "LaborPoints",
              "regularPrice": 50,
              "dynamicRegularPrice": -1,
              "finalPrice": 50,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 50
            }
          ],
          "categories": [],
          "dailyLimit": 2,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "5"
            },
            {
              "key": "MaxWorkshopLevel",
              "value": "6"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 20,
          "title": "Build Random Item",
          "shortDescription": "",
          "description": "Construct a random item, with a chance to get a hero!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "AEDDC9EBE4374E09A6BAAF79EEBBB6A9",
          "devName": "Workshop.Page01.ClassTraining.13",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Misc_ShadowEssence",
              "regularPrice": 4,
              "dynamicRegularPrice": -1,
              "finalPrice": 4,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 4
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "D98E59024D2A05BB8E7773BD4951B36F",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "CF03EC6145560777C8E2D58CD8588386",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "0"
            },
            {
              "key": "ForceShowFirstItemInGrant",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "/Game/Loot/AccountItems/Reagents/Reagent_ClassTraining_Endurance.Reagent_ClassTraining_Endurance",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_ClassTraining_Endurance",
              "quantity": 1
            },
            {
              "templateId": "Currency:Gold",
              "quantity": 10000
            }
          ]
        },
        {
          "offerId": "EA114DA3C08B4A68BD20FCD409819FBD",
          "devName": "Workshop.L01.Page01.BuildRandomGear.04",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Shard_Gear",
              "regularPrice": 4,
              "dynamicRegularPrice": -1,
              "finalPrice": 4,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 4
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "1"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 10,
          "title": "Build Random Armor  (Uncommon)",
          "shortDescription": "",
          "description": "Construct a random Uncommon armor!",
          "displayAssetPath": "/Game/UMG/Textures/HeroGear/T_Gear_Armor_Random_01_Uncommon.T_Gear_Armor_Random_01_Uncommon",
          "itemGrants": []
        },
        {
          "offerId": "6C7C7CAC26C642B394F60C9260DB86EE",
          "devName": "Workshop.L01.Page01.BuildStarterPets.01",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "Other",
              "currencySubType": "LaborPoints",
              "regularPrice": 12,
              "dynamicRegularPrice": -1,
              "finalPrice": 12,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 12
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "8299F3BC42C1058E5AFC2ABF92E17A31",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "1"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "Starter Pets",
          "shortDescription": "",
          "description": "A box of pets! Can be opened on the World Map.",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Giftbox:GB_StarterPets",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "3234AE487D1E4282884CEE01FDE27AF2",
          "devName": "Workshop.L07.Page01.BuildingMaterials.02",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Ore:Ore_Magicite",
              "regularPrice": 10,
              "dynamicRegularPrice": -1,
              "finalPrice": 10,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 10
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "7"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 6,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_SupplyPoints_BuildingUpgrade",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "DD13BD9BFB834706B160634B80D2960C",
          "devName": "Workshop.L01.Page01.BuildRockbeast.03",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Pet_Rockbeast",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "1"
            },
            {
              "key": "AffordOnly",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 3,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Character:Pet_R1_Rockbeast_Light_T03",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "7D679A9B638743F7931F6C36C0A14E6E",
          "devName": "Workshop.L16.Page01.BuildRandomItem.08",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "Other",
              "currencySubType": "LaborPoints",
              "regularPrice": 50,
              "dynamicRegularPrice": -1,
              "finalPrice": 50,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 50
            }
          ],
          "categories": [],
          "dailyLimit": 7,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "16"
            },
            {
              "key": "MaxWorkshopLevel",
              "value": "17"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 20,
          "title": "Build Random Item",
          "shortDescription": "",
          "description": "Construct a random item, with a chance to get a hero!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "53C0C070FB9D427D961922FAFC6C53F2",
          "devName": "Workshop.L20.Page01.BuildingMaterials.08",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "Other",
              "currencySubType": "LaborPoints",
              "regularPrice": 200,
              "dynamicRegularPrice": -1,
              "finalPrice": 100,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 100
            }
          ],
          "categories": [],
          "dailyLimit": 6,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "20"
            },
            {
              "key": "MaxWorkshopLevel",
              "value": "21"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 14,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_SupplyPoints_BuildingUpgrade",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "E881D28285B04871A41BC585729F1430",
          "devName": "Workshop.L22.Page01.BuildingMaterials.09",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "Other",
              "currencySubType": "LaborPoints",
              "regularPrice": 200,
              "dynamicRegularPrice": -1,
              "finalPrice": 100,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 100
            }
          ],
          "categories": [],
          "dailyLimit": 7,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "22"
            },
            {
              "key": "MaxWorkshopLevel",
              "value": "23"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 14,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_SupplyPoints_BuildingUpgrade",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "792ABE08EFD4445A978160AA95676104",
          "devName": "Workshop.Page01.ClassTraining.14",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Misc_ShadowEssence",
              "regularPrice": 4,
              "dynamicRegularPrice": -1,
              "finalPrice": 4,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 4
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "CF03EC6145560777C8E2D58CD8588386",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "38278D54469AA644404255919ABC67CF",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "0"
            },
            {
              "key": "ForceShowFirstItemInGrant",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "/Game/Loot/AccountItems/Reagents/Reagent_ClassTraining_Endurance.Reagent_ClassTraining_Endurance",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_ClassTraining_Endurance",
              "quantity": 1
            },
            {
              "templateId": "Currency:Gold",
              "quantity": 10000
            }
          ]
        },
        {
          "offerId": "94F85A09F8CA4CD1B760D4A4AE598983",
          "devName": "Workshop.Page01.ClassTraining.23",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Misc_ShadowEssence",
              "regularPrice": 5,
              "dynamicRegularPrice": -1,
              "finalPrice": 5,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "38278D54469AA644404255919ABC67CF",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "E7EEA718452DEDED4574BD9D51CE23A1",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "0"
            },
            {
              "key": "ForceShowFirstItemInGrant",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "/Game/Loot/AccountItems/Reagents/Reagent_ClassTraining_Insight.Reagent_ClassTraining_Insight",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_ClassTraining_Insight",
              "quantity": 1
            },
            {
              "templateId": "Currency:Gold",
              "quantity": 10000
            }
          ]
        },
        {
          "offerId": "FD57DC54925E43438479D208009D51AA",
          "devName": "Workshop.L01.Page01.BuildWCHero.02",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_WC_Hero_TripleCombo",
              "regularPrice": 100,
              "dynamicRegularPrice": -1,
              "finalPrice": 100,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 100
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "1"
            },
            {
              "key": "AffordOnly",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 4,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Character:MartialArtist_SR2_Nature_TripleCombo_T04",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "3BC0F14708134510B1061401D580EDD8",
          "devName": "Workshop.L14.Page01.BuildRandomItem.07",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "Other",
              "currencySubType": "LaborPoints",
              "regularPrice": 50,
              "dynamicRegularPrice": -1,
              "finalPrice": 50,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 50
            }
          ],
          "categories": [],
          "dailyLimit": 6,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "14"
            },
            {
              "key": "MaxWorkshopLevel",
              "value": "15"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 20,
          "title": "Build Random Item",
          "shortDescription": "",
          "description": "Construct a random item, with a chance to get a hero!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "B7896D4E2028431DA84ED1CAFF60B282",
          "devName": "Workshop.Page01.ClassTraining.27",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Misc_ShadowEssence",
              "regularPrice": 3,
              "dynamicRegularPrice": -1,
              "finalPrice": 3,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 3
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "689616B946BB3263CDD4F99952A3A666",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "814943904E314407D9148283C9E2F844",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "0"
            },
            {
              "key": "ForceShowFirstItemInGrant",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "/Game/Loot/AccountItems/Reagents/Reagent_ClassTraining_Strength.Reagent_ClassTraining_Strength",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_ClassTraining_Strength",
              "quantity": 1
            },
            {
              "templateId": "Currency:Gold",
              "quantity": 10000
            }
          ]
        },
        {
          "offerId": "83D99E84967645AB81A03B99684C8F81",
          "devName": "Workshop.L26.Page01.BuildRandomItem.13",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "Other",
              "currencySubType": "LaborPoints",
              "regularPrice": 50,
              "dynamicRegularPrice": -1,
              "finalPrice": 50,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 50
            }
          ],
          "categories": [],
          "dailyLimit": 12,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "26"
            },
            {
              "key": "MaxWorkshopLevel",
              "value": "27"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 20,
          "title": "Build Random Item",
          "shortDescription": "",
          "description": "Construct a random item, with a chance to get a hero!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "D7FDE1D864D2492A80098D0F94D4347F",
          "devName": "Workshop.Page01.ClassTraining.18",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Misc_ShadowEssence",
              "regularPrice": 2,
              "dynamicRegularPrice": -1,
              "finalPrice": 2,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 2
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "8550273E418A227A2CCFE7B8825472FF",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "689616B946BB3263CDD4F99952A3A666",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "0"
            },
            {
              "key": "ForceShowFirstItemInGrant",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "/Game/Loot/AccountItems/Reagents/Reagent_ClassTraining_Insight.Reagent_ClassTraining_Insight",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_ClassTraining_Insight",
              "quantity": 1
            },
            {
              "templateId": "Currency:Gold",
              "quantity": 10000
            }
          ]
        },
        {
          "offerId": "FD72465BF9C7450995D11CA951ED14CA",
          "devName": "Workshop.L28.Page01.BuildRandomItem.14",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "Other",
              "currencySubType": "LaborPoints",
              "regularPrice": 50,
              "dynamicRegularPrice": -1,
              "finalPrice": 50,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 50
            }
          ],
          "categories": [],
          "dailyLimit": 13,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "28"
            },
            {
              "key": "MaxWorkshopLevel",
              "value": "29"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 20,
          "title": "Build Random Item",
          "shortDescription": "",
          "description": "Construct a random item, with a chance to get a hero!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "CE9B09D0BB6E44B5BF25CE8A0A375014",
          "devName": "Workshop.L01.Page01.BuildRandomGear.03",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Shard_Gear",
              "regularPrice": 20,
              "dynamicRegularPrice": -1,
              "finalPrice": 20,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 20
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "1"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 11,
          "title": "Build Random Weapon  (VeryRare)",
          "shortDescription": "",
          "description": "Construct a random Very Rare weapon!",
          "displayAssetPath": "/Game/UMG/Textures/HeroGear/T_Gear_Weapon_Random_03_VeryRare.T_Gear_Weapon_Random_03_VeryRare",
          "itemGrants": []
        },
        {
          "offerId": "A322035FE49443A198939406F96417DE",
          "devName": "Workshop.Page01.ClassTraining.09",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Misc_ShadowEssence",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "8550273E418A227A2CCFE7B8825472FF",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "0"
            },
            {
              "key": "AffordOnly",
              "value": "true"
            },
            {
              "key": "ForceShowFirstItemInGrant",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 19,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "/Game/Loot/AccountItems/Reagents/Reagent_ClassTraining_Endurance.Reagent_ClassTraining_Endurance",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_ClassTraining_Endurance",
              "quantity": 1
            },
            {
              "templateId": "Currency:Gold",
              "quantity": 10000
            }
          ]
        },
        {
          "offerId": "927CE6F9076143E2BBFEAAB341EBF3D9",
          "devName": "Workshop.Page01.ClassTraining.15",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Misc_ShadowEssence",
              "regularPrice": 5,
              "dynamicRegularPrice": -1,
              "finalPrice": 5,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "38278D54469AA644404255919ABC67CF",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "E7EEA718452DEDED4574BD9D51CE23A1",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "0"
            },
            {
              "key": "ForceShowFirstItemInGrant",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "/Game/Loot/AccountItems/Reagents/Reagent_ClassTraining_Endurance.Reagent_ClassTraining_Endurance",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_ClassTraining_Endurance",
              "quantity": 1
            },
            {
              "templateId": "Currency:Gold",
              "quantity": 10000
            }
          ]
        },
        {
          "offerId": "C51FD14F091B47A88D2743D2AE3A49FA",
          "devName": "Workshop.Page01.ClassTraining.28",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Misc_ShadowEssence",
              "regularPrice": 4,
              "dynamicRegularPrice": -1,
              "finalPrice": 4,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 4
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "814943904E314407D9148283C9E2F844",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "D98E59024D2A05BB8E7773BD4951B36F",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "0"
            },
            {
              "key": "ForceShowFirstItemInGrant",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "/Game/Loot/AccountItems/Reagents/Reagent_ClassTraining_Strength.Reagent_ClassTraining_Strength",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_ClassTraining_Strength",
              "quantity": 1
            },
            {
              "templateId": "Currency:Gold",
              "quantity": 10000
            }
          ]
        },
        {
          "offerId": "96C2B3F56549429CAE5862D122B97102",
          "devName": "Workshop.L01.Page01.BuildWCHero.03",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_WC_Hero_TripleCombo",
              "regularPrice": 100,
              "dynamicRegularPrice": -1,
              "finalPrice": 100,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 100
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "1"
            },
            {
              "key": "AffordOnly",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 4,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Character:MartialArtist_SR2_Water_TripleCombo_T04",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "D80B13049A804C3FBA56C6C9C589F60C",
          "devName": "Workshop.L30.Page01.BuildRandomItem.15",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "Other",
              "currencySubType": "LaborPoints",
              "regularPrice": 50,
              "dynamicRegularPrice": -1,
              "finalPrice": 50,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 50
            }
          ],
          "categories": [],
          "dailyLimit": 14,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "30"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 20,
          "title": "Build Random Item",
          "shortDescription": "",
          "description": "Construct a random item, with a chance to get a hero!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "2B6943D5F2C5450EBB015025D336077B",
          "devName": "Workshop.L07.Page01.BuildRandomItem.04",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "Other",
              "currencySubType": "LaborPoints",
              "regularPrice": 50,
              "dynamicRegularPrice": -1,
              "finalPrice": 50,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 50
            }
          ],
          "categories": [],
          "dailyLimit": 3,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "7"
            },
            {
              "key": "MaxWorkshopLevel",
              "value": "9"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 20,
          "title": "Build Random Item",
          "shortDescription": "",
          "description": "Construct a random item, with a chance to get a hero!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "8A509646F7D24171A36D05C5F924CEA3",
          "devName": "Workshop.L10.Page01.BuildRandomItem.05",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "Other",
              "currencySubType": "LaborPoints",
              "regularPrice": 50,
              "dynamicRegularPrice": -1,
              "finalPrice": 50,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 50
            }
          ],
          "categories": [],
          "dailyLimit": 4,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "10"
            },
            {
              "key": "MaxWorkshopLevel",
              "value": "11"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 20,
          "title": "Build Random Item",
          "shortDescription": "",
          "description": "Construct a random item, with a chance to get a hero!",
          "displayAssetPath": "",
          "itemGrants": []
        },
        {
          "offerId": "5D6C4EE12C844BC59ABB107D88DA5C6A",
          "devName": "Workshop.Page01.ClassTraining.19",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Misc_ShadowEssence",
              "regularPrice": 3,
              "dynamicRegularPrice": -1,
              "finalPrice": 3,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 3
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "689616B946BB3263CDD4F99952A3A666",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "814943904E314407D9148283C9E2F844",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "0"
            },
            {
              "key": "ForceShowFirstItemInGrant",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "/Game/Loot/AccountItems/Reagents/Reagent_ClassTraining_Insight.Reagent_ClassTraining_Insight",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_ClassTraining_Insight",
              "quantity": 1
            },
            {
              "templateId": "Currency:Gold",
              "quantity": 10000
            }
          ]
        },
        {
          "offerId": "2965FC95A8A84C51B7980CADD027A731",
          "devName": "Workshop.Page01.ClassTraining.21",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Misc_ShadowEssence",
              "regularPrice": 4,
              "dynamicRegularPrice": -1,
              "finalPrice": 4,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 4
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "D98E59024D2A05BB8E7773BD4951B36F",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "CF03EC6145560777C8E2D58CD8588386",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "0"
            },
            {
              "key": "ForceShowFirstItemInGrant",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "/Game/Loot/AccountItems/Reagents/Reagent_ClassTraining_Insight.Reagent_ClassTraining_Insight",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_ClassTraining_Insight",
              "quantity": 1
            },
            {
              "templateId": "Currency:Gold",
              "quantity": 10000
            }
          ]
        },
        {
          "offerId": "524F0F7663CF41F7B10E1719BE9E0D0C",
          "devName": "Workshop.Page01.ClassTraining.22",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Misc_ShadowEssence",
              "regularPrice": 4,
              "dynamicRegularPrice": -1,
              "finalPrice": 4,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 4
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "CF03EC6145560777C8E2D58CD8588386",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "38278D54469AA644404255919ABC67CF",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "0"
            },
            {
              "key": "ForceShowFirstItemInGrant",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "/Game/Loot/AccountItems/Reagents/Reagent_ClassTraining_Insight.Reagent_ClassTraining_Insight",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_ClassTraining_Insight",
              "quantity": 1
            },
            {
              "templateId": "Currency:Gold",
              "quantity": 10000
            }
          ]
        },
        {
          "offerId": "39343131B8CC409D83781CD03FF8BE93",
          "devName": "Workshop.Page01.ClassTraining.06",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Misc_ShadowEssence",
              "regularPrice": 4,
              "dynamicRegularPrice": -1,
              "finalPrice": 4,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 4
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "CF03EC6145560777C8E2D58CD8588386",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "38278D54469AA644404255919ABC67CF",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "0"
            },
            {
              "key": "ForceShowFirstItemInGrant",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "/Game/Loot/AccountItems/Reagents/Reagent_ClassTraining_Agility.Reagent_ClassTraining_Agility",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_ClassTraining_Agility",
              "quantity": 1
            },
            {
              "templateId": "Currency:Gold",
              "quantity": 10000
            }
          ]
        },
        {
          "offerId": "3462326DE9BC4C40AB6F9842C7CD0CC1",
          "devName": "Workshop.L07.Page01.BuildingMaterials.03",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "Other",
              "currencySubType": "LaborPoints",
              "regularPrice": 200,
              "dynamicRegularPrice": -1,
              "finalPrice": 100,
              "saleType": "AmountOff",
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 100
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "7"
            },
            {
              "key": "MaxWorkshopLevel",
              "value": "7"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 14,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_SupplyPoints_BuildingUpgrade",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "C2BFCE1B94FC43E09FEEAB703A1020B1",
          "devName": "Workshop.Page01.ClassTraining.32",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Misc_ShadowEssence",
              "regularPrice": 5,
              "dynamicRegularPrice": -1,
              "finalPrice": 5,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "E7EEA718452DEDED4574BD9D51CE23A1",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "EBDAA0DC4684721269F4F29A5494519E",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "0"
            },
            {
              "key": "ForceShowFirstItemInGrant",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "/Game/Loot/AccountItems/Reagents/Reagent_ClassTraining_Strength.Reagent_ClassTraining_Strength",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_ClassTraining_Strength",
              "quantity": 1
            },
            {
              "templateId": "Currency:Gold",
              "quantity": 10000
            }
          ]
        },
        {
          "offerId": "8EA392B3527244AB92C81A6E5A0B1418",
          "devName": "Workshop.Page01.ClassTraining.02",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Misc_ShadowEssence",
              "regularPrice": 2,
              "dynamicRegularPrice": -1,
              "finalPrice": 2,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 2
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "8550273E418A227A2CCFE7B8825472FF",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "689616B946BB3263CDD4F99952A3A666",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "0"
            },
            {
              "key": "ForceShowFirstItemInGrant",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "/Game/Loot/AccountItems/Reagents/Reagent_ClassTraining_Agility.Reagent_ClassTraining_Agility",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_ClassTraining_Agility",
              "quantity": 1
            },
            {
              "templateId": "Currency:Gold",
              "quantity": 10000
            }
          ]
        },
        {
          "offerId": "CB2331F8D2C04FC08ED86C1CA9F60ABC",
          "devName": "Workshop.Page01.ClassTraining.01",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Misc_ShadowEssence",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "8550273E418A227A2CCFE7B8825472FF",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "0"
            },
            {
              "key": "AffordOnly",
              "value": "true"
            },
            {
              "key": "ForceShowFirstItemInGrant",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 19,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "/Game/Loot/AccountItems/Reagents/Reagent_ClassTraining_Agility.Reagent_ClassTraining_Agility",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_ClassTraining_Agility",
              "quantity": 1
            },
            {
              "templateId": "Currency:Gold",
              "quantity": 10000
            }
          ]
        },
        {
          "offerId": "67874B020E8949A29A1B4EE00FFE5B2B",
          "devName": "Workshop.L01.Page01.BuildRandomGear.02",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Shard_Gear",
              "regularPrice": 10,
              "dynamicRegularPrice": -1,
              "finalPrice": 10,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 10
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "1"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 12,
          "title": "Build Random Weapon  (Rare)",
          "shortDescription": "",
          "description": "Construct a random Rare weapon!",
          "displayAssetPath": "/Game/UMG/Textures/HeroGear/T_Gear_Weapon_Random_02_Rare.T_Gear_Weapon_Random_02_Rare",
          "itemGrants": []
        },
        {
          "offerId": "8EA48D2163DE42D394B3AE2E192FD4D1",
          "devName": "Workshop.Page01.ClassTraining.26",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Misc_ShadowEssence",
              "regularPrice": 2,
              "dynamicRegularPrice": -1,
              "finalPrice": 2,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 2
            }
          ],
          "categories": [],
          "dailyLimit": 1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [
            {
              "requirementType": "RequireFulfillment",
              "requiredId": "8550273E418A227A2CCFE7B8825472FF",
              "minQuantity": 1
            },
            {
              "requirementType": "DenyOnFulfillment",
              "requiredId": "689616B946BB3263CDD4F99952A3A666",
              "minQuantity": 1
            }
          ],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "0"
            },
            {
              "key": "ForceShowFirstItemInGrant",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 0,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "/Game/Loot/AccountItems/Reagents/Reagent_ClassTraining_Strength.Reagent_ClassTraining_Strength",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_ClassTraining_Strength",
              "quantity": 1
            },
            {
              "templateId": "Currency:Gold",
              "quantity": 10000
            }
          ]
        },
        {
          "offerId": "F3C70C0BDCDF4AD6B5CC49703466F2DB",
          "devName": "Workshop.L01.Page01.BuildWCHero.01",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_WC_Hero_TripleCombo",
              "regularPrice": 100,
              "dynamicRegularPrice": -1,
              "finalPrice": 100,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 100
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "1"
            },
            {
              "key": "AffordOnly",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 4,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Character:MartialArtist_SR2_Fire_TripleCombo_T04",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "FE1764674550435EA71F95C4DE11AC32",
          "devName": "Workshop.L01.Page01.BuildRxT.03",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_RXT_Parts_Small",
              "regularPrice": 100,
              "dynamicRegularPrice": -1,
              "finalPrice": 100,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 100
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "1"
            },
            {
              "key": "AffordOnly",
              "value": "true"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 5,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Character:Warrior_SR2_Light_RoboGuy_T05",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "CB1B6DE6B938471392033377C59D07A1",
          "devName": "Workshop.L24.Page01.BuildRandomItem.12",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "Other",
              "currencySubType": "LaborPoints",
              "regularPrice": 50,
              "dynamicRegularPrice": -1,
              "finalPrice": 50,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 50
            }
          ],
          "categories": [],
          "dailyLimit": 11,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [
            {
              "key": "WorkshopLevel",
              "value": "24"
            },
            {
              "key": "MaxWorkshopLevel",
              "value": "25"
            }
          ],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 20,
          "title": "Build Random Item",
          "shortDescription": "",
          "description": "Construct a random item, with a chance to get a hero!",
          "displayAssetPath": "",
          "itemGrants": []
        }
      ]
    },
    {
      "name": "Loyalty",
      "catalogEntries": [
        {
          "offerId": "AA3FFA0E094C458288F767E35252F9EF",
          "devName": "Loyalty.Core.07",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Loyalty",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 108,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Currency:Hammer",
              "quantity": 10
            }
          ]
        },
        {
          "offerId": "056554B3FF0F418BB3552D4F5DB7492C",
          "devName": "Loyalty.Core.01",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Loyalty",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 105,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Dark",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "2D61B2E4BEC54B0C868AB5F4B6AB5DC2",
          "devName": "Loyalty.Core.11",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Loyalty",
              "regularPrice": 5,
              "dynamicRegularPrice": -1,
              "finalPrice": 5,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 5
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 124,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Voucher:Voucher_Chest_Gold",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "EF704CF0A84043BCB11AD8F9ABA7CC7F",
          "devName": "Loyalty.Core.10",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Loyalty",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 109,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "UpgradePotion:UpgradeMana",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "D3CB18AB960D498D96989D8B90269023",
          "devName": "Loyalty.Core.02",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Loyalty",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 104,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Fire",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "79E8E5F67DA7444D922FAFCD75DCEEF9",
          "devName": "Loyalty.Core.24",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Loyalty",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 112,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Foil",
              "quantity": 10
            }
          ]
        },
        {
          "offerId": "E21DB557AA3944158DE9B1FDFCF26E7A",
          "devName": "Loyalty.Core.23",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Loyalty",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 113,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Currency:SkillXP",
              "quantity": 1000
            }
          ]
        },
        {
          "offerId": "8D71F61D65704ADFB0AC44E632B1B0B4",
          "devName": "Loyalty.Core.09",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Loyalty",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 107,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Ore:Ore_Magicite",
              "quantity": 10
            }
          ]
        },
        {
          "offerId": "DA55598A71C946CDBB5E06BC5D70B7B9",
          "devName": "Loyalty.Core.13",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Loyalty",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 122,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_HeroMap_Elemental",
              "quantity": 40
            }
          ]
        },
        {
          "offerId": "061580998D7E4B169085B020B158C76E",
          "devName": "Loyalty.Core.05",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Loyalty",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 101,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Water",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "DDB177DDFA4D41CE8E8C9F709D1C2A09",
          "devName": "Loyalty.Core.14",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Loyalty",
              "regularPrice": 3,
              "dynamicRegularPrice": -1,
              "finalPrice": 3,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 3
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 123,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_HeroMap_SuperRare",
              "quantity": 4
            }
          ]
        },
        {
          "offerId": "5A897D6674364002915EDD91769EDE4A",
          "devName": "Loyalty.Core.19",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Loyalty",
              "regularPrice": 10,
              "dynamicRegularPrice": -1,
              "finalPrice": 10,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 10
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 115,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_RXT_Parts_Large",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "A09EFF312ACC4C0A9D8F137709879751",
          "devName": "Loyalty.Core.15",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Loyalty",
              "regularPrice": 25,
              "dynamicRegularPrice": -1,
              "finalPrice": 25,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 25
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 119,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Misc_CeremonialArmor",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "42CEF781441C458E9E79E18DF15E7440",
          "devName": "Loyalty.Core.04",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Loyalty",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 102,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Nature",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "CED30C36836C4FFFACAC5034DDFBDFDC",
          "devName": "Loyalty.Core.22",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Loyalty",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 106,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Currency:Gold",
              "quantity": 1000000
            }
          ]
        },
        {
          "offerId": "5965E83FA8984B46BB636994F7B0D604",
          "devName": "Loyalty.Core.20",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Loyalty",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 114,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_RXT_Parts_Small",
              "quantity": 10
            }
          ]
        },
        {
          "offerId": "87366DCFB6634722BEDD55AB3BE2959D",
          "devName": "Loyalty.Core.21",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Loyalty",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 108,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_SupplyPoints_BuildingUpgrade",
              "quantity": 5
            }
          ]
        },
        {
          "offerId": "A249D316D4C0451B84DD6ACB01B4B228",
          "devName": "Loyalty.Core.03",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Loyalty",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 103,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shard_Light",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "8B2CE0BC32A94FBE877B47F1A74A405F",
          "devName": "Loyalty.Core.25",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Loyalty",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 120,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_SupplyPoints_Elite",
              "quantity": 20
            }
          ]
        },
        {
          "offerId": "F6B435AE52DD422CB67B43526BB5D4C7",
          "devName": "Loyalty.Core.16",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Loyalty",
              "regularPrice": 7,
              "dynamicRegularPrice": -1,
              "finalPrice": 7,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 7
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 118,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Misc_CeremonialShield",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "CF0BEDCD785546FC899B910F34461ADC",
          "devName": "Loyalty.Core.17",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Loyalty",
              "regularPrice": 2,
              "dynamicRegularPrice": -1,
              "finalPrice": 2,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 2
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 117,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Misc_CeremonialSword",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "84FD0A89046A457D8514EE88A0F6C4DD",
          "devName": "Loyalty.Core.12",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Loyalty",
              "regularPrice": 3,
              "dynamicRegularPrice": -1,
              "finalPrice": 3,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 3
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 121,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_HeroMap_Bronze",
              "quantity": 2
            }
          ]
        },
        {
          "offerId": "5FB082AF85044E4198618888C61D2D09",
          "devName": "Loyalty.Core.06",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Loyalty",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 100,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shared_T02",
              "quantity": 75
            }
          ]
        },
        {
          "offerId": "29F46B6355AC4BFE832F178E6F9527F2",
          "devName": "Loyalty.Core.18",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Loyalty",
              "regularPrice": 15,
              "dynamicRegularPrice": -1,
              "finalPrice": 15,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 15
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 116,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Reagent:Reagent_Shared_MysteryGoo",
              "quantity": 1
            }
          ]
        },
        {
          "offerId": "C27AAA587BF0405C9E4836E9F4D5F056",
          "devName": "Loyalty.Core.08",
          "offerType": "StaticPrice",
          "prices": [
            {
              "currencyType": "GameItem",
              "currencySubType": "Reagent:Reagent_Loyalty",
              "regularPrice": 1,
              "dynamicRegularPrice": -1,
              "finalPrice": 1,
              "saleExpiration": "9999-12-31T23:59:59.999Z",
              "basePrice": 1
            }
          ],
          "categories": [],
          "dailyLimit": -1,
          "weeklyLimit": -1,
          "monthlyLimit": -1,
          "refundable": false,
          "appStoreId": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "requirements": [],
          "metaInfo": [],
          "catalogGroup": "",
          "catalogGroupPriority": 0,
          "sortPriority": 125,
          "title": "",
          "shortDescription": "",
          "description": "",
          "displayAssetPath": "",
          "itemGrants": [
            {
              "templateId": "Currency:MtxGiveaway",
              "quantity": 100
            }
          ]
        }
      ]
    }
  ]
}
```

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
