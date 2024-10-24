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