usuarios_nomes = ['danilo', 'passabola']
usuarios_senhas = ['1234', 'fiap']

dados_times = {
    'FC Sol Nascente': {'pontos': 12, 'jogos': 5, 'vitorias': 4},
    'FC Fenix': {'pontos': 10, 'jogos': 5, 'vitorias': 3},
    'FC Novo Horizonte': {'pontos': 7, 'jogos': 5, 'vitorias': 2},
    'FC Estrela Candente': {'pontos': 1, 'jogos': 5, 'vitorias': 0}
}

jogadoras = [
    {
        'nome': 'Sofia Rossi',
        'time': 'FC Sol Nascente',
        'posicao': 'Atacante',
        'historico': [
            {'adversario': 'FC Fenix', 'gols': 3, 'assistencias': 1},
            {'adversario': 'FC Esperança Viva', 'gols': 2, 'assistencias': 0}
        ],
        'premios': ['Artilheira 2024', 'Melhor Atacante 2023']
    },
    {
        'nome': 'Isabela Silva',
        'time': 'FC Fenix',
        'posicao': 'Meio-Campo',
        'historico': [
            {'adversario': 'FC Vitória Regia', 'gols': 2, 'assistencias': 3},
            {'adversario': 'FC União das Forças', 'gols': 1, 'assistencias': 2}
        ],
        'premios': ['Melhor Meio-Campo 2024']
    }
]

# --- ELENCO FIXO DO FC VITÓRIA REGIA ---
elenco_vitoria_regia = [
    {'nome': 'Elena Ramirez', 'posicao': 'Atacante', 'numero': 9},
    {'nome': 'Sofia Zhang', 'posicao': 'Meio Campo', 'numero': 10},
    {'nome': 'Isabella Rossi', 'posicao': 'Zagueira', 'numero': 3},
    {'nome': 'Ava Carter', 'posicao': 'Goleira', 'numero': 1},
    {'nome': 'Emily Silva', 'posicao': 'Atacante', 'numero': 7},
    {'nome': 'Chloe Park', 'posicao': 'Meio Campo', 'numero': 8},
    {'nome': 'Mia Dubois', 'posicao': 'Zagueira', 'numero': 2},
    {'nome': 'Madison Clark', 'posicao': 'Atacante', 'numero': 11},
    {'nome': 'Abigail Gonzalez', 'posicao': 'Meio Campo', 'numero': 6},
    {'nome': 'Ella Bennett', 'posicao': 'Defensora', 'numero': 4},
]

# --- LISTA DE TIMES CRIADOS PELO USUÁRIO ---
times_personalizados = []


# --- FUNÇÕES BASE ---

def verifica_numero(mensagem):
    num_str = input(mensagem)
    while not num_str.isnumeric():
        print("Entrada inválida. Digite apenas números!")
        num_str = input(mensagem)
    return int(num_str)


def tela_cadastro():
    print("\n--- Cadastro ---")
    usuario = input("Diga o nome de usuário: ")
    senha = input("Diga a senha: ")

    usuario_existe = False
    for nome_cadastrado in usuarios_nomes:
        if nome_cadastrado == usuario:
            usuario_existe = True
            break

    if usuario_existe:
        print("Usuário já existe. Tente outro nome!")
    else:
        usuarios_nomes.append(usuario)
        usuarios_senhas.append(senha)
        print("Cadastro realizado com sucesso!")


def tela_login():
    print("\n--- Login ---")
    usuario = input("Diga seu usuário: ")
    senha = input("Diga sua senha: ")

    login_sucesso = False
    for i in range(len(usuarios_nomes)):
        if usuarios_nomes[i] == usuario and usuarios_senhas[i] == senha:
            login_sucesso = True
            break

    if login_sucesso:
        print("Acesso liberado!")
        return True
    else:
        print("Usuário ou senha incorretos.")
        return False


# --- MENU ELENCOS ---

