#!/bin/bash

case "$1" in
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
	*)
		
        echo
        echo
        echo    "   Command:"
        echo    "       $ sh catalog <opt>"
        echo
        echo    "   Catalogs Opt List:"
        echo    "       Python:             py, python"
        echo    "       Python Projects:    pypro, py-projects"
        echo    "       Pacman:             pac,pacman"
        echo    "       Git:                git"
        echo    "       Conda:              conda"
        echo    "       "
        echo    "       Catalog Directory:  dir"
        echo    "       Catalog Script:     script, file"
        echo    "       "
        echo
        echo		
		
		;;
esac

# make a git repository later, then add a update option here
