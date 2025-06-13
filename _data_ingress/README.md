# Data Ingress Scripts

This directory contains scripts for processing and importing data into the Scala Days website.

## Talk Generation Script

The `generate_talk_files.py` script processes talk submissions and schedule data to generate markdown files for each talk and a schedule YAML file.

### Prerequisites

- Python 3.x
- Required Python packages (install using pip):
  ```bash
  pip install -r _data_ingress/requirements.txt
  ```

### Input Files

Place the following files in the `_data_ingress/data` directory:

1. `schedule.csv` - Conference schedule with talk times and locations
2. `submissions.csv` - Talk submissions with speaker information
3. `schedule-old.yml` - Previous schedule file with additional speaker metadata

### Usage

1. Ensure all input files are in the `_data_ingress/data` directory
2. Run the script from the project root:
   ```bash
   python _data_ingress/generate_talk_files.py
   ```

The script will:
- Process all input files
- Generate markdown files for each talk in `_data_ingress/dest/talks`
- Create a new schedule YAML file in `_data_ingress/dest/schedule.yml`
- Log progress and any issues encountered

### Output

1. **Talk Markdown Files**
   - Location: `_data_ingress/dest/talks/`
   - Format:
   ```markdown
   ---
   title: "Talk Title"
   day: day1
   stage: stage1
   time: 10:00
   speaker: Speaker Name
   ---

   Talk description...
   ```

2. **Schedule YAML**
   - Location: `_data_ingress/dest/schedule.yml`
   - Contains:
     - Days and stages configuration
     - Speaker information
     - Talk assignments

### Error Handling

The script includes robust error handling:
- Logs all major steps and any issues
- Continues processing even if some data is missing
- Provides a summary of processed talks and missing metadata
- Raises exceptions for critical errors

### Logging

The script logs:
- File creation events
- Number of talks processed
- Missing speaker metadata
- Any errors encountered

Check the console output for the processing summary and any warnings or errors.