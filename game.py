# Name: Alisha Gursahaney
# Net Id: amg9zd

import gamebox
import pygame
import random

# Game: "Why did the turtle cross the river?"
# Player begins in the grass on one side and must make it to the other side to pass the level
# If they touch a moving fish, they lose
# There are rocks as obstacles (the player cannot pass through), so the player must go around them
# Each level there are 3 leaves in the river
# If the player touches a leaf, they will earn 10 additional points
# Each level is worth 50 points
# Every level, the fish get faster and more obstacles are placed, making it more difficult to cross
# There is an option to restart the game if the player loses
# The score can be viewed in the top left corner of the screen

width = 600
height = 400
camera = gamebox.Camera(width, height)

turtle = "turtleup.png"
player = gamebox.from_image(300, 400, turtle)

water = gamebox.from_image(300, 200, "water.jpg")
level = 1
counter = 0
score = 0
fish_xspeed = 0.5
fish_yspeed = 1
left_fish = []
right_fish = []
fish = []
obstacles = []
leaves = [gamebox.from_image(random.randint(0, 600), random.randint(50, 325), "leaf.png"),
          gamebox.from_image(random.randint(0, 600), random.randint(50, 325), "leaf.png"),
          gamebox.from_image(random.randint(0, 600), random.randint(50, 325), "leaf.png")]
pause = False

# initial fish to spawn
left_fish.append(gamebox.from_image(random.randint(0, 600), random.randint(50, 325), "left_fish.png"))
left_fish.append(gamebox.from_image(random.randint(0, 600), random.randint(50, 325), "left_fish.png"))
left_fish.append(gamebox.from_image(random.randint(0, 600), random.randint(50, 325), "left_fish.png"))

right_fish.append(gamebox.from_image(random.randint(0, 600), random.randint(50, 325), "right_fish.png"))
right_fish.append(gamebox.from_image(random.randint(0, 600), random.randint(50, 325), "right_fish.png"))
right_fish.append(gamebox.from_image(random.randint(0, 600), random.randint(50, 325), "right_fish.png"))

# initial rocks to spawn
obstacles.append(gamebox.from_image(random.randint(0, 600), random.randint(50, 325), "rock.png"))
obstacles.append(gamebox.from_image(random.randint(0, 600), random.randint(50, 325), "rock.png"))
obstacles.append(gamebox.from_image(random.randint(0, 600), random.randint(50, 325), "rock.png"))


