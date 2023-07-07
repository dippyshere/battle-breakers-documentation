# Query Profile (Profile0)

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/:accountId/QueryProfile?profileId=profile0&rvn=-1*

___

## Request

```http
POST /wex/api/game/v2/profile/:accountId/QueryProfile?profileId=profile0&rvn=-1 HTTP/1.1
```

### Path Parameters

| Name     | Value                             |
|----------|-----------------------------------|
| acountId | ec0ebb7e56f6454e86c62299a7b32e21  |

### Query String

| Name      | Value    |
|-----------|----------|
| profileId | profile0 |
| rvn       | -1       |

### Request Headers

| Name                         | Value                                                                                                                                                                                                                                                                   |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Host                         | wex-public-service-live-prod.ol.epicgames.com                                                                                                                                                                                                                           |
| Accept-Encoding              | deflate, gzip                                                                                                                                                                                                                                                           |
| Accept                       | \*/\*                                                                                                                                                                                                                                                                   |
| Content-Type                 | application/json                                                                                                                                                                                                                                                        |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":-1},{"profileId":"levels","clientCommandRevision":-1},{"profileId":"friends","clientCommandRevision":-1},{"profileId":"monsterpit","clientCommandRevision":-1},{"profileId":"multiplayer","clientCommandRevision":-1}] |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-0B7F237845879274156B60BDF32E84BB                                                                                                                                                                  |
| User-Agent                   | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit                                                                                                                                                                                                        |
| Authorization                | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md)                                                                                                                                                   |
| Content-Length               | 4                                                                                                                                                                                                                                                                       |

### Request Body

