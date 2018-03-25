COUNT=$(python /usr/hdp/current/phoenix-client/bin/sqlline.py < ~/a.sql)
PATH="/root/s.txt"
read CUN < $PATH
echo $COUNT
echo $CUN
