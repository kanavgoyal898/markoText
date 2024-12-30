import re
import random

def read_story(story_path):
    text, data = '', []

    with open(story_path, 'r') as lines:
        text = lines.read()
        lines.seek(0)
        for line in lines:
            line = line.strip()
            if line:
                data.append(line)
    
    return text, data

def clean_data(lines):
    cleaned_data = []

    for line in lines:
        line = line.upper().strip()
        if not line:
            continue

        line = re.sub(r"[^\w\s]", "", line)
        words = line.split()
        words = [word for word in words if word.isalpha()]
        cleaned_data += words

    return cleaned_data

def make_markov_model(cleaned_data, n_gram=1):
    # data structure { i : { j : count } }  where i is the current word and j is the next word
    markov_model = {}

    for i in range(len(cleaned_data)-n_gram-1):
        curr_state, next_state = '', ''
        for j in range(n_gram):
            if i+j+n_gram >= len(cleaned_data):
                break
            curr_state += cleaned_data[i+j] + ' '
            next_state += cleaned_data[i+j+n_gram] + ' '

        curr_state = curr_state.strip()
        next_state = next_state.strip()

        markov_model[curr_state] = markov_model.get(curr_state, {})
        markov_model[curr_state][next_state] = markov_model[curr_state].get(next_state, 0) + 1

    for curr_state, transitions in markov_model.items():
        total_transitions = sum(transitions.values())
        for next_state, count in transitions.items():
            markov_model[curr_state][next_state] = count / total_transitions

    return markov_model

def train_model(story_path, n_gram=1):
    text, data = read_story(story_path)
    cleaned_data = clean_data(data)
    markov_model = make_markov_model(cleaned_data, n_gram)

    return markov_model

def generate_story(markov_model, n=1024, state='THE GAME'):
    i = 0
    state = state.upper().strip()
    if state not in markov_model:
        return 'State not found in the model'

    curr_state = state
    next_state = None

    story = curr_state + ' '
    
    while i < n:
        next_state = random.choices(list(markov_model[curr_state].keys()), list(markov_model[curr_state].values()))
        curr_state = next_state[0]
        story += curr_state + ' '
        i += 1

    return story

story_path = input('enter story path: ')
n_gram = int(input('enter n-gram: '))
markov_model = train_model(story_path, n_gram)
print(f'number of states: {len(markov_model):,} in a {n_gram}-gram model')

state = input('enter starting state: ')
count = input('enter number of words to generate: ')
generated_story = generate_story(markov_model, int(count), state)
print(generated_story)
