
# NOTE: It seems possible to simplify things in conversation mode - just asking a problem, then always sending the same task string.

feedback_prompt = 

"""
Problem: 
{problem}

Response:
{response}

Task:
Please check the math for the response above. If there is an error, state what the error is, but don't fix it. If there are no errors, output STOP.
"""


refiner_prompt = 

"""
Problem: 
{problem}

Response:
{response}

Feedback:
{feedback}

Task:
Use the provided feedback to re-write the response.
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
