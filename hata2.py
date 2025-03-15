from pprint import pprint
import json
import time
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

try:
    openai_key = os.getenv('OPENAI_KEY')
    org_ID = os.getenv('ORG_ID')

    client = OpenAI(
        organization=org_ID,
        api_key=openai_key
    )

    # List the last 5 assistants
    try:
        my_assistants = client.beta.assistants.list(order="desc", limit="5")
    except Exception as e:
        print(f"Error listing assistants: {e}")
        exit(1)

    # Retrieve a specific assistant
    try:
        assistant = client.beta.assistants.retrieve("asst_W9WhhX3DRDu8e0A5T5TjQMup")
    except Exception as e:
        print(f"Error retrieving assistant: {e}")
        exit(1)

    # Create a new thread
    try:
        thread = client.beta.threads.create()
    except Exception as e:
        print(f"Error creating thread: {e}")
        exit(1)

    # Send a message to the thread
    try:
        message = client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content="lompat"
        )
    except Exception as e:
        print(f"Error sending message to thread: {e}")
        exit(1)

    # Run the assistant
    try:
        run = client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant.id
        )
    except Exception as e:
        print(f"Error running assistant: {e}")
        exit(1)

    # Wait for completion
    while True:
        try:
            run = client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id
            )
            if run.status == 'completed':
                break
            else:
                time.sleep(1)
        except Exception as e:
            print(f"Error while waiting for run to complete: {e}")
            exit(1)

    # Retrieve and print responses
    try:
        messages = client.beta.threads.messages.list(thread_id=thread.id)
        for each in messages:
            if each.role == 'assistant':
                if isinstance(each.content, list) and hasattr(each.content[0], 'text'):
                    print("Assistant: " + each.content[0].text.value)
                else:
                    print("Assistant message content: " + str(each.content))
    except Exception as e:
        print(f"Error retrieving messages: {e}")
    finally:
        # Close the thread or perform any final thread management here
        pass

except Exception as e:
    print(f"Unhandled exception: {e}")
