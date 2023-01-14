# Verify

#####

*https://account-public-service-prod.ol.epicgames.com/account/api/oauth/verify?includePerms=true*



___

## Request

```http request
GET /account/api/oauth/verify?includePerms=true HTTP/1.1
```

### Query String

| Name | Value |
|---|---|
| includePerms | true |




### Request Headers

| Name | Value |
|---|---|
| Host | account-public-service-prod.ol.epicgames.com |
| Accept | \*/\* |
| Accept-Encoding | deflate, gzip |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-5ED322ED4C671FD609E4DEB09D995E27 |
| User-Agent | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit |
| Content-Type | application/json |
| Authorization | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |
| Content-Length | 0 |



___

## Response

#### Status: 200 OK




### Response Headers

| Name | Value |
|---|---|
| Date | Thu, 29 Dec 2022 06:09:54 GMT |
| Content-Type | application/json |
| Transfer-Encoding | chunked |
| Vary | Accept-Encoding |
| Cache-Control | no-cache, no-store, no-transform |
| X-Epic-Device-ID | 68009daed09498667a8039cce09983ed |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-5ED322ED4C671FD609E4DEB09D995E27 |
| X-Epic-From-Cache | 1 |
| Content-Encoding | gzip |
| Connection | keep-alive |


### Response Body

```json
{
  "token": "eg1~token...",
  "session_id": "c06ad6d546524b97a1ba082075dc835b",
  "token_type": "bearer",
  "client_id": "3cf78cd3b00b439a8755a878b160c7ad",
  "internal_client": true,
  "client_service": "wex",
  "account_id": "ec0ebb7e56f6454e86c62299a7b32e21",
  "expires_in": 28738,
  "expires_at": "2022-12-29T13:42:49.336Z",
  "auth_method": "exchange_code",
  "display_name": "Dippyshere",
  "ext_auth_id": "111111111111111111111",
  "ext_auth_type": "exchange_code",
  "ext_auth_method": "google_id_token",
  "ext_auth_display_name": "Name",
  "app": "wex",
  "in_app_id": "ec0ebb7e56f6454e86c62299a7b32e21",
  "device_id": "68009daed09498667a8039cce09983ed",
  "perms": [
    {
      "resource": "blockList:ec0ebb7e56f6454e86c62299a7b32e21",
      "action": 14
    },
    {
      "resource": "wexp:cloudstorage:system",
      "action": 2
    },
    {
      "resource": "account:public:account:*",
      "action": 2
    },
    {
      "resource": "account:oauth:exchangeTokenCode",
      "action": 15
    },
    {
      "resource": "account:public:account",
      "action": 2
    },
    {
      "resource": "priceengine:shared:offer:price",
      "action": 2
    },
    {
      "resource": "xmpp:session:*:ec0ebb7e56f6454e86c62299a7b32e21",
      "action": 1
    },
    {
      "resource": "wexp:wexp_role:client",
      "action": 15
    },
    {
      "resource": "wexp:profile:ec0ebb7e56f6454e86c62299a7b32e21:*",
      "action": 15
    },
    {
      "resource": "account:public:account:externalAuths",
      "action": 15
    },
    {
      "resource": "wexp:calendar",
      "action": 2
    },
    {
      "resource": "account:token:otherSessionsForAccountClient",
      "action": 8
    },
    {
      "resource": "account:token:otherSessionsForAccountClientService",
      "action": 8
    },
    {
      "resource": "account:public:account:deviceAuths",
      "action": 11
    },
    {
      "resource": "wexp:cloudstorage:system:*",
      "action": 2
    },
    {
      "resource": "serviceinstance",
      "action": 2
    },
    {
      "resource": "wexp:storefront",
      "action": 2
    },
    {
      "resource": "wexp:push:devices:ec0ebb7e56f6454e86c62299a7b32e21",
      "action": 15
    },
    {
      "resource": "friends:ec0ebb7e56f6454e86c62299a7b32e21",
      "action": 15
    }
  ]
}
```

*Response body was encoded in base64*

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
