# FinalizeLevel

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/FinalizeLevel?profileId=levels&rvn=29645*



___

## Request

```http request
POST /wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/FinalizeLevel?profileId=levels&rvn=29645 HTTP/1.1
```

### Query String

| Name | Value |
|---|---|
| profileId | levels |
| rvn | 29645 |




### Request Headers

| Name | Value |
|---|---|
| Host | wex-public-service-live-prod.ol.epicgames.com |
| Accept-Encoding | deflate, gzip |
| Accept | \*/\* |
| Content-Type | application/json |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":24143},{"profileId":"levels","clientCommandRevision":14479},{"profileId":"friends","clientCommandRevision":8264},{"profileId":"monsterpit","clientCommandRevision":1081},{"profileId":"multiplayer","clientCommandRevision":900}] |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-21148B4747F7F5E27BF6B39F9138F5B4 |
| User-Agent | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit |
| Authorization | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |
| Content-Length | 4344 |


### Request Body

```json
{
  "levelItemId": "8f690514-530b-4075-83aa-bb1fac447650",
  "levelElement": "Fire",
  "claimDepth": 5,
  "claimedItems": [
    {
      "itemTemplateId": "Currency:Gold",
      "quantity": 27744
    },
    {
      "itemTemplateId": "StandIn:AccountXp",
      "quantity": 1670
    },
    {
      "itemTemplateId": "Container:Chest_Fire_VeryHigh",
      "quantity": 1
    },
    {
      "itemTemplateId": "Container:Chest_Fire_High",
      "quantity": 1
    }
  ],
  "seenCharacters": [],
  "postBattleResults": {
    "defeatedEnemyMap": {
      "Fire": 31,
      "Light": 12,
      "Boss": 4
    },
    "uniqueHeroesDefeated": [
      "f01dfe95-6a2c-4a18-a3d9-19709c5f7de1",
      "0cb63754-8755-47cd-96ad-c2d8df596735"
    ],
    "uniqueEnemiesDefeated": [
      "Character:Knight_UC1_Fire_Reconstruction_T03:RoomDepth=1 Slot=23 SideRoom=0",
      "Character:Mage_Basic_Fire_EnergyBlast_T03:RoomDepth=1 Slot=33 SideRoom=0",
      "Character:Cleric_UC1_Light_Heal_T03:RoomDepth=1 Slot=23 SideRoom=0",
      "Character:Assassin_C1_Light_ImpStab_T01:RoomDepth=1 Slot=30 SideRoom=0",
      "Character:Assassin_C1_Fire_ImpStab_T01:RoomDepth=1 Slot=32 SideRoom=0",
      "Character:Archer_UC1_Fire_ElementalBreath_T03:RoomDepth=1 Slot=16 SideRoom=0",
      "Character:Archer_UC1_Fire_ElementalBreath_T04:RoomDepth=1 Slot=17 SideRoom=0",
      "Character:Assassin_C1_Fire_ImpStab_T01:RoomDepth=1 Slot=31 SideRoom=0",
      "Character:MartialArtist_UC1_Fire_ChargedFist_T03:RoomDepth=1 Slot=38 SideRoom=0",
      "Character:Ninja_UC1_Fire_SwiftStrike_T03:RoomDepth=1 Slot=45 SideRoom=0",
      "Character:Knight_UC1_Fire_Reconstruction_T03:RoomDepth=2 Slot=16 SideRoom=0",
      "Character:Ninja_Basic_Fire_Flurry_T02:RoomDepth=2 Slot=16 SideRoom=0",
      "Character:Ninja_UC1_Fire_SwiftStrike_T03:RoomDepth=2 Slot=22 SideRoom=0",
      "Character:Warrior_UC1_Light_Pummel_T03:RoomDepth=2 Slot=37 SideRoom=0",
      "Character:Assassin_C1_Light_ImpStab_T01:RoomDepth=2 Slot=38 SideRoom=0",
      "Character:Assassin_C1_Fire_ImpStab_T01:RoomDepth=2 Slot=40 SideRoom=0",
      "Character:Assassin_C1_Fire_ImpStab_T01:RoomDepth=2 Slot=39 SideRoom=0",
      "Character:Warrior_UC1_Fire_Pummel_T03:RoomDepth=3 Slot=15 SideRoom=0",
      "Character:Assassin_C1_Fire_ImpStab_T01:RoomDepth=3 Slot=18 SideRoom=0",
      "Character:Assassin_C1_Light_ImpStab_T01:RoomDepth=3 Slot=22 SideRoom=0",
      "Character:AI_PoisonTank_Fire_T04:RoomDepth=3 Slot=23 SideRoom=0",
      "Character:Archer_UC1_Fire_ElementalBreath_T04:RoomDepth=3 Slot=31 SideRoom=0",
      "Character:Cleric_UC1_Light_Heal_T03:RoomDepth=3 Slot=15 SideRoom=0",
      "Character:Cleric_UC1_Light_Heal_T03:RoomDepth=3 Slot=31 SideRoom=0",
      "Character:Ninja_R2_Fire_TripleStab_T04:RoomDepth=3 Slot=39 SideRoom=0",
      "Character:Knight_Basic_Light_GuardianStance_T03:RoomDepth=3 Slot=23 SideRoom=0",
      "Character:Assassin_C1_Light_ImpStab_T01:RoomDepth=3 Slot=15 SideRoom=0",
      "Character:Assassin_C1_Fire_ImpStab_T01:RoomDepth=3 Slot=22 SideRoom=0",
      "Character:Assassin_C1_Fire_ImpStab_T01:RoomDepth=3 Slot=30 SideRoom=0",
      "Character:Ninja_Basic_Fire_Flurry_T03:RoomDepth=3 Slot=37 SideRoom=0",
      "Character:Assassin_C1_Fire_ImpStab_T01:RoomDepth=3 Slot=45 SideRoom=0",
      "Character:Ninja_UC1_Light_SwiftStrike_T03:RoomDepth=4 Slot=18 SideRoom=0",
      "Character:Archer_UC1_Light_ElementalBreath_T03:RoomDepth=4 Slot=25 SideRoom=0",
      "Character:Knight_UC1_Fire_Reconstruction_T03:RoomDepth=4 Slot=33 SideRoom=0",
      "Character:Ninja_Basic_Fire_Flurry_T03:RoomDepth=4 Slot=41 SideRoom=0",
      "Character:Shadowknight_UC2_Fire_Ghoul_T03:RoomDepth=4 Slot=38 SideRoom=0",
      "Character:Ninja_Basic_Fire_Flurry_T03:RoomDepth=4 Slot=45 SideRoom=0",
      "Character:Warrior_UC1_Fire_LesserDemon_T03:RoomDepth=4 Slot=26 SideRoom=0",
      "Character:Mage_UC1_Fire_ElementalPhantom_T03:RoomDepth=4 Slot=37 SideRoom=0",
      "Character:AI_Summoner_Fire_T04:RoomDepth=4 Slot=16 SideRoom=0",
      "Character:AI_Tower_Fire_Buff_T03:RoomDepth=4 Slot=46 SideRoom=0",
      "Character:HolyKnight_VR1_Fire_FireSword_T05:RoomDepth=4 Slot=31 SideRoom=0"
    ]
  },
  "battleMetaData": "Bs/hcVp66gAA0DUVTSkEFgAtNET3wn8gtfSwTsRs4CkB40fASmQQAQ2AsshTe9mPawb3dOGEOABdgEFqHbaLlJ2mr7jBy9Pc5e73AB8dFCssNRNLUFtmaWVeTpaXtLi3vdvN2+Pv9/w1xQInLjU6RmNRXmh0eaLMV460o6rCyfHd5+76AhpD3DUpJE1IVnBjb3d4jqBqYQ==",
  "dailyQuestZoneType": 0,
  "partyItemId": "7fb2db84",
  "bShouldGiveBonus": false
}
```

