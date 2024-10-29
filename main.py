# print("---1.1---")
# file = open("data2")
# print(file.read())
#
# with open ("data2") as file:
#     print(file.read())
#
# with open("data2") as file:
#     print(file.readline())
#
# print("---1.2---")
#
# with open("temp/data.txt", "w") as file:
#     file.write("pirma\n")
#     file.write("pirma\n")
#
# with open("temp/data.txt", "a") as file:
#     file.write("pirma\n")
#     file.write("antra\n")
from os.path import split

# print("---1.3---")
# with open ("Automobiliai") as file:
#     cars = file.read().splitlines()
#     suma = 0
#     kiekis = 0
#     for car in cars:
#         print(int(car.split(",")[2]))
#         suma +=int(car.split(",")[2])
#         kiekis += 1
# vidurkis = suma / kiekis
# print("pagaminimo metų vidurkis:", vidurkis)
#
# with open("isvesta info.txt", "a") as file:
#     file.write(str(vidurkis))
#     file.write(f' visi automobiliai vidutiniškai yra pagaminti {vidurkis} metais')

# print("---1.4---")
# from csv import reader
# with open('studentai.csv', encoding='windows-1257') as failas:
#     csv_reader = reader(failas, delimiter=";")
#     # for eilute in csv_reader:
#     #     print(eilute)
#     pažymių_suma = 0
#     studentų_kiekis = 0
#     next(csv_reader)
#     for matematika in csv_reader:
#         print(matematika)
#         print(int(matematika[2]))
#         pažymių_suma +=int(matematika[2])
#         studentų_kiekis += 1
# vidurkis = pažymių_suma / studentų_kiekis
# print("Matematikos balų vidurkis:", vidurkis)
#
# from csv import DictReader
# with open('studentai.csv', encoding='windows-1257') as file:
#     csv_reader = DictReader(file, delimiter=";")
#     for row in csv_reader:
#         # print(row)
#         print(f"Studentas(-e) {row['Vardas']} {row['Pavardė']} yra iš {row['Miestas']}")
