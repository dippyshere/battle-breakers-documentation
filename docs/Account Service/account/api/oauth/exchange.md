# Exchange

#####

*https://account-public-service-prod.ol.epicgames.com/account/api/oauth/exchange*

___

## Request

```http
GET /account/api/oauth/exchange HTTP/1.1
```

### Request Headers

| Name                  | Value                                                                                                                 |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------|
| Host                  | account-public-service-prod.ol.epicgames.com                                                                          |
| Accept                | \*/\*                                                                                                                 |
| Accept-Encoding       | deflate, gzip                                                                                                         |
| X-Epic-Correlation-ID | UE4-550659054c6fbbba966be789c8ecf002-D77C844B4D0785D0053F3CBFB86C4B7D-CDA15EF74FCB2BEE69475A8156209142                |
| User-Agent            | WorldExplorers/1.88.244-r17036752 Windows/10.0.25267.1.256.64bit                                                      |
| Content-Type          | application/json                                                                                                      |
| Authorization         | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |
| Content-Length        | 0                                                                                                                     |

___

## Response

#### Status: 200 OK

### Response Headers

| Name                  | Value                                                                                                  |
|-----------------------|--------------------------------------------------------------------------------------------------------|
| Date                  | Sat, 17 Dec 2022 13:55:04 GMT                                                                          |
| Content-Type          | application/json                                                                                       |
| Content-Length        | 120                                                                                                    |
| Cache-Control         | no-cache, no-store, no-transform                                                                       |
| X-Epic-Device-ID      | 7b6449837a601db90694fa85168cb856                                                                       |
| X-Epic-Correlation-ID | UE4-550659054c6fbbba966be789c8ecf002-D77C844B4D0785D0053F3CBFB86C4B7D-CDA15EF74FCB2BEE69475A8156209142 |
| Connection            | keep-alive                                                                                             |

### Response Body

```json
{
  "expiresInSeconds": 299,
  "code": "accesstoken...",
  "creatingClientId": "3cf78cd3b00b439a8755a878b160c7ad"
}
```

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
