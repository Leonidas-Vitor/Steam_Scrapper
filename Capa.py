import streamlit as st
import VisualizacaoATBiblioteca as at_lib

at_lib.SetPageConfig("AT - Visualização de dados - Capa")
at_lib.SetTheme()

st.markdown('''<h1 style='text-align: center; '><b>INSTITUTO INFNET</b></h1>''',unsafe_allow_html = True)

st.markdown('''<h2 style='text-align: center; '>ESCOLA SUPERIOR DE TECNOLOGIA GRADUAÇÃO EM CIÊNCIA DE DADOS<h2>''',unsafe_allow_html = True)

st.divider()

dp_link = '''https://deepnote.com/workspace/data-science-3c52-cdea60e4-672c-4dfd-b559-a460bfd540ad/project/AT-01ed26c9-a8a8-4de2-9fba-8265c76babf7/notebook/AT_Visualiza%C3%A7%C3%A3o%20de%20Dados-edae64a222844fc7929a4f70fed52a4b'''
email = '''leonidas.almeida@al.infnet.edu.br'''
columns = st.columns([0.4,0.6])
with columns[0]:
    st.image('Infnet_logo.png')
with columns[1]:
    st.markdown('''<h3 style='text-align: center; '>Visualização de Dados<h3>''',unsafe_allow_html = True)
    st.markdown('''<h3 style='text-align: center; '>AT<h3>''',unsafe_allow_html = True)
    st.markdown('''<h3 style='text-align: center; '>Aluno: Leônidas Almeida<h3>''',unsafe_allow_html = True)
    st.markdown(f'''<h3 style='text-align: center; '>E-mail: <a href= mailto:{email}>{email}</a><h3>''',unsafe_allow_html = True)
    st.markdown(f'''<h3 style='text-align: center; '>Deep Note: <a href={dp_link}>Link para o notebook</a><h3>''',unsafe_allow_html = True)
    #st.write("[link]()")
    tabs = st.tabs(['Instruções','Observações','Notas do autor'])
    with tabs[0]:
        st.write('''Os exercícios do AT foram organizados em páginas, 
            que podem ser acessadas pela barra lateral''')
    with tabs[1]:
        st.write('Na última página há um breve registro de dificuldades encontradas na realização do trabalho')
    with tabs[2]:
        st.markdown('<p> Dá bastante trabalho organizar a estética de uma aplicação web	&#129394;</P>',unsafe_allow_html=True)
