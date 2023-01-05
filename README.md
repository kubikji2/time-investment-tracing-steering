# TITS - Time Investment Tracing and Steering

Time Investment Tracing and Steering is a command-line utility to analyze time spent using the [ICREAM](https://github.com/kubikji2/icream) (ICal (RFC 5545) Extractor And Manager) and ICALs with a certain structure.

## How it works

- ICREAM is used to parse provided ICALs (either by a path to the folder or by file list)
- The tag file is used to classify `icream.calendar`s' `icream.event`s to the categories
  - Each category has aliases that groups events into a particular category
  - Each category has sub-categories
  - Is a category exclusive to a calendar 
  - Managed in `tits/category.py`
- The additional settings such as grouping by months/weeks produce results

## Roadmap

- [ ] 1. integrate ICREAM
- [ ] 2. create category format
- [ ] 3. create 

- [ ] decide categories
