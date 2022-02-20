import common_settings
from view import index
from aiohttp import web

def setup_routes(app):
    app.router.add_get('/', index)

@web.middleware
async def middleware1(request, handler):
    response = await handler(request)
    response.text = response.text + '8080'
    common_settings.visited_8080 = True
    return response

@web.middleware
async def middleware2(request, handler):
    response = await handler(request)
    response.text = response.text + '8081'
    common_settings.visited_8081 = True
    return response

@web.middleware
async def middleware3(request, handler):
    response = await handler(request)
    response.text = response.text + '8082'
    common_settings.visited_8082 = True
    return response