import pygame
import sys
import random


pygame.init()
WIDTH, HEIGHT = 600, 400
FPS = 60
GAME_DURATION = 10   
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
mole_size = 50
mole_speed = 10
mole = pygame.Rect(WIDTH // 2 - mole_size // 2, HEIGHT // 2 - mole_size // 2, mole_size, mole_size)
last_movement_time = pygame.time.get_ticks()
score = 0
start_time = pygame.time.get_ticks()
font = pygame.font.Font(None, 36)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Whack-a-Mole")
clock = pygame.time.Clock()

# Function to draw score and timer
def draw_score_timer():
    score_text = font.render(f"Score: {score}", True, WHITE)
    timer_text = font.render(f"Time: {max(0, GAME_DURATION - (pygame.time.get_ticks() - start_time) // 1000)}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(timer_text, (10, 50))

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if mole.collidepoint(event.pos):
                score += 1
                print(f"Whacked! Score: {score}")

    current_time = pygame.time.get_ticks()
    if current_time - last_movement_time > random.randint(500, 1500):
        mole.x += random.randint(-mole_speed, mole_speed)
        mole.y += random.randint(-mole_speed, mole_speed)
        mole.x = max(0, min(WIDTH - mole_size, mole.x))
        mole.y = max(0, min(HEIGHT - mole_size, mole.y))
        last_movement_time = current_time

    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, mole)

    draw_score_timer()
    pygame.display.flip()

    if pygame.time.get_ticks() - start_time > GAME_DURATION * 1000:
        print("Game Over! Time's up!")
        pygame.quit()
        sys.exit()

    clock.tick(FPS)