___

## Response

#### Status: 200 OK




### Response Headers

| Name | Value |
|---|---|
| Date | Thu, 29 Dec 2022 05:56:43 GMT |
| Content-Type | application/json |
| Content-Length | 6448 |
| X-EpicGames-Profile-Revision | 29645 |
| X-EpicGames-McpVersion | prod Release-1.88-1.88 build 107 cl 19310354 |
| X-EpicGames-ContentVersion | 1.88.244-r17036752 |
| X-EpicGames-MinBuild | 17036752 |
| X-Epic-Device-ID | 68009daed09498667a8039cce09983ed |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-21148B4747F7F5E27BF6B39F9138F5B4 |
| Connection | keep-alive |


### Response Body

```json
{
  "profileRevision": 29647,
  "profileId": "levels",
  "profileChangesBaseRevision": 29645,
  "profileChanges": [
    {
      "changeType": "statModified",
      "name": "limited_time_mode",
      "value": {
        "eventInstanceId": "Week1_LTM",
        "levelProgressMap": {
          "TimeAttack_01": {
            "ltm_id": "TimeAttack_01",
            "level_index": 0
          },
          "Campaign21": {
            "ltm_id": "Campaign21",
            "level_index": 0
          },
          "Endless_01": {
            "ltm_id": "Endless_01",
            "level_index": 9
          },
          "PvP_Duels": {
            "ltm_id": "PvP_Duels",
            "level_index": 0
          },
          "Campaign01": {
            "ltm_id": "Campaign01",
            "level_index": 0
          }
        }
      }
    },
    {
      "changeType": "itemRemoved",
      "itemId": "8f690514-530b-4075-83aa-bb1fac447650"
    },
    {
      "changeType": "statModified",
      "name": "last_played_level",
      "value": "Level.BurnyVolcano.Map1.D4"
    }
  ],
  "notifications": [
    {
      "type": "WExpLevelCompleted",
      "primary": false,
      "accountXp": 3340,
      "bonusAccountXp": 0,
      "levelId": "Level.BurnyVolcano.Map1.D4",
      "completed": true,
      "loot": [
        {
          "tierGroupName": "Container:Chest_Fire_VeryHigh",
          "items": [
            {
              "itemType": "Currency:HeroXp_Basic",
              "itemGuid": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
              "itemProfile": "profile0",
              "quantity": 15740
            }
          ]
        },
        {
          "tierGroupName": "Container:Chest_Fire_High",
          "items": [
            {
              "itemType": "Currency:HeroXp_Basic",
              "itemGuid": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
              "itemProfile": "profile0",
              "quantity": 8457
            }
          ]
        },
        {
          "tierGroupName": "",
          "items": [
            {
              "itemType": "Currency:Gold",
              "itemGuid": "daa87593-4b4a-4ffa-a21d-8979d6eb38ed",
              "itemProfile": "profile0",
              "quantity": 27744
            }
          ]
        },
        {
          "tierGroupName": "Level.FirstInstance",
          "items": [
            {
              "itemType": "Reagent:Reagent_Shard_Gear",
              "itemGuid": "59dae826-9491-4a3d-8dae-23708d4220a7",
              "itemProfile": "profile0",
              "quantity": 3
            },
            {
              "itemType": "Gear:GD_Armor_TechRobes_Light",
              "itemGuid": "8c4f6e6c-31bc-4b36-b259-99f032b0a940",
              "itemProfile": "profile0",
              "quantity": 1
            }
          ]
        },
        {
          "tierGroupName": "Level.Instance",
          "items": [
            {
              "itemType": "Currency:Gold",
              "itemGuid": "daa87593-4b4a-4ffa-a21d-8979d6eb38ed",
              "itemProfile": "profile0",
              "quantity": 100000
            },
            {
              "itemType": "Currency:Gold",
              "itemGuid": "daa87593-4b4a-4ffa-a21d-8979d6eb38ed",
              "itemProfile": "profile0",
              "quantity": 100000
            },
            {
              "itemType": "Currency:HeroXp_Basic",
              "itemGuid": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
              "itemProfile": "profile0",
              "quantity": 1000
            },
            {
              "itemType": "Currency:SkillXP",
              "itemGuid": "9aec267c-4ab3-451f-8762-2dfc405de2a0",
              "itemProfile": "profile0",
              "quantity": 100
            },
            {
              "itemType": "Reagent:Reagent_Shard_Light",
              "itemGuid": "1b148e65-99c0-4eb8-a99d-7377f537276e",
              "itemProfile": "profile0",
              "quantity": 1
            },
            {
              "itemType": "Reagent:Reagent_Event_Evergreen5",
              "itemGuid": "fbbadeb5-fa02-4182-9e61-2c2368dd1bae",
              "itemProfile": "profile0",
              "quantity": 1000
            },
            {
              "itemType": "Voucher:Voucher_HeroSilver_Fire",
              "itemGuid": "1a5fa559-329d-4e83-98f7-03ae6877bcda",
              "itemProfile": "profile0",
              "quantity": 1
            },
            {
              "itemType": "Gear:GD_Weapon_Avenger_Light",
              "itemGuid": "fd5a7a38-3aee-4ca9-9454-4d097c5eab51",
              "itemProfile": "profile0",
              "quantity": 1
            }
          ]
        },
        {
          "tierGroupName": "Level.EventsLoot",
          "items": [
            {
              "itemType": "Reagent:Reagent_Event_Evergreen5",
              "itemGuid": "fbbadeb5-fa02-4182-9e61-2c2368dd1bae",
              "itemProfile": "profile0",
              "quantity": 450
            }
          ]
        }
      ]
    }
  ],
  "profileCommandRevision": 14480,
  "serverTime": "2022-12-29T05:56:43.259Z",
  "multiUpdate": [
    {
      "profileRevision": 40459,
      "profileId": "profile0",
      "profileChangesBaseRevision": 40457,
      "profileChanges": [
        {
          "changeType": "itemAttrChanged",
          "itemId": "492bb23f-74bf-42bb-a5b5-5ee27deb6169",
          "attributeName": "updated",
          "attributeValue": "2022-12-29T05:54:05.826Z"
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
                "EnergySpent": 8
              }
            },
            "standardGift": 10
          }
        },
        {
          "changeType": "statModified",
          "name": "hammer_quest_energy",
          "value": {
            "energy_spent": 6,
            "energy_required": 100,
            "claim_count": 0
          }
        },
        {
          "changeType": "statModified",
          "name": "xp",
          "value": 221029
        },
        {
          "changeType": "itemAttrChanged",
          "itemId": "0cb63754-8755-47cd-96ad-c2d8df596735",
          "attributeName": "skill_xp",
          "attributeValue": 5
        },
        {
          "changeType": "itemQuantityChanged",
          "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
          "quantity": 14751670
        },
        {
          "changeType": "itemQuantityChanged",
          "itemId": "daa87593-4b4a-4ffa-a21d-8979d6eb38ed",
          "quantity": 567300462
        },
        {
          "changeType": "itemQuantityChanged",
          "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
          "quantity": 14760127
        },
        {
          "changeType": "itemQuantityChanged",
          "itemId": "59dae826-9491-4a3d-8dae-23708d4220a7",
          "quantity": 110
        },
        {
          "changeType": "itemAdded",
          "itemId": "8c4f6e6c-31bc-4b36-b259-99f032b0a940",
          "item": {
            "templateId": "Gear:GD_Armor_TechRobes_Light",
            "attributes": {
              "is_new": false,
              "is_disabled": false,
              "hero_item_id": "",
              "extra_affixes": [
                "GearAffix:AD_Special_ReduceCooldown"
              ],
              "rarity": "Rare"
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemQuantityChanged",
          "itemId": "daa87593-4b4a-4ffa-a21d-8979d6eb38ed",
          "quantity": 567400462
        },
        {
          "changeType": "itemQuantityChanged",
          "itemId": "daa87593-4b4a-4ffa-a21d-8979d6eb38ed",
          "quantity": 567500462
        },
        {
          "changeType": "itemQuantityChanged",
          "itemId": "e8e1e6f0-606e-4f31-8214-bfcf80e2ab7d",
          "quantity": 14761127
        },
        {
          "changeType": "itemQuantityChanged",
          "itemId": "9aec267c-4ab3-451f-8762-2dfc405de2a0",
          "quantity": 195694
        },
        {
          "changeType": "itemQuantityChanged",
          "itemId": "1b148e65-99c0-4eb8-a99d-7377f537276e",
          "quantity": 351
        },
        {
          "changeType": "statModified",
          "name": "season_xp",
          "value": 23755
        },
        {
          "changeType": "itemQuantityChanged",
          "itemId": "fbbadeb5-fa02-4182-9e61-2c2368dd1bae",
          "quantity": 1027
        },
        {
          "changeType": "itemAdded",
          "itemId": "1a5fa559-329d-4e83-98f7-03ae6877bcda",
          "item": {
            "templateId": "Voucher:Voucher_HeroSilver_Fire",
            "attributes": {},
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "fd5a7a38-3aee-4ca9-9454-4d097c5eab51",
          "item": {
            "templateId": "Gear:GD_Weapon_Avenger_Light",
            "attributes": {
              "is_new": false,
              "is_disabled": false,
              "hero_item_id": "",
              "extra_affixes": [],
              "rarity": "Common"
            },
            "quantity": 1
          }
        },
        {
          "changeType": "statModified",
          "name": "season_xp",
          "value": 24205
        },
        {
          "changeType": "itemAttrChanged",
          "itemId": "a5145ec8-a445-445e-b11e-d1efc7119bb3",
          "attributeName": "level",
          "attributeValue": 6
        },
        {
          "changeType": "itemQuantityChanged",
          "itemId": "fbbadeb5-fa02-4182-9e61-2c2368dd1bae",
          "quantity": 1477
        },
        {
          "changeType": "itemAttrChanged",
          "itemId": "1c0122d5-3314-4260-aec2-44a4f8a92b2a",
          "attributeName": "score",
          "attributeValue": 18
        },
        {
          "changeType": "itemAttrChanged",
          "itemId": "a2bce9c2-fd38-44eb-a830-b270b5743a03",
          "attributeName": "score",
          "attributeValue": 10
        },
        {
          "changeType": "itemAttrChanged",
          "itemId": "2866efb0-7f20-463d-9b24-0bf2d437b9b9",
          "attributeName": "score",
          "attributeValue": 85
        }
      ],
      "profileCommandRevision": 24144
    }
  ],
  "responseVersion": 1
}
```

*Response body was encoded in base64*

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
