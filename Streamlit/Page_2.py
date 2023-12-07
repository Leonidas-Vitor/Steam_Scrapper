import ATBiblioteca as at_lib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sb
import streamlit as st

st.header('Conhecendo a base de dados',divider=True)

markdown = '''
|Coluna|Descrição|Tipo|
|------|---------|----|
|appid|Id de identificação na loja steam|Numérico discreto
|name|Nome do jogo|Textual
|scrap_status|Estado do processo de scrap|Textual categórica
|type|Se é um jogo, demo ou dlc|Categorico
|steam_appid|Id de identificação na loja steam, o nome da coluna é diferente quando o dado é extraído via API da steam|Numérico discreto
|required_age|Idade mínima recomendada para o jogo|Numérico discreto
|is_free|Se é um jogo gratuito|Booleano
|short_description|Descrição breve do jogo|Textual
|fullgame|Endereçamento para o jogo completo caso seja uma demo| Dicionário com id e nome do jogo completo
|supported_languages|Lista de linguas suportadas pelo jogo|Textual
|pc_requirements|Dicionário dos requisitos para "rodar" o jogo|Textual
|developers|Nome da desenvolvedora|Textual
|publishers|Nome da publicadora|Textual
|platforms|Dicionário relacionando a plataforma e se o jogo está disponível nela|Booleano
|categories|Dicionário de macro características do jogo|Textual categórica
|release_date|Dicionário relacionando se o jogo já foi lançada e qual a data de lançamento|Temporal
|controller_support|Tipo de suporte a controles|Textual categórica
|positive|Quantidade de avaliações positivas|Numérico discreto
|negative|Quantidade de avaliações negativas|Numérico discreto
|tags|Tags do jogo|Textual categórica
|steamspy_owners|Faixa estimada de proprietários de um jogo|Textual categórica
|spy_status|Estado do processo de scrap dos dados do SteamSpy|Textual categórica
|hltb_status|Estado do processo de scrap dos dados do HowLongToBeat|Textual categórica
|genres|Lista de gêneros do jogo|Textual categórica
|achievements|Quantidade de conquistas e o nome de algumas delas|Numérico discreta e Textual
|price_overview|Dicionário contendo os dados de preço e promoções em dólar|Numérico contínuo
|demos|Endereçamento para a demo caso possua| Dicionário com id e nome da demo
|hltb_id|Id de identificação no HowLongToBeat|Numérico discreto
|hltb_name|Nome do jogo no HowLongToBeat|Textual
|hltb_alias|Apelido do jogo no HowLongToBeat|Textual
|hltb_similarity|Grau de similaridade entre o nome do jogo buscado e o nome do jogo encontrado no HLTB|Numérico contínuo
|hltb_main_story|Duração dos objetivos principais do jogo em hrs|Numérico contínuo
|hltb_main_extra|Duração dos extras do jogo em hrs|Numérico contínuo
|hltb_completionist|Duração dos objetivos principais, extras e outros em hrs|Numérico contínuo
|hltb_all_styles|Duração em hrs levando em consideração todos os tipos de jogadores|Numérico contínuo
|ext_user_account_notice|Desconhecido|Textual
|recommendations|Quantidade de avaliações do jogo na loja steam|Numérico discreto
|metacritic|Nota do jogo no site metacritic|Numérico discreto
|drm_notice|Tipo de DRM do jogo|Textual
|alternate_appid|Desconhecido|Numérico discreto
'''

st.markdown(markdown)
