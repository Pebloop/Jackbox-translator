[⬅ back](../../../README.md)

# Version 1 : Project Features
*TranslatorBox/Dev documentation/Version 1/Project features*

# Creating a new project

# Analysing a project's game

# Layout manager

# SWF manager

## Decompiling a SWF

## Editing a SWF

## Rebuilding a SWF

# minigames manager

# Export

# Files structure

## Exported package structure

* Package structure
  * zip format
  * contain root folder of the game with every modified files
  * contain a data.json file

* data.json file :
```json
{
    "name": "JackBox 2 FR",
    "game": "Jackbox Party Pack 2",
    "language": "fr",
    "version": "1.0.0",
    "authors": ["French Jackbox Community"],
    "Translation-status": {
        "general": "Not started",
        "Earwax": "Not included",
        "Quiplash XL": "Ongoing",
        "Bidiots": "Finished",
        "Bomb Corps": "Not started"
    },
    "data": {
        // Additional content for specific games, like Trivial murder theme, for example.
    }
}
```