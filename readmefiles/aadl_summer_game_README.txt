# aadl_summer_game
Postman collection to batch-submit library codes for the Ann Arbor District Library Summer Game

You must be familiar with Postman to use this.  Some handy references:
* [Intro to collection runs](https://learning.getpostman.com/docs/postman/collection_runs/intro_to_collection_runs)
* [Working with data files](https://learning.getpostman.com/docs/postman/collection_runs/working_with_data_files)
* [Test scripts](https://learning.getpostman.com/docs/postman/scripts/test_scripts)
* [Postman Sandbox](https://learning.getpostman.com/docs/postman/scripts/postman_sandbox)

To get started:
1. Set the {{user}} and {{pass}} variables to your library username and password.
2. In the Collection Runner interface, check the "Keep variable values" and "Save cookies after collection run" boxes.  
3. In the View menu, choose Show Postman Console.
4. Configure only the Login script to run, and run the collection.  At this point, you should be logged in.
5. Create a .csv file with a single column and the header "gamecode" on the first line.

For example:
```csv
gamecode
SNACKATTACK
WACKBACKPACK
RALPHLAURENHILL
```

6. Change the collection to run only the Get Populated Form and Post Code scripts.
7. Use your CSV file as the data file.
8. Run the collection.  You should see your score increment in the Console window as each code is submitted.

