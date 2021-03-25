#! /bin/bash

cp -u $0 this-file-backup
clear
echo 'Backup.'

sleep 2

rm $0
clear
echo 'Removed!'

sleep 2

cp this-file-backup $0
clear
echo 'Restore.'

sleep 2

rm this-file-backup
clear
echo 'Byeee.'
