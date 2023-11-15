
# Functions useful for grading responses

####################################################################################################

# Basic infrastructure for conversations

import openai

# Get and set API key
with open('C:/Users/ijyli/Documents/OpenAI/anlp23-project.txt', 'r') as file:
    api_key = file.read()
openai.api_key = api_key

# GPT-4
# Send the current conversation as well as a new prompt and get a response
def prompt_gpt_4_and_get_convo(messages, prompt):
    messages_and_prompt = messages.copy()
    messages_and_prompt.append({"role": "user", "content": prompt})
    new_message = openai.ChatCompletion.create(
        model="gpt-4-0613", 
        messages=messages_and_prompt
    )
    with_new_message = messages_and_prompt.copy()
    with_new_message.append(dict(new_message['choices'][0]['message']))
    return with_new_message

####################################################################################################

# Function to grade coherence of a creative writing passage
def grade_creative_writing_coherence(conversation):
    # Collapse conversation into a single string with newlines
    conversation_string = ""
    for message in conversation:
        conversation_string += message['content'] + "\n"
    # Create task
    task = conversation_string + "Your Task: Rate the coherence of the final answer on a scale of 1 to 10, 1 being incoherent and 10 being very coherent. Write your justification and then put the numeric rating on its own line as the last line of your response."
    # Storing conversation elements
    conversation_with_grading = []
    # Get response
    conversation_with_grading = prompt_gpt_4_and_get_convo(conversation_with_grading, task)
    # Get "Content" of last message and extract rating as the last line of the response
    rating = int(conversation_with_grading[-1]['content'])
    return rating

# Function to grade ease of evaluation of a conversation
def grade_ease_of_evaluation(conversation):
    # Collapse conversation into a single string with newlines
    conversation_string = ""
    for message in conversation:
        conversation_string += message['content'] + "\n"
    # Create task
    task = conversation_string + "On a scale of 1-10 (1 being easy and 10 being difficult), how difficult is it to check the reasoning behind the above conversation? Write your justification then put the numeric rating on its own line as the last line of your response."
    # Storing conversation elements
    conversation_with_grading = []
    # Get response
    conversation_with_grading = prompt_gpt_4_and_get_convo(conversation_with_grading, task)
    # Get "Content" of last message and extract rating as the last line of the response
    rating = int(conversation_with_grading[-1]['content'])
    return rating

# Function to grade GSM8K conversation using provided answer
def grade_gsm8k_with_provided_answer(conversation, answer):
    conversation_with_answer = conversation.copy()
    task = "\nTask:\nOutput 0 if the final answer does not match the provided answer and 1 if it matches the final answer."
    # Get 0 or 1 value to return
    conversation_with_grade = prompt_gpt_4_and_get_convo(conversation_with_answer, "Provided Answer:\n" + answer + task)
    # Get last element of conversation_with_grade
    last_element = conversation_with_grade[-1]
    # Return 0 or 1
    return int(last_element['content'])
