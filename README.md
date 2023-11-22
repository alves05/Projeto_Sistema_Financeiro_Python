
# Sistema de Controle Financeiro

## Objetivo do Projeto:

Desenvolver um sistema para controle financeiro que receba as movimentações e as armazene em um arquivo .csv, com importação dos lançamentos originais (se existentes) e possibilidade de exportação do arquivo com todo o histórico de lançamentos realizados pelo usuário.

## Equipe de Desenvolvimento:

- [Wiliams Alves](https://github.com/alves05)
- [Humberto Tiggemann](https://github.com/HumbertoTiggemann)
- [Tamires Souza](https://github.com/tamiresouza)   
- [Augusto Messias](https://github.com/mineironovale) 

## Arquivos do Projeto:

||Nome|Link|
|---|---|---|
|1.|Código da Aplicação|[codigo](./codigo/control_finance.py)|
|2.|Bases CSV|[bases](./codigo/bases/)|
|3.|Outros Arquivos|[outros](./outros/)|
|4.|License|[license](./LICENSE)|

## Contextualização:

O controle financeiro é uma parte crucial da gestão de recursos de qualquer negócio ou indivíduo. Este projeto visa fornecer uma solução eficaz para o gerenciamento de transações financeiras, permitindo ao usuário Criar, Ler, Atualizar, Extrair e Deletar registros de entradas, saídas e saldo corrente de investimentos realizados.

## Proposta de Solução:

O sistema proposto será capaz de realizar as seguintes operações:

### 1. Criar Novos Registros

Os registros devem possuir a data em que foram realizados, o tipo de movimentação e valor. Os tipos podem ser despesas, receita ou investimento:

-   No caso de receita, o valor inserido deverá ser positivo e armazenado normalmente neste formato.
-   No caso de despesas, o valor deve ser recebido como positivo mas armazenado como negativo.
-   No caso de investimento deve ter uma informação a mais de ‘montante’, em que será calculado quanto o dinheiro rendeu desde o dia em que foi investido. Para essa finalidade foi utilizada a fórmula de juros compostos a seguir:

	M=C∗(1+i)***t* em que:
	
	**M** é o Montante  
	**C** é o Capital  
	**i** é a Taxa do investimento  
	**t** é o Tempo  

### 2. Ler Registros

O sistema deverá consultar os registros por data, tipo, valor, histórico e id de lançamento.

### 3. Gerar Relatórios

O sistema deverá ser ser capaz de gerar relatórios e exportar.

### 4. Atualizar Registros

Os registros serão atualizados pelo id de lançamento, sendo possivel atualizar o tipo de lançamento, o valor e o histórico, nos casos de atualização de investimento deverá informar támbem a taxa de juros diário.

### 5. Deletar Registros

Deverá ser possível deletar o registro usando o id do lançamento.

## Ferramentas Utilizadas no Projeto:

- [Python 3.11](https://docs.python.org/3/)
- [csv](https://docs.python.org/3/library/csv.html)  
- [datetime](https://docs.python.org/3/library/datetime.html)  
- [os](https://docs.python.org/3/library/os.html)  
- [random](https://docs.python.org/3/library/random.html)
- [calendar](https://docs.python.org/3/library/calendar.html)
- [faker](https://faker.readthedocs.io/en/master/)
- [locale](https://docs.python.org/pt-br/3.8/library/locale.html)
- [sys](https://docs.python.org/3/library/sys.html)

## Diagrama de Funcionamento do Sistema:
![Fluxo logica](/outros/logica_contro_lfinance.jpg) 

# Sobre a Aplicação:

O nome do sistema é "CONTROL FINANCE", sistema para controle e gestão financeira.

## Tarefas Realizadas:

- [x] Inserir novos registros receita, despesa, investimento.
- [x] Consultar registro por data, tipo ou valor.
- [x] Atualizar registro.
- [x] Deletar registro.
- [x] Atualizar os rendimentos diários.
- [x] Crie uma função exportar_relatorio, que seja possível exportar um relatorio final em csv ou json.
- [x] Crie pelo menos uma função de agrupamento, que seja capaz de mostrar o total de valor baseado em alguma informação (mes, tipo...).
- [x] Crie valores separados para identificar a data (dia, mes, ano).
- [x] Nomear a aplicação


## Funções da Aplicação:


<details>
<summary><b>Função cria_base_csv():</b></summary>

- A função cria uma base pré estruturada para o sistema.

```
def cria_base_csv(numero_linhas: int = 100) -> None:
    '''Função cria base de dados no fromato csv para armazenamento
    dos lançamentos do sitema Control Finance.'''
      
    # Verifica se já existe a base csv    
    if os.path.exists('./bases/base.csv'):
        pass
        
    if not os.path.exists('./bases/base.csv'):
        # Criando cabeçalho
        with open('./bases/base.csv', 'w') as arquivo:
            escritor = csv.writer(arquivo, delimiter=';', lineterminator='\n')
            escritor.writerow(['ID_lancamento','dia','mes','ano','tipo','valor','historico','taxa','montante','rendimento'])

        # Coluna ID do lançamento
        numero_lancamento = list(range(1,numero_linhas + 1))

        # Criando coluna de datas aleatórias
        # Definindo uma semente
        Faker.seed(10)
        random.seed(10)
        fake = Faker()    
        # Data inicial e final
        inicio = datetime(2023,1,1)
        final = datetime(2023,11,19)
        # Adicionando datas a uma lista
        datas = []
        for _ in range(numero_linhas):
            data_aleatoria = fake.date_between_dates(date_start=inicio, date_end=final)
            datas.append(data_aleatoria)
        # Ordendando pela data e mês
        datas = sorted(datas)

        # Criando coluna tipo de lançamento
        tipo_lancamento = []
        for _ in range(numero_linhas):
            palavra_aleatoria = random.choice(['receita', 'despesa', 'investimento'])
            tipo_lancamento.append(palavra_aleatoria)

        # Criando coluna dos valores dos lançamentos
        valores = []
        for tipo in tipo_lancamento:
            if tipo == 'receita':
                valor_aleatorio = round(float(random.randint(100.00, 1000.00)),2)
            elif tipo == 'despesa':
                valor_aleatorio = round(float(random.randint(100.00, 1000.00) * -1), 2)
            else:
                valor_aleatorio = round(float(random.randint(100.00, 100.00)), 2)
            valores.append(valor_aleatorio)

        # Criando coluna historico
        historico = []
        for tipo in tipo_lancamento:
            if tipo == 'receita':
                receitas = random.choice(['vendas', 'servicos'])
                historico.append(receitas)

            elif tipo == 'despesa':
                despesas = random.choice(['energia', 'agua e esgoto', 'internet', 'despesa geral'])
                historico.append(despesas)

            else:
                historico.append('poupanca')

        # Criando coluna taxa de aplicação
        taxa = []
        for tipo in tipo_lancamento:
            if tipo == 'investimento':
                taxa.append(0.0005)
            else:
                taxa.append('')
                
        # Criando a coluna montante e rendimento
        montante = []
        rendimento = []
        for indice in range(len(tipo_lancamento)):
            tipo = tipo_lancamento[indice]
            
            if tipo == 'investimento':
                tempo_dias = (datetime.today().date() - datas[indice]).days
                acumulado = acumulado = round(valores[indice] * (1 + taxa[indice]) ** tempo_dias, 2)
                juros = round(acumulado - valores[indice], 2)
            else:
                acumulado = ''
                juros = ''
            
            montante.append(acumulado)
            rendimento.append(juros)

        ### Salvando a base CSV

        # Unindo as colunas
        matriz = []
        for indice in range(numero_linhas):
            registros = [numero_lancamento[indice], datas[indice].day, datas[indice].month, datas[indice].year,
                         tipo_lancamento[indice], valores[indice], historico[indice], taxa[indice],
                         montante[indice], rendimento[indice]]
            matriz.append(registros)
            
        # Salvando base
        with open('./bases/base.csv', 'a', newline='') as arquivo:
            escritor = csv.writer(arquivo, delimiter=';', lineterminator='\n')
            escritor.writerows(matriz)
        
    return None
```

</details>
<details>
<summary><b>Função atualizar_rendimentos_csv():</b></summary>

- A função recebe o arquivo com os registros financeiros do sistema e recebe a função calcula_rendimento(). A função filtra os registros pelo tipo de lançamento, calcula a diferença de dias entre o dia do lançamento e o dia atual, calcula o valor atual da aplicação e atualiza os registros de montante e rendimento.

```
def atualizar_rendimentos_csv(nome_arquivo: str='./bases/base.csv') -> None:
    def calcular_rendimento(valor:float, taxa:float, dias:int) -> float:
        return round(valor * (1 + taxa) ** dias, 2)

    # Ler o CSV
    with open(nome_arquivo, 'r', newline='') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Lê a primeira linha (cabeçalho)

        # Extrair colunas do CSV
        linhas = list(csv_reader)

    # Calcular rendimentos
    hoje = datetime.today().date()
    for linha in linhas:
        if len(linha) >= 10:
            tipo = linha[4]
            if tipo == 'investimento':
                data = datetime(int(linha[3]), int(linha[2]), int(linha[1])).date()
                tempo_dias = (hoje - data).days

                # Atualizar o montante e o rendimento
                valor = float(linha[5])
                taxa = float(linha[7])
                novo_montante = calcular_rendimento(valor, taxa, tempo_dias)
                rendimento = novo_montante - valor

                linha[8] = str(round(novo_montante, 2))
                linha[9] = str(round(rendimento, 2))

    # Escrever de volta no CSV
    with open(nome_arquivo, 'w', newline='') as file:
        csv_writer = csv.writer(file)

        # Escrever o cabeçalho
        csv_writer.writerow(header)

        # Escrever as linhas atualizadas
        csv_writer.writerows(linhas)

    return None
```
</details>
<details>
<summary><b>Função entradas():</b></summary>

- A função entradas() recebe dados e realiza o registro na base csv, a função recebe os parâmetros tipo, valor e historico, nos casos de investimento recebe támbem o parâmetro taxa.

```
def entradas(tipo=str,valor=float,historico= str, taxa=None):
    '''Lança novos registros na base CSV.'''

    with open('./bases/base.csv', 'r') as arquivo: #abre o csv como leitor
            leitor = csv.reader(arquivo, delimiter=';')
            movimentacao = list(leitor)

    #cria as variaveis dos dados

    indice= len(movimentacao)
    data = datetime.today().date().strftime("%Y-%m-%d")
    rendimento=0
    valor_corigido= lambda valor: valor*-1 if tipo == "despesa" else valor #ajustando o sinal do valor
    if tipo == "investimento":
        montante= valor
        rendimento=0
    else:
        montante= ""
        rendimento= ""

    #variavel no formato de lista para a inclusao 
    entrada_linha= [indice, int(data.split('-')[2]), int(data.split('-')[1]), int(data.split('-')[0]),tipo, valor_corigido(valor), historico, taxa, montante, rendimento]

    movimentacao.append(entrada_linha)
    
    #abre o csv como modo de gravação
    with open('./bases/base.csv', 'a', newline='') as arquivo:
        escritor = csv.writer(arquivo, delimiter=';')
        escritor.writerow(entrada_linha) #grava a linha no csv
        arquivo.close()

    return movimentacao 
```
</details>
<details>
<summary><b>Função atualizar_movimentacao():</b></summary>

- A função altera um registro na base csv a partir do id de lançamento, recebe os parâmetros indice, tipo, valor e historico, no caso de investimento recebe o parâmetro taxa.

```
def atualizar_movimentacao(indice: int, tipo:str, valor:float, historico:str, taxa:str) -> list:
    with open('./bases/base.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo, delimiter=';')
        movimentacao = list(leitor)

    if not movimentacao:
        pass

    indice = indice

    if 0 <= indice < len(movimentacao):
        tipo = tipo
        data = datetime.today().date().strftime("%Y-%m-%d")

        if tipo.lower() == 'despesa':
            valor = float(-valor)
            montante = 0
            taxa = 0
            rendimento = 0
            historico = historico
        elif tipo.lower() == 'investimento':
            valor = float(valor)
            taxa = float(taxa)
            tempo_dias = (datetime.today().date() - datetime.strptime(data, "%Y-%m-%d").date())
            montante = round(valor * (1 + taxa) ** tempo_dias.days, 2)
            rendimento = round(montante - valor, 2)
            historico = historico
        else:
            valor = float(valor)
            montante = 0
            taxa = 0
            rendimento = 0
            historico = historico

        if tipo.lower() == 'investimento':
            movimentacao[indice] = [
                str(indice), str(int(data.split('-')[2])),
                str(int(data.split('-')[1])),
                str(int(data.split('-')[0])),
                tipo, valor, historico, taxa,
                montante, rendimento]
        else:
            movimentacao[indice] = [
                str(indice), str(int(data.split('-')[2])),
                str(int(data.split('-')[1])),
                str(int(data.split('-')[0])),
                tipo, valor, historico, '', '', '']
            
        # Salva as alterações no arquivo CSV
        with open('./bases/base.csv', 'w', newline='') as novo_arquivo:
            escritor = csv.writer(novo_arquivo, delimiter=';')
            escritor.writerows(movimentacao)

    return movimentacao
```
</details>
<details>
<summary><b>Função consultar_por_data():</b></summary>

- A função recebe dois parâmetros de data no fromato string 'dd/mm/aaaa' e utiliza a função auxiliar consultar() para acessar a base de dados e aplicar o filtro.

```
def consultar_por_data(data_consulta_inicio: str, data_consulta_fim: str) -> list:
    '''A função consulta o lançamento conforme a data.'''
    data_inicio = datetime.strptime(data_consulta_inicio, "%d/%m/%Y").date()
    data_fim = datetime.strptime(data_consulta_fim, "%d/%m/%Y").date()
    return consultar(lambda linha: datetime(int(linha[3]), int(linha[2]), int(linha[1])).date() >= data_inicio and datetime(int(linha[3]), int(linha[2]), int(linha[1])).date() <= data_fim)
```
</details>
<details>
<summary><b>Função consultar_por_tipo():</b></summary>

- A função recebe o parâmetro tipo_consulta no formato string e utiliza a função auxiliar consultar() para acessar a base de dados e aplicar o filtro.

```
def consultar_por_tipo(tipo_consulta: str) -> list:
    '''A função consulta os lançamentos conforme tipo de lançamento.'''
    return consultar(lambda linha: linha and len(linha) >= 5 and linha[4] == tipo_consulta)
```

</details>
<details>
<summary><b>Função consultar_por_historico():</b></summary>

- A função recebe o parâmetro historico_consulta no formato string e utiliza a função auxiliar consultar() para acessar a base de dados e aplicar o filtro.

```
def consultar_por_historico(historico_consulta: str) -> list:
    '''A função consulta os lançamentos conforme historico de lançamento.'''
    return consultar(lambda linha: linha and len(linha) >= 7 and linha[6] == historico_consulta)
```

</details>
<details>
<summary><b>Função consultar_por_id():</b></summary>

- A função recebe dois parâmetros id_consulta_inicio e id_consulta_final em formato de string e usa a função auxiliar consultar() para acessar a base de dados e aplicar o filtro.

```
def consultar_por_id(id_consulta_inicio: str, id_consulta_final: str) -> list:
    '''A função consulta os lançamentos conforme o id de lançamento.'''
    return consultar(lambda linha: linha and len(linha) >= 1 and id_consulta_inicio <= int(linha[0]) <= id_consulta_final)
```
</details>
<details>
<summary><b>Função consultar_por_valor():</b></summary>

- A função recebe dois parâmetros valor_consulta_inicio e valor_consulta_fim em formato de string e usa a função auxiliar consultar() para acessar a base de dados e aplicar o filtro.

```
def consultar_por_valor(valor_consulta_inicio: str, valor_consulta_fim: str) -> list:
    '''A função consulta os lançamentos conforme o valor de lançamento.'''
    return consultar(lambda linha: linha and len(linha) >= 5 and float(linha[5]) >= float(valor_consulta_inicio) and float(linha[5]) <= float(valor_consulta_fim))
```
</details>
<details>
<summary><b>Função consultar():</b></summary>

- A função auxilia na consulta a base de dados, ela recebe uma função como parametro e realiza o filtro e retorna a consulta da base.

```
def consultar(condicao: callable) -> list:
    '''A função é uma função auxiliar que recebe a base e uma condição
    (expressa como uma função lambda) e retorna os registros que atendem à condição.'''
    
    # Armazena os registros da consulta
    registros_encontrados = []
    
    # Acessa a base
    with open('./bases/base.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo, delimiter=';')
        next(leitor)
        
        # Itera e adiciona a lista os registros encontrados na consulta
        for linha in leitor:
            if condicao(linha):
                registros_encontrados.append(linha)

    return registros_encontrados
```
</details>
<details>
<summary><b>Função agrupar_por():</b></summary>

- A função agrupa os valores disponiveis na base de dados conforme o criterio informado como string.

```
def agrupar_por(criterio: str) -> dict:
    '''Função para agrupar o total de valores com base em um critério específico.'''
    
    # Acessando base
    base = './bases/base.csv'
    
    # Carregar a base existente
    with open(base, 'r') as arquivo:
        leitor = csv.reader(arquivo, delimiter=';')
        tabela = list(leitor)

    # Identificar o índice da coluna correspondente ao critério
    cabecalho = tabela[0]
    indice_criterio = cabecalho.index(criterio.strip().lower())

    # Inicializar o dicionário para armazenar os totais
    totais_por_categoria = {}

    # Calcular os totais com base no critério
    for linha in tabela[1:]:
        categoria = linha[indice_criterio]
        valor = float(linha[5])  # Índice 5 corresponde à coluna 'valor'

        if categoria not in totais_por_categoria:
            totais_por_categoria[categoria] = 0

        totais_por_categoria[categoria] += valor
    
    return totais_por_categoria
```

</details>
<details>
<summary><b>Função exporta_csv():</b></summary>

- A função faz uma consulta consulta se já existe o arquivo 'arquivo.csv' no repositorio 'bases', se exitir ele é substituido pelo novo arquivo gerado pela função, o arquivo é gerado a partir do resultado da função consulta().

```
def exporta_csv(resultados: list) -> None:
    '''A função exporta um arquivo csv conforme consulta.'''
    if os.path.exists('./bases/arquivo.csv'):
        os.remove('./bases/arquivo.csv')
        with open('./bases/arquivo.csv', 'w', newline='') as novo_arquivo:
            escritor = csv.writer(novo_arquivo, delimiter=';')
            registros = resultados
            escritor.writerows(registros)
    else:
        with open('./bases/arquivo.csv', 'w', newline='') as novo_arquivo:
            escritor = csv.writer(novo_arquivo, delimiter=';')
            registros = resultados
            escritor.writerows(registros)
    
    return None
```
</details>
<details>
<summary><b>Função excluir_lancamento():</b></summary>

- A função recebe o número do id de lançamento e procura, caso exista será excluido e a base será atualizada.

```
def exclui_lancamento(numero_lancamento: int) -> list:
    '''A função exclui o lançamento conforme o número do lançamento da coluna ID_lançamento'''

    # Ler todo o conteúdo do arquivo
    with open('./bases/base.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo, delimiter=';')
        linhas = list(leitor)

    # Procurar o índice do registro com base no número de lançamento
    indice_exclusao = None
    for i, linha in enumerate(linhas):
        if linha and linha[0] == str(numero_lancamento):
            indice_exclusao = i
            break

    # Verificar se o registro foi encontrado antes de excluí-lo
    if indice_exclusao is not None:
        # Excluir o registro encontrado
        registro_excluido = linhas.pop(indice_exclusao)

        # Escrever as linhas atualizadas de volta ao arquivo
        with open('./bases/base.csv', 'w', newline='') as arquivo:
            escritor = csv.writer(arquivo, delimiter=';')
            escritor.writerows(linhas)

    return registro_excluido
```
</details>
<details>
<summary><b>Função menu_principal():</b></summary>

- A função auxilia na interação do usuário com a aplicação oferecendo um menu principal para iniciar a navegação, essa função chama todas as outras funções de menu secundários.

```
def menu_principal() -> None:
    '''Função para executar o menu principal e os demais menus.'''
    executa_programa = True
    while executa_programa:
        # Menu principal
        print('*'*80,'\n')
        print(' '*32,'Seja Bem-Vindo!\n')
        print(' '*25,'Sistema de Gestão Financeira\n')
        print(' '*31,'CONTROL FINANCE\n')
        print('\n','*'*80,'\n')
        print('''
        Selecione uma das opções a seguir:
              
        [ 1 ] - adicionar lançamentos.
        [ 2 ] - consultar lançamentos.
        [ 3 ] - gerar relatórios agrupados.
        [ 4 ] - exportar relatório.
        [ 5 ] - alterar registro.
        [ 6 ] - excluir registro.
        [ 0 ] - fechar o programa.''')
        print()
        opcao = int(input('Digite a opção: '))

        if opcao == 0:
            print('\nPrograma encerrado! Volte sempre!\n')
            sys.exit()

        if opcao == 1:
            menu_opcao_1()

        elif opcao == 2:
            menu_opcao_2()

        elif opcao == 3:
            menu_opcao_3()

        elif opcao == 4:
            menu_opcao_4()

        elif opcao == 5:
            menu_opcao_5()

        elif opcao == 6:
            menu_opcao_6()

        else:
            print('\nOpção inválida. Tente novamente.\n')
```
</details>
<details>
<summary><b>Função menu_opcao_1():</b></summary>

- A função auxilia na interação com o menu 'Adiciona Lançamento'.

```
def menu_opcao_1() -> None:
    '''Função para executar o menu de lançamento de registro financeiro.'''
    while True:
        # Menu opção 1
        print('*'*80,'\n')
        print(' '*30,'Adicionar Lançamentos')
        print('\n','*'*80,'\n')
        print('''
        Selecione uma opção a seguir:
        
        [ 1 ] - realizar lançamento.
        [ 0 ] - voltar ao menu.''')
        print()
        opcao = int(input('Digite a opção: '))

        if opcao == 1:
            tipo = input("Digite um tipo (receita/despesa/investimento): ").lower()
            if tipo == 'investimento':
                valor = round(float(input("Digite o valor: ").replace(',','.')),2)
                historico = input("Digite o historico do lançamento: ").lower()
                taxa = round(float(input("Digite a taxa diária: ").replace(',','.')),4)
                entradas(tipo=tipo,valor=valor,historico=historico, taxa=taxa)
                arquivo = open('./bases/base.csv', 'r')
                consulta_lancamento = csv.reader(arquivo, delimiter=';')
                consulta_lancamento = list(consulta_lancamento)[-1]
                arquivo.close() 
                print("\nLançamento realizado:\n")
                print("Número de Lançamento:", consulta_lancamento[0])
                print(f"Data: {consulta_lancamento[1]}/{consulta_lancamento[2]}/{consulta_lancamento[3]}")
                print("Tipo:", consulta_lancamento[4])
                print(f"Valor: {float(consulta_lancamento[5]):.2f}")
                print("Histórico:", consulta_lancamento[6])
                print(f"Taxa: {float(consulta_lancamento[7]):.4f}")
                print("Acumulado:", consulta_lancamento[8])
                print("Rendimento:", consulta_lancamento[9])

            else:
                valor = round(float(input("Digite o valor: ").replace(',','.')),2)
                historico = input("Digite o historico do lançamento: ").lower()
                entradas(tipo=tipo,valor=valor,historico=historico, taxa="")
                arquivo = open('./bases/base.csv', 'r')
                consulta_lancamento = csv.reader(arquivo, delimiter=';')
                consulta_lancamento = list(consulta_lancamento)[-1]
                arquivo.close() 
                print("\nLançamento realizado:\n")
                print("Número de Lançamento:", consulta_lancamento[0])
                print(f"Data: {consulta_lancamento[1]}/{consulta_lancamento[2]}/{consulta_lancamento[3]}")
                print("Tipo:", consulta_lancamento[4])
                print(f"Valor: {float(consulta_lancamento[5]):.2f}")
                print("Histórico:", consulta_lancamento[6])

        elif opcao == 0:
            break

        else:
           print('\nOpção inválida. Tente novamente.\n')
```
</details>
<details>
<summary><b>Função menu_opcao_2():</b></summary>

- A função auxilia na interação com o menu 'Consultar Lançamento'.

```
def menu_opcao_2() -> None:
    '''Função para executar o menu de consultas dos lançamento financeiro.'''
    while True:
        # Menu opção 2
        print('*'*80,'\n')
        print(' '*30,'Consultar Lançamentos')
        print('\n','*'*80,'\n')
        print('''
        Selecione uma opção de consulta a seguir:

        [ 1 ] - consultar por datas.
        [ 2 ] - consultar por tipo de lançamentos.
        [ 3 ] - consultar por valores.
        [ 4 ] - consultar por históricos.
        [ 5 ] - consultar por IDs de lançamentos.
        [ 0 ] - voltar ao menu.''')
        print()
        opcao = int(input('Digite a opção: '))

        if opcao == 1:
            # Solicitar a data para consulta
            print("\nDigite o intervalo de datas no formato dd/mm/aaaa.")
            data_inicio = input("Data inicial: ")
            data_final = input("Data final: ")
            resultado_data = consultar_por_data(data_inicio, data_final)
            if len(resultado_data) > 0:
                print("\nResultados encontrados:\n")
                for i in range(len(resultado_data)):
                    if resultado_data[i][4] == 'investimento':
                        print("Número de Lançamento:", resultado_data[i][0])
                        print(f"Data: {resultado_data[i][1]}/{resultado_data[i][2]}/{resultado_data[i][3]}")
                        print("Tipo:", resultado_data[i][4])
                        print(f"Valor: {float(resultado_data[i][5]):.2f}")
                        print("Histórico:", resultado_data[i][6])
                        print(f"Taxa: {float(resultado_data[i][7]):.4f}")
                        print(f"Acumulado: {float(resultado_data[i][8]):.2f}")
                        print(f"Rendimento: {float(resultado_data[i][9]):.2f}")
                        print('-'*5)
                    else:
                        print("Número de Lançamento:", resultado_data[i][0])
                        print(f"Data: {resultado_data[i][1]}/{resultado_data[i][2]}/{resultado_data[i][3]}")
                        print("Tipo:", resultado_data[i][4])
                        print(f"Valor: {float(resultado_data[i][5]):.2f}")
                        print("Histórico:", resultado_data[i][6])
                        print('-'*5)

            else:
                # Se a data não for encontrada
                print("\nNenhum registro encontrado! Verifique os dados informados.\n")

        elif opcao == 2:
            # Solicitar o tipo para consulta
            tipo_consulta = input("Digite o tipo para consulta (receita/despesa/investimento): ").lower()
            resultado_tipo = consultar_por_tipo(tipo_consulta)
            if len(resultado_tipo) > 0:
                print("\nResultados encontrados:\n")
                for i in range(len(resultado_tipo)):
                    if resultado_tipo[i][4] == 'investimento':
                        print("Número de Lançamento:", resultado_tipo[i][0])
                        print(f"Data: {resultado_tipo[i][1]}/{resultado_tipo[i][2]}/{resultado_tipo[i][3]}")
                        print("Tipo:", tipo_consulta)
                        print(f"Valor: {float(resultado_tipo[i][5]):.2f}")
                        print("Histórico:", resultado_tipo[i][6])
                        print(f"Taxa: {float(resultado_tipo[i][7]):.4f}")
                        print(f"Acumulado: {float(resultado_tipo[i][8]):.2f}")
                        print(f"Rendimento: {float(resultado_tipo[i][9]):.2f}")
                        print('-'*5)
                    else:
                        print("Número de Lançamento:", resultado_tipo[i][0])
                        print(f"Data: {resultado_tipo[i][1]}/{resultado_tipo[i][2]}/{resultado_tipo[i][3]}")
                        print("Tipo:", tipo_consulta)
                        print(f"Valor: {float(resultado_tipo[i][5]):.2f}")
                        print("Histórico:", resultado_tipo[i][6])
                        print('-'*5)

            else:
                # Se o tipo não for encontrado
                print("\nNenhum registro encontrado! Verifique os dados informados.\n")
            
        elif opcao == 3:
            # Solicitar o valor para consulta
            print("\nDigite o intervalo de valores para consulta.")
            valor_inicio = float(input("Valor inicial: "))
            valor_fim = float(input("Valor final: "))
            resultado_valor = consultar_por_valor(valor_inicio, valor_fim)
            if len(resultado_valor) > 0:
                print("\nResultados encontrados:\n")
                for i in range(len(resultado_valor)):
                    if resultado_valor[i][4] == 'investimento':
                        print("Número de Lançamento:", resultado_valor[i][0])
                        print(f"Data: {resultado_valor[i][1]}/{resultado_valor[i][2]}/{resultado_valor[i][3]}")
                        print("Tipo:", resultado_valor[i][4])
                        print(f"Valor: {float(resultado_valor[i][5]):.2f}")
                        print("Histórico:", resultado_valor[i][6])
                        print(f"Taxa: {float(resultado_valor[i][7]):.4f}")
                        print(f"Acumulado: {float(resultado_valor[i][8]):.2f}")
                        print(f"Rendimento: {float(resultado_valor[i][9]):.2f}")
                        print('-'*5)
                    else:
                        print("Número de Lançamento:", resultado_valor[i][0])
                        print(f"Data: {resultado_valor[i][1]}/{resultado_valor[i][2]}/{resultado_valor[i][3]}")
                        print("Tipo:", resultado_valor[i][4])
                        print(f"Valor: {float(resultado_valor[i][5]):.2f}")
                        print("Histórico:", resultado_valor[i][6])
                        print('-'*5)

            else:
                # Se o valor não for encontrado
                print("\nNenhum registro encontrado! Verifique os dados informados.\n")
 
        elif opcao == 4:
            # Solicitar o valor para consulta
            historico_consulta = input("Digite o historico: ").lower()
            resultado_historico = consultar_por_historico(historico_consulta)
            if len(resultado_historico) > 0:
                print("\nResultados encontrados:\n")
                for i in range(len(resultado_historico)):
                    if resultado_historico[i][4] == 'investimento':
                        print("Número de Lançamento:", resultado_historico[i][0])
                        print(f"Data: {resultado_historico[i][1]}/{resultado_historico[i][2]}/{resultado_historico[i][3]}")
                        print("Tipo:", resultado_historico[i][4])
                        print(f"Valor: {float(resultado_historico[i][5]):.2f}")
                        print("Histórico:", resultado_historico[i][6])
                        print(f"Taxa: {float(resultado_historico[i][7]):.4f}")
                        print(f"Acumulado: {float(resultado_historico[i][8]):.2f}")
                        print(f"Rendimento: {float(resultado_historico[i][9]):.2f}")
                        print('-'*5)
                    else:
                        print("Número de Lançamento:", resultado_historico[i][0])
                        print(f"Data: {resultado_historico[i][1]}/{resultado_historico[i][2]}/{resultado_historico[i][3]}")
                        print("Tipo:", resultado_historico[i][4])
                        print(f"Valor: {float(resultado_historico[i][5]):.2f}")
                        print("Histórico:", resultado_historico[i][6])
                        print('-'*5)

            else:
                # Se o valor não for encontrado
                print("\nNenhum registro encontrado! Verifique os dados informados.\n")

        elif opcao == 5:
            # Solicitar o valor para consulta
            print("\nDigite o intervalo de IDs.")
            id_inicio_consulta = int(input("Inicio: "))
            id_fim_consulta = int(input("Fim: "))
            resultado_id = consultar_por_id(id_inicio_consulta, id_fim_consulta)
            if len(resultado_id) > 0:
                print("\nResultados encontrados:\n")
                for i in range(len(resultado_id)):
                    if resultado_id[i][4] == 'investimento':
                        print("Número de Lançamento:", resultado_id[i][0])
                        print(f"Data: {resultado_id[i][1]}/{resultado_id[i][2]}/{resultado_id[i][3]}")
                        print("Tipo:", resultado_id[i][4])
                        print(f"Valor: {float(resultado_id[i][5]):.2f}")
                        print("Histórico:", resultado_id[i][6])
                        print(f"Taxa: {float(resultado_id[i][7]):.4f}")
                        print(f"Acumulado: {float(resultado_id[i][8]):.2f}")
                        print(f"Rendimento: {float(resultado_id[i][9]):.2f}")
                        print('-'*5)
                    else:
                        print("Número de Lançamento:", resultado_id[i][0])
                        print(f"Data: {resultado_id[i][1]}/{resultado_id[i][2]}/{resultado_id[i][3]}")
                        print("Tipo:", resultado_id[i][4])
                        print(f"Valor: {float(resultado_id[i][5]):.2f}")
                        print("Histórico:", resultado_id[i][6])
                        print('-'*5)

            else:
                # Se o intervalo de IDs não forem encontrados
                print("\nNenhum registro encontrado! Verifique os dados informados.\n")
            
        elif opcao == 0:
            break

        else:
            print('\nOpção inválida. Tente novamente.\n')
```
</details>
<details>
<summary><b>Função menu_opcao_3():</b></summary>

- A função auxilia na interação com o menu 'Relatórios Agrupados'.

```
def menu_opcao_3() -> None:
    while True:
        # Menu opção 3
        print('*'*80,'\n')
        print(' '*30,'Relatórios Agrupados')
        print('\n','*'*80,'\n')
        print('''
        Selecione uma opção a seguir:

        [ 1 ] - agrupar por Tipo.
        [ 2 ] - agrupar por Mês.
        [ 3 ] - agrupar por histórico.
        [ 0 ] - voltar ao menu.''')
        print()
        opcao = int(input('Digite a opção: '))
    
        if opcao == 1:
            # Agrupar por tipo
            criterio_agrupamento = 'tipo'        
            resultado_agrupamento = agrupar_por(criterio_agrupamento)
            print("\nRelatório Totais Agrupados por Tipo de Lançamento.\n")
            for chave, valor in resultado_agrupamento.items():
                print(f"{chave.upper()}: {valor}")
            print('-'*5)
             
        elif opcao == 2:
            # Agrupar por Mês
            criterio_agrupamento = 'mes'        
            resultado_agrupamento = agrupar_por(criterio_agrupamento)
            locale.setlocale(locale.LC_TIME, 'pt_BR')
            print("\nRelatório Totais Agrupados por Mês.\n")
            for mes in range(1, 13):
                total_mes = resultado_agrupamento.get(str(mes), 0)
                nome_mes = calendar.month_name[mes]
                print(f"{nome_mes.upper()}: {float(total_mes):.2f}")
            print('-'*5)

        elif opcao == 3:
            # Agrupar por Mês
            criterio_agrupamento = 'historico'        
            resultado_agrupamento = agrupar_por(criterio_agrupamento)
            print("\nRelatório Totais Agrupados por Históricos.\n")
            for chave, valor in resultado_agrupamento.items():
                print(f"{chave.upper()}: {valor}")
            print('-'*5)

        elif opcao == 0:
            break

        else:
            print('\nOpção inválida. Tente novamente.\n')
```
</details>
<details>
<summary><b>Função menu_opcao_4():</b></summary>

- A função auxilia na interação com o menu 'Exportar Relatório CSV'.

```
def menu_opcao_4() -> None:
    '''Função para executar o menu de exportação de relatório dos registro financeiro
    a partir de consultas.'''

    while True:
        print('*'*80,'\n')
        print(' '*30,'Exportar Relatórios CSV')
        print('\n','*'*80,'\n')
        print('''
        Selecione uma opção a seguir:

        [ 1 ] - exportar relatório por datas.
        [ 2 ] - exportar relatório por tipo.
        [ 3 ] - exportar relatório por valor.
        [ 4 ] - exportar relatório por histórico.
        [ 5 ] - exportar relatório por por IDs.
        [ 0 ] - voltar ao menu.\n''')

        opcao = int(input('Digite a opção: '))

        if opcao == 1:
            # Solicitar a data para consulta e exportar o relatório
            print("\nDigite o intervalo de datas no formato dd/mm/aaaa.")
            data_inicio = input("Data inicial: ")
            data_final = input("Data final: ")
            resultado_data = consultar_por_data(data_inicio, data_final)
            resultado_data_csv = [['ID_lancamento', 'dia', 'mes', 'ano', 'tipo', 'valor', 
                                    'historico', 'taxa', 'montante', 'rendimento']]
            resultado_data_csv.extend(resultado_data)
            exporta_csv(resultado_data_csv)
            print(f"Relatório CSV criado ./bases/arquivo.csv")

        elif opcao == 2:
            # Solicitar o tipo para consulta
            tipo_consulta = input("Digite o tipo (receita/despesa/investimento): ").lower()
            resultado_tipo = consultar_por_tipo(tipo_consulta)
            resultado_data_csv = [['ID_lancamento', 'dia', 'mes', 'ano', 'tipo', 'valor', 
                                    'historico', 'taxa', 'montante', 'rendimento']]
            resultado_data_csv.extend(resultado_tipo)
            exporta_csv(resultado_data_csv)
            print(f"Relatório CSV criado ./bases/arquivo.csv")

        elif opcao == 3:
            # Solicitar o valor para consulta e exportar o relatório
            print("\nDigite o intervalo de valores para consulta.")
            valor_inicio = float(input("Valor inicial: "))
            valor_fim = float(input("Valor final: "))
            resultado_valor = consultar_por_valor(valor_inicio, valor_fim)
            resultado_data_csv = [['ID_lancamento', 'dia', 'mes', 'ano', 'tipo', 'valor', 
                                    'historico', 'taxa', 'montante', 'rendimento']]
            resultado_data_csv.extend(resultado_valor)
            exporta_csv(resultado_data_csv, )
            print(f"Relatório CSV criado ./bases/arquivo.csv")

        elif opcao == 4:
            historico_consulta = input("Digite o historico: ").lower()
            resultado_historico = consultar_por_historico(historico_consulta)
            resultado_data_csv = [['ID_lancamento', 'dia', 'mes', 'ano', 'tipo', 'valor', 
                                    'historico', 'taxa', 'montante', 'rendimento']]
            resultado_data_csv.extend(resultado_historico)
            exporta_csv(resultado_data_csv)
            print(f"Relatório CSV criado ./bases/arquivo.csv")

        elif opcao == 5:
            print("\nDigite o intervalo de IDs.")
            id_inicio_consulta = int(input("Inicio: "))
            id_fim_consulta = int(input("Fim: "))
            resultado_id = consultar_por_id(id_inicio_consulta, id_fim_consulta)
            resultado_data_csv = [['ID_lancamento', 'dia', 'mes', 'ano', 'tipo', 'valor', 
                                    'historico', 'taxa', 'montante', 'rendimento']]
            resultado_data_csv.extend(resultado_id)
            exporta_csv(resultado_data_csv, )
            print(f"Relatório CSV criado ./bases/arquivo.csv")

        elif opcao == 0:
            break
        
        else:
            print('\nOpção inválida. Tente novamente.\n')
```
</details>
<details>
<summary><b>Função menu_opcao_5():</b></summary>

- A função auxilia na interação com o menu 'Alterar Lançamento'.

```
def menu_opcao_5() -> None:
    '''Função para executar o menu de alterar lançamento na base de registros.'''
    while True:
        # Menu opção 5
        print('*'*80,'\n')
        print(' '*30,'Alterar Lançamentos')
        print('\n','*'*80,'\n')
        print('''
        Selecione uma opção a seguir:
        
        [ 1 ] - realizar alteração.
        [ 0 ] - voltar ao menu.\n''')

        opcao = int(input('Digite a opção: '))

        if opcao == 1:
            indice_movimentacao = int(input("\nDigite o ID do lançamento: "))
            tipo_movimentacao = input("Digite o tipo de lançamento (receita/despesa/investimento): ").lower()

            # Condição para alterar lnaçamento para investiemnto, receita ou despesa
            if tipo_movimentacao == 'investimento':
                valor_movimentacao = float(input("Digite o valor: ").replace(',','.'))
                historico_movimentacao = input("Digite o histórico: ").lower()
                taxa_movimentacao = input("Digite a taxa diária: ").replace(',','.')
                movimentacao_atualizada = atualizar_movimentacao(indice_movimentacao, tipo_movimentacao, valor_movimentacao, 
                                                                    historico_movimentacao, taxa_movimentacao)
                registro = [linha for linha in movimentacao_atualizada if str(indice_movimentacao) in linha]
                print("\nRegistro Alterado.\n")
                print("Número de Lançamento:", registro[0][0])
                print(f"Data: {registro[0][1]}/{registro[0][2]}/{registro[0][3]}")
                print("Tipo:", registro[0][4])
                print(f"Valor: {float(registro[0][5]):.2f}")
                print("Histórico:", registro[0][6])
                print(f"Taxa: {float(registro[0][7]):.4f}")
                print(f"Acumulado: {float(registro[0][8]):.2f}")
                print(f"Rendimento: {float(registro[0][9]):.2f}")
                print('-'*5)

            else:
                valor_movimentacao = float(input("Digite o valor: ").replace(',','.'))
                historico_movimentacao = input("Digite o histórico: ").lower()
                movimentacao_atualizada = atualizar_movimentacao(indice_movimentacao,tipo_movimentacao, valor_movimentacao, 
                                                                    historico_movimentacao, None)
                registro = [linha for linha in movimentacao_atualizada if str(indice_movimentacao) in linha]
                print("\nRegistro Alterado.\n")
                print("Número de Lançamento:", registro[0][0])
                print(f"Data: {registro[0][1]}/{registro[0][2]}/{registro[0][3]}")
                print("Tipo:", registro[0][4])
                print(f"Valor: {float(registro[0][5]):.2f}")
                print("Histórico:", registro[0][6])
                print('-'*5)

        elif opcao == 0:
            break

        else:
            print('\nOpção inválida. Tente novamente.\n')
```
</details>
<details>
<summary><b>Função menu_opcao_6():</b></summary>

- A função auxilia na interação com o menu 'Excluir Lançamentos'.

```
def menu_opcao_6() -> None:
    '''Função para executar o menu de exclusão de lançamento na base.'''
    while True:
        # Menu opção 6
        print('*'*80,'\n')
        print(' '*30,'Excluir Lançamentos')
        print('\n','*'*80,'\n')
        print('''
        Selecione uma opção a seguir:
        
        [ 1 ] - excluir lançamento.
        [ 0 ] - voltar ao menu.\n''')

        opcao = int(input('Digite a opção: '))         
            
        if opcao == 1:    
            # Solicitar o número de lançamento para excluir
            numero_lancamento_excluir = int(input("\nDigite o número de lançamento para excluir: "))
            registro_excluido = exclui_lancamento(numero_lancamento_excluir)
            print("\nRegistro excluído:\n")
            print("Número de Lançamento:", registro_excluido[0])
            print("Data:", f"{registro_excluido[1]}/{registro_excluido[2]}/{registro_excluido[3]}")
            print("Tipo:", registro_excluido[4])
            print("Valor:", registro_excluido[5])
            print("Histórico:", registro_excluido[6])

        elif opcao == 0:
            break

        else:
            print('\nOpção inválida. Tente novamente.\n')
```
</details>
<details>
<summary><b>Função main()</b></summary>

- Possibilita o funcionamento da aplicação.

```
def main():
    '''Função para executar o programa.'''
    while True:
        # Criar a base CSV
        cria_base_csv()

        # Atualizar rendimentos no CSV
        atualizar_rendimentos_csv()

        # Menu principal
        menu_principal()
```
</details>
