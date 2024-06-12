TODO:
- run queries for sampling
- organize code
- look at article for any potential queries
- fix directions

Milestone:
- create a scripts/directions to be more clear and user-friendly

Directions on how to run:
1) Run pip install -r requirements.txt in your terminal
2) Retrieve the diary CSV of your choice and place it in the same directory as with parse.py
3) Run the following line with file name being the diary CSV of your choice: python3 parse.py filename
4) Check if there is a new CSV created in the directory that starts with "d-" with your file name
5) Replace the "uri" on line 44 with your MongoDB information in convert.py
6) Run the following line with file name being the diary CSV that you have parsed (ex: d-p3.csv): python3 convert.py filename
7) Check if the collection has been populated by filtering with {participant: "p#"} in the filter section on MongoDB
8) Replace the "uri" on line 5 with your MongoDB information in find.py
9) Run python3 find.py
10) Check if a new txt file is created called query_results.txt

voila! all done!

*remember to delete query_results.txt file or its contents before running python3 find.py so
that all results are up to date instead of new results being appended below the old results
*remember to delete your personal uri when committing code