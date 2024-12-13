import asyncio
import websocket
from _ import cmcHandler

async def run(websocket):

    device = cmdHandler()

    while True:
        try:
            msg = await websocket.recv()

            await cmcHandler(msg)

        except:
            print('disconnected.')
            break
    return

async def main():
    while True:
        async with websocket.serve(run, 'localhost',3000) as ws:
            await asyncio.Future()

asyncio.run(main())


