
Analysis (most notable ones):
- (#1) popular days for meetings on Mondays and Wednesdays
- (#5) top 3 types of creative work: architecture (77 hours), data (44 hours), plan (82 hours)
- (#6) least amount of time doing work is on Friday and most on Mondays-Wednesdays
- (#9) avg meeting time between managers and devlopers are 9.9 and 10.9 hours respectively (very close)
- (#13) meetings vs convo times for managerial role have a rough 1:1 ratio
- (#14) coding vs creative times for managerial is 1:4, technical 1:2

TODO (priority from top to bottom):
>>> focus on fixing logic for query results
   - 6 (triple check this)
   - 11 (# hours don't align on a typical work day)
   - 12 (check definition of coding via transcripts)
>> perform comparisons between roles/fields/work locations
> make folders for drafted diaries and processed diaries, respectively

Questions:
- Based on results of coding hours, perhaps look at transcripts and update csvs
   - look thru via 2-3 diary logs to calc code hours vs others
   - review query logic to see any discrepancies

Directions on how to run:
1) Run pip install -r requirements.txt in your terminal
2) Create a .env file. Within this set the URI, DB and COLLECTION variables. Use the .env_EXAMPLE as a template
3) Retrieve the diary CSV of your choice and place it in the same directory as with parse.py
4) Run the following line with file name being the diary CSV of your choice: python3 parse.py filename
5) Check if there is a new CSV created in the directory that starts with "d-" with your file name
6) Run the following line with file name being the diary CSV that you have parsed (ex: d-p3.csv): python3 convert.py filename
7) Check if the collection has been populated by filtering with {participant: "p#"} in the filter section on MongoDB
8) Run python3 find.py
9) Check if a new txt file is created called query_results.txt
10) To do this in bulk, firstly run convert.py in a shell window. This converts all the files beginning with p# (excluding 3 and 20) into the d- format. Then run upload.py to upload each of them to the database.

voila! all done!

*remember to delete query_results.txt file or its contents before running python3 find.py so
that all results are up to date instead of new results being appended below the old results