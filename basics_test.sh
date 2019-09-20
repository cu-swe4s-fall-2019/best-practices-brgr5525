test -e ssshtest || curl https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest -o ssshtest

source ssshtest

run test_pycodestyle_style pycodestyle style.py
assert_no_stdout

run test_pycodestyle_get_column_stats pycodestyle get_column_stats.py
assert_no_stdout

run test_pycodestyle_basics_test pycodestyle basics_test.py
assert_no_stdout

V=1
(for i in `seq 1 100`; do
    echo -e "$V\t$V\t$V\t$V\t$V";
done )> data.txt

run constant_int_file python get_column_stats.py --file_name data.txt --col_num 2
assert_in_stdout 'mean: 1.0'
assert_in_stdout 'stdev: 0.0'
assert_exit_code 0


(for i in `seq 1 100`; do
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done )> data.txt

run random_int_file python get_column_stats.py --file_name data.txt --col_num 2
assert_exit_code 0


run file_not_found python get_column_stats.py --file_name wrong_file.txt --col_num 2
assert_in_stdout 'File not found.'
assert_exit_code 1


V=1
X='a'
(for i in `seq 1 100`; do
    echo -e "$V\t$X\t$V\t$X\t$V";
done )> data.txt

run const_with_char_file python get_column_stats.py --file_name data.txt --col_num 2
assert_in_stdout 'File contains a non integer character!'
assert_exit_code 1


V=1
(for i in `seq 1 100`; do
    echo -e "$V\t$V\t$V\t$V\t$V";
done )> data.txt

run not_tab_delimited_file python get_column_stats.py --file_name data.txt --col_num 10
assert_in_stdout 'Column number is out of range!'
assert_exit_code 1


> data_empty.txt

run empty_file python get_column_stats.py --file_name data_empty.txt --col_num 0
assert_in_stdout 'Divide by zero! File may be empty.'
assert_exit_code 1
