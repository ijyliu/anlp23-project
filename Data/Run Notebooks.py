import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

def execute_notebook(notebook_path):
    """
    Function to execute a single Jupyter notebook.
    """
    with open(notebook_path, encoding='utf-8') as file:
        nb = nbformat.read(file, as_version=4)
        ep = ExecutePreprocessor(timeout=None, kernel_name='anlp')
        ep.preprocess(nb, {'metadata': {'path': os.path.dirname(notebook_path)}})

        with open(notebook_path, 'wt') as file:
            nbformat.write(nb, file)

def main():
    """
    Main function to execute multiple Jupyter notebooks.
    """
    notebooks = [
                 #"01a - Conduct Conversations - GPT4 CW Manual Few Shot.ipynb",
                 #"01a - Conduct Conversations - GPT4 CW Zero Shot CoT.ipynb",
                 #"01a - Conduct Conversations - GPT4 GSM8K APE Zero Shot CoT.ipynb", 
                 #"01a - Conduct Conversations - GPT4 GSM8K Direct Prompting.ipynb", 
                 #"01a - Conduct Conversations - GPT4 GSM8K Least to Most.ipynb",
                 #"01a - Conduct Conversations - GPT4 GSM8K Manual CoT.ipynb",
                 #"01a - Conduct Conversations - GPT4 GSM8K Manual Few Shot.ipynb",
                 #"01a - Conduct Conversations - GPT4 GSM8K Self-Refine.ipynb",
                 #"01a - Conduct Conversations - GPT4 GSM8K Tree of Thought.ipynb",
                 "01a - Conduct Conversations - GPT4 GSM8K Zero Shot CoT.ipynb"
                 ]  # List of notebooks to execute
    notebooks = ["C:/Users/ijyli/repo/anlp23-project/Data/" + nb for nb in notebooks]
    
    for nb in notebooks:
        print(f"Executing {nb}...")
        execute_notebook(nb)
        print(f"Finished executing {nb}.")

if __name__ == "__main__":
    main()
