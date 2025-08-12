import os
lista_tarefas = [] 
menu=None

while menu != 5:
    menu =int(input("Para adicionar uma nova tarefa digite 1\nPara ver a sua lista de tarefas digite 2\nPara modificar qualquer tarefa digite 3\nPara excluir uma tarefa digite 4\nPara sair do TO DO digite 5\n-->"))
    
    os.system("cls")
    os.system("cls")

    if menu > 5 or menu < 1:

        menu=(input("Digite uma ação válida\n-->"))

    if menu == 1: #adicionar tarefa
        
        tarefas=input("Adicione uma nova tarefa aqui\n-->")

        print("Tarefa adicionada com sucesso")

        lista_tarefas.append(tarefas)

        os.system("pause")
        os.system("cls")
    
    elif menu == 2: #lista completa

        if len (tarefas) != 0:
            cont = 1
            for tarefa in lista_tarefas:
                print (f"{cont}ª TAREFA: {tarefa}")
                cont += 1
        else:
            print("Nao existe tarefas adicionadas")
        
        os.system("pause")
    
    elif menu == 3: #modificar
        
        os.system("cls")
        
        modificar=int(input("Qual tarefa voce deseja modificar?\n-->"))
        
        modificar -= 1
        
        print("Sua tarefa atual é:")
        
        print(lista_tarefas[modificar])
        
        print("")
        
        novatarefa=input("Qual a nova tarefa que deseja?\n-->")
        
        lista_tarefas[modificar]=novatarefa
        
        print("Tarefa atualizada com sucesso")
        
        os.system("pause")
        os.system("cls")

    elif menu == 4: #Excluir tarefa
        os.system("cls")
        excluir=int(input("Qual tarefa deseja excluir?\n-->"))
        excluir -= 1
        lista_tarefas.pop(excluir)
        print("Tarefa excluida com sucesso")
        os.system("pause")
else:
    print("Saindo...")
    os.system("pause")
    os.system("cls")