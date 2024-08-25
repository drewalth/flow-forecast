# flow-forecast

![hero](/Public/flowforecast-logo.jpeg)

An experimental feature for [GaugeWatcher](https://apps.apple.com/us/app/gaugewatcher/id6498313776) that forecasts the
flow rate of a river based on historical data.

> This API is _experimental_ and is subject to change. It also does not work as expected... Any contributions and/or suggestions are welcome.

## Introduction

There are many ways to do time series based predictions. The Facebook Prophet library is one of the most popular
libraries for this task. It is a robust library that can handle missing data, outliers, and seasonal data. However, I
wanted to try a different approach using [CreateML](https://developer.apple.com/documentation/createml)
and [CoreML](https://developer.apple.com/documentation/coreml) backed by a simple [Vapor](https://vapor.codes/) web
server.

Currently, the API only supports a single USGS site ID and discharge (CFS) predictions. The API will return a forecast of the flow rate for the next 30
days.

## Example

### Request

```http
GET /forecast?siteID=09359500
```

#### Returns

```json
[
  {
    "flow": 863.292005685042,
    "date": "2024-08-25T19:21:59Z"
  },
  {
    "flow": 863.292005685042,
    "date": "2024-08-26T19:21:59Z"
  },
  {
    "date": "2024-08-27T19:21:59Z",
    "flow": 863.292005685042
  }
]
```
