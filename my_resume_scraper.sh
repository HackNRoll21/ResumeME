#!/bin/bash
saveLocation="/home/sean/Desktop/ResumeWriter"
out="out"

if [ ! -w $saveLocation ]
then
	echo Please let me write to the save location
	exit
else
	test -f $saveLocation/$out.json && rm $saveLocation/$out.json
fi

cd ResumeWriter/ResumeWriter/spiders/

scrapy crawl my-resume-spider -a link=$1 -a driver=/home/sean/Desktop/ResumeWriter/driver/chromedriver -o "$saveLocation/$out.json"
