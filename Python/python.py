# [Sintaxe básica] Definindo uma classe chamada Pessoa
class Pessoa:
    def __init__(self, nome, idade):
        # 'self' representa o próprio objeto
        self.nome = nome
        self.idade = idade

    def __str__(self):
        # Retorna uma representação em texto do objeto
        return f"{self.nome} tem {self.idade} anos." #concatenação de strings

# [Estrutura de dados] Lista para armazenar objetos Pessoa
pessoas = []

# [Função] Cadastra uma nova pessoa
def cadastrar():
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    nova_pessoa = Pessoa(nome, idade) # [Instanciação] Cria um novo objeto Pessoa
    pessoas.append(nova_pessoa)
    print("✅ Pessoa cadastrada com sucesso!\n")

# [Função] Lista todas as pessoas cadastradas
def listar():
    if not pessoas:  # [Estrutura de controle] Condicional
        print("⚠️ Nenhuma pessoa cadastrada.\n")
    else:
        print("📋 Pessoas cadastradas:")
        for p in pessoas:  # [Loop] Percorre a lista
            print("-", p)
        print()

        
# [Função] Busca pessoas pelo nome
def buscar():
    termo = input("Digite o nome para buscar: ")
    resultados = [p for p in pessoas if termo.lower() in p.nome.lower()]
    if resultados:
        print("🔍 Resultados encontrados:")
        for p in resultados:
            print("-", p)
    else:
        print("❌ Nenhum resultado encontrado.")
    print()

# [Função principal] Menu com opções
def menu():
    while True:  # [Loop] Executa até que o usuário escolha sair
        print("=== Menu ===")
        print("1. Cadastrar pessoa")
        print("2. Listar pessoas")
        print("3. Buscar pessoa")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        # [Estrutura de controle] if/elif/else como um 'switch'
        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            buscar()
        elif opcao == "4":
            print("👋 Saindo do sistema.")
            break
        else:
            print("❗ Opção inválida. Tente novamente.\n")

# [Chamada da função principal]
menu()

# match opcao:
#     case "1":
#         cadastrar_usuario()
#     case "2":
#         listar_usuarios()
#     case "3":
#         buscar_usuario()
#     case "4":
#         print("👋 Encerrando o sistema.")
#     case _:
#         print("❗ Opção inválida. Tente novamente.\n")

