import csv
import os
import re
import yaml
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
from dataclasses import dataclass

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants
TITLE_COLUMN = "ma"
DESCRIPTION_COLUMN = "description"
SPEAKER_COLUMN = "Speaker Name"
TWITTER_COLUMN = "twitter"
GITHUB_COLUMN = "github"
LINKEDIN_COLUMN = "linkedin"
ORGANIZATION_COLUMN = "organization"
BIO_COLUMN = "bio"

@dataclass
class Speaker:
    name: str
    position: str = "TODO"
    image: str = "TODO"
    about: str = "TODO"
    linkedin: str = "TODO"
    twitter: str = "TODO"
    github: str = "TODO"

@dataclass
class Talk:
    title: str
    description: str = "TODO"
    speaker_name: str = "TODO"  # Reference to speaker by name
    day: str = "TODO"
    stage: str = "TODO"
    time: str = "TODO"

def slugify(text: str) -> str:
    """Convert text to a valid filename, limited to 5 words."""
    # Convert to lowercase
    text = text.lower()
    # Split into words and take first 5
    words = text.split()
    text = ' '.join(words[:5])
    # Replace spaces and special chars with hyphens
    text = re.sub(r'[^a-z0-9]+', '-', text)
    # Remove leading/trailing hyphens
    text = text.strip('-')
    return text

def generate_speaker_image_url(speaker_name: str) -> str:
    """Generate image URL for a speaker based on the naming pattern."""
    # Convert name to lowercase and replace spaces with hyphens
    name_slug = slugify(speaker_name)
    return f"assets/img/2025/speakers/{name_slug}.jpg"

def load_schedule_csv(filepath: str) -> Dict[str, Talk]:
    """Load and parse the schedule CSV file to create the initial talks data structure."""
    print('Loading schedule from', filepath)

    talks: Dict[str, Talk] = {}
    current_day = None
    day_num = 0
    current_time = None
    next_time = None
    found_wednesday = False

    with open(filepath, 'r', encoding='utf-8') as f:
        rows = list(csv.reader(f))  # Read all rows to look ahead

        for i, row in enumerate(rows):
            # Skip completely empty rows
            if not any(row):
                continue

            # Check for day header (e.g., "Monday 18 August")
            if row[0] and ('Wednesday' in row[0] or 'Thursday' in row[0]):
                if 'Wednesday' in row[0]:
                    found_wednesday = True
                current_day = row[0].split(',')[0]
                day_num = list(['Tuesday', 'Wednesday', 'Thursday']).index(current_day.split()[0]) + 1

            # Skip all rows until we find Wednesday
            if not found_wednesday:
                continue

            # Update time if present in the row
            if row[1]:
                current_time = row[1]
                # Look ahead to find next time slot
                next_time = None
                if i + 1 < len(rows) and rows[i+1][1] and rows[i+1][1] != current_time:
                    next_time = rows[i+1][1]

            # Process each stage column (2-5)
            for stage_num, col_idx in enumerate([2, 3, 4, 5], 1):
                if col_idx >= len(row) or not row[col_idx]:
                    continue

                content = row[col_idx]

                # Skip if it's a break, lunch, or other non-talk event
                if any(skip in content.lower() for skip in ['break', 'lunch', 'registration', 'keynote', 'panel', 'end of day', 'networking']):
                    continue

                # Extract talk title (remove rating if present)
                if ' - ' in content:
                    # Split on last " - " to handle titles that might contain dashes
                    talk_title = content.rsplit(' - ', 1)[0]
                else:
                    talk_title = content

                # Skip if it's not a talk
                if not talk_title or talk_title == '#N/A':
                    continue

                # Create time range
                time_range = f"{current_time} - {next_time}" if next_time else current_time

                talk = Talk(
                    title=talk_title,
                    day=f"day{day_num}",
                    stage=f"stage{stage_num}",
                    time=time_range
                )
                talks[talk_title] = talk

    return talks

