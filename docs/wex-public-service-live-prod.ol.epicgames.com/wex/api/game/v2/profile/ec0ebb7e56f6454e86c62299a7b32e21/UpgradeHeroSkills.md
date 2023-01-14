# UpgradeHeroSkills

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/UpgradeHeroSkills?profileId=profile0&rvn=40503*



___

## Request

```http request
POST /wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/UpgradeHeroSkills?profileId=profile0&rvn=40503 HTTP/1.1
```

### Query String

| Name | Value |
|---|---|
| profileId | profile0 |
| rvn | 40503 |




### Request Headers

| Name | Value |
|---|---|
| Host | wex-public-service-live-prod.ol.epicgames.com |
| Accept-Encoding | deflate, gzip |
| Accept | \*/\* |
| Content-Type | application/json |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":24188},{"profileId":"levels","clientCommandRevision":14480},{"profileId":"friends","clientCommandRevision":8264},{"profileId":"monsterpit","clientCommandRevision":1081},{"profileId":"multiplayer","clientCommandRevision":900}] |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-9464BCAA4D34E3C5363C9880E319DFD0 |
| User-Agent | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit |
| Authorization | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |
| Content-Length | 101 |


### Request Body

```json
{
  "heroItemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
  "bIsInPit": false,
  "xpToSpend": 1900
}
```

___

## Response

#### Status: 200 OK




### Response Headers

| Name | Value |
|---|---|
| Date | Thu, 29 Dec 2022 06:07:35 GMT |
| Content-Type | application/json |
| Content-Length | 553 |
| X-EpicGames-Profile-Revision | 40503 |
| X-EpicGames-McpVersion | prod Release-1.88-1.88 build 107 cl 19310354 |
| X-EpicGames-ContentVersion | 1.88.244-r17036752 |
| X-EpicGames-MinBuild | 17036752 |
| X-Epic-Device-ID | 68009daed09498667a8039cce09983ed |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-9464BCAA4D34E3C5363C9880E319DFD0 |
| Connection | keep-alive |


### Response Body

```json
{
  "profileRevision": 40504,
  "profileId": "profile0",
  "profileChangesBaseRevision": 40503,
  "profileChanges": [
    {
      "changeType": "itemQuantityChanged",
      "itemId": "9aec267c-4ab3-451f-8762-2dfc405de2a0",
      "quantity": 176694
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "attributeName": "skill_level",
      "attributeValue": 20
    }
  ],
  "notifications": [
    {
      "type": "CharacterSkillLevelUp",
      "primary": false,
      "itemId": "9ffabcc0-9cc4-40e7-ab89-5edd4b0c328d",
      "level": 20
    }
  ],
  "profileCommandRevision": 24189,
  "serverTime": "2022-12-29T06:07:35.759Z",
  "responseVersion": 1
}
```

*Response body was encoded in base64*

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
