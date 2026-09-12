import pandas as pd
from IPython.display import display
cadastro_clientes = pd.read_csv(r'CadastroClientes.csv',sep=';',decimal=',')
cadastro_funcionarios = pd.read_csv(r'CadastroFuncionarios.csv',sep=';',decimal=',')
base_servicos_prest = pd.read_excel(r'BaseServiçosPrestados.xlsx',decimal=',')

#Calcula o Gasto Total salarial de cada funcionário da empresa
calc_gasto_func = cadastro_funcionarios['Salario Base'] + cadastro_funcionarios['Impostos'] + cadastro_funcionarios['Beneficios'] + cadastro_funcionarios['VT'] + cadastro_funcionarios['VR']

#transforma em um Dataframe de Fácil Visualização
total_gastos_func = pd.DataFrame({"Nome Funcionário": cadastro_funcionarios["Nome Completo"],
    "Gasto Total": calc_gasto_func})
display(total_gastos_func)

#Calcular o faturamento Total da empresa = Fórmula = Cadastro_clientes['Valor do contrato mensal'] * Base_servicos_prest['Tempo Total de Contrato (Meses)']
calc_fat_total = cadastro_clientes['Valor Contrato Mensal'] * base_servicos_prest['Tempo Total de Contrato (Meses)']
calc_fat_total = calc_fat_total.sum()
print(f'Faturamento Total da Empresa: R$ {calc_fat_total}')

# % Funcionários que já fecharam algum contrato
calc_func_fecha_contratos = base_servicos_prest['ID Funcionário'].nunique() / len(cadastro_funcionarios['Nome Completo'])
print(f'Porcentagem de funcionários que ja fecharam Contratos {calc_func_fecha_contratos :.2%}')

#Total Contratos Fechados Por Cada Àrea da Empresa
base_com_areas = base_servicos_prest.merge(
    cadastro_funcionarios[["ID Funcionário", "Area"]],
    on="ID Funcionário"
)
contratos_por_area = base_com_areas["Area"].value_counts()
display(contratos_por_area)

#Quantidade de funcionários por área
qtd_func_por_area = cadastro_funcionarios["Area"].value_counts().reset_index()
qtd_func_por_area.columns = ["AREAS","QUANTIDADE FUNCIONÁRIOS"]
display(qtd_func_por_area)

#Faturamento Médio mensal
faturamento_medio_mensal = cadastro_clientes["Valor Contrato Mensal"].mean()
print(f'Faturamento Médio Mensal R$ {faturamento_medio_mensal:.2f}')










