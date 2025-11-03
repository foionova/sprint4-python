# ===============================================================
# PROJETO: Plataforma para Jogadoras e Olheiros
# ===============================================================

# -------------------- Funções de Entrada e Validação -------------------- #

def forca_opcao(msg, opcoes):
    opcoes_txt = '\n'.join(opcoes)
    escolha = input(f"{msg}\n{opcoes_txt}\n-> ").strip().lower()
    while escolha not in opcoes:
        print("❌ Opção inválida! Tente novamente.")
        escolha = input(f"{msg}\n{opcoes_txt}\n-> ").strip().lower()
    return escolha


def input_nome(msg):
    """Valida nome"""
    while True:
        nome = input(msg).strip()
        if nome.replace(" ", "").isalpha():
            return nome
        print("❌ Nome inválido! Apenas letras e espaços são permitidos.")


def input_idade(msg):
    """Valida idade"""
    while True:
        idade = input(msg).strip()
        if idade.isdigit() and int(idade) > 0:
            return idade
        print("❌ Idade inválida. Digite apenas números positivos.")


def input_posicao(msg):
    """Valida posição"""
    posicoes = ["goleira", "defensora", "meio-campista", "atacante"]
    return forca_opcao(msg, posicoes)


def input_texto(msg, campo):
    """Lê texto não vazio."""
    while True:
        texto = input(msg).strip()
        if texto:
            return texto
        print(f"❌ {campo} não pode ficar vazio.")


def input_link(msg):
    """Valida link HTTP ou HTTPS."""
    while True:
        link = input(msg).strip()
        if link.startswith("http://") or link.startswith("https://"):
            return link
        print("❌ Link inválido. Deve começar com http:// ou https://")


def input_senha(msg):
    """Valida"""
    while True:
        senha = input(msg).strip()
        if senha:
            return senha
        print("❌ Senha inválida. Não pode estar vazia.")


def input_nota(msg):
    """Valida nota"""
    while True:
        valor = input(msg).strip()
        try:
            nota = float(valor)
            if 0 <= nota <= 10:
                return nota
            print("❌ Nota deve ser entre 0 e 10.")
        except ValueError:
            print("❌ Digite apenas números.")


# -------------------- Funções Auxiliares -------------------- #

def printa_dic(dic, nivel=0):
    for chave, valor in dic.items():
        if isinstance(valor, dict):
            print(f"{'  '*nivel}{chave}:")
            printa_dic(valor, nivel + 1)
        else:
            print(f"{'  '*nivel}{chave}: {valor}")


def verificar_senha(jogadora):
    """Confere senha da jogadora antes de alterar ou excluir."""
    senha = input("Digite a senha da jogadora: ").strip()
    if senha == jogadora["senha"]:
        return True
    print("❌ Senha incorreta!")
    return False


# -------------------- CRUD Jogadoras -------------------- #

def cadastrar_jogadora(jogadoras):
    print("\n=== Cadastro de Jogadora ===")
    nome = input_nome("Nome da jogadora: ")
    idade = input_idade("Idade: ")
    posicao = input_posicao("Posição (goleira, defensora, meio-campista, atacante): ")
    time = input_texto("Time atual (ou 'Nenhum'): ", "Time")
    video = input_link("Link do vídeo de apresentação: ")
    senha = input_senha("Crie uma senha: ")

    jogadoras.append({
        "nome": nome,
        "idade": idade,
        "posicao": posicao,
        "time": time,
        "video": video,
        "senha": senha
    })
    print("✅ Jogadora cadastrada com sucesso!")


def listar_jogadoras(jogadoras):
    print("\n=== Lista de Jogadoras ===")
    if not jogadoras:
        print("Nenhuma jogadora cadastrada.")
        return
    for i, jogadora in enumerate(jogadoras, start=1):
        print(f"\n[{i}] {jogadora['nome']} ({jogadora['posicao']}) - {jogadora['time']}")
        print(f"Idade: {jogadora['idade']}")
        print(f"Vídeo: {jogadora['video']}")


def atualizar_jogadora(jogadoras):
    listar_jogadoras(jogadoras)
    if not jogadoras:
        return
    try:
        i = int(input("\nDigite o número da jogadora: ")) - 1
        if 0 <= i < len(jogadoras):
            jogadora = jogadoras[i]
            if verificar_senha(jogadora):
                print("\n--- Atualização ---")
                jogadora["nome"] = input_nome(f"Novo nome ({jogadora['nome']}): ") or jogadora["nome"]
                jogadora["idade"] = input_idade(f"Nova idade ({jogadora['idade']}): ") or jogadora["idade"]
                jogadora["posicao"] = input_posicao(f"Nova posição ({jogadora['posicao']}): ") or jogadora["posicao"]
                jogadora["time"] = input(f"Novo time ({jogadora['time']}): ") or jogadora["time"]
                jogadora["video"] = input_link(f"Novo vídeo ({jogadora['video']}): ") or jogadora["video"]
                print("✅ Jogadora atualizada com sucesso!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Digite um número válido.")


