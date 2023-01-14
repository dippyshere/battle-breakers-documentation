# AbandonLevel

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/AbandonLevel?profileId=levels&rvn=29341*

___

## Request

```http request
POST /wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/AbandonLevel?profileId=levels&rvn=29341 HTTP/1.1
```

### Query String

| Name | Value |
|---|---|
| profileId | levels |
| rvn | 29341 |




### Request Headers

| Name | Value |
|---|---|
| Host | wex-public-service-live-prod.ol.epicgames.com |
| Accept-Encoding | deflate, gzip |
| Accept | \*/\* |
| Content-Type | application/json |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":23776},{"profileId":"levels","clientCommandRevision":14332},{"profileId":"friends","clientCommandRevision":8247},{"profileId":"monsterpit","clientCommandRevision":1074},{"profileId":"multiplayer","clientCommandRevision":847}] |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-BF5B64544412777DD4C71C8545BEAE11-12D83104405730A3E780259C81157401 |
| User-Agent | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit |
| Authorization | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |
| Content-Length | 2184 |


### Request Body

```json
{
  "levelItemId": "df1148e4-2116-4cbe-b50c-ef64fdcbd3e5",
  "depthCompleted": 2,
  "levelElement": "Nature",
  "postBattleResults": {
    "defeatedEnemyMap": {
      "Nature": 22
    },
    "uniqueHeroesDefeated": [
      "6ee61d5c-1c59-4a5b-aae4-347a85ed14c0",
      "2dbc336a-554b-449c-ae84-b4697bb00119",
      "73bc3aeb-a61e-4a87-8c47-93190c8cf727",
      "f01dfe95-6a2c-4a18-a3d9-19709c5f7de1",
      "6f578f8e-2a2c-4eb9-81ab-6f2799202822",
      "dab75d65-7911-4f7b-8cc9-88790171650d"
    ],
    "uniqueEnemiesDefeated": [
      "Character:AI_Troll_Nature_T03:RoomDepth=0 Slot=41 SideRoom=0",
      "Character:Ninja_Basic_Nature_Flurry_T03:RoomDepth=0 Slot=40 SideRoom=0",
      "Character:Ninja_Basic_Nature_Flurry_T02:RoomDepth=0 Slot=33 SideRoom=0",
      "Character:Trap_Elemental_Nature:RoomDepth=0 Slot=46 SideRoom=0",
      "Character:Ninja_Basic_Nature_Flurry_T03:RoomDepth=0 Slot=39 SideRoom=0",
      "Character:MartialArtist_UC1_Nature_ChargedFist_T03:RoomDepth=0 Slot=31 SideRoom=0",
      "Character:Ninja_Basic_Nature_Flurry_T03:RoomDepth=0 Slot=37 SideRoom=0",
      "Character:Warrior_Basic_Nature_T02:RoomDepth=0 Slot=45 SideRoom=0",
      "Character:AI_Tower_Nature_AOE_T03:RoomDepth=1 Slot=22 SideRoom=0",
      "Character:AI_Exploder_Nature_T04:RoomDepth=1 Slot=23 SideRoom=0",
      "Character:AI_Troll_Nature_T03:RoomDepth=1 Slot=31 SideRoom=0",
      "Character:AI_Exploder_Nature_T04:RoomDepth=1 Slot=25 SideRoom=0",
      "Character:Trap_Elemental_Nature:RoomDepth=1 Slot=26 SideRoom=0",
      "Character:Trap_Elemental_Nature:RoomDepth=1 Slot=17 SideRoom=0",
      "Character:Ninja_Basic_Nature_Flurry_T03:RoomDepth=1 Slot=31 SideRoom=0",
      "Character:AI_Exploder_Nature_T04:RoomDepth=1 Slot=39 SideRoom=0",
      "Character:Trap_Elemental_Nature:RoomDepth=1 Slot=40 SideRoom=0",
      "Character:Trap_Elemental_Nature:RoomDepth=1 Slot=48 SideRoom=0",
      "Character:Trap_Elemental_Nature:RoomDepth=1 Slot=38 SideRoom=0",
      "Character:Knight_Basic_Nature_GuardianStance_T03:RoomDepth=2 Slot=16 SideRoom=0",
      "Character:Ninja_UC1_Nature_SwiftStrike_T03:RoomDepth=2 Slot=26 SideRoom=0",
      "Character:Trap_Elemental_Nature:RoomDepth=2 Slot=47 SideRoom=0"
    ]
  },
  "dailyQuestZoneType": 3
}
```

___

## Response

#### Status: 200 OK




### Response Headers

| Name | Value |
|---|---|
| Date | Wed, 28 Dec 2022 11:47:24 GMT |
| Content-Type | application/json |
| Content-Length | 640 |
| X-EpicGames-Profile-Revision | 29341 |
| X-EpicGames-McpVersion | prod Release-1.88-1.88 build 107 cl 19310354 |
| X-EpicGames-ContentVersion | 1.88.244-r17036752 |
| X-EpicGames-MinBuild | 17036752 |
| X-Epic-Device-ID | 68009daed09498667a8039cce09983ed |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-BF5B64544412777DD4C71C8545BEAE11-12D83104405730A3E780259C81157401 |
| Connection | keep-alive |


### Response Body

```json
{
  "profileRevision": 29343,
  "profileId": "levels",
  "profileChangesBaseRevision": 29341,
  "profileChanges": [
    {
      "changeType": "statModified",
      "name": "last_forgiven_abandon",
      "value": "2022-12-28T11:47:24.737Z"
    },
    {
      "changeType": "itemRemoved",
      "itemId": "df1148e4-2116-4cbe-b50c-ef64fdcbd3e5"
    }
  ],
  "profileCommandRevision": 14333,
  "serverTime": "2022-12-28T11:47:24.749Z",
  "multiUpdate": [
    {
      "profileRevision": 39926,
      "profileId": "profile0",
      "profileChangesBaseRevision": 39924,
      "profileChanges": [
        {
          "changeType": "itemAttrChanged",
          "itemId": "3f461882-6e02-4d64-9717-b86103385bae",
          "attributeName": "score",
          "attributeValue": 333
        }
      ],
      "profileCommandRevision": 23777
    }
  ],
  "responseVersion": 1
}
```

*Response body was encoded in base64*

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
