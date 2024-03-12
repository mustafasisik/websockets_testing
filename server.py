import asyncio
import websockets


async def handle_connection(websocket, path):
    async for message in websocket:
        print(f"Received message: {message}")
        await websocket.send(f"Your Message:: {message}")

async def main():
    async with websockets.serve(handle_connection, "localhost", 8765):
        await asyncio.Future()  # Run the server forever

if __name__ == "__main__":
    asyncio.run(main())
