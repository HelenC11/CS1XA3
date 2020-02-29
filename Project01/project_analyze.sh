#!/bin/bash

echo "Hello what action would you like to do? Switch, Backup,TryCommit, NewDir,LatestMerge, FileTypeCount, or FindTag"


#sorry for the long phrases as args I had troubles telling numbers apart for testing
read prompt

if [ "$prompt" = "Backup" ] ; then
	
	# Backup delete and restore
	echo "Hello would you like to Backup or Restore? Please type the action you would like to do (Backup/Restore)"
	read action

	if [ "$action" = "Backup" ] ; then
        	if [ -d "backup" ] ; then
                	rm -r backup
                	mkdir backup
        	else
                	mkdir backup
        	fi


		touch ./backup/restore.log
		#find  . -type f -name "*.tmp" > ./backup/restore.log
        	find -iname '*.tmp' -exec cp {} ./backup/ \; -exec rm {} \; -exec echo "$PWD" >> ./backup/restore.log \;

	elif [ "$action" = "Restore" ]
	then
        	echo "restoring"
		if [ -f "./backup/restore.log" ] ; then
			echo "Returning files"
	
          		while read PERMS  FILE
          		do
             			fullfile=$FILE
             			filename="${FILE##*/}"
             			cp ./backup/$filename $fullfile
          		done <./backup/restore.log
		else
			echo "Error: log does not exist, nothing to restore"
		fi

	else
        echo "That is not a valid command. Please rerun the script and try again"
	fi

#switch to executable
elif [ "$prompt" = "Switch" ] 
then 

	echo Hello, what action would you like to perform today? Please enter Change, Restore

	read action

	



	if [ "$action" = "Change" ]
	then
		for file in *.sh; do
			stat -c '%a %n' *.sh > permission.log
		done
		cat permission.log  
 
		for file in *.sh; do
   
			echo $file
   			if
				test $(find $file -perm -u+w |wc -l) = 1
			then
				chmod u+x $file
			fi

			if
				test $(find $file -perm -g+w |wc -l) = 1
			then
				chmod g+x $file
			fi

			if
				test $(find $file -perm -o+w |wc -l) = 1
			then
				chmod o+x $file
			fi
   		done
  
	elif  [ "$action" = "Restore"  ]
	then	
		echo restore
		while read PERMS  FILE
		do
			chmod  "$PERMS"  "$FILE"

        		done <permission.log

   	else

        	echo  That is not an legal action, please rerun the script and try again

   	fi

#custom2
elif [ "$prompt" = "TryCommit" ]
then
	echo " Do you want to add or remove commit pattern check (A/R)"
	read reply
	if [  "$reply" = "A" ] ; then
	
		mv pre-commit ../.git/hooks
		chmod +x ../.git/hooks/pre-commit
	elif [ "$reply" = "R" ] 
	then	
		cp ../.git/hooks/pre-commit ./Project01
		rm ../.git/hooks/pre-commit
	fi
#custom1
elif [ "$prompt" = "NewDir" ]
then
	echo "What would you like to name this new Directory? " 
	read name
        if [ ! -d $name ] 
        then
        	mkdir $name
		touch $name/README.md 
		echo "# This is README for $name" >> $name/README.md

		read -p "Please enter text for the README: " txt
		echo -e "$txt\n" >> $name/README.md

		git add $name/README.md
    	    	git add $name
    	    	git commit "$name" -m "Created $name"
	else
            echo -e "$A directory of that name already exists."
        fi

#LatestMerge
elif [ "$prompt" = "LatestMerge" ]
then
        p=$(   git show -s  --format=%h :/merge )

        if [ "$p" = "" ]
        then
                echo "no merge to checkout"

        else
                echo $p
                git checkout $p
        fi
#fileTypeCount
elif [ "$prompt" = "FileTypeCount" ]
then
        echo "Please input an extension (txt, pdf, etc)"
        read extension
        echo "Number of files of this type"
        #ls -lR ./*.$extension | wc -l
        cd ..
        find ./** -name *.$extension | wc -l
#findtag
elif [ "$prompt" = "FindTag" ]
then

        if [ -f "fixme.log" ] ; then
                rm fixme.log
                touch fixme.log
        else
                touch fixme.log
        fi
        #tail -n 1 ./** | grep "#FIXME
        tail -f ./** | grep "#FIXME"


        #grep -r "#FIXME" nix* | tail -Z

else 
	echo "That is not a legal action, please rerun the script and try again"
fi
 
