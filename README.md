# flow-forecast

![hero](/assets/flowforecast-logo.jpeg)

An experimental feature for [GaugeWatcher](https://apps.apple.com/us/app/gaugewatcher/id6498313776) that forecasts the
flow rate of a river based on historical data.

> This project is _experimental_ and is subject to change. There is a lot of room for improvement. Any contributions and/or suggestions are welcome.

## Overview

Using Facebook's [Prophet](https://facebook.github.io/prophet/) library, this project aims to forecast the flow rate of a river based on historical data. The goal is to provide users with a prediction of what the flow rate will be in the future to help them plan their activities accordingly.

## Considerations

- The data used for this project is from the [USGS](https://www.usgs.gov/) and is publicly available.
- The data is not always consistent, may contain missing values, and may not always be accurate.
- The training data does not include all possible factors that may affect the flow rate of a river like weather, temperature, dam releases etc.


## Wishlist

- [ ] Improve the model by including more factors that may affect the flow rate of a river. (e.g. weather, temperature, snow pack, dam releases etc.)
- [ ] BYOD (Bring Your Own Data) - Allow users to provide their own data to train the model. Currently, the model is trained on data from the USGS. It would be nice to support other data sources.


## Swift

Since there is a lot TBD with this project, I've also been exploring using Swift, CoreML, and CreateML to build a model that can predict the flow rate of a river based on historical data. This is a work in progress and I'm still learning about machine learning and how to build models.

If you're interested in seeing the Swift code, clone this repo and checkout the `swift` branch.