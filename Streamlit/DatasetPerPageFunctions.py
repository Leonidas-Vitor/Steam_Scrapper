import numpy as np
import pandas as pd
import ast

def GetMainGenre(tags):
    if (type(tags) == str):
        tags= ast.literal_eval(tags)

    if (type(tags) == dict):
        #return max(tags, key=tags.get)
        main_genre = {}
        try:
            for chave,valor in tags.items():
                if (chave in generosValidos):
                    main_genre[chave] = valor
            try:
                return max(main_genre, key=main_genre.get)
            except Exception as e:
                return 'Others'#max(tags, key=tags.get)
        except Exception as e:
            print(tags)
            return 'Erro'
    else:
        return 'NoTags'
    
def OrganizeTags(tags):
    if (type(tags) == str):
        tags= ast.literal_eval(tags)

    newList = []
    for tag in tags:
        newList.append(tag)
    return newList

def IsEarlyAcess(genres):
    '''
    Identifica se um jogo está em early acess através da coluna genres que é uma lista de dicionários de gêneros
    '''
    if (type(genres) == str and genres != ''):
        try:
            genres = ast.literal_eval(genres)
        except Exception as e:
            #st.text(genres)
            pass
    try:
        for g in genres:
            if g['description'] == 'Early Access':
                return True
        return False
    except TypeError as te:
        #jogo não possui tags
        return False
    except Exception as e:
        return False
    
def ContainsTargetCategory(categories, target_category):
    try:
        for category in categories:
            for value in category.values():
                if value == target_category:
                    return True
        return False
    except TypeError as te:
        #o jogo não possui categorias
        return False

def Is_sef_published(developers,publishers):
    try:
        publisherPercent = 1/len(publishers)
        totalPublisher = 0
        for developer in developers:
            for publisher in publishers:
                if developer.strip() == publisher.strip():
                    totalPublisher += publisherPercent
        return totalPublisher if totalPublisher <= 1 else 1
    except TypeError as te:
        #print(te)
        #Ocorre quando não há dado de publicadora e/ou desenvolvedor (Nan)
        return 0

def ParseData(d):
    try:
        return ast.literal_eval(d)
    except Exception as e:
        return d


def DatasetPage2(df_redux : pd.DataFrame) -> pd.DataFrame:
    df = df_redux.drop(df_redux[df_redux['scrap_status'] != 'Scrap_Sucess'].index)
    df = df.drop(df[df['type'] != 'game'].index)
    return df

