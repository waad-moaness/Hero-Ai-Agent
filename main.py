def main():
    print("Hello from hero-ai-agent!")


if __name__ == "__main__":
    main()
import ingest
import search_agent 
import logs

import asyncio


REPO_OWNER = "huggingface"
REPO_NAME = "hub-docs"

def initialize_index():
    print(f"Starting AI Assistant for {REPO_OWNER}/{REPO_NAME}")
    print("Initializing data ingestion...")


    index = ingest.index_data(REPO_OWNER, REPO_NAME)
    print("Data indexing completed successfully!")
    return index


def initialize_agent(index):
    print("Initializing search agent...")
    agent = search_agent.init_agent(index, REPO_OWNER, REPO_NAME)
    print("Agent initialized successfully!")
    return agent


def main():
    index = initialize_index()
    agent = initialize_agent(index)
    print("\nReady to answer your questions!")
    print("Type 'stop' to exit the program.\n")

    while True:
        question = input("Your question: ")
        if question.strip().lower() == 'stop':
            print("Goodbye!")
            break

        print("Processing your question...")
        response = asyncio.run(agent.run(user_prompt=question))
        logs.log_interaction_to_file(agent, response.new_messages())

        print("\nResponse:\n", response.output)
        print("\n" + "="*50 + "\n")


if __name__ == "__main__":
    main()
