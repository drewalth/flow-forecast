//
//  Forecaster.swift
//
//
//  Created by Andrew Althage on 8/25/24.
//

import CoreML
import CreateML
import FlowKit
import Foundation
import Logging

/// A class that can forecast flow for a given siteID
final class Forecaster {

  // MARK: Lifecycle

  init(siteID: String, logger: Logger) {
    self.siteID = siteID
    self.logger = logger
  }

  // MARK: Internal

  enum Errors: Error {
    case noRegressor
    case noPredictionValue
  }


  /// Get the forecast for the next 30 days
  func forecast() async throws -> [FlowForecast] {
    logger.info("Forecasting flow for siteID: \(siteID)")

    if regressor == nil {
      try await train()
    }

    guard let regressor else {
      throw Errors.noRegressor
    }

    let nextTimeSteps = (0..<30).map { Date().addingTimeInterval(TimeInterval(86400 * $0)) }
    var predictions: [FlowForecast] = []

    for time in nextTimeSteps {
      let featureProvider =
        try MLDictionaryFeatureProvider(dictionary: ["x": MLFeatureValue(double: time.timeIntervalSince1970)])

      let prediction = try regressor.model.prediction(from: featureProvider)

      guard let flow = prediction.featureValue(for: "y")?.doubleValue else {
        throw Errors.noPredictionValue
      }

      predictions.append(.init(flow: flow, date: time))
    }

    logger.info("Flow forecasted successfully for siteID: \(siteID)")

    return predictions
  }

  // MARK: Private

  private let siteID: String
  private let logger: Logger

  private var regressor: MLRegressor?

  /// Train the model using the last year of data
  private func train() async throws {
    logger.info("Training model for siteID: \(siteID)")
    let readings = try await fetchReadings()
    let trainingDataOne: [(x: Double, y: Double)] = readings.map { (x: $0.timestamp.timeIntervalSince1970, y: $0.value) }
    var inputArr: [Double] = []
    var outputArr: [Double] = []

    for data in trainingDataOne {
      inputArr.append(data.x)
      outputArr.append(data.y)
    }

    let trainingData = try MLDataTable(dictionary: ["x": inputArr, "y": outputArr])

    regressor = try MLRegressor(trainingData: trainingData, targetColumn: "y")
    logger.info("Model trained successfully for siteID: \(siteID)")
  }

  /// fetch readings from the USGS API
  private func fetchReadings() async throws -> [FKReading] {
    logger.info("Fetching readings for siteID: \(siteID)")
    let api = USGS.WaterServices()
    return try await api.fetchGaugeStationData(siteID: siteID, timePeriod: .predefined(.oneYear), parameters: [.discharge])
  }
}

