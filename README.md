# SEM1 AlgoProg Final Project

## Project Overview

### 1. Calendar Application

`Calendar.py` is a command-line calendar manager built with Python's standard `calendar` and `datetime` modules.

Main features:

- View a selected month and year in calendar format
- Highlight user events with ANSI terminal colors
- Highlight predefined global holidays
- Add custom events with descriptions and colors
- Repeat events weekly for a chosen number of weeks
- Remove events from a selected month
- Print a full 12-month summary for a selected year

Core structure:

- `Event` class stores day, month, year, description, and color
- `CalendarApp` manages events, holidays, rendering, and menu actions
- The script runs through an interactive terminal menu

## Requirements

### For `Calendar.py`

No external packages are required.

- Python 3.x

The program opens an interactive menu with these options:

- View Calendar
- Add Events
- Remove Events
- Summary
- Exit

## Notes

- `Calendar.py` uses ANSI escape codes for color output, so colors depend on terminal support.
- The calendar script includes sample events and predefined holidays.