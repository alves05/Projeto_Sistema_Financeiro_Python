
# Gerenciador financeiro em Python

## Contextualização

O controle financeiro é uma parte crucial da gestão de recursos de qualquer negócio ou indivíduo. Este projeto visa fornecer uma solução eficaz para o gerenciamento de transações financeiras, permitindo ao usuário Criar, Ler, Atualizar e Deletar registros de entradas, saídas e saldo corrente de investimentos realizados

## Objetivo do projeto

Desenvolver um sistema para controle financeiro que receba as movimentações e as armazene em um arquivo .csv ou .json, com importação dos lançamentos originais (se existentes) e possibilidade de exportação do arquivo com todo o histórico de lançamentos realizados pelo usuário

## Proposta de solução

O sistema proposto será capaz de realizar as seguintes operações:

### 1. Criar novos registros

Os registros devem possuir a data em que foram realizados, o tipo de movimentação e valor. Os tipos podem ser despesas, receita ou investimento:

-   No caso de receita, o valor inserido deverá ser positivo e armazenado normalmente neste formato;
-   No caso de despesas, o valor deve ser recebido como positivo mas armazenado como negativo;
-   No caso de investimento deve ter uma informação a mais de ‘montante’, em que será calculado quanto o dinheiro rendeu desde o dia em que foi investido. Para essa finalidade foi utilizada a seguinte fórmula.

	M=C∗(1+i)***t* em que:
	
	**M** é o Montante  
	**C** é o Capital  
	**i** é a Taxa do investimento  
	**t** é o Tempo  

### 2. Ler registros

Deverá ser possível consultar os registros por data, tipo ou valor.

### 3. Atualizar registros

No caso de atualização, pode-se atualizar o valor, o tipo e a data deverá ser a de atualização do registro.

### 4. Deletar registros

Deverá ser possível deletar o registro.

##### Módulos e bibliotecas utilizados
[csv](https://docs.python.org/3/library/csv.html)  
[datetime](https://docs.python.org/3/library/datetime.html)  
[os](https://docs.python.org/3/library/os.html)  
[random](https://docs.python.org/3/library/random.html)  

##### Membros do grupo:
[Augusto Messias](https://github.com/mineironovale)  
[Humberto Tiggemann](https://github.com/HumbertoTiggemann)  
[Tamires Souza](https://github.com/tamiresouza)  
[Wiliams Alves](https://github.com/alves05)  

![Fluxo logica](/outros/logica_contro_lfinance.jpg) 