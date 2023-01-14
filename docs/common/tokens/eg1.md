# eg1~token

This [JWT](https://jwt.io/introduction) token is used to authenticate with the majority of endpoints

### Example

```text
bearer eg1~eyJraWQiOiJ0RkMyVUloRnBUTV9FYTNxY09kX01xUVQxY0JCbTlrRkxTRGZlSmhzUkc4IiwiYWxnIjoiUFMyNTYifQ.eyJhcHxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxNSJ9.AHS7KVubDlyEcy3ZM4XyXPivUivLqrBrGe7NrDkqJVcnj4HFpcQs-U6a19rJ2lZNdzTgt3I_8wHQYt7YZd1pny4M
```

### Details

The token is a JSON Web token. It's Base64URL encoded in 3 parts:

Header (algorithm + token type)

```json
{
  "kid": "tFC2UIhFpTM_Ea3qcOd_MqQT1cBBm9kFLSDfeJhsRG8",
  "alg": "PS256"
}
```

Payload

```json
{
  "app": "wex",
  "sub": "690xxxxxxxxxxxxxxxxxxxxxxxxxca11",
  "dvid": "680xxxxxxxxxxxxxxxxxxxxxxxxxc3ed",
  "mver": false,
  "clid": "3cf78cd3b00b439a8755a878b160c7ad",
  "dn": "display name here",
  "am": "exchange_code",
  "p": "eNqVUsxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxEIrnYg==",
  "iai": "690xxxxxxxxxxxxxxxxxxxxxxxxxca11",
  "sec": 1,
  "clsvc": "wex",
  "t": "s",
  "ic": true,
  "exp": 1672348766,
  "iat": 1672319966,
  "jti": "cb0xxxxxxxxxxxxxxxxxxxxxxxxxc375"
}
```

Signature

```py
RSAPSSSHA256(base64UrlEncode(header) + "." + base64UrlEncode(payload), public_key, private_key)
```

#### Permissions:

Depends...