import negyedik
def hatodikFeladat():
    szam1 = negyedik.beolvas()
    szam2 = negyedik.beolvas()

    print(str(szam1)+"+"+str(szam2)+"="+str(szam1+szam2))
    print(str(szam1)+"-"+str(szam2)+"="+str(szam1-szam2))
    print(str(szam1) + "*" + str(szam2) + "=" + str(szam1 * szam2))
    print(str(szam1) + "/" + str(szam2) + "=" + str(szam1 / szam2))
    print(str(szam1) + "mod" + str(szam2) + "=" + str(szam1 % szam2))
    print(str(szam1) + "^" + str(szam2) + "=" + str(szam1 ** szam2))
    print(str(szam2) + "^" + str(szam1) + "=" + str(szam2 ** szam1))