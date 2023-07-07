# Account Id

#####

*https://account-public-service-prod.ol.epicgames.com/account/api/public/account/:accountId*

___

## Request

```http
GET /account/api/public/account/:accountId HTTP/1.1
```

### Path Parameters

| Name     | Value                             |
|----------|-----------------------------------|
| acountId | ec0ebb7e56f6454e86c62299a7b32e21  |

### Request Headers

| Name                  | Value                                                                                                                 |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------|
| Host                  | account-public-service-prod.ol.epicgames.com                                                                          |
| Accept                | \*/\*                                                                                                                 |
| Accept-Encoding       | deflate, gzip                                                                                                         |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-942378154110DD544DE89092A9DFE100                |
| User-Agent            | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit                                                      |
| Content-Type          | application/json                                                                                                      |
| Authorization         | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |
| Content-Length        | 0                                                                                                                     |

___

## Response

#### Status: 200 OK

### Response Headers

| Name                  | Value                                                                                                  |
|-----------------------|--------------------------------------------------------------------------------------------------------|
| Date                  | Thu, 29 Dec 2022 05:42:50 GMT                                                                          |
| Content-Type          | application/json                                                                                       |
| Content-Length        | 594                                                                                                    |
| Cache-Control         | no-cache, no-store, no-transform                                                                       |
| X-Epic-Device-ID      | 68009daed09498667a8039cce09983ed                                                                       |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-942378154110DD544DE89092A9DFE100 |
| Connection            | keep-alive                                                                                             |

### Response Body

```json
{
  "id": "ec0ebb7e56f6454e86c62299a7b32e21",
  "displayName": "Dippyshere",
  "name": "Name",
  "email": "email@gmail.com",
  "failedLoginAttempts": 0,
  "lastLogin": "2022-12-28T11:31:00.246Z",
  "numberOfDisplayNameChanges": 1,
  "dateOfBirth": "YYYY-MM-DD",
  "ageGroup": "ADULT",
  "headless": false,
  "country": "AU",
  "lastName": "Name",
  "phoneNumber": "Number",
  "preferredLanguage": "en",
  "lastDisplayNameChange": "2018-12-13T09:40:54.555Z",
  "canUpdateDisplayName": true,
  "tfaEnabled": false,
  "emailVerified": true,
  "minorVerified": false,
  "minorExpected": false,
  "minorStatus": "NOT_MINOR",
  "cabinedMode": false,
  "hasHashedEmail": false
}
```

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
