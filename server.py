import asyncio
import websockets

async def echo(websocket, path):
    print("新しいクライアントと接続しました！")
    
    async for message in websocket:
        print(f"クライアントからのメッセージ:{message}")
        await websocket.send("こんにちは！")


start_server = websockets. serve(echo, "localhost",8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()