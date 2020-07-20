# Credit card challenge

Note: this challenge (and the input data) is stolen shamelessly from a
[Gist posted by Jorin
Vogel](https://gist.github.com/jorinvo/2e43ffa981a97bc17259). Don't
click that link until you've tried to solve the problem; it's literally
a list of solutions!

The file
[data.json](https://gist.githubusercontent.com/jorinvo/7f19ce95a9a842956358/raw/e319340c2f6691f9cc8d8cc57ed532b5093e3619/data.json)
contains the credit card information of a cache of stolen credit cards
in JSON objects. 

Your job is to save the names and credit card numbers to a CSV file
whose columns should be `name` and `creditcard`. The CSV file should be
named `20150516.csv` where `20150516` should be replaced with today's
date in YYYYMMDD (ISO) format. One complication: not every record has a
credit card number. These records should not be included in your output.

## Bonus

No Python! Solve this problem using only `curl` and
[jq](https://stedolan.github.io/jq/). If you decide to try this, don't
look at `solution.sh`!