```json
{
  "profileRevision": 3,
  "profileId": "profile0",
  "profileChangesBaseRevision": 3,
  "profileChanges": [
    {
      "changeType": "fullProfileUpdate",
      "profile": {
        "_id": "8815cfb4e39d415c8c8196768f3edb37",
        "created": "2022-12-16T16:55:43.016Z",
        "updated": "2022-12-24T00:30:32.039Z",
        "rvn": 3,
        "wipeNumber": 4,
        "accountId": "d330e65d299748e9ad8c06a4a1fc3d85",
        "profileId": "profile0",
        "version": "initialize_season_end_date",
        "items": {
          "e9454156-680f-4276-8a37-9288f49c075d": {
            "templateId": "HqBuilding:HQ_Market",
            "attributes": {
              "level": 0
            },
            "quantity": 1
          },
          "b791d0a4-e834-44ea-991b-a3fa478c8ab4": {
            "templateId": "Currency:SB_Silver",
            "attributes": {},
            "quantity": 40000
          },
          "d10df50e-51a6-4f88-93b7-88a98105aa58": {
            "templateId": "Energy:PvP",
            "attributes": {
              "fatigue": 0,
              "updated": "2022-12-16T16:55:43.015Z",
              "charge_rate": 1,
              "max_value": 120
            },
            "quantity": 120
          },
          "57e14217-b662-4f07-bb68-3f4a35dff5c8": {
            "templateId": "Currency:SB_WS",
            "attributes": {},
            "quantity": 15000
          },
          "4e52c96d-1691-4afb-8cdb-358402160af1": {
            "templateId": "HqBuilding:HQ_SpiralTower",
            "attributes": {
              "level": 0
            },
            "quantity": 1
          },
          "fbb40e8d-7ca2-4d8c-94a3-946f7e4f6edc": {
            "templateId": "Currency:SB_Bronze",
            "attributes": {},
            "quantity": 80000
          },
          "2679b01f-5947-4da2-9697-b6d4e9a95c79": {
            "templateId": "HqBuilding:HQ_HeroTower_Elemental",
            "attributes": {
              "Normal_static_currency_amount": 100,
              "Special_static_reward_template_id": "Reagent:Reagent_HeroMap_SuperRare",
              "level": 0,
              "chest_options": [
                {
                  "heroChoicesDeprecated": [],
                  "itemChoices": [
                    "Character:Warrior_Starter_Fire_Berserking_T03",
                    "Character:Warrior_R2_Nature_Whirlwind_T03",
                    "Character:MartialArtist_R2_Water_Ironfist_T03"
                  ],
                  "itemQuantities": [
                    1,
                    1,
                    1
                  ],
                  "heroTrackId": "CoreBasic",
                  "foilLevel": 0
                }
              ],
              "Special_static_currency_template_id": "Reagent:Reagent_HeroMap_Elemental",
              "Special_static_currency_amount": 500,
              "Normal_static_reward_amount": 1,
              "Special_static_reward_amount": 5,
              "Normal_static_currency_template_id": "Reagent:Reagent_HeroMap_Elemental",
              "CoreBasic_progress": 0,
              "chest_info_content_version": "",
              "page_index": 0,
              "foil_lvl": -1,
              "Normal_static_reward_template_id": "Reagent:Reagent_HeroMap_SuperRare"
            },
            "quantity": 1
          },
          "621d6ee6-b4ca-4a24-94f7-359aac769e1d": {
            "templateId": "Giftbox:GB_AccountLevel01",
            "attributes": {
              "sealed_days": 0,
              "params": {},
              "min_level": 10
            },
            "quantity": 1
          },
          "10682228-fbaa-476a-b124-4466e334c431": {
            "templateId": "Energy:PvE",
            "attributes": {
              "fatigue": 0,
              "updated": "2022-12-16T16:55:43.015Z",
              "charge_rate": 30,
              "max_value": 300
            },
            "quantity": 300
          },
          "17ae727c-6625-471a-b811-91ecdc02fc48": {
            "templateId": "HqBuilding:HQ_HeroTower_Bronze",
            "attributes": {
              "Normal_static_currency_amount": 1,
              "Normal_static_currency_template_id": "Reagent:Reagent_HeroMap_Bronze",
              "chest_info_content_version": "",
              "level": 0,
              "chest_options": [
                {
                  "heroChoicesDeprecated": [
                    "Character:Archer_UC1_Fire_ElementalBreath_T03",
                    "Character:MartialArtist_UC1_Nature_ChargedFist_T03",
                    "Character:Knight_UC2_Water_SpearThrust_T03"
                  ],
                  "itemChoices": [],
                  "itemQuantities": [],
                  "heroTrackId": "CoreBronze",
                  "foilLevel": 0
                }
              ],
              "CoreBronze_progress": 0,
              "page_index": -1,
              "foil_lvl": -1,
              "Normal_static_reward_template_id": "",
              "Normal_static_reward_amount": 1
            },
            "quantity": 1
          },
          "687595c6-0bfb-4f28-9c51-4091a0785ff6": {
            "templateId": "HqBuilding:HQ_PlanarRifts",
            "attributes": {
              "level": 1
            },
            "quantity": 1
          },
          "73e51722-464b-46eb-b91c-0bab6890bc19": {
            "templateId": "MajorEventTracker:MajorEventTracker",
            "attributes": {
              "level": 0,
              "seasonId": "0",
              "totalLevels": 0,
              "xp": 0,
              "totalRuns": 0
            },
            "quantity": 1
          },
          "e4d82df5-e845-4b80-9014-2a875ebe5990": {
            "templateId": "HqBuilding:HQ_CrystalForge",
            "attributes": {
              "level": 0
            },
            "quantity": 1
          },
          "bf3f0e5e-9e26-4561-bbd8-26368181fd7b": {
            "templateId": "Currency:SB_Gold",
            "attributes": {},
            "quantity": 25000
          },
          "9600ab33-6fd3-46bf-8861-d15f517d9528": {
            "templateId": "MajorEventTracker:BattlepassSeason",
            "attributes": {
              "seasonId": "Battlepass4",
              "level": 0,
              "totalLevels": 0,
              "xp": 0,
              "totalRuns": 0
            },
            "quantity": 1
          },
          "a08fd8e7-c5d9-4fdf-b122-55abcd038ef9": {
            "templateId": "Currency:SB_LevelCompletion",
            "attributes": {},
            "quantity": 125000
          },
          "e1ec3219-a507-4868-b478-faf39b2ab727": {
            "templateId": "Currency:MtxGiveaway",
            "attributes": {},
            "quantity": 100
          },
          "cde63832-96e0-4d33-b6f2-fe76636fc717": {
            "templateId": "Currency:SB_Mine",
            "attributes": {},
            "quantity": 18000000
          },
          "04460f8d-51ef-40c1-9cb1-e45b7feec476": {
            "templateId": "HqBuilding:HQ_HeroTower_SuperRare",
            "attributes": {
              "Normal_static_currency_amount": 100,
              "Normal_static_currency_template_id": "Reagent:Reagent_HeroMap_SuperRare",
              "chest_info_content_version": "",
              "level": 0,
              "chest_options": [
                {
                  "heroChoicesDeprecated": [
                    "Character:Warmage_SR2_Fire_Shadowflame_T05",
                    "Character:MartialArtist_SR1_Dark_ExplodingPalm_T05",
                    "Character:DragonKnight_SR1_Water_JumpStrike_T05"
                  ],
                  "itemChoices": [],
                  "itemQuantities": [],
                  "heroTrackId": "CoreSuperRare",
                  "foilLevel": 0
                }
              ],
              "page_index": -1,
              "foil_lvl": -1,
              "Normal_static_reward_template_id": "",
              "CoreSuperRare_progress": 0,
              "Normal_static_reward_amount": 1
            },
            "quantity": 1
          },
          "7301d052-2d74-48a9-8526-81b151626311": {
            "templateId": "HqBuilding:HQ_AncientFactory",
            "attributes": {
              "level": 0
            },
            "quantity": 1
          },
          "7402b7d3-417d-4361-9878-e12ad13460fe": {
            "templateId": "Currency:SB_Platinum",
            "attributes": {},
            "quantity": 15000
          }
        },
        "stats": {
          "attributes": {
            "active_hammer_chest": "",
            "labor_force": {},
            "labor_refill_cd": "min",
            "affiliate_id": "",
            "normalized_name": "",
            "season_xp": 0,
            "mtx_purchase_history": {},
            "default_parties": {},
            "daily_purchases": {},
            "in_app_purchases": {
              "receipts": [],
              "packages": []
            },
            "current_battlepass": "Battlepass4",
            "hero_limit": 15,
            "is_pvp_unlocked": false,
            "days_since_started": 0,
            "mtx_level": 0,
            "level": 1,
            "battlepass_purchase_history": {},
            "current_major_event": "",
            "weekly_challenge_xp": 0,
            "starter_hero": "",
            "rep_hero_ids": [],
            "has_started": false,
            "display_name": "",
            "secret_shop_page": {
              "unlock_time": null,
              "page": 0
            },
            "store_level": 0,
            "market_page": {
              "unlock_time": null,
              "page": 0
            },
            "tracked_days_since_started": 0,
            "recent_party_id": "",
            "notification_optin_reward_claimed": false,
            "weapon_limit": 500,
            "starter_hero_template_id": "",
            "vip_level": 0,
            "event_purchases": {
              "event_id": "",
              "offers": {}
            },
            "account_perks": {},
            "hero_store_page": {
              "unlock_time": null,
              "page": 0
            },
            "activity": {
              "a": {
                "date": "2022-12-24T00:00:00.000Z",
                "claimed": false,
                "props": {
                  "BaseBonus": 10
                }
              },
              "standardGift": 10
            },
            "hammer_quest_energy": {
              "energy_spent": 0,
              "energy_required": 100,
              "claim_count": 0
            },
            "standard_gift": 10,
            "num_territories_claimed": 0,
            "daily_quest_last_refresh": "0021-12-01T21:12:00.000Z",
            "debug_ltm": "",
            "recovery_code": "987946",
            "has_external_account": false,
            "hammer_quest_realtime": {
              "next_claim": null,
              "claim_count": 0
            },
            "is_headless": true,
            "current_season_end_date": "2022-12-28T00:00:00.000Z",
            "max_rep_heroes": 1,
            "armor_limit": 500,
            "season_regular_claim_level": -1,
            "rewards_claimed": {},
            "last_reported_account_level_milestone": 0,
            "rocket_unlock": 0,
            "last_battlepass_purchased": "",
            "inventory_limit_bonus": 0,
            "weekly_purchases": {},
            "num_levels_completed": 0,
            "avatar_url": "wex-temp-avatar.png",
            "weekly_challenge_level": 0,
            "monthly_purchases": {},
            "xp": 0,
            "event_next_level": 0,
            "login_reward": {
              "last_claim_time": "2022-12-24T00:30:32.038Z",
              "next_level": 2
            },
            "season_premium_claim_level": -1,
            "come_back_reward_claimed": false,
            "is_developer": false
          }
        },
        "commandRevision": 2
      }
    }
  ],
  "profileCommandRevision": 2,
  "serverTime": "2022-12-24T00:50:48.771Z",
  "responseVersion": 1
}
```

___

## Response

#### Status: 200 OK

### Response Headers

| Name                         | Value                                                                                                  |
|------------------------------|--------------------------------------------------------------------------------------------------------|
| Date                         | Thu, 29 Dec 2022 05:43:02 GMT                                                                          |
| Content-Type                 | application/json                                                                                       |
| Transfer-Encoding            | chunked                                                                                                |
| X-EpicGames-Profile-Revision | 1884                                                                                                   |
| X-EpicGames-McpVersion       | prod Release-1.88-1.88 build 107 cl 19310354                                                           |
| X-EpicGames-ContentVersion   | 1.88.244-r17036752                                                                                     |
| X-EpicGames-MinBuild         | 17036752                                                                                               |
| X-Epic-Device-ID             | 68009daed09498667a8039cce09983ed                                                                       |
| X-Epic-Correlation-ID        | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-0B7F237845879274156B60BDF32E84BB |
| Connection                   | keep-alive                                                                                             |

### Response Body

```json

```

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
