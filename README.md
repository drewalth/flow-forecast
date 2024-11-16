# flow-forecast

![Hero](assets/flowforecast-logo.jpeg)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![OpenAPI](https://img.shields.io/badge/OpenAPI-3.0.0-green.svg)](https://swagger.io/specification/)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Development](#development)
  - [Using Docker](#using-docker)
- [Making Requests](#making-requests)
- [OpenAPI & Client SDKs](#openapi--client-sdks)
- [Swift Integration](#swift-integration)
- [Considerations](#considerations)
- [Related Projects](#related-projects)
- [Contributing](#contributing)
- [License](#license)

## Introduction

**flow-forecast** is an experimental project aimed at forecasting the flow rate of rivers using historical data. Leveraging Facebook's [Prophet](https://facebook.github.io/prophet/) library, the API provides valuable insights for kayakers, rafters, and river enthusiasts to plan their trips effectively.

> This project is _experimental_ and is subject to change. There is ample room for improvement. Contributions and suggestions are highly encouraged!

## Features

- ✅ **Flow Rate Forecasting**: Predict river flow rates based on historical data.
- ✅ **Dockerized API**: Simplify deployment with Docker.
- ✅ **OpenAPI Documentation**: Comprehensive API documentation for easy integration.

## Overview

Using Prophet, the project analyzes historical river flow data to generate accurate forecasts. The primary goal is to assist outdoor enthusiasts in anticipating river conditions, enhancing safety and planning for their adventures.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.12**: [Download Python](https://www.python.org/downloads/)
- **[Poetry](https://python-poetry.org/)**: A dependency management and packaging tool for Python.
- **[Node.js](https://nodejs.org/en)**: Required for generating client SDKs.

### Development

Follow these steps to set up the development environment:

1. **Clone the Repository**
    ```bash
    git clone https://github.com/drewalth/flow-forecast.git
    cd flow-forecast
    ```

2. **Install Dependencies**
    ```bash
    poetry install
    ```

3. **Run the Application**
    ```bash
    poetry run start
    ```

4. **Make a Test Request**
    ```bash
    curl -X GET "http://127.0.0.1:8000/forecast?site_id=09359500"
    ```

### Using Docker

Docker simplifies the setup/deployment process. Here's how to build and run the application using Docker:

1. **Build the Docker Image**
    ```bash
    docker build -t flow-forecast .
    ```

2. **Run the Docker Container**
    ```bash
    docker run -p 8000:8000 flow-forecast
    ```
    *Alternatively, use Docker Compose:*
    ```bash
    docker compose up
    ```

3. **Make a Test Request**
    ```bash
    curl -X GET "http://127.0.0.1:8000/usgs/forecast?site_id=09359500"
    ```

## Making Requests

To interact with the API, provide a `site_id` as a query parameter. This ID corresponds to a specific USGS monitoring station.

- **Find a Site ID**: Search for rivers on the [USGS website](https://waterdata.usgs.gov/nwis) to obtain the `site_id`.
  
- **Example**: The site ID `09359500` corresponds to the [Animas River at Tall Timber Resort Above Tacoma, CO](https://waterdata.usgs.gov/monitoring-location/09359500/).

## OpenAPI & Client SDKs

The API is documented using **OpenAPI**. Use the provided [OpenAPI Specification](flow-forecast.openapi.yml) to generate client SDKs in various languages.

### Generating Client SDKs

Ensure you have **Node.js** and **npm** installed, then run:

```bash
npm install
```

Generate all client SDKs:

```bash
make generate_clients
```

## Considerations

- **Data Source**: Utilizes publicly available data from [USGS](https://www.usgs.gov/).
- **Data Limitations**: The model currently doesn't account for factors like weather, temperature, snowpack, or dam releases, which can influence river flow rates.

## Related Projects

- [FlowKit](https://github.com/drewalth/FlowKit): A Swift package for working with flow data from USGS, Canadian Hydrometric Data, and other sources.
- [GaugeWatcher](https://apps.apple.com/us/app/gaugewatcher/id6498313776): An iOS app for tracking the flow rate of your favorite rivers.

## Contributing

We welcome contributions and suggestions! To get started:

1. **Fork the Repository**
2. **Create a Feature Branch**
    ```bash
    git checkout -b feature/YourFeature
    ```
3. **Commit Your Changes**
    ```bash
    git commit -m "Add your message"
    ```
4. **Push to the Branch**
    ```bash
    git push origin feature/YourFeature
    ```
5. **Open a Pull Request**

Please ensure your code adheres to the project's coding standards and all tests pass. For detailed guidelines, refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## License

This project is licensed under the [MIT License](LICENSE). See the [LICENSE](LICENSE) file for details.