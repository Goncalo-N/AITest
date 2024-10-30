from transformers import pipeline
from datasets import load_dataset

# Load a pre-trained question-answering model from Hugging Face
qa_pipeline = pipeline("question-answering")

# Load a dataset (using the "squad" dataset here as an example)
dataset = load_dataset("squad", split="train")

def find_context(question):
    """Find the most relevant context for a question."""
    for entry in dataset:
        if all(word in entry['context'].lower() for word in question.lower().split()):
            return entry['context']
    # Default to a general context if no specific match is found
    return "Artificial intelligence (AI) is the simulation of human intelligence in machines."

def get_answer(question, context):
    """Get an answer based on the question and context provided."""
    response = qa_pipeline({
        'question': question,
        'context': context
    })
    return response['answer']

if __name__ == "__main__":
    print("Welcome to the bot! Ask a question, or type 'exit' to quit.")

    while True:
        user_question = input("You: ")
        if user_question.lower() == "exit":
            print("Goodbye!")
            break

        # Find context for the current question
        context_text = find_context(user_question)
        answer = get_answer(user_question, context_text)
        print(f"Bot: {answer}")
