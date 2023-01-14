# Hi

#####

*https://account-public-service-prod.ol.epicgames.com/account/api/public/account/displayName/hi*

___

## Request

```http request
GET /account/api/public/account/displayName/hi HTTP/1.1
```





### Request Headers

| Name | Value |
|---|---|
| Host | account-public-service-prod.ol.epicgames.com |
| Accept | \*/\* |
| Accept-Encoding | deflate, gzip |
| Content-Type | text/plain |
| X-Epic-Correlation-ID | UE4-550659054c6fbbba966be789c8ecf002-D77C844B4D0785D0053F3CBFB86C4B7D-9101BAAA4DDE6D7348D47D89CD5FE641 |
| User-Agent | WorldExplorers/1.88.244-r17036752 Windows/10.0.25267.1.256.64bit |
| Authorization | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |
| Content-Length | 0 |


### Request Body

```text

```

___

## Response

#### Status: 404 Not Found




### Response Headers

| Name | Value |
|---|---|
| Date | Sat, 17 Dec 2022 13:36:27 GMT |
| Content-Type | application/json;charset=utf-8 |
| Content-Length | 235 |
| X-Epic-Error-Code | 18007 |
| X-Epic-Error-Name | errors.com.epicgames.account.account_not_found |
| Cache-Control | no-cache, no-store, no-transform |
| X-Epic-Device-ID | 7b6449837a601db90694fa85168cb856 |
| X-Epic-Correlation-ID | UE4-550659054c6fbbba966be789c8ecf002-D77C844B4D0785D0053F3CBFB86C4B7D-9101BAAA4DDE6D7348D47D89CD5FE641 |
| Connection | keep-alive |


### Response Body

```json
{
  "errorCode": "errors.com.epicgames.account.account_not_found",
  "errorMessage": "Sorry, we couldn't find an account for hi",
  "messageVars": [
    "hi"
  ],
  "numericErrorCode": 18007,
  "originatingService": "com.epicgames.account.public",
  "intent": "prod"
}
```

*Response body was encoded in base64*

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
