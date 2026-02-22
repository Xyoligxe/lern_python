# moment the player enter the name and pv
player1 = input('Entrez le nom du 1er joueur :').capitalize() # name for player 1.
heal1 = int(input('Et son nombre de PV :')) # heal for player 1
player2 = input('Entrez le nom du 2ème joueur :').capitalize() # name for second player
heal2 = int(input('Et son nombre de pv :')) # with your pv
msg = player1 + ' ( ' + str(heal1) + 'PV ) affronte ' + player2 + ' ( ' + str(heal2) + ' PV )'
# variable using after

print('+' * (len(msg) + 4 )) # generation + using len of msg
print('+', msg, '+') # show the msg contante
print('+' * (len(msg) + 4 ))

# moment or user can using one attack
# it's for player 1 and 2
charge = 20
tonnerre = 50

print(player1, 'quelle attaque voulez-vous utiliser ?')
print('1. Charge (-20 PV)')
print('2. Tonnerre (-50 PV)')

choix_attack = input('>')
if choix_attack == 'charge' or choix_attack == '1' :
    print(player1 + ' attaque ' + player2 + ' qui perd ' + str(charge) + ' PV')
    heal2 = heal2 - charge
if choix_attack == 'Tonnerre' or choix_attack == '2' :
    print(player1 + ' attaque ' + player2 + ' qui perd ' + str(tonnerre) + ' PV')
    heal2 = heal2 - tonnerre

print(player2, 'quelle attaque voulez-vous utiliser ?')
print('1. Charge (-20 PV)')
print('2. Tonnerre (-50 PV)')

choix_attack2 = input('>')

if choix_attack2 == 'charge' or choix_attack == '1' :
    print(player2 + ' attaque ' + player1 + ' qui perd ' + str(charge) + ' PV')
    heal1 = heal1 - charge
if choix_attack2 == 'Tonnerre' or choix_attack == '2' :
    print(player2 + ' attaque ' + player1 + ' qui perd ' + str(tonnerre) + ' PV')
    heal1 = heal1 - tonnerre
if heal1 > heal2 :
    print(player1, ' remporte le combat')
if heal2 > heal1 :
    print(player2, ' remporte le combat')

#result fight
resultat1 = player1 + ' a ' + str(heal1) + ' PV'
resultat2 = player2 + ' a ' + str(heal2) + ' PV'
show = 'Résultat du combat :'
resultat_print1 = resultat1 + ' ' * (len(show) - len(resultat1))
resultat_print2 = resultat2 + ' ' * (len(show) - len(resultat2))

print('+' * (len(show) + 4))
print('+', show, '+')
print('+', resultat_print1, '+')
print('+', resultat_print2, '+')
print('+' * (len(show) + 4))