# Join Matchmaking (Success)

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/:accountId/JoinMatchmaking?profileId=multiplayer&rvn=1*

___

## Request

```http
POST /wex/api/game/v2/profile/:accountId/JoinMatchmaking?profileId=multiplayer&rvn=1 HTTP/1.1
```

### Path Parameters

| Name     | Value                             |
|----------|-----------------------------------|
| acountId | ec0ebb7e56f6454e86c62299a7b32e21  |

### Query String

| Name      | Value       |
|-----------|-------------|
| profileId | multiplayer |
| rvn       | 1           |

### Request Headers

| Name                         | Value                                                                                                                                                                                                                                                              |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Host                         | wex-public-service-live-prod.ol.epicgames.com                                                                                                                                                                                                                      |
| Accept-Encoding              | deflate, gzip                                                                                                                                                                                                                                                      |
| Accept                       | \*/\*                                                                                                                                                                                                                                                              |
| Content-Type                 | application/json                                                                                                                                                                                                                                                   |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":4},{"profileId":"levels","clientCommandRevision":1},{"profileId":"friends","clientCommandRevision":2},{"profileId":"monsterpit","clientCommandRevision":0},{"profileId":"multiplayer","clientCommandRevision":0}] |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-420FE66A4AACA5058BA3B193D82F56CE-AC245A2049FA3CE0DB8F4F8D6987E95C                                                                                                                                                             |
| User-Agent                   | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit                                                                                                                                                                                                   |
| Authorization                | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md)                                                                                                                                              |
| Content-Length               | 4                                                                                                                                                                                                                                                                  |

### Request Body

```json
{}
```

___

## Response

#### Status: 400 Bad Request

### Response Headers

| Name                         | Value                                                                                                  |
|------------------------------|--------------------------------------------------------------------------------------------------------|
| Date                         | Thu, 29 Dec 2022 13:42:33 GMT                                                                          |
| Content-Type                 | application/json                                                                                       |
| Transfer-Encoding            | chunked                                                                                                |
| X-EpicGames-McpVersion       | prod Release-1.88-1.88 build 107 cl 19310354                                                           |
| X-EpicGames-ContentVersion   | 1.88.244-r17036752                                                                                     |
| X-EpicGames-MinBuild         | 17036752                                                                                               |
| X-EpicGames-Profile-Revision | 1                                                                                                      |
| X-Epic-Device-ID             | 68009daed09498667a8039cce09983ed                                                                       |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-A6F351B3452D40656B964A9D6327636F-14CE8CFA409820F074114F907747B2D9 |
| Connection                   | keep-alive                                                                                             |

### Response Body

