# Don't Remove Credit @Opleech
# Telegram @Opleech
# Copyright (c) 2023 WOODcraft

from aiohttp import web
from .route import routes


async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app
