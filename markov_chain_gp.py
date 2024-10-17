import random

def learn_word_frequencies(path: str, lookback: int = 2) -> dict:
    """Learn word frequencies from a text file. You can set the "state"
    of the markov model with lookback.

    Args:
        path (str): location of the training file
        lookback (int, optional): the number of words to define as the
            current "state". Defaults to 2.

    Returns:
        dict: a dictionary of states and the following words
    """
    with open(path) as fo:
        words = fo.read().split(' ')
    words = [word for word in words if len(word) > 0]

    db = {}
    for i in range(len(words) - lookback):
        key = tuple(words[i:i + lookback])
        val = words[i + lookback]
        db[key] = db.get(key, []) + [val]
  
    return db


def markov_chain(db: dict, lookback: int = 2) -> str:
    """Use a markov chain to generate new text from the dictionary.

    Args:
        db (dict): the dictionary output from learn_word_frequencies
        lookback (int, optional): the number of words to define as the
            current "state". Defaults to 2.

    Returns:
        str: newly generated text
    """
    paragraph = list(random.choice(list(db.keys())))
  
    for i in range(100):
        if random.random() < 0.01:
            last_words = random.choice(list(db.keys()))
        else:
            last_words = paragraph[-lookback:]
    
        next_word_options = db.get(tuple(last_words))
        if next_word_options:
            paragraph.append(random.choice(next_word_options))
  
    return ' '.join(paragraph)


db = learn_word_frequencies('twilight-fanfic.txt')
markov_chain(db)