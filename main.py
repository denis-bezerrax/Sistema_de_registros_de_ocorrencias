# Cadastrar ocorrências com identificador, categoria, descrição, local genérico, data simulada e situação atual;
# Organizar os registros em estruturas como listas, filas, pilhas, dicionários e matrizes, de acordo com sua finalidade;
# Consultar registros por identificador, categoria e status, aplicando condições e busca;
# Atualizar o status das demandas e preservar um histórico simples das alterações realizadas;
# Calcular e apresentar indicadores básicos, como total de ocorrências por categoria, quantidade por situação e tempo simulado de acompanhamento;
# Exibir orientações e informações de forma compreensível, utilizando uma interface textual funcional ou outra solução compatível com os conteúdos estudados.

import os
import subprocess

# Função que limpar o console para uma melhor visualização
def clear_console():
    cmd = "cls" if os.name == "nt" else "clear"
    subprocess.call(cmd, shell=True)


occurrence = [{"id": 1,"categoria": "Acessibilidade","descricao":"A rampa do PoupaTempo está com vários buracos","local":"Rua Treze de Maio, Bela Vista","data":"16/11/2026","situacao": "Aberta","historico": ["Ocorrência cadastrada"], "devolutiva":""},
 {"id":2, "categoria": "Escola","descricao":"A escola está frequentemente suja na entrada dos alunos","local":"Av. Srg. Mario Kozel Filho, Paraíso","data":"17/11/2026","situacao": "Aberta","historico": ["Ocorrência cadastrada"], "devolutiva":""},
 {"id":3, "categoria": "Rua","descricao":"A rua está com um enorme buraco, tendo risco de acidentes.","local":"Rua Conselheiro Zacarias, Jardim Paulista","data":"18/11/2026","situacao": "Em análise","historico": ["Ocorrência cadastrada", ["Ocorrência em análise"]], "devolutiva":""},
 {"id":4, "categoria": "Calçada","descricao":"Os cantos da calçada estão quebrados, necessitando ser reparado.","local":"Rua José Clemente, Jardim Paulista","data":"17/11/2026","situacao": "Aberta","historico": ["Ocorrência cadastrada"], "devolutiva":""},
 {"id":5, "categoria": "Iluminação","descricao":"Os postes estão sem energia.","local":"Rua Mirassol, Vila da Saúde","data":"19/11/2026","situacao": "Aberta","historico": ["Ocorrência cadastrada"], "devolutiva":""},
 {"id":6, "categoria": "Hospital","descricao":"O hospital sempre está lotado, tendo uma enorme fila todos os dias.","local":"Rua Napoleão de Barros, Vila Clementino","data":"17/11/2026","situacao": "Aberta","historico": ["Ocorrência cadastrada"], "devolutiva":""},
 {"id":7, "categoria": "Outros","descricao":"A pracinha precisa de uma reforma","local":"Rua Botucatu, Vila Clementino","data":"15/11/2026","situacao": "Aberta","historico": ["Ocorrência cadastrada"], "devolutiva":""},
 {"id":8, "categoria": "Outros","descricao":"Os ônibus estão demorando muito para passar nos pontos.","local":"Todos","data":"19/11/2026","situacao": "Aberta","historico": ["Ocorrência cadastrada"], "devolutiva":""},
 {"id":9, "categoria": "Escola","descricao":"O estacionamento da escola está indisponível por causa que depositaram entulho.","local":"Rua São Joaquim, Liberdade","data":"19/11/2026","situacao": "Em análise","historico": ["Ocorrência cadastrada", "Ocorrência em análise "], "devolutiva":""},
 {"id":10, "categoria": "Rua","descricao":"A rua está com asfalto cheio de buracos.","local":"Rua Muniz de Sousa, Cambuci","data":"17/11/2026","situacao": "Concluída","historico": ["Ocorrência cadastrada", "Ocorrência em análise", "Ocorrência concluída"], "devolutiva":""},
 {"id":11, "categoria": "Iluminação","descricao":"Não tem nenhuma iluminaçao funcionando na rua.","local":"Rua Gama Cerqueira","data":"16/11/2026","situacao": "Concluída","historico": ["Ocorrência cadastrada", "Ocorrência em análise", "Ocorrência concluída"], "devolutiva":""},
 {"id":12, "categoria": "Acessibilidade","descricao":"A rampa para deficientes está indisponível por causa de reformas no Museu há mais de um Mês.","local":"Rua Dr. Cesário Mota Junior, Vila Buarque","data":"19/11/2026","situacao": "Concluída","historico": ["Ocorrência cadastrada", "Ocorrência em análise", "Ocorrência concluída"], "devolutiva":""},
 {"id":13, "categoria": "Outros","descricao":"O prédio é lindo.","local":"Narnia, Narnia","data":"41/13/2015","situacao": "Aberta","historico": ["Ocorrência cadastrada"], "devolutiva":""}]
