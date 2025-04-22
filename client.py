import pygame, socket, sys

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Chess Client")

sock = socket.socket()
sock.connect(('localhost', 12345))

run = True
while run:
    for r in range(8):
        for c in range(8):
            pygame.draw.rect(screen, (255, 255, 255) if (r+c)%2==0 else (180,180,180), (c*75, r*75, 75, 75))
    pygame.display.flip()

    for e in pygame.event.get():
        if e.type == pygame.QUIT: run = False
        elif e.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            msg = f"Click at {pos}"
            sock.send(msg.encode())
            print("Server:", sock.recv(1024).decode())

pygame.quit()
sock.close()
sys.exit()
