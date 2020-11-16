
cd /home/sheepbot/Bot

for i in `seq 0 39`;
do
	bash single.sh $i&
done

while [ true ];
do
	sleep 10m
done