def load_submissions_csv(filepath: str, existing_talks: Dict[str, Talk]) -> Tuple[Dict[str, Talk], Dict[str, Speaker]]:
    """Load and parse the submissions CSV file to update talks and create speakers data structure."""
    print('Loading submissions from', filepath)

    speakers: Dict[str, Speaker] = {}

    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['state'] == 'rejected' or row[TITLE_COLUMN] not in existing_talks:
                continue
            # Create or update speaker
            speaker_name = row[SPEAKER_COLUMN]
            if speaker_name not in speakers:
                speakers[speaker_name] = Speaker(
                    name=speaker_name,
                    position=row.get(ORGANIZATION_COLUMN, "TODO"),
                    about=row.get(BIO_COLUMN, "TODO"),
                    linkedin=row.get(LINKEDIN_COLUMN, "TODO"),
                    twitter=row.get(TWITTER_COLUMN, "TODO"),
                    github=row.get(GITHUB_COLUMN, "TODO")
                )

            # Update existing talk if it exists
            talk_title = row[TITLE_COLUMN]
            if talk_title in existing_talks:
                existing_talks[talk_title].description = row[DESCRIPTION_COLUMN]
                existing_talks[talk_title].speaker_name = speaker_name

    return existing_talks, speakers

def load_old_speakers_yaml(filepath: str) -> Dict[str, Speaker]:
    """Load and parse the old speakers YAML file."""
    print('Loading old speakers from', filepath)

    with open(filepath, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    speakers = {}
    for speaker_data in data['speakers']:
        speaker = Speaker(
            name=speaker_data['name'],
            position=speaker_data.get('position', "TODO"),
            image=speaker_data.get('image', "TODO"),
            about=speaker_data.get('about', "TODO"),
            linkedin=speaker_data.get('linkedin', "TODO"),
            twitter=speaker_data.get('twitter', "TODO"),
            github=speaker_data.get('github', "TODO")
        )
        speakers[speaker.name] = speaker

    return speakers

def generate_talk_file(talk: Talk, output_dir: str) -> None:
    """Generate a markdown file for a talk."""
    filename = f"{slugify(talk.title)}.md"
    filepath = os.path.join(output_dir, filename)

    content = f"""---
title: "{talk.title}"
day: {talk.day}
stage: {talk.stage}
time: {talk.time}
speaker: {talk.speaker_name}
---

{talk.description}
"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    logger.info(f"Created {filepath}")

def generate_schedule_yaml(talks: Dict[str, Talk], speakers: Dict[str, Speaker], output_file: str) -> None:
    """Generate the schedule YAML file."""
    yaml_data = {
        'days': [
            {'id': 'day1', 'title': 'Day 1', 'date': 'Aug 18th', 'stages': ['stage1']},
            {'id': 'day2', 'title': 'Day 2', 'date': 'Aug 19th', 'stages': ['stage1']},
            {'id': 'day3', 'title': 'Day 3', 'date': 'Aug 20th', 'stages': ['stage1', 'stage2', 'stage3', 'stage4']},
            {'id': 'day4', 'title': 'Day 4', 'date': 'Aug 21st', 'stages': ['stage1', 'stage2', 'stage3', 'stage4']}
        ],
        'stages': [
            {'id': 'stage1', 'title': 'Stage 1 (Name 1)'},
            {'id': 'stage2', 'title': 'Stage 2 (Name 2)'},
            {'id': 'stage3', 'title': 'Stage 3 (Name 3)'},
            {'id': 'stage4', 'title': 'Stage 4 (Name 4)'}
        ],
        'speakers': []
    }

    # Add speakers
    for speaker in speakers.values():
        # Generate image URL based on speaker name
        image_url = generate_speaker_image_url(speaker.name)

        yaml_data['speakers'].append({
            'name': speaker.name,
            'position': speaker.position,
            'image': image_url,
            'about': speaker.about,
            'talk': next((slugify(talk.title) for talk in talks.values() if talk.speaker_name == speaker.name), "TODO"),
            'linkedin': speaker.linkedin if speaker.linkedin != "TODO" else "",
            'twitter': speaker.twitter if speaker.twitter != "TODO" else "",
            'github': speaker.github if speaker.github != "TODO" else ""
        })

    with open(output_file, 'w', encoding='utf-8') as f:
        yaml.dump(yaml_data, f, allow_unicode=True, sort_keys=False)

    logger.info(f"Created {output_file}")

def generate_talks_yaml(talks: Dict[str, Talk], output_file: str) -> None:
    """Generate the talks-2025.yml file for the site's Liquid templates."""
    print('Generating talks-2025.yml file for the site\'s Liquid templates')
    yaml_data = []

    for talk in talks.values():
        yaml_data.append({
            'title': talk.title,
            'day': talk.day,
            'stage': talk.stage,
            'time': talk.time,
            'speaker': talk.speaker_name,
            'url': f"/editions/2025/talks/{slugify(talk.title)}"
        })

    with open(output_file, 'w', encoding='utf-8') as f:
        yaml.dump(yaml_data, f, allow_unicode=True, sort_keys=False)

    logger.info(f"Created {output_file}")

def main():
    # Input and output paths
    base_dir = Path(".")
    data_dir = base_dir / "data"
    dest_dir = base_dir / "dest"
    talks_dir = dest_dir / "talks"

    # Create output directories
    if os.path.exists(dest_dir):
        import shutil
        shutil.rmtree(dest_dir)
    os.makedirs(dest_dir, exist_ok=True)
    os.makedirs(talks_dir, exist_ok=True)

    try:
        # Load initial talks from schedule
        talks = load_schedule_csv(data_dir / "schedule.csv")

        # Load submissions to update talks and create speakers
        talks, speakers = load_submissions_csv(data_dir / "submissions.csv", talks)

        # Load old speakers data
        old_speakers = load_old_speakers_yaml(data_dir / "schedule-old.yml")

        # Update speaker information from old speakers
        for speaker_name, speaker in speakers.items():
            if speaker_name in old_speakers:
                old_speaker = old_speakers[speaker_name]
                # Only update fields that are not already set
                if speaker.position == "TODO":
                    speaker.position = old_speaker.position
                if speaker.image == "TODO":
                    speaker.image = old_speaker.image
                if speaker.about == "TODO":
                    speaker.about = old_speaker.about
                if speaker.linkedin == "TODO":
                    speaker.linkedin = old_speaker.linkedin
                if speaker.twitter == "TODO":
                    speaker.twitter = old_speaker.twitter
                if speaker.github == "TODO":
                    speaker.github = old_speaker.github

        # Create logs directory and write debug files
        logs_dir = base_dir / "logs"
        if os.path.exists(logs_dir):
            import shutil
            shutil.rmtree(logs_dir)
        os.makedirs(logs_dir, exist_ok=True)

        # Write talks debug file
        with open(logs_dir / "talks_debug.yml", "w", encoding="utf-8") as f:
            yaml.dump(talks, f, allow_unicode=True, sort_keys=False)

        # Write speakers debug file
        with open(logs_dir / "speakers_debug.yml", "w", encoding="utf-8") as f:
            yaml.dump(speakers, f, allow_unicode=True, sort_keys=False)

        logger.info(f"Debug files written to {logs_dir}")

        # Generate output files
        for talk in talks.values():
            generate_talk_file(talk, talks_dir)

        generate_schedule_yaml(talks, speakers, dest_dir / "schedule.yml")
        generate_talks_yaml(talks, dest_dir / "talks-2025.yml")

        # Print summary
        logger.info(f"Processed {len(talks)} talks and {len(speakers)} speakers")
        missing_metadata = [speaker.name for speaker in speakers.values()
                          if speaker.position == "TODO" or speaker.image == "TODO"]
        if missing_metadata:
            logger.warning(f"Missing speaker metadata for: {', '.join(missing_metadata)}")

    except Exception as e:
        logger.error(f"Error processing files: {str(e)}")
        raise

if __name__ == "__main__":
    main()