# Gemini command line 
Have you ever wanted to use AI in your command line, but can't afford claude code? This custom built program lets you use Gemini-2.5-Flash model in the command line

> note: This model has no context from previous prompts. This is both a good and bad thing.

## how to use

!! video of you using it

!! add -s flag for small responses

## set up

### steps for install

***Prerequisites: To access the Gemini-2.5-Flash API, you need a Google Cloud Account***

1. clone project

2. create and activate python virtual environment
```bash
$ sudo apt update
$ sudo apt install python3-venv  
$ python3 -m venv venv
$ source venv/bin/activate
```

3. install rich to display mark down in bash
```bash
$ pip install rich
```

4. create context.txt file
    a. This step is optional, but very helpful. I add system information and preferences to mine.

5. add bash alias to .bashrc
```bash
alias gemini='Commandline-Gemini/.venv/bin/python Commandline-gemini/gemini.py'
```

***update path based on where your Commandline-Gemini file lives***

6. connect the gemini model

These are the relevant headings in the following tutorial
* **Before you begin**
    * this projects, as is, assumes ADC authentication
* **Set up required roles**
* **Install the SDK and set up your environment**

> Note: To access the Gemini API, you must have a Google Cloud Account and Project to connect to. After you have an account created, I recommend just creating a new project specifically for this.

[Connect Gemini-2.5-Flash](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/start?hl=en&_gl=1*17zfjba*_ga*MTAyNTUwNjM0Mi4xNzc3NzUxOTU4*_ga_WH2QY8WWF5*czE3ODAwNjQ1MjEkbzE4JGcxJHQxNzgwMDY1MTQzJGo0JGwwJGgw#python) Note 