id_ocurrence = 13


# Menu principal do programa
def program():
    # Verificação da opção digitada pelo usuário
    while True:
        menu_main()
        repeat = True
        answer = input("Digite o número da opção desejada: ")
        clear_console()
        # Cadastrar ocorrência
        if answer == "1":
            register_occurrence()
            repeat = False

        # Consultar ocorrências
        elif answer == "2":
            consult_occurrence()
            repeat = False
        # Modificar ocorrências
        elif answer == "3":
            modify_occurrence()
            repeat = False
        elif answer == "0":
            repeat = False
        else:
            clear_console()
            print("Opção inválida.")

        if repeat == False:
            break

# Lista das opções disponíveis do menu principal
def menu_main():
    print("Menu Principal")
    print("(1) Cadastrar ocorrência")
    print("(2) Consultar ocorrências")
    print("(3) Modificar ocorrência")
    print("(0) Sair do programa")


def register_occurrence():
    global id_ocurrence
    global category
    repeat = True
    menu_category()
    print("(0) Voltar")
    answer = str(input("Digite o número da categoria desejada: "))

    while True:
        if answer == "1":
            category = "Acessibilidade"
            informations_register()
            repeat = False
        elif answer == "2":
            category = "Calçada"
            informations_register()
            repeat = False
        elif answer == "3":
            category = "Escola"
            informations_register()
            repeat = False
        elif answer == "4":
            category = "Hospital"
            informations_register()
            repeat = False
        elif answer == "5":
            category = "Iluminação"
            informations_register()
            repeat = False
        elif answer == "6":
            category = "Rua"
            informations_register()
            repeat = False
        elif answer == "7":
            category = "Outros"
            informations_register()
            repeat = False
        elif answer == "0":
            repeat = False
            clear_console()
            program()
        else:
            clear_console()
            menu_category()
            answer = input("Opção inválida. Digite uma opção disponível: ")

        if repeat == False:
            break


def informations_register():
    global id_ocurrence
    global category
    clear_console()
    description = input("Digite uma breve descrição sobre a sua ocorrência: ")
    while description == "":
        print("A descrição não pode ficar vazia, preencha abordando a ocorrência.")
        description = input("Digite uma breve descrição sobre a sua ocorrência: ")
    clear_console()
    local = input("Digite o local da sua ocorrência, exemplo 'Av. Paulista, Bela Vista': ")
    while local == "":
        print("O local não pode ficar vazio, informe o local da ocorrência.")
        local = input("Digite o local da sua ocorrência, exemplo 'Av. Paulista, Bela Vista': ")
    clear_console()
    data = input("Digite a data da ocorrência (Exemplo: 15/10/2026): ")
    while data == "":
        print("A data não pode ficar vazia, preencha a data do ocorrido.")
        data = input("Digite a data da ocorrência (Exemplo: 15/10/2026): ")
    clear_console()
    print("Resumo da ocorrência")
    print(f"Categoria: {category}")
    print(f"Descrição: {description}")
    print(f"Local: {local}")
    print(f"Data: {data}")

    while True:
        answer = input("Você deseja modificar as informações? Digite 's' para sim ou 'n' para não: ")
        repeat = True
        if answer == "s":
            clear_console()
            register_occurrence()
        elif answer == "n":
            clear_console()
            print("A sua ocorrência foi salva!")
            id_ocurrence += 1
            print(
                f"O id da sua ocorrência é {id_ocurrence}. Basta digitar o ID na consulta de ocorrências para acompanha-la"
            )
            new_occurrence = {
                "id": id_ocurrence,
                "categoria": category,
                "descricao": description,
                "local": local,
                "data": data,
                "situacao": "Aberta",
                "historico": ["Ocorrência cadastrada"],
                "devolutiva": ""
            }
            occurrence.append(new_occurrence)
            input("Aperte para voltar ao menu principal ")
            clear_console()
            repeat = False
            program()
            
        else:
            print("Opção inválida")

        if repeat == False:
            break


