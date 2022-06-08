from collections import defaultdict
from typing import List

from fastapi import WebSocket


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def conenct(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, data):
        for connection in self.active_connections:
            await connection.send_json(data)


class MessageManager:
    def __init__(self):
        self.message_counter = 0

    async def get_data_to_send(self, message: str) -> dict:
        self.message_counter += 1
        id_message = self.message_counter
        data = {
            "id": id_message,
            "message": message
        }
        return data
