
```bash
[ $[ $RANDOM % 6 ] == 0 ]|| echo "hited"
```

$date +%s
1754264011

$date +%D
08/03/25

$date -d "3 days ago"

$date +"%Y-%m-%d %H:%m:%S"
2025-08-03 23:08:23

┌─[user@parrot]─[~]
└──╼ $mkdir -m 777 task

ps aux|grep -v -n bin  # -v 不包含 -n行号


$grep --help
Usage: grep [OPTION]... PATTERNS [FILE]...
Search for PATTERNS in each FILE.
Example: grep -i 'hello world' menu.h main.c
PATTERNS can contain multiple patterns separated by newlines.

Pattern selection and interpretation:
  -E, --extended-regexp     PATTERNS are extended regular expressions
  -F, --fixed-strings       PATTERNS are strings
  -G, --basic-regexp        PATTERNS are basic regular expressions
  -P, --perl-regexp         PATTERNS are Perl regular expressions
  -e, --regexp=PATTERNS     use PATTERNS for matching
  -f, --file=FILE           take PATTERNS from FILE
  -i, --ignore-case         ignore case distinctions in patterns and data
      --no-ignore-case      do not ignore case distinctions (default)
  -w, --word-regexp         match only whole words
  -x, --line-regexp         match only whole lines
  -z, --null-data           a data line ends in 0 byte, not newline

Miscellaneous:
  -s, --no-messages         suppress error messages
  -v, --invert-match        select non-matching lines
  -V, --version             display version information and exit
      --help                display this help text and exit

Output control:
  -m, --max-count=NUM       stop after NUM selected lines
  -b, --byte-offset         print the byte offset with output lines
  -n, --line-number         print line number with output lines
      --line-buffered       flush output on every line
  -H, --with-filename       print file name with output lines
  -h, --no-filename         suppress the file name prefix on output
      --label=LABEL         use LABEL as the standard input file name prefix
  -o, --only-matching       show only nonempty parts of lines that match
  -q, --quiet, --silent     suppress all normal output
      --binary-files=TYPE   assume that binary files are TYPE;
                            TYPE is 'binary', 'text', or 'without-match'
  -a, --text                equivalent to --binary-files=text
  -I                        equivalent to --binary-files=without-match
  -d, --directories=ACTION  how to handle directories;
                            ACTION is 'read', 'recurse', or 'skip'
  -D, --devices=ACTION      how to handle devices, FIFOs and sockets;
                            ACTION is 'read' or 'skip'
  -r, --recursive           like --directories=recurse
  -R, --dereference-recursive  likewise, but follow all symlinks
      --include=GLOB        search only files that match GLOB (a file pattern)
      --exclude=GLOB        skip files that match GLOB
      --exclude-from=FILE   skip files that match any file pattern from FILE
      --exclude-dir=GLOB    skip directories that match GLOB
  -L, --files-without-match  print only names of FILEs with no selected lines
  -l, --files-with-matches  print only names of FILEs with selected lines
  -c, --count               print only a count of selected lines per FILE
  -T, --initial-tab         make tabs line up (if needed)
  -Z, --null                print 0 byte after FILE name

Context control:
  -B, --before-context=NUM  print NUM lines of leading context
  -A, --after-context=NUM   print NUM lines of trailing context
  -C, --context=NUM         print NUM lines of output context
  -NUM                      same as --context=NUM
      --group-separator=SEP  print SEP on line between matches with context
      --no-group-separator  do not print separator for matches with context
      --color[=WHEN],
      --colour[=WHEN]       use markers to highlight the matching strings;
                            WHEN is 'always', 'never', or 'auto'
  -U, --binary              do not strip CR characters at EOL (MSDOS/Windows)

When FILE is '-', read standard input.  With no FILE, read '.' if
recursive, '-' otherwise.  With fewer than two FILEs, assume -h.
Exit status is 0 if any line is selected, 1 otherwise;
if any error occurs and -q is not given, the exit status is 2.

Report bugs to: bug-grep@gnu.org
GNU grep home page: <https://www.gnu.org/software/grep/>
General help using GNU software: <https://www.gnu.org/gethelp/>

$echo "scale=7;355/113" |bc
3.1415929
$echo "ibase=16;obase=2;FF"|bc
11111111
$echo "scale=30; a(1)*4" | bc -l
3.141592653589793238462643383276

$echo -e "\033[47;36m isgsi gggg\033[0m"
 isgsi gggg
47 白色背景 36天蓝前景 黑30 红31 绿 黄 蓝 紫 天蓝 白37

printf "\033[31m红色文字\033[0m\n"

$ip a

$seq 10

$seq -s ' ' 97 $((97+25))

$seq -s ' '  5 -0.2 4
5.0 4.8 4.6 4.4 4.2 4.0

seq [OPTION]... FIRST INCREMENT LAST

for i in $(seq 1 10); do printf "%03d\t" "$i"; done
for i in {1..5}; do echo $i; done

END=5
for ((i=1;i<=END;i++)); do
    echo $i
done

#!/bin/sh
limit=4

i=1; while [ $i -le $limit ]; do
  echo $i
  i=$(($i + 1))
done

time (seq 1 1000000 | wc)
echo {A..z}

echo {20..10..-2}

$echo {A..z..5}
A F K P U Z _ d i n s x