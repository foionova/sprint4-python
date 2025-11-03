import json

# ---------------- ARQUIVOS PARA PERSISTÊNCIA ----------------

ARQ_USUARIOS = "usuarios.json"
ARQ_TIMES_PERSONALIZADOS = "times_personalizados.json"


# ---------------- DADOS FIXOS EM MEMÓRIA ----------------
# (não precisam ser salvos em arquivo, já fazem parte do "jogo")

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

# ---------------- LISTAS EM MEMÓRIA ----------------

usuarios = []             
times_personalizados = [] 


# ---------------- FUNÇÕES DE PERSISTENCIA ----------------

def carregar_usuarios():

    try:
        with open(ARQ_USUARIOS, "r", encoding="utf-8") as f:
            lista = json.load(f)
            return lista
    except FileNotFoundError:
        # usuários padrão para o sistema
        lista = [
            {'nome': 'danilo', 'senha': '1234'},
            {'nome': 'passabola', 'senha': 'fiap'}
        ]
        return lista
    except json.JSONDecodeError:
        print("⚠ Erro ao ler arquivo de usuários. Iniciando lista vazia.")
        return []


def salvar_usuarios(lista):

    try:
        with open(ARQ_USUARIOS, "w", encoding="utf-8") as f:
            json.dump(lista, f, ensure_ascii=False, indent=4)
    except Exception as erro:
        print("Erro ao salvar usuários:", erro)


def carregar_times_personalizados():

    try:
        with open(ARQ_TIMES_PERSONALIZADOS, "r", encoding="utf-8") as f:
            lista = json.load(f)
            return lista
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("⚠ Erro ao ler arquivo de times personalizados. Iniciando lista vazia.")
        return []


def salvar_times_personalizados(lista):

    try:
        with open(ARQ_TIMES_PERSONALIZADOS, "w", encoding="utf-8") as f:
            json.dump(lista, f, ensure_ascii=False, indent=4)
    except Exception as erro:
        print("Erro ao salvar times personalizados:", erro)


def carregar_dados_iniciais():

    global usuarios, times_personalizados
    usuarios = carregar_usuarios()
    times_personalizados = carregar_times_personalizados()


# ---------------- FUNÇÕES BASE ----------------

def verifica_numero(mensagem):
    while True:
        num_str = input(mensagem)
        try:
            num_int = int(num_str)
            return num_int
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros!")


def pausa():
    input("\nPressione ENTER para continuar... ")


def tela_cadastro():
    print("\n--- Cadastro / Sign up ---")
    usuario = input("Diga o nome de usuário (username): ")
    senha = input("Diga a senha (password): ")

    usuario_existe = False
    for u in usuarios:
        if u['nome'] == usuario:
            usuario_existe = True
            break

    if usuario_existe:
        print("Usuário já existe. Tente outro nome!")
    else:
        novo_usuario = {'nome': usuario, 'senha': senha}
        usuarios.append(novo_usuario)
        salvar_usuarios(usuarios)
        print("Cadastro realizado com sucesso! / Sign up completed!")


def tela_login():
    print("\n--- Login ---")
    usuario = input("Diga seu usuário: ")
    senha = input("Diga sua senha: ")

    login_sucesso = False
    for u in usuarios:
        if u['nome'] == usuario and u['senha'] == senha:
            login_sucesso = True
            break

    if login_sucesso:
        print("Acesso liberado! / Access granted!")
        return True
    else:
        print("Usuário ou senha incorretos.")
        return False


# ---------------- FUNÇÕES PARA TIMES PERSONALIZADOS (CRUD) ----------------

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
    pausa()


def criar_time():

    nome_time = input("\nDigite o nome do seu time: ")

    for time in times_personalizados:
        if time['nome'].lower() == nome_time.lower():
            print(f"\nO time '{nome_time}' já existe!")
            exibir_elenco(time['nome'], time['elenco'])
            return

    elenco_novo = []
    while True:
        print("\n--- Cadastro de Jogadora ---")
        nome = input("Nome da jogadora: ")
        posicao = input("Posição (position): ")
        numero = verifica_numero("Número da camisa: ")

        elenco_novo.append({'nome': nome, 'posicao': posicao, 'numero': numero})

        mais = input("Deseja adicionar outra jogadora? (s/n): ")
        if mais not in ['s', 'S']:
            break

    times_personalizados.append({'nome': nome_time, 'elenco': elenco_novo})
    salvar_times_personalizados(times_personalizados)
    print(f"\nTime '{nome_time}' criado com sucesso!")
    exibir_elenco(nome_time, elenco_novo)


def listar_times_personalizados():
    if not times_personalizados:
        print("\nNenhum time personalizado cadastrado.")
        pausa()
        return

    print("\n--- TIMES PERSONALIZADOS ---")
    for i in range(len(times_personalizados)):
        print(f"{i + 1}. {times_personalizados[i]['nome']}")

    opc = verifica_numero("Escolha o time para ver o elenco: ")
    if 1 <= opc <= len(times_personalizados):
        time_escolhido = times_personalizados[opc - 1]
        exibir_elenco(time_escolhido['nome'], time_escolhido['elenco'])
    else:
        print("Opção inválida!")
        pausa()


