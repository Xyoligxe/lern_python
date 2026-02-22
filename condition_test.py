#teste de condition a l'entrer d'un mot de passe
texte2 = 'Des trucs a eviter, ecrire : Utilisateur dans la section où il faut entrer son nom d\'utilisateur'
texte1 = 'ce programme a pour but de tester si vous souvenez de votre mot de passe' 
texte3 = 'Ecrire Mot de passe dans la section de mot de passe.' 
texte4 = "Pour relancer, ecrire 'py con' puis tab sur le clavier" 
print('+' * (len(texte2) + 4))
print('+' + texte1 + ' ' *((len(texte2) - len(texte1)) + 2) + '+')
print('+', texte2, '+')
print('+' + texte3 + ' ' *((len(texte2) - len(texte3)) + 2) + '+')
print('+' + texte4 + ' ' *((len(texte2) - len(texte4)) + 2) + '+')
print('+' * (len(texte2) + 4))

user = input('Entrer le nom de l\'utilisateur :')
password = input('Entrer votre nom de passe :')

if user == '' :
    print('Entrer un nom d\'utilisateur valide')
    print('Relancer le programme')

if user == 'Utilisateur' :
    print('te fou pas de ma geule connard !')
    print('relance')

elif user ==  user :
    print('Utilsateur :', user)

    if password == 'Mot de passe' :
        print('Con ! relence c\'est pas valide imbecile')


    if password == password and password != 'Mot de passe':
        print('Votre mot de passe est ', password)
        choix_password = input('Oui pour confirmé et Non pour non :')

        if choix_password == 'Oui' :
            print('Utilisateur :', user)
            print('Mot de passe :', password)
            validification = input('Entrer à nouveau votre mot de passe :')

            if validification == password :
                print('Bravo, vous vous souvenez de votre mot de passe')
                print(password)

            else :
                print('je vais pas de mentir, t\'as un problème de mémoire !')

        else :
            print('Utilisateur :', user)
            print('Pas foutu d\'enter un mot de passe correcte')









