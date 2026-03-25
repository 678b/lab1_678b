#!/bin/bash

FILE="grades.csv"
ARCHIVE_DIR="archive"
LOG_FILE="organizer.log"

# Check if grades.csv exists
if [ ! -f "$FILE" ]; then
    echo "Error: $FILE does not exist."
    exit 1
fi

# Create archive directory if it does not exist
if [ ! -d "$ARCHIVE_DIR" ]; then
    mkdir "$ARCHIVE_DIR"
    echo "Archive directory created."
fi

# Generate timestamp
TIMESTAMP=$(date +"%Y%m%d-%H%M%S")

# New filename
NEW_NAME="grades_$TIMESTAMP.csv"

# Move and rename file
mv "$FILE" "$ARCHIVE_DIR/$NEW_NAME"

# Check if move was successful
if [ $? -eq 0 ]; then
    echo "File archived successfully."

    # Create new empty grades.csv
    touch "$FILE"

    # Logging
    echo "$TIMESTAMP | Original: $FILE | Archived: $ARCHIVE_DIR/$NEW_NAME" >> "$LOG_FILE"

else
    echo "Error: Failed to archive file."
    exit 1
fi