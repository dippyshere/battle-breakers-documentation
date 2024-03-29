# Price

#####

*https://priceengine-public-service-prod.ol.epicgames.com/priceengine/api/shared/offers/price*

___

## Request

```http
POST /priceengine/api/shared/offers/price HTTP/1.1
```

### Request Headers

| Name                  | Value                                                                                                                 |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------|
| Host                  | priceengine-public-service-prod.ol.epicgames.com                                                                      |
| Accept                | \*/\*                                                                                                                 |
| Accept-Encoding       | deflate, gzip                                                                                                         |
| Content-Type          | application/json                                                                                                      |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-50436E2E48344CEEBDFB1994EC31942E                |
| User-Agent            | WorldExplorers/1.88.244-r17036752 Windows/10.0.22621.1.256.64bit                                                      |
| Authorization         | bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |
| Content-Length        | 699                                                                                                                   |

### Request Body

```json
{
  "accountId": "ec0ebb7e56f6454e86c62299a7b32e21",
  "calculateTax": false,
  "lineOffers": [
    {
      "offerId": "760156eb63ad49b68861a5b269b73b48",
      "quantity": 1
    },
    {
      "offerId": "395a588577834f4089f14440868a3785",
      "quantity": 1
    },
    {
      "offerId": "7d270c7e78d3439db8afe81bcd0b6b6a",
      "quantity": 1
    },
    {
      "offerId": "b1c1372c9d0a428bacde8161117b1b2c",
      "quantity": 1
    },
    {
      "offerId": "1bb845075f334ecaae7b55e421ab3dea",
      "quantity": 1
    },
    {
      "offerId": "11b1aad3c22d4fe58c361b8c913477d6",
      "quantity": 1
    },
    {
      "offerId": "2be4ab85c1ae42bab895be28ab6cb99e",
      "quantity": 1
    },
    {
      "offerId": "20621749aaa04a49b28a2e68049470cb",
      "quantity": 1
    },
    {
      "offerId": "9d517678254c4b27ab85f0d1d149784b",
      "quantity": 1
    },
    {
      "offerId": "8e60722d2cd54953907351b5a94debc5",
      "quantity": 1
    }
  ],
  "country": "AU"
}
```

___

## Response

#### Status: 200 OK

### Response Headers

| Name                  | Value                                                                                                  |
|-----------------------|--------------------------------------------------------------------------------------------------------|
| Date                  | Thu, 29 Dec 2022 05:43:13 GMT                                                                          |
| Content-Type          | application/json                                                                                       |
| Content-Length        | 6262                                                                                                   |
| X-Epic-Device-ID      | 68009daed09498667a8039cce09983ed                                                                       |
| X-Epic-Correlation-ID | UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-50436E2E48344CEEBDFB1994EC31942E |
| Connection            | keep-alive                                                                                             |

### Response Body

