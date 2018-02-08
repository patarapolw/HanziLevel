import zipfile
import os


def extract(path_to_file, output=''):
    output_dir, output_file = os.path.split(output)
    if output_file == '':
        output_dir = 'anki2'
        output_file = os.path.splitext(os.path.split(path_to_file)[1])[0] + '.anki2'
        output = os.path.join(output_dir, output_file)
    if output_dir == '':
        output_dir = 'anki2'

    with zipfile.ZipFile(path_to_file, 'r') as zp:
        zp.extract('collection.anki2', output_dir)

    os.rename(os.path.join(output_dir, 'collection.anki2'), output)


if __name__ == '__main__':
    os.chdir('..')

    # extract('/Users/patarapolw/Downloads/SpoonFed.apkg')
