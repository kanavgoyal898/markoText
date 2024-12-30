# markoText: Bag of Words Markov Chain

markoText is a Python-based story generator that leverages a Bag of Words Markov Chain model to create new text based on an input story or text corpus. This program generates new narratives by predicting the next word in a sequence based on the words that came before it. The Markov Chain model is trained on an input text file, learning the statistical probabilities of transitions between words. By using this trained model, the program can generate new and unique text that mimics the style and structure of the original input.

<div>
  <img src="./library.png" alt="Preview" style="width: 100%;">
</div>

## Features

- **Training with Custom Text:** Train a Markov model from any text file (e.g., stories, books).
- **Customizable n-Grams:** Adjust the n-gram size to control the complexity of word prediction.
- **Story Generation:** Generate text starting from a user-defined state and generate a specific number of words.

## Requirements

- Python 3.x
- `re` and `random` modules (standard library)

## Running the Program

### Step 1: Prepare the Text File
Ensure you have a text file that contains the story or text you'd like to train the model on. This file should be plain text (e.g., `.txt` format).

### Step 2: Run the Program

Open a terminal and run the program using the following command:

```bash
python main.py
```

### Step 3: Command Line Arguments

You will need to provide the following arguments when running the program:

- **Story Path (`story_path`)**: The path to the text file you want to use for training the model.
- **N-Gram Size (`n_gram`)**: The number of words to consider when predicting the next word in the sequence. This value will determine the complexity of the model (e.g., 1 for unigram, 2 for bigram, etc.).
- **Starting State (`state`)**: The word or phrase where the generated story should start. This is the seed for the text generation.
- **Number of Words to Generate (`count`)**: The number of words you want the generated story to contain.

## Usage

### Example Story File (`data/holmes.txt`):

```
(venv) kanavgoyal@MacBook-Pro markoText % cd src/
(venv) kanavgoyal@MacBook-Pro src % python3 main.py 
enter story path: ../data/holmes.txt
enter n-gram: 2
number of states: 215,543 in a 2-gram model
enter starting state: THE GAME
enter number of words to generate: 128
THE GAME WAS IN ALL WAYS AS EXEMPLARY MEMBERS OF THE SOCIETY OF FREEMEN THE YOUNG MANS RETURN AND OF A MAID RUSHED ACROSS THE GLADE HOLMES AND NOW DR STERNDALE HOW DO YOU OBSERVE ANYTHING VERY PECULIAR FELLOW AND ALL THE OTHER LITTLE WEAKNESSES ON WHICH YOU HAVE SO HOMELY A THING AS A GENTLEMAN AT BAKER STREET BUT I SAW THE SPOT WHERE THE TREASURE IS HIDDEN INAT THIS INSTANT WHAT THE RASCAL HAD COPIED THE PAPER IN A LISTLESS WAY BUT I SAW AN ILLDRESSED VAGABOND IN THE LANE WHERE HE HAD GONE BY AND ALL WAS SAFE THREW OFF HIS GLASS I CAME DOWN TO BREAKFAST IN THE ROOM IN EACH CASE CAUGHT MY EYE IN SLEEP SINCE I DID AS HE WOULD DO BETTER TO BE FRANK WITH ME IF I LIGHT MY FIRST THOUGHT WAS THAT I DESIRED TO ACCOMPLISH MY PURPOSE FOR IN MY DESPAIR AND DISAPPOINTMENT AFTER A FEW MONTHS THEY EXACTLY FITTED THE TRACKS I MIGHT IT SHOULD BE STOPPED YOU MUST SPEAK OR I SHOULD HAVE BEEN EXPOSED AND DRAGGED WITH MY KNOWLEDGE THAT I KILLED BLACK PETER AND WHEN DID YOU FIND NOTHING BETTER TO TAKE NO CHANCES OF MISSING HIS MAN THE SAME THOUGHT HAD CROSSED THE LAWN THE LAWN VERY CAREFULLY FOR A MOMENT I FOUND MYSELF WEARY AND YET WAKEFUL TOSSING RESTLESSLY FROM SIDE TO SIDE IN A CHEMICAL PIPETTE NOW I KNEW THAT I HAD TAKEN OVER ANOTHER PROFESSION BUT SHE WOULDNT TELL I DARE SAY IT BEARS EVERY MARK OF REFINEMENT AND 
(venv) kanavgoyal@MacBook-Pro src % 
```

## Conclusion

markoText is a powerful tool for generating creative text based on a given corpus using the Bag of Words Markov Chain model. Whether you’re interested in generating new stories, experimenting with word patterns, or creating unique content for writing or creative projects, this tool offers flexibility and control over how the text is generated. By adjusting the n-gram size and starting state, you can explore a wide range of text generation possibilities, from simple random sequences to more structured and coherent stories. The more diverse and extensive the training corpus, the richer and more varied the generated text will be.

With markoText, you can bring a new level of interactivity and creativity to any text-based project.
