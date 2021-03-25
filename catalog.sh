# #!/bin/bash

case "$1" in
	sh|linux|bash)
        
        kate ~/Coding/CATALOGS/linux-catalog &
        
        ;;
        
	py|python)
        
        kate ~/Coding/CATALOGS/python-catalog &
        
        ;;
        
	py-projects|pypro)
        
        dolphin ~/Coding/python/Projects &
        
        ;;
        
	py-data)
        
        kate ~/home/teles/Coding/CATALOGS/python-data-sci-mach-learning &
        
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
        
        
        # IF Working on 'master' Branch
        cd ~/Coding/CATALOGS
        branch=$(git symbolic-ref HEAD | sed -e 's,.*/\(.*\),\1,')
        
		case "$branch" in
			
			master)
				
				echo "On master Branch. Update and Push."
				
				# Add changes from catalog script
				cp -u ~/catalog ~/Coding/CATALOGS/catalog.sh
				
				# Commit on PRIVATE master and Push to priv Remote.
				git add .
				git commit -m "Update on master (Catalog script)."
				git push priv master
				
				echo "Done."
				;;
			
			dev)
				
				echo
				echo
				echo "You are working on dev Branch."
				echo "Go check if the Work-tree is clean, then switch."
				echo "Nothing done."
				echo
				echo
				;;
			
			*)
			
				echo
				echo
				echo "Not 'master', nor 'dev'. "
				echo "Nothing done."
				echo
				echo "Branch: $branch"
				echo
				echo
				;;
		
		esac
        
        ;;
        
	*)
		
        echo
        echo
        echo    "   Command:"
        echo    "       $ sh catalog <opt>"
        echo
        echo    "   Catalogs Opt List:"
        echo    "       Linux:              sh, linux, bash"
        echo    "       Python:             py, python"
        echo    "       Python Projects:    pypro, py-projects"
        echo    "       Python DataSci:     py-data"
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

