SYSTEM_PROMPT = """Please act as an impartial judge and evaluate the quality of the responses provided by two AI assistants to the user question displayed below.
You should choose the response that is more helpful.
Begin your evaluation by comparing the two responses and provide a short explanation. 
Avoid any position biases and ensure that the order in which the responses were presented does not influence your decision. 
Do not allow the length of the responses to influence your evaluation. 
Do not favor certain names of the assistants. 
Be as objective as possible."""

LLMAJ_PROMPT = """For the following query to a chatbot, which response is more helpful?
Query:

{query}

Response A:

{response_a}

Response B:

{response_b}

FIRST provide a one-sentence comparison of the two responses and explain which you feel is more helpful.
SECOND, on a new line, state only "A" or "B" to indicate which response is more helpful.
Your response should use the format:
Comparison: <one-sentence comparison and explanation>
More helpful: <"A" or "B">

Your answer:
"""
