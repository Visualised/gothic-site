def print_menu():
    menu = """0 - help (wyświetla się ta pomoc)
1 - wylistowanie wszystkich nazw mieczy
2 - pokazanie szczegółów danego miecza wg indeksu
3 - wyłącz program"""
    print(menu)

def print_sword_list(sword_list):
    for index, sword in enumerate(sword_list):
        print(f'{index} - {sword["name"]}')

def print_sword_details(sword_list, sword_index):
    sword = sword_list[sword_index]
    print(f'{sword["name"]}, ' 
        + f'Obrażenia: {sword["damage"]}, '
        + f'Wymagana siła: {sword["required_strength"]}')


sword_list = [
    {
    "name": "Zardzewiały miecz", 
    "damage": 10, 
    "required_strength": 5,
    },
    {
    "name": "Miecz Świstaka", 
    "damage": 20, 
    "required_strength": 15,
    },
    {
    "name": "Miecz strachu", 
    "damage": 42, 
    "required_strength": 18,
    },
    {
    "name": "Miecz śmierci", 
    "damage": 48, 
    "required_strength": 21,
    },
    {
    "name": "Miecz Blizny", 
    "damage": 85, 
    "required_strength": 70,
    },
]

print_menu()
while True:
    try:
        user_selection = int(input("Wybierz opcje: "))
    except ValueError:
        print("Niepoprawna opcja, wybierz opcję ponownie.")
        continue

    if user_selection == 0:
        print_menu()
    elif user_selection == 1:
        print_sword_list(sword_list)
    elif user_selection == 2:
        sword_index = int(input("Wpisz indeks miecza: "))
        print_sword_details(sword_list, sword_index)
    elif user_selection == 3:
        break