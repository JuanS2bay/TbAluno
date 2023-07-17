import streamlit as st

import controller.cliente as cliente

def inserir():
    st.title('Inserir Dados')
    cursos = ['Informática', 'Mineração']
    
    with st.form(key='insert'):
        input_matricula = st.number_input(label='Insira a matricula', format='%d', step=1)
        input_name = st.text_input(label='Insira o nome')
        input_cursos = st.selectbox(label='Insira o curso', options=cursos)
        input_age = st.number_input(label='Insira a idade', format='%d', step=1)
        buttom_submit = st.form_submit_button('Enviar')
        if buttom_submit:
            cliente.incluir(input_name, input_age, input_cursos, input_matricula)
            st.success('Cliente incluido com sucesso')