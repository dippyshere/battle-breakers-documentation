# SelectStartOptions

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/SelectStartOptions?profileId=profile0&rvn=3*

___

## Request

```http request
POST /wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/SelectStartOptions?profileId=profile0&rvn=3 HTTP/1.1
```

### Query String

| Name | Value |
|---|---|
| profileId | profile0 |
| rvn | 3 |




### Request Headers

| Name | Value |
|---|---|
| Host | wex-public-service-live-prod.ol.epicgames.com |
| Accept-Encoding | deflate, gzip |
| Accept | \*/\* |
| Content-Type | application/json |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":2},{"profileId":"levels","clientCommandRevision":0},{"profileId":"friends","clientCommandRevision":0},{"profileId":"monsterpit","clientCommandRevision":0},{"profileId":"multiplayer","clientCommandRevision":0}] |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-A6F351B3452D40656B964A9D6327636F-8C48CEB741C1058B2C30C393FB76E4A7 |
| User-Agent | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit |
| Authorization | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |
| Content-Length | 127 |


### Request Body

```json
{
  "characterTemplateId": "Character:Mage_Starter_Fire_Fireball_T03",
  "displayName": "EpicName1",
  "affiliateId": ""
}
```

___

## Response

#### Status: 200 OK




### Response Headers

| Name | Value |
|---|---|
| Date | Thu, 29 Dec 2022 13:24:37 GMT |
| Content-Type | application/json |
| Transfer-Encoding | chunked |
| X-EpicGames-McpVersion | prod Release-1.88-1.88 build 107 cl 19310354 |
| X-EpicGames-ContentVersion | 1.88.244-r17036752 |
| X-EpicGames-MinBuild | 17036752 |
| X-EpicGames-Profile-Revision | 3 |
| X-Epic-Device-ID | 68009daed09498667a8039cce09983ed |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-A6F351B3452D40656B964A9D6327636F-8C48CEB741C1058B2C30C393FB76E4A7 |
| Connection | keep-alive |


### Response Body

