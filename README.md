# flow-forecast

![hero](/assets/flowforecast-logo.jpeg)

Forecast the flow rate of a river based on historical data.

> This project is _experimental_ and is subject to change. There is a lot of room for improvement. Any contributions and/or suggestions are welcome.

### Features

- [x] Forecast the flow rate of a river based on historical data.
- [x] Dockerized API.
- [x] OpenAPI documentation.

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

### Docker

If you prefer to use [Docker](https://www.docker.com/), you can build and run the app using the provided `Dockerfile`.

1. Build the image: `docker build -t flow-forecast .`
2. Run the container: `docker run -p 3000:3000 flow-forecast` or `docker compose up`.

```bash
curl -X GET "http://127.0.0.1:3000/forecast?site_id=09359500"
```

> Note: The current Dockerfile runs the production server. If you want to run the development server, you'll need to update the `CMD` in the Dockerfile.
> See the [Flask docs](https://flask.palletsprojects.com/en/3.0.x/deploying/waitress/) for more info on deploying Flask apps.

## Making Requests

To make a request to the API, you need to provide a `site_id` query parameter. The `site_id` is the USGS site id for the river you want to forecast. You can find the site id by searching for the river on the [USGS website](https://waterdata.usgs.gov/nwis).

In the example `curl` requests above we are using the site id `09359500` which is the site id for the [Animas River at Tall Timber Resort Above Tacoma, CO](https://waterdata.usgs.gov/monitoring-location/09359500/#parameterCode=00065&period=P7D&showMedian=false).
 
## Considerations

- The data used for this project is from the [USGS](https://www.usgs.gov/) and is publicly available.
- The training data does not include all possible factors that may affect the flow rate of a river like weather, temperature, snowpack, dam releases etc.

## OpenAPI + Client SDKs

> Requires Nodejs and npm. Run `npm install` before generating clients.

The API is documented using [OpenAPI](https://swagger.io/specification/). The [OAS file](/flow-forecast.openapi.yml) is helpful for generating client SDKs in different languages. The [Makefile](/Makefile) has targets for generating Swift, Kotlin, and TypeScript client SDKs.

Before generating clients, be sure to update the `servers` section of the OAS file to point to the correct host.

```bash
# Generates all clients
make generate_clients 

# Generates Swift client
make swift_client

# Generates Kotlin client
make kotlin_client

# Generates TypeScript client
make typescript_client
```

Once you've generated the client(s) of your choosing, you can then use/distribute them as needed.

For the full list of generators and options, see the [OpenAPI Generator CLI docs](https://openapi-generator.tech/docs/generators).

## Swift

I've also been exploring using [Swift](https://developer.apple.com/swift/), [CoreML](https://developer.apple.com/documentation/coreml), and [CreateML](https://developer.apple.com/documentation/createml) to build a model that can predict the flow rate of a river based on historical data. This is a POC that doesn't quite work... I'm still learning about ML and how to build models.

If you're interested in seeing the Swift code, clone this repo and checkout the [swift](https://github.com/drewalth/flow-forecast/tree/swift) branch.

## Related Projects

- [FlowKit](https://github.com/drewalth/FlowKit) - A Swift package for working with flow data from the USGS, Canadian Hydrometric Data, and other sources.
- [GaugeWatcher](https://apps.apple.com/us/app/gaugewatcher/id6498313776) - An iOS app for tracking the flow rate of your favorite rivers.
