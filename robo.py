class ponto:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return '<%s, %s>' % (self.x, self.y)

class Recompensa(ponto):
    
    def __init__(self,x,y,name):
        super(Recompensa,self).__init__(x,y)
        self.name = name
        
   
    def __repr__(self):
        return '<recompensa> %s' %str(self)

class Robo(ponto):
  
    
    def move_up(self):
        if self.y < 10:
            self.y = self.y +1
        else:
            print('movimento proibido')
    
    def move_down(self):
        if self.y > 0: 
            self.y = self.y -1
        else:
            print('movimento proibido')
        
    def move_left(self):
        if self.x > 0:
            self.x = self.x -1
        else:
            print('movimento proibido')
            
    
    def move_right(self):
        if self.x < 10:
            self.x = self.x +1
        else:
            print('movimento proibido')

    def check_reward(robo,recompensa):
        ok = False
        for rec in recompensa:
            if rec.x == robo.x and rec.y == robo.y:
                print('o robo achou a recompensa %s'%rec.name)
                ok = True
        return ok

import random
r1 = Recompensa(random.randint(0,10),random.randint(0,10),'moeda')
r2 = Recompensa(random.randint(0,10),random.randint(0,10),'gasolina')
r3 = Recompensa(random.randint(0,10),random.randint(0,10),'arma')
recs = [r1,r2,r3]

robo = Robo(random.randint(0,10),random.randint(0,10))

for i in range(10):
    movimento = input('Digite up, down, left ou right para o movimento')
    if movimento == 'up':
        robo.move_up()
    elif movimento == 'down':
        robo.move_down()
    elif movimento == 'left':
        robo.move_left()
    elif movimento == 'right':
        robo.move_right()
    else:
        print('movimento invalido')
        continue
    print(robo)
    check_reward(robo,recs)

recs
