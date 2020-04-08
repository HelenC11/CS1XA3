# CS 1XA3 Project01 - <Chenh214>
## Usage
Execute this script from project root with:
chmod +x CS1XA3/Project01/project_analyze.sh
./CS1XA3/Project01/project_analyze arg1 arg2 ...
With possible arguments
- arg1: LatestMerge
- arg2: FileTypeCount
- arg3: FIXME
- arg4: TryCommit
- arg5: Switch 
- arg6: Backup
- arg7: NewDir

## Feature 01 Checkout Latest Merge
Description: this feature finds and will checkout the latest merge commit

Execution: execute this feature by inputting LatestMerge after the action prompt

Reference: some code was taken from [here](https://stackoverflow.com/questions/4898837/how-to-find-last-merge-in-git)
## Feature 02 File Type Count

Description: this feature returns the number of files in a repo of a certain type (extension)

Execution: execute this feature by inputting FileTypeCount after the action prompt and then inputting an extension type

Reference: some code was taken from [here](https://askubuntu.com/questions/454564/count-total-number-of-files-in-particular-directory-with-specific-extension)

## Feature 03 FIXME Log

Description: this feature finds all files with #FIXME on the last line and adds them to a log

Execution:Input FIXME after the action prompt

Reference:[here](https://cmdlinetips.com/2011/08/how-to-count-the-number-of-lines-words-and-characters-in-a-text-file-from-te$)

## Feature 04 Backup and Delete / Restore:

Description: This feature stores all files ending with .tmp in a directory and will restore them to their orignal location if prompted

Execution: Input Backup, then Backup to backup the files. Rerun and enter Restore, to Restore files

Reference:[here](https://www.ostechnix.com/find-copy-certain-type-files-one-directory-another-linux/)

## Feature 04 Switch to Executable:

Description: This feature will add executable perms to anyone with write perms on  .sh files

Execution:Input Switch and then Change to change perms and Restore to restore perms

Reference:[here](https://askubuntu.com/questions/229589/how-to-make-a-file-e-g-a-sh-script-executable-so-it-can-be-run-from-a-termi)

## Custom Features

Custom feature 1:A feature that adds, commits a new directory with a README.md file 

Execution: input NewDir and a name

Reference: [here](https://github.com/jessica-dl/COMPSCI-1XA3/blob/master/Assign1/ProjectAnalyze.sh)

Custom feature 2:A feature that validates that a README.md file matches a certain pattern(must have a certain phrase or word) in order to commit

Execution: input TryCommit and choose to add the pattern or not

Reference: [here](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks)

tryMe
