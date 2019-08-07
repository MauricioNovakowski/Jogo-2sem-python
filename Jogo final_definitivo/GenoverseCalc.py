import pygame, os, random
import os
from pygame.locals import QUIT, MOUSEBUTTONDOWN, KEYDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT, KEYUP, Rect
from random import randint

# 0 - Menu Principal
# 1 - Jogando
# 2 - Início
# 3 - personagem
# 4 - créditos
# 5 - Tutorial
# 6 - GameOver

estado = 0
indice_menu = 0
Nave = 0

#definir a interface do display
L, A = 794, 600



def calcular_menu(menu_opcoes):
    global indice_menu
    for opcao in menu_opcoes:
        opcao_renderizada = font.render(opcao['text'], True, opcao['cor'])
        opcao['surface'] = opcao_renderizada
        opcao['rect'] = opcao_renderizada.get_rect()
        opcao['rect'].x = opcao['pos'][0]
        opcao['rect'].y = opcao['pos'][1]
    if indice_menu < 0:
        indice_menu = 0
    if indice_menu == len(menu_opcoes):
        indice_menu = len(menu_opcoes) - 1


def pintar_menu(scr, menu_opcoes):
    global indice_menu
    for opcao in menu_opcoes:
        scr.blit(opcao['surface'], opcao['pos'])
    menu_selecionado = menu_opcoes[indice_menu]
    pos = menu_selecionado['pos']
    pygame.draw.circle(scr, (31, 247, 3), pos, 10)


def capturar_menu(menu_opcoes, e):
    for opcao in menu_opcoes:
        if opcao['rect'].collidepoint(e.pos[0], e.pos[1]):
            if estado == 3:
                global Nave
                if opcao['nave'] == 'amarela':
                    Nave = pygame.image.load('images/MS_amarela.png').convert_alpha()
                elif opcao['nave'] == 'vermelha':
                    Nave = pygame.image.load('images/MainShip.png').convert_alpha()
                else:
                    Nave = pygame.image.load('images/MS_verde.png').convert_alpha()
            opcao['execute']()
            pygame.draw.rect(tela_menu, (255, 0, 0), opcao['rect'], 3)



def menu_inicio():
    global estado
    estado = 2


def menu_principal():
    global estado
    estado = 0


def menu_jogar():
    global estado
    estado = 1


def menu_personagem():
    global estado
    estado = 3


def menu_créditos():
    global estado
    estado = 4


def menu_tutorial():
    global estado
    estado = 5

def menu_GameOver():
    global estado
    estado = 6














os.environ['SDL_VIDEO_WINDOW_POS'] = "50,50"
pygame.init()
Clock = pygame.time.Clock()
Tela = pygame.display.set_mode((L, A))
pygame.display.set_caption("GenoVerse")
tela_menu = pygame.display.set_mode((800, 600), 0, 32)
#linux font
font = pygame.font.Font('/usr/share/fonts/truetype/abyssinica/AbyssinicaSIL-R.ttf', 55)
#font = pygame.font.Font('C:/Windows/Fonts/Georgia.TTF', 55)
fundo_menu = pygame.image.load('fundo.jpg')
GameOver_img = pygame.image.load('gameover.png').convert()
creditos_img = pygame.image.load('creditos.png').convert()
tutorial_img = pygame.image.load('tutorial.png').convert()


p1 = pygame.image.load('p1.jpg')
p2 = pygame.image.load('p2.jpg')
p3 = pygame.image.load('p3.jpg')


Nuvem = pygame.image.load('fundo_unico.png').convert()
Meteoro = pygame.image.load('Meteorito7.png').convert_alpha()


#cores
Verde = (0,255,0)
Amarelo = (255,255,0)
Vermelho = (255,0,0)
Cor = (255,255,255)


# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
myfont = pygame.font.SysFont("monospace", 15)

#music
pygame.mixer.music.load('Genoverse.mp3')
pygame.mixer.music.play(-1, 0)
if os.path.exists('inicial.mp3'):
    pygame.mixer.music.load('inicial.mp3')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1)


