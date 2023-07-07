# Friend Summary

#####

*https://friends-public-service-prod.ol.epicgames.com/friends/api/v1/:accountId/summary*

___

## Request

```http
GET /friends/api/v1/:accountId/summary HTTP/1.1
```

### Path Parameters

| Name     | Value                             |
|----------|-----------------------------------|
| acountId | ec0ebb7e56f6454e86c62299a7b32e21  |

### Request Headers

| Name                  | Value                                                                                                                 |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------|
| Host                  | friends-public-service-prod.ol.epicgames.com                                                                          |
| Accept                | \*/\*                                                                                                                 |
| Accept-Encoding       | deflate, gzip                                                                                                         |
| Content-Type          | application/json                                                                                                      |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-F474E41340900BD7AA6659AAB784FCEA                |
| User-Agent            | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit                                                      |
| Authorization         | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |
| Content-Length        | 0                                                                                                                     |

___

## Response

#### Status: 200 OK

### Response Headers

| Name                  | Value                                                                                                  |
|-----------------------|--------------------------------------------------------------------------------------------------------|
| Date                  | Thu, 29 Dec 2022 05:43:43 GMT                                                                          |
| Content-Type          | application/json                                                                                       |
| Transfer-Encoding     | chunked                                                                                                |
| X-Epic-Device-ID      | 68009daed09498667a8039cce09983ed                                                                       |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-F474E41340900BD7AA6659AAB784FCEA |
| Connection            | keep-alive                                                                                             |

### Response Body

```json
{
  "friends": [
    {
      "accountId": "58067600bef64139a0144493364eb25b",
      "groups": [],
      "mutual": 0,
      "alias": "",
      "note": "",
      "favorite": false,
      "created": "2019-12-20T04:09:36.949Z"
    },
    {
      "accountId": "1cc85e2d61384b2f8ea494a18bc6446b",
      "groups": [],
      "mutual": 5,
      "alias": "FN Nickname",
      "note": "",
      "favorite": false,
      "created": "2018-06-23T06:53:09.154Z"
    }
  ],
  "incoming": [
    {
      "accountId": "677b63f5976f45da9d8acd8fb073fa8b",
      "mutual": 1,
      "favorite": false,
      "created": "2021-08-18T03:08:09.409Z"
    }
  ],
  "outgoing": [
    {
      "accountId": "13fcd1a4661643ccacb2bdd5e152234b",
      "mutual": 0,
      "favorite": false,
      "created": "2020-02-07T11:09:41.474Z"
    }
  ],
  "suggested": [
    {
      "accountId": "c3358eb46ee14a9ebddb0493286f6dab",
      "mutual": 25
    }
  ],
  "blocklist": [
    {
      "accountId": "85b9500e81b546fa9b0978b53d90675f"
    },
    {
      "accountId": "a5f4958d844946538053d23ec063122a"
    },
    {
      "accountId": "efb703bd474e4bdf85010e883313c78f"
    }
  ],
  "settings": {
    "acceptInvites": "public",
    "mutualPrivacy": "ALL"
  },
  "limitsReached": {
    "incoming": false,
    "outgoing": false,
    "accepted": false
  }
}
```

*Screw the ppl in this blocklist 😠*

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
