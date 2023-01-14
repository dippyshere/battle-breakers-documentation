# UpdateMonsterPitPower

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/UpdateMonsterPitPower?profileId=monsterpit&rvn=6487*

___

## Request

```http request
POST /wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/UpdateMonsterPitPower?profileId=monsterpit&rvn=6487 HTTP/1.1
```

### Query String

| Name | Value |
|---|---|
| profileId | monsterpit |
| rvn | 6487 |




### Request Headers

| Name | Value |
|---|---|
| Host | wex-public-service-live-prod.ol.epicgames.com |
| Accept-Encoding | deflate, gzip |
| Accept | \*/\* |
| Content-Type | application/json |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":23951},{"profileId":"levels","clientCommandRevision":14433},{"profileId":"friends","clientCommandRevision":8252},{"profileId":"monsterpit","clientCommandRevision":1080},{"profileId":"multiplayer","clientCommandRevision":900}] |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-BF5B64544412777DD4C71C8545BEAE11-A17C161844A45BEB8831DC891A0EF6C5 |
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
| Date | Wed, 28 Dec 2022 12:09:44 GMT |
| Content-Type | application/json |
| Content-Length | 1420 |
| X-EpicGames-Profile-Revision | 6487 |
| X-EpicGames-McpVersion | prod Release-1.88-1.88 build 107 cl 19310354 |
| X-EpicGames-ContentVersion | 1.88.244-r17036752 |
| X-EpicGames-MinBuild | 17036752 |
| X-Epic-Device-ID | 68009daed09498667a8039cce09983ed |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-BF5B64544412777DD4C71C8545BEAE11-A17C161844A45BEB8831DC891A0EF6C5 |
| Connection | keep-alive |


### Response Body

```json
{
  "profileRevision": 6489,
  "profileId": "monsterpit",
  "profileChangesBaseRevision": 6487,
  "profileChanges": [
    {
      "changeType": "statModified",
      "name": "pit_power",
      "value": 4303905
    },
    {
      "changeType": "statModified",
      "name": "pit_level",
      "value": 136
    },
    {
      "changeType": "statModified",
      "name": "highest_pit_power",
      "value": 4303905
    },
    {
      "changeType": "statModified",
      "name": "pit_power_dirty",
      "value": false
    }
  ],
  "notifications": [
    {
      "type": "WExpMonsterPitLevelUp",
      "primary": true,
      "level": 136,
      "lootResult": {
        "tierGroupName": "MonsterPit:136",
        "items": [
          {
            "itemType": "AccountReward:AccountPerk_ATK_DEF",
            "itemGuid": "ab80755b-5aa4-4145-be57-1821b86ff221",
            "itemProfile": "profile0",
            "quantity": 1
          }
        ]
      }
    }
  ],
  "profileCommandRevision": 1081,
  "serverTime": "2022-12-28T12:09:44.870Z",
  "multiUpdate": [
    {
      "profileRevision": 40212,
      "profileId": "profile0",
      "profileChangesBaseRevision": 40210,
      "profileChanges": [
        {
          "changeType": "itemAdded",
          "itemId": "ab80755b-5aa4-4145-be57-1821b86ff221",
          "item": {
            "templateId": "AccountReward:AccountPerk_ATK_DEF",
            "attributes": {},
            "quantity": 1
          }
        },
        {
          "changeType": "statModified",
          "name": "activity",
          "value": {
            "a": {
              "date": "2022-12-28T00:00:00.000Z",
              "claimed": false,
              "props": {
                "HeroAcquired": 137,
                "HeroPromote": 1,
                "HeroEvolve": 1,
                "MonsterPitLevelUp": 1,
                "HeroFoil": 1,
                "AccountLevelUp": 2,
                "BaseBonus": 10,
                "EnergySpent": 167
              }
            },
            "b": {
              "date": "2022-12-27T00:00:00.000Z",
              "claimed": true,
              "props": {
                "BaseBonus": 10,
                "EnergySpent": 3
              }
            },
            "standardGift": 10
          }
        }
      ],
      "profileCommandRevision": 23952
    }
  ],
  "responseVersion": 1
}
```

*Response body was encoded in base64*

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
