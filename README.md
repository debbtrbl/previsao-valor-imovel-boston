# 🏠 Boston Housing AI

Aplicação web interativa para previsão de preços de imóveis em Boston utilizando Machine Learning.

🌐 Clique [aqui](https://bostonhousingai.streamlit.app/) para acessar a Demo.

---

## 📊 Sobre o projeto

Este projeto utiliza o clássico dataset **Boston Housing** para treinar um modelo de regressão capaz de estimar o valor de imóveis com base em características como:

* Número de quartos (`RM`)
* Taxa de criminalidade (`CRIM`)
* Proporção de indústrias (`INDUS`)
* Concentração de óxido nítrico (`NOX`)
* Relação aluno/professor (`PTRATIO`)
* Proximidade com o rio (`CHAS`)

A aplicação foi construída com **Streamlit**, permitindo interação em tempo real com o modelo.

---

## 🤖 Modelo de Machine Learning

* Algoritmo: Random Forest Regressor
* Biblioteca: scikit-learn
* Treinamento realizado previamente (modelo salvo em `.pkl`)
* Predição baseada em inputs do usuário via interface

---

## 🚀 Demonstração

A aplicação permite:

* Visualizar dados do dataset
* Explorar distribuição de preços
* Inserir características de um imóvel
* Obter previsão instantânea de valor

---

## 🛠️ Tecnologias utilizadas

* Python
* Streamlit
* Pandas
* Scikit-learn
* Plotly
* Joblib

---

## 📁 Estrutura do projeto

```
previsao-imovel/
│
├── app.py
├── modelo_rf_regressor_boston.pkl
├── data.csv
├── requirements.txt
└── README.md
```

---

## ⚙️ Como rodar o projeto

### 1. Clonar o repositório

```
git clone https://github.com/debbtrbl/previsao-valor-imovel-boston.git
cd previsao-imovel
```

### 2. Criar ambiente virtual

```
python -m venv venv
```

### 3. Ativar ambiente

**Windows**

```
venv\Scripts\activate
```

**Mac/Linux**

```
source venv/bin/activate
```

### 4. Instalar dependências

```
pip install -r requirements.txt
```

### 5. Executar aplicação

```
streamlit run app.py
```

---

## 📈 Exemplo de uso

1. Acesse a interface no navegador
2. Ajuste os parâmetros do imóvel na barra lateral
3. Clique em **"Realizar predição"**
4. Visualize o valor estimado

---

## 💡 Possíveis melhorias

* Validação de inputs do usuário
* Uso de pipeline com normalização
* Comparação entre diferentes modelos
* Deploy em nuvem (Streamlit Cloud)
* Interface mais customizada

---

## 📌 Observações

Este projeto tem fins educacionais e utiliza um dataset clássico amplamente usado para aprendizado em Machine Learning.

---

## 👩‍💻 Autor

Projeto desenvolvido para fins de estudo e prática em Data Science.
