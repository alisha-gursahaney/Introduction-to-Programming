# Name: Alisha Gursahaney
# Net Id: amg9zd

import gamebox
import pygame
import random

width = 600
height = 400
camera = gamebox.Camera(width, height)
floors = []
player = gamebox.from_image(300, 350, "toad.png")
score = 0
counter = 0
lose = False


def tick(keys):
    """
    runs our game at certain speed and runs the game falldown
    :param keys: gamebox function parameter
    :return: the game falldown
    """
    camera.display()
    camera.clear("white")
    camera.draw(player)
    player.speedy += 1
    player.move_speed()
    if pygame.K_LEFT in keys:
        player.speedx -= 1
    if pygame.K_RIGHT in keys:
        player.speedx += 1
    camera.y += 2
    # keep player on screen
    if player.x < 15:
        player.x = 15
    if player.x > 585:
        player.x = 585
    if player.y < 0:
        player.y = 15
    for floor in floors:
        camera.draw(floor)
        if player.touches(floor):
            player.move_to_stop_overlapping(floor)
    global score
    global counter
    if counter % 50 == 0:
        gap = random.randint(0, 1050)
        new_floor_left = gamebox.from_color(0, 250 + camera.y, "black", gap, 30)
        new_floor_right = gamebox.from_color(600, 250 + camera.y, "black", 1050-gap, 30)
        floors.append(new_floor_left)
        floors.append(new_floor_right)
        score += 1
    if player.y <= camera.y - 300:
        camera.draw(gamebox.from_text(300, camera.y + 100, "GAME OVER", 75, "red"))
        camera.draw(gamebox.from_text(300, camera.y + 125, f"Final Score: {score}", 25, "blue"))
        camera.display()
        gamebox.pause()
    counter += 1
    camera.draw(gamebox.from_text(40, camera.y - 150, f"Score: {score}", 25, "blue"))

gamebox.timer_loop(30, tick)