def menu_elencos():
    while True:
        print("\n--- MENU ELENCOS ---")
        print("1. Ver FC Vitória Regia")
        print("2. Criar seu time")
        print("3. Ver times personalizados")
        print("4. Voltar")

        escolha = verifica_numero("-> ")

        if escolha == 1:
            exibir_elenco("FC Vitória Regia", elenco_vitoria_regia)
        elif escolha == 2:
            criar_time()
        elif escolha == 3:
            if times_personalizados:
                i = 1
                for t in times_personalizados:
                    print(f"{i}. {t['nome']}")
                    i += 1
                opc = verifica_numero("Escolha o time: ")
                if 1 <= opc <= len(times_personalizados):
                    exibir_elenco(times_personalizados[opc-1]['nome'], times_personalizados[opc-1]['elenco'])
                else:
                    print("Opção inválida!")
            else:
                print("Nenhum time cadastrado.")
        elif escolha == 4:
            break
        else:
            print("Opção inválida!")


def exibir_elenco(nome_time, elenco):
    print(f"\n--- ELENCO DO {nome_time.upper()} ---")
    print("=" * 50)
    print(f"{'Jogadora':<20}{'Posição':<15}{'Número':<5}")
    print("-" * 50)

    if elenco:
        for j in elenco:
            print(f"{j['nome']:<20}{j['posicao']:<15}{j['numero']:<5}")
    else:
        print("Nenhuma jogadora cadastrada ainda.")

    print("=" * 50)
    input("Pressione Enter para continuar...")


def criar_time():
    nome_time = input("\nDigite o nome do seu time: ")

    # Verificar se já existe um time com esse nome
    for time in times_personalizados:
        if time['nome'] == nome_time:
            print(f"\nO time '{nome_time}' já existe!")
            exibir_elenco(nome_time, time['elenco'])
            return

    elenco_novo = []
    while True:
        print("\n--- Cadastro de Jogadora ---")
        nome = input("Nome da jogadora: ")
        posicao = input("Posição: ")
        numero = verifica_numero("Número da camisa: ")

        elenco_novo.append({'nome': nome, 'posicao': posicao, 'numero': numero})

        mais = input("Deseja adicionar outra jogadora? (s/n): ")
        if mais not in ['s', 'S']:
            break

    times_personalizados.append({'nome': nome_time, 'elenco': elenco_novo})
    print(f"\nTime '{nome_time}' criado com sucesso!")

    exibir_elenco(nome_time, elenco_novo)


# --- MENU PRINCIPAL ---

def menu_principal():
    while True:
        print("\n\n=== MENU PRINCIPAL ===")
        print("1. Classificação de Times")
        print("2. Histórico de Jogadora")
        print("3. Elencos de Times")
        print("4. Sair da Conta")

        escolha = verifica_numero("\nQual opção você quer?\n-> ")

        if escolha == 1:
            exibir_classificacao()
        elif escolha == 2:
            exibir_historico_jogadora()
        elif escolha == 3:
            menu_elencos()
        elif escolha == 4:
            print("Saindo da conta...")
            break
        else:
            print("Opção inválida!")


def exibir_classificacao():
    print("\n--- CLASSIFICAÇÃO DA COPA ---")
    print("=" * 40)
    print(f"{'Time':<20}{'P':<5}{'J':<5}{'V':<5}")
    print("-" * 40)

    for time, dados in dados_times.items():
        print(f"{time:<20}{dados['pontos']:<5}{dados['jogos']:<5}{dados['vitorias']:<5}")
    print("=" * 40)
    input("Pressione Enter para continuar...")


def exibir_historico_jogadora():
    print("\n--- HISTÓRICO DE JOGADORA ---")
    nome = input("Diga o nome da jogadora (ex: Sofia Rossi): ")

    for jogadora in jogadoras:
        if jogadora['nome'] == nome:
            print(f"\nNome: {jogadora['nome']} | Posição: {jogadora['posicao']} | Time: {jogadora['time']}")

            print("\nHistórico de Partidas:")
            for partida in jogadora['historico']:
                print(
                    f"- Adversário: {partida['adversario']} | Gols: {partida['gols']} | Assistências: {partida['assistencias']}"
                )

            print("\nPrêmios:")
            for premio in jogadora['premios']:
                print(f"- {premio}")
            break
    else:
        print("Jogadora não encontrada!")

    input("\nPressione Enter para continuar...")


# --- INÍCIO DO SISTEMA ---

def main():
    while True:
        print("\n\n=== PASSA A BOLA ===")
        print("1. Login")
        print("2. Cadastro")
        print("3. Sair do Sistema")

        escolha = verifica_numero("\nO que você quer fazer?\n-> ")

        if escolha == 1:
            if tela_login():
                menu_principal()
        elif escolha == 2:
            tela_cadastro()
        elif escolha == 3:
            print("Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
