## Setup for Miniconda, Virtual Environment, PyCharm, and Jupyter Notebook

1. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
  - Follow the instructions at [this link](https://docs.conda.io/projects/conda/en/latest/user-guide/install/#regular-installation).
  - Conda is a package manager that sandboxes your project’s dependencies in a virtual environment
  - Miniconda contains Conda and its dependencies with no extra packages by default (as opposed to Anaconda, which installs some extra packages)
  - You will need to add Conda to PATH, just so you're not having to write its full directory name when you use the "conda" command.
  - Note where the path of the saved Miniconda folder; this is where you'll find the env if you're adding it to PyCharm.
2. Open the Anaconda prompt, cd into src, run `conda env create -f environment.yml`
  - This creates a Conda environment called `marinebioproject`
3. Run `conda activate marinebioproject`
  - This activates the `marinebioproject` environment
  - Do this each time you want to write/test your code
  - Enter "conda deactivate marinebioenv"
4. For PyCharm
  - https://www.jetbrains.com/pycharm/download/#section=windows to download PyCharm.
  - Open the `src` directory in PyCharm, or just the MarineBioDataProject folder. I think that is the "project" here.
  - Go to `File` > `Settings` > `Project` > `Project interpreter`
  - Click the gear in the top-right corner, then `Add`
  - Select `Conda environment` > `Existing environment` > Button on the right with `…`
  - Select `/Users/YOUR_USERNAME/miniconda3/envs/marinebioenv/bin/python`
  - You can also navigate to the python.exe file within the marinebioenv folder.
  - Select `OK` then `Apply`
  - This will allow your project to automatically use your virtual environment within PyCharm.
5. Jupyter Notebook
  - This is probably going to be the most convenient way for you to work with these large sets of data without needing to rerun an entire
    program each time. Code is executed in cells that you determine so that you can, for instance, load a dataset,
    and then execute and change the following code without having to reload it.
  - The yml file contains the call to install jupyter notebook, so it should be taken care of.
  - Navigate to the directory ../Users/Jesse/MarineBioDataProject/src in the Anaconda Prompt.
  - Type "activate marinebioenv" to start the virtual environment.
  - Then enter "jupyter notebook" and it should open jupyter notebook in your browser showing the contents of src.
  - You should see a jupyter notebook file I've created there. Take a look at it to see some of the data manipulations
    you'll want to do. It's called shark_attack_data.ipynb
