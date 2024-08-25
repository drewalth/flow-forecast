//
//  FlowForecast.swift
//
//
//  Created by Andrew Althage on 8/25/24.
//

import Foundation
import Vapor

struct FlowForecast: Content {
  let flow: Double
  let date: Date
}
