#! /bin/bash


#printf "\n*********  RUN TESTS  *******\n"
echo "*****************************"
python3 -m pytest --disable-pytest-warnings -vv --gherkin-terminal-reporter --cucumberjson=$REPORT_PATH -m "precipitation" -s
echo "*****************************"


