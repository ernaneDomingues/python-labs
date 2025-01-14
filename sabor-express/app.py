import os

restaurants = []


def show_menu():
    print("Sabor Express\n")

    print("1 - Cadastrar Restaurante")
    print("2 - Listar Restaurantes")
    print("3 - Ativar Restaurante")
    print("4 - Sair")


def option_choice():
    try:
        option = int(input("\nEscolha uma das opções: "))

        match option:
            case 1:
                restaurant_register()
            case 2:
                show_restaurant()
            case 3:
                activate_restaurant()
            case 4:
                exit_app()
            case _:
                invalid_choice()
    except:
        invalid_choice()


def restaurant_register():
    os.system("cls")
    print("Bem-vindo ao cadastro de restaurante.")
    name_restaurant = input("\nDigite o nome do restaurante: ")
    category_restaurant = input("Digite a categoria do restaurante: ")
    restaurants.append({"Nome": name_restaurant, "Categoria": category_restaurant, 'Status': 'Inativo'})
    print('Cadastro realizado com sucesso!\n')
    input("Pressione qualquer tecla para retornar ao menu inicial.")
    main()

def show_restaurant():
    os.system("cls")
    print("Lista de restaurantes.\n")
    for restaurant in restaurants:
        print(f"Restaurante: {restaurant['Nome']}, Categoria: {restaurant['Categoria']}, Status: {restaurant['Status']}")
    input("\nPressione qualquer tecla para retornar ao menu inicial.")
    main()

def activate_restaurant():
    os.system('cls')
    print("Bem-vindo a ativaçáo de restaurante.")
    name_restaurant = input('\nDigite o nome do restaurante que deseja ativar: ')
    for restaurant in restaurants:
        if restaurant['Nome'] == name_restaurant:
            restaurant['Status'] = 'Ativo'
            print('Restaurante ativo com sucesso!')
    input("\nPressione qualquer tecla para retornar ao menu inicial.")
    main()

def invalid_choice():
    print("Opção inválida.")
    input("Pressione qualquer tecla para retornar ao menu inicial.")
    main()

def exit_app():
    os.system('cls')
    print("Saindo!")

def main():
    os.system("cls")
    show_menu()
    option_choice()


if __name__ == "__main__":
    main()