```json
{
  "accountId": "ec0ebb7e56f6454e86c62299a7b32e21",
  "identityId": "ec0ebb7e56f6454e86c62299a7b32e21",
  "namespace": "wex",
  "country": "AU",
  "taxType": "Tax",
  "taxCalculationStatus": "SUCCEEDED",
  "totalPrice": {
    "currencyCode": "AUD",
    "discountPrice": 21110,
    "originalPrice": 21110,
    "discountPercentage": 100,
    "discount": 0,
    "voucherDiscount": 0,
    "sellerVat": 1919,
    "vat": 1919,
    "vatRate": 0.1,
    "convenienceFee": 0,
    "basePayoutPrice": 12948,
    "basePayoutCurrencyCode": "USD",
    "revenueWithoutTax": 12948,
    "revenueWithoutTaxCurrencyCode": "USD",
    "payoutCurrencyExchangeRate": 0.674685939256375
  },
  "totalPaymentPrice": {
    "paymentCurrencyExchangeRate": 1.0,
    "paymentCurrencyCode": "AUD",
    "paymentCurrencySymbol": "$",
    "paymentCurrencyAmount": 21110,
    "paymentCurrencyDecimal": 2
  },
  "coupons": [],
  "lineOffers": [
    {
      "lineId": "1",
      "quantity": 1,
      "taxSkuId": "FR_Game",
      "price": {
        "currencyCode": "AUD",
        "discountPrice": 2195,
        "unitPrice": 2195,
        "originalPrice": 2195,
        "originalUnitPrice": 2195,
        "discountPercentage": 100,
        "discount": 0,
        "voucherDiscount": 0,
        "sellerVat": 200,
        "vat": 200,
        "vatRate": 0.1,
        "convenienceFee": 0,
        "basePayoutPrice": 1346,
        "basePayoutCurrencyCode": "USD",
        "revenueWithoutTax": 1346,
        "revenueWithoutTaxCurrencyCode": "USD",
        "payoutCurrencyExchangeRate": 0.674685939256375
      },
      "offerId": "760156eb63ad49b68861a5b269b73b48",
      "appliedRules": [],
      "ref": "760156eb63ad49b68861a5b269b73b48"
    },
    {
      "lineId": "2",
      "quantity": 1,
      "taxSkuId": "FR_Game",
      "price": {
        "currencyCode": "AUD",
        "discountPrice": 2195,
        "unitPrice": 2195,
        "originalPrice": 2195,
        "originalUnitPrice": 2195,
        "discountPercentage": 100,
        "discount": 0,
        "voucherDiscount": 0,
        "sellerVat": 200,
        "vat": 200,
        "vatRate": 0.1,
        "convenienceFee": 0,
        "basePayoutPrice": 1346,
        "basePayoutCurrencyCode": "USD",
        "revenueWithoutTax": 1346,
        "revenueWithoutTaxCurrencyCode": "USD",
        "payoutCurrencyExchangeRate": 0.674685939256375
      },
      "offerId": "395a588577834f4089f14440868a3785",
      "appliedRules": [],
      "ref": "395a588577834f4089f14440868a3785"
    },
    {
      "lineId": "3",
      "quantity": 1,
      "taxSkuId": "FR_Game",
      "price": {
        "currencyCode": "AUD",
        "discountPrice": 4495,
        "unitPrice": 4495,
        "originalPrice": 4495,
        "originalUnitPrice": 4495,
        "discountPercentage": 100,
        "discount": 0,
        "voucherDiscount": 0,
        "sellerVat": 409,
        "vat": 409,
        "vatRate": 0.1,
        "convenienceFee": 0,
        "basePayoutPrice": 2757,
        "basePayoutCurrencyCode": "USD",
        "revenueWithoutTax": 2757,
        "revenueWithoutTaxCurrencyCode": "USD",
        "payoutCurrencyExchangeRate": 0.674685939256375
      },
      "offerId": "7d270c7e78d3439db8afe81bcd0b6b6a",
      "appliedRules": [],
      "ref": "7d270c7e78d3439db8afe81bcd0b6b6a"
    },
    {
      "lineId": "4",
      "quantity": 1,
      "taxSkuId": "FR_Game",
      "price": {
        "currencyCode": "AUD",
        "discountPrice": 1495,
        "unitPrice": 1495,
        "originalPrice": 1495,
        "originalUnitPrice": 1495,
        "discountPercentage": 100,
        "discount": 0,
        "voucherDiscount": 0,
        "sellerVat": 136,
        "vat": 136,
        "vatRate": 0.1,
        "convenienceFee": 0,
        "basePayoutPrice": 917,
        "basePayoutCurrencyCode": "USD",
        "revenueWithoutTax": 917,
        "revenueWithoutTaxCurrencyCode": "USD",
        "payoutCurrencyExchangeRate": 0.674685939256375
      },
      "offerId": "b1c1372c9d0a428bacde8161117b1b2c",
      "appliedRules": [],
      "ref": "b1c1372c9d0a428bacde8161117b1b2c"
    },
    {
      "lineId": "5",
      "quantity": 1,
      "taxSkuId": "FR_Game",
      "price": {
        "currencyCode": "AUD",
        "discountPrice": 755,
        "unitPrice": 755,
        "originalPrice": 755,
        "originalUnitPrice": 755,
        "discountPercentage": 100,
        "discount": 0,
        "voucherDiscount": 0,
        "sellerVat": 69,
        "vat": 69,
        "vatRate": 0.1,
        "convenienceFee": 0,
        "basePayoutPrice": 463,
        "basePayoutCurrencyCode": "USD",
        "revenueWithoutTax": 463,
        "revenueWithoutTaxCurrencyCode": "USD",
        "payoutCurrencyExchangeRate": 0.674685939256375
      },
      "offerId": "1bb845075f334ecaae7b55e421ab3dea",
      "appliedRules": [],
      "ref": "1bb845075f334ecaae7b55e421ab3dea"
    },
    {
      "lineId": "6",
      "quantity": 1,
      "taxSkuId": "FR_Game",
      "price": {
        "currencyCode": "AUD",
        "discountPrice": 2195,
        "unitPrice": 2195,
        "originalPrice": 2195,
        "originalUnitPrice": 2195,
        "discountPercentage": 100,
        "discount": 0,
        "voucherDiscount": 0,
        "sellerVat": 200,
        "vat": 200,
        "vatRate": 0.1,
        "convenienceFee": 0,
        "basePayoutPrice": 1346,
        "basePayoutCurrencyCode": "USD",
        "revenueWithoutTax": 1346,
        "revenueWithoutTaxCurrencyCode": "USD",
        "payoutCurrencyExchangeRate": 0.674685939256375
      },
      "offerId": "11b1aad3c22d4fe58c361b8c913477d6",
      "appliedRules": [],
      "ref": "11b1aad3c22d4fe58c361b8c913477d6"
    },
    {
      "lineId": "7",
      "quantity": 1,
      "taxSkuId": "FR_Game",
      "price": {
        "currencyCode": "AUD",
        "discountPrice": 2195,
        "unitPrice": 2195,
        "originalPrice": 2195,
        "originalUnitPrice": 2195,
        "discountPercentage": 100,
        "discount": 0,
        "voucherDiscount": 0,
        "sellerVat": 200,
        "vat": 200,
        "vatRate": 0.1,
        "convenienceFee": 0,
        "basePayoutPrice": 1346,
        "basePayoutCurrencyCode": "USD",
        "revenueWithoutTax": 1346,
        "revenueWithoutTaxCurrencyCode": "USD",
        "payoutCurrencyExchangeRate": 0.674685939256375
      },
      "offerId": "2be4ab85c1ae42bab895be28ab6cb99e",
      "appliedRules": [],
      "ref": "2be4ab85c1ae42bab895be28ab6cb99e"
    },
    {
      "lineId": "8",
      "quantity": 1,
      "taxSkuId": "FR_Game",
      "price": {
        "currencyCode": "AUD",
        "discountPrice": 2195,
        "unitPrice": 2195,
        "originalPrice": 2195,
        "originalUnitPrice": 2195,
        "discountPercentage": 100,
        "discount": 0,
        "voucherDiscount": 0,
        "sellerVat": 200,
        "vat": 200,
        "vatRate": 0.1,
        "convenienceFee": 0,
        "basePayoutPrice": 1346,
        "basePayoutCurrencyCode": "USD",
        "revenueWithoutTax": 1346,
        "revenueWithoutTaxCurrencyCode": "USD",
        "payoutCurrencyExchangeRate": 0.674685939256375
      },
      "offerId": "20621749aaa04a49b28a2e68049470cb",
      "appliedRules": [],
      "ref": "20621749aaa04a49b28a2e68049470cb"
    },
    {
      "lineId": "9",
      "quantity": 1,
      "taxSkuId": "FR_Game",
      "price": {
        "currencyCode": "AUD",
        "discountPrice": 395,
        "unitPrice": 395,
        "originalPrice": 395,
        "originalUnitPrice": 395,
        "discountPercentage": 100,
        "discount": 0,
        "voucherDiscount": 0,
        "sellerVat": 36,
        "vat": 36,
        "vatRate": 0.1,
        "convenienceFee": 0,
        "basePayoutPrice": 242,
        "basePayoutCurrencyCode": "USD",
        "revenueWithoutTax": 242,
        "revenueWithoutTaxCurrencyCode": "USD",
        "payoutCurrencyExchangeRate": 0.674685939256375
      },
      "offerId": "9d517678254c4b27ab85f0d1d149784b",
      "appliedRules": [],
      "ref": "9d517678254c4b27ab85f0d1d149784b"
    },
    {
      "lineId": "10",
      "quantity": 1,
      "taxSkuId": "FR_Game",
      "price": {
        "currencyCode": "AUD",
        "discountPrice": 2995,
        "unitPrice": 2995,
        "originalPrice": 2995,
        "originalUnitPrice": 2995,
        "discountPercentage": 100,
        "discount": 0,
        "voucherDiscount": 0,
        "sellerVat": 269,
        "vat": 269,
        "vatRate": 0.1,
        "convenienceFee": 0,
        "basePayoutPrice": 1839,
        "basePayoutCurrencyCode": "USD",
        "revenueWithoutTax": 1839,
        "revenueWithoutTaxCurrencyCode": "USD",
        "payoutCurrencyExchangeRate": 0.674685939256375
      },
      "offerId": "8e60722d2cd54953907351b5a94debc5",
      "appliedRules": [],
      "ref": "8e60722d2cd54953907351b5a94debc5"
    }
  ],
  "isB2bVatReverseCharge": true,
  "vatEnabled": true
}
```

___

###### This file was created by [dippyshere](https://github.com/dippyshere) for [Battle Breakers Documentation](https://github.com/dippyshere/battle-breakers-documentation)
