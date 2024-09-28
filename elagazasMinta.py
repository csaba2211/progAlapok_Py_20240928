def elso():
    print('A program eldonti egy egesz szamrol, hogy pozitiv e')
    szam = int(input('Kerem adjon meg egy egesz szamot: '))
    if szam > 0:
        print('A szam pozitiv: ')

def masodik():
    print('A program kiirja a bekert szam megelozo es kovetkezo szamot')
    szam = int(input('Kerem adjon meg egy egesz szamot: '))
    if (szam >= -9) and (szam <= 9):
        megelozo=(szam - 1)
        rakovetkezo=(szam + 1)
        print('A rakovetkezo ertek: '+str(rakovetkezo),', a megleozo ertek: '+str(megelozo))

