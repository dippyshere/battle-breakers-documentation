# BlitzLevel

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/BlitzLevel?profileId=levels&rvn=29657*



___

## Request

```http request
POST /wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/BlitzLevel?profileId=levels&rvn=29657 HTTP/1.1
```

### Query String

| Name | Value |
|---|---|
| profileId | levels |
| rvn | 29657 |




### Request Headers

| Name | Value |
|---|---|
| Host | wex-public-service-live-prod.ol.epicgames.com |
| Accept-Encoding | deflate, gzip |
| Accept | \*/\* |
| Content-Type | application/json |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":24196},{"profileId":"levels","clientCommandRevision":14485},{"profileId":"friends","clientCommandRevision":8264},{"profileId":"monsterpit","clientCommandRevision":1081},{"profileId":"multiplayer","clientCommandRevision":900}] |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-28FED7A740BEC43021AA438EA48E9BDF |
| User-Agent | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit |
| Authorization | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |
| Content-Length | 678 |


### Request Body

```json
{
  "manifestVersion": "1.88.244-r17036752",
  "levelId": "Level.Mine.Map4.D4",
  "partyMembers": [
    {
      "heroType": "LocalCommander",
      "heroItemId": "73bc3aeb-a61e-4a87-8c47-93190c8cf727"
    },
    {
      "heroType": "Empty",
      "heroItemId": ""
    },
    {
      "heroType": "LocalHero",
      "heroItemId": "dab75d65-7911-4f7b-8cc9-88790171650d"
    },
    {
      "heroType": "LocalHero",
      "heroItemId": "2dbc336a-554b-449c-ae84-b4697bb00119"
    },
    {
      "heroType": "LocalHero",
      "heroItemId": "a2daa288-5203-4c3e-b7fc-5602edfbc625"
    },
    {
      "heroType": "LocalHero",
      "heroItemId": "0cb63754-8755-47cd-96ad-c2d8df596735"
    }
  ],
  "friendInstanceId": ""
}
```

___

## Response

#### Status: 200 OK




### Response Headers

| Name | Value |
|---|---|
| Date | Thu, 29 Dec 2022 06:08:18 GMT |
| Content-Type | application/json |
| Content-Length | 1710 |
| X-EpicGames-Profile-Revision | 29657 |
| X-EpicGames-McpVersion | prod Release-1.88-1.88 build 107 cl 19310354 |
| X-EpicGames-ContentVersion | 1.88.244-r17036752 |
| X-EpicGames-MinBuild | 17036752 |
| X-Epic-Device-ID | 68009daed09498667a8039cce09983ed |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-28FED7A740BEC43021AA438EA48E9BDF |
| Connection | keep-alive |


### Response Body

```json
{
  "profileRevision": 29659,
  "profileId": "levels",
  "profileChangesBaseRevision": 29657,
  "profileChanges": [],
  "notifications": [
    {
      "type": "WExpLevelCompleted",
      "primary": false,
      "accountXp": 0,
      "bonusAccountXp": 0,
      "levelId": "Level.Mine.Map4.D4",
      "completed": true,
      "loot": [
        {
          "tierGroupName": "",
          "items": [
            {
              "itemType": "Ore:Ore_Iron",
              "itemGuid": "03e1d076-957e-43f2-9702-71d521413717",
              "itemProfile": "profile0",
              "quantity": 529
            },
            {
              "itemType": "Ore:Ore_Silver",
              "itemGuid": "5dabb8ed-cc42-403e-8904-d1653af4e507",
              "itemProfile": "profile0",
              "quantity": 546
            }
          ]
        },
        {
          "tierGroupName": "Level.Instance",
          "items": [
            {
              "itemType": "Ore:Ore_Iron",
              "itemGuid": "03e1d076-957e-43f2-9702-71d521413717",
              "itemProfile": "profile0",
              "quantity": 7
            }
          ]
        },
        {
          "tierGroupName": "Level.EventsLoot",
          "items": [
            {
              "itemType": "Currency:Gold",
              "itemGuid": "daa87593-4b4a-4ffa-a21d-8979d6eb38ed",
              "itemProfile": "profile0",
              "quantity": 1
            }
          ]
        }
      ]
    }
  ],
  "profileCommandRevision": 14486,
  "serverTime": "2022-12-29T06:08:18.955Z",
  "multiUpdate": [
    {
      "profileRevision": 40518,
      "profileId": "profile0",
      "profileChangesBaseRevision": 40516,
      "profileChanges": [
        {
          "changeType": "itemQuantityChanged",
          "itemId": "daa87593-4b4a-4ffa-a21d-8979d6eb38ed",
          "quantity": 564390467
        },
        {
          "changeType": "itemQuantityChanged",
          "itemId": "03e1d076-957e-43f2-9702-71d521413717",
          "quantity": 3784
        },
        {
          "changeType": "itemQuantityChanged",
          "itemId": "5dabb8ed-cc42-403e-8904-d1653af4e507",
          "quantity": 3507
        },
        {
          "changeType": "itemQuantityChanged",
          "itemId": "3f74512a-2250-4b5c-8e11-a665d99b2bfa",
          "quantity": 32597487
        },
        {
          "changeType": "itemQuantityChanged",
          "itemId": "03e1d076-957e-43f2-9702-71d521413717",
          "quantity": 3791
        },
        {
          "changeType": "itemQuantityChanged",
          "itemId": "daa87593-4b4a-4ffa-a21d-8979d6eb38ed",
          "quantity": 564390468
        }
      ],
      "profileCommandRevision": 24197
    }
  ],
  "responseVersion": 1
}
```

*Response body was encoded in base64*

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
