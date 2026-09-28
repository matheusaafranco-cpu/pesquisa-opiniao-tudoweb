# ============================================================
# Programa: Pesquisa de Opinião - TudoWeb
# Estrutura de Repetição com Validação e Loop Contínuo
# ============================================================

# Variáveis contadoras
quantidade_excelente = 0
quantidade_ruim = 0
contador_entrevistados = 0

print("=== PESQUISA DE SATISFAÇÃO - TUDOWEB ===")

# Estrutura de repetição para tornar a pesquisa "infinita" até o utilizador decidir parar
while True:
    contador_entrevistados += 1
    print(f"\n--- Entrevistado {contador_entrevistados} ---")
    
    nome = input("Digite o nome: ")
    
    # Validação da idade: aceita apenas números inteiros
    while True:
        try:
            idade = int(input("Digite a idade: "))
            if idade > 0:
                break
            else:
                print("Erro: A idade deve ser um número maior que zero.")
        except ValueError:
            print("Erro: Digite apenas números inteiros para a idade!")

    # Validação da opinião (1, 2 ou 3)
    while True:
        print("\nOpinião sobre o atendimento:")
        print("1 - EXCELENTE")
        print("2 - BOM")
        print("3 - RUIM")
        try:
            opiniao = int(input("Digite a opção (1, 2 ou 3): "))
            if opiniao in [1, 2, 3]:
                break
            else:
                print("Erro: Opção inválida! Escolha entre 1, 2 ou 3.")
        except ValueError:
            print("Erro: Digite apenas o número 1, 2 ou 3.")

    # Estrutura de decisão para verificar a opinião
    if opiniao == 1:
        quantidade_excelente += 1
    elif opiniao == 3:
        quantidade_ruim += 1

    # Pergunta se deseja continuar a pesquisa
    while True:
        resposta = input("\nDeseja cadastrar mais uma opinião? (S/N): ").strip().upper()
        if resposta in ["S", "N"]:
            break
        print("Erro: Resposta inválida! Digite apenas 'S' para Sim ou 'N' para Não.")

    # Se a resposta for 'N', encerra a pesquisa
    if resposta == "N":
        break

# Exibição dos resultados finais
print("\n" + "=" * 40)
print("RESULTADO FINAL DA PESQUISA")
print("=" * 40)
print(f"Total de entrevistados: {contador_entrevistados}")
print(f"a) Quantidade de respostas 'EXCELENTE': {quantidade_excelente}")
print(f"b) Quantidade de respostas 'RUIM': {quantidade_ruim}")
print("=" * 40)
print("Pesquisa encerrada com sucesso!")