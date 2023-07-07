# Display Name Lookup

#####

*https://account-public-service-prod.ol.epicgames.com/account/api/public/account/displayName/:displayName*

___

## Request

```http
GET /account/api/public/account/displayName/:displayName HTTP/1.1
```

### Path Parameters

| Name        | Value        |
|-------------|--------------|
| displayName | Display Name |

### Request Headers

| Name                  | Value                                                                                                                 |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------|
| Host                  | account-public-service-prod.ol.epicgames.com                                                                          |
| Accept                | \*/\*                                                                                                                 |
| Accept-Encoding       | deflate, gzip                                                                                                         |
| Content-Type          | text/plain                                                                                                            |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-420FE66A4AACA5058BA3B193D82F56CE-7E4F771A44D59856377E14A9840B9043                |
| User-Agent            | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit                                                      |
| Authorization         | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |
| Content-Length        | 0                                                                                                                     |

### Request Body

```text

```

___

## Response

#### Status: 404 Not Found

### Response Headers

| Name                  | Value                                                                                                  |
|-----------------------|--------------------------------------------------------------------------------------------------------|
| Date                  | Tue, 27 Dec 2022 06:09:06 GMT                                                                          |
| Content-Type          | application/json;charset=utf-8                                                                         |
| Content-Length        | 233                                                                                                    |
| X-Epic-Error-Code     | 18007                                                                                                  |
| X-Epic-Error-Name     | errors.com.epicgames.account.account_not_found                                                         |
| Cache-Control         | no-cache, no-store, no-transform                                                                       |
| X-Epic-Device-ID      | 68009daed09498667a8039cce09983ed                                                                       |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-420FE66A4AACA5058BA3B193D82F56CE-7E4F771A44D59856377E14A9840B9043 |
| Connection            | keep-alive                                                                                             |

### Response Body

```json
{
  "errorCode": "errors.com.epicgames.account.account_not_found",
  "errorMessage": "Sorry, we couldn't find an account for  ",
  "messageVars": [
    " "
  ],
  "numericErrorCode": 18007,
  "originatingService": "com.epicgames.account.public",
  "intent": "prod"
}
```

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
