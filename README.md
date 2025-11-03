🏆 Passa a Bola – Sistema de Gerenciamento de Times Femininos

O Passa a Bola é um sistema interativo em Python voltado para o gerenciamento de times, jogadoras e campeonatos de futebol feminino.
Ele permite cadastro e login de usuários, criação de times personalizados, visualização de elencos, consulta de classificações e históricos de jogadoras.

📋 Funcionalidades Principais
👤 Sistema de Usuários

Login e Cadastro com validação simples de nome e senha.

Armazena usuários em listas (usuarios_nomes e usuarios_senhas).

🏟️ Classificação da Copa

Exibe os times pré-cadastrados e seus desempenhos:

Pontos

Jogos

Vitórias

⚽ Histórico de Jogadoras

Consulta jogadoras cadastradas com:

Nome, time e posição

Histórico de partidas (gols e assistências)

Prêmios conquistados

🧢 Elencos e Times Personalizados

Visualize o elenco fixo do FC Vitória Regia.

Crie e personalize novos times, adicionando jogadoras com nome, posição e número.

Consulte os times criados por você com seus respectivos elencos.

🧠 Estrutura do Código
Seção	Descrição
usuarios_nomes, usuarios_senhas	Armazenam dados de login.
dados_times	Dicionário com informações dos times da copa.
jogadoras	Lista de jogadoras com histórico e prêmios.
elenco_vitoria_regia	Time fixo disponível no sistema.
times_personalizados	Lista que armazena os times criados pelos usuários.
Funções principais	Responsáveis pelo funcionamento dos menus e exibição de dados.
🖥️ Menus do Sistema
🏁 Menu Inicial

Login

Cadastro

Sair do Sistema

📜 Menu Principal

Classificação de Times

Histórico de Jogadora

Elencos de Times

Sair da Conta

👥 Menu Elencos

Ver FC Vitória Regia

Criar seu time

Ver times personalizados

Voltar

💡 Exemplo de Uso

Ao executar o código (python passa_a_bola.py):

=== PASSA A BOLA ===
1. Login
2. Cadastro
3. Sair do Sistema


🔹 Se o usuário fizer login com sucesso, poderá navegar entre os menus, visualizar informações dos times e criar novos elencos.
🔹 O sistema valida entradas numéricas e evita duplicação de usuários ou times.

📂 Estrutura Recomendada de Arquivos
passa_a_bola/
│
├── passa_a_bola.py     # Código principal do sistema
└── README.md            # Documentação do projeto

👨‍💻 Tecnologias Utilizadas

🐍 Python 3.x

Entrada e saída padrão (funções input() e print())

Estruturas de dados nativas: listas e dicionários

🚀 Como Executar

Certifique-se de ter o Python 3 instalado.

Baixe o arquivo passa_a_bola.py.

No terminal, execute:

python passa_a_bola.py


Siga as instruções exibidas na tela.

🏅 Créditos

Desenvolvido por:
Samuel de Oliveira da Silva – RM 566244
Projeto Passa a Bola – Sprint Python