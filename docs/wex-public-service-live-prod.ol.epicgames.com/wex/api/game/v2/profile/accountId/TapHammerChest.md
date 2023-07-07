# Tap Hammer Chest

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/:accountId/TapHammerChest?profileId=profile0&rvn=40453*

___

## Request

```http
POST /wex/api/game/v2/profile/:accountId/TapHammerChest?profileId=profile0&rvn=40453 HTTP/1.1
```

### Path Parameters

| Name     | Value                             |
|----------|-----------------------------------|
| acountId | ec0ebb7e56f6454e86c62299a7b32e21  |

### Query String

| Name | Value |
|---|---|
| profileId | profile0 |
| rvn | 40453 |

### Request Headers

| Name | Value |
|---|---|
| Host | wex-public-service-live-prod.ol.epicgames.com |
| Accept-Encoding | deflate, gzip |
| Accept | \*/\* |
| Content-Type | application/json |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":24140},{"profileId":"levels","clientCommandRevision":14478},{"profileId":"friends","clientCommandRevision":8264},{"profileId":"monsterpit","clientCommandRevision":1081},{"profileId":"multiplayer","clientCommandRevision":900}] |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-4062E7984D4E789AC6BD2187EDA88976 |
| User-Agent | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit |
| Authorization | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |
| Content-Length | 4 |

### Request Body

```json
{}
```

___

## Response

#### Status: 200 OK

### Response Headers

| Name | Value |
|---|---|
| Date | Thu, 29 Dec 2022 05:53:30 GMT |
| Content-Type | application/json |
| Content-Length | 995 |
| X-EpicGames-Profile-Revision | 40453 |
| X-EpicGames-McpVersion | prod Release-1.88-1.88 build 107 cl 19310354 |
| X-EpicGames-ContentVersion | 1.88.244-r17036752 |
| X-EpicGames-MinBuild | 17036752 |
| X-Epic-Device-ID | 68009daed09498667a8039cce09983ed |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-4062E7984D4E789AC6BD2187EDA88976 |
| Connection | keep-alive |

### Response Body

```json
{
  "profileRevision": 40454,
  "profileId": "profile0",
  "profileChangesBaseRevision": 40453,
  "profileChanges": [
    {
      "changeType": "itemRemoved",
      "itemId": "5f600e85-d9a4-4f31-8e31-8f025618661b"
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "128a407b-f755-42f1-9370-4f6e3beec0b7",
      "attributeName": "taps_remaining",
      "attributeValue": 6
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "128a407b-f755-42f1-9370-4f6e3beec0b7",
      "attributeName": "taps_applied",
      "attributeValue": 2
    },
    {
      "changeType": "itemQuantityChanged",
      "itemId": "161dcb8d-4116-47b9-a0c4-53449ac7eb89",
      "quantity": 26
    }
  ],
  "notifications": [
    {
      "type": "WExpHammerChestOpened",
      "primary": true,
      "templateId": "HammerChest:HC_Upgrade_Advanced_Normal",
      "bCompleted": false,
      "lootResult": {
        "tierGroupName": "LTG.HammerChest.Upgrade.Advanced.Normal.Hit",
        "items": [
          {
            "itemType": "UpgradePotion:UpgradeHealthMajor",
            "itemGuid": "161dcb8d-4116-47b9-a0c4-53449ac7eb89",
            "itemProfile": "profile0",
            "quantity": 2
          }
        ]
      }
    }
  ],
  "profileCommandRevision": 24141,
  "serverTime": "2022-12-29T05:53:30.029Z",
  "responseVersion": 1
}
```

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
