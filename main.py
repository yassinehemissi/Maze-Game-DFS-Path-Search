import pygame
import sys
from config import DISPLAY
from maze import gameMaze
from menu import game_menu
from player import player
import path
#from menu import game_menu


newPath = None

currentPage = 0 


def main():
    global currentPage
    pygame.init()

    pygame.time.Clock()

    FramePerSec = pygame.time.Clock()

    screen = pygame.display.set_mode(
        (DISPLAY["WIDTH"] * DISPLAY["MULTIPLIER"], DISPLAY["HEIGHT"] * DISPLAY["MULTIPLIER"]))

    def generate_game():
        global newPath
        newPath = None
        while newPath == None:
            gameMaze.generate_maze()
            player.update_position(1, gameMaze.start["x"], gameMaze.start["y"])
            newPath = path.PathFinder(
                gameMaze.maze, gameMaze.start, gameMaze.end)

    generate_game()
    while True:
        if (currentPage) == 0:
            game_menu.display_menu(screen)
            game_menu.display_arrow(screen)
            pygame.display.update()
            FramePerSec.tick(DISPLAY["FPS"])
            pygame.display.set_caption("FPS: " + str(FramePerSec.get_fps()))
            try:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_UP:
                            game_menu.update_arrow("UP")
                        elif event.key == pygame.K_DOWN:
                            game_menu.update_arrow("DOWN")
                        elif event.key == pygame.K_RETURN:
                            if (game_menu.arrow_pos == 0):
                                currentPage = 1
                            elif (game_menu.arrow_pos == 1):
                                pygame.quit()
                                sys.exit()                         
            except:
                print("")
            continue 
        isOver = False
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        isOver = player.update_position(
                            gameMaze.maze[player.y - 1][player.x], player.x, player.y - 1)
                    elif event.key == pygame.K_DOWN:
                        isOver = player.update_position(
                            gameMaze.maze[player.y + 1][player.x], player.x, player.y + 1)
                    elif event.key == pygame.K_LEFT:
                        isOver = player.update_position(
                            gameMaze.maze[player.y][player.x - 1], player.x - 1, player.y)
                    elif event.key == pygame.K_RIGHT:
                        isOver = player.update_position(
                            gameMaze.maze[player.y][player.x + 1], player.x + 1, player.y)
                    elif event.key == pygame.K_SPACE:
                        generate_game()
            if (isOver):
                generate_game()

        except:
            print("")
        gameMaze.display_maze(screen)
        if (newPath.pathfound != None):
            newPath.display_path(screen)
        player.display_player(screen)
        # game_menu.display_menu(screen)
        pygame.display.update()
        FramePerSec.tick(DISPLAY["FPS"])
        pygame.display.set_caption("FPS: " + str(FramePerSec.get_fps()))


main()
