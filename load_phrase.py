import pandas as pd
import numpy as np
import re


class LoadPhrase:
    phrases = pd.read_csv('./csv/phrases.csv', delimiter='\n')
    phrases.columns = ['word']
    phrases['word'] = phrases['word'].apply(lambda x: x.lower())
    phrases['word'] = phrases['word'].apply(lambda x: re.sub(r"(^\s*)|(\s*$)", "", x))
    phrases = np.array(phrases['word']).tolist()
    phrases = list(dict.fromkeys(phrases))

    def get_phrases(self):
        return self.phrases
