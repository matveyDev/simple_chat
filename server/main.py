from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from manager import ConnectionManager, MessageManager


app = FastAPI()
connection_manager = ConnectionManager()


@app.websocket('/')
async def websocket_endpoint(websocket: WebSocket):
    await connection_manager.conenct(websocket)
    message_manager = MessageManager()

    try:
        while True:
            message = await websocket.receive_json()
            message = message['message']

            data = await message_manager.get_data_to_send(message)
            await connection_manager.broadcast(data)

    except WebSocketDisconnect:
        connection_manager.disconnect(websocket)
        del message_manager
