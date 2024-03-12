import asyncio
import time
import websockets
from sys import argv

seconds = int(argv[1])


async def connect():
    async with websockets.connect("ws://localhost:8765") as websocket:
        start_time = time.time()
        messages_sent = 0
        while True:  # Adjust the number of messages as needed
            await websocket.send(f"Message {messages_sent}")
            response = await websocket.recv()
            messages_sent += 1
            if time.time() - start_time >= seconds:
                break

        print(f"Messages sent: {messages_sent} messages/s")

if __name__ == "__main__":
    asyncio.run(connect())
