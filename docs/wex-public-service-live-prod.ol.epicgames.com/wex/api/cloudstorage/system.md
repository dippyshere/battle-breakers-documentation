# System

#####

*https://wex-public-service-live-prod.ol.epicgames.com/wex/api/cloudstorage/system*



___

## Request

```http request
GET /wex/api/cloudstorage/system HTTP/1.1
```





### Request Headers

| Name | Value |
|---|---|
| Host | wex-public-service-live-prod.ol.epicgames.com |
| Accept | \*/\* |
| Accept-Encoding | deflate, gzip |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-7A6E98274DD070B2CE3ABE813636A5E7 |
| User-Agent | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit |
| Authorization | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |
| Content-Length | 0 |



___

## Response

#### Status: 200 OK




### Response Headers

| Name | Value |
|---|---|
| Date | Thu, 29 Dec 2022 05:42:47 GMT |
| Content-Type | application/json |
| Content-Length | 684 |
| X-EpicGames-McpVersion | prod Release-1.88-1.88 build 107 cl 19310354 |
| X-EpicGames-ContentVersion | 1.88.244-r17036752 |
| X-EpicGames-MinBuild | 17036752 |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-7A6E98274DD070B2CE3ABE813636A5E7 |
| Connection | keep-alive |


### Response Body

```json
[
  {
    "uniqueFilename": "a6b5e5b09d0b426db3616c919b2af9b0",
    "filename": "DefaultEngine.ini",
    "hash": "ac740e157b4ef5c578e76f50ee8997ffb5c9f442",
    "hash256": "ab74b8b51e673b3fa8095192e6463de35e6683fcaacf38538bd0392f6e6b9894",
    "length": 137,
    "contentType": "application/octet-stream",
    "uploaded": "2019-12-15T19:36:11.935Z",
    "storageType": "S3",
    "doNotCache": false
  },
  {
    "uniqueFilename": "b91b0a42b48740bfaaf0acae1df48cb1",
    "filename": "DefaultGame.ini",
    "hash": "3e985d66a070a1c9b9aab16a7210c81a7f6b6754",
    "hash256": "6037e7333f5dbf974e2b24148232f52d594a99b1db402f4a9af485f7b8e46527",
    "length": 1004,
    "contentType": "application/octet-stream",
    "uploaded": "2019-11-19T02:12:44.627Z",
    "storageType": "S3",
    "doNotCache": false
  }
]
```

*Response body was encoded in base64*

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
