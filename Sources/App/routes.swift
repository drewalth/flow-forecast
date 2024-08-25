import Vapor

func routes(_ app: Application) throws {
  app.get { req in
    req.view.render("index", ["title": "Hello, world!"])
  }
  try app.register(collection: ForecastController())
}
