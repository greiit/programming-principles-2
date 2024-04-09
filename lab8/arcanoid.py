import pygame
import random
import sys

# Initialize Pygame
pygame.init()

WIDTH, HEIGHT = 1200, 800
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

#Paddle
paddle_WIDTH = 150
paddle_HEIGHT = 25
paddleSpeed = 20
paddle = pygame.Rect(WIDTH // 2 - paddle_WIDTH // 2, HEIGHT -paddle_HEIGHT - 30, paddle_WIDTH, paddle_HEIGHT)

# Ball
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, WIDTH - ball_rect), HEIGHT // 2, ball_rect, ball_rect)
dx, dy = 1, -1

#Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

#Catching sound
collision_sound = pygame.mixer.Sound('catch.mp3')

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

#block settings 
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j,
        100, 50) for i in range(10) for j in range (4)]
color_list = [(random.randrange(0, 255), 
     random.randrange(0, 255),  random.randrange(0, 255))
              for i in range(10) for j in range(4)] 
print(block_list)

#Game over Screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (WIDTH // 2, HEIGHT // 2)

#Win Screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (WIDTH // 2, HEIGHT // 2)

# Initialize unbreakable and breakable bricks
unbreakable_blocks = set(random.sample(range(len(block_list)), 7))  # Let's assume 10 unbreakable bricks
bonus_blocks = set(random.sample(range(len(block_list)), 7)) - unbreakable_blocks  # Ensure no overlap
for ub_index in unbreakable_blocks:
        pygame.draw.rect(screen, (128, 128, 128), block_list[ub_index])
        
start_time = pygame.time.get_ticks()
increase_difficulty_interval = 30  # Increase difficulty every 30 seconds
shrink_paddle_interval = 60  # Shrink paddle every 60 seconds

is_paused = False
settings_menu_active = False

# Game settings (example)
settings = {
    'ball_speed': ballSpeed,
    'paddle_width': paddle_WIDTH,
}

def display_pause_menu(screen):
    # Placeholder for pause menu rendering
    pause_text = pygame.font.SysFont('comicsansms', 40).render('Game Paused', True, (255, 255, 255))
    screen.blit(pause_text, (WIDTH // 2 - 100, HEIGHT // 2 - 20))

def display_settings_menu(screen, settings):
    # Placeholder for settings menu rendering
    settings_text = pygame.font.SysFont('comicsansms', 40).render('Settings', True, (255, 255, 255))
    ball_speed_text = settings_text.render(f'Ball Speed: {settings["ball_speed"]}', True, (255, 255, 255))
    paddle_width_text = settings_text.render(f'Paddle Width: {settings["paddle_width"]}', True, (255, 255, 255))

    screen.blit(settings_text.render('Settings', True, (255, 255, 255)), (50, 50))
    screen.blit(ball_speed_text, (50, 150))
    screen.blit(paddle_width_text, (50, 250))
    screen.blit(settings_text, (WIDTH // 2 - 80, HEIGHT // 2 - 100))

selected_setting = 0 

while not done:
    current_time = pygame.time.get_ticks()

    # Increase ball speed over time
    if (current_time - start_time) > increase_difficulty_interval:
        ballSpeed += 1
        start_time = current_time

    # Shrink paddle over time
    if (current_time - start_time) > shrink_paddle_interval and paddle_WIDTH > 100:
        paddle_WIDTH -= 10
        paddle.inflate_ip(-10, 0)  # Shrink paddle width

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p and not settings_menu_active:  # Toggle pause
                is_paused = not is_paused
            elif event.key == pygame.K_s and is_paused:  # Open settings menu
                settings_menu_active = True
            elif settings_menu_active:
                # Navigate through settings
                if event.key == pygame.K_UP:
                    selected_setting = max(0, selected_setting - 1)
                elif event.key == pygame.K_DOWN:
                    selected_setting = min(len(settings) - 1, selected_setting + 1)
                # Adjust selected setting
                elif event.key == pygame.K_LEFT:
                    if selected_setting == 0:
                        settings['ball_speed'] = max(1, settings['ball_speed'] - 1)
                    elif selected_setting == 1:
                        settings['paddle_width'] = max(100, settings['paddle_width'] - 10)
                elif event.key == pygame.K_RIGHT:
                    if selected_setting == 0:
                        settings['ball_speed'] += 1
                    elif selected_setting == 1:
                        settings['paddle_width'] += 10

    if is_paused:
        if settings_menu_active:
            display_settings_menu(screen, settings)
        else:
            display_pause_menu(screen)

        pygame.display.flip()
        continue  # Skip the rest of the game loop

    # Apply settings
    ballSpeed = settings['ball_speed']
    paddle_WIDTH = settings['paddle_width']
    paddle.width = paddle_WIDTH  # Adjust the paddle Rect width
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_p:  # Press 'P' to pause/unpause
        #         is_paused = not is_paused
        #         settings_menu_active = False  # Close settings when unpausing
        # if is_paused:
        #     display_pause_menu(screen)
        #     pygame.display.flip()
        #     continue 
        # if is_paused:
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_s:  # Press 'S' to toggle settings menu
        #             settings_menu_active = not settings_menu_active

        #     if settings_menu_active:
        #         display_settings_menu(screen)
        #     else:
        #         display_pause_menu(screen)

        # pygame.display.flip()
        # continue  # Skip the rest of the game loop while paused
    screen.fill(bg)
    
    print(next(enumerate(block_list)))

    [pygame.draw.rect(screen, color_list[color], block)
     for color, block in enumerate (block_list)] #drawing blocks
    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)
    # print(next(enumerate (block_list)))

    #Ball movement
    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    #Collision left 
    if ball.centerx < ballRadius or ball.centerx > WIDTH - ballRadius:
        dx = -dx
    #Collision top
    if ball.centery < ballRadius + 50: 
        dy = -dy
    #Collision with paddle
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    #Collision blocks
    hitIndex = ball.collidelist(block_list)

    if hitIndex != -1:
        if hitIndex not in unbreakable_blocks:
            hitRect = block_list.pop(hitIndex)
            hitColor = color_list.pop(hitIndex)
            dx, dy = detect_collision(dx, dy, ball, hitRect)
            game_score += 1
            collision_sound.play()

            # Check if it's a bonus block
            if hitIndex in bonus_blocks:
                # Add your perk logic here, for example:
                # Increase paddle size, slow down ball, etc.
                paddle_WIDTH += 20
                bonus_blocks.remove(hitIndex)  # Remove the bonus block from the set

        
    #Game score
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)
    # Draw unbreakable blocks with a different color, e.g., grey
    
    #Win/lose screens
    if ball.bottom > HEIGHT:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif not len(block_list):
        screen.fill((255,255, 255))
        screen.blit(wintext, wintextRect)
    # print(pygame.K_LEFT)
    #Paddle Control
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.right += paddleSpeed


    pygame.display.flip()
    clock.tick(FPS)