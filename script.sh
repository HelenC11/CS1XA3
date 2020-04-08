#!/bin/bash

echo Hello, what action would you like to perform today? Please enter LatestMerge, FileTypeCount, or FindTag
read action
if [ "$action" = "LatestMerge" ]  ; then
	p=$(   git show -s  --format=%h :/merge )

	if [ "$p" = "" ]
	then
		echo "no merge to checkout"

	else
		echo $p
		git checkout $p
	fi

elif [ "$action" = "FileTypeCount" ] ; then
	echo "Please input an extension (txt, pdf, etc)"
	read extension
	echo "Number of files of this type"
	#ls -lR ./*.$extension | wc -l
	cd ..
	find ./** -name *.$extension | wc -l
	
elif [ "$action" = "FindTag" ] ; then

	if [ -f "fixme.log" ] ; then
		rm fixme.log
		touch fixme.log
	else
		touch fixme.log
	fi
	#tail -n 1 ./** | grep "#FIXME
	tail -f ./** | grep "#FIXME"	
	
	
	#grep -r "#FIXME" nix* | tail -Z
fi

