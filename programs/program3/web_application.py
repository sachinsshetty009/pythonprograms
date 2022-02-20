import common_settings 
import logging
from aiohttp import web
from route import *

import asyncio

logger = logging.getLogger("Web Application")


async def web_app(app, port):
  """
  port 8080
  """
  runner = web.AppRunner(app)
  setup_routes(app)
  await runner.setup()
  site = web.TCPSite(runner, '0.0.0.0', port)
  await site.start()

def web_application_lauch():

    loop = asyncio.get_event_loop()

    loop.create_task(web_app(web.Application(middlewares=[middleware1]), port=8080))
    loop.create_task(web_app(web.Application(middlewares=[middleware2]), port=8081))
    loop.create_task(web_app(web.Application(middlewares=[middleware3]), port=8082))

    while True:
        loop.run_until_complete(asyncio.sleep(5))
        logger.info("Listen on port 8080, 8081 and 8082")
        if common_settings.visited_8080 and common_settings.visited_8081 and common_settings.visited_8082:
            logger.info("All port web app visited")
            break