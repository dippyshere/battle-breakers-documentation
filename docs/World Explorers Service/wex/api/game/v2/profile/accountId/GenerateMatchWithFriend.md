# Generate Match With Friend

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/:accountId/GenerateMatchWithFriend?profileId=multiplayer&rvn=1742*

___

## Request

```http
POST /wex/api/game/v2/profile/:accountId/GenerateMatchWithFriend?profileId=multiplayer&rvn=1742 HTTP/1.1
```

### Path Parameters

| Name     | Value                             |
|----------|-----------------------------------|
| acountId | ec0ebb7e56f6454e86c62299a7b32e21  |

### Query String

| Name      | Value       |
|-----------|-------------|
| profileId | multiplayer |
| rvn       | 1742        |

### Request Headers

| Name                         | Value                                                                                                                                                                                                                                                                              |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Host                         | wex-public-service-live-prod.ol.epicgames.com                                                                                                                                                                                                                                      |
| Accept-Encoding              | deflate, gzip                                                                                                                                                                                                                                                                      |
| Accept                       | \*/\*                                                                                                                                                                                                                                                                              |
| Content-Type                 | application/json                                                                                                                                                                                                                                                                   |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":23252},{"profileId":"levels","clientCommandRevision":14236},{"profileId":"friends","clientCommandRevision":8236},{"profileId":"monsterpit","clientCommandRevision":1036},{"profileId":"multiplayer","clientCommandRevision":833}] |
| X-Epic-Correlation-ID        | UE4-550659054c6fbbba966be789c8ecf002-D77C844B4D0785D0053F3CBFB86C4B7D-8D10D529479F4E5B5A880F8F8121614B                                                                                                                                                                             |
| User-Agent                   | WorldExplorers/1.88.244-r17036752 Windows/10.0.25267.1.256.64bit                                                                                                                                                                                                                   |
| Authorization                | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md)                                                                                                                                                              |
| Content-Length               | 65                                                                                                                                                                                                                                                                                 |

### Request Body

```json
{
  "friendInstanceId": "c3f69aba-0cea-4253-880f-d0dbb276ad1a"
}
```

___

## Response

#### Status: 200 OK

### Response Headers

| Name                         | Value                                                                                                  |
|------------------------------|--------------------------------------------------------------------------------------------------------|
| Date                         | Sat, 17 Dec 2022 13:26:16 GMT                                                                          |
| Content-Type                 | application/json                                                                                       |
| Transfer-Encoding            | chunked                                                                                                |
| X-EpicGames-Profile-Revision | 1742                                                                                                   |
| X-EpicGames-McpVersion       | prod Release-1.88-1.88 build 107 cl 19310354                                                           |
| X-EpicGames-ContentVersion   | 1.88.244-r17036752                                                                                     |
| X-EpicGames-MinBuild         | 17036752                                                                                               |
| X-Epic-Device-ID             | 7b6449837a601db90694fa85168cb856                                                                       |
| X-Epic-Correlation-ID        | UE4-550659054c6fbbba966be789c8ecf002-D77C844B4D0785D0053F3CBFB86C4B7D-8D10D529479F4E5B5A880F8F8121614B |
| Connection                   | keep-alive                                                                                             |

### Response Body

