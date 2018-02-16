from shared.r import vocabToLevel
from AnkiTools.tools.read import readAnki2

import pandas as pd


with readAnki2('../shared/r/Chinese.anki2') as anki:
    anki.loadQuery()
    params = {
        'type': 'model',
        'key': 'name'
    }
    result = dict()
    for query in anki.getCardQuery('Chinese Vocab', params):
        Hanzi_level = str(vocabToLevel(query['note']['content'][0]))
        HSK_level = query['note']['content'][7]
        result[HSK_level][Hanzi_level] = result.setdefault(HSK_level, dict()).setdefault(Hanzi_level, 0) + 1
    print(result)

data = pd.DataFrame(result)
data = data.fillna(' ')
data.to_csv('level_vs_hsk.csv', sep='\t')