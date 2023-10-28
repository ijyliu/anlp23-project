feedback_prompt = 

"""We want to score each acronym on five qualities: i) ease of pronunciation, ii) ease of spelling, and iii) relation to the title, iv) positive connotation, v) well-known.

Here are some examples of this scoring rubric:

"""

"""Title: {title}

Acronym: {answer}

Scores:

* Ease of pronunciation: {pronunciation_score}
* Ease of spelling: {spelling_score}
* Relation to title: {relation_score}
* Positive connotation: {connotation_score}
* Well-known: {well_known_score}

* Total score: {total_score}"""


"IF then STOP"

refiner_prompt = 

"""Title: {title}

Acronym: {acronym}

Scores:

{scores}

Okay, let's use this feedback to improve the acronym.

"""

def self_refine(prompt: str) -> str:
    def is_refinement_sufficient(prompt, feedback, initial, refined) -> bool:
        # Define stopping criteria here
        pass

    answer = ChatGPT(prompt)

    while True:
        feedback = ChatGPT(feedback_prompt, answer)
        refined = ChatGPT(refiner_prompt, feedback, answer)

        if is_refinement_sufficient(prompt, feedback, answer, refined):
            break

        answer = refined

    return refined
