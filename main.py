import streamlit as st
from multiapp import MultiApp
from despliegue import modelo_random_forest_regression, modelo_svc
# from despliegue import modelo_arima, modelo_decision_tree, modelo_lstm, modelo_prophet,  modelo_svr


app = MultiApp()
st.markdown("#  Inteligencia de Negocios - Equipo C - Ciencia de Datos ")


# Add all your application here
# app.add_app("Modelo Arima", modelo_arima.app)
# app.add_app("Modelo Árbol de decisión", modelo_decision_tree.app)
# app.add_app("Modelo LSTM", modelo_lstm.app)
# app.add_app("Modelo Prophet", modelo_prophet.app)
app.add_app("Modelo Random Forest Regression", modelo_random_forest_regression.app)
app.add_app("Modelo SVC", modelo_svc.app)
# app.add_app("Modelo SVR", modelo_svr.app)
# The main app
app.run()



# with header:
#     st.title('Hello World')
#     st.write('This is a simple Streamlit app')

# with dataset:
#     st.title('Hello World')
#     st.write('This is the dataset')

# with features:
#     st.title('Hello World')
#     st.write('This is the features')


# st.write('This is the model training')
# st.write(fig)
# st.write()
