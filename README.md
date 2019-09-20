# best-practices

## style.py
1. Updated file to follow style guidelines using *pycodestyle*

## get_column_stats.py
1. Added *argparse* to handle the users inputs
2. Updated file to follow style guidelines using *pycodestyle*
3. Added exception to handle the input file not being formatted properly
4. Added exception to handle file inout errors

## basics_test.sh
5. Added tests to show that get_column_stats follows best practices

# functional-and-unit-testing

## get_column_stats.py
1. Added methods for finding the mean and standard deviation
2. Implemented checks and exception handling for the methods
3. Improved error handling in main function
      - File formatted incorrectly
      - Non integer characters in file
      - Dividing by zero in mean function
4. Add appropriate error print statments and exit codes

## basics_test.py
1. Added new file to run *unit testing* on the mean and standard deviation methods
2. Tests included:
      - checking for correct values on known and random lists
      - catching ZeroDivisionError and TypeError

## basics_test.sh
1. Updated existing tests to follow *sssh testing*
2. Added new tests to check proper behavior and error catching
3. Tests included:
      - passing a non existent file
      - passing a file containing non integer characters
      - passing a blank file

## .travis.yml
1. Updated file to run:
      - *pycodestyle* on basics_test.py
      - basics_test.py on get_column_stats.py
