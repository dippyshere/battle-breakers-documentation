# Kill Token

#####

*https://account-public-service-prod.ol.epicgames.com/account/api/oauth/sessions/kill/:token*

___

## Request

```http
DELETE /account/api/oauth/sessions/kill/:token HTTP/1.1
```

### Path Parameters

| Name  | Value                                                                                                          |
|-------|----------------------------------------------------------------------------------------------------------------|
| token | [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |

### Request Headers

| Name                  | Value                                                                                                                 |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------|
| Host                  | account-public-service-prod.ol.epicgames.com                                                                          |
| Accept                | \*/\*                                                                                                                 |
| Accept-Encoding       | deflate, gzip                                                                                                         |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-966F8F7C496F70F1928B9C836B801D51                |
| User-Agent            | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit                                                      |
| Content-Type          | application/json                                                                                                      |
| Authorization         | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |
| Content-Length        | 0                                                                                                                     |

___

## Response

#### Status: 204 No Content

### Response Headers

| Name                  | Value                                                                                                  |
|-----------------------|--------------------------------------------------------------------------------------------------------|
| Date                  | Thu, 29 Dec 2022 06:11:18 GMT                                                                          |
| Cache-Control         | no-cache, no-store, no-transform                                                                       |
| X-Epic-Device-ID      | 68009daed09498667a8039cce09983ed                                                                       |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-966F8F7C496F70F1928B9C836B801D51 |
| Connection            | keep-alive                                                                                             |

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
