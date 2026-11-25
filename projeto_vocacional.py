
areas = {
    "Tecnologia": 0,
    "Saúde": 0,
    "Humanas": 0,
    "Negócios": 0
}

carreiras = {
    "Tecnologia": [
        "Programador",
        "Desenvolvedor Web",
        "Analista de Dados"
    ],
    "Saúde": [
        "Enfermeiro",
        "Fisioterapeuta",
        "Médico"
    ],
    "Humanas": [
        "Professor",
        "Jornalista",
        "Advogado"
    ],
    "Negócios": [
        "Administrador",
        "Vendedor",
        "Empreendedor"
    ]
}

def fazer_pergunta(pergunta, area, pontos):
    while True:
        resposta = input(f"{pergunta} (S/N): ")
        if resposta.upper() == "S":  
            areas[area] += pontos
            break
        elif resposta.upper() == "N":
            break
        else:
            print("Digite apenas S ou N")

def questionario():    
    for area in areas:
        areas[area] = 0
        
    fazer_pergunta("Lida bem com computadores?", "Tecnologia", 3)
    fazer_pergunta("Está sempre ajudando as pessoas?", "Saúde", 3)
    fazer_pergunta("Você gosta de ler e escrever?", "Humanas", 3)
    fazer_pergunta("Realizar vendas te atrai?", "Negócios", 3)
    fazer_pergunta("É curioso (a) sobre assuntos de Tecnologia?", "Tecnologia", 3)
    fazer_pergunta("Gosta de Artes e Design?", "Humanas", 3)
    fazer_pergunta("Tem curiosidade em aprender sobre doenças?", "Saúde", 3)
    fazer_pergunta("Em um ambiente competitivo você se sente à vontade?", "Negócios", 3)
    fazer_pergunta("Se sente confortável quando o assunto é Lógica? ", "Tecnologia", 3)
    fazer_pergunta("Para você, cortar peles, lidar com sangue e agulhas, tudo bem? ", "Saúde", 3)
    fazer_pergunta("Você se vê discursando, dando palestras, ou ensinando outras pessoas? ", "Humanas", 3)
    fazer_pergunta("Taxas, indicadores, índices, gráficos, fazem parte do seu universo? ", "Negócios", 3)


def mostrar_resultado():
    print(f"\nPontuação Final:")    
    
    for area in areas:
        print(area, ":", areas[area])
    
    melhor_area = max(areas, key=areas.get)    
    
    print("\nÁrea Recomendada: ")
    print(melhor_area)
    
    print("\nProfissões Sugeridas: ")
    for profissao in carreiras[melhor_area]:
        print("-", profissao)  

def menu():    
    while True:
        print("\n ====MENU====")
        print("1 - Fazer Teste Vocacional")
        print("2 - Sair")
        
        opcao = input("Escolha uma opção: ") 
        
        match opcao:
            case "1":
                questionario()
                mostrar_resultado()
            case "2":
                print("Programa encerrado.")
                break
            case _: 
                print("Opção inválida.")

if __name__ == "__main__":
    menu()
