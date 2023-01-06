# TITS - Time Investment Tracing and Steering

Time Investment Tracing and Steering is a command-line utility to analyze time spent using the [ICREAM](https://github.com/kubikji2/icream) (ICal (RFC 5545) Extractor And Manager) and ICALs with a certain structure.

## How it works

- ICREAM is used to parse provided ICALs (either by a path to the folder or by file list)
  - ICALs events are expected to be labeled in followingformat:
    ```
    '[' + <tag> + '-' + <activity> + ']' + <event name, or additional information>
    ```
    - where tag (such as project name, 'AS', 'DoD') is usually unique to the calendar, but activity (such as 'writing', 'reading', 'coding', 'emails', 'tutorials') can be shared across multiple tags
    - the tag is used to trace how much time was dedicated to a given project
    - the activity label is used to steer the future time investments into particular project area
- The classification file is used to classify `icream.calendar`s' `icream.event`s to the categories
  - Each category has aliases that groups events into a particular category
  - Each category is usually exclusive to a calendar
  - Activities are shared across the categories and calendars 
  - Classification is managed in `tits/category.py`
- The additional settings such as grouping by months/weeks produce results

## Roadmap

- [ ] 1. integrate ICREAM
- [ ] 2. create category format
- [ ] 3. create 

- [ ] decide categories
