#!/bin/bash

chmod -x basics_test.sh

echo ...running pycodestyle on style.py...
pycodestyle style.py

echo ...running pycodestyle on get_column_stats.py...
pycodestyle get_column_stats.py

echo ...running get_column_stats.py -h...
python get_column_stats.py -h

echo ...running get_column_stats with wrong_file.txt...
python get_column_stats.py --file_name wrong_file.txt --col_num 2

echo ...running get_column_stats using original tests...
(for i in `seq 1 100`; do
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done )> data.txt

 python get_column_stats.py --file_name data.txt --col_num 2


V=1
(for i in `seq 1 100`; do
    echo -e "$V\t$V\t$V\t$V\t$V";
done )> data.txt

python get_column_stats.py --file_name data.txt --col_num 2
