from tkinter.font import BOLD
import pygame
import random


board_size = 10



score = 0

game_arr = [[" " for x in range (board_size)] for y in range(board_size)]

game_arr [2][3] = "2"

game_arr [0][3] = "2"
print(game_arr)

screen_width = screen_height = 100*board_size
interval = int(screen_width/(board_size*2))

pygame.init()
black=(0,0,0)
white=(255,255,255)
screen = pygame.display.set_mode((screen_width + 1,screen_height + 100))
screen.fill(white)



myFont = pygame.font.SysFont("arial", 30)
myFont.set_bold(BOLD)

def draw_grid():
    for x in range(0,board_size):
        for y in range(0,board_size):
            num = myFont.render(game_arr[x][y],1,black)
            text_rect = num.get_rect(center=((interval)*2*y + interval,(interval)*2*x + interval))
            screen.blit(num,text_rect)
            pygame.display.update()
            
def update_score():
    score_text = myFont.render(str(score),1,black)
    score_rect = num.get_rect(center=(int(screen_width/2),screen_height + 50))
    screen.blit(score_text,score_rect)


### pass a string to myFont.render
num = myFont.render("2", 1, black)
text_rect = num.get_rect(center=(interval, interval))

def drawGrid():
    blockSize = int(screen_width/board_size) #Set the size of the grid block
    for x in range(0, screen_width, blockSize):
        for y in range(0, screen_height, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, black, rect, 1)
            
def move_up():
    for col in range (0,board_size):
        for row in range(0,board_size):
            if game_arr[row][col] != " ":
                temp = row
                while(temp != 0 and game_arr[temp-1][col] == " "):
                    temp -= 1
                if temp != row:
                    game_arr[temp][col] = game_arr[row][col]
                    game_arr[row][col] = " "
                if temp != 0:
                    if game_arr[temp-1][col] == game_arr[temp][col]:
                        global score 
                        score += (int(game_arr[temp-1][col]) + int(game_arr[temp][col]))
                        game_arr[temp-1][col] = str(int(game_arr[temp-1][col]) + int(game_arr[temp][col]))
                        game_arr[temp][col] = " "

                    

def move_down():
    for col in range (board_size - 1,-1,-1):
        for row in range(board_size - 1, -1,-1):
            if game_arr[row][col] != " ":
                temp = row
                while(temp != board_size - 1 and game_arr[temp+1][col] == " "):
                    temp += 1
                if temp != row:
                    game_arr[temp][col] = game_arr[row][col]
                    game_arr[row][col] = " "
                if temp != board_size - 1:
                    if game_arr[temp+1][col] == game_arr[temp][col]:
                        global score 
                        score += int(game_arr[temp+1][col]) + int(game_arr[temp][col])
                        game_arr[temp+1][col] = str(int(game_arr[temp+1][col]) + int(game_arr[temp][col]))
                        game_arr[temp][col] = " "
                    
def move_r_l(lOrR):
    if lOrR == "L":
        start = 0
        end = board_size
        itr = 1
        check = board_size - 1
    if lOrR == "R":
        start = board_size - 1
        end = -1
        itr = -1
        check = 0
    for row in range(start,end,itr):
        for col in range(start,end,itr):
            if game_arr[row][col] != " ":
                temp = col
                while(temp != start and game_arr[row][temp+itr*-1] == " "):
                    temp += itr*-1
                if temp != col:
                    game_arr[row][temp] = game_arr[row][col]
                    game_arr[row][col] = " "
                if temp != start:
                    if game_arr[row][temp - itr] == game_arr[row][temp]:
                        global score 
                        score += (int(game_arr[row][temp-itr]) + int(game_arr[row][temp]))
                        game_arr[row][temp-itr] = str(int(game_arr[row][temp-itr]) + int(game_arr[row][temp]))
                        game_arr[row][temp] = " "

def game_over():
    for x in game_arr:
        for y in x:
            if y == " ":
                return True
    return False


def place_random_2():
    x = random.randrange(0,board_size)
    y = random.randrange(0,board_size)
    while(game_arr[x][y] != " "):
        x = random.randrange(board_size)
        y = random.randrange(board_size)
    #print(x,y)
    game_arr[x][y] = "2"
run = True
drawGrid()
draw_grid()
while run:
    


    e = pygame.event.wait()
    if e.type == pygame.QUIT:
        run = False
    elif e.type == pygame.KEYDOWN:
        drawGrid()
        draw_grid()
        if e.key == pygame.K_LEFT:
            move_r_l("L")
        elif e.key == pygame.K_RIGHT:
            move_r_l("R")
        elif e.key == pygame.K_UP:
            move_up()
        elif e.key == pygame.K_DOWN:
            move_down()
        #print("hi")
        place_random_2()
        
        run = game_over()
        screen.fill(white)
        update_score()
        drawGrid()
        draw_grid()
        
    elif e.type != pygame.KEYDOWN:
        continue
