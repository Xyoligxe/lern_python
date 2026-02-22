#Phase où on entre les noms des joueurs et leur pv respectif

player1 = input('Entrez le nom du 1er joueur :').capitalize() #on ecrit le nom du 1er joueur.
heal1 = int(input('Et son nombre de PV :')) #pv du joueur 1 en nombre entier narutel
player2 = input('Entrez le nom du 2ème joueur :').capitalize() #nom du joueur 2
heal2 = int(input('Et son nombre de pv :')) #pv du joueur 2 en entier naturel

msg = player1 + ' ( ' + str(heal1) + 'PV ) affronte ' + player2 + ' ( ' + str(heal2) + ' PV )' #stocker dans une variable ce que l'on veux afficher plus tard

print('+' * (len(msg) + 4 )) # utiliser le nombre maximal de de ce que l'on veux afficher pour generer le nombre de + adquat
print('+', msg, '+') #meme principe qu'avant
print('+' * (len(msg) + 4 ))

#phase où on demande a l'utilisateur l'attaque qu'il veut utiliser
print(player1, 'quelle attaque voulez-vous utiliser ?')
charge = 20
Tonnerre = 50
print('1. Charge (-20 PV)')
print('2. Tonnerre (-50 PV)')
choix_attack = input(' :')
if choix_attack == 'charge' or choix_attack == '1' :
    print(player1 + ' attaque ' + player2 + 'qui perd ' + str(heal2 - charge) + ' PV')
if choix_attack == 'Tonnerre' or choix_attack == '2' :
     print(player1 + ' attaque ' + player2 + 'qui perd ' + str(heal2 - Tonnerre) + ' PV')

print(player2, 'quelle attaque voulez-vous utiliser ?')
print('1. Charge (-20 PV)')
print('2. Tonnerre (-50 PV)')
choix_attack2 = input(' :')
if choix_attack2 == 'charge' or choix_attack == '1' :
    print(player2 + ' attaque ' + player1 + 'qui perd ' + str(heal1 - charge) + ' PV')
if choix_attack2 == 'Tonnerre' or choix_attack == '2' :
     print(player2 + ' attaque ' + player1 + 'qui perd ' + str(heal1 - Tonnerre) + ' PV')
print(heal1, heal2)
#Phase où on entre les nombres de dégats souhaiter a être infliger

#Joueur 1 attaque
phrase1 = player1 + ' combien de dégats infligez-vous à ' + player2 + ' ? ' #phrase a utiliser dans input, il peut prendre qu'une seule argument voila le pourquoi.
attack1 = int(input(phrase1)) 
pv_after_attack1 = heal2 - attack1 #le pv restent après l'attack

msg1_for_player1 = player1 + ' attaque ' + player2 + ' qui perd ' + str(attack1) + ' PV' #le truc a afficher dans print, c'est a cause des +
msg2_for_player1 = player2 + ' a maintenant ' + str(pv_after_attack1) + 'PV' #la phrase a afficher avant le calcul du len, lenmax - len du msg_for_player1
msg2_for_player1_print = msg2_for_player1 + ' ' * (len(msg1_for_player1) - len(msg2_for_player1)) #message a affichier a cause des decos de +

print('+' * (len(msg1_for_player1) + 4))
print('+' ,msg1_for_player1, '+' )
print('+', msg2_for_player1_print, '+')
print('+' * (len(msg1_for_player1) + 4))

#joueur 2 attaque
phrase2 = player2 + ' combien de dégats infligez-vous à ' + player1 + ' ? ' #phrase a utiliser dans input, il peut prendre qu'une seule argument voila le pourquoi.
attack2 = int(input(phrase2)) 
pv_after_attack2 = heal1 - attack2 #le pv restent après l'attack

msg1_for_player2 = player2 + ' attaque ' + player1 + ' qui perd ' + str(attack2) + ' PV' #le truc a afficher dans print, c'est a cause des +
msg2_for_player2 = player1 + ' a maintenant ' + str(pv_after_attack2) + 'PV' #la phrase a afficher avant le calcul du len, lenmax - len du msg_for_player2
msg2_for_player2_print = msg2_for_player2 + ' ' * (len(msg1_for_player2) - len(msg2_for_player2)) #message a affichier a cause des decos de +

print('+' * (len(msg1_for_player2) + 4))
print('+' ,msg1_for_player2, '+' )
print('+', msg2_for_player2_print, '+')
print('+' * (len(msg1_for_player2) + 4))

#resultat du combat
resultat1 = player1 + ' a ' + str(pv_after_attack2) + ' PV'
resultat2 = player2 + ' a ' + str(pv_after_attack1) + ' PV'
annoncement = 'Résultat du combat :'

resultat_print1 = resultat1 + ' ' * (len(annoncement) - len(resultat1))
resultat_print2 = resultat2 + ' ' * (len(annoncement) - len(resultat2))

print('+' * (len(annoncement) + 4))
print('+', annoncement, '+')
print('+', resultat_print1, '+')
print('+', resultat_print2, '+')
print('+' * (len(annoncement) + 4))