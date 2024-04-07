import calendar
from tabulate import tabulate

# Tworzenie kalendarza na rok 2024
cal = calendar.Calendar()

# Definicja zadań dla każdego dnia
zadania = {
    1: "Odkurz pokój",
    2: "Napisz wiersz",
    3: "Jedna strona książki",
    # Tutaj kontynuuj z pozostałymi zadaniami dla kolejnych dni
}

# Funkcja generująca kalendarz jako tabelę
def generuj_kalendarz_z_zadaniami(year, month):
    data = []
    for day in range(1, calendar.monthrange(year, month)[1] + 1):
        data.append([f"{year}-{month:02d}-{day:02d}", zadania.get(day, 'Brak zadania')])
    return tabulate(data, headers=["Data", "Zadanie"], tablefmt="grid")

# Wywołanie funkcji dla roku 2024 i miesiąca kwiecień (numer miesiąca 4)
print(generuj_kalendarz_z_zadaniami(2024, 4))
