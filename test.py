from shared import r

lv = r.Level()
with open('test.txt') as f:
    for line in f.readlines():
        print(r.vocabToLevel(line))
