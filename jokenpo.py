from random import randint
from time import sleep
import emoji
r=0
cont=0
empate=0
while True:
    if cont==0:
        print('Vamos brincar de jokenpo!')
    if cont>=1:
        print('Vamos brincar de novo!')
    print(emoji.emojize('[1]=:hand:',use_aliases=True))
    print(emoji.emojize('[2]=:v:',use_aliases=True))
    print(emoji.emojize('[3]=:fist:',use_aliases=True))
    jogador=(int(input('Digite o que deseja jogar :')))
    pc=randint(1,3)
    print('JO',end='')
    sleep(0.5)
    print('KEN',end='')
    sleep(0.5)
    print('PO!')
    sleep(0.5)
    #papel :hand:
    #tesoura :v:
    #pedra :fist:
    if jogador==pc:
        print('Empate tente de novo!')
        empate+=1
    elif jogador==1 and pc==2:
        print(emoji.emojize('Você escolheu :hand: papel e o pc :v: tesoura.Você perdeu !',use_aliases=True))
        r=1
    elif jogador==1 and pc==3:
        print(emoji.emojize('Você escolheu :hand: papel e o pc :fist: pedra.Você ganhou!',use_aliases=True))
        cont=cont+1
    elif jogador==2 and pc==1:
        print(emoji.emojize('Você escolheu :v: tesoura e o pc :hand: papel.Você ganhou!',use_aliases=True))
        cont=cont+1
    elif jogador==2 and pc==3:
        print(emoji.emojize('Você escolheu :v: tesoura e o pc :fist: pedra.Você perdeu!',use_aliases=True))
        r=1
    elif jogador==3 and pc==1:
        print(emoji.emojize('Você escolheu :fist: pedra e o pc :hand: papel.Você perdeu!',use_aliases=True))
        r=1
    elif jogador==3 and pc==2:
        print(emoji.emojize('Você escolheu :fist: pedra e o pc :v: tesoura.Você ganhou!',use_aliases=True))
        cont=cont+1
    else:
        print('ERRO TENTE NOVAMENTE!')

    if r==1:
        break
print('-='*70)
print(f'você ganhou {cont} vezes e empatou {empate} ')
print('-='*70)