import yaml

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