#!/bin/bash
sh my_resume_scraper.sh $1
python textToJsonConvert.py
python filter.py
