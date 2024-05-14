import os
import yaml
import sys
from argparse import ArgumentParser

# Function to extract teams and severities from a YAML file
def extract_teams_and_severities(file_path):
    with open(file_path) as file:
        data = yaml.safe_load(file)
    
    groups = data.get('groups', [])
    teams_and_severities = []

    for group in groups:
        rules = group.get('rules', [])
        for rule in rules:
            labels = rule.get('labels', {})
            team = labels.get('team')
            severity = labels.get('severity')
            if team and severity:
                teams_and_severities.append({'team': team, 'severity': severity})

    return teams_and_severities

if __name__ == '__main__':
    parser = ArgumentParser(description='Process alert rules.')
    parser.add_argument('-d', '--directory', dest='rules_directory', default='./rules',
                        help='directory containing alert rules')
    args = parser.parse_args()

    rules_directory = args.rules_directory

    if os.path.exists(rules_directory):
        print(f'rules_directory = {rules_directory}')
        # List all YAML files in the directory
        yaml_files = [file for file in os.listdir(rules_directory) if file.endswith('.rules')]
        
        # List to store teams and severities from all files
        all_teams_and_severities = []

        # Iterate over each YAML file and extract teams and severities
        for yaml_file in yaml_files:
            file_path = os.path.join(rules_directory, yaml_file)
            teams_and_severities = extract_teams_and_severities(file_path)
            all_teams_and_severities.extend(teams_and_severities)

        # Remove duplicates
        all_teams_and_severities = [dict(t) for t in {tuple(d.items()) for d in all_teams_and_severities}]

        print("List of teams and severities from all rules:")
        for item in all_teams_and_severities:
            print(f"Team: {item['team']}, Severity: {item['severity']}")
    else:
        raise Exception("No such file or directory!")
