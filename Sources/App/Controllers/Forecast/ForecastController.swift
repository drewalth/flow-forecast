//
//  ForecastController.swift
//
//
//  Created by Andrew Althage on 8/25/24.
//

import Foundation
import Vapor

struct ForecastController: RouteCollection {

  func boot(routes: any RoutesBuilder) throws {
    let forecastController = routes.grouped("forecast")
    forecastController.get(use: index)
  }

  func index(req: Request) async throws -> [FlowForecast] {
    let siteID = try req.query.decode(ForecastRequestQuery.self).siteID

    let forecaster = Forecaster(siteID: siteID, logger: req.logger)

    return try await forecaster.forecast()
  }

  struct ForecastRequestQuery: Decodable {
    let siteID: String
  }
}


