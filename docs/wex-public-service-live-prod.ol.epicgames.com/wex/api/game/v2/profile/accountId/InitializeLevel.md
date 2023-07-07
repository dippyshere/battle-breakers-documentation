# Initialize Level

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/:accountId/InitializeLevel?profileId=levels&rvn=29643*

___

## Request

```http
POST /wex/api/game/v2/profile/:accountId/InitializeLevel?profileId=levels&rvn=29643 HTTP/1.1
```

### Path Parameters

| Name     | Value                             |
|----------|-----------------------------------|
| acountId | ec0ebb7e56f6454e86c62299a7b32e21  |

### Query String

| Name      | Value  |
|-----------|--------|
| profileId | levels |
| rvn       | 29643  |

### Request Headers

| Name                         | Value                                                                                                                                                                                                                                                                              |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Host                         | wex-public-service-live-prod.ol.epicgames.com                                                                                                                                                                                                                                      |
| Accept-Encoding              | deflate, gzip                                                                                                                                                                                                                                                                      |
| Accept                       | \*/\*                                                                                                                                                                                                                                                                              |
| Content-Type                 | application/json                                                                                                                                                                                                                                                                   |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":24142},{"profileId":"levels","clientCommandRevision":14478},{"profileId":"friends","clientCommandRevision":8264},{"profileId":"monsterpit","clientCommandRevision":1081},{"profileId":"multiplayer","clientCommandRevision":900}] |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-458F23FB45529989FC24EA84C117DC35                                                                                                                                                                             |
| User-Agent                   | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit                                                                                                                                                                                                                   |
| Authorization                | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md)                                                                                                                                                              |
| Content-Length               | 781                                                                                                                                                                                                                                                                                |

### Request Body

```json
{
  "manifestVersion": "1.88.244-r17036752",
  "levelId": "Level.BurnyVolcano.Map1.D4",
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
      "heroItemId": "f01dfe95-6a2c-4a18-a3d9-19709c5f7de1"
    },
    {
      "heroType": "LocalHero",
      "heroItemId": "0cb63754-8755-47cd-96ad-c2d8df596735"
    }
  ],
  "friendInstanceId": "",
  "ltmId": "TimeAttack_01",
  "normalMode": true,
  "blitzMode": false,
  "teamPower": 364155
}
```

___

## Response

#### Status: 200 OK

### Response Headers

| Name                         | Value                                                                                                  |
|------------------------------|--------------------------------------------------------------------------------------------------------|
| Date                         | Thu, 29 Dec 2022 05:54:05 GMT                                                                          |
| Content-Type                 | application/json                                                                                       |
| Transfer-Encoding            | chunked                                                                                                |
| X-EpicGames-McpVersion       | prod Release-1.88-1.88 build 107 cl 19310354                                                           |
| X-EpicGames-ContentVersion   | 1.88.244-r17036752                                                                                     |
| X-EpicGames-MinBuild         | 17036752                                                                                               |
| X-EpicGames-Profile-Revision | 29643                                                                                                  |
| X-Epic-Device-ID             | 68009daed09498667a8039cce09983ed                                                                       |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-458F23FB45529989FC24EA84C117DC35 |
| Connection                   | keep-alive                                                                                             |

### Response Body

