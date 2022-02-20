import common_settings
from aiohttp import web

async def index(request):
    return web.Response(text='Hello from the server (0.0.0.0) port =')