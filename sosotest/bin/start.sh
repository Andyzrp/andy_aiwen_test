#!/bin/sh
echo "========***************开机自启开始********************========="
start_time=$(date +%s)
sleep 1
DIR="$(cd "$(dirname "$0")" && pwd)"
echo $DIR
#cd /usr/local/src/sosotest/
#check_results=`ls -l |awk '/^d/ {print $NF}'`
#echo "输出的文件目录未: $check_results"
end_time=$(date +%s)
cost_time=$[ $end_time-$start_time ]
echo "运行时间: $(($cost_time/60))min $(($cost_time%60))s"