# Lista das opções disponíveis do menu de categoria
def menu_category():
    print("Categorias disponíveis:")
    print("(1) Acessibilidade")
    print("(2) Calçada")
    print("(3) Escola")
    print("(4) Hospital")
    print("(5) Iluminação")
    print("(6) Rua")
    print("(7) Outros")

def consult_occurrence():
    global occurrence
    repeat = True
    clear_console()
    print("(1) Consultar por ID")
    print("(2) Consultar por categoria")
    print("(3) Consultar por status")
    print("(0) Voltar")

    while True:
        answer = input("Digite o número da opção desejada: ")
        if answer == "1":
            clear_console()
            repeat = True
            while True:
                try: 
                    answer = int(input("Digite o id da ocorrência: "))
                except ValueError:
                    print("Digite apenas números no id.")
                for item in occurrence:
                    value_id = item["id"]
                    if answer == value_id:
                        print("Resumo da ocorrência")
                        print(f"Categoria: {item["categoria"]}")
                        print(f"Descrição: {item["descricao"]}")
                        print(f"Local: {item["local"]}")
                        print(f"Data: {item["data"]}")
                        print(f"Situação: {item["situacao"]}")
                        print(f"Histórico: {item["historico"]}")
                        print(f"Devolutiva: {item["devolutiva"]}")

                        input("Aperte para voltar ao menu principal ")
                        clear_console()
                        program()
                        repeat = False

                if repeat == False:
                    break
                while True:
                    repeat = True
                    print("ID não encontrado!")
                    answer = input("Você deseja tentar buscar novamente pelo ID a ocorrência? Digite 's' para sim ou 'n' para não: ")
                    if answer == "s":
                        break
                    elif answer == "n":
                        clear_console()
                        program()
                        repeat = False
                        break
                    else:
                        print("Reposta inválida, digite uma opção válida.")
                        answer = input("Você deseja tentar buscar novamente pelo ID a ocorrência? Digite 's' para sim ou 'n' para não: ")

                if repeat == False:
                    break


        elif answer == "2":
            clear_console()
            menu_category()
            answer = input("Digite o número da categoria para buscar as ocorrências: ")
            while True:
                if answer == "1":
                    clear_console()
                    answer = "Acessibilidade"
                    repeat = True
                    for item in occurrence:
                        value_category = item["categoria"]

                        if answer == value_category:
                            repeat = False
                            print(f"ID:{item["id"]} | Categoria: {item["categoria"]} | Data: {item["data"]} | Situação: {item["situacao"]}")

                    if repeat == True:
                        print(f"Não foi encontrado nenhuma ocorrência na categoria {answer}.")
                    
                    input("Aperte para voltar ao menu principal ")
                    clear_console()
                    program()
                    repeat = False
                    break
                elif answer == "2":
                    clear_console()
                    answer = "Calçada"
                    repeat = True
                    for item in occurrence:
                        value_category = item["categoria"]

                        if answer == value_category:
                            repeat = False
                            print(f"ID:{item["id"]} | Categoria: {item["categoria"]} | Data: {item["data"]} | Situação: {item["situacao"]}")

                    if repeat == True:
                        print(f"Não foi encontrado nenhuma ocorrência na categoria {answer}.")
                    
                    input("Aperte para voltar ao menu principal ")
                    clear_console()
                    program()
                    repeat = False
                    break
                elif answer == "3":
                    clear_console()
                    answer = "Escola"
                    repeat = True
                    for item in occurrence:
                        value_category = item["categoria"]

                        if answer == value_category:
                            repeat = False
                            print(f"ID:{item["id"]} | Categoria: {item["categoria"]} | Data: {item["data"]} | Situação: {item["situacao"]}")

                    if repeat == True:
                        print(f"Não foi encontrado nenhuma ocorrência na categoria {answer}.")
                    
                    input("Aperte para voltar ao menu principal ")
                    clear_console()
                    program()
                    repeat = False
                    break
                elif answer == "4":
                    clear_console()
                    answer = "Hospital"
                    repeat = True
                    for item in occurrence:
                        value_category = item["categoria"]

                        if answer == value_category:
                            repeat = False
                            print(f"ID:{item["id"]} | Categoria: {item["categoria"]} | Data: {item["data"]} | Situação: {item["situacao"]}")

                    if repeat == True:
                        print(f"Não foi encontrado nenhuma ocorrência na categoria {answer}.")
                    
                    input("Aperte para voltar ao menu principal ")
                    clear_console()
                    program()
                    repeat = False
                    break
                elif answer == "5":
                    clear_console()
                    answer = "Iluminação"
                    repeat = True
                    for item in occurrence:
                        value_category = item["categoria"]

                        if answer == value_category:
                            repeat = False
                            print(f"ID:{item["id"]} | Categoria: {item["categoria"]} | Data: {item["data"]} | Situação: {item["situacao"]}")

                    if repeat == True:
                        print(f"Não foi encontrado nenhuma ocorrência na categoria {answer}.")
                    
                    input("Aperte para voltar ao menu principal ")
                    clear_console()
                    program()
                    repeat = False
                    break
                elif answer == "6":
                    clear_console()
                    answer = "Rua"
                    repeat = True
                    for item in occurrence:
                        value_category = item["categoria"]

                        if answer == value_category:
                            repeat = False
                            print(f"ID:{item["id"]} | Categoria: {item["categoria"]} | Data: {item["data"]} | Situação: {item["situacao"]}")

                    if repeat == True:
                        print(f"Não foi encontrado nenhuma ocorrência na categoria {answer}.")
                    
                    input("Aperte para voltar ao menu principal ")
                    clear_console()
                    program()
                    repeat = False
                    break
                elif answer == "7":
                    clear_console()
                    answer = "Outros"
                    repeat = True
                    for item in occurrence:
                        value_category = item["categoria"]

                        if answer == value_category:
                            repeat = False
                            print(f"ID:{item["id"]} | Categoria: {item["categoria"]} | Data: {item["data"]} | Situação: {item["situacao"]}")

                    if repeat == True:
                        print(f"Não foi encontrado nenhuma ocorrência na categoria {answer}.")
                    
                    input("Aperte para voltar ao menu principal ")
                    clear_console()
                    program()
                    repeat = False
                    break
                elif answer == "8":
                    consult_occurrence()
                    repeat = False

                else:
                    print("Opção inválida.")
                    answer = input("Digite o número da categoria para buscar as ocorrências: ")

                if repeat == False:
                    break
            
                    
        elif answer == "3":
            clear_console()
            menu_situation()
            answer = input("Digite o número da situação para buscar as ocorrências: ")
            while True:
                if answer == "1":
                    clear_console()
                    answer = "Aberta"
                    repeat = True
                    for item in occurrence:
                        value_category = item["situacao"]

                        if answer == value_category:
                            repeat = False
                            print(f"ID:{item["id"]} | Categoria: {item["categoria"]} | Data: {item["data"]} | Situação: {item["situacao"]}")

                    if repeat == True:
                        print(f"Não foi encontrado nenhuma ocorrência com a situação {answer}.")
                    
                    input("Aperte para voltar ao menu principal ")
                    clear_console()
                    program()
                    repeat = False
                    break
                elif answer == "2":
                    clear_console()
                    answer = "Em análise"
                    repeat = True
                    for item in occurrence:
                        value_category = item["situacao"]

                        if answer == value_category:
                            repeat = False
                            print(f"ID:{item["id"]} | Categoria: {item["categoria"]} | Data: {item["data"]} | Situação: {item["situacao"]}")

                    if repeat == True:
                        print(f"Não foi encontrado nenhuma ocorrência com a situação {answer}.")
                    
                    input("Aperte para voltar ao menu principal ")
                    clear_console()
                    program()
                    repeat = False
                    break
                elif answer == "3":
                    clear_console()
                    answer = "Concluída"
                    repeat = True
                    for item in occurrence:
                        value_category = item["situacao"]

                        if answer == value_category:
                            repeat = False
                            print(f"ID:{item["id"]} | Categoria: {item["categoria"]} | Data: {item["data"]} | Situação: {item["situacao"]}")

                    if repeat == True:
                        print(f"Não foi encontrado nenhuma ocorrência com a situação {answer}.")
                    
                    input("Aperte para voltar ao menu principal ")
                    clear_console()
                    program()
                    repeat = False
                    break

                elif answer == "8":
                    consult_occurrence()
                    repeat = False

                else:
                    print("Opção inválida.")
                    answer = input("Digite o número da categoria para buscar as ocorrências: ")

                if repeat == False:
                    break

        elif answer == "0":
            repeat = False
            clear_console()
            program()
        
        else:
            print("Opção inválida")

        if repeat == False:
            break