def DatasetPage3(df : pd.DataFrame) -> pd.DataFrame:
    generosValidos = [
    'Roguelike Deckbuilder','4X',
    'Simulation','Management', #=> Esses dois são juntos
    'Open World Survival Craft','City Builder','RPG','Rogue-like','Metroidvania','Dungeon Crawler','Souls-like',
    'Visual Novel','Twin Stick Shooter','Horror','Sexual Content','Card Battler','Beat \'em up','FPS','Shoot \'Em Up'
    'Tower Defense','Match 3','Puzzle-Platformer','Puzzle','2D Platformer','3D Platformer','Battle Royale']
    
    df_redux = df.drop(columns=['scrap_status','type','required_age','spy_status','hltb_status',
        'hltb_name', 'recommendations'])

    df_redux['release_date'] = df_redux['release_date'].apply(ast.literal_eval)

    df_redux = df_redux[(df_redux['is_free'] == False)]

    df_redux = df_redux[(df_redux['release_date'].str['coming_soon'] == False)]

    df_redux = df_redux[df_redux['genres'] != '']

    df_redux = df_redux[df_redux['price_overview'] != '']

    df_redux = df_redux[df_redux['categories'] != '']

    df_redux = df_redux.assign(main_genre = df_redux['tags'].apply(lambda tags: GetMainGenre(tags)))

    #------------ Organização das tags

    df_redux['tags'] = df_redux['tags'].apply(lambda tags: OrganizeTags(tags))

    #Criação de uma coluna que identifica se um jogo está ou não em acesso antecipado
    df_redux = df_redux.assign(isEarlyAcess = df_redux['genres'].apply(lambda genres: IsEarlyAcess(genres)))

    #------------ Data de lançamento
    df_redux['release_date'] = pd.to_datetime(df_redux['release_date'].str['date'].apply(lambda d: None if len(d) == 0 else d[:3] + ' 1, ' + d[4:8] if len(d) <= 8  else d))

    #------------ Dias em comercialização
    df_redux['commercialization_days'] = (pd.Timestamp('2023/11/08') - df_redux['release_date']).dt.days
    #----------- Preço
    df_redux['price_overview'] = df_redux['price_overview'].apply(ast.literal_eval)
    df_redux['price'] = df_redux['price_overview'].str['initial']/100


    df_redux.drop(columns=['price_overview'],inplace=True)

    #----------- Modos de jogo
    df_redux['categories'] = df_redux['categories'].apply(ast.literal_eval)

    df_redux['hasSingleplayer'] = df_redux['categories'].apply(lambda s : ContainsTargetCategory(s,'Single-player'))
    df_redux['hasMultiplayer'] = df_redux['categories'].apply(lambda s : ContainsTargetCategory(s,'Multi-player'))
    df_redux['hasCoop'] = df_redux['categories'].apply(lambda s : ContainsTargetCategory(s,'Co-op'))

    #----------- Avaliações

    df_redux['total_reviews'] = df_redux['positive'].copy() + df_redux['negative'].copy()
    df_redux['positive_reviews_percent'] = df_redux['positive'].copy()/df_redux['total_reviews']

    #----------- Línguas suportadas

    df_redux['total_supported_languages'] = df_redux.supported_languages.str.split(',')
    df_redux['total_supported_languages'] = df_redux['total_supported_languages'].fillna('')
    df_redux['total_supported_languages'] = df_redux['total_supported_languages'].apply(lambda languages: len(languages))

    #----------- Auto publicação
    df_redux['developers'] = df_redux['developers'].apply(ParseData)
    df_redux['publishers'] = df_redux['publishers'].apply(ParseData)

    df_redux['self_published_percent'] = df_redux.apply(lambda x: Is_sef_published(x.developers,x.publishers),axis=1)

    df_redux['developers'] = df_redux['developers'].apply(lambda x: ', '.join(x) if isinstance(x, list) else x)

    #----------- Duração
    def FillDuration(row):
        if (row['hltb_main_story'] == 0 or np.isnan(row['hltb_main_story']) or type(row['hltb_main_story']) == str):
            row['hltb_main_story'] = df_duration_median[df_duration_median['main_genre'] == row['main_genre']]['hltb_main_story'].values[0]
        return row

    df_duration_median = df_redux[(df_redux['hltb_main_story'] > 0) & (~np.isnan(df_redux['hltb_main_story'])) &
        (df_redux['hltb_similarity'] > 0.9)].copy()

    df_duration_median = df_duration_median[['main_genre','hltb_main_story']]
    df_duration_median = df_duration_median.groupby('main_genre').median().reset_index()

    df_redux = df_redux.apply(FillDuration,axis=1)

    #----------- Conquistas

    df_redux['achievements'] = df_redux['achievements'].apply(ParseData)
    df_redux['total_achievements'] = df_redux['achievements'].str['total']

    df_redux['total_achievements'].fillna(0)

    df_redux['total_achievements'] = df_redux['total_achievements'].apply(lambda x: 0 if np.isnan(x) else x)

    #----------- Rename das colunas

    df_redux.rename(columns={'steam_appid':'id','hltb_main_story':'total_duration'},inplace=True)

    df_redux.drop(columns=['is_free','genres','supported_languages','categories','positive','negative',
        'developers','publishers','achievements','hltb_similarity','steamspy_owners'],inplace=True)
    
    return df_redux


    