```json
{
  "profileRevision": 1744,
  "profileId": "multiplayer",
  "profileChangesBaseRevision": 1742,
  "profileChanges": [
    {
      "changeType": "itemAttrChanged",
      "itemId": "d6f9a500-82c4-4226-98cd-d69d16304ba5",
      "attributeName": "match_roster",
      "attributeValue": [
        {
          "opponent": {
            "matchmakingId": "002295f59fe146808568a8ff659afed5",
            "isRobot": false,
            "displayName": "PCreeper",
            "avatarUrl": "wex-temp-avatar.png",
            "rating": 9,
            "taunt": "",
            "type": "Duel"
          },
          "mainCommanderIdx": 1,
          "heroInfo": [
            {
              "itemId": "9daf12c8-c43b-41da-a897-5f6f3591623d",
              "templateId": "Character:Warrior_Starter_Nature_PowerStrike_T03",
              "bIsCommander": false,
              "level": 15,
              "skillLevel": 2,
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
              ],
              "accountInfo": {
                "level": 21,
                "perks": [
                  0,
                  3,
                  12,
                  3,
                  0,
                  1,
                  0,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "2c475a43-e6fb-481e-885f-3ad644add2d0",
              "templateId": "Character:Warrior_Starter_Fire_Berserking_T03",
              "bIsCommander": true,
              "level": 15,
              "skillLevel": 1,
              "upgrades": [
                2,
                0,
                2,
                0,
                0,
                0,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 21,
                "perks": [
                  0,
                  3,
                  12,
                  3,
                  0,
                  1,
                  0,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "be2371d0-6b73-4835-9257-35fb45842878",
              "templateId": "Character:TreasureHunter_R2_Nature_PowerEfflux_T03",
              "bIsCommander": false,
              "level": 15,
              "skillLevel": 2,
              "upgrades": [
                3,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 21,
                "perks": [
                  0,
                  3,
                  12,
                  3,
                  0,
                  1,
                  0,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "20ae46cb-39ff-4a3d-8fb5-6ff24b09989f",
              "templateId": "Character:Mage_UC1_Fire_ElementalBlast_T03",
              "bIsCommander": false,
              "level": 15,
              "skillLevel": 1,
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
              ],
              "accountInfo": {
                "level": 21,
                "perks": [
                  0,
                  3,
                  12,
                  3,
                  0,
                  1,
                  0,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "a1747df5-a9b9-4d9a-9dc6-cdb120f26c54",
              "templateId": "Character:Mage_R2_Dark_BloodMagic_T03",
              "bIsCommander": false,
              "level": 15,
              "skillLevel": 2,
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
              ],
              "accountInfo": {
                "level": 21,
                "perks": [
                  0,
                  3,
                  12,
                  3,
                  0,
                  1,
                  0,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "bIsCommander": false,
              "level": 0,
              "skillLevel": 0,
              "foilLevel": 0
            }
          ]
        },
        {
          "opponent": {
            "matchmakingId": "0d87d6f44ba54ff8bb4de8b9df0d938c",
            "isRobot": false,
            "displayName": "WakefulJungle29",
            "avatarUrl": "wex-temp-avatar.png",
            "rating": 38,
            "taunt": "",
            "type": "Duel"
          },
          "mainCommanderIdx": 0,
          "heroInfo": [
            {
              "itemId": "83480547-da97-4213-84a9-860ba803d6db",
              "templateId": "Character:TreasureHunter_VR2_Fire_AntiMaterialCharge_T05",
              "bIsCommander": true,
              "level": 70,
              "skillLevel": 15,
              "upgrades": [
                60,
                54,
                60,
                53,
                4,
                15,
                0,
                15,
                0
              ],
              "accountInfo": {
                "level": 54,
                "perks": [
                  3,
                  46,
                  34,
                  5,
                  3,
                  0,
                  1,
                  4
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "f834e130-3664-4c0c-914b-ed56dad49a8e",
              "templateId": "Character:Archer_VR2_Fire_Rustlord_T04",
              "bIsCommander": false,
              "level": 67,
              "skillLevel": 13,
              "upgrades": [
                53,
                53,
                53,
                39,
                4,
                25,
                1,
                0,
                0
              ],
              "accountInfo": {
                "level": 54,
                "perks": [
                  3,
                  46,
                  34,
                  5,
                  3,
                  0,
                  1,
                  4
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "ce95991f-a265-4251-8568-68f7ba253265",
              "templateId": "Character:Archer_SR2_Light_LoveRanger_T05",
              "bIsCommander": false,
              "level": 67,
              "skillLevel": 13,
              "upgrades": [
                53,
                25,
                53,
                25,
                4,
                17,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 54,
                "perks": [
                  3,
                  46,
                  34,
                  5,
                  3,
                  0,
                  1,
                  4
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "1835f895-5a15-44aa-971d-71c74fbddf15",
              "templateId": "Character:Warmage_SR2_Dark_CuddleTeamLeader_T05",
              "bIsCommander": false,
              "level": 76,
              "skillLevel": 12,
              "upgrades": [
                74,
                67,
                74,
                34,
                4,
                25,
                1,
                15,
                0
              ],
              "accountInfo": {
                "level": 54,
                "perks": [
                  3,
                  46,
                  34,
                  5,
                  3,
                  0,
                  1,
                  4
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "84db1c7a-7143-41a8-a74c-58616e16dbf4",
              "templateId": "Character:Archer_VR2_Nature_GoinCommando_T05",
              "bIsCommander": false,
              "level": 70,
              "skillLevel": 13,
              "upgrades": [
                60,
                3,
                60,
                1,
                0,
                15,
                0,
                15,
                0
              ],
              "accountInfo": {
                "level": 54,
                "perks": [
                  3,
                  46,
                  34,
                  5,
                  3,
                  0,
                  1,
                  4
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "bIsCommander": false,
              "level": 0,
              "skillLevel": 0,
              "foilLevel": 0
            }
          ]
        },
        {
          "opponent": {
            "matchmakingId": "1bdc9801e5004df8810217ec550a6669",
            "isRobot": false,
            "displayName": "Metalking_3",
            "avatarUrl": "wex-temp-avatar.png",
            "rating": 3,
            "taunt": "",
            "type": "Duel"
          },
          "mainCommanderIdx": 0,
          "heroInfo": [
            {
              "itemId": "ea131cbe-678b-4dc0-b1c0-2272d97a77d4",
              "templateId": "Character:Warrior_Starter_Nature_PowerStrike_T03",
              "bIsCommander": true,
              "level": 15,
              "skillLevel": 1,
              "upgrades": [
                2,
                0,
                2,
                0,
                0,
                0,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 12,
                "perks": [
                  0,
                  5,
                  4,
                  3,
                  0,
                  0,
                  1,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "4f447c03-2eba-4a62-bf1c-9f0ab8c24bec",
              "templateId": "Character:Warrior_Starter_Fire_Berserking_T03",
              "bIsCommander": false,
              "level": 15,
              "skillLevel": 1,
              "upgrades": [
                0,
                0,
                2,
                0,
                0,
                0,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 12,
                "perks": [
                  0,
                  5,
                  4,
                  3,
                  0,
                  0,
                  1,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "36ff4130-389f-4f15-98d1-0589ad274f38",
              "templateId": "Character:Cleric_VR2_Dark_TerraRifle_T04",
              "bIsCommander": false,
              "level": 15,
              "skillLevel": 1,
              "upgrades": [
                2,
                0,
                2,
                0,
                0,
                0,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 12,
                "perks": [
                  0,
                  5,
                  4,
                  3,
                  0,
                  0,
                  1,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "0eebd7e8-78f6-48de-bfc3-f6d80d60f942",
              "templateId": "Character:Mage_R2_Dark_BloodMagic_T03",
              "bIsCommander": false,
              "level": 15,
              "skillLevel": 1,
              "upgrades": [
                1,
                0,
                2,
                0,
                0,
                0,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 12,
                "perks": [
                  0,
                  5,
                  4,
                  3,
                  0,
                  0,
                  1,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "254d7fa9-bb8b-46e9-82ab-7f80ea2db0b0",
              "templateId": "Character:Ninja_UC1_Water_SwiftStrike_T03",
              "bIsCommander": false,
              "level": 15,
              "skillLevel": 1,
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
              ],
              "accountInfo": {
                "level": 12,
                "perks": [
                  0,
                  5,
                  4,
                  3,
                  0,
                  0,
                  1,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "bIsCommander": false,
              "level": 0,
              "skillLevel": 0,
              "foilLevel": 0
            }
          ]
        },
        {
          "opponent": {
            "matchmakingId": "1d9ac0390a4d4125a4dcc9a3d529f452",
            "isRobot": false,
            "displayName": "Mabon.\u7dcf\u9577\u304b\u304f\u3099\u3084\u3068\u4e09\u7396\u59c9",
            "avatarUrl": "wex-temp-avatar.png",
            "rating": 3,
            "taunt": "",
            "type": "Duel"
          },
          "mainCommanderIdx": 0,
          "heroInfo": [
            {
              "itemId": "aa0f85c0-39d9-4113-9eb3-dd1572f50286",
              "templateId": "Character:HolyKnight_VR2_Light_BASE_T05",
              "bIsCommander": true,
              "level": 20,
              "skillLevel": 2,
              "upgrades": [
                0,
                1,
                3,
                1,
                1,
                0,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  1,
                  10,
                  4,
                  0,
                  3,
                  0,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "60af6303-9afb-434b-99b4-8b45eff70afe",
              "templateId": "Character:TreasureHunter_VR2_Fire_AntiMaterialCharge_T05",
              "bIsCommander": false,
              "level": 20,
              "skillLevel": 2,
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
              ],
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  1,
                  10,
                  4,
                  0,
                  3,
                  0,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "fbc0561f-6aca-44b9-9e01-2f3d2b36f2b1",
              "templateId": "Character:TreasureHunter_R2_Fire_PowerEfflux_T03",
              "bIsCommander": false,
              "level": 20,
              "skillLevel": 1,
              "upgrades": [
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  1,
                  10,
                  4,
                  0,
                  3,
                  0,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "2e9f2320-be77-4554-8a9c-5e817b33923a",
              "templateId": "Character:Ninja_R2_Dark_TripleStab_T03",
              "bIsCommander": false,
              "level": 20,
              "skillLevel": 1,
              "upgrades": [
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  1,
                  10,
                  4,
                  0,
                  3,
                  0,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "c632ce83-1563-4b78-94c2-c13494b5d87b",
              "templateId": "Character:Warmage_R1_Fire_FuelTheFire_T03",
              "bIsCommander": false,
              "level": 20,
              "skillLevel": 1,
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
              ],
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  1,
                  10,
                  4,
                  0,
                  3,
                  0,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "bIsCommander": false,
              "level": 0,
              "skillLevel": 0,
              "foilLevel": 0
            }
          ]
        },
        {
          "opponent": {
            "matchmakingId": "262d69068fe94004ae5faff6894988c2",
            "isRobot": false,
            "displayName": "T.R.I.X.I",
            "avatarUrl": "wex-temp-avatar.png",
            "rating": 49,
            "taunt": "",
            "type": "Duel"
          },
          "mainCommanderIdx": 1,
          "heroInfo": [
            {
              "itemId": "a49a5951-f35d-415e-a4d2-a576d613bba1",
              "templateId": "Character:HolyKnight_VR2_Light_BASE_T05",
              "bIsCommander": false,
              "level": 142,
              "skillLevel": 20,
              "upgrades": [
                95,
                95,
                95,
                95,
                34,
                105,
                4,
                50,
                2
              ],
              "accountInfo": {
                "level": 167,
                "perks": [
                  2,
                  46,
                  45,
                  45,
                  2,
                  43,
                  5,
                  6
                ]
              },
              "foilLevel": 1,
              "gearTemplateId": ""
            },
            {
              "itemId": "e766602c-a745-402a-b75a-f485c7466aaf",
              "templateId": "Character:TreasureHunter_VR2_Fire_AntiMaterialCharge_T06",
              "bIsCommander": true,
              "level": 142,
              "skillLevel": 20,
              "upgrades": [
                95,
                95,
                95,
                95,
                34,
                105,
                4,
                50,
                2
              ],
              "accountInfo": {
                "level": 167,
                "perks": [
                  2,
                  46,
                  45,
                  45,
                  2,
                  43,
                  5,
                  6
                ]
              },
              "foilLevel": 1,
              "gearTemplateId": ""
            },
            {
              "itemId": "0d90f178-804f-4ed8-bc77-3f2de65c74ee",
              "templateId": "Character:Cleric_R1_Water_RejuvenatingBreeze_T05",
              "bIsCommander": false,
              "level": 142,
              "skillLevel": 20,
              "upgrades": [
                95,
                95,
                95,
                95,
                34,
                105,
                4,
                50,
                2
              ],
              "accountInfo": {
                "level": 167,
                "perks": [
                  2,
                  46,
                  45,
                  45,
                  2,
                  43,
                  5,
                  6
                ]
              },
              "foilLevel": 1,
              "gearTemplateId": ""
            },
            {
              "itemId": "35cd8f10-3fc1-494a-ae82-d3282b1acd7a",
              "templateId": "Character:Warmage_SR2_Dark_CuddleTeamLeader_T06",
              "bIsCommander": false,
              "level": 142,
              "skillLevel": 20,
              "upgrades": [
                95,
                95,
                95,
                95,
                34,
                105,
                4,
                50,
                2
              ],
              "accountInfo": {
                "level": 167,
                "perks": [
                  2,
                  46,
                  45,
                  45,
                  2,
                  43,
                  5,
                  6
                ]
              },
              "foilLevel": 1,
              "gearTemplateId": ""
            },
            {
              "itemId": "d657aedd-def9-44e9-b9d6-00ec645f0a3e",
              "templateId": "Character:Archer_VR2_Nature_GoinCommando_T06",
              "bIsCommander": false,
              "level": 142,
              "skillLevel": 20,
              "upgrades": [
                95,
                95,
                95,
                95,
                34,
                105,
                4,
                50,
                2
              ],
              "accountInfo": {
                "level": 167,
                "perks": [
                  2,
                  46,
                  45,
                  45,
                  2,
                  43,
                  5,
                  6
                ]
              },
              "foilLevel": 1,
              "gearTemplateId": ""
            },
            {
              "bIsCommander": false,
              "level": 0,
              "skillLevel": 0,
              "foilLevel": 0
            }
          ]
        },
        {
          "opponent": {
            "matchmakingId": "45c226ac94e1471e96e4e66f09289f41",
            "isRobot": false,
            "displayName": "Dr. Sad",
            "avatarUrl": "wex-temp-avatar.png",
            "rating": 0,
            "taunt": "",
            "type": "Duel"
          },
          "mainCommanderIdx": 0,
          "heroInfo": [
            {
              "itemId": "43dd0d92-76ce-4526-b8ad-c374aa23e2d0",
              "templateId": "Character:Warmage_VR1_Fire_CleansingLight_T04",
              "bIsCommander": true,
              "level": 50,
              "skillLevel": 9,
              "upgrades": [
                21,
                0,
                13,
                16,
                2,
                18,
                1,
                19,
                1
              ],
              "accountInfo": {
                "level": 45,
                "perks": [
                  1,
                  15,
                  32,
                  5,
                  2,
                  1,
                  3,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "0cd2b2b3-4545-4112-b321-e7906083697c",
              "templateId": "Character:Archer_VR2_Nature_GoinCommando_T05",
              "bIsCommander": false,
              "level": 50,
              "skillLevel": 3,
              "upgrades": [
                1,
                2,
                7,
                16,
                4,
                10,
                0,
                14,
                1
              ],
              "accountInfo": {
                "level": 45,
                "perks": [
                  1,
                  15,
                  32,
                  5,
                  2,
                  1,
                  3,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "e640d604-1084-4b12-9d01-ca5e2c5cefbe",
              "templateId": "Character:Ninja_VR1_Light_CrystalDaggers_T04",
              "bIsCommander": false,
              "level": 50,
              "skillLevel": 4,
              "upgrades": [
                25,
                0,
                8,
                0,
                0,
                10,
                0,
                10,
                0
              ],
              "accountInfo": {
                "level": 45,
                "perks": [
                  1,
                  15,
                  32,
                  5,
                  2,
                  1,
                  3,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "b602e79b-ef9a-4508-8d44-edc480ae3dbc",
              "templateId": "Character:TreasureHunter_R2_Water_PowerEfflux_T04",
              "bIsCommander": false,
              "level": 50,
              "skillLevel": 1,
              "upgrades": [
                0,
                0,
                0,
                0,
                0,
                10,
                0,
                10,
                0
              ],
              "accountInfo": {
                "level": 45,
                "perks": [
                  1,
                  15,
                  32,
                  5,
                  2,
                  1,
                  3,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "cfe5b8f9-2720-4239-995d-88dc8b099e28",
              "templateId": "Character:Cleric_VR2_Dark_TerraRifle_T04",
              "bIsCommander": false,
              "level": 50,
              "skillLevel": 4,
              "upgrades": [
                1,
                0,
                1,
                1,
                0,
                10,
                0,
                10,
                0
              ],
              "accountInfo": {
                "level": 45,
                "perks": [
                  1,
                  15,
                  32,
                  5,
                  2,
                  1,
                  3,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "bIsCommander": false,
              "level": 0,
              "skillLevel": 0,
              "foilLevel": 0
            }
          ]
        },
        {
          "opponent": {
            "matchmakingId": "4a06bd4c3f46425e8a810ed1badada0a",
            "isRobot": false,
            "displayName": "Erick \u0ca0_\u0ca0 \u9b5a\u306e\u9854",
            "avatarUrl": "wex-temp-avatar.png",
            "rating": 9,
            "taunt": "",
            "type": "Duel"
          },
          "mainCommanderIdx": 0,
          "heroInfo": [
            {
              "itemId": "55ad8d70-7282-4b3b-85a3-9542cc64d0b6",
              "templateId": "Character:Warrior_VR2_Dark_Rampage_T04",
              "bIsCommander": true,
              "level": 25,
              "skillLevel": 6,
              "upgrades": [
                22,
                8,
                20,
                8,
                0,
                8,
                0,
                10,
                0
              ],
              "accountInfo": {
                "level": 27,
                "perks": [
                  0,
                  5,
                  13,
                  5,
                  0,
                  2,
                  1,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "a92ce249-3e6e-4b6f-8652-fc9c8b13a877",
              "templateId": "Character:Ninja_VR1_Light_CrystalDaggers_T04",
              "bIsCommander": false,
              "level": 25,
              "skillLevel": 10,
              "upgrades": [
                0,
                0,
                0,
                0,
                0,
                3,
                0,
                5,
                0
              ],
              "accountInfo": {
                "level": 27,
                "perks": [
                  0,
                  5,
                  13,
                  5,
                  0,
                  2,
                  1,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "4af96186-8d0b-42bd-8d89-c3fd7af77a6d",
              "templateId": "Character:Knight_VR1_Water_ShieldStance_T04",
              "bIsCommander": false,
              "level": 2,
              "skillLevel": 1,
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
              ],
              "accountInfo": {
                "level": 27,
                "perks": [
                  0,
                  5,
                  13,
                  5,
                  0,
                  2,
                  1,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "e8653c96-5966-4fdc-9764-5b847a19a9e9",
              "templateId": "Character:TreasureHunter_R2_Fire_PowerEfflux_T03",
              "bIsCommander": false,
              "level": 25,
              "skillLevel": 2,
              "upgrades": [
                0,
                3,
                3,
                3,
                0,
                0,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 27,
                "perks": [
                  0,
                  5,
                  13,
                  5,
                  0,
                  2,
                  1,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "8ad162bd-504b-4180-8f9b-f82d267fa3fc",
              "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
              "bIsCommander": false,
              "level": 25,
              "skillLevel": 3,
              "upgrades": [
                3,
                2,
                3,
                2,
                0,
                0,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 27,
                "perks": [
                  0,
                  5,
                  13,
                  5,
                  0,
                  2,
                  1,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "bIsCommander": false,
              "level": 0,
              "skillLevel": 0,
              "foilLevel": 0
            }
          ]
        },
        {
          "opponent": {
            "matchmakingId": "4b6ca1b347174bebb5efc288d33665d3",
            "isRobot": false,
            "displayName": "Vinsont93300",
            "avatarUrl": "wex-temp-avatar.png",
            "rating": 1,
            "taunt": "",
            "type": "Duel"
          },
          "mainCommanderIdx": 3,
          "heroInfo": [
            {
              "itemId": "6d1cb1d5-a65e-4c3e-b6f8-620c8c271bf7",
              "templateId": "Character:Cleric_VR2_Dark_TerraRifle_T04",
              "bIsCommander": false,
              "level": 15,
              "skillLevel": 1,
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
              ],
              "accountInfo": {
                "level": 10,
                "perks": [
                  0,
                  3,
                  3,
                  2,
                  0,
                  1,
                  0,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "fe0c21b2-af58-4b88-abdb-c8cf0f6e9d63",
              "templateId": "Character:Warrior_R2_Nature_Whirlwind_T03",
              "bIsCommander": false,
              "level": 15,
              "skillLevel": 1,
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
              ],
              "accountInfo": {
                "level": 10,
                "perks": [
                  0,
                  3,
                  3,
                  2,
                  0,
                  1,
                  0,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "70f6070f-456e-4247-a69b-88d6b8f92abc",
              "templateId": "Character:Ninja_R2_Dark_TripleStab_T03",
              "bIsCommander": false,
              "level": 10,
              "skillLevel": 1,
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
              ],
              "accountInfo": {
                "level": 10,
                "perks": [
                  0,
                  3,
                  3,
                  2,
                  0,
                  1,
                  0,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "45c38636-7cbd-45e5-be63-5348c02fed4f",
              "templateId": "Character:Archer_Starter_Water_MultiShot_T03",
              "bIsCommander": true,
              "level": 15,
              "skillLevel": 1,
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
              ],
              "accountInfo": {
                "level": 10,
                "perks": [
                  0,
                  3,
                  3,
                  2,
                  0,
                  1,
                  0,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "3bf0613b-74a1-44ba-82e9-dbaa8ec3704f",
              "templateId": "Character:Mage_Starter_Fire_BurningSwordCombo_T03",
              "bIsCommander": false,
              "level": 15,
              "skillLevel": 1,
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
              ],
              "accountInfo": {
                "level": 10,
                "perks": [
                  0,
                  3,
                  3,
                  2,
                  0,
                  1,
                  0,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "bIsCommander": false,
              "level": 0,
              "skillLevel": 0,
              "foilLevel": 0
            }
          ]
        },
        {
          "opponent": {
            "matchmakingId": "502e47c02e4846ba81f157c20e7781db",
            "isRobot": false,
            "displayName": "Tryharderscrubs",
            "avatarUrl": "wex-temp-avatar.png",
            "rating": 0,
            "taunt": "",
            "type": "Duel"
          },
          "mainCommanderIdx": 0,
          "heroInfo": [
            {
              "itemId": "547a2a0f-df13-4969-8909-f3ffc7cb87c8",
              "templateId": "Character:HolyKnight_VR2_Light_BASE_T05",
              "bIsCommander": true,
              "level": 40,
              "skillLevel": 3,
              "upgrades": [
                11,
                0,
                23,
                0,
                0,
                40,
                1,
                0,
                0
              ],
              "accountInfo": {
                "level": 39,
                "perks": [
                  0,
                  14,
                  25,
                  8,
                  2,
                  0,
                  1,
                  2
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "12951162-7ebd-4ee8-a33f-268df2d77e8d",
              "templateId": "Character:Archer_VR2_Nature_GoinCommando_T05",
              "bIsCommander": false,
              "level": 40,
              "skillLevel": 3,
              "upgrades": [
                24,
                0,
                0,
                0,
                0,
                35,
                1,
                0,
                0
              ],
              "accountInfo": {
                "level": 39,
                "perks": [
                  0,
                  14,
                  25,
                  8,
                  2,
                  0,
                  1,
                  2
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "c986f635-7b51-43ad-8650-91fa93442efc",
              "templateId": "Character:TreasureHunter_VR2_Fire_AntiMaterialCharge_T05",
              "bIsCommander": false,
              "level": 40,
              "skillLevel": 4,
              "upgrades": [
                25,
                0,
                10,
                3,
                0,
                25,
                1,
                0,
                0
              ],
              "accountInfo": {
                "level": 39,
                "perks": [
                  0,
                  14,
                  25,
                  8,
                  2,
                  0,
                  1,
                  2
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "9986b03d-3be1-4c99-a1fa-2a8bc8080681",
              "templateId": "Character:Knight_UC2_Dark_SpearThrust_T04",
              "bIsCommander": false,
              "level": 40,
              "skillLevel": 2,
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
              ],
              "accountInfo": {
                "level": 39,
                "perks": [
                  0,
                  14,
                  25,
                  8,
                  2,
                  0,
                  1,
                  2
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "eb0af67a-d742-414c-b35a-8025165d91fb",
              "templateId": "Character:Archer_Starter_Water_MultiShot_T03",
              "bIsCommander": false,
              "level": 40,
              "skillLevel": 3,
              "upgrades": [
                4,
                0,
                0,
                0,
                0,
                25,
                1,
                0,
                0
              ],
              "accountInfo": {
                "level": 39,
                "perks": [
                  0,
                  14,
                  25,
                  8,
                  2,
                  0,
                  1,
                  2
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "bIsCommander": false,
              "level": 0,
              "skillLevel": 0,
              "foilLevel": 0
            }
          ]
        },
        {
          "opponent": {
            "matchmakingId": "5933aec04201443d899ae459ba5ea058",
            "isRobot": false,
            "displayName": "lexa072004",
            "avatarUrl": "wex-temp-avatar.png",
            "rating": 0,
            "taunt": "",
            "type": "Duel"
          },
          "mainCommanderIdx": 0,
          "heroInfo": [
            {
              "itemId": "500a8dc1-4657-414f-b21e-7ce61afc1f65",
              "templateId": "Character:Cleric_VR2_Dark_TerraRifle_T04",
              "bIsCommander": true,
              "level": 20,
              "skillLevel": 2,
              "upgrades": [
                0,
                0,
                1,
                0,
                0,
                7,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 18,
                "perks": [
                  0,
                  5,
                  8,
                  4,
                  0,
                  0,
                  0,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "a6e34ecb-7e26-491e-ad0e-412b14ab3190",
              "templateId": "Character:TreasureHunter_R2_Fire_PowerEfflux_T03",
              "bIsCommander": false,
              "level": 20,
              "skillLevel": 2,
              "upgrades": [
                0,
                0,
                6,
                0,
                0,
                6,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 18,
                "perks": [
                  0,
                  5,
                  8,
                  4,
                  0,
                  0,
                  0,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "a3d96569-4761-4265-b87f-319b5abb0254",
              "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
              "bIsCommander": false,
              "level": 20,
              "skillLevel": 1,
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
              ],
              "accountInfo": {
                "level": 18,
                "perks": [
                  0,
                  5,
                  8,
                  4,
                  0,
                  0,
                  0,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "164bfc9e-a3a1-4867-8425-16ecd69c546b",
              "templateId": "Character:Mage_Starter_Fire_BurningSwordCombo_T03",
              "bIsCommander": false,
              "level": 20,
              "skillLevel": 1,
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
              ],
              "accountInfo": {
                "level": 18,
                "perks": [
                  0,
                  5,
                  8,
                  4,
                  0,
                  0,
                  0,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "c6d95f64-6935-4496-bf95-b77962e6bd83",
              "templateId": "Character:Mage_R2_Dark_BloodMagic_T03",
              "bIsCommander": false,
              "level": 20,
              "skillLevel": 1,
              "upgrades": [
                25,
                0,
                24,
                0,
                0,
                24,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 18,
                "perks": [
                  0,
                  5,
                  8,
                  4,
                  0,
                  0,
                  0,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "bIsCommander": false,
              "level": 0,
              "skillLevel": 0,
              "foilLevel": 0
            }
          ]
        },
        {
          "opponent": {
            "matchmakingId": "61fefd7a2d8c4d9396f56e1fc44bb0b1",
            "isRobot": false,
            "displayName": "JJulianBL14",
            "avatarUrl": "wex-temp-avatar.png",
            "rating": 5,
            "taunt": "",
            "type": "Duel"
          },
          "mainCommanderIdx": 2,
          "heroInfo": [
            {
              "itemId": "7ca391db-866d-4859-bdba-71c8c2e4b9bf",
              "templateId": "Character:Warrior_Starter_Fire_Berserking_T03",
              "bIsCommander": false,
              "level": 15,
              "skillLevel": 1,
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
              ],
              "accountInfo": {
                "level": 13,
                "perks": [
                  0,
                  5,
                  7,
                  5,
                  1,
                  2,
                  2,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "bIsCommander": false,
              "level": 0,
              "skillLevel": 0,
              "foilLevel": 0
            },
            {
              "itemId": "74162db9-63a0-4581-9fb6-766447eb71b9",
              "templateId": "Character:Ninja_VR1_Light_CrystalDaggers_T04",
              "bIsCommander": true,
              "level": 15,
              "skillLevel": 1,
              "upgrades": [
                0,
                0,
                9,
                0,
                0,
                0,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 13,
                "perks": [
                  0,
                  5,
                  7,
                  5,
                  1,
                  2,
                  2,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "ea7ce91e-d851-43c0-9933-5905ecbfcd6a",
              "templateId": "Character:Archer_Starter_Water_MultiShot_T03",
              "bIsCommander": false,
              "level": 15,
              "skillLevel": 1,
              "upgrades": [
                0,
                0,
                2,
                0,
                0,
                0,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 13,
                "perks": [
                  0,
                  5,
                  7,
                  5,
                  1,
                  2,
                  2,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "f4701aa5-5e5e-4b68-b3f7-5ef5ac635687",
              "templateId": "Character:Ninja_UC1_Water_SwiftStrike_T03",
              "bIsCommander": false,
              "level": 15,
              "skillLevel": 1,
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
              ],
              "accountInfo": {
                "level": 13,
                "perks": [
                  0,
                  5,
                  7,
                  5,
                  1,
                  2,
                  2,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "bIsCommander": false,
              "level": 0,
              "skillLevel": 0,
              "foilLevel": 0
            }
          ]
        },
        {
          "opponent": {
            "matchmakingId": "682c6677455f4f579ccb03b296fd3b6a",
            "isRobot": false,
            "displayName": "\u0632\u0628\u0627\u062f\u064a 69",
            "avatarUrl": "wex-temp-avatar.png",
            "rating": 0,
            "taunt": "",
            "type": "Duel"
          },
          "mainCommanderIdx": 0,
          "heroInfo": [
            {
              "itemId": "f71a38e7-37ba-436f-9c14-624ec082c492",
              "templateId": "Character:HolyKnight_VR2_Light_BASE_T05",
              "bIsCommander": true,
              "level": 25,
              "skillLevel": 2,
              "upgrades": [
                5,
                3,
                6,
                0,
                0,
                6,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 21,
                "perks": [
                  0,
                  4,
                  7,
                  8,
                  0,
                  0,
                  1,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "232eeaa2-938d-4e3f-8e02-738e17c45293",
              "templateId": "Character:TreasureHunter_VR2_Fire_AntiMaterialCharge_T05",
              "bIsCommander": false,
              "level": 25,
              "skillLevel": 2,
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
              ],
              "accountInfo": {
                "level": 21,
                "perks": [
                  0,
                  4,
                  7,
                  8,
                  0,
                  0,
                  1,
                  0
                ]
              },
              "foilLevel": 1,
              "gearTemplateId": ""
            },
            {
              "itemId": "4cba9e18-382a-4979-9329-260f0f4e7cfe",
              "templateId": "Character:Warrior_Starter_Fire_Berserking_T03",
              "bIsCommander": false,
              "level": 25,
              "skillLevel": 2,
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
              ],
              "accountInfo": {
                "level": 21,
                "perks": [
                  0,
                  4,
                  7,
                  8,
                  0,
                  0,
                  1,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "1a76f94e-95be-4c3f-bdec-28c6b5350b67",
              "templateId": "Character:Mage_UC1_Fire_ElementalBlast_T03",
              "bIsCommander": false,
              "level": 25,
              "skillLevel": 1,
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
              ],
              "accountInfo": {
                "level": 21,
                "perks": [
                  0,
                  4,
                  7,
                  8,
                  0,
                  0,
                  1,
                  0
                ]
              },
              "foilLevel": 1,
              "gearTemplateId": ""
            },
            {
              "itemId": "4290371c-3654-4b0a-9b44-33dc2c7c7214",
              "templateId": "Character:Mage_Starter_Fire_BurningSwordCombo_T03",
              "bIsCommander": false,
              "level": 25,
              "skillLevel": 2,
              "upgrades": [
                0,
                0,
                7,
                0,
                0,
                0,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 21,
                "perks": [
                  0,
                  4,
                  7,
                  8,
                  0,
                  0,
                  1,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "bIsCommander": false,
              "level": 0,
              "skillLevel": 0,
              "foilLevel": 0
            }
          ]
        },
        {
          "opponent": {
            "matchmakingId": "6bff281dd94143878d9cce6ade2cd9f2",
            "isRobot": false,
            "displayName": "MichaelShow11",
            "avatarUrl": "wex-temp-avatar.png",
            "rating": 3,
            "taunt": "",
            "type": "Duel"
          },
          "mainCommanderIdx": 1,
          "heroInfo": [
            {
              "itemId": "ac741c5e-0193-4593-a272-1e8a1de2b934",
              "templateId": "Character:Ninja_R2_Dark_TripleStab_T03",
              "bIsCommander": false,
              "level": 25,
              "skillLevel": 1,
              "upgrades": [
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 23,
                "perks": [
                  0,
                  5,
                  9,
                  4,
                  1,
                  8,
                  2,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "53dcf89a-684f-49f5-8f04-350744cc16e7",
              "templateId": "Character:Ninja_VR1_Light_CrystalDaggers_T04",
              "bIsCommander": true,
              "level": 25,
              "skillLevel": 5,
              "upgrades": [
                19,
                5,
                0,
                3,
                1,
                0,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 23,
                "perks": [
                  0,
                  5,
                  9,
                  4,
                  1,
                  8,
                  2,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "6ee80b67-756a-451e-8adf-02d8f577a2b7",
              "templateId": "Character:Archer_Starter_Water_MultiShot_T03",
              "bIsCommander": false,
              "level": 25,
              "skillLevel": 2,
              "upgrades": [
                16,
                5,
                0,
                5,
                1,
                0,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 23,
                "perks": [
                  0,
                  5,
                  9,
                  4,
                  1,
                  8,
                  2,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "03ce9ba9-6d82-4dd8-94a8-c9c65276689c",
              "templateId": "Character:Assassin_R2_Nature_Slasher_T03",
              "bIsCommander": false,
              "level": 25,
              "skillLevel": 2,
              "upgrades": [
                24,
                4,
                3,
                3,
                0,
                0,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 23,
                "perks": [
                  0,
                  5,
                  9,
                  4,
                  1,
                  8,
                  2,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "f763cbd4-db54-4551-95ae-031080100356",
              "templateId": "Character:Mage_Starter_Fire_BurningSwordCombo_T03",
              "bIsCommander": false,
              "level": 25,
              "skillLevel": 2,
              "upgrades": [
                1,
                3,
                0,
                3,
                0,
                0,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 23,
                "perks": [
                  0,
                  5,
                  9,
                  4,
                  1,
                  8,
                  2,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "bIsCommander": false,
              "level": 0,
              "skillLevel": 0,
              "foilLevel": 0
            }
          ]
        },
        {
          "opponent": {
            "matchmakingId": "7cd34f48c1c34681bc996f37a84bb717",
            "isRobot": false,
            "displayName": "magicSODAA",
            "avatarUrl": "wex-temp-avatar.png",
            "rating": 0,
            "taunt": "",
            "type": "Duel"
          },
          "mainCommanderIdx": 0,
          "heroInfo": [
            {
              "itemId": "70837a67-0c87-4252-9d28-9baed56022ce",
              "templateId": "Character:Warrior_Starter_Fire_Berserking_T03",
              "bIsCommander": true,
              "level": 25,
              "skillLevel": 2,
              "upgrades": [
                15,
                0,
                7,
                1,
                0,
                24,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 21,
                "perks": [
                  0,
                  3,
                  9,
                  5,
                  0,
                  2,
                  1,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "88a734d0-169d-439a-8743-a4b097bbca71",
              "templateId": "Character:Warrior_VR2_Dark_Rampage_T04",
              "bIsCommander": false,
              "level": 25,
              "skillLevel": 2,
              "upgrades": [
                25,
                0,
                0,
                0,
                0,
                24,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 21,
                "perks": [
                  0,
                  3,
                  9,
                  5,
                  0,
                  2,
                  1,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "b1bf581a-9a82-4ae3-9e4d-a3edbe09e2e1",
              "templateId": "Character:TreasureHunter_R2_Fire_PowerEfflux_T03",
              "bIsCommander": false,
              "level": 25,
              "skillLevel": 1,
              "upgrades": [
                25,
                0,
                2,
                0,
                0,
                24,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 21,
                "perks": [
                  0,
                  3,
                  9,
                  5,
                  0,
                  2,
                  1,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "d2dde3c9-5824-4a84-8b29-a879a6a3d701",
              "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
              "bIsCommander": false,
              "level": 25,
              "skillLevel": 2,
              "upgrades": [
                25,
                0,
                25,
                0,
                0,
                24,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 21,
                "perks": [
                  0,
                  3,
                  9,
                  5,
                  0,
                  2,
                  1,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "704e09da-4de5-45cb-a786-1b4efc2a2386",
              "templateId": "Character:Mage_Starter_Fire_BurningSwordCombo_T03",
              "bIsCommander": false,
              "level": 25,
              "skillLevel": 2,
              "upgrades": [
                25,
                0,
                25,
                0,
                0,
                24,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 21,
                "perks": [
                  0,
                  3,
                  9,
                  5,
                  0,
                  2,
                  1,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "bIsCommander": false,
              "level": 0,
              "skillLevel": 0,
              "foilLevel": 0
            }
          ]
        },
        {
          "opponent": {
            "matchmakingId": "90e731755b2f40dbb28fc0c3fe6f0104",
            "isRobot": false,
            "displayName": "Judananas987",
            "avatarUrl": "wex-temp-avatar.png",
            "rating": 0,
            "taunt": "",
            "type": "Duel"
          },
          "mainCommanderIdx": 1,
          "heroInfo": [
            {
              "itemId": "d6c338dc-3654-47a9-8ab3-5373867fbb0e",
              "templateId": "Character:Archer_R1_Nature_VolleyOfArrows_T03",
              "bIsCommander": false,
              "level": 19,
              "skillLevel": 1,
              "upgrades": [
                17,
                0,
                20,
                0,
                0,
                0,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  4,
                  5,
                  5,
                  0,
                  4,
                  0,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "2f0115f6-8a0a-45a5-9fe6-5591af048369",
              "templateId": "Character:TreasureHunter_R2_Fire_PowerEfflux_T03",
              "bIsCommander": true,
              "level": 20,
              "skillLevel": 2,
              "upgrades": [
                2,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  4,
                  5,
                  5,
                  0,
                  4,
                  0,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "522c080e-3262-4787-b777-2ee29e827a92",
              "templateId": "Character:Cleric_VR2_Dark_TerraRifle_T04",
              "bIsCommander": false,
              "level": 20,
              "skillLevel": 2,
              "upgrades": [
                7,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  4,
                  5,
                  5,
                  0,
                  4,
                  0,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "55227cc4-b511-4bbe-aa19-22aa2c85043e",
              "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
              "bIsCommander": false,
              "level": 20,
              "skillLevel": 2,
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
              ],
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  4,
                  5,
                  5,
                  0,
                  4,
                  0,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "604f8637-7f6e-45a8-a75c-d0fd9298eb5f",
              "templateId": "Character:Assassin_R2_Nature_Slasher_T03",
              "bIsCommander": false,
              "level": 20,
              "skillLevel": 2,
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
              ],
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  4,
                  5,
                  5,
                  0,
                  4,
                  0,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "bIsCommander": false,
              "level": 0,
              "skillLevel": 0,
              "foilLevel": 0
            }
          ]
        },
        {
          "opponent": {
            "matchmakingId": "9586895dc50d45698d142f4b1314ac21",
            "isRobot": false,
            "displayName": "NCRniki",
            "avatarUrl": "wex-temp-avatar.png",
            "rating": 0,
            "taunt": "",
            "type": "Duel"
          },
          "mainCommanderIdx": 0,
          "heroInfo": [
            {
              "itemId": "a82cd42a-e058-4a8d-9a44-66cbc62fb421",
              "templateId": "Character:Warrior_Starter_Fire_Berserking_T03",
              "bIsCommander": true,
              "level": 30,
              "skillLevel": 2,
              "upgrades": [
                1,
                0,
                8,
                0,
                0,
                0,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 30,
                "perks": [
                  0,
                  2,
                  12,
                  14,
                  0,
                  0,
                  0,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "8138e398-96e0-4655-b2eb-5e157d6c0f2a",
              "templateId": "Character:TreasureHunter_R2_Fire_PowerEfflux_T03",
              "bIsCommander": false,
              "level": 30,
              "skillLevel": 2,
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
              ],
              "accountInfo": {
                "level": 30,
                "perks": [
                  0,
                  2,
                  12,
                  14,
                  0,
                  0,
                  0,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "1194de0a-d95c-47da-acf3-895b0b309b29",
              "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
              "bIsCommander": false,
              "level": 25,
              "skillLevel": 2,
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
              ],
              "accountInfo": {
                "level": 30,
                "perks": [
                  0,
                  2,
                  12,
                  14,
                  0,
                  0,
                  0,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "ec2a142a-076f-4d85-9f7d-5357eb43d670",
              "templateId": "Character:Mage_Starter_Fire_BurningSwordCombo_T03",
              "bIsCommander": false,
              "level": 15,
              "skillLevel": 1,
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
              ],
              "accountInfo": {
                "level": 30,
                "perks": [
                  0,
                  2,
                  12,
                  14,
                  0,
                  0,
                  0,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "9dd9a837-bd15-4eef-aee0-1b402154fcba",
              "templateId": "Character:Mage_R2_Dark_BloodMagic_T03",
              "bIsCommander": false,
              "level": 30,
              "skillLevel": 2,
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
              ],
              "accountInfo": {
                "level": 30,
                "perks": [
                  0,
                  2,
                  12,
                  14,
                  0,
                  0,
                  0,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "bIsCommander": false,
              "level": 0,
              "skillLevel": 0,
              "foilLevel": 0
            }
          ]
        },
        {
          "opponent": {
            "matchmakingId": "993d596cd913486e8f6de96541071f2d",
            "isRobot": false,
            "displayName": "Thenakedarabian",
            "avatarUrl": "wex-temp-avatar.png",
            "rating": 0,
            "taunt": "",
            "type": "Duel"
          },
          "mainCommanderIdx": 2,
          "heroInfo": [
            {
              "itemId": "f154b12d-eed3-4b7b-aa57-2798350e8122",
              "templateId": "Character:TreasureHunter_R2_Fire_PowerEfflux_T03",
              "bIsCommander": false,
              "level": 20,
              "skillLevel": 2,
              "upgrades": [
                2,
                0,
                3,
                0,
                0,
                0,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 17,
                "perks": [
                  0,
                  4,
                  7,
                  4,
                  0,
                  1,
                  0,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "5ad7bb23-515a-4611-85dd-7a57f8475585",
              "templateId": "Character:Warrior_Starter_Fire_Berserking_T03",
              "bIsCommander": false,
              "level": 20,
              "skillLevel": 2,
              "upgrades": [
                2,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 17,
                "perks": [
                  0,
                  4,
                  7,
                  4,
                  0,
                  1,
                  0,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "7ff28a46-3f83-47fc-80a4-f689588aa83b",
              "templateId": "Character:Cleric_VR2_Dark_TerraRifle_T04",
              "bIsCommander": true,
              "level": 20,
              "skillLevel": 2,
              "upgrades": [
                9,
                3,
                1,
                1,
                0,
                0,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 17,
                "perks": [
                  0,
                  4,
                  7,
                  4,
                  0,
                  1,
                  0,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "917b003b-5a06-4696-9c4b-3058e5c7d023",
              "templateId": "Character:Mage_UC1_Fire_ElementalBlast_T03",
              "bIsCommander": false,
              "level": 20,
              "skillLevel": 1,
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
              ],
              "accountInfo": {
                "level": 17,
                "perks": [
                  0,
                  4,
                  7,
                  4,
                  0,
                  1,
                  0,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "4f1a3272-0d30-48b6-bbda-080d8f0513ce",
              "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
              "bIsCommander": false,
              "level": 20,
              "skillLevel": 1,
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
              ],
              "accountInfo": {
                "level": 17,
                "perks": [
                  0,
                  4,
                  7,
                  4,
                  0,
                  1,
                  0,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "bIsCommander": false,
              "level": 0,
              "skillLevel": 0,
              "foilLevel": 0
            }
          ]
        },
        {
          "opponent": {
            "matchmakingId": "a54df92ade374a7c9bd7e48e4972cfee",
            "isRobot": false,
            "displayName": "CatReader",
            "avatarUrl": "wex-temp-avatar.png",
            "rating": 0,
            "taunt": "",
            "type": "Duel"
          },
          "mainCommanderIdx": 4,
          "heroInfo": [
            {
              "itemId": "f44db3d4-bd13-4157-8454-80a3979fd91d",
              "templateId": "Character:Shadowknight_VR1_Dark_AbyssalGaze_T06",
              "bIsCommander": false,
              "level": 150,
              "skillLevel": 20,
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
              ],
              "accountInfo": {
                "level": 336,
                "perks": [
                  8,
                  48,
                  280,
                  125,
                  8,
                  0,
                  0,
                  25
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "6c0db724-ab3e-4b07-9d40-09547db62fb3",
              "templateId": "Character:Blademaster_SR1_Nature_HurricaneBlade_T06",
              "bIsCommander": false,
              "level": 150,
              "skillLevel": 14,
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
              ],
              "accountInfo": {
                "level": 336,
                "perks": [
                  8,
                  48,
                  280,
                  125,
                  8,
                  0,
                  0,
                  25
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "4cf96fe3-0856-4fc6-8ce2-73d60725e928",
              "templateId": "Character:MartialArtist_VR1_Fire_BleedingPalm_T05",
              "bIsCommander": false,
              "level": 132,
              "skillLevel": 11,
              "upgrades": [
                53,
                3,
                53,
                0,
                16,
                120,
                2,
                120,
                2
              ],
              "accountInfo": {
                "level": 336,
                "perks": [
                  8,
                  48,
                  280,
                  125,
                  8,
                  0,
                  0,
                  25
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "73b5db66-81f0-433a-83a2-bd9727efc079",
              "templateId": "Character:Archer_SR1_Nature_FlurryOfArrows_T06",
              "bIsCommander": false,
              "level": 150,
              "skillLevel": 20,
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
              ],
              "accountInfo": {
                "level": 336,
                "perks": [
                  8,
                  48,
                  280,
                  125,
                  8,
                  0,
                  0,
                  25
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "746bcaca-1f89-4e77-a86b-cd396ea34abe",
              "templateId": "Character:Cleric_SR1_Water_RevitalizingWaters_T06",
              "bIsCommander": true,
              "level": 150,
              "skillLevel": 16,
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
              ],
              "accountInfo": {
                "level": 336,
                "perks": [
                  8,
                  48,
                  280,
                  125,
                  8,
                  0,
                  0,
                  25
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "bIsCommander": false,
              "level": 0,
              "skillLevel": 0,
              "foilLevel": 0
            }
          ]
        },
        {
          "opponent": {
            "matchmakingId": "accab96960164a7483d03bd136fdc203",
            "isRobot": false,
            "displayName": "alex280com",
            "avatarUrl": "wex-temp-avatar.png",
            "rating": 0,
            "taunt": "",
            "type": "Duel"
          },
          "mainCommanderIdx": 1,
          "heroInfo": [
            {
              "itemId": "65468570-2d1a-4fab-a9db-bdd55881cbc4",
              "templateId": "Character:Warrior_Starter_Nature_PowerStrike_T03",
              "bIsCommander": false,
              "level": 10,
              "skillLevel": 1,
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
              ],
              "accountInfo": {
                "level": 11,
                "perks": [
                  0,
                  6,
                  2,
                  1,
                  0,
                  1,
                  0,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "87d1168a-f417-4a6f-aaf4-64a29f62c77a",
              "templateId": "Character:Warrior_R2_Nature_Whirlwind_T03",
              "bIsCommander": true,
              "level": 10,
              "skillLevel": 1,
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
              ],
              "accountInfo": {
                "level": 11,
                "perks": [
                  0,
                  6,
                  2,
                  1,
                  0,
                  1,
                  0,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "3bd36d90-b0ab-4da5-bd5b-08200c7cd076",
              "templateId": "Character:Mage_Starter_Fire_BurningSwordCombo_T03",
              "bIsCommander": false,
              "level": 10,
              "skillLevel": 1,
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
              ],
              "accountInfo": {
                "level": 11,
                "perks": [
                  0,
                  6,
                  2,
                  1,
                  0,
                  1,
                  0,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "6127c2f4-ee97-4c5e-accd-fbc350048499",
              "templateId": "Character:Ninja_UC1_Water_SwiftStrike_T03",
              "bIsCommander": false,
              "level": 10,
              "skillLevel": 1,
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
              ],
              "accountInfo": {
                "level": 11,
                "perks": [
                  0,
                  6,
                  2,
                  1,
                  0,
                  1,
                  0,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "5bd2706d-8df0-43f3-b674-65c7cf8ac227",
              "templateId": "Character:Warrior_Starter_Dark_RoboGuy_T02",
              "bIsCommander": false,
              "level": 10,
              "skillLevel": 1,
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
              ],
              "accountInfo": {
                "level": 11,
                "perks": [
                  0,
                  6,
                  2,
                  1,
                  0,
                  1,
                  0,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "bIsCommander": false,
              "level": 0,
              "skillLevel": 0,
              "foilLevel": 0
            }
          ]
        },
        {
          "opponent": {
            "matchmakingId": "c3d35fa036304df9aade0af43aafef5c",
            "isRobot": false,
            "displayName": "FF TheMine3",
            "avatarUrl": "wex-temp-avatar.png",
            "rating": 0,
            "taunt": "",
            "type": "Duel"
          },
          "mainCommanderIdx": 1,
          "heroInfo": [
            {
              "itemId": "bf82b569-8f65-404b-9374-19329a5c9732",
              "templateId": "Character:Mage_Starter_Fire_BurningSwordCombo_T03",
              "bIsCommander": false,
              "level": 5,
              "skillLevel": 1,
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
              ],
              "accountInfo": {
                "level": 12,
                "perks": [
                  0,
                  4,
                  4,
                  3,
                  0,
                  0,
                  0,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "e64d7d5d-b5d9-42f7-ba07-709971dbe85b",
              "templateId": "Character:Warrior_R2_Nature_Whirlwind_T03",
              "bIsCommander": true,
              "level": 15,
              "skillLevel": 1,
              "upgrades": [
                2,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 12,
                "perks": [
                  0,
                  4,
                  4,
                  3,
                  0,
                  0,
                  0,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "c5f418a0-87ca-4594-b4d8-49d565b437e6",
              "templateId": "Character:Ninja_UC1_Water_SwiftStrike_T03",
              "bIsCommander": false,
              "level": 15,
              "skillLevel": 1,
              "upgrades": [
                2,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 12,
                "perks": [
                  0,
                  4,
                  4,
                  3,
                  0,
                  0,
                  0,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "465e31fb-2c6f-4472-a256-7956b391f5cb",
              "templateId": "Character:Ninja_VR1_Light_CrystalDaggers_T04",
              "bIsCommander": false,
              "level": 15,
              "skillLevel": 1,
              "upgrades": [
                1,
                1,
                0,
                0,
                1,
                0,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 12,
                "perks": [
                  0,
                  4,
                  4,
                  3,
                  0,
                  0,
                  0,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "a51284fb-b5d7-4fc1-b66d-c0c6e14da9f3",
              "templateId": "Character:Cleric_VR2_Dark_TerraRifle_T04",
              "bIsCommander": false,
              "level": 15,
              "skillLevel": 1,
              "upgrades": [
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 12,
                "perks": [
                  0,
                  4,
                  4,
                  3,
                  0,
                  0,
                  0,
                  0
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "bIsCommander": false,
              "level": 0,
              "skillLevel": 0,
              "foilLevel": 0
            }
          ]
        },
        {
          "opponent": {
            "matchmakingId": "c805249dbb104181823096abcf7751d2",
            "isRobot": false,
            "displayName": "\u0645\u064f\u0639\u0633\u0651\u0644 \u0646\u064e\u0639\u0646\u0639",
            "avatarUrl": "wex-temp-avatar.png",
            "rating": 0,
            "taunt": "",
            "type": "Duel"
          },
          "mainCommanderIdx": 0,
          "heroInfo": [
            {
              "itemId": "71026284-8874-4d8c-802b-0575d1b4cb1a",
              "templateId": "Character:Warrior_VR2_Dark_Rampage_T04",
              "bIsCommander": true,
              "level": 55,
              "skillLevel": 4,
              "upgrades": [
                25,
                6,
                25,
                2,
                2,
                45,
                1,
                0,
                0
              ],
              "accountInfo": {
                "level": 50,
                "perks": [
                  0,
                  15,
                  15,
                  14,
                  1,
                  11,
                  2,
                  2
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "666a6aee-ffdb-4810-b525-f70ab6201190",
              "templateId": "Character:HolyKnight_VR2_Light_BASE_T05",
              "bIsCommander": false,
              "level": 55,
              "skillLevel": 4,
              "upgrades": [
                13,
                0,
                1,
                1,
                0,
                45,
                1,
                0,
                0
              ],
              "accountInfo": {
                "level": 50,
                "perks": [
                  0,
                  15,
                  15,
                  14,
                  1,
                  11,
                  2,
                  2
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "fb870ebd-0983-42e0-8838-aad5ea6ed445",
              "templateId": "Character:Archer_VR2_Nature_GoinCommando_T05",
              "bIsCommander": false,
              "level": 64,
              "skillLevel": 9,
              "upgrades": [
                25,
                12,
                25,
                15,
                2,
                45,
                1,
                0,
                0
              ],
              "accountInfo": {
                "level": 50,
                "perks": [
                  0,
                  15,
                  15,
                  14,
                  1,
                  11,
                  2,
                  2
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "87059472-1d64-4f9f-b554-3e0c29266e99",
              "templateId": "Character:Warmage_VR1_Fire_CleansingLight_T04",
              "bIsCommander": false,
              "level": 50,
              "skillLevel": 2,
              "upgrades": [
                0,
                0,
                0,
                0,
                0,
                45,
                1,
                0,
                0
              ],
              "accountInfo": {
                "level": 50,
                "perks": [
                  0,
                  15,
                  15,
                  14,
                  1,
                  11,
                  2,
                  2
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "e0572a59-d4c8-40c5-9ae6-680a15a51479",
              "templateId": "Character:TreasureHunter_R2_Water_PowerEfflux_T04",
              "bIsCommander": false,
              "level": 55,
              "skillLevel": 3,
              "upgrades": [
                2,
                1,
                0,
                4,
                0,
                45,
                1,
                0,
                0
              ],
              "accountInfo": {
                "level": 50,
                "perks": [
                  0,
                  15,
                  15,
                  14,
                  1,
                  11,
                  2,
                  2
                ]
              },
              "foilLevel": 1,
              "gearTemplateId": ""
            },
            {
              "bIsCommander": false,
              "level": 0,
              "skillLevel": 0,
              "foilLevel": 0
            }
          ]
        },
        {
          "opponent": {
            "matchmakingId": "d4a9bb28a977409d8ea1ac0daaba8406",
            "isRobot": false,
            "displayName": "Pirojok1441",
            "avatarUrl": "wex-temp-avatar.png",
            "rating": 0,
            "taunt": "",
            "type": "Duel"
          },
          "mainCommanderIdx": 0,
          "heroInfo": [
            {
              "itemId": "977eacc8-c717-440c-9a4c-9deee30dfd75",
              "templateId": "Character:Cleric_VR2_Dark_TerraRifle_T04",
              "bIsCommander": true,
              "level": 25,
              "skillLevel": 2,
              "upgrades": [
                20,
                5,
                23,
                0,
                0,
                0,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 22,
                "perks": [
                  0,
                  5,
                  9,
                  3,
                  0,
                  4,
                  0,
                  3
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "d44b335f-01b9-4d61-9f93-07f9f435069e",
              "templateId": "Character:Archer_UC1_Fire_ElementalBreath_T03",
              "bIsCommander": false,
              "level": 25,
              "skillLevel": 1,
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
              ],
              "accountInfo": {
                "level": 22,
                "perks": [
                  0,
                  5,
                  9,
                  3,
                  0,
                  4,
                  0,
                  3
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "d3731854-f556-4051-b1c5-1239399c8875",
              "templateId": "Character:Warrior_Starter_Nature_PowerStrike_T03",
              "bIsCommander": false,
              "level": 25,
              "skillLevel": 2,
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
              ],
              "accountInfo": {
                "level": 22,
                "perks": [
                  0,
                  5,
                  9,
                  3,
                  0,
                  4,
                  0,
                  3
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "dc94c71f-1382-4e23-8b15-cc1d460a07ad",
              "templateId": "Character:Cleric_UC1_Nature_Heal_T03",
              "bIsCommander": false,
              "level": 15,
              "skillLevel": 1,
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
              ],
              "accountInfo": {
                "level": 22,
                "perks": [
                  0,
                  5,
                  9,
                  3,
                  0,
                  4,
                  0,
                  3
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "82a474c8-efe9-43e6-b2e2-d54da3c69fb3",
              "templateId": "Character:Ninja_VR1_Light_CrystalDaggers_T04",
              "bIsCommander": false,
              "level": 25,
              "skillLevel": 2,
              "upgrades": [
                20,
                5,
                0,
                11,
                0,
                0,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 22,
                "perks": [
                  0,
                  5,
                  9,
                  3,
                  0,
                  4,
                  0,
                  3
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "bIsCommander": false,
              "level": 0,
              "skillLevel": 0,
              "foilLevel": 0
            }
          ]
        },
        {
          "opponent": {
            "matchmakingId": "d8df9be5efd7471bb41e8909a591927e",
            "isRobot": false,
            "displayName": "XpLOz_wezzer",
            "avatarUrl": "wex-temp-avatar.png",
            "rating": 0,
            "taunt": "",
            "type": "Duel"
          },
          "mainCommanderIdx": 1,
          "heroInfo": [
            {
              "itemId": "83c87f19-afbe-4397-86bb-3dbcca4150e2",
              "templateId": "Character:Knight_UC1_Light_Reconstruction_T03",
              "bIsCommander": false,
              "level": 10,
              "skillLevel": 2,
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
              ],
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  4,
                  5,
                  7,
                  0,
                  2,
                  0,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "79c48a94-d710-4001-b7c4-68db86574612",
              "templateId": "Character:Ninja_UC1_Water_SwiftStrike_T03",
              "bIsCommander": true,
              "level": 20,
              "skillLevel": 2,
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
              ],
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  4,
                  5,
                  7,
                  0,
                  2,
                  0,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "156b2df6-9cdd-4bb7-97cd-f4898fc9293a",
              "templateId": "Character:Knight_UC2_Dark_SpearThrust_T04",
              "bIsCommander": false,
              "level": 20,
              "skillLevel": 2,
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
              ],
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  4,
                  5,
                  7,
                  0,
                  2,
                  0,
                  1
                ]
              },
              "foilLevel": 1,
              "gearTemplateId": ""
            },
            {
              "itemId": "0f93c5fb-bd76-42a2-bc5d-bf884cf0558e",
              "templateId": "Character:Archer_VR2_Nature_GoinCommando_T05",
              "bIsCommander": false,
              "level": 20,
              "skillLevel": 1,
              "upgrades": [
                2,
                0,
                0,
                6,
                0,
                0,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  4,
                  5,
                  7,
                  0,
                  2,
                  0,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "f4ed7100-fecf-4fae-879a-3eed5e5e6691",
              "templateId": "Character:Mage_Basic_Fire_EnergyBlast_T02",
              "bIsCommander": false,
              "level": 20,
              "skillLevel": 1,
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
              ],
              "accountInfo": {
                "level": 20,
                "perks": [
                  0,
                  4,
                  5,
                  7,
                  0,
                  2,
                  0,
                  1
                ]
              },
              "foilLevel": 1,
              "gearTemplateId": ""
            },
            {
              "bIsCommander": false,
              "level": 0,
              "skillLevel": 0,
              "foilLevel": 0
            }
          ]
        },
        {
          "opponent": {
            "matchmakingId": "de6aad4459db4edea536866918b9b7e0",
            "isRobot": false,
            "displayName": "XaviGa\u0328mer11",
            "avatarUrl": "wex-temp-avatar.png",
            "rating": 0,
            "taunt": "",
            "type": "Duel"
          },
          "mainCommanderIdx": 0,
          "heroInfo": [
            {
              "itemId": "07f60045-426e-4afa-a373-f0ba4f352e6a",
              "templateId": "Character:HolyKnight_VR2_Light_BASE_T05",
              "bIsCommander": true,
              "level": 25,
              "skillLevel": 2,
              "upgrades": [
                1,
                18,
                1,
                18,
                0,
                0,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 25,
                "perks": [
                  0,
                  6,
                  6,
                  6,
                  0,
                  2,
                  0,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "6544eae9-0796-4ed6-894e-cb0cd95a9480",
              "templateId": "Character:TreasureHunter_VR2_Fire_AntiMaterialCharge_T05",
              "bIsCommander": false,
              "level": 25,
              "skillLevel": 2,
              "upgrades": [
                1,
                2,
                1,
                2,
                0,
                0,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 25,
                "perks": [
                  0,
                  6,
                  6,
                  6,
                  0,
                  2,
                  0,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "481ec15f-21c7-46ec-af9d-c5c5f5e3e69f",
              "templateId": "Character:Archer_VR2_Nature_GoinCommando_T05",
              "bIsCommander": false,
              "level": 25,
              "skillLevel": 2,
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
              ],
              "accountInfo": {
                "level": 25,
                "perks": [
                  0,
                  6,
                  6,
                  6,
                  0,
                  2,
                  0,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "c0d77679-895d-4ad9-a559-8b19db18e16b",
              "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
              "bIsCommander": false,
              "level": 25,
              "skillLevel": 2,
              "upgrades": [
                21,
                0,
                20,
                0,
                0,
                0,
                0,
                0,
                0
              ],
              "accountInfo": {
                "level": 25,
                "perks": [
                  0,
                  6,
                  6,
                  6,
                  0,
                  2,
                  0,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "itemId": "574fb51f-e3d0-4471-b06d-f7c35da6f609",
              "templateId": "Character:Ninja_R2_Dark_TripleStab_T03",
              "bIsCommander": false,
              "level": 20,
              "skillLevel": 2,
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
              ],
              "accountInfo": {
                "level": 25,
                "perks": [
                  0,
                  6,
                  6,
                  6,
                  0,
                  2,
                  0,
                  1
                ]
              },
              "foilLevel": -1,
              "gearTemplateId": ""
            },
            {
              "bIsCommander": false,
              "level": 0,
              "skillLevel": 0,
              "foilLevel": 0
            }
          ]
        },
        {
          "opponent": {
            "matchmakingId": "618ca94b-f17c-4dbf-bf83-b8c516ae1b24",
            "isRobot": true,
            "displayName": "Mr. Roboto",
            "avatarUrl": "http://epic-dnikdel-test.s3.amazonaws.com/avatars/wex-temp-machine-avatar.png",
            "rating": 1780,
            "taunt": "Come at me bro!",
            "type": "Duel"
          },
          "mainCommanderIdx": 4,
          "heroInfo": [
            {
              "itemId": "",
              "templateId": "",
              "bIsCommander": false,
              "level": 1,
              "skillLevel": 1,
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
              ],
              "foilLevel": 0
            },
            {
              "itemId": "a8bc2c32-4988-49f0-a929-9a88decf48cb",
              "templateId": "Character:Blademaster_VR1_Dark_SinisterStrike_T05",
              "bIsCommander": false,
              "level": 1,
              "skillLevel": 1,
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
              ],
              "accountInfo": {
                "level": 0,
                "perks": [
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
              "foilLevel": 0,
              "gearTemplateId": ""
            },
            {
              "itemId": "44b65475-299d-44bb-bc6f-0df3c8f8d932",
              "templateId": "Character:Warrior_VR1_Light_Deflect_T04",
              "bIsCommander": false,
              "level": 1,
              "skillLevel": 1,
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
              ],
              "accountInfo": {
                "level": 0,
                "perks": [
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
              "foilLevel": 0,
              "gearTemplateId": ""
            },
            {
              "itemId": "aa3c9526-565b-4b35-8d0d-d2f5dc6aad59",
              "templateId": "Character:Cleric_R1_Water_RejuvenatingBreeze_T03",
              "bIsCommander": false,
              "level": 1,
              "skillLevel": 1,
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
              ],
              "accountInfo": {
                "level": 0,
                "perks": [
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
              "foilLevel": 0,
              "gearTemplateId": ""
            },
            {
              "itemId": "637d4f2b-bebd-47ac-b35a-43e35885b14f",
              "templateId": "Character:Warmage_R1_Fire_FuelTheFire_T05",
              "bIsCommander": true,
              "level": 1,
              "skillLevel": 1,
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
              ],
              "accountInfo": {
                "level": 0,
                "perks": [
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
              "foilLevel": 0,
              "gearTemplateId": ""
            },
            {
              "itemId": "6659d759-ad4a-40ee-a375-0e5fcf6c14e8",
              "templateId": "Character:Spellsword_SR1_Dark_BladesOfDecay_T05",
              "bIsCommander": false,
              "level": 1,
              "skillLevel": 1,
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
              ],
              "accountInfo": {
                "level": 0,
                "perks": [
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
              "foilLevel": 0,
              "gearTemplateId": ""
            }
          ]
        },
        {
          "opponent": {
            "matchmakingId": "15512b25e6c44acaa5b3f993d93e2574",
            "isRobot": false,
            "displayName": "1911_SPETNAZ",
            "avatarUrl": "wex-temp-avatar.png",
            "rating": 0,
            "taunt": "",
            "type": "Sparring"
          },
          "mainCommanderIdx": 0,
          "heroInfo": [
            {
              "itemId": "aa8378af-1d3d-443f-a75a-40d9b192939e",
              "templateId": "Character:DragonKnight_SR1_Water_DragonForm_T06",
              "bIsCommander": true,
              "level": 150,
              "skillLevel": 20,
              "upgrades": [
                95,
                95,
                95,
                95,
                34,
                150,
                6,
                0,
                0
              ],
              "accountInfo": {
                "level": 887,
                "perks": [
                  20,
                  130,
                  776,
                  324,
                  18,
                  0,
                  0,
                  69
                ]
              },
              "foilLevel": 1,
              "gearTemplateId": "Character:DragonKnight_SR1_Water_JumpStrike_T06"
            },
            {
              "itemId": "a85ca951-2863-400a-a1db-8a6d3369deb3",
              "templateId": "Character:Warmage_SR2_Dark_CuddleTeamLeader_T06",
              "bIsCommander": false,
              "level": 150,
              "skillLevel": 20,
              "upgrades": [
                95,
                95,
                95,
                95,
                34,
                150,
                6,
                0,
                0
              ],
              "accountInfo": {
                "level": 887,
                "perks": [
                  20,
                  130,
                  776,
                  324,
                  18,
                  0,
                  0,
                  69
                ]
              },
              "foilLevel": 1,
              "gearTemplateId": "Character:Warmage_SR2_Dark_Shadowflame_T06"
            },
            {
              "itemId": "f23eb7b5-ee93-4bef-a785-2303dbc6529f",
              "templateId": "Character:Knight_SR2_Water_CryosteelGolem_T06",
              "bIsCommander": false,
              "level": 150,
              "skillLevel": 20,
              "upgrades": [
                95,
                95,
                95,
                95,
                34,
                150,
                6,
                0,
                0
              ],
              "accountInfo": {
                "level": 887,
                "perks": [
                  20,
                  130,
                  776,
                  324,
                  18,
                  0,
                  0,
                  69
                ]
              },
              "foilLevel": 1,
              "gearTemplateId": "Character:Mage_VR1_Water_Hailstorm_T05"
            },
            {
              "itemId": "5b7b7f3b-bcdf-4ebe-aa34-ac1247c9dff6",
              "templateId": "Character:Cleric_SR1_Water_RevitalizingWaters_T06",
              "bIsCommander": false,
              "level": 150,
              "skillLevel": 20,
              "upgrades": [
                95,
                95,
                95,
                95,
                34,
                150,
                6,
                0,
                0
              ],
              "accountInfo": {
                "level": 887,
                "perks": [
                  20,
                  130,
                  776,
                  324,
                  18,
                  0,
                  0,
                  69
                ]
              },
              "foilLevel": 1,
              "gearTemplateId": "Character:Mage_VR1_Water_Hailstorm_T05"
            },
            {
              "bIsCommander": false,
              "level": 0,
              "skillLevel": 0,
              "foilLevel": 0
            },
            {
              "itemId": "8b26fd42-f98d-4663-bb11-3c4831c43007",
              "templateId": "Character:Warrior_VR1_Light_Deflect_T05",
              "bIsCommander": false,
              "level": 150,
              "skillLevel": 20,
              "upgrades": [
                95,
                95,
                95,
                95,
                34,
                150,
                6,
                0,
                0
              ],
              "accountInfo": {
                "level": 887,
                "perks": [
                  20,
                  130,
                  776,
                  324,
                  18,
                  0,
                  0,
                  69
                ]
              },
              "foilLevel": 1,
              "gearTemplateId": "Character:Warrior_SR1_Light_AxeToss_T06"
            }
          ]
        }
      ]
    }
  ],
  "profileCommandRevision": 834,
  "serverTime": "2022-12-17T13:26:16.683Z",
  "multiUpdate": [
    {
      "profileRevision": 9832,
      "profileId": "friends",
      "profileChangesBaseRevision": 9830,
      "profileChanges": [],
      "profileCommandRevision": 8236
    }
  ],
  "responseVersion": 1
}
```

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
