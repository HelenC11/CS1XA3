#!/bin/bash
echo "Hello, what action would you like to perform today? Please enter LatestMerge, FileTypeCount, or FIXME"
echo "LatestMerge: will find and checkout the latest merge"
echo "FileTypeCount: Will give you the number of files of a certain type"
echo "FIXME: Will give you a log of all the files with #FIXME on the last line"
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
        find ./** -name *."$extension" | wc -l

elif [ "$action" = "FIXME" ] ; then
	rm fixme.log	
	for file in *; do 

 		if [ -f "$file" ]; then 
			count=$(tail -1 $file | grep '#FIXME' | wc -l)
       			if [ $count -gt 0 ]; then

        			echo $file >> 'fixme.log'
       			fi
    		fi 

	done


else
	echo "That is not a legal action, please rerun the script and try again"
fi

