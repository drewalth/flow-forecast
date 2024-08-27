# flow-forecast

![hero](/assets/flowforecast-logo.jpeg)

Forecast the flow rate of a river based on historical data.

> This project is _experimental_ and is subject to change. There is a lot of room for improvement. Any contributions and/or suggestions are welcome.

## Overview

Using Facebook's [Prophet](https://facebook.github.io/prophet/) library, this project aims to forecast the flow rate of a river based on historical data. The goal is to help kayakers, rafters, and other river enthusiasts predict the flow rate of a river so they can plan their trips accordingly.

## Getting Started

### Prerequisites

- Python 3.12
- [Poetry](https://python-poetry.org/)

### Development

1. clone the repo
2. `cd` into the project directory: `cd /path/to/flow-forecast`
3. Install dependencies: `poetry install`
4. Run the app: `poetry run flask --app flow_forecast run`
5. Make a request: `curl -X GET "http://127.0.0.1:5000/forecast?site_id=09359500"`

## Considerations

- The data used for this project is from the [USGS](https://www.usgs.gov/) and is publicly available.
- The training data does not include all possible factors that may affect the flow rate of a river like weather, temperature, snowpack, dam releases etc.


## Wishlist

- [ ] Improve the model by including more factors that may affect the flow rate of a river. (e.g. weather, temperature, snow pack, dam releases etc.)
- [ ] BYOD (Bring Your Own Data) - Allow users to provide their own data to train the model. Currently, the model is trained on data from the USGS. It would be nice to support other data sources.
- [ ] Open API Spec - Create an OpenAPI spec for the API to auto-generate client libraries.


## Swift

I've also been exploring using [Swift](https://developer.apple.com/swift/), [CoreML](https://developer.apple.com/documentation/coreml), and [CreateML](https://developer.apple.com/documentation/createml) to build a model that can predict the flow rate of a river based on historical data. This is a POC that doesn't quite work... I'm still learning about ML and how to build models.

If you're interested in seeing the Swift code, clone this repo and checkout the [swift](https://github.com/drewalth/flow-forecast/tree/swift) branch.

## Related Projects

- [FlowKit](https://github.com/drewalth/FlowKit) - A Swift package for working with flow data from the USGS, Canadian Hydrometric Data, and other sources.
- [GaugeWatcher](https://apps.apple.com/us/app/gaugewatcher/id6498313776) - An iOS app for tracking the flow rate of your favorite rivers.