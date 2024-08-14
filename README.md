TODO:
- run queries for sampling
- organize code
- perform comparisons between roles/fields/work locations

Milestone:
- create a scripts/directions to be more clear and user-friendly

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

voila! all done!

*remember to delete query_results.txt file or its contents before running python3 find.py so
that all results are up to date instead of new results being appended below the old results