import streamlit as st

import controller.cliente as cliente

def Deletar():
    st.title ('Deletar dados')
    
    with st.form(key='delete'):
        nome = st.text_input(label='Insira o nome')
        buttom_submit = st.form_submit_buttom('Deletar')

        if buttom_submit:
            cliente.excluir(nome)
            st.success('Aluno excluido com sucesso')