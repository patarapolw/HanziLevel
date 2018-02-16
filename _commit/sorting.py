import os

from shared import r
from AnkiTools.tools.read import readApkg
from AnkiTools.AnkiConnect import POST


def vocabToLevel(vocab):
    lv = r.Level()
    level_array = []
    for char in vocab:
        for i, lv_kanji in enumerate(lv.levels):
            if char in lv_kanji:
                level_array.append(i)

    try:
        return max(level_array)
    except ValueError:
        return -1


if __name__ == '__main__':
    os.chdir('..')

    with readApkg(os.path.join('/Users/patarapolw/Dropbox/Uploads', 'Chinese.apkg')) as anki:
        anki.loadQuery()
        lv = r.Level()

        cid_levels = []
        params = {
            'type': 'deck',
            'key': 'name'
        }
        for card in anki.getCardQuery('Chinese::sentence', params):
            content = card['note']['content'][2]
            cid_levels.append({
                'cid': card['cid'],
                'level': vocabToLevel(content),
                'ord': card['ord']
            })

        cid_list = []
        for i, name in enumerate(['CE', 'EC']):
            key1 = name
            for label in lv.getLabels():
                key2 = label['full name']
                if '1-10' in key2:
                    key2 = ' ' + key2
                for level in label['levels']:
                    key3 = 'Level {:2d}'.format(level)
                    cids = []
                    for cid_level in cid_levels:
                        if cid_level['level'] == level and cid_level['ord'] == i:
                            cids.append(int(cid_level['cid']))
                    if cids != []:
                        cid_list.append({
                            'name': 'Chinese::sentence::{}::{}::{}'.format(key1, key2, key3),
                            'cids': cids,
                        })
                        cids = []

        print(cid_list)

        for cid in cid_list:
            deck_name = cid['name']
            cids = cid['cids']
            print(deck_name)
            print(cids[:10])
            result = POST('changeDeck', params={
                'cards': cids,
                'deck': deck_name
            })
            print(result)