```json
{
  "profileRevision": 5,
  "profileId": "profile0",
  "profileChangesBaseRevision": 3,
  "profileChanges": [
    {
      "changeType": "statModified",
      "name": "has_started",
      "value": true
    },
    {
      "changeType": "statModified",
      "name": "starter_hero",
      "value": "StarterFire"
    },
    {
      "changeType": "statModified",
      "name": "starter_hero_template_id",
      "value": "Character:Mage_Starter_Fire_Fireball_T03"
    },
    {
      "changeType": "itemAdded",
      "itemId": "0e263ef8-4b09-4630-8ff0-8b56ef4757cc",
      "item": {
        "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
        "attributes": {
          "gear_weapon_item_id": "",
          "weapon_unlocked": false,
          "sidekick_template_id": "",
          "is_new": false,
          "level": 1,
          "num_sold": 0,
          "skill_level": 1,
          "sidekick_unlocked": false,
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
          "used_as_sidekick": false,
          "gear_armor_item_id": "",
          "skill_xp": 0,
          "armor_unlocked": false,
          "foil_lvl": -1,
          "xp": 0,
          "rank": 0,
          "sidekick_item_id": ""
        },
        "quantity": 1
      }
    },
    {
      "changeType": "statModified",
      "name": "rep_hero_ids",
      "value": [
        "0e263ef8-4b09-4630-8ff0-8b56ef4757cc"
      ]
    },
    {
      "changeType": "itemAdded",
      "itemId": "f34e1909-b588-403a-9f07-bb692305f015",
      "item": {
        "templateId": "Party:Instance",
        "attributes": {
          "commander_index": 3,
          "date_created": "2022-12-29T13:24:37.239Z",
          "character_ids": [
            "",
            "",
            "",
            "0e263ef8-4b09-4630-8ff0-8b56ef4757cc",
            "",
            ""
          ],
          "friend_index": 5,
          "party_icon": "None"
        },
        "quantity": 1
      }
    },
    {
      "changeType": "statModified",
      "name": "default_parties",
      "value": {
        "LastPvePartyUsed": "f34e1909-b588-403a-9f07-bb692305f015"
      }
    },
    {
      "changeType": "itemAdded",
      "itemId": "7125b5e1-d07a-452c-81a7-ae10b8ee13e1",
      "item": {
        "templateId": "Party:Instance",
        "attributes": {
          "commander_index": 0,
          "date_created": "2022-12-29T13:24:37.239Z",
          "character_ids": [],
          "friend_index": 5,
          "party_icon": "None"
        },
        "quantity": 1
      }
    },
    {
      "changeType": "itemAdded",
      "itemId": "cbe73d26-b7a6-46ad-97e4-140ddbd64d96",
      "item": {
        "templateId": "Party:Instance",
        "attributes": {
          "commander_index": 0,
          "date_created": "2022-12-29T13:24:37.239Z",
          "character_ids": [],
          "friend_index": 5,
          "party_icon": "None"
        },
        "quantity": 1
      }
    },
    {
      "changeType": "itemAdded",
      "itemId": "c163bb89-f0d6-4c29-82ba-b7ce34a10029",
      "item": {
        "templateId": "Party:Instance",
        "attributes": {
          "commander_index": 0,
          "date_created": "2022-12-29T13:24:37.239Z",
          "character_ids": [],
          "friend_index": 5,
          "party_icon": "None"
        },
        "quantity": 1
      }
    },
    {
      "changeType": "itemAdded",
      "itemId": "136cbff7-1b5b-4de9-b5b3-d4bc087f28e1",
      "item": {
        "templateId": "Currency:MtxGiveaway",
        "attributes": {},
        "quantity": 40
      }
    },
    {
      "changeType": "itemAdded",
      "itemId": "f766a9b7-43c5-4fc4-8237-ece964f04599",
      "item": {
        "templateId": "Currency:Gold",
        "attributes": {},
        "quantity": 700
      }
    },
    {
      "changeType": "itemAdded",
      "itemId": "6b8142b4-99cf-47e1-b459-8f0e58a2e061",
      "item": {
        "templateId": "Currency:HeroXp_Basic",
        "attributes": {},
        "quantity": 1000
      }
    },
    {
      "changeType": "itemAdded",
      "itemId": "55294f6d-035a-4ad9-bea8-c2dbf390cbdd",
      "item": {
        "templateId": "HammerChest:HC_Tutorial",
        "attributes": {
          "taps_applied": 0,
          "taps_remaining": 10
        },
        "quantity": 1
      }
    },
    {
      "changeType": "statModified",
      "name": "display_name",
      "value": "Epic Name 1"
    },
    {
      "changeType": "statModified",
      "name": "normalized_name",
      "value": "EPICNAME1"
    }
  ],
  "profileCommandRevision": 3,
  "serverTime": "2022-12-29T13:24:37.313Z",
  "multiUpdate": [
    {
      "profileRevision": 3,
      "profileId": "friends",
      "profileChangesBaseRevision": 1,
      "profileChanges": [
        {
          "changeType": "statModified",
          "name": "suggestion_timeout",
          "value": "2022-12-29T14:24:37.240Z"
        },
        {
          "changeType": "itemAdded",
          "itemId": "39e300b4-e380-4908-938a-342cf1e9fab7",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "baaa736cc9e342c88dc12c70cf5b78a8",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "ilKingDelCaccia1",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "0c250921-a187-4e02-9541-c4329cb743b6",
                    "templateId": "Character:Archer_Starter_Water_MultiShot_T03",
                    "bIsCommander": true,
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
                      "level": 15,
                      "perks": [
                        0,
                        4,
                        6,
                        3,
                        0,
                        1,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-29T13:23:52.554Z",
                "numLevelsCompleted": 20,
                "numTerritoriesClaimed": 0,
                "accountLevel": 15,
                "numRepHeroes": 1,
                "isPvPUnlocked": true
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "c3ec2819-37e0-497d-93b7-90fa70a239b1",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "0854b7243a074ff38d93b28055984b90",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Akylyon",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "0c1c52bf-dbca-4589-b8e0-b90ef57cb9a6",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
                    "level": 6,
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
                      "level": 15,
                      "perks": [
                        0,
                        4,
                        5,
                        1,
                        0,
                        4,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-29T11:37:49.964Z",
                "numLevelsCompleted": 16,
                "numTerritoriesClaimed": 0,
                "accountLevel": 15,
                "numRepHeroes": 1,
                "isPvPUnlocked": true
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "b87c7eb8-2e8d-47c9-9c77-34d9bce616e2",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "aafa201eea134c629a601a9d55cd2f90",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "MicheladaKlasik",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "6dbd48a2-d0d3-4710-8cae-248e6d7ff5f2",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
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
                      "level": 15,
                      "perks": [
                        0,
                        4,
                        6,
                        3,
                        0,
                        1,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-29T08:36:18.272Z",
                "numLevelsCompleted": 18,
                "numTerritoriesClaimed": 0,
                "accountLevel": 15,
                "numRepHeroes": 1,
                "isPvPUnlocked": true
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "ac6a40a8-e30b-48ee-9b50-da2e5d2e5093",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "1cc85e2d61384b2f8ea494a18bc6446d",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "EpikSh\u03b1rk",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "b809872c-c6a0-429f-9c76-06cfcb79ac8c",
                    "templateId": "Character:Archer_VR2_Nature_GoinCommando_T05",
                    "bIsCommander": true,
                    "level": 20,
                    "skillLevel": 2,
                    "upgrades": [
                      10,
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
                      "level": 15,
                      "perks": [
                        0,
                        5,
                        7,
                        2,
                        0,
                        0,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-29T05:45:50.646Z",
                "numLevelsCompleted": 22,
                "numTerritoriesClaimed": 1,
                "accountLevel": 15,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "e12478e1-a3b8-4a47-a92a-04cbed7a3b26",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "5123745124794fbfb6315e42d463683d",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Guri\u0308ncri\u0301vel",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "70fbeb2b-f391-4b0c-b468-2593f4689436",
                    "templateId": "Character:Archer_VR2_Nature_GoinCommando_T05",
                    "bIsCommander": true,
                    "level": 15,
                    "skillLevel": 1,
                    "upgrades": [
                      5,
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
                      "level": 15,
                      "perks": [
                        0,
                        3,
                        6,
                        4,
                        0,
                        1,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-28T21:48:24.568Z",
                "numLevelsCompleted": 26,
                "numTerritoriesClaimed": 1,
                "accountLevel": 15,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "549febb9-d40f-40bc-9fc7-3002d3c99244",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "297139ec951b422ab4405e79d6c03205",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Nix10m10",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "8ed41d5f-3ef8-4ec2-aeb5-8ad499f6ba12",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
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
                      "level": 15,
                      "perks": [
                        0,
                        4,
                        6,
                        3,
                        1,
                        4,
                        2,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-27T10:25:37.234Z",
                "numLevelsCompleted": 23,
                "numTerritoriesClaimed": 2,
                "accountLevel": 15,
                "numRepHeroes": 1,
                "isPvPUnlocked": true
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "c817dbcd-3e21-465b-9e14-bb80c562f06c",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "899de865d32148b3a5d7ec2030c3bcb1",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Gogether88",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "f7a47046-133f-402c-8cb8-cfef992287cc",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
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
                      "level": 15,
                      "perks": [
                        0,
                        4,
                        7,
                        1,
                        0,
                        2,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-27T08:47:02.105Z",
                "numLevelsCompleted": 15,
                "numTerritoriesClaimed": 1,
                "accountLevel": 15,
                "numRepHeroes": 1,
                "isPvPUnlocked": true
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "326fb790-364e-4846-afeb-cc28cacd0af9",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "e7363c9260154c4aad7bddb62fb8e793",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "KingRaptor2121",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "9867e32c-6046-4b83-a509-d2ad6e3d9bfb",
                    "templateId": "Character:Archer_Starter_Water_MultiShot_T03",
                    "bIsCommander": true,
                    "level": 20,
                    "skillLevel": 1,
                    "upgrades": [
                      0,
                      0,
                      25,
                      0,
                      0,
                      0,
                      0,
                      0,
                      0
                    ],
                    "accountInfo": {
                      "level": 15,
                      "perks": [
                        0,
                        4,
                        7,
                        3,
                        0,
                        1,
                        0,
                        1
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-26T21:20:51.709Z",
                "numLevelsCompleted": 24,
                "numTerritoriesClaimed": 1,
                "accountLevel": 15,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "63e43370-b81a-4f60-bb4b-c0a1ebdc0645",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "2e0b3af2e9f84b10ab47f171a64b0003",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "GabeTheKid34",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "73780f7d-37c7-4c6c-8ae5-0ce210cc396f",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
                    "level": 15,
                    "skillLevel": 1,
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
                      "level": 15,
                      "perks": [
                        0,
                        3,
                        7,
                        4,
                        0,
                        0,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-26T21:20:51.534Z",
                "numLevelsCompleted": 22,
                "numTerritoriesClaimed": 0,
                "accountLevel": 15,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "96796354-7d91-440a-935a-c9fbf77e8f12",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "9b001a75f9864074ac12a6afb02cad78",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Gjsyis",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "6cea8054-468d-4ead-a493-575b7b52bc33",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
                    "level": 15,
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
                      "level": 15,
                      "perks": [
                        0,
                        7,
                        3,
                        4,
                        0,
                        0,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-26T18:02:37.522Z",
                "numLevelsCompleted": 19,
                "numTerritoriesClaimed": 1,
                "accountLevel": 15,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "f78d84c2-cddd-4284-85b8-a9bb7e819888",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "b25c4ec66f644d25af01a7a7b68f7c3b",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Vladisval_yt",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "64210597-4aa5-4069-b589-b6978f7bbbc2",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
                    "level": 15,
                    "skillLevel": 1,
                    "upgrades": [
                      0,
                      1,
                      1,
                      0,
                      0,
                      0,
                      0,
                      0,
                      0
                    ],
                    "accountInfo": {
                      "level": 15,
                      "perks": [
                        0,
                        6,
                        7,
                        1,
                        0,
                        0,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-26T14:34:21.503Z",
                "numLevelsCompleted": 19,
                "numTerritoriesClaimed": 0,
                "accountLevel": 15,
                "numRepHeroes": 1,
                "isPvPUnlocked": true
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "80bb29e5-be26-4f47-873a-f45746bd7d0c",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "b5b4809b53f940dea767c2056ddf548d",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "qsswe-",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "301a4541-d56a-4d98-9bc5-2d94fcb86b65",
                    "templateId": "Character:Archer_Starter_Water_MultiShot_T03",
                    "bIsCommander": true,
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
                      "level": 14,
                      "perks": [
                        0,
                        3,
                        4,
                        3,
                        0,
                        2,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-29T13:18:33.751Z",
                "numLevelsCompleted": 14,
                "numTerritoriesClaimed": 1,
                "accountLevel": 14,
                "numRepHeroes": 1,
                "isPvPUnlocked": true
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "e7508507-de4b-4024-a620-e7d2a749fee1",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "d5e7bf9d43494b5dbf6a9b093cea15c7",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "anviltoe.",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "119b9f35-0142-4666-9143-36185246e27b",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
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
                      "level": 14,
                      "perks": [
                        0,
                        4,
                        4,
                        3,
                        0,
                        2,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-29T13:17:03.985Z",
                "numLevelsCompleted": 23,
                "numTerritoriesClaimed": 0,
                "accountLevel": 14,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "f9a38e0c-8452-49ab-83a3-694a542c35af",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "aa36b7df8c004fe097ae8f87a35c8b3d",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "SeniorTheImafix",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "017a6a52-664f-46b5-945c-5b7662d761f0",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
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
                      "level": 14,
                      "perks": [
                        0,
                        4,
                        8,
                        2,
                        0,
                        0,
                        0,
                        1
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-29T10:00:00.597Z",
                "numLevelsCompleted": 21,
                "numTerritoriesClaimed": 1,
                "accountLevel": 14,
                "numRepHeroes": 1,
                "isPvPUnlocked": true
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "d352be7a-9e6d-4a21-ae73-0a1a4187df27",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "4791caf274704386b6d54a0bc779e3a1",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Ty 103",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "2587c98c-e54e-4f5f-9972-b18009b83038",
                    "templateId": "Character:Warrior_Starter_Nature_PowerStrike_T03",
                    "bIsCommander": true,
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
                      "level": 14,
                      "perks": [
                        0,
                        6,
                        4,
                        1,
                        0,
                        2,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-28T15:24:51.445Z",
                "numLevelsCompleted": 19,
                "numTerritoriesClaimed": 1,
                "accountLevel": 14,
                "numRepHeroes": 1,
                "isPvPUnlocked": true
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "0857f458-2af9-4995-9562-e3098cffb1a1",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "7c2a41ee8b504a21803daff35f737824",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "stampedeadam",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "4c784c91-0276-4686-a3c8-89b161d0d77b",
                    "templateId": "Character:Archer_Starter_Water_MultiShot_T03",
                    "bIsCommander": true,
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
                      "level": 14,
                      "perks": [
                        0,
                        9,
                        3,
                        1,
                        0,
                        0,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-28T14:50:15.479Z",
                "numLevelsCompleted": 19,
                "numTerritoriesClaimed": 0,
                "accountLevel": 14,
                "numRepHeroes": 1,
                "isPvPUnlocked": true
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "456e7351-b763-427c-bb97-cae9bdf3f846",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "03459431953b44748ebe3b80a16847f1",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "\u6811\u4e0a\u9a91\u4e2a\u7334\u5730\u4e0a\u4e00\u4e2a\u7334",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "9d25ea62-2426-4825-81cf-dfd13b6fb2c8",
                    "templateId": "Character:Archer_Starter_Water_MultiShot_T03",
                    "bIsCommander": true,
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
                      "level": 14,
                      "perks": [
                        0,
                        4,
                        4,
                        3,
                        0,
                        2,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-28T12:03:50.318Z",
                "numLevelsCompleted": 19,
                "numTerritoriesClaimed": 1,
                "accountLevel": 14,
                "numRepHeroes": 1,
                "isPvPUnlocked": true
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "489109c0-2de3-46fa-98ad-7cdab1434bb3",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "2ba38751f2a14697803481bc03c731b5",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "COWBOYS-4-21-88",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "80ca0e90-9c9d-4100-972f-81e5986b4ef6",
                    "templateId": "Character:Archer_Starter_Water_MultiShot_T03",
                    "bIsCommander": true,
                    "level": 10,
                    "skillLevel": 1,
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
                      "level": 14,
                      "perks": [
                        0,
                        4,
                        4,
                        3,
                        0,
                        2,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-27T18:49:48.226Z",
                "numLevelsCompleted": 19,
                "numTerritoriesClaimed": 1,
                "accountLevel": 14,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "23a45f8f-3c1d-4b80-a923-42a1b6a34bce",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "a62ce1707af0443182903bb6a13a28f1",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "\u0422\u0438\u043c\u0443\u0440\u043a\u04302284",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "625968a6-4f12-41bc-8656-fd15eedf52ef",
                    "templateId": "Character:Archer_Starter_Water_MultiShot_T03",
                    "bIsCommander": true,
                    "level": 15,
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
                      "level": 14,
                      "perks": [
                        0,
                        5,
                        4,
                        3,
                        0,
                        1,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-27T17:23:18.291Z",
                "numLevelsCompleted": 21,
                "numTerritoriesClaimed": 1,
                "accountLevel": 14,
                "numRepHeroes": 1,
                "isPvPUnlocked": true
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "e56eb263-8e94-4c16-823c-1e3cf76d98b1",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "75b4aa3f27de4ae6866f8e9250cea935",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Dockiedoc",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "0c6718f3-2e4b-4487-8d58-2b9af7d76225",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
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
                      "level": 14,
                      "perks": [
                        0,
                        7,
                        4,
                        0,
                        0,
                        2,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-27T13:38:17.040Z",
                "numLevelsCompleted": 19,
                "numTerritoriesClaimed": 1,
                "accountLevel": 14,
                "numRepHeroes": 1,
                "isPvPUnlocked": true
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "993cce97-65eb-4af3-8eb9-1d21e7a284e5",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "fa8b7a337ff747faad8cad896e4be4ba",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Savageguy8706",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "2c9747b4-2e68-4f58-b91a-942a996383e6",
                    "templateId": "Character:Archer_Starter_Water_MultiShot_T03",
                    "bIsCommander": true,
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
                      "level": 14,
                      "perks": [
                        0,
                        6,
                        6,
                        5,
                        1,
                        1,
                        2,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-27T07:38:41.906Z",
                "numLevelsCompleted": 19,
                "numTerritoriesClaimed": 1,
                "accountLevel": 14,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "60326320-eb07-402d-aa51-faff5741dbc0",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "2aa9c4b191ab4855bea843754b9eafc4",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Earn92",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "14b882df-cbc1-4f2c-b61a-bfb41ed0cae4",
                    "templateId": "Character:Archer_Starter_Water_MultiShot_T03",
                    "bIsCommander": true,
                    "level": 15,
                    "skillLevel": 1,
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
                      "level": 14,
                      "perks": [
                        0,
                        5,
                        6,
                        2,
                        0,
                        0,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-27T04:53:52.616Z",
                "numLevelsCompleted": 22,
                "numTerritoriesClaimed": 1,
                "accountLevel": 14,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "de73a0d3-74f1-4be6-b34b-b83481ba73b7",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "43272036be2741a7b9352d579051698a",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Bigchuy 12",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "6e5961ec-d055-4130-af3f-53da042761e1",
                    "templateId": "Character:Warrior_Starter_Nature_PowerStrike_T03",
                    "bIsCommander": true,
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
                      "level": 14,
                      "perks": [
                        0,
                        3,
                        7,
                        3,
                        0,
                        0,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-27T04:48:55.520Z",
                "numLevelsCompleted": 13,
                "numTerritoriesClaimed": 0,
                "accountLevel": 14,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "d27665ab-7b8e-40ce-bd37-4bdcdcebc054",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "698733282ae74928820dd43b51e4add1",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "RED \u4e48",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "44a6bd91-6095-48e4-a143-ce10079ba87c",
                    "templateId": "Character:TreasureHunter_VR2_Fire_AntiMaterialCharge_T05",
                    "bIsCommander": true,
                    "level": 15,
                    "skillLevel": 2,
                    "upgrades": [
                      5,
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
                      "level": 14,
                      "perks": [
                        0,
                        3,
                        5,
                        5,
                        0,
                        1,
                        1,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-27T01:23:11.184Z",
                "numLevelsCompleted": 20,
                "numTerritoriesClaimed": 1,
                "accountLevel": 14,
                "numRepHeroes": 1,
                "isPvPUnlocked": true
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "a1e573fd-43ca-471d-be1c-3bdbdee71cf5",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "927bc55ea3384522b26fd7aa0a9381db",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "TacoBell-WC",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "652c6d4b-7c76-4933-a07a-045b951946cd",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
                    "level": 15,
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
                      "level": 14,
                      "perks": [
                        0,
                        4,
                        4,
                        3,
                        0,
                        2,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-26T19:13:02.798Z",
                "numLevelsCompleted": 23,
                "numTerritoriesClaimed": 1,
                "accountLevel": 14,
                "numRepHeroes": 1,
                "isPvPUnlocked": true
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "fb2ea16b-105b-40f0-9ac6-9b95e9abb2c9",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "2de6cf851c0a4b038600a42920f05592",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Alexby Roca",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "2e1ae343-f480-4bb3-b458-b539be11da04",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
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
                      "level": 13,
                      "perks": [
                        0,
                        6,
                        4,
                        1,
                        0,
                        1,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-29T01:37:05.630Z",
                "numLevelsCompleted": 17,
                "numTerritoriesClaimed": 0,
                "accountLevel": 13,
                "numRepHeroes": 1,
                "isPvPUnlocked": true
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "7e03ceb4-bd9c-4e79-99d4-259d4d8fe055",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "7deeb75f5ede464a92687fd2fc306a53",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "khalid-4-life",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "224537c4-a2b4-46c5-bc07-ce624ebc50f3",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
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
                        5,
                        1,
                        0,
                        0,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-29T00:28:44.718Z",
                "numLevelsCompleted": 15,
                "numTerritoriesClaimed": 0,
                "accountLevel": 13,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "be3c6e0c-5686-4127-8d78-4e02e97d38da",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "4a71cd84bef843dfbeab9e9981d99c50",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "hopedboot23248",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "d529a2b7-2b9d-46e4-944a-4f102221925c",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
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
                        3,
                        6,
                        2,
                        0,
                        1,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-28T13:51:24.030Z",
                "numLevelsCompleted": 20,
                "numTerritoriesClaimed": 0,
                "accountLevel": 13,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "71e260d1-e449-4164-a506-c50835e33ce5",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "40e0100a635f4cb6ab37adb12b7e3436",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "FaDe_ChrisACBL",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "36cf4b20-45b2-4998-b3ad-a69e0adf1cb1",
                    "templateId": "Character:Archer_Starter_Water_MultiShot_T03",
                    "bIsCommander": true,
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
                        4,
                        6,
                        2,
                        0,
                        0,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-28T02:54:25.296Z",
                "numLevelsCompleted": 19,
                "numTerritoriesClaimed": 0,
                "accountLevel": 13,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "5d99f0d0-4998-41e4-97b6-98c07693752b",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "5a889f75adcc43e0876fb67652aaf3e1",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "DJStrohdawg",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "3cd6e6fa-d5d7-43ba-9332-05f57c36ac45",
                    "templateId": "Character:Warrior_Starter_Nature_PowerStrike_T03",
                    "bIsCommander": true,
                    "level": 6,
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
                        3,
                        4,
                        3,
                        0,
                        2,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-27T22:28:20.025Z",
                "numLevelsCompleted": 16,
                "numTerritoriesClaimed": 0,
                "accountLevel": 13,
                "numRepHeroes": 1,
                "isPvPUnlocked": true
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "64d4da34-1087-4c92-b76d-1339d1a737b0",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "d7085dd2c03741f797ade99fd259ba7d",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "EN Tripp",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "06fd48cd-8769-4b29-93e3-fedb9e2a3586",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
                    "level": 6,
                    "skillLevel": 1,
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
                    ],
                    "accountInfo": {
                      "level": 12,
                      "perks": [
                        0,
                        6,
                        5,
                        2,
                        1,
                        1,
                        1,
                        1
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-29T13:17:03.969Z",
                "numLevelsCompleted": 15,
                "numTerritoriesClaimed": 0,
                "accountLevel": 12,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "234b8432-19d2-4306-8a85-17c1e8577073",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "9370707d88aa46b0a33c40930397e1c7",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "COKARTEL",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "a98b3693-4e1f-4dc5-9596-9252dba40352",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
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
                        1,
                        6,
                        3,
                        0,
                        1,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-28T23:46:44.043Z",
                "numLevelsCompleted": 17,
                "numTerritoriesClaimed": 0,
                "accountLevel": 12,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "d92b24ad-5380-4b45-86d2-d8271845f462",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "15e9e5be037e4eaf81c99ccef7e39781",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "rasta275",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "87706368-1965-49c2-adc0-c1446e8860d4",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
                    "level": 11,
                    "skillLevel": 1,
                    "upgrades": [
                      6,
                      0,
                      6,
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
                        2,
                        5,
                        2,
                        0,
                        2,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-28T20:30:55.511Z",
                "numLevelsCompleted": 18,
                "numTerritoriesClaimed": 0,
                "accountLevel": 12,
                "numRepHeroes": 1,
                "isPvPUnlocked": true
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "37fd1bf8-90e1-41bf-a483-84fca37eaa4e",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "60972797593d40aebe2c4073a6c87059",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "NeMo hiySeriy",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "c9aba0f7-5425-47c7-9196-d6ffaf5b9773",
                    "templateId": "Character:Archer_VR2_Nature_GoinCommando_T05",
                    "bIsCommander": true,
                    "level": 15,
                    "skillLevel": 1,
                    "upgrades": [
                      1,
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
                      "level": 12,
                      "perks": [
                        0,
                        7,
                        3,
                        1,
                        0,
                        0,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-28T17:40:37.721Z",
                "numLevelsCompleted": 17,
                "numTerritoriesClaimed": 0,
                "accountLevel": 12,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "f36239ad-7106-4115-afb7-ffc29b0e120a",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "dc1066956c534cd9a8657c882e4a395c",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "TPM_OrneryCannon",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "a7f9c81e-f7a7-4b9f-a2a7-84b5b9177927",
                    "templateId": "Character:Warrior_Starter_Nature_PowerStrike_T03",
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
                      "level": 12,
                      "perks": [
                        0,
                        4,
                        4,
                        2,
                        0,
                        1,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-28T07:56:20.611Z",
                "numLevelsCompleted": 15,
                "numTerritoriesClaimed": 0,
                "accountLevel": 12,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "080453fc-e32f-4454-9ac5-c6b4612a22fa",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "c9389c4060e94b51bcd311b8a8a58a9a",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Adnanekiller123",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "b02aecc2-e851-4d4c-9eca-b65bb70fbfbb",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
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
                        6,
                        4,
                        2,
                        1,
                        1,
                        2,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-28T07:08:46.181Z",
                "numLevelsCompleted": 15,
                "numTerritoriesClaimed": 1,
                "accountLevel": 12,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "f821cfc0-d901-4dee-abda-d25dcb90935b",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "86c583d490e54d0da67b785e4ba8126c",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Myzorgil",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "6510a2da-2c75-4876-92bf-265dbf851c32",
                    "templateId": "Character:Warrior_Starter_Nature_PowerStrike_T03",
                    "bIsCommander": true,
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
                      "level": 12,
                      "perks": [
                        0,
                        0,
                        5,
                        3,
                        0,
                        3,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-27T20:22:53.008Z",
                "numLevelsCompleted": 8,
                "numTerritoriesClaimed": 0,
                "accountLevel": 12,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "18b7b6ec-1ebb-42aa-b33e-6becc0c81f85",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "04de67a2d45d430496d463dfb5a329f3",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Jok3r504hn",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "191fa55c-c1c3-4af9-a5da-6a1a739a8330",
                    "templateId": "Character:Archer_Starter_Water_MultiShot_T03",
                    "bIsCommander": true,
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
                      "level": 12,
                      "perks": [
                        0,
                        1,
                        4,
                        3,
                        0,
                        3,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-27T18:49:48.197Z",
                "numLevelsCompleted": 16,
                "numTerritoriesClaimed": 1,
                "accountLevel": 12,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "86f1207a-c469-4bf2-a21a-c869ae93a739",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "4ad4a88a6d114ceaa634eba1f2b5eaa5",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Dibol",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "aa078085-dd4b-4d70-b5ed-60b3bddfdf29",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
                    "level": 10,
                    "skillLevel": 1,
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
                    ],
                    "accountInfo": {
                      "level": 12,
                      "perks": [
                        0,
                        1,
                        5,
                        3,
                        0,
                        2,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-26T23:49:38.148Z",
                "numLevelsCompleted": 13,
                "numTerritoriesClaimed": 0,
                "accountLevel": 12,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "4f97d02d-1736-473a-8912-0e209afebeb4",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "b8e26b48e75347fc93276c5be8a86b0d",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Ajanvs",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "e1650681-13ec-4a15-854c-e978105acf96",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
                    "level": 15,
                    "skillLevel": 1,
                    "upgrades": [
                      6,
                      3,
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
                        5,
                        2,
                        3,
                        0,
                        1,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-26T21:20:51.590Z",
                "numLevelsCompleted": 16,
                "numTerritoriesClaimed": 0,
                "accountLevel": 12,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "badba24a-6f73-4e96-9d0d-26df5d2dead3",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "ff9826000d2b40a9afc158e63de72e57",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "dhvhcaw",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "015a6621-a9c8-488f-aba3-e7a65c02483c",
                    "templateId": "Character:Warrior_Starter_Nature_PowerStrike_T03",
                    "bIsCommander": true,
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
                      "level": 12,
                      "perks": [
                        0,
                        1,
                        3,
                        4,
                        0,
                        3,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-26T17:23:07.476Z",
                "numLevelsCompleted": 14,
                "numTerritoriesClaimed": 1,
                "accountLevel": 12,
                "numRepHeroes": 1,
                "isPvPUnlocked": true
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "d0a6a4de-f324-472b-af2c-ffb6eeeb7e1b",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "f9fa43a94cb94312b80d3036ce0edb49",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Nerdiser",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "835d0254-3b07-4f3a-9851-2b5d613acd09",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
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
                        4,
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
                  }
                ],
                "lastPlayTime": "2022-12-29T11:22:35.139Z",
                "numLevelsCompleted": 12,
                "numTerritoriesClaimed": 1,
                "accountLevel": 11,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "43d794d5-7b7f-4874-bcc5-db7f2d7edde2",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "ef54b1c77ccf4a0689ee58359cd7dde9",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "phungtuan2591996",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "193740d4-2af8-4a5f-ba10-12bc1b17945d",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
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
                      "level": 11,
                      "perks": [
                        0,
                        3,
                        5,
                        1,
                        0,
                        1,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-29T11:00:29.312Z",
                "numLevelsCompleted": 13,
                "numTerritoriesClaimed": 0,
                "accountLevel": 11,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "94ccf838-f150-4e56-af70-e80ea20a900c",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "fc2a238b4bce4972b5e40efaa818d0fb",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Elhabaner0",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "992777bc-8fef-4144-949d-d412e6820802",
                    "templateId": "Character:Archer_Starter_Water_MultiShot_T03",
                    "bIsCommander": true,
                    "level": 5,
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
                      "level": 11,
                      "perks": [
                        0,
                        3,
                        4,
                        2,
                        0,
                        1,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-29T08:40:52.434Z",
                "numLevelsCompleted": 0,
                "numTerritoriesClaimed": 0,
                "accountLevel": 11,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "1d588abe-bda6-4456-9567-09c4371bc476",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "78b81197d79d41cba08a46e3076605d0",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "XavierXD321",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "8ac713fa-8cfc-45c2-bb3b-cd8450e9cc5d",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
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
                      "level": 11,
                      "perks": [
                        0,
                        6,
                        4,
                        0,
                        0,
                        0,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-29T05:43:59.464Z",
                "numLevelsCompleted": 12,
                "numTerritoriesClaimed": 0,
                "accountLevel": 11,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "bbac8f65-ae79-4501-86f1-685d8dc52b21",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "97dd4ec821924cb893b14d38831c7870",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "SolidSlayed437",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "f6fee12e-189b-48bd-9142-5479a119a8b1",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
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
                        3,
                        1,
                        0,
                        0,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-28T10:54:41.705Z",
                "numLevelsCompleted": 14,
                "numTerritoriesClaimed": 0,
                "accountLevel": 11,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "b09410d0-38d7-4043-ad6e-4e9df800effa",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "81e63a4d6eb147e7b36948ce7e68924b",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "zCrvnchyz",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "a4346d3b-b55a-4bae-9ec7-6f8e3d5678d9",
                    "templateId": "Character:Archer_Starter_Water_MultiShot_T03",
                    "bIsCommander": true,
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
                      "level": 11,
                      "perks": [
                        0,
                        2,
                        3,
                        2,
                        0,
                        3,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-28T04:47:14.497Z",
                "numLevelsCompleted": 14,
                "numTerritoriesClaimed": 1,
                "accountLevel": 11,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "2892536c-e0e6-4cca-895f-772288585d55",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "cdb6195928864103b5d5265626e7d5d1",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "UTA-298",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "3be97a33-c493-41f5-b152-58ebe4458b45",
                    "templateId": "Character:Archer_Starter_Water_MultiShot_T03",
                    "bIsCommander": true,
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
                      "level": 11,
                      "perks": [
                        0,
                        3,
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
                  }
                ],
                "lastPlayTime": "2022-12-28T04:17:18.053Z",
                "numLevelsCompleted": 14,
                "numTerritoriesClaimed": 0,
                "accountLevel": 11,
                "numRepHeroes": 1,
                "isPvPUnlocked": true
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "82c5c53b-2c10-41a7-aa8a-4480b81855cd",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "0712607a91194351adae4a5f2387aa05",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "ya_p1rs0lop89sk",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "56bc68b3-ec8c-4c46-919b-77a421692313",
                    "templateId": "Character:Warrior_R2_Light_Warbear_T03",
                    "bIsCommander": true,
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
                      "level": 11,
                      "perks": [
                        0,
                        4,
                        7,
                        4,
                        1,
                        0,
                        2,
                        0
                      ]
                    },
                    "foilLevel": 1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-27T21:56:07.579Z",
                "numLevelsCompleted": 15,
                "numTerritoriesClaimed": 1,
                "accountLevel": 11,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "88fed4dd-d9c9-49ac-9c56-62e26cdceb11",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "ccf4e94806fc42469df91bace6714e33",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Raypell",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "e0c86831-d572-409f-990c-59b0d7ad2e2f",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
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
                        4,
                        4,
                        2,
                        0,
                        0,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-27T07:38:41.944Z",
                "numLevelsCompleted": 13,
                "numTerritoriesClaimed": 1,
                "accountLevel": 11,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "fba4397e-a05a-401e-9606-4f53626b7b9d",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "13ea0afe71a34e2e97c7fbc9f31f84c6",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "caspa del diablo",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "7c26b7ff-c2ac-4ef5-96b8-dc93f2acb2f1",
                    "templateId": "Character:Archer_Starter_Water_MultiShot_T03",
                    "bIsCommander": true,
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
                      "level": 11,
                      "perks": [
                        0,
                        5,
                        7,
                        4,
                        1,
                        0,
                        1,
                        1
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-26T21:30:47.587Z",
                "numLevelsCompleted": 16,
                "numTerritoriesClaimed": 0,
                "accountLevel": 11,
                "numRepHeroes": 1,
                "isPvPUnlocked": true
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "288a38ac-5816-4417-b079-427ce854269c",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "f2f02a4d2c374140b549756b5eb3c7a5",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "SharkyswitchYT",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "5d508ee1-fa7b-4461-8682-1068baee48b9",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
                    "level": 12,
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
                      "level": 11,
                      "perks": [
                        0,
                        6,
                        3,
                        0,
                        0,
                        1,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-26T20:03:47.168Z",
                "numLevelsCompleted": 15,
                "numTerritoriesClaimed": 0,
                "accountLevel": 11,
                "numRepHeroes": 1,
                "isPvPUnlocked": true
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "ae491fe4-84c7-41ef-b372-cfb05b917cb7",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "8e9e528ace2c47d7aff4f738b0edf999",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Mia-Sophie05",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "3ed8df5c-61ea-4e05-b2dd-8415a469a00f",
                    "templateId": "Character:Archer_Starter_Water_MultiShot_T03",
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
                      "level": 10,
                      "perks": [
                        0,
                        4,
                        2,
                        3,
                        0,
                        0,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-29T12:04:49.848Z",
                "numLevelsCompleted": 7,
                "numTerritoriesClaimed": 0,
                "accountLevel": 10,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "66b47db6-a70b-4483-ac5f-3179bca8c8ed",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "87bce5d2c48a427e8ee4e8ba76c32d1d",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "TomiHUN9076",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "bbbc2435-4e5f-4145-8a7e-141abf1b4ea9",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
                    "level": 9,
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
                      "level": 10,
                      "perks": [
                        0,
                        3,
                        5,
                        1,
                        0,
                        0,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-29T00:13:56.104Z",
                "numLevelsCompleted": 11,
                "numTerritoriesClaimed": 0,
                "accountLevel": 10,
                "numRepHeroes": 1,
                "isPvPUnlocked": true
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "f6a8237e-b75e-4671-afd7-1c1701d9d1b8",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "3f6794b153694181b3d15cdfddd2e812",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "vl-intoxicated_",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "43d2b803-5dee-4b40-9271-7aa517207dec",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
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
                        1,
                        5,
                        2,
                        0,
                        1,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-28T21:37:44.621Z",
                "numLevelsCompleted": 7,
                "numTerritoriesClaimed": 0,
                "accountLevel": 10,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "cdd49e21-4e2a-4d2a-b8f8-9a2fcd7a476c",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "56786acacb5c448db4e947d472738fea",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Heavyhead100",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "825f7bd7-d56c-4d67-9c5f-5e0d004608f9",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
                    "level": 10,
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
                      "level": 10,
                      "perks": [
                        0,
                        4,
                        2,
                        3,
                        0,
                        0,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-28T21:30:55.838Z",
                "numLevelsCompleted": 6,
                "numTerritoriesClaimed": 0,
                "accountLevel": 10,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "2156e073-7344-49b3-b6c3-82aa8d48e00d",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "7bae045ede7343c39f2ab2064fe86a7c",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "\u0438\u0432\u0430\u043d547",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "1e806ec4-5d2f-45f7-ae8f-875914c9f67a",
                    "templateId": "Character:Warrior_Starter_Nature_PowerStrike_T03",
                    "bIsCommander": true,
                    "level": 10,
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
                        4,
                        5,
                        0,
                        0,
                        0,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-28T17:40:37.746Z",
                "numLevelsCompleted": 6,
                "numTerritoriesClaimed": 0,
                "accountLevel": 10,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "9cb52e4a-94a4-4e1a-9ad3-d39e7e4de9c4",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "94ad21a6b6ac4eb1a928a2bd8368eb2a",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Berlin-\u30c4",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "94989cf8-9d85-4c2c-8ffb-e0a4ef37db5c",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
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
                        4,
                        2,
                        3,
                        0,
                        0,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-28T17:20:35.053Z",
                "numLevelsCompleted": 10,
                "numTerritoriesClaimed": 0,
                "accountLevel": 10,
                "numRepHeroes": 1,
                "isPvPUnlocked": true
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "21971ce3-cded-4673-8826-9a578b7c0eda",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "f2b5a9a61e174e08b189f8f96d90252e",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "ego4011",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "28d49e0a-be8a-4c20-9ff2-8a96efbaf565",
                    "templateId": "Character:Cleric_VR2_Dark_TerraRifle_T04",
                    "bIsCommander": true,
                    "level": 15,
                    "skillLevel": 1,
                    "upgrades": [
                      13,
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
                        4,
                        4,
                        2,
                        0,
                        0,
                        0,
                        1
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-28T08:54:31.227Z",
                "numLevelsCompleted": 9,
                "numTerritoriesClaimed": 0,
                "accountLevel": 10,
                "numRepHeroes": 1,
                "isPvPUnlocked": true
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "8c0acf0e-89a3-42e2-9d2a-83ab0cbbd591",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "d7573b0a73ff4b0e9ffbeccf8bb711bf",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Mcdeymon",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "70853849-6582-4aa0-ba98-3e57063d0b34",
                    "templateId": "Character:Archer_Starter_Water_MultiShot_T03",
                    "bIsCommander": true,
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
                        2,
                        3,
                        3,
                        0,
                        1,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-28T07:56:20.547Z",
                "numLevelsCompleted": 10,
                "numTerritoriesClaimed": 0,
                "accountLevel": 10,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "4ed10b34-0aa8-48ea-a55b-232c12356bdb",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "f2b348ec17314e0790966e574233e6cb",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Agony_23",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "7a43a7a2-ec38-4904-b497-03141a3fb33e",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
                    "level": 10,
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
                        2,
                        7,
                        2,
                        0,
                        0,
                        1,
                        1
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-28T07:05:13.424Z",
                "numLevelsCompleted": 9,
                "numTerritoriesClaimed": 1,
                "accountLevel": 10,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "3b26fb85-fab4-4fff-9cb5-a1dee4ec9ce9",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "569166f5452f48d0973c4245b8ffa3a2",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Turtlematics",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "e1540eb9-9b3b-422a-88dd-28506d377347",
                    "templateId": "Character:Warrior_Starter_Nature_PowerStrike_T03",
                    "bIsCommander": true,
                    "level": 10,
                    "skillLevel": 1,
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
                      "level": 10,
                      "perks": [
                        0,
                        4,
                        3,
                        1,
                        0,
                        1,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-28T04:07:14.727Z",
                "numLevelsCompleted": 10,
                "numTerritoriesClaimed": 0,
                "accountLevel": 10,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "2d9f785a-34dc-435b-849e-1a0e3bdf81bf",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "d6c321d58b07493ca4dc8085beb3965e",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "TED Ashley",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "ed266748-9bdb-4db8-8789-b5fb90ca2f82",
                    "templateId": "Character:Cleric_VR2_Dark_TerraRifle_T04",
                    "bIsCommander": true,
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
                        5,
                        2,
                        0,
                        0,
                        2,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-28T03:53:05.874Z",
                "numLevelsCompleted": 6,
                "numTerritoriesClaimed": 0,
                "accountLevel": 10,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "972a5dfe-0521-4e60-a082-5fbf7097c5be",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "204048d045684e9095388aedb91ce99e",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "HOLO G4M3R",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "701d80da-519f-44de-b3c3-01ec5e6163a0",
                    "templateId": "Character:Archer_Starter_Water_MultiShot_T03",
                    "bIsCommander": true,
                    "level": 5,
                    "skillLevel": 1,
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
                      "level": 10,
                      "perks": [
                        0,
                        5,
                        6,
                        0,
                        0,
                        0,
                        2,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-28T00:26:09.753Z",
                "numLevelsCompleted": 10,
                "numTerritoriesClaimed": 0,
                "accountLevel": 10,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "51c2bab4-4457-4104-a70a-d34a070f4d31",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "55d1005fa4cb4f46abcbade236bee869",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "fabiokappa006",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "49e5902f-2459-45b9-9f33-2df9358f0e90",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
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
                      "level": 10,
                      "perks": [
                        0,
                        6,
                        3,
                        0,
                        0,
                        0,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-27T23:21:42.541Z",
                "numLevelsCompleted": 14,
                "numTerritoriesClaimed": 0,
                "accountLevel": 10,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "85f287f3-8b54-471d-8a0d-ce358a77403f",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "2d6276fe5ad74f94a97595c62e29c08b",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Flame Ginger322",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "98549030-c548-4de0-be02-68a76eb57a96",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
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
                        4,
                        4,
                        4,
                        1,
                        1,
                        1,
                        1
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-27T22:23:25.104Z",
                "numLevelsCompleted": 10,
                "numTerritoriesClaimed": 0,
                "accountLevel": 10,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "73914cc6-fe7d-4f4a-bfb4-112ccda80d4c",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "4d4fde2bcc134c0ab32762becd15768d",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Yung_ArticFox",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "57c222ad-34b4-4147-9e26-3a8ba774788d",
                    "templateId": "Character:Archer_Starter_Water_MultiShot_T03",
                    "bIsCommander": true,
                    "level": 10,
                    "skillLevel": 1,
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
                    ],
                    "accountInfo": {
                      "level": 10,
                      "perks": [
                        0,
                        5,
                        3,
                        0,
                        0,
                        1,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-27T22:23:25.056Z",
                "numLevelsCompleted": 10,
                "numTerritoriesClaimed": 0,
                "accountLevel": 10,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "a11cc236-744e-45f3-a483-f80e60c4a8b8",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "a807e69e006448eba2d860a590dc48b3",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Vimas125",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "7bcd5a8c-97a3-4add-894f-e906939127d1",
                    "templateId": "Character:Ninja_VR1_Light_CrystalDaggers_T04",
                    "bIsCommander": true,
                    "level": 15,
                    "skillLevel": 1,
                    "upgrades": [
                      2,
                      4,
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
                        5,
                        3,
                        2,
                        0,
                        0,
                        0,
                        1
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-27T09:58:24.675Z",
                "numLevelsCompleted": 11,
                "numTerritoriesClaimed": 0,
                "accountLevel": 10,
                "numRepHeroes": 1,
                "isPvPUnlocked": true
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "09d53894-84c5-4fef-8f7b-c4bdc6b2f9be",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "e861688993b34c0d932a927012d62c0f",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Liamjgw",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "121492e8-8034-456f-84c7-7b553f4cbfda",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
                    "level": 7,
                    "skillLevel": 1,
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
                      "level": 10,
                      "perks": [
                        0,
                        2,
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
                  }
                ],
                "lastPlayTime": "2022-12-27T03:10:28.388Z",
                "numLevelsCompleted": 12,
                "numTerritoriesClaimed": 1,
                "accountLevel": 10,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "9ebc2cdb-79f0-43bf-9676-c2620fbec061",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "ae050638cce843308b82c78f094c303c",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "ERmilburn02-Rec",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "9f7949a4-5e57-4f02-b68c-6f1f0f1afe33",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
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
                      "level": 9,
                      "perks": [
                        0,
                        5,
                        2,
                        1,
                        0,
                        0,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-29T13:23:55.883Z",
                "numLevelsCompleted": 9,
                "numTerritoriesClaimed": 0,
                "accountLevel": 9,
                "numRepHeroes": 1,
                "isPvPUnlocked": true
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "28b27422-e926-481b-96f4-cc5116e2abfd",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "23efa549e9264e61b2000d354b7d1516",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Yt_zorg_playz",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "8a827aa8-230b-4d8c-b3c9-26ea6635d47a",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
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
                      "level": 9,
                      "perks": [
                        0,
                        3,
                        5,
                        0,
                        0,
                        0,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-29T13:16:57.504Z",
                "numLevelsCompleted": 9,
                "numTerritoriesClaimed": 0,
                "accountLevel": 9,
                "numRepHeroes": 1,
                "isPvPUnlocked": true
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "ad5a6992-b940-40d5-9bce-3a6a359365aa",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "edfd4064d52242d1befb013df31ccf76",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "readyforwarfare",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "fa48e5b4-fb6d-42b8-bb15-3ef6a6bbe085",
                    "templateId": "Character:HolyKnight_VR2_Light_BASE_T05",
                    "bIsCommander": true,
                    "level": 10,
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
                      "level": 9,
                      "perks": [
                        0,
                        2,
                        3,
                        1,
                        0,
                        2,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-29T13:03:45.694Z",
                "numLevelsCompleted": 4,
                "numTerritoriesClaimed": 0,
                "accountLevel": 9,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "e6a8f215-4ce5-4698-b7c7-dc5e68fc9e47",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "c7f17750d00f4fdfb7bf5de0d4b821c7",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "13_sashko_13",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "93c5b8ec-7701-420f-831d-dc5d714525a0",
                    "templateId": "Character:Warrior_Starter_Nature_PowerStrike_T03",
                    "bIsCommander": true,
                    "level": 9,
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
                      "level": 9,
                      "perks": [
                        0,
                        3,
                        3,
                        2,
                        0,
                        0,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-29T08:43:01.114Z",
                "numLevelsCompleted": 9,
                "numTerritoriesClaimed": 0,
                "accountLevel": 9,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "f507fd64-5095-443e-a8e5-c593470792b4",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "2bedab23d12b48d88503391ca618c507",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "BeaconGaming_HD",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "9333da70-2e17-4b10-a1d9-97b779907c4e",
                    "templateId": "Character:Warrior_Starter_Nature_PowerStrike_T03",
                    "bIsCommander": true,
                    "level": 10,
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
                      "level": 9,
                      "perks": [
                        0,
                        1,
                        2,
                        3,
                        0,
                        2,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-29T06:06:14.707Z",
                "numLevelsCompleted": 6,
                "numTerritoriesClaimed": 0,
                "accountLevel": 9,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "1ec5bbf2-daae-4cae-b259-b41e6797d3d1",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "4dc439a36ea84ebba88f85f45fa22cf8",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "kixoemrxn._",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "bf4911be-6dff-4a27-a6f6-246b3797782b",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
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
                      "level": 9,
                      "perks": [
                        0,
                        3,
                        2,
                        2,
                        0,
                        0,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-28T19:31:52.651Z",
                "numLevelsCompleted": 10,
                "numTerritoriesClaimed": 0,
                "accountLevel": 9,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "4fdcccd9-92f8-4811-8b3f-6ff45a9977e2",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "d2894b2d36d54ba09298b14881ac38a0",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Zollfrei Stuhl",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "8d10c104-27fd-48f4-a2c2-ae63e9a9beda",
                    "templateId": "Character:Warrior_Starter_Nature_PowerStrike_T03",
                    "bIsCommander": true,
                    "level": 10,
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
                      "level": 9,
                      "perks": [
                        0,
                        4,
                        3,
                        1,
                        0,
                        0,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-28T19:02:04.080Z",
                "numLevelsCompleted": 12,
                "numTerritoriesClaimed": 0,
                "accountLevel": 9,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "f4d58e7b-0b9b-43ce-b878-16c42b76bd2e",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "d6f966cc890a47a4826bc43b4014176e",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "PIXEL HOW",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "04b6bf3e-b89c-4762-aee0-e64ce01a2e67",
                    "templateId": "Character:Ninja_UC1_Water_SwiftStrike_T03",
                    "bIsCommander": true,
                    "level": 8,
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
                      "level": 9,
                      "perks": [
                        0,
                        2,
                        2,
                        3,
                        0,
                        1,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-28T10:54:41.692Z",
                "numLevelsCompleted": 9,
                "numTerritoriesClaimed": 0,
                "accountLevel": 9,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "4ba14483-fac4-43ab-b34c-5da77b8d4534",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "377855e53fbb4554af35ec8522e178ce",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "C\u024e\u0299\u01b7r\u030f2212",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "592c1f8a-8886-40cb-bfb0-910e43f7331b",
                    "templateId": "Character:Archer_Starter_Water_MultiShot_T03",
                    "bIsCommander": true,
                    "level": 10,
                    "skillLevel": 1,
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
                      "level": 9,
                      "perks": [
                        0,
                        2,
                        4,
                        2,
                        0,
                        0,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-28T01:55:08.923Z",
                "numLevelsCompleted": 8,
                "numTerritoriesClaimed": 0,
                "accountLevel": 9,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "2711fe42-d1ff-4343-89ba-00ef90a362f7",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "db58a41357c54adb95ff11edd8902f06",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Mgdai07",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "754ca83c-429a-48b8-b7a1-dafbb12fef36",
                    "templateId": "Character:Warrior_Starter_Nature_PowerStrike_T03",
                    "bIsCommander": true,
                    "level": 8,
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
                      "level": 9,
                      "perks": [
                        0,
                        2,
                        5,
                        0,
                        0,
                        1,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-28T01:25:19.519Z",
                "numLevelsCompleted": 7,
                "numTerritoriesClaimed": 0,
                "accountLevel": 9,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "ee9873c4-1be5-4bf3-9df2-71a83b661749",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "c178d0da99fb4e85bf6bdccf46982229",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "FifaElias06",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "ec3f2c29-f8e6-4b9e-9798-f48107e4fd07",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
                    "level": 5,
                    "skillLevel": 1,
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
                    ],
                    "accountInfo": {
                      "level": 9,
                      "perks": [
                        0,
                        2,
                        4,
                        2,
                        0,
                        0,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-27T23:53:39.203Z",
                "numLevelsCompleted": 10,
                "numTerritoriesClaimed": 0,
                "accountLevel": 9,
                "numRepHeroes": 1,
                "isPvPUnlocked": true
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "579ddb82-a47e-4b8e-b81f-f1087baf9e0f",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "a12132d9439d4e25adc7a37dba2ea94a",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "\u0414\u0438\u043c\u0430\u0441\u0438\u043a228 337",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "23c7929e-9212-456d-bc40-5574fea7936a",
                    "templateId": "Character:Warrior_Starter_Nature_PowerStrike_T03",
                    "bIsCommander": true,
                    "level": 5,
                    "skillLevel": 1,
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
                    ],
                    "accountInfo": {
                      "level": 9,
                      "perks": [
                        0,
                        3,
                        3,
                        2,
                        0,
                        0,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-27T23:19:39.688Z",
                "numLevelsCompleted": 8,
                "numTerritoriesClaimed": 0,
                "accountLevel": 9,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "664dcd57-3a53-407f-8fda-362df5248a25",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "10aa6c90787544d9ba981058d7a00428",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Maha_Bk",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "99714992-a81c-40a1-bfef-e8996a9970e7",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
                    "level": 6,
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
                      "level": 9,
                      "perks": [
                        0,
                        3,
                        2,
                        2,
                        0,
                        1,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-27T22:49:42.165Z",
                "numLevelsCompleted": 7,
                "numTerritoriesClaimed": 0,
                "accountLevel": 9,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "77bc6341-168f-4ef9-8d61-dbc8d2625e76",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "a03bc422624140e8ad239f2cc58fca84",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Charbrine8706",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "87751ef1-4613-4480-9ea7-2c1e0e81ac95",
                    "templateId": "Character:Warrior_Starter_Nature_PowerStrike_T03",
                    "bIsCommander": true,
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
                      "level": 9,
                      "perks": [
                        0,
                        6,
                        2,
                        0,
                        0,
                        0,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-27T08:35:06.025Z",
                "numLevelsCompleted": 9,
                "numTerritoriesClaimed": 0,
                "accountLevel": 9,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "43105d73-239b-462b-81cc-6581249a8c55",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "d3b6bdd793e3415e951ce19d8f2cf549",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Zaywoll2",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "c20015f2-ce39-4982-b840-aa0317865657",
                    "templateId": "Character:Archer_Starter_Water_MultiShot_T03",
                    "bIsCommander": true,
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
                      "level": 9,
                      "perks": [
                        0,
                        2,
                        2,
                        2,
                        0,
                        2,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-27T05:09:54.777Z",
                "numLevelsCompleted": 13,
                "numTerritoriesClaimed": 0,
                "accountLevel": 9,
                "numRepHeroes": 1,
                "isPvPUnlocked": true
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "79be5a0a-3cd2-4d41-bf0d-8dc44c0b7acd",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "fdf3cf9079574d57bb8e1efe0976db23",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "victors271",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "35bbbf69-3315-4e17-a509-90fa88f9ce62",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
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
                      "level": 9,
                      "perks": [
                        0,
                        1,
                        4,
                        2,
                        0,
                        1,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-26T20:16:23.160Z",
                "numLevelsCompleted": 11,
                "numTerritoriesClaimed": 1,
                "accountLevel": 9,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "61ccb515-65f0-4630-b4ea-5276c3d56a78",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "561dace60f604156b3b52fbf96005548",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "DER.MEISTER.",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "ca9404bb-ef6c-4342-8f4f-b969c18f4ff4",
                    "templateId": "Character:Cleric_VR2_Dark_TerraRifle_T04",
                    "bIsCommander": true,
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
                      "level": 9,
                      "perks": [
                        0,
                        4,
                        4,
                        2,
                        0,
                        0,
                        1,
                        1
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-26T20:05:29.984Z",
                "numLevelsCompleted": 2,
                "numTerritoriesClaimed": 0,
                "accountLevel": 9,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "9e0c9ff7-ebae-423c-933b-7f0f035bbc43",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "a2e43c0db92942ee9867f572a961936e",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Code Zipz6556",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "5c6d63ae-d239-4ae9-a1fe-b50d8e929de5",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
                    "level": 6,
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
                      "level": 9,
                      "perks": [
                        0,
                        3,
                        3,
                        0,
                        0,
                        2,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-26T17:25:37.071Z",
                "numLevelsCompleted": 8,
                "numTerritoriesClaimed": 0,
                "accountLevel": 9,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "010d54dd-f0f9-454a-a11f-d61122e245ed",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "d50e84da90ba4eae939c89357ade02f3",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Adri_dh8",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "03778631-d895-4331-bc4f-68ef5c0a9421",
                    "templateId": "Character:Warrior_Starter_Nature_PowerStrike_T03",
                    "bIsCommander": true,
                    "level": 10,
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
                      "level": 8,
                      "perks": [
                        0,
                        2,
                        4,
                        1,
                        0,
                        0,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-29T12:32:09.487Z",
                "numLevelsCompleted": 7,
                "numTerritoriesClaimed": 0,
                "accountLevel": 8,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "6f099198-0ad3-4e51-8bb2-72363d6e2b1d",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "ca2bfc3123514f7bbde6a0fda6b50eed",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "\u0410\u0438\u0306\u043a\u0440\u043e\u043b",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "5edbc585-ed2d-4b24-81ac-8da4b0939e6e",
                    "templateId": "Character:Archer_Starter_Water_MultiShot_T03",
                    "bIsCommander": true,
                    "level": 5,
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
                      "level": 8,
                      "perks": [
                        0,
                        2,
                        4,
                        1,
                        0,
                        0,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-29T08:54:44.274Z",
                "numLevelsCompleted": 6,
                "numTerritoriesClaimed": 0,
                "accountLevel": 8,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "2e87e0e4-67c4-4617-9a69-7b69693ae325",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "878aebd5699845169155a6c503ab1ae4",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "AlchemistDars",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "fd1884c7-3cec-4b9d-862d-84879c78a6f9",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
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
                      "level": 8,
                      "perks": [
                        0,
                        2,
                        4,
                        0,
                        0,
                        1,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-29T04:15:27.992Z",
                "numLevelsCompleted": 8,
                "numTerritoriesClaimed": 0,
                "accountLevel": 8,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "f2255a32-9e90-4f2d-8f7a-6996716bc667",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "648f63e3add245e383c6d6b588acbe99",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "To_dam_kiwi",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "fb7b8fc6-aa34-41ba-9f23-45a2c4dd0f9f",
                    "templateId": "Character:Archer_Starter_Water_MultiShot_T03",
                    "bIsCommander": true,
                    "level": 5,
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
                      "level": 8,
                      "perks": [
                        0,
                        3,
                        2,
                        2,
                        0,
                        0,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-28T23:46:43.800Z",
                "numLevelsCompleted": 7,
                "numTerritoriesClaimed": 0,
                "accountLevel": 8,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "6de76c8a-eac3-4bfa-8dd3-025980962b31",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "07752b065e7f4b8197eacca14cba8784",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Smertanosec70",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "b71ea940-1d14-4f05-9e8d-16272a1efc0b",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
                    "level": 10,
                    "skillLevel": 1,
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
                      "level": 8,
                      "perks": [
                        0,
                        3,
                        2,
                        2,
                        0,
                        0,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-28T20:16:33.696Z",
                "numLevelsCompleted": 6,
                "numTerritoriesClaimed": 0,
                "accountLevel": 8,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "24651fbf-1cb8-4195-b073-0424ca5e03f0",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "52446d9eea814e94952d94b033c3046c",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "yppuphtead",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "0cc04078-95bc-4c07-93dc-c537bfdbcf0c",
                    "templateId": "Character:Warrior_Starter_Nature_PowerStrike_T03",
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
                      "level": 8,
                      "perks": [
                        0,
                        5,
                        1,
                        1,
                        0,
                        0,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-28T17:10:25.797Z",
                "numLevelsCompleted": 7,
                "numTerritoriesClaimed": 0,
                "accountLevel": 8,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "dfceb4b3-395a-4da0-be39-d53d99337cdf",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "c6b01570d50742ef8b5ba52e5463b66c",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "cool_nrdir",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "acf2e0ee-3a0f-4722-9a0e-b2ca480ff1fb",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
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
                      "level": 8,
                      "perks": [
                        0,
                        3,
                        3,
                        1,
                        0,
                        0,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-28T16:20:18.913Z",
                "numLevelsCompleted": 6,
                "numTerritoriesClaimed": 0,
                "accountLevel": 8,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "14523a4e-033d-4b40-a2b1-70361bba25a9",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "33c85b62c22c40c3a1676d5de19514c3",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Ylianobanano",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "8b818411-2419-4620-8d63-e23414a8379f",
                    "templateId": "Character:Mage_Starter_Fire_BurningSwordCombo_T03",
                    "bIsCommander": true,
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
                      "level": 8,
                      "perks": [
                        0,
                        3,
                        2,
                        1,
                        0,
                        2,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-28T15:12:40.272Z",
                "numLevelsCompleted": 7,
                "numTerritoriesClaimed": 0,
                "accountLevel": 8,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "7d9055f6-8e5f-4b6f-842f-ac489cb67fe7",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "73de29cf39e245178647d4acc8e55509",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Diego Malone",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "97ea33c9-25e8-4564-a418-7b596e3d4d75",
                    "templateId": "Character:Warrior_Starter_Nature_PowerStrike_T03",
                    "bIsCommander": true,
                    "level": 10,
                    "skillLevel": 1,
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
                      "level": 8,
                      "perks": [
                        0,
                        2,
                        3,
                        1,
                        0,
                        1,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-28T07:08:46.159Z",
                "numLevelsCompleted": 7,
                "numTerritoriesClaimed": 0,
                "accountLevel": 8,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "485c1d6d-33b7-4c52-b4ee-c63a7e3ea370",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "0f329ec9d2ca4ce298ddfd5bbe287383",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Fire_Raider285",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "ebe7b194-5c39-4a00-be25-2937adacffaa",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
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
                      "level": 8,
                      "perks": [
                        0,
                        2,
                        3,
                        0,
                        0,
                        2,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-28T02:54:25.242Z",
                "numLevelsCompleted": 6,
                "numTerritoriesClaimed": 0,
                "accountLevel": 8,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "7c7ee96e-be58-43cc-9a54-1fdf98da2948",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "a1270eee6303481ab7f4c2b203ec710e",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Mi ID 141992811",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "b498a890-bd06-4b7f-9b5c-00303f85be82",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
                    "level": 10,
                    "skillLevel": 1,
                    "upgrades": [
                      5,
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
                      "level": 8,
                      "perks": [
                        0,
                        5,
                        0,
                        1,
                        0,
                        1,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-28T00:26:09.860Z",
                "numLevelsCompleted": 8,
                "numTerritoriesClaimed": 0,
                "accountLevel": 8,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "5eea2c6f-e7fa-4523-89cb-d27f86228191",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "ef8a063a6cc94c7591a5dbd6fcdf1c5a",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Que me miras 3",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "1a8ea113-fac8-4de1-a40d-8a0fae7dca96",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
                    "level": 10,
                    "skillLevel": 1,
                    "upgrades": [
                      4,
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
                      "level": 8,
                      "perks": [
                        0,
                        3,
                        1,
                        1,
                        0,
                        2,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-27T20:03:03.531Z",
                "numLevelsCompleted": 11,
                "numTerritoriesClaimed": 0,
                "accountLevel": 8,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "dad6cd5c-3cd1-40c2-9676-e32acd415e36",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "eed0a5bfa4da48caaca952acc8eb50ad",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Ekaderix",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "c9bb6a74-45b5-4473-9daa-4c41d084225e",
                    "templateId": "Character:Archer_Starter_Water_MultiShot_T03",
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
                      "level": 8,
                      "perks": [
                        0,
                        1,
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
                  }
                ],
                "lastPlayTime": "2022-12-27T09:28:01.920Z",
                "numLevelsCompleted": 8,
                "numTerritoriesClaimed": 0,
                "accountLevel": 8,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "87e13106-44c4-4c5f-980a-0bb3cbb203b7",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "22a99f1efbd844cea0bd38ca54ff9d2a",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Playrobert55",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "b9530e7f-3e71-4917-a2f6-b23c0675a6fb",
                    "templateId": "Character:Archer_Starter_Water_MultiShot_T03",
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
                      "level": 8,
                      "perks": [
                        0,
                        2,
                        3,
                        1,
                        0,
                        1,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-27T04:53:52.529Z",
                "numLevelsCompleted": 7,
                "numTerritoriesClaimed": 0,
                "accountLevel": 8,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "c51ad91c-9370-4f42-b70d-3726554001ca",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "5ad09e03868246c18716a997e66abcfe",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "Aaron peez",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "e0398795-4bb9-4848-8fcf-8820a7e6b551",
                    "templateId": "Character:Warrior_Starter_Nature_PowerStrike_T03",
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
                      "level": 8,
                      "perks": [
                        0,
                        1,
                        2,
                        2,
                        0,
                        2,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-27T00:53:35.223Z",
                "numLevelsCompleted": 6,
                "numTerritoriesClaimed": 0,
                "accountLevel": 8,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "5c021950-f8fc-4958-b6ac-388fa2fef228",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "045d4c5ac3e6486fb318e076cb979f32",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "PTAK-5.5",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "bc1ed0e7-8db3-4097-9569-57e662c10104",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
                    "level": 10,
                    "skillLevel": 1,
                    "upgrades": [
                      25,
                      25,
                      25,
                      25,
                      4,
                      0,
                      0,
                      0,
                      0
                    ],
                    "accountInfo": {
                      "level": 7,
                      "perks": [
                        1,
                        6,
                        5,
                        5,
                        2,
                        1,
                        1,
                        1
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-29T00:01:26.297Z",
                "numLevelsCompleted": 7,
                "numTerritoriesClaimed": 0,
                "accountLevel": 7,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "cb77fb67-4278-490c-8024-6a1939916b7b",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "e6e1b3a68bf04fc2bfb891e4c08d151e",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "NeroNai00",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "e4b683c5-6cdb-4f69-8902-cd11b847218e",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
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
                      "level": 7,
                      "perks": [
                        0,
                        2,
                        2,
                        2,
                        0,
                        0,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-27T21:52:32.315Z",
                "numLevelsCompleted": 5,
                "numTerritoriesClaimed": 0,
                "accountLevel": 7,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        },
        {
          "changeType": "itemAdded",
          "itemId": "490076f7-f9c5-4f35-8e4b-643d835f419b",
          "item": {
            "templateId": "Friend:Instance",
            "attributes": {
              "lifetime_claimed": 0,
              "accountId": "46da798790a349a29107bebc1278d561",
              "canBeSparred": false,
              "snapshot_expires": "2022-12-29T16:24:37.240Z",
              "best_gift": 0,
              "lifetime_gifted": 0,
              "snapshot": {
                "displayName": "ItzaLuxe",
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": [
                  {
                    "itemId": "1d623fa9-54fd-4c19-a495-75d25292a1fa",
                    "templateId": "Character:Mage_Starter_Fire_Fireball_T03",
                    "bIsCommander": true,
                    "level": 10,
                    "skillLevel": 1,
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
                      "level": 7,
                      "perks": [
                        0,
                        2,
                        3,
                        1,
                        0,
                        0,
                        0,
                        0
                      ]
                    },
                    "foilLevel": -1,
                    "gearTemplateId": ""
                  }
                ],
                "lastPlayTime": "2022-12-27T08:27:15.367Z",
                "numLevelsCompleted": 7,
                "numTerritoriesClaimed": 0,
                "accountLevel": 7,
                "numRepHeroes": 1,
                "isPvPUnlocked": false
              },
              "remoteFriendId": "",
              "status": "Suggested",
              "gifts": {}
            },
            "quantity": 1
          }
        }
      ],
      "profileCommandRevision": 1
    },
    {
      "profileRevision": 3,
      "profileId": "levels",
      "profileChangesBaseRevision": 1,
      "profileChanges": [
        {
          "changeType": "statModified",
          "name": "personal_events",
          "value": [
            {
              "expiresAt": "2023-03-28T16:55:45.264Z",
              "sortPriority": 5,
              "zoneId": "Zone.Event.PE.MidgamePet.First.Map1",
              "maxRuns": 1,
              "resetCostMtx": 0,
              "eventKey": "ea2894c5-9f3d-490e-8895-69d869eea350",
              "flags": [],
              "dynamicTier": -1,
              "dynamicGoldTier": -1,
              "dynamicWorldLevel": -1
            },
            {
              "expiresAt": "2023-03-28T16:55:45.264Z",
              "sortPriority": 4,
              "zoneId": "Zone.Event.PE.MidgamePet.Second.Map1",
              "maxRuns": 1,
              "resetCostMtx": 0,
              "eventKey": "ea2894c5-9f3d-490e-8895-69d869eea350",
              "flags": [],
              "dynamicTier": -1,
              "dynamicGoldTier": -1,
              "dynamicWorldLevel": -1
            },
            {
              "expiresAt": "2023-03-28T16:55:45.264Z",
              "sortPriority": 3,
              "zoneId": "Zone.Event.PE.MidgamePet.Third.Map1",
              "maxRuns": 1,
              "resetCostMtx": 0,
              "eventKey": "ea2894c5-9f3d-490e-8895-69d869eea350",
              "flags": [],
              "dynamicTier": -1,
              "dynamicGoldTier": -1,
              "dynamicWorldLevel": -1
            },
            {
              "expiresAt": "2023-03-28T16:55:45.264Z",
              "sortPriority": 2,
              "zoneId": "Zone.Event.PE.MidgamePet.Fourth.Map1",
              "maxRuns": 1,
              "resetCostMtx": 0,
              "eventKey": "ea2894c5-9f3d-490e-8895-69d869eea350",
              "flags": [],
              "dynamicTier": -1,
              "dynamicGoldTier": -1,
              "dynamicWorldLevel": -1
            },
            {
              "expiresAt": "2023-03-28T16:55:45.264Z",
              "sortPriority": 1,
              "zoneId": "Zone.Event.PE.MidgamePet.Fifth.Map1",
              "maxRuns": 1,
              "resetCostMtx": 0,
              "eventKey": "ea2894c5-9f3d-490e-8895-69d869eea350",
              "flags": [],
              "dynamicTier": -1,
              "dynamicGoldTier": -1,
              "dynamicWorldLevel": -1
            },
            {
              "expiresAt": "2023-03-28T16:55:45.265Z",
              "sortPriority": 5,
              "zoneId": "Zone.Event.PE.MidgameChallenge.First.Map1",
              "maxRuns": 1,
              "resetCostMtx": 0,
              "eventKey": "614f498f-e93b-47fb-8399-4a8ad35be995",
              "flags": [],
              "dynamicTier": -1,
              "dynamicGoldTier": -1,
              "dynamicWorldLevel": -1
            },
            {
              "expiresAt": "2023-03-28T16:55:45.265Z",
              "sortPriority": 4,
              "zoneId": "Zone.Event.PE.MidgameChallenge.Second.Map1",
              "maxRuns": 1,
              "resetCostMtx": 0,
              "eventKey": "614f498f-e93b-47fb-8399-4a8ad35be995",
              "flags": [],
              "dynamicTier": -1,
              "dynamicGoldTier": -1,
              "dynamicWorldLevel": -1
            },
            {
              "expiresAt": "2023-03-28T16:55:45.265Z",
              "sortPriority": 3,
              "zoneId": "Zone.Event.PE.MidgameChallenge.Third.Map1",
              "maxRuns": 1,
              "resetCostMtx": 0,
              "eventKey": "614f498f-e93b-47fb-8399-4a8ad35be995",
              "flags": [],
              "dynamicTier": -1,
              "dynamicGoldTier": -1,
              "dynamicWorldLevel": -1
            },
            {
              "expiresAt": "2023-03-28T16:55:45.265Z",
              "sortPriority": 2,
              "zoneId": "Zone.Event.PE.MidgameChallenge.Fourth.Map1",
              "maxRuns": 1,
              "resetCostMtx": 0,
              "eventKey": "614f498f-e93b-47fb-8399-4a8ad35be995",
              "flags": [],
              "dynamicTier": -1,
              "dynamicGoldTier": -1,
              "dynamicWorldLevel": -1
            },
            {
              "expiresAt": "2023-03-28T16:55:45.265Z",
              "sortPriority": 1,
              "zoneId": "Zone.Event.PE.MidgameChallenge.Fifth.Map1",
              "maxRuns": 1,
              "resetCostMtx": 0,
              "eventKey": "614f498f-e93b-47fb-8399-4a8ad35be995",
              "flags": [],
              "dynamicTier": -1,
              "dynamicGoldTier": -1,
              "dynamicWorldLevel": -1
            },
            {
              "expiresAt": "2023-01-12T13:24:37.296Z",
              "sortPriority": 8,
              "zoneId": "Zone.Event.NewPlayer.Map1",
              "maxRuns": 1,
              "resetCostMtx": 0,
              "eventKey": "4c08026d-88ea-416a-8477-340b9c2c73c6",
              "flags": [],
              "dynamicTier": -1,
              "dynamicGoldTier": -1,
              "dynamicWorldLevel": -1
            },
            {
              "expiresAt": "2023-01-12T13:24:37.296Z",
              "sortPriority": 7,
              "zoneId": "Zone.Event.NewPlayer.Map2",
              "maxRuns": 1,
              "resetCostMtx": 0,
              "eventKey": "4c08026d-88ea-416a-8477-340b9c2c73c6",
              "flags": [],
              "dynamicTier": -1,
              "dynamicGoldTier": -1,
              "dynamicWorldLevel": -1
            },
            {
              "expiresAt": "2023-01-12T13:24:37.296Z",
              "sortPriority": 6,
              "zoneId": "Zone.Event.NewPlayer.Map3",
              "maxRuns": 1,
              "resetCostMtx": 0,
              "eventKey": "4c08026d-88ea-416a-8477-340b9c2c73c6",
              "flags": [],
              "dynamicTier": -1,
              "dynamicGoldTier": -1,
              "dynamicWorldLevel": -1
            },
            {
              "expiresAt": "2023-01-12T13:24:37.296Z",
              "sortPriority": 5,
              "zoneId": "Zone.Event.NewPlayer.Map4",
              "maxRuns": 1,
              "resetCostMtx": 0,
              "eventKey": "4c08026d-88ea-416a-8477-340b9c2c73c6",
              "flags": [],
              "dynamicTier": -1,
              "dynamicGoldTier": -1,
              "dynamicWorldLevel": -1
            },
            {
              "expiresAt": "2023-01-12T13:24:37.296Z",
              "sortPriority": 4,
              "zoneId": "Zone.Event.NewPlayer.Map5",
              "maxRuns": 1,
              "resetCostMtx": 0,
              "eventKey": "4c08026d-88ea-416a-8477-340b9c2c73c6",
              "flags": [],
              "dynamicTier": -1,
              "dynamicGoldTier": -1,
              "dynamicWorldLevel": -1
            },
            {
              "expiresAt": "2023-01-12T13:24:37.296Z",
              "sortPriority": 3,
              "zoneId": "Zone.Event.NewPlayer.Map6",
              "maxRuns": 1,
              "resetCostMtx": 0,
              "eventKey": "4c08026d-88ea-416a-8477-340b9c2c73c6",
              "flags": [],
              "dynamicTier": -1,
              "dynamicGoldTier": -1,
              "dynamicWorldLevel": -1
            },
            {
              "expiresAt": "2023-01-12T13:24:37.296Z",
              "sortPriority": 2,
              "zoneId": "Zone.Event.NewPlayer.Map7",
              "maxRuns": 1,
              "resetCostMtx": 0,
              "eventKey": "4c08026d-88ea-416a-8477-340b9c2c73c6",
              "flags": [],
              "dynamicTier": -1,
              "dynamicGoldTier": -1,
              "dynamicWorldLevel": -1
            },
            {
              "expiresAt": "2023-01-12T13:24:37.296Z",
              "sortPriority": 1,
              "zoneId": "Zone.Event.NewPlayer.Map8",
              "maxRuns": 1,
              "resetCostMtx": 0,
              "eventKey": "4c08026d-88ea-416a-8477-340b9c2c73c6",
              "flags": [],
              "dynamicTier": -1,
              "dynamicGoldTier": -1,
              "dynamicWorldLevel": -1
            }
          ]
        }
      ],
      "profileCommandRevision": 1
    }
  ],
  "responseVersion": 1
}
```

*Response body was encoded in base64*

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
