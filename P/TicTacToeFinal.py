import pygame
from collections import Counter
pygame.mixer.init()
BOARD_EMPTY = 0
BOARD_PLAYER_X = 1
BOARD_PLAYER_O = -1
screen= pygame.display.set_mode((600,600))
pygame.display.set_caption('Tic-Tac-Toe')
background_dd = pygame.image.load("/Users/jeelp/Desktop/P/fluid-7.png")
background_dd = pygame.transform.scale(background_dd,(600,600))
circle_image = pygame.image.load("/Users/jeelp/Desktop/P/cancel.png")
circle_image = pygame.transform.scale(circle_image, (150,150))
cross_image = pygame.image.load("/Users/jeelp/Desktop/P/o_letter.png") #reversed name of images.
cross_image = pygame.transform.scale(cross_image, (150,150))
click_sound= pygame.mixer.Sound("/Users/jeelp/Desktop/P/Mouse_click.mp3")
mouse_position=[]
player_turn_flag,running_flag=True,True
ai_position = []

def player(s):
    counter = Counter(s)
    x_places = counter[1]
    o_places = counter[-1]
    if x_places + o_places == 9:
        return None
    elif x_places > o_places:
        return BOARD_PLAYER_O 
    else:
        return BOARD_PLAYER_X

def actions(s):
    play = player(s)
    actions_list = [(play, i) for i in range(len(s)) if s[i] == BOARD_EMPTY]
    return actions_list

def result(s, a):
    (play, index) = a
    s_copy = s.copy()
    s_copy[index] = play
    return s_copy

def terminal(s):
    for i in range(3):
        if s[3 * i] == s[3 * i + 1] == s[3 * i + 2] != BOARD_EMPTY:
            return s[3 * i]
        if s[i] == s[i + 3] == s[i + 6] != BOARD_EMPTY:
            return s[i]

    if s[0] == s[4] == s[8] != BOARD_EMPTY:
        return s[0]
    if s[2] == s[4] == s[6] != BOARD_EMPTY:
        return s[2]

    if player(s) is None:
        return 0
    
    return None

def utility(s, cost):
    term = terminal(s)
    if term is not None:
        return (term, cost)
    
    action_list = actions(s)
    utils = []
    for action in action_list:
        new_s = result(s, action)
        utils.append(utility(new_s, cost + 1))

    score = utils[0][0]
    idx_cost = utils[0][1]
    play = player(s)
    if play == BOARD_PLAYER_X:
        for i in range(len(utils)):
           if utils[i][0] > score:
                score = utils[i][0]
                idx_cost = utils[i][1]
    else:
        for i in range(len(utils)):
           if utils[i][0] < score:
                score = utils[i][0]
                idx_cost = utils[i][1]
    return (score, idx_cost) 

def minimax(s):
    action_list = actions(s)
    utils = []
    for action in action_list:
        new_s = result(s, action)
        utils.append((action, utility(new_s, 1)))

    if len(utils) == 0:
        return ((0,0), (0, 0))

    sorted_list = sorted(utils, key=lambda l : l[0][1])
    action = min(sorted_list, key = lambda l : l[1])
    return action


def print_board(s):
    def convert(num):
        if num == BOARD_PLAYER_X:
            return 'X'
        if num == BOARD_PLAYER_O:
            return 'O'
        return '_'

    i = 0
    for _ in range(3):
        for _ in range(3):
            print(convert(s[i]), end=' ')
            i += 1
        print()


def position_integrator(pos_tup):
    global s
    for i in range(len(pos_tup)):
        if pos_tup[i] < 200:
            pos_tup[i] = 30
        elif pos_tup[i] <= 400:
            pos_tup[i] = 230
        else:
            pos_tup[i] = 430
    if pos_tup==[30,30]:
        s[0]=1
    elif pos_tup==[230,30]:
        s[1]=1
    elif pos_tup==[430,30]:
        s[2]=1
    elif pos_tup==[30,230]:
        s[3]=1
    elif pos_tup==[230,230]:
        s[4]=1
    elif pos_tup==[430,230]:
        s[5]=1
    elif pos_tup==[30,430]:
        s[6]=1
    elif pos_tup==[230,430]:
        s[7]=1
    elif pos_tup==[430,430]:
        s[8]=1
    return pos_tup

def ai_position_generator(s):
    ai_position=[]
    for i in range(len(s)):
        if s[i]==-1:
            if i ==0:
                ai_position.append([30,30])
            if i ==1:
                ai_position.append([230,30])
            if i ==2:
                ai_position.append([430,30])
            if i ==3:
                ai_position.append([30,230])
            if i ==4:
                ai_position.append([230,230])
            if i ==5:
                ai_position.append([430,230])
            if i ==6:
                ai_position.append([30,430])
            if i ==7:
                ai_position.append([230,430])
            if i ==8:
                ai_position.append([430,430])
    return ai_position

def tittle_screen():
    runnes=True
    tittle_image=pygame.image.load("/Users/jeelp/Desktop/P/tittle.png")
    tittle_image=pygame.transform.scale(tittle_image, (500,100))
    start_text_image=pygame.image.load("/Users/jeelp/Desktop/P/Start_text.png")
    start_text_image=pygame.transform.scale(start_text_image, (400,50))
    while runnes:
        screen.blit(background_dd,(0,0))
        screen.blit(tittle_image,(50,225))
        screen.blit(start_text_image,(100,325))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_sound.play()
                runnes = False
        pygame.display.flip()
    return 




if __name__ == '__main__':
    s = [BOARD_EMPTY for _ in range(9)]
    print('|------- WELCOME TO TIC TAC TOE -----------|')
    print('You are X while the Computer is O')
    tittle_screen()
    while running_flag and (terminal(s) is None):
        play = player(s)
        screen.blit(background_dd,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_flag = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click_sound.play()
                pos_tup=list(pygame.mouse.get_pos())
                pos_tup=position_integrator(pos_tup)
                winner = utility(s, 1)[0]
                mouse_position.append(pos_tup)
                player_turn_flag=False
        for posi in mouse_position:
            screen.blit(circle_image, posi)
        for posi in ai_position:
            screen.blit(cross_image, posi)
        lin1= pygame.draw.aaline(screen, (255, 255, 255), (200,00), (200,600))
        lin2= pygame.draw.aaline(screen, (255, 255, 255), (400,00), (400,600))
        lin3= pygame.draw.aaline(screen, (255, 255, 255), (00,200), (600,200))
        lin4= pygame.draw.aaline(screen, (255, 255, 255), (00,400), (600,400))
        pygame.display.flip()
        if not player_turn_flag:
            print('\n\nThe is computer is playing its turn')
            action = minimax(s)
            s = result(s, action[0])
            winner = utility(s, 1)[0]
            ai_position=ai_position_generator(s)
            player_turn_flag=True
            #print(bool(winner))
pygame.quit()



"""if play == BOARD_PLAYER_X and player_turn_flag:
    print('\n\nIt is your turn', end='\n\n')
    winner = utility(s, 1)[0]
    if winner == BOARD_PLAYER_X:
        print("You have won!")
    elif winner == BOARD_PLAYER_O:
        print("You have lost!")
    else:
        print("It's a tie.")"""