import sys, os, unicodedata, re
from big_sleep import Imagine
from pathlib import Path

def slugify(value, allow_unicode=False):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')

starting_dirname = os.getcwd()
output_dirname = './output'
Path(output_dirname).mkdir(exist_ok=True)

with open(sys.argv[1], 'r') as lyrics:
    for lyric in lyrics:
        input = lyric.strip()
        if len(input) == 0:
            break

        dirname = output_dirname + '/{}'.format(slugify(input[:40]))
        
        Path(dirname).mkdir(exist_ok=True)
        os.chdir(dirname)
        dream = Imagine(
            text=input,
            save_progress=True,
            save_every=10,
            save_best=True,
            epochs=6,
            iterations=150,
            open_folder=False
        )
        dream()
        
        os.chdir(starting_dirname)
        dream.reset()