lista_opcoes = []
lista_opcoes.append({'text': 'Início', 'pos': [70, 400], 'cor': (31, 247, 3), 'execute': menu_inicio})
lista_opcoes.append({'text': 'Créditos', 'pos': [300, 450], 'cor': (31, 247, 3), 'execute': menu_créditos})
lista_opcoes.append({'text': 'Sair', 'pos': [600, 500], 'cor': (31, 247, 3), 'execute': exit})

lista_opcoes_config = []
lista_opcoes_config.append({'text': 'Selecionar Personagem', 'pos': [100, 400], 'cor': (31, 247, 3), 'execute': menu_personagem})
lista_opcoes_config.append({'text': 'Tutorial', 'pos': [60, 500], 'cor': (31, 247, 3), 'execute': menu_tutorial})
lista_opcoes_config.append({'text': 'Voltar', 'pos': [600, 500], 'cor': (31, 247, 3), 'execute': menu_principal})

lista_opcoes_personagem = []
lista_opcoes_personagem.append({'text': 'Select', 'pos': [80, 470], 'cor': (255, 255, 0), 'execute': menu_jogar, 'nave': 'amarela'})
lista_opcoes_personagem.append({'text': 'Select', 'pos': [300, 470], 'cor': (255, 0, 0,), 'execute': menu_jogar, 'nave': 'vermelha'})
lista_opcoes_personagem.append({'text': 'Select', 'pos': [580, 470], 'cor': (31, 247, 3), 'execute': menu_jogar, 'nave': 'verde'})
lista_opcoes_personagem.append({'text': 'Voltar', 'pos': [300, 540], 'cor': (31, 247, 3), 'execute': menu_principal})

lista_opcoes_tutorial = []
lista_opcoes_tutorial.append({'text': 'Voltar', 'pos': [600, 500], 'cor': (31, 247, 3), 'execute': menu_principal})

lista_opcoes_créditos = []
lista_opcoes_créditos.append({'text': 'Voltar', 'pos': [600, 500], 'cor': (31, 247, 3), 'execute': menu_principal})

lista_opcoes_GameOver = []
lista_opcoes_GameOver.append({'text': 'Voltar', 'pos': [600, 500], 'cor': (31, 247, 3), 'execute': menu_inicio})

