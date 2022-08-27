import streamlit as st
from multiapp import MultiApp
from despliegue import modelo_decision_tree, modelo_svc


app = MultiApp()
st.markdown("#  Inteligencia de Negocios - Equipo A ")


# Add all your application here
app.add_app("Arbol", modelo_decision_tree.app)
app.add_app("Modelo SVC", modelo_svc.app)
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
