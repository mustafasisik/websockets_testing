import asyncio
import time
import websockets
from sys import argv


async def connect():
    async with websockets.connect("ws://localhost:8765") as websocket:
        start_time = time.time()
        for i in range(int(argv[1])):  # Adjust the number of messages as needed
            await websocket.send(f"Message {i}")
            response = await websocket.recv()
        end_time = time.time()
        total_time = end_time - start_time
        print(f"Total time taken: {total_time} seconds")
        print(f"Average latency: {total_time / 100} seconds")  # Adjust this based on the number of messages


if __name__ == "__main__":
    asyncio.run(connect())