def tick(keys):
    """

    :param keys: keyboard buttons to sense which buttons are being pressed during the game
    :return: "Why did the turtle cross the river?" game runs
    """
    global player, pause, fish_xspeed, fish_yspeed, level, score, counter, turtle, leaves

    counter += 1
    camera.clear("darkgreen")
    camera.draw(water)
    camera.draw(player)
    player.move_speed()
    if not pause:
        camera.draw(gamebox.from_text(45, 15, f"Score: {score}", 25, "red"))

        # delayed start to wait for fish to spawn
        if counter <= 100:
            if 0 <= counter <= 30:
                camera.draw(gamebox.from_text(300, 200, "Starting in 3", 50, "red"))
            if 30 <= counter <= 60:
                camera.draw(gamebox.from_text(300, 200, "Starting in 2", 50, "red"))
            if 60 <= counter <= 90:
                camera.draw(gamebox.from_text(300, 200, "Starting in 1", 50, "red"))
            if counter >= 90:
                camera.draw(gamebox.from_text(300, 200, "Go!", 50, "red"))

        if counter >= 100:
            # animates turtle
            # he will face the direction he is moving in
            player = gamebox.from_image(player.x, player.y, turtle)

            # allows player to move
            if pygame.K_LEFT in keys:
                turtle = "turtleleft.png"
                player.x -= 3
            if pygame.K_RIGHT in keys:
                turtle = "turtleright.png"
                player.x += 3
            if pygame.K_UP in keys:
                turtle = "turtleup.png"
                player.y -= 3
            if pygame.K_DOWN in keys:
                turtle = "turtledown.png"
                player.y += 3

        # keeps player on screen
        if player.x < 15:
            player.x = 15
        if player.x > 585:
            player.x = 585
        if player.y > 385:
            player.y = 385
        if counter % 100 == 0:
            left_fish.append(gamebox.from_image(0, random.randint(50, 325), "left_fish.png"))
            right_fish.append(gamebox.from_image(600, random.randint(50, 325), "right_fish.png"))
        if counter % 25 == 0:
            fish_yspeed = -fish_yspeed
        for one in left_fish:
            fish.append(one)
            one.xspeed = fish_xspeed
            one.yspeed = fish_yspeed
            camera.draw(one)
            one.move_speed()
            if one.y < 40:
                one.y = 40
            if one.y > 350:
                one.y = 350
        for two in right_fish:
            fish.append(two)
            two.xspeed = -fish_xspeed
            two.yspeed = fish_yspeed
            camera.draw(two)
            two.move_speed()
            if two.y < 40:
                two.y = 40
            if two.y > 350:
                two.y = 350

        if player.y < 20:
            level += 1
            score += 50
            fish_xspeed += 0.5
            fish_yspeed += 1
            pause = True

    # the player crossed the river and moves on to the next level
    if player.y < 20:
        camera.draw(gamebox.from_text(300, 150, "+ 50 Points", 35, "red"))
        camera.draw(gamebox.from_text(300, 200, f"Level {level - 1} complete!", 50, "white"))
        camera.draw(gamebox.from_text(300, 250, f"Press the spacebar to begin Level {level}", 25, "white"))

    if pygame.K_SPACE in keys:
        counter = 0
        pause = False
        player.x = 300
        player.y = 400
        obstacles.append(gamebox.from_image(random.randint(0, 600), random.randint(50, 325), "rock.png"))
        # more fish
        # left_fish.append(gamebox.from_image(random.randint(0, 600), random.randint(50, 325), "left_fish.png"))
        # right_fish.append(gamebox.from_image(random.randint(0, 600), random.randint(50, 325), "right_fish.png"))
        leaves = [gamebox.from_image(random.randint(0, 600), random.randint(50, 325), "leaf.png"),
                  gamebox.from_image(random.randint(0, 600), random.randint(50, 325), "leaf.png"),
                  gamebox.from_image(random.randint(0, 600), random.randint(50, 325), "leaf.png")]

    for rock in obstacles:
        camera.draw(rock)
        player.move_to_stop_overlapping(rock)

    for leaf in leaves:
        if player.touches(leaf, -3, -3):
            score += 10
            leaves.remove(leaf)
        camera.draw(leaf)

    for each in fish:
        if player.touches(each, -20, -20):
            pause = True
            camera.draw(gamebox.from_text(300, 200, "Game Over!", 75, "red"))
            camera.draw(gamebox.from_text(300, 250, 'Press the "R" key to restart', 35, "white"))

    # Game restart tends to lag on my own laptop, but it is working as it should with the correct code
    if pygame.K_r in keys:
        pause = False

        # reset original variables
        level = 1
        counter = 0
        score = 0
        fish_xspeed = 0.5
        fish_yspeed = 1
        left_fish.clear()
        right_fish.clear()
        fish.clear()
        obstacles.clear()

        # initial fish to spawn
        left_fish.append(gamebox.from_image(random.randint(0, 600), random.randint(50, 325), "left_fish.png"))
        left_fish.append(gamebox.from_image(random.randint(0, 600), random.randint(50, 325), "left_fish.png"))
        left_fish.append(gamebox.from_image(random.randint(0, 600), random.randint(50, 325), "left_fish.png"))

        right_fish.append(gamebox.from_image(random.randint(0, 600), random.randint(50, 325), "right_fish.png"))
        right_fish.append(gamebox.from_image(random.randint(0, 600), random.randint(50, 325), "right_fish.png"))
        right_fish.append(gamebox.from_image(random.randint(0, 600), random.randint(50, 325), "right_fish.png"))

        player.x = 300
        player.y = 400
    camera.display()


gamebox.timer_loop(30, tick)
