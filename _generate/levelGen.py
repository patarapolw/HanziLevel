import os


def splitLevels(output, num_level, char_string):
    batch = len(char_string) // num_level + 1
    with open(output, 'a') as fout:
        for i, char in enumerate(char_string):
            fout.write(char)
            if (i+1)%batch == 0:
                fout.write('\n')
        fout.write('\n')


if __name__ == '__main__':
    # os.chdir('../r')
    #
    # sf_string = ''
    # with open('SpoonFed.txt', encoding='utf8') as f:
    #     while True:
    #         char = f.read(1)
    #         if char == '':
    #             break
    #         if char != '\n':
    #             sf_string += char
    # print(len(sf_string))
    # # # splitLevels('levels.txt', 55, sf_string)
    # #
    # hsk_string = ''
    # with open('HSK.txt', encoding='utf8') as f:
    #     while True:
    #         char = f.read(1)
    #         if char == '':
    #             break
    #         if char not in '\n…' + sf_string:
    #             hsk_string += char
    # print(len(hsk_string))
    # # splitLevels('levels.txt', 5, hsk_string)
    #
    # f_string = ''
    # with open('freq.tsv', encoding='utf8') as f:
    #     for line in f.readlines():
    #         f_string += line.split('\t')[1]
    #
    # max = -1
    # for i, char in enumerate(f_string):
    #     if char in sf_string + hsk_string:
    #         max = i
    # print(max)
    #
    # j = 0
    # with open('levels.txt', 'a', encoding='utf8') as fout:
    #     for i, char in enumerate(f_string):
    #         if i > max:
    #             break
    #         if char not in sf_string + hsk_string:
    #             fout.write(char)
    #             j += 1
    #         if (j+1)%65 == 0:
    #             fout.write('\n')
    #     fout.write('\n')
    pass
