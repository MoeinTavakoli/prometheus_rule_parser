# Extract Data from Prometheus Alert Rules

This Python script extracts the `Team` and `Severity` from Prometheus alert rules located in a specified directory. The default directory is `./rules`, but this can be changed using the `-d` option.

## Requirements

- Python 3.x

## Usage

1. Place your Prometheus alert rule files in the directory of your choice.
2. Run the script with the appropriate directory path if not using the default `./rules`.

### Command Line Options

- `-d` or `--directory`: Specifies the directory containing the alert rules. The default is `./rules`.

### Example

```bash
python main.py -d /path/to/your/rules
```

## Output

The script prints the list of teams and severities extracted from all the `.rules` files in the specified directory, removing any duplicates.

## Notes

- Modify the `extract_teams_and_severities` function in the `extraction.py` module to fit the specific format and structure of your Prometheus alert rule files.