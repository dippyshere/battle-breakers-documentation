# Timeline

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/calendar/v1/timeline*

___

## Request

```http
GET /wex/api/calendar/v1/timeline HTTP/1.1
```

### Request Headers

| Name                  | Value                                                                                                                 |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------|
| Host                  | wex-public-service-live-prod.ol.epicgames.com                                                                         |
| Accept                | \*/\*                                                                                                                 |
| Accept-Encoding       | deflate, gzip                                                                                                         |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-2250526540F7CC298312D6957B2C40BC                |
| User-Agent            | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit                                                      |
| Authorization         | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |
| Content-Length        | 0                                                                                                                     |

___

## Response

#### Status: 200 OK

### Response Headers

| Name                       | Value                                                                                                  |
|----------------------------|--------------------------------------------------------------------------------------------------------|
| Date                       | Thu, 29 Dec 2022 05:42:54 GMT                                                                          |
| Content-Type               | application/json                                                                                       |
| Transfer-Encoding          | chunked                                                                                                |
| X-EpicGames-McpVersion     | prod Release-1.88-1.88 build 107 cl 19310354                                                           |
| X-EpicGames-ContentVersion | 1.88.244-r17036752                                                                                     |
| X-EpicGames-MinBuild       | 17036752                                                                                               |
| X-Epic-Correlation-ID      | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-2250526540F7CC298312D6957B2C40BC |
| Connection                 | keep-alive                                                                                             |

### Response Body

