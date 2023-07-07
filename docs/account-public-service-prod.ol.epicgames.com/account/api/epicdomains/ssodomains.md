# SSO Domains

#####

*https://account-public-service-prod.ol.epicgames.com/account/api/epicdomains/ssodomains*

___

## Request

```http
GET /account/api/epicdomains/ssodomains HTTP/1.1
```

### Request Headers

| Name                  | Value                                                                                                  |
|-----------------------|--------------------------------------------------------------------------------------------------------|
| Host                  | account-public-service-prod.ol.epicgames.com                                                           |
| Accept                | \*/\*                                                                                                  |
| Accept-Encoding       | deflate, gzip                                                                                          |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-733DB8194AC09416E0DF9BADCD042B8E |
| User-Agent            | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit                                       |
| Content-Type          | application/json                                                                                       |
| Content-Length        | 0                                                                                                      |

___

## Response

#### Status: 200 OK

### Response Headers

| Name                  | Value                                                                                                  |
|-----------------------|--------------------------------------------------------------------------------------------------------|
| Date                  | Thu, 29 Dec 2022 05:42:52 GMT                                                                          |
| Content-Type          | application/json                                                                                       |
| Content-Length        | 74                                                                                                     |
| Cache-Control         | no-cache, no-store, no-transform                                                                       |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-733DB8194AC09416E0DF9BADCD042B8E |
| Connection            | keep-alive                                                                                             |

### Response Body

```json
[
  "unrealengine.com",
  "unrealtournament.com",
  "fortnite.com",
  "epicgames.com"
]
```

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
