TODO:
- run queries for sampling

Milestone:
- create a scripts/directions to be more clear and user-friendly

Directions on how to run:
1) Retrieve the diary CSV of your choice and place it in the same directory as with parse.py
2) Run the following line with file name being the diary CSV of your choice: python3 parse.py <filename>
3) Check if there is a new CSV created that starts with "d-" with your file name
4) Hard code that "d-<filename>" into line 5 in the diaries.py
5) Replace the <username><password>@<projectname> on line 52 with your MongoDB information
6) Run python3 diaries.py
7) Check if the collection has been populated on MongoDB
8) voila!