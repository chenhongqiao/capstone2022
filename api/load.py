from os import walk
import nltk

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')


def load_sentences():
    texts = []
    for (_, _, file) in walk('texts'):
        texts.extend(file)
        break

    sentences = []
    titles = []
    backgrounds = []
    sources = []
    for text in texts:
        content = open('texts/'+text, 'r').read()
        content_sentences = nltk.tokenize.sent_tokenize(content)
        meta = open('metas/'+text, 'r').readlines()
        for sentence in content_sentences:
            sentences.append(sentence.strip())
            titles.append(meta[0].strip())
            backgrounds.append(meta[1].strip())
            sources.append(meta[2].strip())

    return sentences, titles, backgrounds, sources
