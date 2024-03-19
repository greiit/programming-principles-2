import pygame
import time
import math


pygame.init()


screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Mickey's Clock")


clock_img = pygame.image.load("images/main-clock.png").convert_alpha()
left_hand_img = pygame.image.load("images/left-hand.png").convert_alpha()
right_hand_img = pygame.image.load("images/right-hand.png").convert_alpha()


def resize_images():
    clock_img_scaled = pygame.transform.scale(clock_img, (screen_width, screen_height))
    left_hand_img_scaled = pygame.transform.scale(left_hand_img, (int(screen_width * 0.55), int(screen_height * 0.35)))
    right_hand_img_scaled = pygame.transform.scale(right_hand_img, (int(screen_width * 0.55), int(screen_height * 0.35)))
    return clock_img_scaled, left_hand_img_scaled, right_hand_img_scaled

clock_img, left_hand_img, right_hand_img = resize_images()


clock_center = (screen_width // 2, screen_height // 2)
hand_length = 120
hand_thickness = 5


def rotate_image(image, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_rect = rotated_image.get_rect(center=image.get_rect(center=clock_center).center)
    return rotated_image, rotated_rect


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            screen_width, screen_height = event.size
            screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
            clock_img, left_hand_img, right_hand_img = resize_images()

    
    screen.fill((255, 255, 255))

    
    screen.blit(clock_img, (0, 0))

    
    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

   
    minute_angle = 360 * (minutes / 60) - 90
    second_angle = 360 * (seconds / 60) - 90

    
    rotated_left_hand, left_hand_rect = rotate_image(left_hand_img, -second_angle)
    rotated_right_hand, right_hand_rect = rotate_image(right_hand_img, -minute_angle)

   
    screen.blit(rotated_left_hand, left_hand_rect)
    screen.blit(rotated_right_hand, right_hand_rect)

    
    pygame.display.flip()

    
    pygame.time.delay(1000)


pygame.quit()
