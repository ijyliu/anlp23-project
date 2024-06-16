# The Practicality of Prompt Engineering

Isaac Liu

This paper examines the practicality of prompt engineering in improving the performance of Large Language Models. Through empirical analysis, I evaluate the trade-offs between costs and benefits of prompting using novel metrics. Different prompting methods are assessed using standardized tasks and both state-of-the-art and older models. Although gains on task performance are falling, chain-of-thought prompting (zero-shot varieties in particular) through a series of concise and organized steps still offers a generally cost-effective way to get significant performance improvement. The complexity of responses and adherence to rules and human preferences can be serious issues for prompting techniques and are a reason for few-shot methods in some cases.

The report can be found [here](Report/Report.pdf). Analysis includes experiments conducted on a standard GSM8K math task and a creative writing coherence task (with a finetuned LLM used, in part, to grade responses), as well as appropriate statistical testing. In addition to devising and applying unique metrics such as inter-paragraph cosine similarity and the ratio of model to human interaction length, I also contribute data on the popularity of prompt engineering techniques as implied by Semantic Scholar citations.

The structure of this repository is generally self-explanatory. Environment/package specs can be found [here](https://github.com/ijyliu/anlp23-project/blob/main/Code/environment.yml).

## Technologies (not exhaustive!)

- Python
  - Transformers, Sentence Transformers
  - NLTK
  - OpenAI API
  - Tiktoken
  - Statsmodels
  - Textstat
  - Matplotlib
  - Pandas
  - Conda
- LaTeX
