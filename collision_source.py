import pyxel
from random import randint


#direcoes carro
CIMA = 0
DIREITA = 1
BAIXO = 2
ESQUERDA = 3
PARADO = 4


class CarGame:
    def __init__(self):
        pyxel.init(200, 200, caption='COLLISION')
        
        self.iniciox = 100
        self.inicioy = 188
        self.x = 30
        self.x2 = 30
        self.x3 = 30
        self.y = 0
        self.y2 = 0
        self.y3 = 0
        self.direcao = 4
        self.tamanho_sprite = 30
        self.largura = 16
        self.altura = 12
        self.colidiu = False
        self.colisao = 0
        self.start = 0

        pyxel.run(self.update, self.draw)


    def update(self):
        #controles
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btn(pyxel.KEY_UP):
            self.direcao = CIMA
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.direcao = DIREITA
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.direcao = BAIXO
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.direcao = ESQUERDA

        #aceleração carro e colisão com a parede
        if pyxel.frame_count % 1 == 0:
            if self.direcao == CIMA:
                if self.inicioy - self.tamanho_sprite < 0:
                    self.inicioy = 188
                else:
                    self.inicioy -= 3
            elif self.direcao == BAIXO:
                if self.inicioy + self.tamanho_sprite > pyxel.height - self.tamanho_sprite:
                    self.inicioy =  pyxel.height - self.tamanho_sprite
                    self.inicioy = 188
                else:
                    self.inicioy += 3

            elif self.direcao == ESQUERDA:
                if self.iniciox - self.tamanho_sprite < 0:
                    self.iniciox = 28
                else:
                    self.iniciox -= 3
            elif self.direcao == DIREITA:
                if self.iniciox + self.tamanho_sprite > pyxel.width - self.tamanho_sprite:
                    self.iniciox = 154
                else:
                    self.iniciox += 3
            
        #colisao carros
        self.colidiu = self.detectar_colisao(self.x + 5, self.y, self.largura, self.largura, self.iniciox, self.inicioy, self.largura, self.altura) or self.detectar_colisao(self.x + 65, self.y2, self.largura, self.largura, self.iniciox, self.inicioy, self.largura,self.altura) or self.detectar_colisao(self.x + 119, self.y3, self.largura, self.largura, self.iniciox, self.inicioy, self.largura,self.altura)


        #repetição
        if self.y >= 250:
            self.y =  randint(-200, 0)
        if self.y2 >= 250:
            self.y2 = randint(-350, 0)
        if self.y3 >= 250:
            self.y3 = randint(-350, 0)

        #aceleração outros
        self.y += 2
        self.y2 += 3
        self.y3 += 3    
        
        #colisão outros
        if self.colidiu:
            self.iniciox = 100
            self.inicioy = 184
            self.colisao += 1
        

    def draw(self):
        pyxel.load("assets/data.pyxres")
        pyxel.cls(13)
        pyxel.rect(0, 0, 30, 200, 11)
        pyxel.rect(170, 0, 30, 200, 11)
        pyxel.rect(66, 0, 5, 18, 10)
        pyxel.rect(66, 36, 5, 18, 10)
        pyxel.rect(66, 72, 5, 18, 10)
        pyxel.rect(66, 108, 5, 18, 10)
        pyxel.rect(66, 144, 5, 18, 10)
        pyxel.rect(66, 180, 5, 18, 10)
        pyxel.rect(126, 0, 5, 18, 10)
        pyxel.rect(126, 36, 5, 18, 10)
        pyxel.rect(126, 72, 5, 18, 10)
        pyxel.rect(126, 108, 5, 18, 10)
        pyxel.rect(126, 144, 5, 18, 10)
        pyxel.rect(126, 180, 5, 18, 10)
        pyxel.blt(self.iniciox, self.inicioy, 0, 16, 0, 16, 16, 0)
        pyxel.blt(self.x + 65, self.y2, 0, 0, 0, 16, 16, 0)
        pyxel.blt(self.x + 5, self.y, 0, 32, 0, 16,16, 0)
        pyxel.blt(self.x + 119, self.y3, 0, 48, 0, 16, 16, 0)
        pyxel.blt(100, 10, 0, 32, 16, 16, 16, 13)
        pyxel.blt(75, 10, 0, 48, 16, 16, 16, 0)
        pyxel.blt(5, 0, 0, 16, 16, 16, 16, 0)
        pyxel.blt(5, 20, 0, 16, 16, 16, 16, 0)
        pyxel.blt(5, 40, 0, 0, 16, 16, 16, 0)
        pyxel.blt(5, 60, 0, 16, 16, 16, 16, 0)
        pyxel.blt(5, 80, 0, 0, 16, 16, 16, 0)
        pyxel.blt(5, 100, 0, 16, 16, 16, 16, 0)
        pyxel.blt(5, 120, 0, 0, 16, 16, 16, 0)
        pyxel.blt(5, 140, 0, 16, 16, 16, 16, 0)
        pyxel.blt(180, 0, 0, 16, 16, 16, 16, 0)
        pyxel.blt(180, 20, 0, 16, 16, 16, 16, 0)
        pyxel.blt(180, 40, 0, 0, 16, 16, 16, 0)
        pyxel.blt(180, 60, 0, 16, 16, 16, 16, 0)
        pyxel.blt(180, 80, 0, 0, 16, 16, 16, 0)
        pyxel.blt(180, 100, 0, 16, 16, 16, 16, 0)
        pyxel.blt(180, 120, 0, 0, 16, 16, 16, 0)
        pyxel.blt(180, 140, 0, 16, 16, 16, 16, 0)
        pyxel.blt(180, 160, 0, 0, 16, 16, 16, 0)
        pyxel.blt(180, 180, 0, 16, 16, 16, 16, 0)
        pyxel.blt(180, 200, 0, 0, 16, 16, 16, 0)
        
        pyxel.text(80,2,"Collision", pyxel.frame_count % 16)
        pyxel.text(8,160, "UPE", 8)
        pyxel.text(2,170, "Gabriel", 8)
        pyxel.text(2,180, "   &", 8)
        pyxel.text(2,190, " Igor", 8)
        
        self.cor = 15
        
        if self.colisao >= 1:
            pyxel.cls(2)
            pyxel.text(70, 40, "  GAME OVER", pyxel.frame_count % 16)
            pyxel.text(70, 60, "   PRESS Q", 0)
            pyxel.text(70, 80, "   TO QUIT", 0)
            pyxel.text(70, 100, "    OR R", 0)
            pyxel.text(70, 120, "  TO RESTART", 0)
            if pyxel.btn(pyxel.KEY_Q):
                pyxel.quit()
            if pyxel.btn(pyxel.KEY_R) or pyxel.btn(pyxel.KEY_ENTER):
                self.colisao -= 1
                self.iniciox = 100
                self.inicioy = 188
                self.x = 30
                self.y = 0
                self.y2 = 0
                self.y3 = 0
                self.direcao = 4
        
        if self.start == 0:
            self.iniciox += 200
            self.inicioy += 200
            pyxel.cls(8)
            pyxel.text(85, 40, "COLLISION", pyxel.frame_count % 16)
            pyxel.blt(68, 35, 0, 0, 16, 16, 16, 0)
            pyxel.text(62, 60, "PRESS        TO PLAY", 7)
            pyxel.text(88, 60, "ENTER", pyxel.frame_count % 8)
            pyxel.text(62, 70, "HOLD     TO CREDITS", 7)
            pyxel.text(88, 70, "C", pyxel.frame_count % 8)
            pyxel.text(62, 80, "PRESS    TO QUIT", 7)
            pyxel.text(88, 80, "Q", pyxel.frame_count % 8)
            pyxel.blt(80, 160, 0, 0, 32, 16, 16, 0)
            pyxel.blt(90, 160, 0, 16, 32, 16, 16, 0)
            pyxel.blt(100, 160, 0, 32, 32, 16, 16, 0)
            if pyxel.btn(pyxel.KEY_ENTER):
                self.start = 1
                self.iniciox = 100
                self.inicioy = 188
                self.x = 30
                self.y = 0
                self.y2 = 0
                self.y3 = 0
                self.direcao = 4

            if pyxel.btn(pyxel.KEY_C):
                pyxel.cls(8)
                pyxel.text(85, 40, "COLLISION", pyxel.frame_count % 16)
                pyxel.blt(68, 35, 0, 0, 16, 16, 16, 0)
                pyxel.text(50, 60,"Projeto de PROGRAMACAO I", 7)
                pyxel.text(75, 70,"Criado por:", 7)
                pyxel.text(60, 90,"Gabriel Rodrigues", 7)
                pyxel.text(70, 100,"Igor Leonardo", 7)
                pyxel.blt(80, 160, 0, 0, 32, 16, 16, 0)
                pyxel.blt(90, 160, 0, 16, 32, 16, 16, 0)
                pyxel.blt(100, 160, 0, 32, 32, 16, 16, 0)
                if pyxel.btn(pyxel.KEY_ENTER):
                    self.start = 1
                    self.iniciox = 100
                    self.inicioy = 188
                    self.x = 30
                    self.y = 0
                    self.y2 = 0
                    self.y3 = 0
                    self.direcao = 4

    def detectar_colisao(self, x1, y1, l1, a1, x2, y2, l2, a2):
        if x1 < x2 + l2 and x1 + l1 > x2 and y1 < y2 + a2 and y1 + a1 > y2:
            return True
        else:
            return False
CarGame()