while True:
    tela_menu.fill((0, 0, 0))


  # Calcular Regras
    if estado == 0:
        calcular_menu(lista_opcoes)
        tela_menu.blit(fundo_menu, (0, 0))
    if estado == 1:
        #variaveis de inicializacao
        vel_relx = 0
        rect_meteoro = []
        rect_meteoro.clear()
        rect_meteoro.append([Meteoro.get_rect(), random.randint(50, 790), 0])
        Chase_Calc = []
        Angulo_Nave = 0
        Escala = 0.5
        Fundoy = 0
        Tremor = 0
        Cont = 0
        Integridade = 100
        Pontos = 0
        GameOver = 0
        x = 400
        y = 300
        velyd = 0
        velyu = 0
        velxr = 0
        velxl = 0

        #loop de gameplay
        while estado == 1:
            Clock.tick(120)
            Cont += 1
            # paralax
            rep_y = Fundoy % Nuvem.get_rect().height
            Tela.blit(Nuvem, (0, rep_y - Nuvem.get_rect().height))
            if rep_y < A:
                Tela.blit(Nuvem, (0, rep_y))
            Fundoy += 8

            # movimento
            y += velyd - velyu
            x += velxr - velxl
            if x > 400 and velxr > 0:
                velxr = (5 / ((x - 320) / 80))
                Angulo_Nave = (-45 / ((x - 320) / 80))
                if x > 740:
                    Angulo_Nave = (-45 / ((x - 320) / 40))
            if x < 400 and velxl > 0:
                velxl = (5 / ((480 - x) / 80))
                Angulo_Nave = (45 / ((480 - x) / 80))
                if x < 60:
                    Angulo_Nave = (45 / ((480 - x) / 40))
            if not 40 <= x <= 760 or not 250 <= y <= 550:
                if y <= 250:
                    velyu = 0
                if y >= 550:
                    velyd = 0
                if x <= 40:
                    velxl = 0
                if x >= 760:
                    velxr = 0
            if Angulo_Nave < 0:
                Angulo_Nave += 0.02
            elif Angulo_Nave > 0:
                Angulo_Nave -= 0.02
            if 250 <= y:
                y -= 0.1


            # Angulo rotacao nave
            Nave_Rot = pygame.transform.rotate(Nave, Angulo_Nave)
            r = Nave_Rot.get_rect()
            Nave_Escala = pygame.transform.scale(Nave_Rot, (int(r.w * Escala), int(r.h * Escala)))

            r1 = Nave_Escala.get_rect()
            r1.x = x - r1.centerx
            r1.y = y - r1.centery

            #movimentação Chase
            if Cont % 2 == 0:
                if velxr > velxl:
                    Chase_Calc.append(velxr)
                elif velxr < velxl:
                    Chase_Calc.append(-velxl)
                else:
                    Chase_Calc.append(0)
                if len(Chase_Calc) == 16:
                    del Chase_Calc[0]




            # movimentação meteoro
            n_met = len(rect_meteoro)
            for m in range(n_met):
                rect_meteoro[m][2] += 2
            if rect_meteoro[0][2] >= 630:
                for m in range(n_met):
                    rect_meteoro[m][2] = random.randint(-30,0)
                if m == 0:
                    vel_relx = sum(Chase_Calc) / len(Chase_Calc) / 2
                    rect_meteoro[0][1] = x+(vel_relx*(y/2))-22
                    if rect_meteoro[0][1] > 738:
                        rect_meteoro[0][1] = 738
                    elif rect_meteoro[0][1] < 18:
                        rect_meteoro[0][1] = 18
                else:
                    rect_meteoro[m][1] = random.randint(50, 790)
                if len(rect_meteoro) < int(10/(1+(11*(1.05**-Distancia)))):
                    rect_meteoro.append([Meteoro.get_rect(), random.randint(50, 790), random.randint(-30,0)])



            # Pintar
            for m in range(n_met):
                rect_meteoro[m][0][0] = rect_meteoro[m][1]
                rect_meteoro[m][0][1] = rect_meteoro[m][2]
                rect_meteoro[m][0][2] = 30
                rect_meteoro[m][0][3] = 30
            for m in range(n_met):
                Tela.blit(Meteoro, (rect_meteoro[m][1], rect_meteoro[m][2]))

            # colisão
            n_met = len(rect_meteoro)
            for m in range(n_met):
                rect_meteoro[m][2] += 0.1

            for m in range(n_met):
                if r1.colliderect(rect_meteoro[m][0]) or Integridade <= 0:
                    #play == False
                    menu_GameOver()
                    pygame.display.update()
                    tela_menu.blit(GameOver_img, (0, 0))
                    Tela.blit(GameOver_img, (0, 0))

                Ponto = "Pontos: " + str(int(Pontos))
                if y <= 300:
                    Pontos += 0.5
                    Cor = Verde
                elif y <= 500:
                    Pontos += 0.1
                    Cor = Amarelo
                else:
                    Cor = Vermelho

                VisorDireito = myfont.render(Ponto, 50, Cor, (100, 100, 50))
                Tela.blit(VisorDireito, (650, 20))

            # Tremores em cantos
            if x > 740 or x < 60 or y < 280:
                Integridade = Integridade - 0.008
                if Cont % 2 == 0:
                    Tremor = 3
                else:
                    Tremor = -3
            else:
                Tremor = 0

            # desenha os quadrados e a tela e a nave
            Tela.blit(Nave_Escala, [(r1.x + Tremor), (r1.y + Tremor)])
            for m in range(n_met):
                Tela.blit(Meteoro, (rect_meteoro[m][1], rect_meteoro[m][2]))

            # integridade estrutural
            IntegridadeTotal = "Integridade: " + str(int(Integridade))
            if Integridade > 75:
                Cor = Verde
            elif Integridade > 25:
                Cor = Amarelo
            else:
                Cor = Vermelho
            VisorDireito = myfont.render(IntegridadeTotal, 1, Cor, (50, 50, 50))
            Tela.blit(VisorDireito, (650, 550))

            # calculo dist
            Distancia = int((Cont // 120))
            VisorEsquerdo = myfont.render(("Distancia: " + str(Distancia)), 1, (0, 0, 255), (50, 50, 50))
            Tela.blit(VisorEsquerdo, (20, 550))

            # printa tela
            pygame.display.flip()

            # sai do jogo
            for e in pygame.event.get():
                if e.type == QUIT:
                    exit()
                # comandos de movimento
                if e.type == KEYDOWN:
                    if e.key == K_DOWN and y < 550:
                        velyd = 5
                        velyu = 0
                    elif e.key == K_UP and y > 250:
                        velyu = 2.5
                        velyd = 0
                        if velxl == 0 and velxr == 0:
                            Angulo_Nave = 0
                    elif e.key == K_LEFT and x > 40:
                        velxl = 5
                        velxr = 0
                        Angulo_Nave = 45
                    elif e.key == K_RIGHT and x < 760:
                        velxr = 5
                        velxl = 0
                        Angulo_Nave = -45
                elif e.type == KEYUP:
                    if e.key == K_DOWN:
                        velyd = 0
                    elif e.key == K_UP:
                        velyu = 0
                    elif e.key == K_LEFT:
                        velxl = 0
                    elif e.key == K_RIGHT:
                        velxr = 0
                # informacoes tecnicas

    if estado == 2:
        calcular_menu(lista_opcoes_config)
        tela_menu.blit(fundo_menu, (0, 0))
    if estado == 3:
        calcular_menu(lista_opcoes_personagem)
        tela_menu.blit(p2, (250, 20))
        tela_menu.blit(p1, (0, 20))
        tela_menu.blit(p3, (500, 20))
    if estado == 4:
        calcular_menu(lista_opcoes_créditos)
        tela_menu.blit(creditos_img,(0,0))
    if estado == 5:
        calcular_menu(lista_opcoes_tutorial)
        tela_menu.blit(tutorial_img,(0,0))
    if estado == 6:
        calcular_menu(lista_opcoes_GameOver)
        tela_menu.blit(GameOver_img, (0, 0))


    #Pintar
    if estado == 0:
        pintar_menu(tela_menu, lista_opcoes)
    elif estado == 2:
        pintar_menu(tela_menu, lista_opcoes_config)
    elif estado == 3:
        pintar_menu(tela_menu, lista_opcoes_personagem)
    elif estado == 4:
        pintar_menu(tela_menu, lista_opcoes_créditos)
    elif estado == 5:
        pintar_menu(tela_menu, lista_opcoes_tutorial)
    elif estado == 6:
        pintar_menu(tela_menu, lista_opcoes_GameOver)




    pygame.display.update()

    #Capturar Eventos
    for e in pygame.event.get():
        if e.type == QUIT:
            exit()
        elif e.type == MOUSEBUTTONDOWN:
            if estado == 0:
                capturar_menu(lista_opcoes, e)
            elif estado == 2:
                capturar_menu(lista_opcoes_config, e)
            elif estado == 3:
                capturar_menu(lista_opcoes_personagem, e)
            elif estado == 4:
                capturar_menu(lista_opcoes_créditos, e)
            elif estado == 5:
                capturar_menu(lista_opcoes_tutorial, e)
            elif estado == 6:
                capturar_menu(lista_opcoes_GameOver, e)


        elif e.type == KEYDOWN:
            if estado == 0 or estado == 2:
                if e.key == K_UP:
                    indice_menu -= 1

                elif e.key == K_DOWN:
                    indice_menu += 1
