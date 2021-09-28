import numpy as np
import pandas as pd

def result(emotion,kind):
    if emotion in ['anger', 'contempt', 'disgust', 'fear']:
        emotion = 'cat1' 
    if emotion in ['happiness', 'surprise']:
        emotion = 'cat2'
    if emotion in ['neutral']:
        emotion = 'cat3'
    if emotion in ['sadness']:
        emotion = 'cat4'
    
    df = pd.read_csv('poemlist.csv')
    df.columns = ['情緒', '歌/詩', '名稱', '內容']

    catagories = []

    for value in df['情緒']:
        if value == df['情緒'].unique()[0]:
            catagories.append('cat1')
        if value == df['情緒'].unique()[1]:
            catagories.append('cat2')
        if value == df['情緒'].unique()[2]:
            catagories.append('cat3')
        if value == df['情緒'].unique()[3]:
            catagories.append('cat4')

    df['catagory'] = catagories

    chosen_cat = (df['catagory'] == emotion) & (df['歌/詩'] == kind)
    chosen_cat_df = df[chosen_cat]
    chosen_cat_df = chosen_cat_df.reset_index(drop=True)

    num = np.random.randint(0, 10)

    name = chosen_cat_df.loc[num]['名稱']
    content = chosen_cat_df.loc[num]['內容']

    return name, content


if __name__ == '__main__':
    emotion = "contempt"
    kind = '詩'
    print(result(emotion,kind))