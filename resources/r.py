import os


class Level:
    def __init__(self):
        self.levels = ['']  # Placeholder of level 0
        with open(os.path.join('resources', 'levels.txt'), encoding='utf8') as f:
            for row in f.readlines():
                self.levels.append(row[:-1])

        self.level_labels = []
        with open(os.path.join('resources', 'level_labels.txt'), encoding='utf8') as f:
            for row in f.readlines():
                self.level_labels.append(row[:-1])

    def getLabels(self):
        for label in self.level_labels:
            result = {
                'full name': label,
                'short name': label.split(' ')[1],
                'levels': _parseRange(label.split(' ')[0])
            }
            yield result


def _parseRange(string_range):
    if '-' in string_range:
        start, end = string_range.split('-')
        return list(range(int(start), int(end)+1))
    else:
        return [int(string_range)]


if __name__ == '__main__':
    pass