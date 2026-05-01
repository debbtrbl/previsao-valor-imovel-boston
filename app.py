# Deploy da aplicação

# importações
import pandas as pd
import streamlit as st
import plotly.express as px
import joblib
from sklearn.ensemble import RandomForestRegressor

# função pra carregar os dados
@st.cache_data
def get_data():
    return pd.read_csv('data.csv')

# função para treinar o modelo
@st.cache_resource
def load_model():
    return joblib.load('modelo_rf_regressor_boston.pkl')


data = get_data() # criando dataframe
model = load_model() # carregando o modelo treinado

#titulo
st.title("Boston Housing AI - Prevendo valores de imóveis")

#subtitulo
st.markdown("Este é um Data App utilizado para exibir a solução de Machine Learning para o problema de predição de valores de imóveis com o dataset Boston House Prices do MIT.")

#verificando o dataset
st.subheader("Selecionando apenas um pequeno conjunto de atributos")

#atributos para serem exibidos por padrão
defaultcols = ['RM','PTRATIO','CRIM','MEDV']

#definindo atrivutos a partirt do multiselect
cols = st.multiselect('Atributos', data.columns.tolist(), default=defaultcols)


#exibindo os top 10 registros
st.dataframe(data[cols].head(10))

st.subheader('Distribuição de imóveis por preço')

#definindo a faixa de valores
faixa_valores = st.slider('Faixa de preço', float(data.MEDV.min()), 150., (10.0, 100.0))

#filtrando os dados
dados = data[data['MEDV'].between(left=faixa_valores[0], right=faixa_valores[1])]

#plot da distribuição dos dados
f = px.histogram(dados, x='MEDV', nbins=100, title='Distribuição de Preços')
f.update_xaxes(title='MEDV')
f.update_yaxes(title='Total imóveis')
st.plotly_chart(f)

st.sidebar.subheader('Defina os atributos dos imoveis para predição')

#mapeando dados do usuario para cada atributo
crim = st.sidebar.number_input('Taxa de criminalidade', value=data.CRIM.mean())
indus = st.sidebar.number_input("Proporção de hectares de Industrias", value=data.INDUS.mean())
chas = st.sidebar.selectbox('Faz limite com o rio?', ('Sim', 'Não'))

#transformando o dado de entrada em binario
chas = 1 if chas == "Sim" else 0

nox = st.sidebar.number_input('Concentração de oxico nitrico', value=data.NOX.mean())

rm = st.sidebar.number_input('Número de quartos', value=1)

ptratio = st.sidebar.number_input('Índice de alunos por professores', value=data.PTRATIO.mean())

#botao de predição
btn_predict = st.sidebar.button('Realizar predição')

#verificar se o botao foi acionado
if btn_predict:
    result = model.predict([[crim, indus, chas, nox, rm, ptratio]])
    st.subheader('O valor previsto para o imóvel é: ')
    result = 'US $ '+str(round(result[0]*10,2))
    st.write(result)
