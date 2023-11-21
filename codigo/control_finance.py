def atualizar_movimentacao():
    with open('base.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo, delimiter=';')
        movimentacao = list(leitor)

    if not movimentacao:
        pass

    indice = int(input("Digite o número da movimentação que deseja atualizar: "))

    if 0 <= indice < len(movimentacao):
        tipo = input("Digite o novo tipo de movimentação (receita, despesa, investimento): ")
        data = datetime.date.today().strftime("%Y-%m-%d")

        if tipo.lower() == 'despesa':
            valor = -float(input("Digite o novo valor da movimentação: "))
            montante = 0
            taxa = 0
            rendimento = 0
            historico = ''
        elif tipo.lower() == 'investimento':
            valor = float(input("Digite o novo valor investido: "))
            taxa = float(input("Digite a nova taxa de rendimento (em decimal): "))
            tempo_dias = (datetime.date.today() - datetime.datetime.strptime(data, "%Y-%m-%d").date())
            montante = round(valor * (1 + taxa) ** tempo_dias.days, 2)
            rendimento = round(montante - valor, 2)
            historico = ''
        else:
            valor = float(input("Digite o novo valor da movimentação: "))
            montante = 0
            taxa = 0
            rendimento = 0
            historico = ''

        movimentacao[indice] = [
            str(indice), str(int(data.split('-')[2])), str(int(data.split('-')[1])), str(int(data.split('-')[0])),
            tipo, valor, historico, taxa, montante, 
            rendimento] if tipo.lower() == 'investimento' else [
                                                                str(indice),str(int(data.split('-')[2])),
                                                                str(int(data.split('-')[1])),
                                                                str(int(data.split('-')[0])),tipo,valor,historico,
                                                                '','','']
                                                                              
        return movimentacao
        
             
         
     

    