def menu_situation():
    print("Situações disponíveis das ocorrências:")
    print("(1) Aberta")
    print("(2) Em Análise")
    print("(3) Concluída")

def modify_occurrence():
    clear_console()
    repeat = True
    answer = 0
    while True:
        try: 
            answer = int(input("Digite o id da ocorrência: "))
        except ValueError:
            print("Digite apenas números no id.")
        for item in occurrence:
            value_id = item["id"]
            if answer == value_id:
                print(f"Resumo da ocorrência | ID: {value_id}")
                print(f"(1) Categoria: {item["categoria"]}")
                print(f"(2) Descrição: {item["descricao"]}")
                print(f"(3) Local: {item["local"]}")
                print(f"(4) Data: {item["data"]}")
                print(f"(5) Situação: {item["situacao"]}")
                print(f"(6) Devolutiva: {item["devolutiva"]}")
                print("(0) Voltar")

                while True:
                    answer = input("Selecione o número da parte que deseja modificar da ocorrência: ")
                    clear_console()
                    if answer == "1":
                        print(f"A categoria atual da ocorrência é {item["categoria"]}.")
                        menu_category()
                        print("(0) Voltar")
    
                        while True:
                            answer = input("Selecione a categoria que a ocorrência mude: ")
                            if answer == "1":
                                item["categoria"] = "Acessibilidade"
                                repeat = False
                                print("A sua modificação foi salva com sucesso!")
                                input("Aperte para voltar ao menu principal")
                                clear_console()
                                program()
                            elif answer == "2":
                                item["categoria"] = "Calçada"
                                repeat = False
                                print("A sua modificação foi salva com sucesso!")
                                input("Aperte para voltar ao menu principal")
                                clear_console()
                                program() 
                            elif answer == "3":
                                item["categoria"] = "Escola"
                                repeat = False
                                print("A sua modificação foi salva com sucesso!")
                                input("Aperte para voltar ao menu principal")
                                clear_console()
                                program()
                            elif answer == "4":
                                item["categoria"] = "Hospital"
                                repeat = False
                                print("A sua modificação foi salva com sucesso!")
                                input("Aperte para voltar ao menu principal")
                                clear_console()
                                program()
                            elif answer == "5":
                                item["categoria"] = "Iluminação"
                                repeat = False
                                print("A sua modificação foi salva com sucesso!")
                                input("Aperte para voltar ao menu principal")
                                clear_console()
                                program()
                            elif answer == "6":
                                item["categoria"] = "Rua"
                                repeat = False
                                print("A sua modificação foi salva com sucesso!")
                                input("Aperte para voltar ao menu principal")
                                clear_console()
                                program()
                            elif answer == "7":
                                item["categoria"] = "Outros"
                                repeat = False
                                print("A sua modificação foi salva com sucesso!")
                                input("Aperte para voltar ao menu principal")
                                clear_console()
                                program()
                            elif answer == "0":
                                repeat = False
                                clear_console()
                                program()

                            else:
                                print("Opção inválida.")

                            if repeat == False:
                                break
                        if repeat == False:
                            break

                    elif answer == "2":
                        print("Descrição atual:")
                        print(item["descricao"])
                        item["descricao"] = input("Digite a nova descrição da ocorrência: ")
                        print("A sua modificação foi salva com sucesso!")
                        input("Aperte para voltar ao menu principal")
                        repeat = False
                        clear_console()
                        program()
                    elif answer == "3":
                        print("Local atual:")
                        print(item["local"])
                        item["local"] = input("Digite o novo local da ocorrência: ")
                        print("A sua modificação foi salva com sucesso!")
                        input("Aperte para voltar ao menu principal")
                        repeat = False
                        clear_console()
                        program()
                    elif answer == "4":
                        print("Data atual:")
                        print(item["data"])
                        item["data"] = input("Digite a nova data da ocorrência: ")
                        print("A sua modificação foi salva com sucesso!")
                        input("Aperte para voltar ao menu principal")
                        repeat = False
                        clear_console()
                        program()
                    elif answer == "5":
                        print("Situação atual:")
                        print(item["situacao"])
                        menu_situation()
                        answer = input("Digite o número da situação que deseje alterar: ")

                        while True:
                            repeat = True
                            if answer == "1":
                                repeat = False
                                item["situacao"] = "Aberta"
                                print("A sua modificação foi salva com sucesso!")
                                input("Aperte para voltar ao menu principal")
                                clear_console()
                                program()

                            elif answer == "2":
                                repeat = False
                                item["situacao"] = "Em análise"
                                print("A sua modificação foi salva com sucesso!")
                                item["historico"].append("Ocorrência em análise")
                                input("Aperte para voltar ao menu principal")
                                clear_console()
                                program()

                            elif answer == "3":
                                repeat = False
                                item["situacao"] = "Concluída"
                                print("A sua modificação foi salva com sucesso!")
                                item["historico"].append("Ocorrência concluída")
                                input("Aperte para voltar ao menu principal")
                                clear_console()
                                program()

                            else:
                                print("Opção inválida.")
                                answer = input("Digite o número da situação que deseje alterar: ")

                            if repeat == False:
                                break

                    elif answer == "6":
                        item["devolutiva"] = input("Digite uma devolutiva para a ocorrência: ")
                        print("A sua modificação foi salva com sucesso!")
                        repeat = False
                        input("Aperte para voltar ao menu principal")
                        clear_console()
                        program()

                    elif answer == "0":
                        repeat = False
                        clear_console()
                        program()
                    
                    else:
                        print("Opção inválida.")

                    if repeat == False:
                        break
            
        if repeat == False:
            break

        while True:
            repeat = True
            print("ID não encontrado!")
            answer = input("Você deseja tentar buscar novamente pelo ID a ocorrência? Digite 's' para sim ou 'n' para não: ")
            if answer == "s":
                break
            elif answer == "n":
                clear_console()
                repeat = False
                program()
                break
            else:
                print("Reposta inválida, digite uma opção válida.")

            if repeat == False:
                break

        if repeat == False:
            break

# Program
print("Bem vindo ao Neighborhood Action Dashboard!")
program()
