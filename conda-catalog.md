
# CONDA

------------------------------------

### TERMINOLOGY



| Term/Expression | Meaning |
| --------------: | :------ |
| `<description>` | To replace, or that will be replaced, according to description |
| `$`             | Some command to be used on the Terminal (shell) |
| `(<env>)$`      | Some Terminal command to be used on a specific environment |



------------------------------------

### REFERENCE

- [Documentation][conda]


- [Conda Forge][conda]



[conda]:https://docs.conda.io/projects/conda/en/latest/index.html "Conda Documentation"
[conda-forge]:https://conda-forge.org/feedstock-outputs/ "Packages on Conda Forge"
[non-conda-forge]:https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-pkgs.html#installing-non-conda-packages "Installing non-conda packages"

------------------------------------

### HELP

- Help on a command:

$ `conda <command> --help`



------------------------------------

### ENVIRONMENTS

- List enviroments:

$ `conda env list`

$ `conda info --envs`
<!-- --><br/>


- Activate/deactivate enviroment (conda>=4.6):

$ `conda activate <enviroment>`

(`<env>`)$ `conda deactivate <enviroment>`
<!-- --><br/>


- Create enviroment:

$ `conda create --name <env-name>`

$ `conda create -n <env-name> python=<version>`
<!-- --><br/>


- Create enviroment with specific package:

$ `conda create -n <env-name> <package>`

$ `conda create -n <env-name> <package>=<pack-version>`
<!-- --><br/>


- Exporting environment.yml:

(`<env>`)$ `conda env export > environment.yml`
<!-- --><br/>


- Creating an environment from a environment.yml:

$ `conda env create -f environment.yml`
<!-- --><br/>


------------------------------------

### JUPYTER

- Open jupyter:

(`<env>`)$ `jupyter notebook`

(`<env>`)$ `jupyter notebook <file.ipynb>`

(`<env>`)$ `jupyper lab`

(`<env>`)$ `jupyper lab <file.ipynb>`
<!-- --><br/>


- List running Jupyter servers:

(`<env>`)$ `jupyter notebook list`
<!-- --><br/>


- Terminate Jupyter server:

(`<env>`)$ `jupyter notebook stop`

(`<env>`)$ `jupyter notebook stop <port>`
<!-- --><br/>


- Jupyter shortcuts (when a cell is selected):

| ShortCut | Meaning |
| :---: | :--- |
| [shift] + [Enter] | Run cell & go to the next |
| [ctrl] + [Enter]  | Run cell & DON'T go next |
| [alt] + [Enter]   | Run cell, add new cell under & go to it |
| [d] + [d]         | Delete selected cell |
<!-- --><br/>




------------------------------------

### PACKAGES

> :warning: **WARNING** *(for Arch)* **:**
>
>> DO NOT run `pip install <module>` on TERMINAL.
>> You should never make any changes to `/usr`, except through `pacman`.
>> If a package isn´t available by conda, try [Conda Forge][conda-forge] before even thinking on pip.
>> If you need to install with `pip` do it in a Virtual Enviroment.
>> For more info see [this][non-conda-forge].
>
> **TL;DR :**
>> Basically, never use `pip`.
>> Use `conda` on Virtual Enviroment.
>> Use `pacman` (or your package manager) on the system.
<!-- --><br/>


- Install packages on current env:

(`<env>`)$ `conda install <package>`

(`<env>`)$ `conda install <package>=<version>`
<!-- --><br/>


- Install packages on other env:

$ `conda install <package> -n <env>`
<!-- --><br/>


- Remove a packages:

(`<env>`)$ `conda remove <package>`

$ `conda remove <package> -n <env>`
<!-- --><br/>


- Search package:

$ `conda search <package>`
<!-- --><br/>


- Search package info:

$ `conda search <package> --info`
<!-- --><br/>


- Search package on the channel conda-forge:

$ `conda search <package> --channel conda-forge`

$ `conda search <package> -c conda-forge`
<!-- --><br/>


- Install packages from the channel conda-forge:

(`<env>`)$ `conda install <package> -c conda-forge`
<!-- --><br/>


- List installed package:

(`<env>`)$ `conda list`

(`<env>`)$ `conda list <package>`



------------------------------------

### UPDATES

- Check available updates:

$ `conda update`
<!-- --><br/>


- Update a package:

$ `conda update <package>`

$ `conda update python`

$ `conda update conda`

$ `conda update anaconda`
<!-- --><br/>


- Update all packages on enviroment:

(`<env>`)$ `conda update --all`
<!-- --><br/>


------------------------------------

### MISC

- Finding anaconda's install directory:

$ `which conda`
<!-- --><br/>


- Finding the anaconda's python interpreter (environmental):

(`<env>`)$ `which python`
<!-- --><br/>


------------------------------------



------------------------------------



------------------------------------



------------------------------------



