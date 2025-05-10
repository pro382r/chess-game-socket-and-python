import socket
import threading
import chess

class ChessServer:
    def __init__(self, host='localhost', port=12345):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(2)
        self.board = chess.Board()
        self.clients = []
        self.current_turn = "white"

    def handle_client(self, client_socket, color):
        try:
            client_socket.sendall(f"color:{color}".encode('utf-8'))
            while True:
                message = client_socket.recv(1024).decode('utf-8')
                if message.startswith("move"):
                    _, chess_move = message.split()
                    if self.board.is_legal(chess.Move.from_uci(chess_move)):
                        self.board.push(chess.Move.from_uci(chess_move))
                        self.current_turn = "black" if self.current_turn == "white" else "white"
                        self.broadcast_board()
                elif message.startswith("chat"):
                    chat_message = message[5:]  # remove "chat:" prefix
                    self.broadcast_chat(chat_message)
        except:
            print(f"{color} player disconnected.")
            self.clients.remove(client_socket)
            client_socket.close()

    def broadcast_board(self):
        board_state = self.board.fen()
        for client in self.clients:
            client.sendall(f"board:{board_state}".encode('utf-8'))

    def broadcast_chat(self, chat_message):
        for client in self.clients:
            client.sendall(f"chat:{chat_message}".encode('utf-8'))

    def start(self):
        print("Chess Server Started. Waiting for players...")
        while len(self.clients) < 2:
            client_socket, _ = self.server_socket.accept()
            self.clients.append(client_socket)
            color = "white" if len(self.clients) == 1 else "black"
            threading.Thread(target=self.handle_client, args=(client_socket, color)).start()

if __name__ == "__main__":
    server = ChessServer()
    server.start()
