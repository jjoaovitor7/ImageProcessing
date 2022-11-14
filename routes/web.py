from masonite.routes import Route

ROUTES = [
    Route.get("/", "IndexController@show"),
    Route.post("/", "IndexController@show")
]
