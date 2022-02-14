T = int(input("Cik litru ūdens ir akvārijā? "))
V = int(input("Cik litru ūdens vajag 1 zivtiņai? "))
Z = int(input("Cik zivtinu ir akvārijā? "))

N = int(T / V)

print("Jāpārceļ " , int(Z - N) , "zivtiņas.")