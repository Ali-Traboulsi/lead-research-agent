import json
import csv

# Load the CSV data
csv_file = './customer_leads_agent_QA_data.csv'
json_data = []

try:
    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)

        # Loop through each row and extract question and answer pairs
        for row in csv_reader:
            # Ensure the keys match your CSV headers
            question_answer = {
                "question": row['prompt_text'],
                "answer": row['expected_response']
            }
            json_data.append(question_answer)

    # (Optional) Print or save json_data to verify the output
    print(json.dumps(json_data, indent=4))

except FileNotFoundError:
    print(f"Error: The file '{csv_file}' was not found.")
except KeyError as e:
    print(f"Error: Missing expected column in CSV file - {e}")


def load_config(path: str):
    with open(path, 'r') as json_file:
        loaded_file = json.load(json_file)
    print(f"Config file loaded from {path}")
    return loaded_file


