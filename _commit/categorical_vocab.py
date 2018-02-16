from AnkiTools.AnkiConnect import POST


with open('vocab.txt') as f:
    for row in f.readlines():
        content = row[:-1].split('\t')
        params = {
            "note": {
                "deckName": "Chinese::Categorical Vocab::English::Love",
                "modelName": "Chinese Custom Vocab",
                "fields": {
                    "Simplified": content[0],
                    "Pinyin": content[1],
                    "English": content[2],
                    "Hanzi level": content[3]
                },
                "tags": []
            }
        }
        print(POST('addNote', params=params))
