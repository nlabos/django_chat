import asyncio
import websockets
import datetime

async def time_sender():
    async with websockets.connect("ws://localhost:8765") as websocket:
        while True:
            now = datetime.datetime.now(). isoformat()
            message =f"現在の時刻は{now}です"
            print(message)
            
            await websocket. send(message)
            response = await websocket.recv()
            print(f"サーバーからのメッセージ:{response}")
            await asyncio.sleep(5)
            
asyncio.get_event_loop().run_until_complete(time_sender())