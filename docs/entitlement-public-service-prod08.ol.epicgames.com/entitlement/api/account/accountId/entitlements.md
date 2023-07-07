# Entitlements

#####

*https://entitlement-public-service-prod08.ol.epicgames.com/entitlement/api/account/:accountId/entitlements?start=0&count=1000*

___

## Request

```http
GET /entitlement/api/account/:accountId/entitlements?start=0&count=1000 HTTP/1.1
```

### Path Parameters

| Name     | Value                             |
|----------|-----------------------------------|
| acountId | ec0ebb7e56f6454e86c62299a7b32e21  |

### Query String

| Name  | Value |
|-------|-------|
| start | 0     |
| count | 1000  |

### Request Headers

| Name                  | Value                                                                                                                 |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------|
| Host                  | entitlement-public-service-prod08.ol.epicgames.com                                                                    |
| Accept                | \*/\*                                                                                                                 |
| Accept-Encoding       | deflate, gzip                                                                                                         |
| Content-Type          | application/json                                                                                                      |
| X-Epic-Correlation-ID | UE4-550659054c6fbbba966be789c8ecf002-86FC685A47C89527B30A7CBD94D0F3C0-CD82A35D4FFEBC99BB9262B9E867AFAD                |
| User-Agent            | UELauncher/14.4.1-23462965+++Portal+Release-Live Windows/10.0.25267.1.256.64bit                                       |
| Authorization         | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |
| Content-Length        | 0                                                                                                                     |

___

## Response

#### Status: 200 OK

### Response Headers

| Name                  | Value                                                                                                  |
|-----------------------|--------------------------------------------------------------------------------------------------------|
| Date                  | Sat, 17 Dec 2022 14:02:39 GMT                                                                          |
| Content-Type          | application/json                                                                                       |
| Transfer-Encoding     | chunked                                                                                                |
| X-Epic-MaxPageSize    | 1000                                                                                                   |
| X-Epic-Device-ID      | 550659054c6fbbba966be789c8ecf002                                                                       |
| X-Epic-Correlation-ID | UE4-550659054c6fbbba966be789c8ecf002-86FC685A47C89527B30A7CBD94D0F3C0-CD82A35D4FFEBC99BB9262B9E867AFAD |
| Connection            | keep-alive                                                                                             |

### Response Body

```json
[
  {
    "id": "c34cd5d618424cd7bc76dc85f9dba5ca",
    "entitlementName": "WorldExplorers_Free",
    "namespace": "wex",
    "catalogItemId": "e458e71024404176addca212860f9ef2",
    "accountId": "ec0ebb7e56f6454e86c62299a7b32e21",
    "identityId": "ec0ebb7e56f6454e86c62299a7b32e21",
    "entitlementType": "AUDIENCE",
    "grantDate": "2019-11-08T10:47:00.474Z",
    "consumable": false,
    "status": "ACTIVE",
    "active": true,
    "useCount": 0,
    "originalUseCount": 0,
    "platformType": "EPIC",
    "created": "2019-11-08T10:47:00.476Z",
    "updated": "2019-11-08T10:47:00.476Z",
    "groupEntitlement": false,
    "country": "AU"
  },
  {
    "id": "c8dd7751893344e99f46bb53f016c56b",
    "entitlementName": "d3ec04d33f674fd3a7054b6b6b92d6c9",
    "namespace": "wex",
    "catalogItemId": "d3ec04d33f674fd3a7054b6b6b92d6c9",
    "accountId": "ec0ebb7e56f6454e86c62299a7b32e21",
    "identityId": "ec0ebb7e56f6454e86c62299a7b32e21",
    "entitlementType": "ENTITLEMENT",
    "grantDate": "2019-11-21T00:04:20.018Z",
    "consumable": false,
    "status": "ACTIVE",
    "active": true,
    "platformType": "EPIC",
    "created": "2019-11-21T00:04:20.023Z",
    "updated": "2019-11-21T00:04:20.023Z",
    "groupEntitlement": false,
    "country": "AU"
  },
  {
    "id": "eb665de87ac14ffab73aeb96bd333330",
    "entitlementName": "FN_BB_Jess",
    "namespace": "wex",
    "catalogItemId": "3d329b913b3c44cc8f4c5a2fc84e7cf4",
    "accountId": "ec0ebb7e56f6454e86c62299a7b32e21",
    "identityId": "ec0ebb7e56f6454e86c62299a7b32e21",
    "entitlementType": "ENTITLEMENT",
    "grantDate": "2019-12-05T05:59:44.170Z",
    "consumable": false,
    "status": "ACTIVE",
    "active": true,
    "useCount": 0,
    "originalUseCount": 0,
    "platformType": "EPIC",
    "created": "2019-12-05T05:59:44.175Z",
    "updated": "2019-12-05T05:59:44.175Z",
    "groupEntitlement": false,
    "country": "AU"
  },
  {
    "id": "2e02135793fe4413aa1640498211d7c2",
    "entitlementName": "FN_BB_Kyle",
    "namespace": "wex",
    "catalogItemId": "a1689ab49a0d41e1a0828505861d0bb9",
    "accountId": "ec0ebb7e56f6454e86c62299a7b32e21",
    "identityId": "ec0ebb7e56f6454e86c62299a7b32e21",
    "entitlementType": "ENTITLEMENT",
    "grantDate": "2019-12-05T05:59:59.150Z",
    "consumable": false,
    "status": "ACTIVE",
    "active": true,
    "useCount": 0,
    "originalUseCount": 0,
    "platformType": "EPIC",
    "created": "2019-12-05T05:59:59.153Z",
    "updated": "2019-12-05T05:59:59.153Z",
    "groupEntitlement": false,
    "country": "AU"
  }
]
```

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
