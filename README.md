# LogParserProject
This is the code for third udacity project. The code allows you to use python to interface with a postgresql database. psycopg2 was the python-db API implemented in this project. 

### Downloads

The code can be downloaded from the following repo:

https://github.com/enmanuel17/LogParserProject.git

## REQUIREMENTS:
Python 3 ONLY
Install the following libraries:

- psycopg2
```pip3 install psycopg2```
for more info regarding the library look here http://initd.org/psycopg/docs/install.html

## Views needed
Please create this view before running the code:
```create view dates as
select cast(time as date) as date from log group by cast(time as date);```
## How to Use:

The application can be run with the following ways:
- Typing ```python dbParselog.py``` from the linux command line.

## LICENSE
MIT License

Copyright (c) 2017 Enmanuel Hernandez

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
