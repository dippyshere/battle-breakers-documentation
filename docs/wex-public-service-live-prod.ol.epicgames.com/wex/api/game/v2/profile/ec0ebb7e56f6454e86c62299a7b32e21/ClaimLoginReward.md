# ClaimLoginReward

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/ClaimLoginReward?profileId=profile0&rvn=40314*



___

## Request

```http request
POST /wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/ClaimLoginReward?profileId=profile0&rvn=40314 HTTP/1.1
```

### Query String

| Name | Value |
|---|---|
| profileId | profile0 |
| rvn | 40314 |




### Request Headers

| Name | Value |
|---|---|
| Host | wex-public-service-live-prod.ol.epicgames.com |
| Accept-Encoding | deflate, gzip |
| Accept | \*/\* |
| Content-Type | application/json |
| X-EpicGames-ProfileRevisions | [{"profileId":"profile0","clientCommandRevision":24006},{"profileId":"levels","clientCommandRevision":14476},{"profileId":"friends","clientCommandRevision":8262},{"profileId":"monsterpit","clientCommandRevision":1081},{"profileId":"multiplayer","clientCommandRevision":900}] |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-5C9C30924327232CE4D9978827BE3380 |
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
| Date | Thu, 29 Dec 2022 05:43:30 GMT |
| Content-Type | application/json |
| Content-Length | 5191 |
| X-EpicGames-Profile-Revision | 40314 |
| X-EpicGames-McpVersion | prod Release-1.88-1.88 build 107 cl 19310354 |
| X-EpicGames-ContentVersion | 1.88.244-r17036752 |
| X-EpicGames-MinBuild | 17036752 |
| X-Epic-Device-ID | 68009daed09498667a8039cce09983ed |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-5C9C30924327232CE4D9978827BE3380 |
| Connection | keep-alive |


### Response Body

```json
{
  "profileRevision": 40315,
  "profileId": "profile0",
  "profileChangesBaseRevision": 40314,
  "profileChanges": [
    {
      "changeType": "itemQuantityChanged",
      "itemId": "03e1d076-957e-43f2-9702-71d521413717",
      "quantity": 501
    },
    {
      "changeType": "statModified",
      "name": "login_reward",
      "value": {
        "last_claim_time": "2022-12-29T05:43:30.806Z",
        "next_level": 187
      }
    },
    {
      "changeType": "statModified",
      "name": "hammer_quest_energy",
      "value": {
        "energy_spent": 0,
        "energy_required": 100,
        "claim_count": 0
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
            "EnergySpent": 187
          }
        },
        "b": {
          "date": "2022-12-29T00:00:00.000Z",
          "claimed": false,
          "props": {
            "BaseBonus": 10
          }
        },
        "standardGift": 10
      }
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "f7c3b0c5-d208-4bc4-b6d5-054359784dd0",
      "attributeName": "sealed_days",
      "attributeValue": 0
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "7b899484-837c-4eea-aa0d-a80ce97ae0d7",
      "attributeName": "sealed_days",
      "attributeValue": 0
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "7585df88-2a1e-4ca4-b0ce-33ab0aaac483",
      "attributeName": "sealed_days",
      "attributeValue": 0
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "88721a32-4602-46eb-9662-294610e2e7b5",
      "attributeName": "sealed_days",
      "attributeValue": 0
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "ef81e090-a854-48fd-8924-ef7d07eb0301",
      "attributeName": "sealed_days",
      "attributeValue": 0
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "b8ef336b-e07a-4c41-9b8c-5544746d55d6",
      "attributeName": "sealed_days",
      "attributeValue": 0
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "9b0fffd3-92f3-4018-9799-0bd89c6804c3",
      "attributeName": "sealed_days",
      "attributeValue": 0
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "b83d82de-0cd3-4eac-8cb5-9cfec3360853",
      "attributeName": "sealed_days",
      "attributeValue": 0
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "8b1d13e5-6ee3-4265-96a8-c3e62646a87d",
      "attributeName": "sealed_days",
      "attributeValue": 0
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "dff1fe19-d477-4249-8e2d-258c0df83c78",
      "attributeName": "sealed_days",
      "attributeValue": 0
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "ab0cd5f2-2a8f-47df-8470-0de41c526669",
      "attributeName": "sealed_days",
      "attributeValue": 0
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "881eefbe-f2a5-4646-abb3-c3b74500e94b",
      "attributeName": "sealed_days",
      "attributeValue": 0
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "96f38f41-74dd-4483-a65c-89f2926bd399",
      "attributeName": "sealed_days",
      "attributeValue": 0
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "157e63f4-ba1e-4b3e-9852-bc03eb70087d",
      "attributeName": "sealed_days",
      "attributeValue": 0
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "67ef7c06-d6a8-46fa-9b97-3aa7ea7eca5b",
      "attributeName": "sealed_days",
      "attributeValue": 0
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "37434995-4e63-4c10-ad4c-d19342ed1caa",
      "attributeName": "sealed_days",
      "attributeValue": 0
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "f312dfdf-6d50-42ed-898f-024e45726e7a",
      "attributeName": "sealed_days",
      "attributeValue": 0
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "ac2854b7-ecb2-4451-b683-ff303e98b605",
      "attributeName": "sealed_days",
      "attributeValue": 0
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "517052fe-383b-4c69-97ef-2a7c850e6429",
      "attributeName": "sealed_days",
      "attributeValue": 0
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "ebcfcb8e-7e70-4e05-a0a5-e50b561158d2",
      "attributeName": "sealed_days",
      "attributeValue": 0
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "d922c670-e4c9-4b84-9601-c5f9ec5f3a87",
      "attributeName": "sealed_days",
      "attributeValue": 0
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "b545182f-9443-4a03-a212-95b7d6083067",
      "attributeName": "sealed_days",
      "attributeValue": 0
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "c97235e4-3aab-499c-8b45-9b0c0a2e9a4b",
      "attributeName": "sealed_days",
      "attributeValue": 0
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "e213cc8c-7356-40f7-bef6-9fbadc44efc7",
      "attributeName": "sealed_days",
      "attributeValue": 0
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "1221e7d1-1852-4e8e-9d15-bc29255abb1d",
      "attributeName": "sealed_days",
      "attributeValue": 0
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "372c4622-1b84-4c48-980e-9c42b03ca30b",
      "attributeName": "sealed_days",
      "attributeValue": 0
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "68686864-8ba4-460c-9d89-a7e6b95309ba",
      "attributeName": "sealed_days",
      "attributeValue": 0
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "58c04ea5-b601-4af4-ab83-0e89b7387e15",
      "attributeName": "sealed_days",
      "attributeValue": 0
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "d59ca1b7-3ce9-4053-956b-44d4c0977500",
      "attributeName": "sealed_days",
      "attributeValue": 0
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "cbc1e014-8d1f-434d-8a6b-34bb6128eb4a",
      "attributeName": "sealed_days",
      "attributeValue": 0
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "04535e24-3fb5-4e77-b188-8cf979da47ef",
      "attributeName": "sealed_days",
      "attributeValue": 0
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "736887db-c0b6-459f-af0a-4e6d6a568de2",
      "attributeName": "sealed_days",
      "attributeValue": 0
    },
    {
      "changeType": "itemAttrChanged",
      "itemId": "f25baf81-2fc3-4e2d-940b-b50453ade9c0",
      "attributeName": "sealed_days",
      "attributeValue": 0
    }
  ],
  "profileCommandRevision": 24007,
  "serverTime": "2022-12-29T05:43:30.810Z",
  "responseVersion": 1
}
```

*Response body was encoded in base64*

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