def excluir_jogadora(jogadoras):
    listar_jogadoras(jogadoras)
    if not jogadoras:
        return
    try:
        i = int(input("\nDigite o número da jogadora a excluir: ")) - 1
        if 0 <= i < len(jogadoras):
            jogadora = jogadoras[i]
            if verificar_senha(jogadora):
                nome = jogadora['nome']
                jogadoras.pop(i)
                print(f"✅ Jogadora '{nome}' excluída com sucesso!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Digite um número válido.")


# -------------------- CRUD Olheiros -------------------- #

def cadastrar_olheiro(olheiros):
    print("\n=== Cadastro de Olheiro ===")
    nome = input_nome("Nome do olheiro: ")
    contato = input_texto("Contato (email ou telefone): ", "Contato")
    olheiros.append({"nome": nome, "contato": contato})
    print("✅ Olheiro cadastrado com sucesso!")


def listar_olheiros(olheiros):
    print("\n=== Lista de Olheiros ===")
    if not olheiros:
        print("Nenhum olheiro cadastrado.")
        return
    for i, olheiro in enumerate(olheiros, start=1):
        print(f"[{i}] {olheiro['nome']} - Contato: {olheiro['contato']}")


def atualizar_olheiro(olheiros):
    listar_olheiros(olheiros)
    if not olheiros:
        return
    try:
        i = int(input("\nDigite o número do olheiro: ")) - 1
        if 0 <= i < len(olheiros):
            olheiro = olheiros[i]
            print("\n--- Atualização ---")
            novo_nome = input(f"Novo nome ({olheiro['nome']}): ").strip()
            novo_contato = input(f"Novo contato ({olheiro['contato']}): ").strip()
            if novo_nome:
                olheiro['nome'] = novo_nome
            if novo_contato:
                olheiro['contato'] = novo_contato
            print("✅ Olheiro atualizado com sucesso!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Digite um número válido.")


def excluir_olheiro(olheiros):
    listar_olheiros(olheiros)
    if not olheiros:
        return
    try:
        i = int(input("\nDigite o número do olheiro a excluir: ")) - 1
        if 0 <= i < len(olheiros):
            nome = olheiros[i]['nome']
            olheiros.pop(i)
            print(f"✅ Olheiro '{nome}' excluído com sucesso!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Digite um número válido.")


# -------------------- Avaliações -------------------- #

def avaliar_jogadora(jogadoras, olheiros, avaliacoes):
    listar_jogadoras(jogadoras)
    if not jogadoras:
        return
    listar_olheiros(olheiros)
    if not olheiros:
        return
    try:
        j = int(input("\nNúmero da jogadora: ")) - 1
        o = int(input("Número do olheiro: ")) - 1
        if 0 <= j < len(jogadoras) and 0 <= o < len(olheiros):
            nota = input_nota("Nota (0-10): ")
            comentario = input("Comentário: ").strip()
            avaliacoes.append({
                "jogadora": jogadoras[j]["nome"],
                "olheiro": olheiros[o]["nome"],
                "nota": nota,
                "comentario": comentario
            })
            print("✅ Avaliação registrada!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Digite números válidos.")


def listar_avaliacoes(avaliacoes):
    print("\n=== Avaliações ===")
    if not avaliacoes:
        print("Nenhuma avaliação registrada.")
        return
    for i, a in enumerate(avaliacoes, start=1):
        print(f"\n[{i}] Jogadora: {a['jogadora']}")
        print(f"Olheiro: {a['olheiro']}")
        print(f"Nota: {a['nota']}")
        print(f"Comentário: {a['comentario']}")


# -------------------- Função Principal -------------------- #

def main():
    jogadoras = []
    olheiros = []
    avaliacoes = []

    print("\n⚽ Bem-vindo à Plataforma de Talentos Femininos ⚽")
    while True:
        print("\n=== MENU JOGADORA ===")
        print("1 - Cadastrar jogadora")
        print("2 - Listar jogadoras")
        print("3 - Atualizar jogadora")
        print("4 - Excluir jogadora")
        print("\n=== MENU OLHEIRO ===")
        print("5 - Cadastrar olheiro")
        print("6 - Listar olheiros")
        print("7 - Atualizar olheiro")
        print("8 - Excluir olheiro")
        print("9 - Avaliar jogadora")
        print("\n================")
        print("10 - Listar avaliações")
        print("11 - Sair")
        print("\n\n\n")

        opcao = input("Escolha: ").strip()
        if opcao == "1":
            cadastrar_jogadora(jogadoras)
        elif opcao == "2":
            listar_jogadoras(jogadoras)
        elif opcao == "3":
            atualizar_jogadora(jogadoras)
        elif opcao == "4":
            excluir_jogadora(jogadoras)
        elif opcao == "5":
            cadastrar_olheiro(olheiros)
        elif opcao == "6":
            listar_olheiros(olheiros)
        elif opcao == "7":
            atualizar_olheiro(olheiros)
        elif opcao == "8":
            excluir_olheiro(olheiros)
        elif opcao == "9":
            avaliar_jogadora(jogadoras, olheiros, avaliacoes)
        elif opcao == "10":
            listar_avaliacoes(avaliacoes)
        elif opcao == "11":
            print("👋 Encerrando o sistema. Até mais!")
            break
        else:
            print("❌ Opção inválida!")


# -------------------- Execução -------------------- #
if __name__ == "__main__":
    main()
