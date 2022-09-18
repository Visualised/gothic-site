import os
os.system("cls")

def print_sword_list(sword_list):
    for index, item in enumerate(sword_list):
        print(f'{index} - {item["name"]}')

def print_sword_details(list_of_swords, sword_index):
    print(f'{list_of_swords[sword_index]["name"]}, ' 
        + f'Obrażenia: {list_of_swords[sword_index]["damage"]}, '
        + f'Wymagana siła: {list_of_swords[sword_index]["required_strength"]}')


sword_list = [
    {
    "name": "Zardzewiały miecz", 
    "damage": 10, 
    "required_strength": 5
    },

    {
    "name": "Miecz Świstaka", 
    "damage": 20, 
    "required_strength": 15
    },

    {
    "name": "Miecz strachu", 
    "damage": 42, 
    "required_strength": 18
    },

    {
    "name": "Miecz śmierci", 
    "damage": 48, 
    "required_strength": 21
    },

    {
    "name": "Miecz Blizny", 
    "damage": 85, 
    "required_strength": 70
    }
]

menu = """0 - help (wyświetla się ta pomoc)
1 - wylistowanie wszystkich nazw mieczy
2 - pokazanie szczegółów danego miecza wg indeksu
3 - wyłącz program"""

print(menu)
while True:
    user_selection = int(input("Wybierz opcje: "))
    if user_selection == 0:
        print(menu)
    elif user_selection == 1:
        print_sword_list(sword_list)
    elif user_selection == 2:
        sword_index = int(input("Wpisz indeks miecza: "))
        print_sword_details(sword_list, sword_index)
    elif user_selection == 3:
        break
    else:
        print("Niepoprawna opcja, wybierz opcję ponownie.")