#!/bin/bash

case "$1" in
	linux|bash)
        
        kate ~/Coding/CATALOGS/linux-catalog &
        
        ;;
        
	py|python)
        
        kate ~/Coding/CATALOGS/python-catalog &
        
        ;;
        
	py-projects|pypro)
        
        dolphin ~/Coding/python/Projects &
        
        ;;
        
	pac|pacman)
        
        kate ~/Coding/CATALOGS/pacman-catalog &
        
        ;;
        
	git)
        
        kate ~/Coding/CATALOGS/git-catalog &
        
        ;;
        
	conda)
        
        kate ~/Coding/CATALOGS/conda-catalog &
        
        ;;
        
    dir)
        
        dolphin ~/Coding/CATALOGS/ &
        
        ;;
        
    script|file)
        
        kate ~/catalog &
        
        ;;
        
        
    -u|--update)
        
        cd ~/Coding/CATALOGS
        
        # Add possible changes from catalog script
        cp -u ~/catalog ~/Coding/CATALOGS/catalog.sh
        
        # Commit to master and Push to origin
        git add .
        git commit -m "Full Scripted Update"
        git push origin master
        
        ;;
        
	*)
		
        echo
        echo
        echo    "   Command:"
        echo    "       $ sh catalog <opt>"
        echo
        echo    "   Catalogs Opt List:"
        echo    "       Linux:             linux, bash"
        echo    "       Python:             py, python"
        echo    "       Python Projects:    pypro, py-projects"
        echo    "       Pacman:             pac,pacman"
        echo    "       Git:                git"
        echo    "       Conda:              conda"
        echo    "       "
        echo    "       Catalog Directory:  dir"
        echo    "       Catalog Script:     script, file"
        echo    "       Update to Github:   -u,--update"
        echo    "       "
        echo
        echo		
		
		;;
esac