```json
{
  "multiUpdate": [
    {
      "profileChanges": [
        {
          "changeType": "itemAdded",
          "item": {
            "attributes": {
              "character_ids": [
                "81c2a9b5-28a0-46ff-a3c8-2a8ac67ca02e",
                "64b1754e-d40f-4987-8ea6-7b9e63010836",
                "2e853365-51fb-471e-8f0b-86c94e495b5e",
                "b955dc4a-a78a-4f24-8c18-437bf5c3f7f7",
                "ee6dcdae-31ff-47e6-8cd7-b1ee134ca51d",
                ""
              ],
              "commander_index": 2,
              "date_created": "2022-12-29T13:42:33.030Z",
              "friend_index": 5,
              "party_icon": "None"
            },
            "quantity": 1,
            "templateId": "Party:Instance"
          },
          "itemId": "ffac64be-bf10-4f63-a304-32442b6e7b94"
        },
        {
          "changeType": "itemAdded",
          "item": {
            "attributes": {
              "character_ids": [
                "81c2a9b5-28a0-46ff-a3c8-2a8ac67ca02e",
                "64b1754e-d40f-4987-8ea6-7b9e63010836",
                "2e853365-51fb-471e-8f0b-86c94e495b5e",
                "b955dc4a-a78a-4f24-8c18-437bf5c3f7f7",
                "ee6dcdae-31ff-47e6-8cd7-b1ee134ca51d",
                ""
              ],
              "commander_index": 2,
              "date_created": "2022-12-29T13:42:33.030Z",
              "friend_index": 5,
              "party_icon": "None"
            },
            "quantity": 1,
            "templateId": "Party:Instance"
          },
          "itemId": "a5866ff5-df9d-4dc7-bccf-c07701209ebd"
        },
        {
          "changeType": "statModified",
          "name": "is_pvp_unlocked",
          "value": true
        }
      ],
      "profileChangesBaseRevision": 161,
      "profileCommandRevision": 117,
      "profileId": "profile0",
      "profileRevision": 163
    }
  ],
  "profileChanges": [
    {
      "changeType": "statModified",
      "name": "default_parties",
      "value": {
        "PvpDefense": "ffac64be-bf10-4f63-a304-32442b6e7b94"
      }
    },
    {
      "changeType": "statModified",
      "name": "default_parties",
      "value": {
        "PvpDefense": "ffac64be-bf10-4f63-a304-32442b6e7b94",
        "PvpOffense": "a5866ff5-df9d-4dc7-bccf-c07701209ebd"
      }
    },
    {
      "changeType": "statModified",
      "name": "matchmaking_id",
      "value": "6903003691f949a9bc9e543b37235a11"
    },
    {
      "attributeName": "match_refresh",
      "attributeValue": {
        "credits": 21,
        "interval": "2022-12-29T00:00:00.000Z"
      },
      "changeType": "itemAttrChanged",
      "itemId": "52431032-e69e-473a-8cfc-7218f54aa4ae"
    },
    {
      "attributeName": "match_roster",
      "attributeValue": [
        {
          "heroInfo": [
            {
              "accountInfo": {
                "level": 31,
                "perks": [
                  0,
                  10,
                  10,
                  6,
                  0,
                  3,
                  0,
                  1
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "34dc5b49-bd85-4bf4-ab6e-cab61637876a",
              "level": 35,
              "skillLevel": 3,
              "templateId": "Character:Cleric_VR2_Dark_TerraRifle_T04",
              "upgrades": [
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 31,
                "perks": [
                  0,
                  10,
                  10,
                  6,
                  0,
                  3,
                  0,
                  1
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "71e4886f-e464-49b7-8124-bf95f20c722e",
              "level": 15,
              "skillLevel": 1,
              "templateId": "Character:Knight_UC2_Water_SpearThrust_T03",
              "upgrades": [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 31,
                "perks": [
                  0,
                  10,
                  10,
                  6,
                  0,
                  3,
                  0,
                  1
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "c018e7ad-2fa2-4aec-8a16-008075bf1d3a",
              "level": 30,
              "skillLevel": 2,
              "templateId": "Character:Warrior_R2_Nature_Whirlwind_T03",
              "upgrades": [
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 31,
                "perks": [
                  0,
                  10,
                  10,
                  6,
                  0,
                  3,
                  0,
                  1
                ]
              },
              "bIsCommander": true,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "c408f857-2954-45fb-a615-e283f1b822be",
              "level": 15,
              "skillLevel": 2,
              "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
              "upgrades": [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 31,
                "perks": [
                  0,
                  10,
                  10,
                  6,
                  0,
                  3,
                  0,
                  1
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "44f3120f-661e-4401-a74c-1eb8c5cab6c7",
              "level": 35,
              "skillLevel": 2,
              "templateId": "Character:TreasureHunter_R2_Fire_PowerEfflux_T03",
              "upgrades": [
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "bIsCommander": false,
              "foilLevel": 0,
              "level": 0,
              "skillLevel": 0
            }
          ],
          "mainCommanderIdx": 3,
          "opponent": {
            "avatarUrl": "wex-temp-avatar.png",
            "displayName": "Marlangel31",
            "isRobot": false,
            "matchmakingId": "14fb02b87a6c4d7ba2bc0fa90f103346",
            "rating": 1,
            "taunt": "",
            "type": "Duel"
          }
        },
        {
          "heroInfo": [
            {
              "accountInfo": {
                "level": 48,
                "perks": [
                  0,
                  11,
                  25,
                  10,
                  0,
                  0,
                  2,
                  0
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "10dc2fa8-bc7c-4ca2-be5f-3424c2a53847",
              "level": 50,
              "skillLevel": 2,
              "templateId": "Character:Knight_VR1_Water_ShieldStance_T04",
              "upgrades": [
                10,
                3,
                23,
                25,
                0,
                34,
                1,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 48,
                "perks": [
                  0,
                  11,
                  25,
                  10,
                  0,
                  0,
                  2,
                  0
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "d56e2250-0cae-4fa0-acad-6d4fa1c20585",
              "level": 50,
              "skillLevel": 5,
              "templateId": "Character:HolyKnight_VR2_Light_BASE_T05",
              "upgrades": [
                25,
                25,
                25,
                25,
                0,
                7,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 48,
                "perks": [
                  0,
                  11,
                  25,
                  10,
                  0,
                  0,
                  2,
                  0
                ]
              },
              "bIsCommander": true,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "5165c560-17e0-4794-835e-6f286fd5c73e",
              "level": 50,
              "skillLevel": 5,
              "templateId": "Character:TreasureHunter_VR2_Fire_AntiMaterialCharge_T05",
              "upgrades": [
                25,
                25,
                25,
                14,
                0,
                34,
                1,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 48,
                "perks": [
                  0,
                  11,
                  25,
                  10,
                  0,
                  0,
                  2,
                  0
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "340c893e-e928-4388-a6f3-dda5b9d5c9f0",
              "level": 50,
              "skillLevel": 4,
              "templateId": "Character:Archer_VR2_Nature_GoinCommando_T05",
              "upgrades": [
                25,
                25,
                7,
                3,
                0,
                1,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 48,
                "perks": [
                  0,
                  11,
                  25,
                  10,
                  0,
                  0,
                  2,
                  0
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "41cf03e3-b81e-439e-91a3-6322266f87fb",
              "level": 45,
              "skillLevel": 2,
              "templateId": "Character:Cleric_VR2_Dark_TerraRifle_T04",
              "upgrades": [
                0,
                1,
                4,
                1,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "bIsCommander": false,
              "foilLevel": 0,
              "level": 0,
              "skillLevel": 0
            }
          ],
          "mainCommanderIdx": 2,
          "opponent": {
            "avatarUrl": "wex-temp-avatar.png",
            "displayName": "FABRIZOMBI",
            "isRobot": false,
            "matchmakingId": "199683aac876405991f1cecb891beac5",
            "rating": 29,
            "taunt": "",
            "type": "Duel"
          }
        },
        {
          "heroInfo": [
            {
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  7,
                  11,
                  6,
                  1,
                  1,
                  2,
                  1
                ]
              },
              "bIsCommander": true,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "0c319a63-2fa4-4a17-9a06-c15698ba2ddf",
              "level": 20,
              "skillLevel": 9,
              "templateId": "Character:Warrior_VR2_Dark_Rampage_T04",
              "upgrades": [
                4,
                0,
                2,
                0,
                1,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  7,
                  11,
                  6,
                  1,
                  1,
                  2,
                  1
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "1a70d2b4-0f17-432a-b539-4dc81c3215dc",
              "level": 20,
              "skillLevel": 6,
              "templateId": "Character:Ninja_VR1_Light_CrystalDaggers_T04",
              "upgrades": [
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "bIsCommander": false,
              "foilLevel": 0,
              "level": 0,
              "skillLevel": 0
            },
            {
              "bIsCommander": false,
              "foilLevel": 0,
              "level": 0,
              "skillLevel": 0
            },
            {
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  7,
                  11,
                  6,
                  1,
                  1,
                  2,
                  1
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "5dfb5efe-eb43-4917-b3d0-7ed879b5d886",
              "level": 20,
              "skillLevel": 2,
              "templateId": "Character:Archer_Starter_Water_MultiShot_T03",
              "upgrades": [
                2,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "bIsCommander": false,
              "foilLevel": 0,
              "level": 0,
              "skillLevel": 0
            }
          ],
          "mainCommanderIdx": 0,
          "opponent": {
            "avatarUrl": "wex-temp-avatar.png",
            "displayName": "aaallleeexx3464",
            "isRobot": false,
            "matchmakingId": "39dd6ca928984f818f53819e90737fa1",
            "rating": 0,
            "taunt": "",
            "type": "Duel"
          }
        },
        {
          "heroInfo": [
            {
              "accountInfo": {
                "level": 25,
                "perks": [
                  0,
                  3,
                  12,
                  8,
                  1,
                  2,
                  1,
                  2
                ]
              },
              "bIsCommander": true,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "e60c5af8-55f2-4ddb-893d-95a8c7ecdad2",
              "level": 15,
              "skillLevel": 1,
              "templateId": "Character:HolyKnight_VR2_Light_BASE_T05",
              "upgrades": [
                8,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 25,
                "perks": [
                  0,
                  3,
                  12,
                  8,
                  1,
                  2,
                  1,
                  2
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "58575030-8b95-412f-aa17-97637ef8bd51",
              "level": 30,
              "skillLevel": 2,
              "templateId": "Character:TreasureHunter_VR2_Fire_AntiMaterialCharge_T05",
              "upgrades": [
                24,
                0,
                16,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 25,
                "perks": [
                  0,
                  3,
                  12,
                  8,
                  1,
                  2,
                  1,
                  2
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "16f75840-78db-45f4-a885-15a2eae50aee",
              "level": 30,
              "skillLevel": 2,
              "templateId": "Character:Cleric_VR2_Dark_TerraRifle_T04",
              "upgrades": [
                1,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 25,
                "perks": [
                  0,
                  3,
                  12,
                  8,
                  1,
                  2,
                  1,
                  2
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "61edfce7-272d-4a7f-bab7-eb0ebcc9ca6f",
              "level": 30,
              "skillLevel": 2,
              "templateId": "Character:Archer_VR2_Nature_GoinCommando_T05",
              "upgrades": [
                9,
                0,
                9,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 25,
                "perks": [
                  0,
                  3,
                  12,
                  8,
                  1,
                  2,
                  1,
                  2
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "ccd33a1b-fca9-4840-84c6-710393110f42",
              "level": 30,
              "skillLevel": 2,
              "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
              "upgrades": [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "bIsCommander": false,
              "foilLevel": 0,
              "level": 0,
              "skillLevel": 0
            }
          ],
          "mainCommanderIdx": 0,
          "opponent": {
            "avatarUrl": "wex-temp-avatar.png",
            "displayName": "lesss.",
            "isRobot": false,
            "matchmakingId": "44bc33480c3c445e872dba14e6e44035",
            "rating": 10,
            "taunt": "",
            "type": "Duel"
          }
        },
        {
          "heroInfo": [
            {
              "accountInfo": {
                "level": 14,
                "perks": [
                  0,
                  4,
                  3,
                  4,
                  1,
                  5,
                  0,
                  2
                ]
              },
              "bIsCommander": true,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "05c73d98-e38f-4a97-a91e-eb74cabfbed9",
              "level": 15,
              "skillLevel": 1,
              "templateId": "Character:Ninja_R2_Dark_TripleStab_T03",
              "upgrades": [
                5,
                15,
                11,
                15,
                2,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 14,
                "perks": [
                  0,
                  4,
                  3,
                  4,
                  1,
                  5,
                  0,
                  2
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "81f13540-6c22-49b2-918f-5fc9153bff9a",
              "level": 15,
              "skillLevel": 1,
              "templateId": "Character:Ninja_VR1_Light_CrystalDaggers_T04",
              "upgrades": [
                0,
                8,
                6,
                9,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 14,
                "perks": [
                  0,
                  4,
                  3,
                  4,
                  1,
                  5,
                  0,
                  2
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "dfb73a67-5a82-489c-ae67-1409bf3878bf",
              "level": 15,
              "skillLevel": 1,
              "templateId": "Character:Knight_UC2_Dark_SpearThrust_T04",
              "upgrades": [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 14,
                "perks": [
                  0,
                  4,
                  3,
                  4,
                  1,
                  5,
                  0,
                  2
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "a5481eab-83c1-4e08-8d87-dbbad3af5166",
              "level": 15,
              "skillLevel": 1,
              "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
              "upgrades": [
                10,
                0,
                7,
                1,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 14,
                "perks": [
                  0,
                  4,
                  3,
                  4,
                  1,
                  5,
                  0,
                  2
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "48012d41-ff89-4213-be22-f64cae66c9f7",
              "level": 15,
              "skillLevel": 1,
              "templateId": "Character:Ninja_UC1_Water_SwiftStrike_T03",
              "upgrades": [
                0,
                0,
                1,
                1,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "bIsCommander": false,
              "foilLevel": 0,
              "level": 0,
              "skillLevel": 0
            }
          ],
          "mainCommanderIdx": 0,
          "opponent": {
            "avatarUrl": "wex-temp-avatar.png",
            "displayName": "t\u0326heorganicgummy",
            "isRobot": false,
            "matchmakingId": "4e92da100ab249a69f07522834be66ff",
            "rating": 1,
            "taunt": "",
            "type": "Duel"
          }
        },
        {
          "heroInfo": [
            {
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  3,
                  12,
                  4,
                  0,
                  0,
                  0,
                  2
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "fb7a33a8-3f56-4aed-b2db-c9e5eb1f4121",
              "level": 10,
              "skillLevel": 1,
              "templateId": "Character:Ninja_R2_Dark_TripleStab_T03",
              "upgrades": [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  3,
                  12,
                  4,
                  0,
                  0,
                  0,
                  2
                ]
              },
              "bIsCommander": true,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "a8731975-4a58-46ed-9953-102a4b6aa37a",
              "level": 15,
              "skillLevel": 2,
              "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
              "upgrades": [
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  3,
                  12,
                  4,
                  0,
                  0,
                  0,
                  2
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "b5b2df3f-10bc-44c2-beea-8ebb3d061426",
              "level": 10,
              "skillLevel": 1,
              "templateId": "Character:Mage_Starter_Fire_BurningSwordCombo_T03",
              "upgrades": [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  3,
                  12,
                  4,
                  0,
                  0,
                  0,
                  2
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "221d70d5-6fee-4962-a5fd-a94a07b967c5",
              "level": 10,
              "skillLevel": 1,
              "templateId": "Character:Archer_UC1_Fire_ElementalBreath_T03",
              "upgrades": [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  3,
                  12,
                  4,
                  0,
                  0,
                  0,
                  2
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "e02083ea-8689-46cf-bf87-1ab2480505f3",
              "level": 15,
              "skillLevel": 1,
              "templateId": "Character:Archer_VR2_Nature_GoinCommando_T05",
              "upgrades": [
                0,
                1,
                2,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "bIsCommander": false,
              "foilLevel": 0,
              "level": 0,
              "skillLevel": 0
            }
          ],
          "mainCommanderIdx": 1,
          "opponent": {
            "avatarUrl": "wex-temp-avatar.png",
            "displayName": "Kostya yshe sany",
            "isRobot": false,
            "matchmakingId": "50de10eaab3744e8bcb64707d548a458",
            "rating": 0,
            "taunt": "",
            "type": "Duel"
          }
        },
        {
          "heroInfo": [
            {
              "accountInfo": {
                "level": 13,
                "perks": [
                  0,
                  6,
                  2,
                  1,
                  0,
                  3,
                  0,
                  0
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "ad7cf401-d293-4b8c-ac7a-b29301a2d25c",
              "level": 10,
              "skillLevel": 1,
              "templateId": "Character:Warrior_R2_Nature_Whirlwind_T03",
              "upgrades": [
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 13,
                "perks": [
                  0,
                  6,
                  2,
                  1,
                  0,
                  3,
                  0,
                  0
                ]
              },
              "bIsCommander": true,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "202d028f-7e78-4a8e-b5de-6045fd8cce57",
              "level": 10,
              "skillLevel": 1,
              "templateId": "Character:TreasureHunter_R2_Nature_PowerEfflux_T03",
              "upgrades": [
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 13,
                "perks": [
                  0,
                  6,
                  2,
                  1,
                  0,
                  3,
                  0,
                  0
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "faed8935-2c87-4bc5-9966-f94f2e71cea3",
              "level": 10,
              "skillLevel": 1,
              "templateId": "Character:Warrior_Starter_Nature_PowerStrike_T03",
              "upgrades": [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 13,
                "perks": [
                  0,
                  6,
                  2,
                  1,
                  0,
                  3,
                  0,
                  0
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "05d9a895-74b8-4dfd-95da-e475eb055524",
              "level": 10,
              "skillLevel": 1,
              "templateId": "Character:Mage_UC1_Fire_ElementalBlast_T03",
              "upgrades": [
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 13,
                "perks": [
                  0,
                  6,
                  2,
                  1,
                  0,
                  3,
                  0,
                  0
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "0d7a294f-f189-41d7-9535-2e6bf5bddf21",
              "level": 10,
              "skillLevel": 1,
              "templateId": "Character:Mage_Starter_Fire_BurningSwordCombo_T03",
              "upgrades": [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "bIsCommander": false,
              "foilLevel": 0,
              "level": 0,
              "skillLevel": 0
            }
          ],
          "mainCommanderIdx": 1,
          "opponent": {
            "avatarUrl": "wex-temp-avatar.png",
            "displayName": "\u0428\u0418\u041f\u0427\u0418\u041a1",
            "isRobot": false,
            "matchmakingId": "5212a7e047714577baa9b2fc44474106",
            "rating": 0,
            "taunt": "",
            "type": "Duel"
          }
        },
        {
          "heroInfo": [
            {
              "accountInfo": {
                "level": 53,
                "perks": [
                  0,
                  16,
                  16,
                  17,
                  1,
                  3,
                  3,
                  1
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "49197c9f-8f0e-4d59-9438-41eb08046120",
              "level": 61,
              "skillLevel": 4,
              "templateId": "Character:HolyKnight_VR2_Light_BASE_T05",
              "upgrades": [
                17,
                10,
                29,
                0,
                1,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 53,
                "perks": [
                  0,
                  16,
                  16,
                  17,
                  1,
                  3,
                  3,
                  1
                ]
              },
              "bIsCommander": true,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "49d4165c-ef2b-429b-828c-ec713dae6de0",
              "level": 67,
              "skillLevel": 4,
              "templateId": "Character:TreasureHunter_VR2_Fire_AntiMaterialCharge_T05",
              "upgrades": [
                27,
                0,
                24,
                0,
                7,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 53,
                "perks": [
                  0,
                  16,
                  16,
                  17,
                  1,
                  3,
                  3,
                  1
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "df7f6294-61ac-4d5b-aded-755cb13d7e6e",
              "level": 58,
              "skillLevel": 4,
              "templateId": "Character:Cleric_VR2_Dark_TerraRifle_T04",
              "upgrades": [
                12,
                0,
                6,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 53,
                "perks": [
                  0,
                  16,
                  16,
                  17,
                  1,
                  3,
                  3,
                  1
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "5d394fa0-120d-4111-a6ad-f1c2b09c4ad9",
              "level": 61,
              "skillLevel": 5,
              "templateId": "Character:Archer_VR2_Nature_GoinCommando_T05",
              "upgrades": [
                0,
                0,
                3,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 53,
                "perks": [
                  0,
                  16,
                  16,
                  17,
                  1,
                  3,
                  3,
                  1
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "e5710460-a82c-4780-be72-373b2fef45f2",
              "level": 45,
              "skillLevel": 2,
              "templateId": "Character:Mage_VR1_Nature_Shatter_T04",
              "upgrades": [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "bIsCommander": false,
              "foilLevel": 0,
              "level": 0,
              "skillLevel": 0
            }
          ],
          "mainCommanderIdx": 1,
          "opponent": {
            "avatarUrl": "wex-temp-avatar.png",
            "displayName": "Sykes00",
            "isRobot": false,
            "matchmakingId": "573d5297cc884bdf95f91ff25eba7acd",
            "rating": 1,
            "taunt": "",
            "type": "Duel"
          }
        },
        {
          "heroInfo": [
            {
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  5,
                  8,
                  5,
                  0,
                  0,
                  1,
                  0
                ]
              },
              "bIsCommander": true,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "2c67fdf7-7109-4929-9b64-44e1a912cb3d",
              "level": 20,
              "skillLevel": 2,
              "templateId": "Character:HolyKnight_VR2_Light_BASE_T05",
              "upgrades": [
                11,
                0,
                6,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  5,
                  8,
                  5,
                  0,
                  0,
                  1,
                  0
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "cfcc68ac-f056-4fe3-8e36-44f44d947c21",
              "level": 20,
              "skillLevel": 2,
              "templateId": "Character:Archer_VR2_Nature_GoinCommando_T05",
              "upgrades": [
                1,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  5,
                  8,
                  5,
                  0,
                  0,
                  1,
                  0
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "17ac9586-585d-4ec5-a6b0-0ede2a6e0c58",
              "level": 20,
              "skillLevel": 2,
              "templateId": "Character:TreasureHunter_R2_Fire_PowerEfflux_T03",
              "upgrades": [
                1,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  5,
                  8,
                  5,
                  0,
                  0,
                  1,
                  0
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "964f5149-648a-4fd8-8c46-b58b356e7a19",
              "level": 15,
              "skillLevel": 1,
              "templateId": "Character:Mage_Starter_Fire_BurningSwordCombo_T03",
              "upgrades": [
                1,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  5,
                  8,
                  5,
                  0,
                  0,
                  1,
                  0
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "17a5fd0c-5248-446f-bdcd-0ca178179ce5",
              "level": 20,
              "skillLevel": 2,
              "templateId": "Character:TreasureHunter_VR2_Fire_AntiMaterialCharge_T05",
              "upgrades": [
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "bIsCommander": false,
              "foilLevel": 0,
              "level": 0,
              "skillLevel": 0
            }
          ],
          "mainCommanderIdx": 0,
          "opponent": {
            "avatarUrl": "wex-temp-avatar.png",
            "displayName": "twistedtouch",
            "isRobot": false,
            "matchmakingId": "57c3344696fa42e0a2a5ff8695163454",
            "rating": 1,
            "taunt": "",
            "type": "Duel"
          }
        },
        {
          "heroInfo": [
            {
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  4,
                  4,
                  8,
                  0,
                  2,
                  0,
                  1
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "36f66601-e9c4-4dfa-9333-e1959589451a",
              "level": 1,
              "skillLevel": 1,
              "templateId": "Character:Warmage_R1_Fire_FuelTheFire_T03",
              "upgrades": [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  4,
                  4,
                  8,
                  0,
                  2,
                  0,
                  1
                ]
              },
              "bIsCommander": true,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "6e0245ae-b388-4b57-b3bd-100f2da89bef",
              "level": 20,
              "skillLevel": 2,
              "templateId": "Character:TreasureHunter_R2_Fire_PowerEfflux_T03",
              "upgrades": [
                2,
                0,
                1,
                0,
                0,
                6,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  4,
                  4,
                  8,
                  0,
                  2,
                  0,
                  1
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "e2150d2a-5dc9-4a9d-a82b-d5d7db6ced44",
              "level": 20,
              "skillLevel": 2,
              "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
              "upgrades": [
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  4,
                  4,
                  8,
                  0,
                  2,
                  0,
                  1
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "b17b8b64-a9cb-4561-9141-b277e1dca6ab",
              "level": 20,
              "skillLevel": 2,
              "templateId": "Character:Mage_Starter_Fire_BurningSwordCombo_T03",
              "upgrades": [
                3,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  4,
                  4,
                  8,
                  0,
                  2,
                  0,
                  1
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "96d462f3-6dfb-41bf-8512-868bcb0b0ddf",
              "level": 20,
              "skillLevel": 2,
              "templateId": "Character:Ninja_UC1_Water_SwiftStrike_T03",
              "upgrades": [
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "bIsCommander": false,
              "foilLevel": 0,
              "level": 0,
              "skillLevel": 0
            }
          ],
          "mainCommanderIdx": 1,
          "opponent": {
            "avatarUrl": "wex-temp-avatar.png",
            "displayName": "Stefanpr09",
            "isRobot": false,
            "matchmakingId": "5a19a73b1bc1473eb9e4c99b95c63f84",
            "rating": 0,
            "taunt": "",
            "type": "Duel"
          }
        },
        {
          "heroInfo": [
            {
              "accountInfo": {
                "level": 10,
                "perks": [
                  0,
                  6,
                  2,
                  1,
                  0,
                  1,
                  0,
                  1
                ]
              },
              "bIsCommander": true,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "99897202-8ca2-40a7-8c04-eb0e443d6e10",
              "level": 15,
              "skillLevel": 1,
              "templateId": "Character:Warrior_Starter_Fire_Berserking_T03",
              "upgrades": [
                1,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 10,
                "perks": [
                  0,
                  6,
                  2,
                  1,
                  0,
                  1,
                  0,
                  1
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "1cba5776-6fb8-49b8-9cda-43cf8090fa5f",
              "level": 1,
              "skillLevel": 1,
              "templateId": "Character:Mage_Starter_Fire_BurningSwordCombo_T03",
              "upgrades": [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 10,
                "perks": [
                  0,
                  6,
                  2,
                  1,
                  0,
                  1,
                  0,
                  1
                ]
              },
              "bIsCommander": false,
              "foilLevel": 1,
              "gearTemplateId": "",
              "itemId": "97db8be1-4175-4daf-b617-e3602f16f2e1",
              "level": 10,
              "skillLevel": 1,
              "templateId": "Character:Assassin_R2_Nature_Slasher_T03",
              "upgrades": [
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 10,
                "perks": [
                  0,
                  6,
                  2,
                  1,
                  0,
                  1,
                  0,
                  1
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "a0a5b562-7ef2-4fdb-849f-fe50c6f06480",
              "level": 10,
              "skillLevel": 1,
              "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
              "upgrades": [
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 10,
                "perks": [
                  0,
                  6,
                  2,
                  1,
                  0,
                  1,
                  0,
                  1
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "2545d5a8-6257-487f-af3d-6f5291e46d1a",
              "level": 10,
              "skillLevel": 1,
              "templateId": "Character:Ninja_R2_Dark_TripleStab_T03",
              "upgrades": [
                1,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "bIsCommander": false,
              "foilLevel": 0,
              "level": 0,
              "skillLevel": 0
            }
          ],
          "mainCommanderIdx": 0,
          "opponent": {
            "avatarUrl": "wex-temp-avatar.png",
            "displayName": "Galaxygaymg",
            "isRobot": false,
            "matchmakingId": "613e7d34a15b4953a38e6104058d1c92",
            "rating": 0,
            "taunt": "",
            "type": "Duel"
          }
        },
        {
          "heroInfo": [
            {
              "accountInfo": {
                "level": 933,
                "perks": [
                  6,
                  102,
                  605,
                  250,
                  5,
                  2,
                  0,
                  52
                ]
              },
              "bIsCommander": true,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "0e0998ea-018b-4618-9bfd-463d691ebbfd",
              "level": 150,
              "skillLevel": 20,
              "templateId": "Character:Shadowknight_SR1_Dark_Obliterate_T06",
              "upgrades": [
                95,
                95,
                95,
                95,
                34,
                125,
                5,
                125,
                5
              ]
            },
            {
              "accountInfo": {
                "level": 933,
                "perks": [
                  6,
                  102,
                  605,
                  250,
                  5,
                  2,
                  0,
                  52
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "Character:Knight_VR2_Nature_ElementalTouch_T04",
              "itemId": "8b0b3d88-26ca-4aa7-ac65-db9ec4cef947",
              "level": 150,
              "skillLevel": 20,
              "templateId": "Character:Knight_SR1_Nature_PerfectShield_T06",
              "upgrades": [
                95,
                95,
                95,
                95,
                34,
                150,
                6,
                125,
                5
              ]
            },
            {
              "accountInfo": {
                "level": 933,
                "perks": [
                  6,
                  102,
                  605,
                  250,
                  5,
                  2,
                  0,
                  52
                ]
              },
              "bIsCommander": false,
              "foilLevel": 1,
              "gearTemplateId": "Character:Archer_VR1_Nature_ChargedShot_T04",
              "itemId": "79287b5b-52f6-42c3-9363-4d0667f8fb28",
              "level": 150,
              "skillLevel": 20,
              "templateId": "Character:Archer_SR1_Nature_FlurryOfArrows_T06",
              "upgrades": [
                95,
                95,
                95,
                95,
                34,
                150,
                6,
                125,
                5
              ]
            },
            {
              "bIsCommander": false,
              "foilLevel": 0,
              "level": 0,
              "skillLevel": 0
            },
            {
              "accountInfo": {
                "level": 933,
                "perks": [
                  6,
                  102,
                  605,
                  250,
                  5,
                  2,
                  0,
                  52
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "36fbd51e-91b0-4963-b1ae-d226b0fc21f8",
              "level": 150,
              "skillLevel": 20,
              "templateId": "Character:Cleric_SR2_Nature_MysticBlessing_T06",
              "upgrades": [
                95,
                95,
                95,
                95,
                34,
                125,
                5,
                125,
                5
              ]
            },
            {
              "bIsCommander": false,
              "foilLevel": 0,
              "level": 0,
              "skillLevel": 0
            }
          ],
          "mainCommanderIdx": 0,
          "opponent": {
            "avatarUrl": "wex-temp-avatar.png",
            "displayName": "miffyUnk",
            "isRobot": false,
            "matchmakingId": "6fcf88c206ff407c8be2914e13a289d5",
            "rating": 153,
            "taunt": "",
            "type": "Duel"
          }
        },
        {
          "heroInfo": [
            {
              "accountInfo": {
                "level": 113,
                "perks": [
                  0,
                  35,
                  39,
                  33,
                  2,
                  10,
                  2,
                  5
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "8dc3223f-87ee-439e-bf8c-f82d7d290613",
              "level": 132,
              "skillLevel": 19,
              "templateId": "Character:Shadowknight_SR2_Dark_Devour_T06",
              "upgrades": [
                88,
                88,
                88,
                88,
                16,
                49,
                1,
                21,
                1
              ]
            },
            {
              "accountInfo": {
                "level": 113,
                "perks": [
                  0,
                  35,
                  39,
                  33,
                  2,
                  10,
                  2,
                  5
                ]
              },
              "bIsCommander": true,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "c261aaf6-65d3-41b5-9211-3a9335937a98",
              "level": 132,
              "skillLevel": 20,
              "templateId": "Character:Ninja_VR1_Light_CrystalDaggers_T05",
              "upgrades": [
                95,
                95,
                95,
                95,
                19,
                24,
                1,
                14,
                2
              ]
            },
            {
              "accountInfo": {
                "level": 113,
                "perks": [
                  0,
                  35,
                  39,
                  33,
                  2,
                  10,
                  2,
                  5
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "3c507ebc-be5c-4da2-8541-a8aee768a871",
              "level": 132,
              "skillLevel": 20,
              "templateId": "Character:Assassin_VR2_Nature_Backstab_T06",
              "upgrades": [
                95,
                95,
                95,
                95,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 113,
                "perks": [
                  0,
                  35,
                  39,
                  33,
                  2,
                  10,
                  2,
                  5
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "fe0aac98-f179-424e-9011-fb8502b17d50",
              "level": 132,
              "skillLevel": 20,
              "templateId": "Character:Warrior_R2_Nature_Whirlwind_T05",
              "upgrades": [
                76,
                74,
                92,
                95,
                9,
                11,
                1,
                15,
                1
              ]
            },
            {
              "accountInfo": {
                "level": 113,
                "perks": [
                  0,
                  35,
                  39,
                  33,
                  2,
                  10,
                  2,
                  5
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "4415ef47-2e58-4c96-8698-ddec38fac7c8",
              "level": 121,
              "skillLevel": 11,
              "templateId": "Character:Mage_Starter_Fire_Fireball_T05",
              "upgrades": [
                95,
                77,
                95,
                74,
                5,
                24,
                1,
                10,
                1
              ]
            },
            {
              "bIsCommander": false,
              "foilLevel": 0,
              "level": 0,
              "skillLevel": 0
            }
          ],
          "mainCommanderIdx": 1,
          "opponent": {
            "avatarUrl": "wex-temp-avatar.png",
            "displayName": "bbryan010",
            "isRobot": false,
            "matchmakingId": "8053ca676bb9415fb3ea445073dc3554",
            "rating": 0,
            "taunt": "",
            "type": "Duel"
          }
        },
        {
          "heroInfo": [
            {
              "accountInfo": {
                "level": 11,
                "perks": [
                  0,
                  5,
                  2,
                  2,
                  0,
                  1,
                  0,
                  0
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "f50c8574-1272-4bc6-9a49-0fe5a6e02a9e",
              "level": 1,
              "skillLevel": 1,
              "templateId": "Character:Mage_Basic_Fire_EnergyBlast_T02",
              "upgrades": [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 11,
                "perks": [
                  0,
                  5,
                  2,
                  2,
                  0,
                  1,
                  0,
                  0
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "d00f8367-e1bc-4912-bdd0-173cb54e91d3",
              "level": 3,
              "skillLevel": 1,
              "templateId": "Character:Ninja_R2_Dark_TripleStab_T03",
              "upgrades": [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 11,
                "perks": [
                  0,
                  5,
                  2,
                  2,
                  0,
                  1,
                  0,
                  0
                ]
              },
              "bIsCommander": true,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "e1e127e7-e305-4234-a6e9-8567bdba19cb",
              "level": 15,
              "skillLevel": 1,
              "templateId": "Character:Cleric_VR2_Dark_TerraRifle_T04",
              "upgrades": [
                2,
                1,
                2,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 11,
                "perks": [
                  0,
                  5,
                  2,
                  2,
                  0,
                  1,
                  0,
                  0
                ]
              },
              "bIsCommander": false,
              "foilLevel": 1,
              "gearTemplateId": "",
              "itemId": "534bf893-8692-4b57-9a49-17ef10e5039c",
              "level": 13,
              "skillLevel": 1,
              "templateId": "Character:Mage_UC1_Fire_ElementalBlast_T03",
              "upgrades": [
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 11,
                "perks": [
                  0,
                  5,
                  2,
                  2,
                  0,
                  1,
                  0,
                  0
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "3ba29482-bbc8-4882-9482-6823c8a22e07",
              "level": 10,
              "skillLevel": 1,
              "templateId": "Character:Mage_Starter_Fire_BurningSwordCombo_T03",
              "upgrades": [
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "bIsCommander": false,
              "foilLevel": 0,
              "level": 0,
              "skillLevel": 0
            }
          ],
          "mainCommanderIdx": 2,
          "opponent": {
            "avatarUrl": "wex-temp-avatar.png",
            "displayName": "fabiancitoTNT",
            "isRobot": false,
            "matchmakingId": "8a193619c8134e5f8b5d457f520a0680",
            "rating": 0,
            "taunt": "",
            "type": "Duel"
          }
        },
        {
          "heroInfo": [
            {
              "accountInfo": {
                "level": 11,
                "perks": [
                  0,
                  4,
                  4,
                  1,
                  0,
                  1,
                  0,
                  0
                ]
              },
              "bIsCommander": true,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "9a9bf1cb-3af3-4c5b-bd16-ecb4881895f7",
              "level": 10,
              "skillLevel": 1,
              "templateId": "Character:Warrior_R2_Nature_Whirlwind_T03",
              "upgrades": [
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 11,
                "perks": [
                  0,
                  4,
                  4,
                  1,
                  0,
                  1,
                  0,
                  0
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "aa2cccde-56a4-49b0-9c4c-9b1104227e1f",
              "level": 15,
              "skillLevel": 1,
              "templateId": "Character:TreasureHunter_R2_Fire_PowerEfflux_T03",
              "upgrades": [
                14,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 11,
                "perks": [
                  0,
                  4,
                  4,
                  1,
                  0,
                  1,
                  0,
                  0
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "ece4e602-293e-44dc-9d2e-497133718532",
              "level": 10,
              "skillLevel": 1,
              "templateId": "Character:Archer_UC1_Fire_ElementalBreath_T03",
              "upgrades": [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 11,
                "perks": [
                  0,
                  4,
                  4,
                  1,
                  0,
                  1,
                  0,
                  0
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "fcb0f7ea-9c18-45b2-a40a-a0c2f3dd029e",
              "level": 15,
              "skillLevel": 1,
              "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
              "upgrades": [
                5,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 11,
                "perks": [
                  0,
                  4,
                  4,
                  1,
                  0,
                  1,
                  0,
                  0
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "29c2dc91-1c14-4f93-9511-e8d7337baa62",
              "level": 15,
              "skillLevel": 1,
              "templateId": "Character:Mage_Starter_Fire_BurningSwordCombo_T03",
              "upgrades": [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "bIsCommander": false,
              "foilLevel": 0,
              "level": 0,
              "skillLevel": 0
            }
          ],
          "mainCommanderIdx": 0,
          "opponent": {
            "avatarUrl": "wex-temp-avatar.png",
            "displayName": "anyucik",
            "isRobot": false,
            "matchmakingId": "9a56fb498b404f1599690a6033a67f27",
            "rating": 0,
            "taunt": "",
            "type": "Duel"
          }
        },
        {
          "heroInfo": [
            {
              "accountInfo": {
                "level": 56,
                "perks": [
                  0,
                  14,
                  15,
                  15,
                  0,
                  9,
                  1,
                  1
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "f4b63fb0-e19c-4b3c-bda0-b8210a88dd4f",
              "level": 60,
              "skillLevel": 3,
              "templateId": "Character:Warrior_SR2_Fire_Lacerate_T05",
              "upgrades": [
                0,
                0,
                10,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 56,
                "perks": [
                  0,
                  14,
                  15,
                  15,
                  0,
                  9,
                  1,
                  1
                ]
              },
              "bIsCommander": true,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "5e3f6347-9395-4c44-a6cd-85a79d831f0d",
              "level": 66,
              "skillLevel": 4,
              "templateId": "Character:Archer_VR2_Nature_GoinCommando_T05",
              "upgrades": [
                12,
                0,
                0,
                3,
                1,
                20,
                0,
                20,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 56,
                "perks": [
                  0,
                  14,
                  15,
                  15,
                  0,
                  9,
                  1,
                  1
                ]
              },
              "bIsCommander": false,
              "foilLevel": 1,
              "gearTemplateId": "",
              "itemId": "dc134cdd-03ba-4cf7-b558-21d79a9fa2d6",
              "level": 66,
              "skillLevel": 12,
              "templateId": "Character:Ninja_VR1_Light_CrystalDaggers_T04",
              "upgrades": [
                25,
                0,
                0,
                0,
                0,
                15,
                0,
                15,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 56,
                "perks": [
                  0,
                  14,
                  15,
                  15,
                  0,
                  9,
                  1,
                  1
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "90a0033b-31aa-407b-98e3-1f495c8d22ff",
              "level": 60,
              "skillLevel": 2,
              "templateId": "Character:Shadowknight_UC2_Fire_Ghoul_T03",
              "upgrades": [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 56,
                "perks": [
                  0,
                  14,
                  15,
                  15,
                  0,
                  9,
                  1,
                  1
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "9473705a-5ad7-422f-b436-b21729e4bc8e",
              "level": 60,
              "skillLevel": 1,
              "templateId": "Character:HolyKnight_VR2_Light_BASE_T05",
              "upgrades": [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "bIsCommander": false,
              "foilLevel": 0,
              "level": 0,
              "skillLevel": 0
            }
          ],
          "mainCommanderIdx": 1,
          "opponent": {
            "avatarUrl": "wex-temp-avatar.png",
            "displayName": "Markeve2019",
            "isRobot": false,
            "matchmakingId": "a277bd19718d45368254f90844725c2b",
            "rating": 0,
            "taunt": "",
            "type": "Duel"
          }
        },
        {
          "heroInfo": [
            {
              "accountInfo": {
                "level": 124,
                "perks": [
                  2,
                  40,
                  39,
                  38,
                  3,
                  24,
                  4,
                  5
                ]
              },
              "bIsCommander": true,
              "foilLevel": 1,
              "gearTemplateId": "",
              "itemId": "ac8b2fc9-9007-4a83-87d7-f0ba52366f88",
              "level": 110,
              "skillLevel": 6,
              "templateId": "Character:Cleric_R1_Water_RejuvenatingBreeze_T05",
              "upgrades": [
                13,
                0,
                39,
                0,
                10,
                85,
                3,
                10,
                1
              ]
            },
            {
              "accountInfo": {
                "level": 124,
                "perks": [
                  2,
                  40,
                  39,
                  38,
                  3,
                  24,
                  4,
                  5
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "d4720bb6-1c7a-4111-9653-ef019ccdc9ef",
              "level": 110,
              "skillLevel": 5,
              "templateId": "Character:Cleric_VR2_Dark_TerraRifle_T05",
              "upgrades": [
                20,
                11,
                31,
                5,
                10,
                85,
                3,
                25,
                1
              ]
            },
            {
              "accountInfo": {
                "level": 124,
                "perks": [
                  2,
                  40,
                  39,
                  38,
                  3,
                  24,
                  4,
                  5
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "ceeb250c-1351-4d19-a673-837727bf94dc",
              "level": 110,
              "skillLevel": 6,
              "templateId": "Character:Ninja_VR1_Light_CrystalDaggers_T05",
              "upgrades": [
                39,
                39,
                39,
                22,
                10,
                75,
                3,
                5,
                1
              ]
            },
            {
              "accountInfo": {
                "level": 124,
                "perks": [
                  2,
                  40,
                  39,
                  38,
                  3,
                  24,
                  4,
                  5
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "c7ff00a0-24bd-4f0d-8a4f-e130b8902bbb",
              "level": 110,
              "skillLevel": 4,
              "templateId": "Character:Archer_VR1_Light_LightningArrows_T05",
              "upgrades": [
                0,
                0,
                0,
                0,
                0,
                5,
                0,
                5,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 124,
                "perks": [
                  2,
                  40,
                  39,
                  38,
                  3,
                  24,
                  4,
                  5
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "ca05a653-51bc-47ac-b94b-722bd771d18c",
              "level": 110,
              "skillLevel": 5,
              "templateId": "Character:Assassin_VR1_Fire_HiddenStrike_T05",
              "upgrades": [
                19,
                5,
                39,
                0,
                10,
                65,
                2,
                5,
                0
              ]
            },
            {
              "bIsCommander": false,
              "foilLevel": 0,
              "level": 0,
              "skillLevel": 0
            }
          ],
          "mainCommanderIdx": 0,
          "opponent": {
            "avatarUrl": "wex-temp-avatar.png",
            "displayName": "Creeps547",
            "isRobot": false,
            "matchmakingId": "a6a840af6f114a2fbae88c34e3419d2e",
            "rating": 8,
            "taunt": "",
            "type": "Duel"
          }
        },
        {
          "heroInfo": [
            {
              "accountInfo": {
                "level": 36,
                "perks": [
                  0,
                  10,
                  17,
                  14,
                  2,
                  2,
                  3,
                  0
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "43e1ee1e-64a8-45fd-835f-f3c7b49dbee5",
              "level": 40,
              "skillLevel": 3,
              "templateId": "Character:Warrior_R2_Nature_Whirlwind_T04",
              "upgrades": [
                25,
                6,
                19,
                13,
                2,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 36,
                "perks": [
                  0,
                  10,
                  17,
                  14,
                  2,
                  2,
                  3,
                  0
                ]
              },
              "bIsCommander": true,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "36229e18-67a3-4b96-9565-bb49304282b4",
              "level": 40,
              "skillLevel": 7,
              "templateId": "Character:HolyKnight_SR1_Light_HolyLance_T05",
              "upgrades": [
                25,
                12,
                8,
                1,
                0,
                15,
                1,
                15,
                1
              ]
            },
            {
              "accountInfo": {
                "level": 36,
                "perks": [
                  0,
                  10,
                  17,
                  14,
                  2,
                  2,
                  3,
                  0
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "7a523222-41cd-458a-b8d9-2e63e65348c1",
              "level": 40,
              "skillLevel": 3,
              "templateId": "Character:Knight_VR1_Water_ShieldStance_T04",
              "upgrades": [
                0,
                4,
                0,
                6,
                0,
                15,
                0,
                15,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 36,
                "perks": [
                  0,
                  10,
                  17,
                  14,
                  2,
                  2,
                  3,
                  0
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "18c4d5b7-35b1-4364-aa60-31f51d05fd86",
              "level": 40,
              "skillLevel": 3,
              "templateId": "Character:Warrior_VR2_Dark_Rampage_T04",
              "upgrades": [
                2,
                9,
                2,
                4,
                0,
                15,
                0,
                12,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 36,
                "perks": [
                  0,
                  10,
                  17,
                  14,
                  2,
                  2,
                  3,
                  0
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "284e0791-d43e-4307-aa47-13c174a13b82",
              "level": 40,
              "skillLevel": 4,
              "templateId": "Character:Ninja_VR1_Light_CrystalDaggers_T04",
              "upgrades": [
                3,
                6,
                3,
                4,
                0,
                9,
                0,
                3,
                0
              ]
            },
            {
              "bIsCommander": false,
              "foilLevel": 0,
              "level": 0,
              "skillLevel": 0
            }
          ],
          "mainCommanderIdx": 1,
          "opponent": {
            "avatarUrl": "wex-temp-avatar.png",
            "displayName": "jojolete01",
            "isRobot": false,
            "matchmakingId": "ac48a1264d3e45da82bda46253655585",
            "rating": 0,
            "taunt": "",
            "type": "Duel"
          }
        },
        {
          "heroInfo": [
            {
              "accountInfo": {
                "level": 50,
                "perks": [
                  0,
                  14,
                  19,
                  11,
                  0,
                  3,
                  2,
                  0
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "ed7b3b56-d078-4f57-9596-0ca224d0a39c",
              "level": 50,
              "skillLevel": 4,
              "templateId": "Character:HolyKnight_VR2_Light_BASE_T05",
              "upgrades": [
                15,
                0,
                1,
                0,
                0,
                25,
                1,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 50,
                "perks": [
                  0,
                  14,
                  19,
                  11,
                  0,
                  3,
                  2,
                  0
                ]
              },
              "bIsCommander": true,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "cdcdd038-ba4f-432d-aca3-ec74212f92d7",
              "level": 50,
              "skillLevel": 4,
              "templateId": "Character:TreasureHunter_VR2_Fire_AntiMaterialCharge_T05",
              "upgrades": [
                2,
                0,
                10,
                0,
                0,
                23,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 50,
                "perks": [
                  0,
                  14,
                  19,
                  11,
                  0,
                  3,
                  2,
                  0
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "0a229af9-e6fe-4e77-8008-d3f583c7aaa7",
              "level": 50,
              "skillLevel": 3,
              "templateId": "Character:Archer_Starter_Water_MultiShot_T03",
              "upgrades": [
                0,
                0,
                0,
                0,
                0,
                10,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 50,
                "perks": [
                  0,
                  14,
                  19,
                  11,
                  0,
                  3,
                  2,
                  0
                ]
              },
              "bIsCommander": false,
              "foilLevel": 1,
              "gearTemplateId": "",
              "itemId": "4f3a0920-391b-4be9-9911-970be67a1d2a",
              "level": 10,
              "skillLevel": 2,
              "templateId": "Character:TreasureHunter_R2_Water_PowerEfflux_T03",
              "upgrades": [
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 50,
                "perks": [
                  0,
                  14,
                  19,
                  11,
                  0,
                  3,
                  2,
                  0
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "a5f40540-9b49-4df7-b2ae-923fa1a7c885",
              "level": 50,
              "skillLevel": 4,
              "templateId": "Character:Archer_VR2_Nature_GoinCommando_T05",
              "upgrades": [
                0,
                0,
                3,
                0,
                0,
                40,
                1,
                0,
                0
              ]
            },
            {
              "bIsCommander": false,
              "foilLevel": 0,
              "level": 0,
              "skillLevel": 0
            }
          ],
          "mainCommanderIdx": 1,
          "opponent": {
            "avatarUrl": "wex-temp-avatar.png",
            "displayName": "Mickle_Pickle136",
            "isRobot": false,
            "matchmakingId": "b6d43baa4f8e4e9488909de0b4fdd148",
            "rating": 0,
            "taunt": "",
            "type": "Duel"
          }
        },
        {
          "heroInfo": [
            {
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  3,
                  8,
                  4,
                  0,
                  3,
                  0,
                  1
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "3a3067a2-5f90-47d5-9569-3c94a0ff75b5",
              "level": 15,
              "skillLevel": 2,
              "templateId": "Character:HolyKnight_VR2_Light_BASE_T05",
              "upgrades": [
                0,
                0,
                1,
                0,
                0,
                17,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  3,
                  8,
                  4,
                  0,
                  3,
                  0,
                  1
                ]
              },
              "bIsCommander": true,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "a459bfa0-be1c-4fa7-9b8a-afedbd787363",
              "level": 15,
              "skillLevel": 2,
              "templateId": "Character:TreasureHunter_VR2_Fire_AntiMaterialCharge_T05",
              "upgrades": [
                15,
                0,
                5,
                0,
                0,
                21,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  3,
                  8,
                  4,
                  0,
                  3,
                  0,
                  1
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "7eadd00f-6b32-427d-ba7d-35ec2e35c7ce",
              "level": 15,
              "skillLevel": 2,
              "templateId": "Character:Archer_Starter_Water_MultiShot_T03",
              "upgrades": [
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  3,
                  8,
                  4,
                  0,
                  3,
                  0,
                  1
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "4301a72d-a4a4-4aa1-ad82-d711eec4dabb",
              "level": 15,
              "skillLevel": 2,
              "templateId": "Character:TreasureHunter_R2_Water_PowerEfflux_T03",
              "upgrades": [
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  3,
                  8,
                  4,
                  0,
                  3,
                  0,
                  1
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "dafecf33-feb1-4d8a-8eae-8d93e52cd533",
              "level": 15,
              "skillLevel": 1,
              "templateId": "Character:Archer_VR2_Nature_GoinCommando_T05",
              "upgrades": [
                25,
                0,
                11,
                0,
                0,
                24,
                0,
                0,
                0
              ]
            },
            {
              "bIsCommander": false,
              "foilLevel": 0,
              "level": 0,
              "skillLevel": 0
            }
          ],
          "mainCommanderIdx": 1,
          "opponent": {
            "avatarUrl": "wex-temp-avatar.png",
            "displayName": "ADS_NICHO_2807",
            "isRobot": false,
            "matchmakingId": "c000ecdb6b51480c92d09f3da88efb11",
            "rating": 0,
            "taunt": "",
            "type": "Duel"
          }
        },
        {
          "heroInfo": [
            {
              "accountInfo": {
                "level": 12,
                "perks": [
                  0,
                  6,
                  5,
                  0,
                  0,
                  0,
                  0,
                  0
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "0a36a2c3-1553-4ea8-9c37-0956056c26d8",
              "level": 15,
              "skillLevel": 1,
              "templateId": "Character:Cleric_VR2_Dark_TerraRifle_T04",
              "upgrades": [
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 12,
                "perks": [
                  0,
                  6,
                  5,
                  0,
                  0,
                  0,
                  0,
                  0
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "3b02a017-2b13-4227-a9fa-fa26a5650d05",
              "level": 5,
              "skillLevel": 1,
              "templateId": "Character:Archer_UC1_Fire_ElementalBreath_T03",
              "upgrades": [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 12,
                "perks": [
                  0,
                  6,
                  5,
                  0,
                  0,
                  0,
                  0,
                  0
                ]
              },
              "bIsCommander": true,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "814efb5e-2ece-498c-96da-e781df4d6108",
              "level": 15,
              "skillLevel": 1,
              "templateId": "Character:Archer_VR2_Nature_GoinCommando_T05",
              "upgrades": [
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 12,
                "perks": [
                  0,
                  6,
                  5,
                  0,
                  0,
                  0,
                  0,
                  0
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "4dafdddb-59e1-4a4a-b6c9-2036166eb2cd",
              "level": 15,
              "skillLevel": 1,
              "templateId": "Character:Archer_Starter_Water_MultiShot_T03",
              "upgrades": [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 12,
                "perks": [
                  0,
                  6,
                  5,
                  0,
                  0,
                  0,
                  0,
                  0
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "7c95dbcd-7fb3-40bb-be31-69a96692db2d",
              "level": 15,
              "skillLevel": 1,
              "templateId": "Character:Mage_Starter_Fire_BurningSwordCombo_T03",
              "upgrades": [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "bIsCommander": false,
              "foilLevel": 0,
              "level": 0,
              "skillLevel": 0
            }
          ],
          "mainCommanderIdx": 2,
          "opponent": {
            "avatarUrl": "wex-temp-avatar.png",
            "displayName": "Wadimyr",
            "isRobot": false,
            "matchmakingId": "c30cfc96b31245ef88e53aea9317769e",
            "rating": 0,
            "taunt": "",
            "type": "Duel"
          }
        },
        {
          "heroInfo": [
            {
              "accountInfo": {
                "level": 30,
                "perks": [
                  0,
                  3,
                  21,
                  11,
                  1,
                  0,
                  3,
                  0
                ]
              },
              "bIsCommander": true,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "1aca79e7-6c81-467c-acf4-556d75377ea6",
              "level": 35,
              "skillLevel": 10,
              "templateId": "Character:Warrior_VR2_Dark_Rampage_T04",
              "upgrades": [
                25,
                0,
                25,
                0,
                0,
                15,
                0,
                15,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 30,
                "perks": [
                  0,
                  3,
                  21,
                  11,
                  1,
                  0,
                  3,
                  0
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "99cdc2f0-bf20-4333-99c3-c997ff1902e9",
              "level": 25,
              "skillLevel": 1,
              "templateId": "Character:Cleric_VR2_Dark_TerraRifle_T04",
              "upgrades": [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 30,
                "perks": [
                  0,
                  3,
                  21,
                  11,
                  1,
                  0,
                  3,
                  0
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "7f37374b-241b-4079-8f35-bcf6382a58b3",
              "level": 20,
              "skillLevel": 1,
              "templateId": "Character:Ninja_VR1_Light_CrystalDaggers_T04",
              "upgrades": [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 30,
                "perks": [
                  0,
                  3,
                  21,
                  11,
                  1,
                  0,
                  3,
                  0
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "5b58b924-a109-44e4-a609-597d20482297",
              "level": 25,
              "skillLevel": 1,
              "templateId": "Character:Knight_UC1_Light_Reconstruction_T03",
              "upgrades": [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 30,
                "perks": [
                  0,
                  3,
                  21,
                  11,
                  1,
                  0,
                  3,
                  0
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "7ec18e3a-b584-403b-b31b-e7979deebf8c",
              "level": 35,
              "skillLevel": 7,
              "templateId": "Character:Knight_UC2_Dark_SpearThrust_T04",
              "upgrades": [
                0,
                0,
                0,
                0,
                0,
                15,
                0,
                15,
                0
              ]
            },
            {
              "bIsCommander": false,
              "foilLevel": 0,
              "level": 0,
              "skillLevel": 0
            }
          ],
          "mainCommanderIdx": 0,
          "opponent": {
            "avatarUrl": "wex-temp-avatar.png",
            "displayName": "Peterfenton16",
            "isRobot": false,
            "matchmakingId": "e0e132d388904c8186a6fabaf16bcd97",
            "rating": 0,
            "taunt": "",
            "type": "Duel"
          }
        },
        {
          "heroInfo": [
            {
              "accountInfo": {
                "level": 24,
                "perks": [
                  0,
                  4,
                  10,
                  4,
                  0,
                  4,
                  0,
                  1
                ]
              },
              "bIsCommander": true,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "c61ea836-45b0-4b10-9891-15e948ef3831",
              "level": 25,
              "skillLevel": 1,
              "templateId": "Character:Cleric_VR2_Dark_TerraRifle_T04",
              "upgrades": [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 24,
                "perks": [
                  0,
                  4,
                  10,
                  4,
                  0,
                  4,
                  0,
                  1
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "0feacd6a-8202-47a0-aea9-05e35f9188c1",
              "level": 25,
              "skillLevel": 1,
              "templateId": "Character:Knight_UC2_Dark_SpearThrust_T04",
              "upgrades": [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 24,
                "perks": [
                  0,
                  4,
                  10,
                  4,
                  0,
                  4,
                  0,
                  1
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "9151d87d-9359-49af-8a3c-cfbeccd854a6",
              "level": 25,
              "skillLevel": 2,
              "templateId": "Character:Warrior_R2_Light_Warbear_T03",
              "upgrades": [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 24,
                "perks": [
                  0,
                  4,
                  10,
                  4,
                  0,
                  4,
                  0,
                  1
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "4736cd5f-63b7-4581-afc1-1b424fb18164",
              "level": 25,
              "skillLevel": 2,
              "templateId": "Character:Mage_Starter_Fire_BurningSwordCombo_T03",
              "upgrades": [
                25,
                0,
                22,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 24,
                "perks": [
                  0,
                  4,
                  10,
                  4,
                  0,
                  4,
                  0,
                  1
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "2f9ad425-f40e-4ea3-8a5a-802aa09f0e4d",
              "level": 25,
              "skillLevel": 2,
              "templateId": "Character:Warrior_Starter_Nature_PowerStrike_T03",
              "upgrades": [
                2,
                0,
                1,
                0,
                0,
                18,
                0,
                0,
                0
              ]
            },
            {
              "bIsCommander": false,
              "foilLevel": 0,
              "level": 0,
              "skillLevel": 0
            }
          ],
          "mainCommanderIdx": 0,
          "opponent": {
            "avatarUrl": "wex-temp-avatar.png",
            "displayName": "PRIZRAK2",
            "isRobot": false,
            "matchmakingId": "e2088a541fe44683a7be1b233d327f85",
            "rating": 0,
            "taunt": "",
            "type": "Duel"
          }
        },
        {
          "heroInfo": [
            {
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  4,
                  6,
                  5,
                  1,
                  5,
                  1,
                  2
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "e25453a3-b97b-4fd9-b2db-b2954a6db5c2",
              "level": 25,
              "skillLevel": 2,
              "templateId": "Character:HolyKnight_VR2_Light_BASE_T05",
              "upgrades": [
                23,
                0,
                22,
                0,
                1,
                3,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  4,
                  6,
                  5,
                  1,
                  5,
                  1,
                  2
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "059799f1-df29-4cff-adbf-f3ba70d9822b",
              "level": 20,
              "skillLevel": 1,
              "templateId": "Character:TreasureHunter_VR2_Fire_AntiMaterialCharge_T05",
              "upgrades": [
                1,
                0,
                1,
                0,
                0,
                4,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  4,
                  6,
                  5,
                  1,
                  5,
                  1,
                  2
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "6396fb0a-d97d-49ca-b853-6d2cbe020f2a",
              "level": 25,
              "skillLevel": 2,
              "templateId": "Character:Cleric_VR2_Dark_TerraRifle_T04",
              "upgrades": [
                8,
                0,
                8,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  4,
                  6,
                  5,
                  1,
                  5,
                  1,
                  2
                ]
              },
              "bIsCommander": true,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "84298cd5-0587-4982-8b74-25b32aa4d887",
              "level": 25,
              "skillLevel": 2,
              "templateId": "Character:Archer_VR2_Nature_GoinCommando_T05",
              "upgrades": [
                3,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  4,
                  6,
                  5,
                  1,
                  5,
                  1,
                  2
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "7d47eeb2-7f66-4bcf-9d98-d2c3c67468d8",
              "level": 15,
              "skillLevel": 1,
              "templateId": "Character:Cleric_R1_Water_RejuvenatingBreeze_T03",
              "upgrades": [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
              ]
            },
            {
              "bIsCommander": false,
              "foilLevel": 0,
              "level": 0,
              "skillLevel": 0
            }
          ],
          "mainCommanderIdx": 3,
          "opponent": {
            "avatarUrl": "wex-temp-avatar.png",
            "displayName": "FRANKAWA71",
            "isRobot": false,
            "matchmakingId": "e38c9342c5df412092c8f37efae0ae06",
            "rating": 0,
            "taunt": "",
            "type": "Duel"
          }
        },
        {
          "heroInfo": [
            {
              "accountInfo": {
                "level": 48,
                "perks": [
                  0,
                  15,
                  20,
                  16,
                  2,
                  4,
                  2,
                  2
                ]
              },
              "bIsCommander": true,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "84621e70-5fd7-443b-95dc-4f7dc801e990",
              "level": 50,
              "skillLevel": 3,
              "templateId": "Character:Cleric_VR2_Dark_TerraRifle_T04",
              "upgrades": [
                13,
                1,
                1,
                1,
                0,
                45,
                1,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 48,
                "perks": [
                  0,
                  15,
                  20,
                  16,
                  2,
                  4,
                  2,
                  2
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "d28c093d-0fa5-41d7-ac36-5a83ef783e49",
              "level": 50,
              "skillLevel": 3,
              "templateId": "Character:Warrior_R2_Light_Warbear_T03",
              "upgrades": [
                13,
                5,
                13,
                1,
                2,
                45,
                1,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 48,
                "perks": [
                  0,
                  15,
                  20,
                  16,
                  2,
                  4,
                  2,
                  2
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "bb07e4b0-6a3c-4fd7-a982-439004518e7f",
              "level": 50,
              "skillLevel": 3,
              "templateId": "Character:TreasureHunter_R2_Water_PowerEfflux_T03",
              "upgrades": [
                5,
                1,
                4,
                1,
                0,
                40,
                1,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 48,
                "perks": [
                  0,
                  15,
                  20,
                  16,
                  2,
                  4,
                  2,
                  2
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "95769b02-a92f-4d81-beaf-efdc2d52dc8f",
              "level": 50,
              "skillLevel": 3,
              "templateId": "Character:Ninja_UC1_Water_SwiftStrike_T03",
              "upgrades": [
                5,
                1,
                1,
                1,
                0,
                40,
                1,
                0,
                0
              ]
            },
            {
              "accountInfo": {
                "level": 48,
                "perks": [
                  0,
                  15,
                  20,
                  16,
                  2,
                  4,
                  2,
                  2
                ]
              },
              "bIsCommander": false,
              "foilLevel": -1,
              "gearTemplateId": "",
              "itemId": "f1a7da8f-cca9-4f09-a71e-bf1fb0f0a05c",
              "level": 40,
              "skillLevel": 3,
              "templateId": "Character:Archer_Starter_Water_MultiShot_T03",
              "upgrades": [
                0,
                0,
                0,
                0,
                0,
                38,
                1,
                0,
                0
              ]
            },
            {
              "bIsCommander": false,
              "foilLevel": 0,
              "level": 0,
              "skillLevel": 0
            }
          ],
          "mainCommanderIdx": 0,
          "opponent": {
            "avatarUrl": "wex-temp-avatar.png",
            "displayName": "Tigran_Mets7",
            "isRobot": false,
            "matchmakingId": "f2762941dc0e42d7a86efcb2060c5de4",
            "rating": 0,
            "taunt": "",
            "type": "Duel"
          }
        }
      ],
      "changeType": "itemAttrChanged",
      "itemId": "52431032-e69e-473a-8cfc-7218f54aa4ae"
    },
    {
      "attributeName": "recent_matches",
      "attributeValue": [
        "613e7d34a15b4953a38e6104058d1c92",
        "6fcf88c206ff407c8be2914e13a289d5",
        "8053ca676bb9415fb3ea445073dc3554",
        "8a193619c8134e5f8b5d457f520a0680",
        "9a56fb498b404f1599690a6033a67f27",
        "a277bd19718d45368254f90844725c2b",
        "a6a840af6f114a2fbae88c34e3419d2e",
        "ac48a1264d3e45da82bda46253655585",
        "b6d43baa4f8e4e9488909de0b4fdd148",
        "c000ecdb6b51480c92d09f3da88efb11",
        "c30cfc96b31245ef88e53aea9317769e",
        "e0e132d388904c8186a6fabaf16bcd97",
        "e2088a541fe44683a7be1b233d327f85",
        "e38c9342c5df412092c8f37efae0ae06",
        "f2762941dc0e42d7a86efcb2060c5de4"
      ],
      "changeType": "itemAttrChanged",
      "itemId": "52431032-e69e-473a-8cfc-7218f54aa4ae"
    }
  ],
  "profileChangesBaseRevision": 1,
  "profileCommandRevision": 1,
  "profileId": "multiplayer",
  "profileRevision": 3,
  "responseVersion": 1,
  "serverTime": "2022-12-29T13:42:33.197Z"
}
```

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
