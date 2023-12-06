import streamlit as st
import ATBiblioteca as at_lib

at_lib.SetPageConfig("TP9 - Projeto de Bloco - Capa")
at_lib.SetTheme()

st.markdown('''<h1 style='text-align: center; '><b>INSTITUTO INFNET</b></h1>''',unsafe_allow_html = True)

st.markdown('''<h2 style='text-align: center; '>ESCOLA SUPERIOR DE TECNOLOGIA GRADUAÇÃO EM CIÊNCIA DE DADOS<h2>''',unsafe_allow_html = True)

st.divider()

dp_link = '''https://github.com/Leonidas-Vitor/Steam_Scrapper.git'''
email = '''leonidas.almeida@al.infnet.edu.br'''
columns = st.columns([0.4,0.6])
with columns[0]:
    st.image('Infnet_logo.png')
with columns[1]:
    st.markdown('''<h3 style='text-align: center; '>Projeto de Bloco<h3>''',unsafe_allow_html = True)
    st.markdown('''<h3 style='text-align: center; '>TP9<h3>''',unsafe_allow_html = True)
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
