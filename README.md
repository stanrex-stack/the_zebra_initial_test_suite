## Installation

Pre requirements: you need to have Chrome browser of version 84 installed.

Project includes chromedriver binary file for Mac.
If you are on Windows, you need to download chromedriver and put it into features/support package.
Then modify features/environment.py file to use downloaded driver.

1. Download [Python](https://www.python.org/downloads/) (do NOT use python version below 3.5).
2. Install Python from downloaded package.
3. Open project, configure it to use Python3. Then navigate to the project directory from your terminal, run:
```pip3 install -r requirements.txt```
4. To run all the tests from terminal, inside the project, run ```behave features```
5. To run the tests WITH report, inside the project, run ```behave -f allure_behave.formatter:AllureFormatter -o test_results ./features```
6. To generate report, run ```allure serve test_results``` (Press Ctrl+C to exit)


#### Behave
**features package** contains tests (feature file scenarios), steps, and environment.
- feature files contain test scenarios written as text with behave keywords
- test steps define scenario statements and translate English text to Python
- environment.py file links test steps to *app* package and defines set of methods to execute _before_ and _after_ every test
feature/scenario/step.

[Official documentation](https://behave.readthedocs.io/en/latest/) about BDD, keywords, and running behave scenarios.

