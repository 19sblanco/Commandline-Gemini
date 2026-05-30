# Gemini command line 
// description here


// note: this model has no context from previous prompts
// note: you can customize a message into prompt sent to gemini

## set up

### steps for install in your local environment

1. create a new gemini project

mkdir <gemini_project>
cd <gemini_project>

2. clone project

3. create a python virtual environment
$ sudo apt update
$ sudo apt install python3-venv  
$ python3 -m venv venv

4. activate the python virutal environment
$ source venv/bin/activate

5. install rich
$ pip install rich
// this helps you display mark down in a bash terminal


### connect the gemini model
https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/start?hl=en&_gl=1*17zfjba*_ga*MTAyNTUwNjM0Mi4xNzc3NzUxOTU4*_ga_WH2QY8WWF5*czE3ODAwNjQ1MjEkbzE4JGcxJHQxNzgwMDY1MTQzJGo0JGwwJGgw#python

use this link to set up and access the Gemini model API. Note that to access the Gemini API, you must have a Google Cloud Account and Project to connect it to. I recommend just creating a new project specifically for this.


