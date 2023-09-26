import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 7})
'''
Iremos fazer um projeto com base no Banco de dados da marvel, onde iremos dividir entre masculino e feminino, com o objetivo de ver quais personagens vieram antes, quais morreram mais e quais reviveram mais
'''

df = pd.read_csv('avengers.csv', encoding="latin-1")

df = df[df['Name/Alias'].notna()]


male_characters = df[df['Gender'] == 'MALE']
female_characters = df[df['Gender'] == 'FEMALE']


sorted_male_characters = male_characters.sort_values(by='Years since joining')

sorted_female_characters = female_characters.sort_values(by='Years since joining')

male_years_since_joining_values = sorted_male_characters['Years since joining'].tolist()
female_years_since_joining_values = sorted_female_characters['Years since joining'].tolist()

male_character_names = sorted_male_characters['Name/Alias'].tolist()
female_character_names = sorted_female_characters['Name/Alias'].tolist()

#imprimir personagens masculinos desde que foram lançados
plt.plot(male_character_names, male_years_since_joining_values)

plt.xlabel('Nome do Vingador')
plt.ylabel('Anos desde o lançamento')
plt.title('Vingadores masculinos - Anos desde o lançamento')

plt.xticks(rotation='vertical')
plt.show()

#imprimir personagens feinimos desde que foram lançados

plt.plot(female_character_names, female_years_since_joining_values)

plt.xlabel('Nome do Vingador')
plt.ylabel('Anos desde o lançamento')
plt.title('Vingadores femininos - Anos desde o lançamento')

plt.xticks(rotation='vertical')
plt.show()

#Trecho para imprimir quantidade de vezes que o personagem morreu divido por genero
# Função para contar "YES" nas colunas de morte e agrupar os nomes
def count_and_group_deaths(dataframe):
    dataframe['Total Deaths'] = dataframe[['Death1', 'Death2', 'Death3', 'Death4', 'Death5']].apply(lambda row: row.str.count('YES')).sum(axis=1)
    grouped_data = dataframe.groupby(['Name/Alias'])['Total Deaths'].sum().reset_index()
    return grouped_data

# Conte e agrupe as mortes para personagens masculinos
grouped_male_characters = count_and_group_deaths(male_characters)

# Conte e agrupe as mortes para personagens femininos
grouped_female_characters = count_and_group_deaths(female_characters)

# Combine os DataFrames de personagens masculinos e femininos
combined_data = grouped_male_characters.merge(grouped_female_characters, on='Name/Alias', how='outer', suffixes=('_Male', '_Female'))

# Preencha valores nulos (NaN) com 0
combined_data.fillna(0, inplace=True)

# Crie o gráfico de barras
plt.figure(figsize=(12, 6))
plt.bar(combined_data['Name/Alias'], combined_data['Total Deaths_Male'], label='Masculino', alpha=0.7)
plt.bar(combined_data['Name/Alias'], combined_data['Total Deaths_Female'], label='Feminino', alpha=0.7, bottom=combined_data['Total Deaths_Male'])

# Defina o título e rótulos dos eixos
plt.title('Quantidade de Mortes por Personagem e Gênero')
plt.xlabel('Personagem')
plt.ylabel('Quantidade de Mortes')

# Rotação dos nomes no eixo x para melhor legibilidade
plt.xticks(rotation=90, fontsize=8)

# Adicione uma legenda
plt.legend()

# Mostre o gráfico
plt.tight_layout()
plt.show()

#Trecho para imprimir quantidade de vezes que o personagem retornou dos mortos divido por genero
# Função para contar "YES" nas colunas de retorno e agrupar os nomes
def count_and_group_returns(dataframe):
    return_columns = ['Return1', 'Return2', 'Return3', 'Return4', 'Return5']
    dataframe['Total Returns'] = dataframe[return_columns].apply(lambda row: row.str.count('YES')).sum(axis=1)
    grouped_data = dataframe.groupby(['Name/Alias'])['Total Returns'].sum().reset_index()
    return grouped_data

# Conte e agrupe os retornos para personagens masculinos
grouped_male_characters = count_and_group_returns(male_characters)

# Conte e agrupe os retornos para personagens femininos
grouped_female_characters = count_and_group_returns(female_characters)

# Combine os DataFrames de personagens masculinos e femininos
combined_data = grouped_male_characters.merge(grouped_female_characters, on='Name/Alias', how='outer', suffixes=('_Male', '_Female'))

# Preencha valores nulos (NaN) com 0
combined_data.fillna(0, inplace=True)

# Crie o gráfico de barras
plt.figure(figsize=(12, 6))
plt.bar(combined_data['Name/Alias'], combined_data['Total Returns_Male'], label='Male', alpha=0.7)
plt.bar(combined_data['Name/Alias'], combined_data['Total Returns_Female'], label='Female', alpha=0.7, bottom=combined_data['Total Returns_Male'])

# Defina o título e rótulos dos eixos
plt.title('Quantidade de "YES" por Personagem e Gênero')
plt.xlabel('Personagem')
plt.ylabel('Quantidade de "YES"')

# Rotação dos nomes no eixo x para melhor legibilidade
plt.xticks(rotation=90, fontsize=8)

# Adicione uma legenda
plt.legend()

# Mostre o gráfico
plt.tight_layout()
plt.show()


