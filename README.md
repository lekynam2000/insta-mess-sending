# insta-mess-sending

#Assume that python and pip installer are available in the use machine. 
#Installation step: 
Install [chromedriver](https://chromedriver.chromium.org/downloads)
Install Selenium and Xlrd by using terminal:

```
pip install selenium
pip install xlrd
```
Go to input.xlsx file and edit base on what you need in the first 2 colums of Excel in this format:

The sentence you want to type|Delay time after typing the previous sentence
-----------------------------|---------------------------------------------
This sentence will delay 1s|1
After 1s from enter the above sentence|3

Go to index.py and find two variable userName and password:

```python
userName = #type your Facebook user name here
password = #type your password here
```

Find the variable vnntufoc:
```python
vnntufoc = #type your Xpath to the person you want to chat with
```
