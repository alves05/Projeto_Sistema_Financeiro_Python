import csv
import datetime

movimentacoes = []   #lista que armazena as movimentacoes realizadas
 
def atualizar_movimentacao():
     exibir_movimentacoes()   # antes de da função atualizar criar uma função para exibir as movimentações já realizadas, deverá conter o número (índice) da movimentação
     if not movimentacoes:    # caso não seja encontrada nenhum registro no arquivo csv, retorna "Nenhuma movimentação foi encontrada"
         print("Nenhuma movimentação econtrada")
         
     indice = int(input("Digite o número da movimentação que deseja atualizar: "))
     if 0 <= indice < len(movimentacoes):
         tipo = input("Digite o novo tipo de movimentação (receita, despesa, investimento): ") # resgistra o novo tipo
         data = datetime.date.today().strftime("%Y-%m-%d") #atualiza data para data atual
         
         if tipo.lower() == 'despesa':
             valor = -float(input("Digite o novo valor da movimentação: "))
             montante = 0
             taxa = 0
             rendimento = 0
             
         elif tipo.lower() == 'investimento':
             valor = float(input("Digite o novo valor da movimentação: "))
             taxa = float(input("Digite a nova taxa de rendimento (em decimal): "))
             tempo_dias = (datetime.date.today() - datetime.datetime.strptime(data, "%Y-%m-%d").date()).days
             montante = round(valor * (1 + taxa) ** tempo_dias, 2)  
             rendimento = round(montante - valor, 2)
             
         else:
            valor = float(input("Digite o novo valor da movimentação: "))
            montante = 0
            taxa = 0
            rendimento = 0
             
        # falta criar código para atualizar a lista movimentações  
        print("Movimentação atualizada com sucesso")
    else:
        print("Índice inválido")
        
             
         
     

    