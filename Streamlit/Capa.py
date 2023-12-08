import streamlit as st
import ATBiblioteca as at_lib
from st_pages import Page, show_pages, add_page_title

at_lib.SetPageConfig()

#add_page_title()
show_pages(
    [
        Page('Capa.py','Introdução',":memo:"),
        #Page('Page_0.py','Sobre a aplicação',":building_construction:"),
        Page('Page_1.py','Aquisição de dados',":building_construction:"),
        Page('Page_2.py','Conhecendo a base de dados',":card_file_box:"),
        Page('Page_3.py','Preparação dos dados',":wrench:"),
        Page('Page_5.py','Regressão linear',":bulb:"),
    ]
)


at_lib.SetTheme()

html_p = """<p style='text-align: center; font-size:%spx;'><b>%s</b></p>"""

st.markdown('''<h1 style='text-align: center; '><b>INSTITUTO INFNET</b></h1>''',unsafe_allow_html = True)
st.markdown(html_p % tuple([35,"ESCOLA SUPERIOR DE TECNOLOGIA"]),unsafe_allow_html=True)
st.divider()

github_link = '''https://github.com/Leonidas-Vitor/Steam_Scrapper.git'''
email = '''leonidas.almeida@al.infnet.edu.br'''

columns = st.columns([0.6,0.4])
with columns[0]:
    st.markdown(html_p % tuple([25,'Aluno: Leônidas Almeida']),unsafe_allow_html = True)
    st.markdown(html_p % tuple([25,f'E-mail: <a href= mailto:{email}>{email}</a>']),unsafe_allow_html = True)
    st.markdown(html_p % tuple([25,f'GitHub: <a href={github_link}>Link para o repositório</a><h3>']),unsafe_allow_html = True)
    st.markdown(html_p % tuple([25,'Introdução:']),unsafe_allow_html = True)
    st.text('''
    Esta aplicação foi criada com o propósito de analisar os jogos da loja Steam e então estimar quantas 
    vendas um novo jogo hipotético teria, baseado em suas principais características e então avaliar se 
    vale o investimento nele ou não.
    ''')
    st.text('''
    O modelo de regressão linear foi escolhido por ser um modelo simples e de fácil interpretação, 
    a avaliação do modelo será feita através das métricas de MSE, RMSE e MAE.
    ''')
with columns[1]:
    st.image('Infnet_logo.png',width=400)

#tabs = st.tabs(['Instruções','Observações','Notas do autor'])
#with tabs[0]:
#    st.write('''A aplicação foi organizada em páginas, que podem ser acessadas pela barra lateral à esquerda.''')
#with tabs[1]:
#    st.write('Na última página há um breve registro de dificuldades encontradas na realização do trabalho')
#with tabs[2]:
#    st.markdown('<p> Dá bastante trabalho organizar a estética de uma aplicação web	&#129394;</P>',unsafe_allow_html=True)
#st.divider()
