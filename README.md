# Chess Game with Chat System

This project is a multiplayer chess game with a real-time chat feature. It consists of a client-server architecture, where the server manages the chessboard state and handles communication between two clients. The clients can play chess, make moves, and chat with each other during the game.

## Features
- **Real-time Chess Game:** Two players can connect to the server and play chess with each other.
- **Chat System:** Players can send messages to each other during the game.
- **Board Synchronization:** The chessboard state is synchronized across both clients, ensuring that both players have the same view of the game.

## Project Structure
- `client.py`: The client-side application where the user interacts with the chessboard and chat.
- `server.py`: The server-side application that handles incoming connections, manages the game state, and facilitates communication between clients.

## Requirements
- Python 3.x
- Pygame (for the graphical interface)
- python-chess (for chess logic)

### Install Dependencies
To install the necessary dependencies, use the following command:

```bash
pip install pygame python-chess
```

## Running the Project
### Start the Server
To run the server, use the following command:

```bash
python server.py
```

This will start the server on the default localhost:12345 and wait for players to connect.

### Start the Client
To run the client, use the following command:

```bash

python client.py
```

The client will automatically connect to the server. You can open two instances of the client to simulate two players.

## How to Play
Connect to the Server: Open two instances of the client and they will automatically connect to the server.

Make a Move: Click on the pieces and move them on the board. The server will validate the moves and update the board for both players.

Chat: Use the chat box to send messages to the other player.

## Notes

The game follows standard chess rules.

Only two players are allowed to play at the same time.

The game alternates turns between white and black, and the server manages turn order.

Chat messages are visible to both players.


Author
[Reahoon & Rabbi]

