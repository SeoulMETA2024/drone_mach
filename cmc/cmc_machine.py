import asyncio
import websocket
import cmcHandler


class RemoteControl:
    def __init__(self):

        self.res = (0,0,0)
        
        pass

    async def run(self,websocket):

        while True:
            try:
                msg = await websocket.recv()

                self.res = await cmcHandler(msg)

                

            except:
                print('disconnected.')
                break
        return

    async def main(self):
        
        while True:
            async with websocket.serve(self.run, 'localhost',3000) as ws:
                await asyncio.Future()





