Skaitlis = int(input("Ievadi veselu skaitli: "))

Summa = 0
while (Skaitlis > 0):
  Cipars = Skaitlis % 10
  Skaitlis = int(Skaitlis / 10)
  Summa += Cipars

print("Rezultāts: " + str(Summa))

