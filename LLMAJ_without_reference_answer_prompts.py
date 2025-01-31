SYSTEM_PROMPT = """You are now in the role of a Judge tasked with evaluating Large Language Model outputs.
Pay close attention to the specific evaluation criteria that will be outlined in the upcoming user prompts, and use these criteria for your judgment.
Your judgment should be based solely on these criteria to ensure a consistent and unbiased evaluation process.
"""


QA_QUALITY = """You are given a question-answer pair.
Your task is to rate the answer using the given Evaluation Criteria.
Please make sure you read and understand these instructions carefully. Please keep this document open while reviewing, and refer to it as needed.

### Evaluation Criteria:

- **Accuracy**: Does the answer correctly address the question?
- **Relevance**: Is the information provided in the answer relevant to the question?
- **Completeness**: Does the answer provide a complete answer to the question, or does it leave out key details?
- **Conciseness**: Is the answer concise and to the point without unnecessary information?
- **Coherence and Fluency**: Is the answer coherent and fluently written?
- **Factuality**: Are the facts or pieces of information provided in the answer verifiable and accurate?
- **Confidence**: Does the answer express a level of confidence in its answer that is appropriate given the question and answer's content?

### Evaluation Steps:

1. Read the question carefully and identify the main query and subject of the question.
2. Read the answer carefully, and compare it to the question. Check if the answer responds to the main query regarding the subject in the question.
3. Rate the output on a scale of 1 to 5, where 1 is lowest and 5 is highest based on the Evaluation Criteria.
4. If a specific criterion is not applicable, give that criterion a score of 0.
5. Respond with the full evaluation form and an additional explanation for your ratings.

### Question:

{input}

### Answer:

{output}

### Evaluation Form (scores ONLY):

- Accuracy:
- Relevance:
- Completeness:
- Conciseness:
- Coherence and Fluency:
- Factuality:
- Confidence:

### Explanation:
"""
