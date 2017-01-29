#!/bin/sh

file=`date +'%Y%m%d'`.csv
echo 'name,creditcard' > $file

curl -s https://gist.githubusercontent.com/jorin-vogel/7f19ce95a9a842956358/raw/e319340c2f6691f9cc8d8cc57ed532b5093e3619/data.json | jq -r '.[] | select(.creditcard) | [.name, .creditcard] | @csv' >> $file
