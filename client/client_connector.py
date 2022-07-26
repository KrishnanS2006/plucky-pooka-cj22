"""Websocket Client side script."""

import asyncio
import json
import random
from typing import Dict

import websockets


class WebSocketClient:
    """Websocket client."""

    def __init__(self) -> None:
        """Initialize class with url variables."""
        self.ws_url: str = "ws://127.0.0.1:"
        self.ws_port: int = 8765
        self.uri = f"{self.ws_url}{self.ws_port}"
        self.delay = 1
        self.player_data = None  # Should be output from player.Player.to_dict()

    def create_payload(self, WEBSOCKET_ID: str, MESSAGE: str, player_data: dict) -> Dict:
        """
        Construct payload that can be sent through the websocket connection.

        Should ideally be initialized attributes of client.utility.Player class, but can be
        any data that can be handled by websocket.

        See utility.player.to_dict().

        Attributes:

        """
        payload = {
            "websocket_id": WEBSOCKET_ID,
            "message": MESSAGE,
            "data": player_data,
        }

        return json.dumps(payload).encode("utf-8")

    def create_message(self) -> str:
        """Helper function to create a message to be included in payload for testing."""
        return random.randint(1, 5)

    async def establish_connection(self) -> None:
        """Establish connection to server."""
        try:
            async with websockets.connect(self.uri) as websocket:
                WEBSOCKET_ID = str(websocket.id)
                print(f"Client {websocket.id} connected.")

                while True:
                    await websocket.send(
                        self.create_payload(
                            WEBSOCKET_ID,
                            MESSAGE=self.create_message(),
                            player_data=self.player_data,
                        )
                    )
                    await asyncio.sleep(self.delay)
                    server_response: str = await websocket.recv()
                    print(f"Server response: {server_response}")

        except websockets.exceptions.ConnectionClosedError as e:
            print(f"Error: {e}.")

        finally:
            pass


async def run():
    """Creates an instance of WebSocketClient() and runs it."""
    client = WebSocketClient()
    await client.establish_connection()


if __name__ == "__main__":
    client = WebSocketClient()
    asyncio.run(client.establish_connection())
