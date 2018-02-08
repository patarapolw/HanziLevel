import os

from resources import r
from AnkiTools.tools.read import readAnki2
from AnkiTools.AnkiConnect import POST
from PolUtils.common.common import speedTest


def vocabToLevel(vocab):
    lv = r.Level()
    level_array = []
    for char in vocab:
        for i, lv_kanji in enumerate(lv.levels):
            if char in lv_kanji:
                level_array.append(i)

    return max(level_array)


if __name__ == '__main__':
    os.chdir('..')

    with readAnki2(os.path.join('anki2', 'Chinese.anki2')) as anki:
        # for nid in POST('findNotes', params={'query': 'deck:Chinese::Vocab'}):
        #     vocab = anki.searchNoteById(str(nid))['content'][0]
        #     if vocab is not None:
        #         print(vocabToLevel(vocab))
        params = {
            'type': 'deck',
            'key': 'name'
        }
        with speedTest("Query time"):
            anki.loadQuery()
        for item in anki.getCardQuery('Chinese::Vocab', params):
            print(item)
