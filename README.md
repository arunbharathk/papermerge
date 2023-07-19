# PaperMergeTest

This repository contains automation tests for the Papermerge website.

## Prerequisites

Before running the automation, ensure the following:

1. **Papermerge Website**: Make sure the Papermerge website is up and running.

2. **Python and pip**: Ensure you have the latest version of Python (at least 3.11) installed on your system. You also need pip3 (Python package manager) installed.

## Installation

Follow the steps below to set up and run the automation:

### Step 1:
Ensure you have the latest Python version and pip3 installed on your system.

### Step 2:
Install the required libraries using pipenv. To do this, follow these steps:

1. Make sure you have pipenv installed on your system. If not, you can install it using pip:

   ```bash
   pip install pipenv
   ```

2. Navigate to your project's directory using the command line.

3. Activate your project's virtual environment using pipenv:

   ```bash
   pipenv shell
   ```

4. Install the required libraries using the following command (ignoring any installed packages from a previous environment):

   ```bash
   pipenv install --ignore-Pipfile
   ```

## Running the Automation

Once you have set up the environment and installed the required libraries, you can run the automation using the following pipenv command:

```bash
pipenv run pytest -s
```

This command will execute the automation tests, generate an HTML report under the "reports/failure" directory, and display the test results on the console.

Additionally, the automation is configured to capture screenshots for any failures. Screenshots will be saved in the "reports/screenshots" directory.


