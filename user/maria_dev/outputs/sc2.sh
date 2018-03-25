COUNT=$(python /usr/hdp/current/phoenix-client/bin/sqlline.py < ~/a.sql)
PATH="/root/y.txt"
echo "$COUNT" > s.txt
while read cur; do a="${a}${cur}"; done < y.txt
while read cur; do b="${b}${cur}"; done < s.txt
if [ "$a" == "$b" ]
then
    echo "same"
fi
