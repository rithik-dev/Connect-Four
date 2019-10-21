import pygame
from pygame.locals import *

WIDTH = 540
HEIGHT = 550

RADIUS = 30
ROWS = 6
COLS = 7

# COLORS
COLORS = {
    'BACKGROUND_COLOR': (0, 0, 255),
    'TEXT_COLOR': (0, 0, 0),
    'RED': (255, 0, 0),
    'YELLOW': (255, 255, 0),
    'BLUE': (0, 0, 200),
    'BLACK': (0, 0, 0)
}


def display_text(text, pos, size=30, color=COLORS['TEXT_COLOR']):
    """displays text on the screen

    Args:
        text (string): text to displat
        pos (tuple): pos of text to display (x,y)
        size (int, optional): size of font. Defaults to 30.
        color (tuple, optional): color of font. Defaults to COLORS['TEXT_COLOR'].

    Returns:
        None
    """
    myFont = pygame.font.SysFont('Comic Sans MS', size)
    textsurface = myFont.render(text, False, color)
    win.blit(textsurface, (pos[0], pos[1]))


def welcomeScreen():
    """this is the welcome screen
    """

    # making the mouse invisible
    pygame.mouse.set_visible(False)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == KEYDOWN and event.key == K_RETURN:
                return
            else:
                win.fill(COLORS['BACKGROUND_COLOR'])
                display_text(
                    'CONNECT 4', (WIDTH//2-130, HEIGHT*0.10), 50)
                display_text("Press 'ENTER' to start..",
                             (WIDTH//2-150, HEIGHT*0.80))
                pygame.display.update()


def drawBoard(circles):
    """function used to draw the board of the game

    Args:
        circles (list): data
    """
    win.fill(COLORS['BLUE'])

    pygame.draw.line(win, COLORS['BLACK'], (0, 85), (WIDTH, 85), 5)

    for row in range(0, ROWS):
        for col in range(0, COLS):
            pygame.draw.circle(
                win, COLORS[circles[row][col][2]], (circles[row][col][0], circles[row][col][1]), RADIUS)


def redrawGameWindow(circles, turn, winner_declared):
    """function used to blit items on the screen

    Args:
        circles (list): data
        turn (string): 'RED' or 'YELLOW'
    """

    drawBoard(circles)

    if not winner_declared:
        mouseX = pygame.mouse.get_pos()[0]
        pygame.draw.circle(win, COLORS[turn], (mouseX, 40), RADIUS)

    pygame.display.update()


def addCoin(circles, col, turn):
    """function used to add a coin to the respective column clicked

    Args:
        circles (list): data
        col (int): column
        turn (string): 'RED' OR 'YELLOW'
    """
    color_added = False
    for row in range(0, ROWS):
        if circles[row][col][2] == 'BLACK':
            color_added = True
            circles[row][col][2] = turn
            break
    return color_added


def checkWinCondition(circles, winner):
    """function used to check win condition i.e. for every coin , if 4 corresponding coins are present

    Args:
        circles (list): data
        winner (string): 'RED' OR 'YELLOW'

    Returns:
        True: if a winner is found
    """

    for row in range(0, ROWS):
        for col in range(0, COLS):
            # check horizontally right
            if col <= 3:
                if circles[row][col][2] == winner and circles[row][col+1][2] == winner and circles[row][col+2][2] == winner and circles[row][col+3][2] == winner:
                    return True
            # check horizontally left
            if col >= 3:
                if circles[row][col][2] == winner and circles[row][col-1][2] == winner and circles[row][col-2][2] == winner and circles[row][col-3][2] == winner:
                    return True
            # check vertically up
            if row <= 2:
                if circles[row][col][2] == winner and circles[row+1][col][2] == winner and circles[row+2][col][2] == winner and circles[row+3][col][2] == winner:
                    return True
            # check vertically down
            if row >= 3:
                if circles[row][col][2] == winner and circles[row-1][col][2] == winner and circles[row-2][col][2] == winner and circles[row-3][col][2] == winner:
                    return True
            # check diagonal from top left
            if row <= 2 and col >= 3:
                if circles[row][col][2] == winner and circles[row+1][col-1][2] == winner and circles[row+2][col-2][2] == winner and circles[row+3][col-3][2] == winner:
                    return True
            # check diagonal from top right
            if row <= 2 and col <= 3:
                if circles[row][col][2] == winner and circles[row+1][col+1][2] == winner and circles[row+2][col+2][2] == winner and circles[row+3][col+3][2] == winner:
                    return True
            # check diagonal from bottom left
            if row >= 3 and col >= 3:
                if circles[row][col][2] == winner and circles[row-1][col-1][2] == winner and circles[row-2][col-2][2] == winner and circles[row-3][col-3][2] == winner:
                    return True
            # check diagonal from bottom right
            if row >= 3 and col <= 3:
                if circles[row][col][2] == winner and circles[row-1][col+1][2] == winner and circles[row-2][col+2][2] == winner and circles[row-3][col+3][2] == winner:
                    return True


def getWinner(circles, turn):
    """function used to check for a winner 

    Args:
        circles (list): data
        turn (string): [description]

    Returns: 
        'RED' : if red is winner
        'YELLOW' : if yellow is winner
        'draw' : if game is draw
        None: if no winner found ... game is still progressing
    """

    if turn == 'RED' and checkWinCondition(circles, 'RED'):
        return 'RED'   # red wins

    if turn == 'YELLOW' and checkWinCondition(circles, 'YELLOW'):
        return 'YELLOW'  # yellow wins

    # checking for draw
    draw = True

    for row in range(0, ROWS):
        for col in range(0, COLS):
            if circles[row][col][2] == 'BLACK':
                draw = False
                break

    if draw:
        return 'DRAW'

    return None


def gameOver(winner):
    """function used to display the game over screen 

    Args:
        winner (string): 'RED' OR 'YELLOW' OR 'DRAW'
    """
    while True:
        win.fill(COLORS['BACKGROUND_COLOR'])
        display_text("CONNECT 4", (WIDTH*0.2, HEIGHT*0.2), 50)
        if winner != 'DRAW':
            display_text("WINNER  : ", (WIDTH*0.19, HEIGHT*0.5), 50)
            pygame.draw.circle(win, COLORS[winner], (int(
                WIDTH*0.78), int(HEIGHT*0.5+35)), RADIUS)
        else:
            display_text("DRAW", (WIDTH*0.35, HEIGHT*0.5),
                         50, color=COLORS['RED'])

        display_text("Press 'R' to restart",
                     (WIDTH*0.65, HEIGHT*0.92), 20)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == KEYDOWN and event.key == K_r:  # restart game
                return


def mainGame():
    """main game function
    """

    circles = [[0 for x in range(COLS)] for y in range(ROWS)]

    # adding X and Y of circles to the circles list
    offset = 15
    startX = RADIUS+offset
    startY = HEIGHT-RADIUS-offset
    Y = startY

    circle_color = 'BLACK'
    winner_declared = False
    winner = ''

    for row in range(0, ROWS):
        X = startX
        for col in range(0, COLS):
            circles[row][col] = [X, Y, circle_color]
            X += RADIUS*2+offset
        Y -= RADIUS*2+offset

    turn = 'RED'

    while True:
        redrawGameWindow(circles, turn, winner_declared)

        if winner_declared:
            pygame.time.delay(500)
            return winner

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                mouseX = pygame.mouse.get_pos()[0]
                for row in range(0, ROWS):
                    for col in range(0, COLS):
                        circleX = circles[row][col][0]
                        if circleX-RADIUS-offset/2 < mouseX < circleX+RADIUS+offset/2:
                            if turn == 'RED':
                                color_added = addCoin(circles, col, turn)
                                turn = 'YELLOW'
                            elif turn == 'YELLOW':
                                color_added = addCoin(circles, col, turn)
                                turn = 'RED'
                            if color_added:
                                break
                    if color_added:
                        break
                if color_added:
                    winner = getWinner(
                        circles, 'RED' if turn is 'YELLOW' else 'YELLOW')
                    if winner != None:
                        winner_declared = True


if __name__ == "__main__":
    pygame.init()

    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Connect 4")

    while True:
        welcomeScreen()
        winner = mainGame()
        gameOver(winner)
