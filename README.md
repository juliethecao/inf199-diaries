TODO:
- run queries for sampling
- organize code
- look at article for any potential queries
- fix directions

Milestone:
- create a scripts/directions to be more clear and user-friendly

Directions on how to run:
1) Retrieve the diary CSV of your choice and place it in the same directory as with parse.py
2) Run the following line with file name being the diary CSV of your choice: python3 parse.py filename
3) Check if there is a new CSV created that starts with "d-" with your file name
4) Hard code that "d-filename" into line 5 in convert.py
5) Replace the "uri" on line 44 with your MongoDB information in convert.py
6) Run python3 convert.py
7) Check if the collection has been populated on MongoDB
8) Replace the "uri" on line 5 with your MongoDB information in find.py
9) Run python3 find.py
10) Check if a new txt file is created called output_file.txt
11) voila! all done!