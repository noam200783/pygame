# from constantss import *
#
# import pygame
# def main():
#     index = 0
#     pygame.init()
#     global screen
#     screen_size = (WIDTH, HEIGHT)
#     screen = pygame.display.set_mode(screen_size)
#     pygame.display.set_caption("my game")
#     finish = False
#     while not finish:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 finish = True
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 screen.fill(COLORS[index])
#                 index = (index + 1) % len(COLORS)
#         pygame.display.flip()
#     pygame.quit()
# main()




from constants import *
import random
import pygame
def main():

    pygame.init()
    global screen
    global points
    global car_num
    global direction
    global speed
    speed = 4
    direction = True
    car_num = CARROTS_NUM_START
    points = 0
    screen_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("הכה את הסנאי")
    screen.fill(GREEN)
    sq_pos = rand_squirrel_location()
    finish = False
    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if after_mouse_click(pos, sq_pos[0], sq_pos[1]):
                    points += 1
                    direction=True
                    sq_pos=rand_squirrel_location()

            pos1 = pygame.mouse.get_pos()
            if pos1[1] > MIDLINE:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_NO)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        #speed += points/1000
        screen.fill(GREEN)
        add_text("Tahoma", 39,f"score:{points}", SCORE_TEXT_POS, WHITE)
        for i in range(3):
            # add_image(CARROT_IMAGE,START_X_POS_CAR+SPACE_X_POS_CAR* i,Y_POS_CAR,CARROT_WIDTH,CARROT_HEIGHT)
            add_image(HOLE_IMAGE,START_X_POS_HOL+SPACE_X_POS_HOL* i,Y_POS_HOL,HOLE_WIDTH,HOLE_HEIGHT)
        for i in range(car_num):
            add_image(CARROT_IMAGE, START_X_POS_CAR + SPACE_X_POS_CAR * i, Y_POS_CAR, CARROT_WIDTH, CARROT_HEIGHT)
        sq_pos = squirrel_move(sq_pos)
        add_image(SQUIRREL_IMAGE, sq_pos[0], sq_pos[1], SQUIRREL_WIDTH, SQUIRREL_HEIGHT)
        rectangle = pygame.Rect(0, MIDLINE, WINDOW_WIDTH, 500)
        pygame.draw.rect(screen, GREEN, rectangle)

        for i in range(3):
            add_image(HALF_HOLE_IMAGE,START_X_POS_HOL+SPACE_X_POS_HOL* i,MIDLINE,HALF_HOLE_WIDTH,HALF_HOLE_HEIGHT)

        if car_num < 1:
            screen.fill(B)
            add_text("Tahoma", 150, "GAME OVER", END_TEXT_POS, R)
        else:
            sq_pos = squirrel_move(sq_pos)

        speed += points / 1000
        pygame.display.flip()
    pygame.quit()


def add_image(img_path, x_pos, y_pos, width, height):
    img = pygame.image.load(img_path)
    img = pygame.transform.scale(img,(width,height))
    screen.blit(img, (x_pos, y_pos))


def rand_squirrel_location():
    random1 = random.randint(0,2)
    return [START_X_POS_HOL+50+SPACE_X_POS_HOL* random1,SQUIRREL_MAX_Y-1]

def add_text(font, font_size, massage, text_pos, color):
    font = pygame.font.SysFont(font,font_size)
    text = font.render(massage, True, color)
    screen.blit(text, text_pos )

def squirrel_move(current_Location):
    global direction, car_num, speed
    if direction:
        if current_Location[1] <= SQUIRREL_MIN_Y:
            direction = False
        else:
            current_Location[1] -= speed
    else:
        if current_Location[1] >= SQUIRREL_MAX_Y:
            direction = True
            car_num -= 1
            current_Location[0] = rand_squirrel_location()[0]
            pygame.time.wait(50)

        else:
            current_Location[1] += speed
    return current_Location


def after_mouse_click(pos,start_x_pos,start_y_pos):
    if (pos[0] >= start_x_pos) and (pos[0] <= start_x_pos+SQUIRREL_WIDTH):
        if pos[1] >= start_y_pos and pos[1] <= MIDLINE:
            return True
        else:
            return False







main()








