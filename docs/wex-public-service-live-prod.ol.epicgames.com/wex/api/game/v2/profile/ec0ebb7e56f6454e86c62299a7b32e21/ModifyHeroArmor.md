# ModifyHeroArmor

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/ModifyHeroArmor?profileId=profile0&rvn=40526*



___

## Request

```http request
POST /wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/ModifyHeroArmor?profileId=profile0&rvn=40526 HTTP/1.1
```

### Query String

| Name | Value |
|---|---|
| profileId | profile0 |
| rvn | 40526 |




### Request Headers

| Name | Value |
|---|---|
| Host | wex-public-service-live-prod.ol.epicgames.com |
| Accept-Encoding | deflate, gzip |
| Accept | \*/\* |
| Content-Type | application/json |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":24205},{"profileId":"levels","clientCommandRevision":14486},{"profileId":"friends","clientCommandRevision":8264},{"profileId":"monsterpit","clientCommandRevision":1081},{"profileId":"multiplayer","clientCommandRevision":900}] |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-90A080A34F3E0A697BF55D9A314765E1 |
| User-Agent | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit |
| Authorization | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |
| Content-Length | 141 |


### Request Body

```json
{
  "heroItemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
  "bIsInPit": false,
  "gearArmorItemId": "3ea00890-02b0-42e4-b418-baf54052cec7"
}
```

___

## Response

#### Status: 200 OK




### Response Headers

| Name | Value |
|---|---|
| Date | Thu, 29 Dec 2022 06:09:17 GMT |
| Content-Type | application/json |
| Content-Length | 668 |
| X-EpicGames-Profile-Revision | 40526 |
| X-EpicGames-McpVersion | prod Release-1.88-1.88 build 107 cl 19310354 |
| X-EpicGames-ContentVersion | 1.88.244-r17036752 |
| X-EpicGames-MinBuild | 17036752 |
| X-Epic-Device-ID | 68009daed09498667a8039cce09983ed |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-90A080A34F3E0A697BF55D9A314765E1 |
| Connection | keep-alive |


### Response Body

```json
{
  "profileRevision": 40527,
  "profileId": "profile0",
  "profileChangesBaseRevision": 40526,
  "profileChanges": [
    {
      "changeType": "itemAttrChanged",
      "itemId": "3ea00890-02b0-42e4-b418-baf54052cec7",
      "attributeName": "is_disabled",
      "attributeValue": true
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "3ea00890-02b0-42e4-b418-baf54052cec7",
      "attributeName": "hero_item_id",
      "attributeValue": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d"
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "gear_armor_item_id",
      "attributeValue": "3ea00890-02b0-42e4-b418-baf54052cec7"
    }
  ],
  "profileCommandRevision": 24206,
  "serverTime": "2022-12-29T06:09:17.693Z",
  "responseVersion": 1
}
```

*Response body was encoded in base64*

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
