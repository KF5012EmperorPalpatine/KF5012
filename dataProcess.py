import pandas as pd

def dataProcess(data):
    dataframe = pd.read_csv(data)
    # split data into features (headlines/corpus) and labels (stock movement classified as up and down)
    dataframe['Headlines'] = dataframe[dataframe.columns[2:]].apply(lambda x: '. '.join(x.dropna().astype(str)), axis=1)
    corpus = dataframe['Headlines']
    # remove punctuation and make lowercase
    corpus.replace("[^a-zA-Z]", " ", regex=True, inplace=True)
    corpus = corpus.str.lower()

    try:
        labels = dataframe['Label']
        return corpus, labels
    except KeyError:
        return corpus