```json
{
  "profileRevision": 29645,
  "profileId": "levels",
  "profileChangesBaseRevision": 29643,
  "profileChanges": [
    {
      "changeType": "itemAdded",
      "itemId": "8f690514-530b-4075-83aa-bb1fac447650",
      "item": {
        "templateId": "Level:InProgress",
        "attributes": {
          "debug_name": ""
        },
        "quantity": 1
      }
    }
  ],
  "notifications": [
    {
      "type": "WExpLevelCreated",
      "primary": false,
      "level": {
        "potentialBattlepassXp": 450,
        "levelItemId": "8f690514-530b-4075-83aa-bb1fac447650",
        "rooms": [
          {
            "roomName": "Room.Treasure.FullClear.R01",
            "regionName": "Level.BurnyVolcano.Map1.D4",
            "depth": 1,
            "worldLevel": 231,
            "discoveryGoldMult": 24.0,
            "occupants": [
              {
                "isFriendly": false,
                "killXp": 0,
                "lootTemplateId": "StandIn:AccountXp",
                "lootQuantity": 30
              },
              {
                "isFriendly": false,
                "killXp": 0,
                "lootTemplateId": "Currency:Gold",
                "lootQuantity": 768
              },
              {
                "isFriendly": false,
                "killXp": 0,
                "lootTemplateId": "Currency:Gold",
                "lootQuantity": 936
              },
              {
                "isFriendly": false,
                "killXp": 0,
                "lootTemplateId": "StandIn:AccountXp",
                "lootQuantity": 60
              },
              {
                "isFriendly": false,
                "killXp": 0,
                "lootTemplateId": "Item:HealthVial",
                "lootQuantity": 1
              },
              {
                "isFriendly": false,
                "killXp": 0,
                "lootTemplateId": "Item:LinkAttackScroll",
                "lootQuantity": 1
              },
              {
                "isFriendly": false,
                "killXp": 0,
                "lootTemplateId": "Currency:Gold",
                "lootQuantity": 8496
              },
              {
                "isFriendly": false,
                "characterTemplateId": "Character:Shrine_ResurrectionPool",
                "killXp": 0,
                "spawnClass": "Normal",
                "lootQuantity": 0
              }
            ]
          },
          {
            "roomName": "Room.Boss.FindKeyAndExit.R01",
            "regionName": "Level.BurnyVolcano.Map1.D4",
            "depth": 2,
            "worldLevel": 231,
            "discoveryGoldMult": 6.0,
            "occupants": [
              {
                "isFriendly": false,
                "characterTemplateId": "Character:Archer_UC1_Fire_ElementalBreath_T04",
                "spawnGroup": [
                  {
                    "isFriendly": false,
                    "characterTemplateId": "Character:Archer_UC1_Fire_ElementalBreath_T03",
                    "killXp": 120,
                    "spawnClass": "BossMedium",
                    "lootTemplateId": "Currency:HeroXp_Basic",
                    "lootQuantity": 3076
                  },
                  {
                    "isFriendly": false,
                    "characterTemplateId": "Character:Cleric_UC1_Light_Heal_T03",
                    "killXp": 120,
                    "spawnClass": "BossMedium",
                    "lootTemplateId": "Currency:HeroXp_Basic",
                    "lootQuantity": 2843
                  }
                ],
                "killXp": 160,
                "spawnClass": "BossMedium",
                "lootTemplateId": "Currency:HeroXp_Basic",
                "lootQuantity": 3546
              },
              {
                "isFriendly": false,
                "characterTemplateId": "Character:Knight_UC1_Fire_Reconstruction_T03",
                "spawnGroup": [
                  {
                    "isFriendly": false,
                    "characterTemplateId": "Character:Mage_Basic_Fire_EnergyBlast_T02",
                    "killXp": 20,
                    "spawnClass": "Normal",
                    "lootTemplateId": "Currency:Gold",
                    "lootQuantity": 48
                  }
                ],
                "killXp": 30,
                "spawnClass": "Normal",
                "lootQuantity": 0
              },
              {
                "isFriendly": false,
                "characterTemplateId": "Character:Mage_Basic_Fire_EnergyBlast_T03",
                "spawnGroup": [],
                "killXp": 30,
                "spawnClass": "Normal",
                "lootQuantity": 0
              },
              {
                "isFriendly": false,
                "characterTemplateId": "Character:Ninja_UC1_Fire_SwiftStrike_T03",
                "spawnGroup": [
                  {
                    "isFriendly": false,
                    "characterTemplateId": "Character:MartialArtist_UC1_Fire_ChargedFist_T03",
                    "killXp": 30,
                    "spawnClass": "Normal",
                    "lootQuantity": 0
                  }
                ],
                "killXp": 30,
                "spawnClass": "Normal",
                "lootQuantity": 0
              },
              {
                "isFriendly": false,
                "killXp": 0,
                "lootTemplateId": "StandIn:AccountXp",
                "lootQuantity": 30
              },
              {
                "isFriendly": false,
                "killXp": 0,
                "lootTemplateId": "StandIn:AccountXp",
                "lootQuantity": 30
              },
              {
                "isFriendly": false,
                "killXp": 0,
                "lootTemplateId": "StandIn:AccountXp",
                "lootQuantity": 50
              },
              {
                "isFriendly": false,
                "killXp": 0,
                "lootTemplateId": "StandIn:AccountXp",
                "lootQuantity": 50
              },
              {
                "isFriendly": false,
                "characterTemplateId": "Character:Shrine_Strength",
                "killXp": 0,
                "spawnClass": "Normal",
                "lootQuantity": 0
              }
            ]
          },
          {
            "roomName": "Room.Boss.KillBosses.R02",
            "regionName": "Level.BurnyVolcano.Map1.D4",
            "depth": 3,
            "worldLevel": 231,
            "discoveryGoldMult": 6.0,
            "occupants": [
              {
                "isFriendly": false,
                "characterTemplateId": "Character:Ninja_UC1_Fire_SwiftStrike_T03",
                "spawnGroup": [
                  {
                    "isFriendly": false,
                    "characterTemplateId": "Character:Ninja_Basic_Fire_Flurry_T02",
                    "killXp": 80,
                    "spawnClass": "BossMedium",
                    "lootTemplateId": "Currency:Gold",
                    "lootQuantity": 48
                  },
                  {
                    "isFriendly": false,
                    "characterTemplateId": "Character:Knight_Basic_Fire_GuardianStance_T02",
                    "killXp": 80,
                    "spawnClass": "BossMedium",
                    "lootQuantity": 0
                  }
                ],
                "killXp": 120,
                "spawnClass": "BossMedium",
                "lootTemplateId": "Currency:HeroXp_Basic",
                "lootQuantity": 3236
              },
              {
                "isFriendly": false,
                "characterTemplateId": "Character:Warrior_UC1_Light_Pummel_T03",
                "spawnGroup": [],
                "killXp": 30,
                "spawnClass": "Normal",
                "lootTemplateId": "Currency:HeroXp_Basic",
                "lootQuantity": 1860
              },
              {
                "isFriendly": false,
                "characterTemplateId": "Character:Knight_UC1_Fire_Reconstruction_T03",
                "spawnGroup": [
                  {
                    "isFriendly": false,
                    "characterTemplateId": "Character:MartialArtist_UC1_Fire_ChargedFist_T03",
                    "killXp": 30,
                    "spawnClass": "Normal",
                    "lootTemplateId": "Currency:Gold",
                    "lootQuantity": 198
                  }
                ],
                "killXp": 30,
                "spawnClass": "Normal",
                "lootTemplateId": "Currency:Gold",
                "lootQuantity": 96
              },
              {
                "isFriendly": false,
                "killXp": 0,
                "lootTemplateId": "StandIn:AccountXp",
                "lootQuantity": 20
              },
              {
                "isFriendly": false,
                "killXp": 0,
                "lootTemplateId": "StandIn:AccountXp",
                "lootQuantity": 30
              },
              {
                "isFriendly": false,
                "killXp": 0,
                "lootTemplateId": "Item:HealthVial",
                "lootQuantity": 1
              },
              {
                "isFriendly": false,
                "killXp": 0,
                "lootTemplateId": "Currency:Gold",
                "lootQuantity": 264
              },
              {
                "isFriendly": false,
                "characterTemplateId": "Character:Assassin_C1_Fire_ImpStab_T01",
                "spawnGroup": [
                  {
                    "isFriendly": false,
                    "characterTemplateId": "Character:Assassin_C1_Fire_ImpStab_T01",
                    "killXp": 10,
                    "spawnClass": "Normal",
                    "lootTemplateId": "Currency:Gold",
                    "lootQuantity": 48
                  }
                ],
                "killXp": 10,
                "spawnClass": "Normal",
                "lootQuantity": 0
              }
            ]
          },
          {
            "roomName": "Room.Standard.FullClear.Hard.R03",
            "regionName": "Level.BurnyVolcano.Map1.D4",
            "depth": 4,
            "worldLevel": 231,
            "discoveryGoldMult": 6.0,
            "occupants": [
              {
                "isFriendly": false,
                "characterTemplateId": "Character:Warrior_UC1_Fire_Pummel_T03",
                "spawnGroup": [],
                "killXp": 30,
                "spawnClass": "Normal",
                "lootQuantity": 0
              },
              {
                "isFriendly": false,
                "characterTemplateId": "Character:Ninja_Basic_Fire_Flurry_T03",
                "spawnGroup": [],
                "killXp": 30,
                "spawnClass": "Normal",
                "lootTemplateId": "Currency:Gold",
                "lootQuantity": 54
              },
              {
                "isFriendly": false,
                "characterTemplateId": "Character:Archer_UC1_Fire_ElementalBreath_T04",
                "spawnGroup": [
                  {
                    "isFriendly": false,
                    "characterTemplateId": "Character:AI_PoisonTank_Fire_T04",
                    "killXp": 60,
                    "spawnClass": "Normal",
                    "lootTemplateId": "Currency:Gold",
                    "lootQuantity": 264
                  },
                  {
                    "isFriendly": false,
                    "characterTemplateId": "Character:Cleric_UC1_Light_Heal_T03",
                    "killXp": 30,
                    "spawnClass": "Normal",
                    "lootTemplateId": "Currency:HeroXp_Basic",
                    "lootQuantity": 1989
                  }
                ],
                "killXp": 40,
                "spawnClass": "Normal",
                "lootTemplateId": "Currency:Gold",
                "lootQuantity": 204
              },
              {
                "isFriendly": false,
                "characterTemplateId": "Character:Ninja_R2_Fire_TripleStab_T04",
                "spawnGroup": [
                  {
                    "isFriendly": false,
                    "characterTemplateId": "Character:Cleric_UC1_Light_Heal_T03",
                    "killXp": 30,
                    "spawnClass": "Normal",
                    "lootQuantity": 0
                  },
                  {
                    "isFriendly": false,
                    "characterTemplateId": "Character:Knight_Basic_Light_GuardianStance_T03",
                    "killXp": 30,
                    "spawnClass": "Normal",
                    "lootTemplateId": "Currency:Gold",
                    "lootQuantity": 54
                  }
                ],
                "killXp": 40,
                "spawnClass": "Normal",
                "lootQuantity": 0
              },
              {
                "isFriendly": false,
                "killXp": 0,
                "lootTemplateId": "StandIn:AccountXp",
                "lootQuantity": 20
              },
              {
                "isFriendly": false,
                "killXp": 0,
                "lootTemplateId": "StandIn:AccountXp",
                "lootQuantity": 10
              },
              {
                "isFriendly": false,
                "killXp": 0,
                "lootTemplateId": "Item:ManaVial",
                "lootQuantity": 1
              },
              {
                "isFriendly": false,
                "killXp": 0,
                "lootTemplateId": "StandIn:AccountXp",
                "lootQuantity": 40
              },
              {
                "isFriendly": false,
                "characterTemplateId": "Character:Assassin_C1_Fire_ImpStab_T01",
                "spawnGroup": [
                  {
                    "isFriendly": false,
                    "characterTemplateId": "Character:Assassin_C1_Fire_ImpStab_T01",
                    "killXp": 10,
                    "spawnClass": "Normal",
                    "lootQuantity": 0
                  }
                ],
                "killXp": 10,
                "spawnClass": "Normal",
                "lootQuantity": 0
              }
            ]
          },
          {
            "roomName": "Room.Treasure.FullClear.Side.R01",
            "regionName": "Level.BurnyVolcano.Map1.D4",
            "depth": 4,
            "worldLevel": 231,
            "discoveryGoldMult": 24.0,
            "occupants": [
              {
                "isFriendly": false,
                "killXp": 0,
                "lootTemplateId": "Container:Chest_Fire_VeryHigh",
                "lootQuantity": 1
              },
              {
                "isFriendly": false,
                "killXp": 0,
                "lootTemplateId": "Currency:Gold",
                "lootQuantity": 1056
              },
              {
                "isFriendly": false,
                "killXp": 0,
                "lootTemplateId": "StandIn:AccountXp",
                "lootQuantity": 65
              },
              {
                "isFriendly": false,
                "killXp": 0,
                "lootTemplateId": "Currency:Gold",
                "lootQuantity": 864
              },
              {
                "isFriendly": false,
                "killXp": 0,
                "lootTemplateId": "StandIn:AccountXp",
                "lootQuantity": 117
              },
              {
                "isFriendly": false,
                "killXp": 0,
                "lootTemplateId": "Item:HealthVial",
                "lootQuantity": 1
              },
              {
                "isFriendly": false,
                "killXp": 0,
                "lootTemplateId": "Item:HealthVial",
                "lootQuantity": 1
              },
              {
                "isFriendly": false,
                "killXp": 0,
                "lootTemplateId": "Currency:Gold",
                "lootQuantity": 5328
              },
              {
                "isFriendly": false,
                "killXp": 0,
                "lootTemplateId": "Currency:Gold",
                "lootQuantity": 2352
              }
            ]
          },
          {
            "roomName": "Room.Boss.Reveal.Duo.Mix.KillAllEnemies.R02",
            "regionName": "Level.BurnyVolcano.Map1.D4",
            "depth": 5,
            "worldLevel": 231,
            "discoveryGoldMult": 6.0,
            "occupants": [
              {
                "isFriendly": false,
                "characterTemplateId": "Character:Knight_UC1_Fire_Reconstruction_T03",
                "spawnGroup": [],
                "killXp": 30,
                "spawnClass": "Normal",
                "lootTemplateId": "Currency:Gold",
                "lootQuantity": 54
              },
              {
                "isFriendly": false,
                "characterTemplateId": "Character:Shadowknight_UC2_Fire_Ghoul_T03",
                "spawnGroup": [
                  {
                    "isFriendly": false,
                    "characterTemplateId": "Character:Cleric_UC1_Light_Heal_T03",
                    "killXp": 30,
                    "spawnClass": "Normal",
                    "lootQuantity": 0
                  }
                ],
                "killXp": 30,
                "spawnClass": "Normal",
                "lootQuantity": 0
              },
              {
                "isFriendly": false,
                "characterTemplateId": "Character:Archer_UC1_Light_ElementalBreath_T03",
                "spawnGroup": [
                  {
                    "isFriendly": false,
                    "characterTemplateId": "Character:Archer_Basic_Light_AimedShot_T02",
                    "killXp": 20,
                    "spawnClass": "Normal",
                    "lootTemplateId": "Currency:Gold",
                    "lootQuantity": 96
                  },
                  {
                    "isFriendly": false,
                    "characterTemplateId": "Character:Warrior_Basic_Fire_T02",
                    "killXp": 20,
                    "spawnClass": "Normal",
                    "lootQuantity": 0
                  },
                  {
                    "isFriendly": false,
                    "characterTemplateId": "Character:Ninja_Basic_Light_Flurry_T02",
                    "killXp": 20,
                    "spawnClass": "Normal",
                    "lootQuantity": 0
                  }
                ],
                "killXp": 30,
                "spawnClass": "Normal",
                "lootQuantity": 0
              },
              {
                "isFriendly": false,
                "characterTemplateId": "Character:Warrior_UC1_Fire_LesserDemon_T03",
                "spawnGroup": [
                  {
                    "isFriendly": false,
                    "characterTemplateId": "Character:Ninja_Basic_Fire_Flurry_T02",
                    "killXp": 20,
                    "spawnClass": "Normal",
                    "lootQuantity": 0
                  }
                ],
                "killXp": 30,
                "spawnClass": "Normal",
                "lootQuantity": 0
              },
              {
                "isFriendly": false,
                "characterTemplateId": "Character:Mage_UC1_Fire_ElementalPhantom_T03",
                "spawnGroup": [
                  {
                    "isFriendly": false,
                    "characterTemplateId": "Character:Knight_Basic_Fire_GuardianStance_T02",
                    "killXp": 20,
                    "spawnClass": "Normal",
                    "lootQuantity": 0
                  }
                ],
                "killXp": 30,
                "spawnClass": "Normal",
                "lootQuantity": 0
              },
              {
                "isFriendly": false,
                "characterTemplateId": "Character:Ninja_Basic_Fire_Flurry_T03",
                "spawnGroup": [],
                "killXp": 30,
                "spawnClass": "Normal",
                "lootQuantity": 0
              },
              {
                "isFriendly": false,
                "characterTemplateId": "Character:Ninja_UC1_Light_SwiftStrike_T03",
                "spawnGroup": [
                  {
                    "isFriendly": false,
                    "characterTemplateId": "Character:Mage_Basic_Fire_EnergyBlast_T02",
                    "killXp": 20,
                    "spawnClass": "Normal",
                    "lootQuantity": 0
                  },
                  {
                    "isFriendly": false,
                    "characterTemplateId": "Character:Mage_Basic_Fire_EnergyBlast_T02",
                    "killXp": 20,
                    "spawnClass": "Normal",
                    "lootQuantity": 0
                  }
                ],
                "killXp": 30,
                "spawnClass": "Normal",
                "lootQuantity": 0
              },
              {
                "isFriendly": false,
                "characterTemplateId": "Character:Ninja_Basic_Fire_Flurry_T03",
                "spawnGroup": [],
                "killXp": 30,
                "spawnClass": "Normal",
                "lootQuantity": 0
              },
              {
                "isFriendly": false,
                "characterTemplateId": "Character:HolyKnight_VR1_Fire_FireSword_T05",
                "spawnGroup": [
                  {
                    "isFriendly": false,
                    "characterTemplateId": "Character:Cleric_UC1_Light_Heal_T04",
                    "killXp": 160,
                    "spawnClass": "BossMedium",
                    "lootTemplateId": "Currency:Gold",
                    "lootQuantity": 222
                  }
                ],
                "killXp": 200,
                "spawnClass": "BossMedium",
                "lootTemplateId": "Currency:Gold",
                "lootQuantity": 480
              },
              {
                "isFriendly": false,
                "characterTemplateId": "Character:AI_Summoner_Fire_T04",
                "spawnGroup": [
                  {
                    "isFriendly": false,
                    "characterTemplateId": "Character:AI_Exploder_Fire_T04",
                    "killXp": 160,
                    "spawnClass": "BossMedium",
                    "lootTemplateId": "Container:Chest_Fire_High",
                    "lootQuantity": 1
                  }
                ],
                "killXp": 160,
                "spawnClass": "BossMedium",
                "lootTemplateId": "Container:Chest_Fire_High",
                "lootQuantity": 1
              },
              {
                "isFriendly": false,
                "killXp": 0,
                "lootTemplateId": "StandIn:AccountXp",
                "lootQuantity": 30
              },
              {
                "isFriendly": false,
                "killXp": 0,
                "lootTemplateId": "StandIn:AccountXp",
                "lootQuantity": 20
              },
              {
                "isFriendly": false,
                "killXp": 0,
                "lootTemplateId": "StandIn:AccountXp",
                "lootQuantity": 50
              },
              {
                "isFriendly": false,
                "killXp": 0,
                "lootTemplateId": "StandIn:AccountXp",
                "lootQuantity": 50
              },
              {
                "isFriendly": false,
                "characterTemplateId": "Character:AI_Tower_Fire_Buff_T03",
                "killXp": 30,
                "spawnClass": "Normal",
                "lootQuantity": 0
              }
            ]
          }
        ],
        "levelId": "Level.BurnyVolcano.Map1.D4"
      },
      "heroInfo": [
        {
          "itemId": "73bc3aeb-a61e-4a87-8c47-93190c8cf727",
          "templateId": "Character:Warrior_VR2_Dark_Rampage_T06",
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
            46,
            2
          ],
          "accountInfo": {
            "level": 373,
            "perks": [
              6,
              133,
              209,
              97,
              6,
              12,
              12,
              13
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
          "itemId": "dab75d65-7911-4f7b-8cc9-88790171650d",
          "templateId": "Character:TreasureHunter_VR2_Fire_AntiMaterialCharge_T06",
          "bIsCommander": false,
          "level": 150,
          "skillLevel": 20,
          "upgrades": [
            95,
            95,
            95,
            95,
            34,
            129,
            5,
            55,
            3
          ],
          "accountInfo": {
            "level": 373,
            "perks": [
              6,
              133,
              209,
              97,
              6,
              12,
              12,
              13
            ]
          },
          "foilLevel": -1,
          "gearTemplateId": "Character:TreasureHunter_R2_Fire_PowerEfflux_T03"
        },
        {
          "itemId": "2dbc336a-554b-449c-ae84-b4697bb00119",
          "templateId": "Character:Ninja_VR1_Light_CrystalDaggers_T06",
          "bIsCommander": false,
          "level": 150,
          "skillLevel": 20,
          "upgrades": [
            95,
            95,
            95,
            95,
            34,
            101,
            4,
            65,
            3
          ],
          "accountInfo": {
            "level": 373,
            "perks": [
              6,
              133,
              209,
              97,
              6,
              12,
              12,
              13
            ]
          },
          "foilLevel": 1,
          "gearTemplateId": "Character:Mage_R2_Light_Cloudburst_T03"
        },
        {
          "itemId": "f01dfe95-6a2c-4a18-a3d9-19709c5f7de1",
          "templateId": "Character:Archer_VR2_Nature_GoinCommando_T06",
          "bIsCommander": false,
          "level": 150,
          "skillLevel": 20,
          "upgrades": [
            95,
            95,
            95,
            95,
            34,
            75,
            3,
            65,
            3
          ],
          "accountInfo": {
            "level": 373,
            "perks": [
              6,
              133,
              209,
              97,
              6,
              12,
              12,
              13
            ]
          },
          "foilLevel": -1,
          "gearTemplateId": "Character:Archer_VR1_Dark_BarbedArrows_T04"
        },
        {
          "itemId": "0cb63754-8755-47cd-96ad-c2d8df596735",
          "templateId": "Character:TreasureHunter_VR1_Fire_TrailBlaze_T04",
          "bIsCommander": false,
          "level": 120,
          "skillLevel": 1,
          "upgrades": [
            25,
            25,
            25,
            25,
            4,
            10,
            0,
            0,
            0
          ],
          "accountInfo": {
            "level": 373,
            "perks": [
              6,
              133,
              209,
              97,
              6,
              12,
              12,
              13
            ]
          },
          "foilLevel": -1,
          "gearTemplateId": ""
        }
      ]
    }
  ],
  "profileCommandRevision": 14479,
  "serverTime": "2022-12-29T05:54:05.833Z",
  "multiUpdate": [
    {
      "profileRevision": 40457,
      "profileId": "profile0",
      "profileChangesBaseRevision": 40455,
      "profileChanges": [
        {
          "changeType": "itemQuantityChanged",
          "itemId": "492bb23f-74bf-42bb-a5b5-5ee27deb6169",
          "quantity": 296
        },
        {
          "changeType": "statModified",
          "name": "activity",
          "value": {
            "a": {
              "date": "2022-12-28T00:00:00.000Z",
              "claimed": true,
              "props": {
                "HeroAcquired": 137,
                "HeroPromote": 1,
                "HeroEvolve": 1,
                "MonsterPitLevelUp": 1,
                "HeroFoil": 1,
                "AccountLevelUp": 2,
                "BaseBonus": 10,
                "EnergySpent": 187
              }
            },
            "b": {
              "date": "2022-12-29T00:00:00.000Z",
              "claimed": false,
              "props": {
                "BaseBonus": 10,
                "EnergySpent": 4
              }
            },
            "standardGift": 10
          }
        }
      ],
      "profileCommandRevision": 24143
    }
  ],
  "responseVersion": 1
}
```

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
