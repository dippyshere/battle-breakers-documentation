# Version Check

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/v2/versioncheck/Windows?version=1.88.244-r17036752-Windows*

___

## Request

```http
GET /wex/api/v2/versioncheck/Windows?version=1.88.244-r17036752-Windows HTTP/1.1
```

### Query String

| Name    | Value                      |
|---------|----------------------------|
| version | 1.88.244-r17036752-Windows |

### Request Headers

| Name                  | Value                                                                                                                 |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------|
| Host                  | wex-public-service-live-prod.ol.epicgames.com                                                                         |
| Accept                | \*/\*                                                                                                                 |
| Accept-Encoding       | deflate, gzip                                                                                                         |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-3129B4024A3D79B52730849586A7DA8E                |
| User-Agent            | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit                                                      |
| Content-Type          | application/x-www-form-urlencoded                                                                                     |
| Authorization         | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |
| Content-Length        | 0                                                                                                                     |

___

## Response

#### Status: 200 OK

### Response Headers

| Name                       | Value                                                                                                  |
|----------------------------|--------------------------------------------------------------------------------------------------------|
| Date                       | Thu, 29 Dec 2022 05:42:47 GMT                                                                          |
| Content-Type               | application/json                                                                                       |
| Content-Length             | 20                                                                                                     |
| X-EpicGames-McpVersion     | prod Release-1.88-1.88 build 107 cl 19310354                                                           |
| X-EpicGames-ContentVersion | 1.88.244-r17036752                                                                                     |
| X-EpicGames-MinBuild       | 17036752                                                                                               |
| X-Epic-Correlation-ID      | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-3129B4024A3D79B52730849586A7DA8E |
| Connection                 | keep-alive                                                                                             |

### Response Body

```json
{
  "type": "NO_UPDATE"
}
```

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