```json
{
  "channels": {
    "news": {
      "states": [
        {
          "validFrom": "2022-12-29T05:20:12.857Z",
          "activeEvents": [],
          "state": {}
        }
      ],
      "cacheExpire": "2022-12-29T07:20:12.857Z"
    },
    "limited-time-mode": {
      "states": [
        {
          "validFrom": "2022-12-29T05:20:12.857Z",
          "activeEvents": [],
          "state": {
            "activeLTMs": [
              {
                "LTM_Event_ID": "Week1_LTM",
                "LTM_ID": "Endless_01",
                "PlayMode": {
                  "Mode": "DeepDungeons",
                  "Rules": [
                    {
                      "Rule": "AllBosses",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "StrongSpecial",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "InsightHeroBonus",
                      "RuleDataValue": 0
                    }
                  ],
                  "Zones": [
                    {
                      "ZoneId": "Zone.HauntedWoods.Map1",
                      "Difficulty": "Easy",
                      "completionLoot": "LTG.LTM.Endless.Completion.VeryLow"
                    },
                    {
                      "ZoneId": "Zone.EndlessDesert.Map2",
                      "Difficulty": "Easy",
                      "firstCompletionLoot": "LTG.LTM.Battlepass5_Week1.FirstCompletion",
                      "completionLoot": "LTG.LTM.Battlepass5_Week1.Endless.Low.Gear"
                    },
                    {
                      "ZoneId": "Zone.CollapsedSpire.Map3",
                      "Difficulty": "Easy",
                      "completionLoot": "LTG.LTM.Endless.Completion.Low"
                    },
                    {
                      "ZoneId": "Zone.BlessedPlains.Map1",
                      "Difficulty": "Easy",
                      "firstCompletionLoot": "LTG.LTM.Battlepass5_Week1.FirstCompletion",
                      "completionLoot": "LTG.LTM.Battlepass5_Week1.Endless.Low.Gear"
                    },
                    {
                      "ZoneId": "Zone.OasisOfLife.Map3",
                      "Difficulty": "Medium",
                      "completionLoot": "LTG.LTM.Endless.Completion.Medium"
                    },
                    {
                      "ZoneId": "Zone.MoltenCaverns.Map1",
                      "Difficulty": "Medium",
                      "firstCompletionLoot": "LTG.LTM.Battlepass5_Week1.FirstCompletion",
                      "completionLoot": "LTG.LTM.Battlepass5_Week1.Endless.Medium.Gear"
                    },
                    {
                      "ZoneId": "Zone.LeafyTreeland.Map5",
                      "Difficulty": "Hard",
                      "completionLoot": "LTG.LTM.Endless.Completion.High"
                    },
                    {
                      "ZoneId": "Zone.BurnyVolcano.Map2",
                      "Difficulty": "Hard",
                      "firstCompletionLoot": "LTG.LTM.Battlepass5_Week1.FirstCompletion",
                      "completionLoot": "LTG.LTM.Battlepass5_Week1.Endless.High.Gear"
                    },
                    {
                      "ZoneId": "Zone.FieldsOfDespair.Map1",
                      "Difficulty": "Nightmare",
                      "completionLoot": "LTG.LTM.Endless.Completion.VeryHigh"
                    },
                    {
                      "ZoneId": "Zone.AbyssalPrecipice.Map1",
                      "Difficulty": "Nightmare",
                      "firstCompletionLoot": "LTG.LTM.Battlepass5_Week1.FirstCompletion",
                      "completionLoot": "LTG.LTM.Battlepass5_Week1.Endless.VeryHigh.Gear"
                    }
                  ],
                  "ModeDataValue": 0,
                  "ImageIndex": 151
                },
                "modeNamedWeight": "Modes_Weekly",
                "ruleNamedWeights": [
                  "Rules_AllBosses",
                  "Rules_StrongSpecial",
                  "Rules_InsightHeroBonus"
                ],
                "availabilityBegin": "2022-12-28T00:00:00.000Z",
                "availabilityEnd": "2023-01-04T00:00:00.000Z"
              },
              {
                "LTM_Event_ID": "Week1_LTM",
                "LTM_ID": "TimeAttack_01",
                "PlayMode": {
                  "Mode": "TimeAttack",
                  "Rules": [
                    {
                      "Rule": "InsightHeroBonus",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "MightyMinions",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "AgilityHeroBonus",
                      "RuleDataValue": 0
                    }
                  ],
                  "Zones": [
                    {
                      "ZoneId": "Zone.BurnyVolcano.Map1",
                      "Difficulty": "Nightmare",
                      "firstCompletionLoot": "LTG.LTM.Battlepass5_Week1.FirstCompletion",
                      "completionLoot": "LTG.LTM.Battlepass5_Week1.Completion",
                      "playBonusLoot": "LTG.LTM.TimeAttack.Completion.Bonus"
                    }
                  ],
                  "ModeDataValue": 70,
                  "ImageIndex": 58
                },
                "modeNamedWeight": "Modes_DuelsDoubleCommander",
                "ruleNamedWeights": [
                  "Rules_InsightHeroBonus",
                  "Rules_MightyMinions",
                  "Rules_AgilityHeroBonus"
                ],
                "availabilityBegin": "2022-12-28T00:00:00.000Z",
                "availabilityEnd": "2023-01-04T00:00:00.000Z"
              },
              {
                "LTM_Event_ID": "Week1_LTM",
                "LTM_ID": "TurnAttack_01",
                "PlayMode": {
                  "Mode": "TurnAttack",
                  "Rules": [
                    {
                      "Rule": "FullClearRooms",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "EnduranceHeroBonus",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "StrengthHeroBonus",
                      "RuleDataValue": 0
                    }
                  ],
                  "Zones": [
                    {
                      "ZoneId": "Zone.HauntedWoods.Map3",
                      "Difficulty": "Nightmare",
                      "firstCompletionLoot": "LTG.LTM.Battlepass5_Week1.FirstCompletion",
                      "completionLoot": "LTG.LTM.Battlepass5_Week1.Completion"
                    }
                  ],
                  "ModeDataValue": 175,
                  "ImageIndex": 162
                },
                "modeNamedWeight": "Modes_Duels3v3",
                "ruleNamedWeights": [
                  "Rules_FullClearRooms",
                  "Rules_EnduranceHeroBonus",
                  "Rules_StrengthHeroBonus"
                ],
                "availabilityBegin": "2022-12-28T00:00:00.000Z",
                "availabilityEnd": "2023-01-04T00:00:00.000Z"
              },
              {
                "LTM_Event_ID": "Week1_LTM",
                "LTM_ID": "PvP_Duels",
                "PlayMode": {
                  "Mode": "PvP",
                  "Rules": [
                    {
                      "Rule": "AgilityHeroBonus",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "EnduranceHeroBonus",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "EnemyManaBonus",
                      "RuleDataValue": 0
                    }
                  ],
                  "Zones": [
                    {
                      "ZoneId": "Zone.Event.GrandArena.Aux.Battleford.Map1",
                      "Difficulty": "Easy",
                      "firstCompletionLoot": "LTG.LTM.PvP.FirstCompletion",
                      "completionLoot": "LTG.LTM.PvP.Completion"
                    }
                  ],
                  "ModeDataValue": 0,
                  "ImageIndex": 97
                },
                "ruleNamedWeights": [
                  "Rules_AgilityHeroBonus",
                  "Rules_EnduranceHeroBonus",
                  "Rules_EnemyManaBonus"
                ],
                "availabilityBegin": "2022-12-28T00:00:00.000Z",
                "availabilityEnd": "2023-01-04T00:00:00.000Z"
              },
              {
                "LTM_Event_ID": "Week1_LTM",
                "LTM_ID": "Campaign01",
                "PlayMode": {
                  "Mode": "Campaign01",
                  "Rules": [
                    {
                      "Rule": "EnemyManaBonus",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "StrongSpecial",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "FastCoolDown",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "BlockSummonPets",
                      "RuleDataValue": 0
                    }
                  ],
                  "Zones": [],
                  "ModeDataValue": 0,
                  "ImageIndex": 0
                },
                "modeNamedWeight": "Modes_Campaign",
                "ruleNamedWeights": [
                  "Rules_EnemyManaBonus",
                  "Rules_StrongSpecial",
                  "Rules_FastCoolDown",
                  "Rules_Pets_BlockSummon"
                ]
              },
              {
                "LTM_Event_ID": "Week1_LTM",
                "LTM_ID": "Campaign02",
                "PlayMode": {
                  "Mode": "Campaign02",
                  "Rules": [
                    {
                      "Rule": "AllBosses",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "StrongEnemyATK",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "StrongSpecial",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "ItemSlots",
                      "RuleDataValue": 0
                    }
                  ],
                  "Zones": [],
                  "ModeDataValue": 0,
                  "ImageIndex": 0
                },
                "modeNamedWeight": "Modes_Campaign",
                "ruleNamedWeights": [
                  "Rules_AllBosses",
                  "Rules_StrongEnemyATK",
                  "Rules_StrongSpecial",
                  "Rules_ItemSlots"
                ]
              },
              {
                "LTM_Event_ID": "Week1_LTM",
                "LTM_ID": "Campaign03",
                "PlayMode": {
                  "Mode": "Campaign03",
                  "Rules": [
                    {
                      "Rule": "ItemSlots",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "InsightHeroBonus",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "StrengthHeroBonus",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "FastCoolDown",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "EnemyManaBonus",
                      "RuleDataValue": 0
                    }
                  ],
                  "Zones": [],
                  "ModeDataValue": 0,
                  "ImageIndex": 0
                },
                "modeNamedWeight": "Modes_Campaign",
                "ruleNamedWeights": [
                  "Rules_ItemSlots",
                  "Rules_InsightHeroBonus",
                  "Rules_StrengthHeroBonus",
                  "Rules_FastCoolDown",
                  "Rules_EnemyManaBonus"
                ]
              },
              {
                "LTM_Event_ID": "Week1_LTM",
                "LTM_ID": "Campaign04",
                "PlayMode": {
                  "Mode": "Campaign04",
                  "Rules": [
                    {
                      "Rule": "StrengthHeroBonus",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "StrongSpecial",
                      "RuleDataValue": 0
                    }
                  ],
                  "Zones": [],
                  "ModeDataValue": 0,
                  "ImageIndex": 0
                },
                "modeNamedWeight": "Modes_Campaign",
                "ruleNamedWeights": [
                  "Rules_StrengthHeroBonus",
                  "Rules_StrongSpecial"
                ]
              },
              {
                "LTM_Event_ID": "Week1_LTM",
                "LTM_ID": "Campaign05",
                "PlayMode": {
                  "Mode": "Campaign05",
                  "Rules": [
                    {
                      "Rule": "AgilityHeroBonus",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "StrongEnemyATK",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "DoubleCommander",
                      "RuleDataValue": 0
                    }
                  ],
                  "Zones": [],
                  "ModeDataValue": 0,
                  "ImageIndex": 0
                },
                "modeNamedWeight": "Modes_Campaign",
                "ruleNamedWeights": [
                  "Rules_AgilityHeroBonus",
                  "Rules_StrongEnemyATK",
                  "Rules_Commander_Double"
                ]
              },
              {
                "LTM_Event_ID": "Week1_LTM",
                "LTM_ID": "Campaign06",
                "PlayMode": {
                  "Mode": "Campaign06",
                  "Rules": [
                    {
                      "Rule": "StrongEnemyATK",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "FastCoolDown",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "StrengthHeroBonus",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "ItemSlots",
                      "RuleDataValue": 0
                    }
                  ],
                  "Zones": [],
                  "ModeDataValue": 0,
                  "ImageIndex": 0
                },
                "modeNamedWeight": "Modes_Campaign",
                "ruleNamedWeights": [
                  "Rules_StrongEnemyATK",
                  "Rules_FastCoolDown",
                  "Rules_StrengthHeroBonus",
                  "Rules_ItemSlots"
                ]
              },
              {
                "LTM_Event_ID": "Week1_LTM",
                "LTM_ID": "Campaign07",
                "PlayMode": {
                  "Mode": "Campaign07",
                  "Rules": [
                    {
                      "Rule": "MightyMinions",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "FullClearRooms",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "ItemSlots",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "EnduranceHeroBonus",
                      "RuleDataValue": 0
                    }
                  ],
                  "Zones": [],
                  "ModeDataValue": 0,
                  "ImageIndex": 0
                },
                "modeNamedWeight": "Modes_Campaign",
                "ruleNamedWeights": [
                  "Rules_MightyMinions",
                  "Rules_FullClearRooms",
                  "Rules_ItemSlots",
                  "Rules_EnduranceHeroBonus"
                ]
              },
              {
                "LTM_Event_ID": "Week1_LTM",
                "LTM_ID": "Campaign08",
                "PlayMode": {
                  "Mode": "Campaign08",
                  "Rules": [
                    {
                      "Rule": "ItemSlots",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "EnemyManaBonus",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "AgilityHeroBonus",
                      "RuleDataValue": 0
                    }
                  ],
                  "Zones": [],
                  "ModeDataValue": 0,
                  "ImageIndex": 0
                },
                "modeNamedWeight": "Modes_Campaign",
                "ruleNamedWeights": [
                  "Rules_ItemSlots",
                  "Rules_EnemyManaBonus",
                  "Rules_AgilityHeroBonus"
                ]
              },
              {
                "LTM_Event_ID": "Week1_LTM",
                "LTM_ID": "Campaign09",
                "PlayMode": {
                  "Mode": "Campaign09",
                  "Rules": [
                    {
                      "Rule": "StrongSpecial",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "StrongEnemyATK",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "MightyMinions",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "DoubleCommander",
                      "RuleDataValue": 0
                    }
                  ],
                  "Zones": [],
                  "ModeDataValue": 0,
                  "ImageIndex": 0
                },
                "modeNamedWeight": "Modes_Campaign",
                "ruleNamedWeights": [
                  "Rules_StrongSpecial",
                  "Rules_StrongEnemyATK",
                  "Rules_MightyMinions",
                  "Rules_Commander_Double"
                ]
              },
              {
                "LTM_Event_ID": "Week1_LTM",
                "LTM_ID": "Campaign10",
                "PlayMode": {
                  "Mode": "Campaign10",
                  "Rules": [
                    {
                      "Rule": "StrengthHeroBonus",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "StrongSpecial",
                      "RuleDataValue": 0
                    }
                  ],
                  "Zones": [],
                  "ModeDataValue": 0,
                  "ImageIndex": 0
                },
                "modeNamedWeight": "Modes_Campaign",
                "ruleNamedWeights": [
                  "Rules_StrengthHeroBonus",
                  "Rules_StrongSpecial"
                ]
              },
              {
                "LTM_Event_ID": "Week1_LTM",
                "LTM_ID": "Campaign11",
                "PlayMode": {
                  "Mode": "Campaign11",
                  "Rules": [
                    {
                      "Rule": "ItemSlots",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "AgilityHeroBonus",
                      "RuleDataValue": 0
                    }
                  ],
                  "Zones": [],
                  "ModeDataValue": 0,
                  "ImageIndex": 0
                },
                "modeNamedWeight": "Modes_Campaign",
                "ruleNamedWeights": [
                  "Rules_ItemSlots",
                  "Rules_AgilityHeroBonus"
                ]
              },
              {
                "LTM_Event_ID": "Week1_LTM",
                "LTM_ID": "Campaign12",
                "PlayMode": {
                  "Mode": "Campaign12",
                  "Rules": [
                    {
                      "Rule": "MightyMinions",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "AgilityHeroBonus",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "StrongEnemyATK",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "ItemSlots",
                      "RuleDataValue": 0
                    }
                  ],
                  "Zones": [],
                  "ModeDataValue": 0,
                  "ImageIndex": 0
                },
                "modeNamedWeight": "Modes_Campaign",
                "ruleNamedWeights": [
                  "Rules_MightyMinions",
                  "Rules_AgilityHeroBonus",
                  "Rules_StrongEnemyATK",
                  "Rules_ItemSlots"
                ]
              },
              {
                "LTM_Event_ID": "Week1_LTM",
                "LTM_ID": "Campaign13",
                "PlayMode": {
                  "Mode": "Campaign13",
                  "Rules": [
                    {
                      "Rule": "StrongEnemyATK",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "ItemSlots",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "AllBosses",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "EnemyManaBonus",
                      "RuleDataValue": 0
                    }
                  ],
                  "Zones": [],
                  "ModeDataValue": 0,
                  "ImageIndex": 0
                },
                "modeNamedWeight": "Modes_Campaign",
                "ruleNamedWeights": [
                  "Rules_StrongEnemyATK",
                  "Rules_ItemSlots",
                  "Rules_AllBosses",
                  "Rules_EnemyManaBonus"
                ]
              },
              {
                "LTM_Event_ID": "Week1_LTM",
                "LTM_ID": "Campaign14",
                "PlayMode": {
                  "Mode": "Campaign14",
                  "Rules": [
                    {
                      "Rule": "StrongSpecial",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "StrongEnemyATK",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "FullClearRooms",
                      "RuleDataValue": 0
                    }
                  ],
                  "Zones": [],
                  "ModeDataValue": 0,
                  "ImageIndex": 0
                },
                "modeNamedWeight": "Modes_Campaign",
                "ruleNamedWeights": [
                  "Rules_StrongSpecial",
                  "Rules_StrongEnemyATK",
                  "Rules_FullClearRooms"
                ]
              },
              {
                "LTM_Event_ID": "Week1_LTM",
                "LTM_ID": "Campaign15",
                "PlayMode": {
                  "Mode": "Campaign15",
                  "Rules": [
                    {
                      "Rule": "EnemyManaBonus",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "StrengthHeroBonus",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "AllBosses",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "StrongEnemyATK",
                      "RuleDataValue": 0
                    }
                  ],
                  "Zones": [],
                  "ModeDataValue": 0,
                  "ImageIndex": 0
                },
                "modeNamedWeight": "Modes_Campaign",
                "ruleNamedWeights": [
                  "Rules_EnemyManaBonus",
                  "Rules_StrengthHeroBonus",
                  "Rules_AllBosses",
                  "Rules_StrongEnemyATK"
                ]
              },
              {
                "LTM_Event_ID": "Week1_LTM",
                "LTM_ID": "Campaign16",
                "PlayMode": {
                  "Mode": "Campaign16",
                  "Rules": [
                    {
                      "Rule": "EnemyManaBonus",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "ItemSlots",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "EnduranceHeroBonus",
                      "RuleDataValue": 0
                    }
                  ],
                  "Zones": [],
                  "ModeDataValue": 0,
                  "ImageIndex": 0
                },
                "modeNamedWeight": "Modes_Campaign",
                "ruleNamedWeights": [
                  "Rules_EnemyManaBonus",
                  "Rules_ItemSlots",
                  "Rules_EnduranceHeroBonus"
                ]
              },
              {
                "LTM_Event_ID": "Week1_LTM",
                "LTM_ID": "Campaign17",
                "PlayMode": {
                  "Mode": "Campaign17",
                  "Rules": [
                    {
                      "Rule": "EnduranceHeroBonus",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "MightyMinions",
                      "RuleDataValue": 0
                    }
                  ],
                  "Zones": [],
                  "ModeDataValue": 0,
                  "ImageIndex": 0
                },
                "modeNamedWeight": "Modes_Campaign",
                "ruleNamedWeights": [
                  "Rules_EnduranceHeroBonus",
                  "Rules_MightyMinions"
                ]
              },
              {
                "LTM_Event_ID": "Week1_LTM",
                "LTM_ID": "Campaign18",
                "PlayMode": {
                  "Mode": "Campaign18",
                  "Rules": [
                    {
                      "Rule": "ItemSlots",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "EnemyManaBonus",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "DoubleCommander",
                      "RuleDataValue": 0
                    }
                  ],
                  "Zones": [],
                  "ModeDataValue": 0,
                  "ImageIndex": 0
                },
                "modeNamedWeight": "Modes_Campaign",
                "ruleNamedWeights": [
                  "Rules_ItemSlots",
                  "Rules_EnemyManaBonus",
                  "Rules_Commander_Double"
                ]
              },
              {
                "LTM_Event_ID": "Week1_LTM",
                "LTM_ID": "Campaign19",
                "PlayMode": {
                  "Mode": "Campaign19",
                  "Rules": [
                    {
                      "Rule": "ItemSlots",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "EnduranceHeroBonus",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "AllCommander",
                      "RuleDataValue": 0
                    }
                  ],
                  "Zones": [],
                  "ModeDataValue": 0,
                  "ImageIndex": 0
                },
                "modeNamedWeight": "Modes_Campaign",
                "ruleNamedWeights": [
                  "Rules_ItemSlots",
                  "Rules_EnduranceHeroBonus",
                  "Rules_Commander_All"
                ]
              },
              {
                "LTM_Event_ID": "Week1_LTM",
                "LTM_ID": "Campaign20",
                "PlayMode": {
                  "Mode": "Campaign20",
                  "Rules": [
                    {
                      "Rule": "FullClearRooms",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "EnemyManaBonus",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "FastCoolDown",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "MightyMinions",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "AllBosses",
                      "RuleDataValue": 0
                    }
                  ],
                  "Zones": [],
                  "ModeDataValue": 0,
                  "ImageIndex": 0
                },
                "modeNamedWeight": "Modes_Campaign",
                "ruleNamedWeights": [
                  "Rules_FullClearRooms",
                  "Rules_EnemyManaBonus",
                  "Rules_FastCoolDown",
                  "Rules_MightyMinions",
                  "Rules_AllBosses"
                ]
              },
              {
                "LTM_Event_ID": "Week1_LTM",
                "LTM_ID": "Campaign21",
                "PlayMode": {
                  "Mode": "Campaign21",
                  "Rules": [
                    {
                      "Rule": "FullClearRooms",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "ItemSlots",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "MightyMinions",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "AgilityHeroBonus",
                      "RuleDataValue": 0
                    }
                  ],
                  "Zones": [],
                  "ModeDataValue": 0,
                  "ImageIndex": 0
                },
                "modeNamedWeight": "Modes_Campaign",
                "ruleNamedWeights": [
                  "Rules_FullClearRooms",
                  "Rules_ItemSlots",
                  "Rules_MightyMinions",
                  "Rules_AgilityHeroBonus"
                ]
              },
              {
                "LTM_Event_ID": "Week1_LTM",
                "LTM_ID": "Campaign22",
                "PlayMode": {
                  "Mode": "Campaign22",
                  "Rules": [
                    {
                      "Rule": "FullClearRooms",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "StrongEnemyATK",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "MightyMinions",
                      "RuleDataValue": 0
                    },
                    {
                      "Rule": "FastCoolDown",
                      "RuleDataValue": 0
                    }
                  ],
                  "Zones": [],
                  "ModeDataValue": 0,
                  "ImageIndex": 0
                },
                "modeNamedWeight": "Modes_Campaign",
                "ruleNamedWeights": [
                  "Rules_FullClearRooms",
                  "Rules_StrongEnemyATK",
                  "Rules_MightyMinions",
                  "Rules_FastCoolDown"
                ]
              }
            ],
            "eventInstanceId": "$EVENT_INSTANCE_ID"
          }
        }
      ],
      "cacheExpire": "2022-12-29T07:20:12.857Z"
    },
    "marketing": {
      "states": [
        {
          "validFrom": "2022-12-29T05:20:12.857Z",
          "activeEvents": [],
          "state": {
            "affiliateSelectionEndDate": "0001-01-01T00:00:00.000Z"
          }
        }
      ],
      "cacheExpire": "2022-12-29T07:20:12.857Z"
    },
    "rotational-content": {
      "states": [
        {
          "validFrom": "2022-12-29T05:20:12.857Z",
          "activeEvents": [],
          "state": {
            "activeZones": [
              {
                "sortPriority": 800,
                "zoneId": "Zone.Event.GrandArena.Aux.Battleford.Map1",
                "maxRuns": -1,
                "resetCostMtx": 0,
                "flags": [
                  "IsSpecialEvent"
                ],
                "eventId": "Event.GrandArena",
                "dynamicTier": 1,
                "dynamicGoldTier": 1,
                "dynamicWorldLevel": -1,
                "expiresAt": "2026-01-01T00:00:00Z",
                "eventKey": "37m008vr790voua5ie1g0s0pqg[0]0+0"
              },
              {
                "sortPriority": 800,
                "zoneId": "Zone.Pvp.Sparring1.Map1",
                "maxRuns": -1,
                "resetCostMtx": 0,
                "flags": [
                  "IsSpecialEvent"
                ],
                "eventId": "Event.GrandArena",
                "dynamicTier": -1,
                "dynamicGoldTier": -1,
                "dynamicWorldLevel": -1,
                "expiresAt": "2026-01-01T00:00:00Z",
                "eventKey": "37m008vr790voua5ie1g0s0pqg[1]0+0"
              },
              {
                "sortPriority": -100,
                "zoneId": "Zone.Event.WK.TKVoucher1.Light.Map1",
                "maxRuns": 8,
                "resetCostMtx": 500,
                "flags": [],
                "dynamicTier": -1,
                "dynamicGoldTier": -1,
                "dynamicWorldLevel": -1,
                "expiresAt": "2022-12-31T00:00:00Z",
                "eventKey": "021lv6t1k5dmuuokgcr3cr1m0s[0]199+0"
              },
              {
                "sortPriority": 0,
                "zoneId": "Zone.HallsOfFadedGlory.MapLight1",
                "maxRuns": 1,
                "resetCostMtx": 0,
                "flags": [],
                "dynamicTier": -1,
                "dynamicGoldTier": -1,
                "dynamicWorldLevel": -1,
                "expiresAt": "2022-12-30T00:00:00Z",
                "eventKey": "4gc32rhoebpb4e0onuplqopgjt[0]173+0"
              },
              {
                "sortPriority": 0,
                "zoneId": "Zone.HallsOfFadedGlory.MapGold1",
                "maxRuns": 1,
                "resetCostMtx": 0,
                "flags": [],
                "dynamicTier": 1,
                "dynamicGoldTier": 3,
                "dynamicWorldLevel": -1,
                "expiresAt": "2022-12-30T00:00:00Z",
                "eventKey": "6tojdi2dqvmqbeo0st5bvr919m[0]998+0"
              }
            ],
            "activeEvents": [
              {
                "sortPriority": 999,
                "eventAsset": "/Game/Campaign/Zones/Events/Evergreen5/EventDef_Evergreen5.EventDef_Evergreen5",
                "eventId": "Evergreen5",
                "expiresAt": "2023-01-28T00:00:00Z"
              }
            ],
            "preregRewardZones": [],
            "heroStoreEnd": "2023-01-02T00:00:00.000Z",
            "purchasingEventId": "Event.Evergreen5"
          }
        }
      ],
      "cacheExpire": "2022-12-29T07:20:12.857Z"
    },
    "featured-stores-mcp": {
      "states": [
        {
          "validFrom": "2022-12-29T05:20:12.857Z",
          "activeEvents": [],
          "state": {
            "activePurchaseLimitingEventIds": [],
            "storefront": {}
          }
        }
      ],
      "cacheExpire": "2022-12-29T07:20:12.857Z"
    },
    "weekly-challenge": {
      "states": [
        {
          "validFrom": "2022-12-29T05:20:12.857Z",
          "activeEvents": [],
          "state": {
            "phases": [
              {
                "zoneId": "Zone.Event.WC.Daily.BossTrio.Map1",
                "availabilityBegin": "2022-12-26T00:00:00.000Z",
                "availabilityEnd": "2023-01-02T00:00:00.000Z",
                "minAccountLevel": 1,
                "maxAccountLevel": 2147483647,
                "requirements": {
                  "maxPartySize": 5,
                  "minPartySize": 1,
                  "requirements": [
                    {
                      "count": 1,
                      "heroClass": "Archer",
                      "heroElement": "None"
                    }
                  ],
                  "excludeClasses": [],
                  "excludeElements": []
                }
              },
              {
                "zoneId": "Zone.Event.WC.Daily.SuperBoss.Map1",
                "availabilityBegin": "2022-12-26T00:00:00.000Z",
                "availabilityEnd": "2023-01-02T00:00:00.000Z",
                "minAccountLevel": 1,
                "maxAccountLevel": 2147483647,
                "requirements": {
                  "maxPartySize": 5,
                  "minPartySize": 1,
                  "requirements": [
                    {
                      "count": 1,
                      "heroClass": "Ninja",
                      "heroElement": "None"
                    },
                    {
                      "count": 1,
                      "heroClass": "AnyClass",
                      "heroElement": "Dark"
                    }
                  ],
                  "excludeClasses": [],
                  "excludeElements": []
                }
              },
              {
                "zoneId": "Zone.Event.WC.Daily.BossTrio.Map1",
                "availabilityBegin": "2022-12-26T00:00:00.000Z",
                "availabilityEnd": "2023-01-02T00:00:00.000Z",
                "minAccountLevel": 1,
                "maxAccountLevel": 2147483647,
                "requirements": {
                  "maxPartySize": 5,
                  "minPartySize": 1,
                  "requirements": [
                    {
                      "count": 1,
                      "heroClass": "AnyClass",
                      "heroElement": "Dark"
                    }
                  ],
                  "excludeClasses": [],
                  "excludeElements": []
                }
              },
              {
                "zoneId": "Zone.Event.WC.Daily.BossTrio.Map1",
                "availabilityBegin": "2022-12-26T00:00:00.000Z",
                "availabilityEnd": "2023-01-02T00:00:00.000Z",
                "minAccountLevel": 1,
                "maxAccountLevel": 2147483647,
                "requirements": {
                  "maxPartySize": 5,
                  "minPartySize": 1,
                  "requirements": [
                    {
                      "count": 1,
                      "heroClass": "Archer",
                      "heroElement": "None"
                    }
                  ],
                  "excludeClasses": [],
                  "excludeElements": []
                }
              },
              {
                "zoneId": "Zone.Event.WC.Daily.SuperBoss.Map1",
                "availabilityBegin": "2022-12-26T00:00:00.000Z",
                "availabilityEnd": "2023-01-02T00:00:00.000Z",
                "minAccountLevel": 1,
                "maxAccountLevel": 2147483647,
                "requirements": {
                  "maxPartySize": 5,
                  "minPartySize": 1,
                  "requirements": [
                    {
                      "count": 2,
                      "heroClass": "AnyClass",
                      "heroElement": "Dark"
                    }
                  ],
                  "excludeClasses": [],
                  "excludeElements": []
                }
              }
            ],
            "activePhases": [
              "Weekend",
              "Monday",
              "Tuesday",
              "Wednesday",
              "Thursday",
              "Friday"
            ],
            "eventInstanceId": "70ruue8l0oma4lm9egb3o9koga[0]158",
            "bossZone": {
              "zoneId": "Zone.Event.WC.Weekend.BossSuper.1.Blackguard.Map1",
              "availabilityBegin": "2022-12-26T00:00:00.000Z",
              "availabilityEnd": "2023-01-02T00:00:00.000Z",
              "minAccountLevel": 1,
              "maxAccountLevel": 2147483647,
              "runLimit": 1
            },
            "namedWeights": "Blackguard=1"
          }
        }
      ],
      "cacheExpire": "2022-12-29T07:20:12.857Z"
    },
    "battlepass": {
      "states": [
        {
          "validFrom": "2022-12-29T05:20:12.857Z",
          "activeEvents": [],
          "state": {
            "seasonId": "Evergreen5",
            "seasonEndDate": "2023-01-28T00:00:00Z"
          }
        }
      ],
      "cacheExpire": "2022-12-29T07:20:12.857Z"
    }
  },
  "cacheIntervalMins": 15.0,
  "currentTime": "2022-12-29T05:42:54.945Z"
}
```

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
