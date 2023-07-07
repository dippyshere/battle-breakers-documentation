# Token

#####

*https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token*

___

## Request

```http
POST /account/api/oauth/token HTTP/1.1
```

### Request Headers

| Name                  | Value                                                                                                                                                                                                         |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Host                  | account-public-service-prod.ol.epicgames.com                                                                                                                                                                  |
| Accept                | \*/\*                                                                                                                                                                                                         |
| Accept-Encoding       | deflate, gzip                                                                                                                                                                                                 |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-8F1914244DA67F48B5E1009A0D2C3E0A                                                                                                        |
| User-Agent            | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit                                                                                                                                              |
| Content-Type          | application/x-www-form-urlencoded                                                                                                                                                                             |
| Authorization         | basic [M2NmNzhjZDNiMDBiNDM5YTg3NTVhODc4YjE2MGM3YWQ6YjM4M2UwZjQtZjBjYy00ZDE0LTk5ZTMtODEzYzMzZmMxZTlk](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/wexclient.md) |
| X-Epic-Device-ID      | 68009daed09498667a8039cce09983ed                                                                                                                                                                              |
| Content-Length        | 86                                                                                                                                                                                                            |

### Request Body

| Name          | Value                                                                                                                 |
|---------------|-----------------------------------------------------------------------------------------------------------------------|
| grant_type    | exchange_code                                                                                                         |
| exchange_code | [exchange...](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/exchange.md) |
| token_type    | eg1                                                                                                                   |

___

## Response

#### Status: 200 OK

### Response Headers

| Name                  | Value                                                                                                  |
|-----------------------|--------------------------------------------------------------------------------------------------------|
| Date                  | Thu, 29 Dec 2022 05:42:50 GMT                                                                          |
| Content-Type          | application/json                                                                                       |
| Content-Length        | 2484                                                                                                   |
| Cache-Control         | no-cache, no-store, no-transform                                                                       |
| X-Epic-Device-ID      | 68009daed09498667a8039cce09983ed                                                                       |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-8F1914244DA67F48B5E1009A0D2C3E0A |
| Connection            | keep-alive                                                                                             |

### Response Body

```json
{
  "access_token": "eg1~token...",
  "expires_in": 28800,
  "expires_at": "2022-12-29T13:42:50.142Z",
  "token_type": "bearer",
  "refresh_token": "eg1~token...",
  "refresh_expires": 115200,
  "refresh_expires_at": "2022-12-30T13:42:50.146Z",
  "account_id": "ec0ebb7e56f6454e86c62299a7b32e21",
  "client_id": "3cf78cd3b00b439a8755a878b160c7ad",
  "internal_client": true,
  "client_service": "wex",
  "displayName": "Dippyshere",
  "ext_auth_id": "111111111111111111111",
  "ext_auth_type": "exchange_code",
  "ext_auth_method": "google_id_token",
  "ext_auth_display_name": "Name",
  "app": "wex",
  "in_app_id": "ec0ebb7e56f6454e86c62299a7b32e21",
  "device_id": "68009daed09498667a8039cce09983ed"
}
```

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