def escolher_indice_time():
    if not times_personalizados:
        print("\nNenhum time personalizado cadastrado.")
        pausa()
        return -1

    print("\n--- SELECIONAR TIME ---")
    for i in range(len(times_personalizados)):
        print(f"{i + 1}. {times_personalizados[i]['nome']}")

    opc = verifica_numero("Escolha o time: ")
    if 1 <= opc <= len(times_personalizados):
        return opc - 1
    else:
        print("Opção inválida!")
        pausa()
        return -1


def editar_time():
    indice = escolher_indice_time()
    if indice == -1:
        return

    time = times_personalizados[indice]
    print(f"\nEditando time: {time['nome']}")

    # parte pra alterar nome
    novo_nome = input(f"Novo nome do time (ENTER para manter '{time['nome']}'): ")
    if novo_nome.strip() != "":
        time['nome'] = novo_nome

    # parte pra mostrar elenco atual
    exibir_elenco(time['nome'], time['elenco'])

    # parte pra adicionar jogadora
    opc_add = input("Deseja adicionar jogadora? (s/n): ")
    if opc_add in ['s', 'S']:
        nome = input("Nome da jogadora: ")
        posicao = input("Posição: ")
        numero = verifica_numero("Número da camisa: ")
        time['elenco'].append({'nome': nome, 'posicao': posicao, 'numero': numero})
        print("Jogadora adicionada!")

    # parte pra remover jogadora
    if time['elenco']:
        opc_rem = input("Deseja remover alguma jogadora? (s/n): ")
        if opc_rem in ['s', 'S']:
            for i in range(len(time['elenco'])):
                j = time['elenco'][i]
                print(f"{i + 1}. {j['nome']} ({j['posicao']}) - {j['numero']}")
            rem = verifica_numero("Escolha o número da jogadora para remover: ")
            if 1 <= rem <= len(time['elenco']):
                removida = time['elenco'].pop(rem - 1)
                print(f"Jogadora {removida['nome']} removida!")
            else:
                print("Opção inválida!")

    salvar_times_personalizados(times_personalizados)
    print("\nTime atualizado com sucesso!")
    pausa()


def excluir_time():
    indice = escolher_indice_time()
    if indice == -1:
        return

    time = times_personalizados[indice]
    print(f"\nVocê escolheu excluir o time: {time['nome']}")
    confirma = input("Tem certeza? (s/n): ")
    if confirma in ['s', 'S']:
        times_personalizados.pop(indice)
        salvar_times_personalizados(times_personalizados)
        print("Time excluído com sucesso!")
    else:
        print("Operação cancelada.")

    pausa()


# ---------------- MENU ELENCOS ----------------

def menu_elencos():
    while True:
        print("\n--- MENU ELENCOS ---")
        print("1. Ver FC Vitória Regia (time fixo)")
        print("2. Criar seu time (Create)")
        print("3. Ver times personalizados (Read)")
        print("4. Editar time personalizado (Update)")
        print("5. Excluir time personalizado (Delete)")
        print("6. Voltar")

        escolha = verifica_numero("-> ")

        if escolha == 1:
            exibir_elenco("FC Vitória Regia", elenco_vitoria_regia)
        elif escolha == 2:
            criar_time()
        elif escolha == 3:
            listar_times_personalizados()
        elif escolha == 4:
            editar_time()
        elif escolha == 5:
            excluir_time()
        elif escolha == 6:
            break
        else:
            print("Opção inválida!")


# ---------------- MENUS PRINCIPAIS -------------

def exibir_classificacao():
    print("\n--- CLASSIFICAÇÃO DA COPA ---")
    print("=" * 40)
    print(f"{'Time':<20}{'P':<5}{'J':<5}{'V':<5}")
    print("-" * 40)

    for time, dados in dados_times.items():
        print(f"{time:<20}{dados['pontos']:<5}{dados['jogos']:<5}{dados['vitorias']:<5}")

    print("=" * 40)
    pausa()


def exibir_historico_jogadora():
    print("\n--- HISTÓRICO DE JOGADORA ---")
    nome = input("Diga o nome da jogadora (ex: Sofia Rossi): ")

    encontrada = False
    for j in jogadoras:
        if j['nome'].lower() == nome.lower():
            encontrada = True
            print(f"\nNome: {j['nome']} | Posição: {j['posicao']} | Time: {j['time']}")

            print("\nHistórico de Partidas:")
            for partida in j['historico']:
                print(
                    f"- Adversário: {partida['adversario']} | Gols: {partida['gols']} | Assistências: {partida['assistencias']}"
                )

            print("\nPrêmios:")
            for premio in j['premios']:
                print(f"- {premio}")
            break

    if not encontrada:
        print("Jogadora não encontrada!")

    pausa()


def menu_principal():
    while True:
        print("\n\n=== MENU PRINCIPAL ===")
        print("1. Classificação de Times")
        print("2. Histórico de Jogadora")
        print("3. Elencos de Times (CRUD)")
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


# ---------------- INÍCIO DO SISTEMA ----------------

def main():
    carregar_dados_iniciais()

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
            print("Até logo! Goodbye!")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
