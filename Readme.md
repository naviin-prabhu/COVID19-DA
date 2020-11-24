The dependencies used in the virtual environment can be found in the requirements.txt.

If you already have some libraries in the virtual environment you created but not necessary, first clean it up with 
pip freeze | grep -v -f requirements.txt - | xargs pip uninstall -y

Once done, install all the dependencies with 
pip install -r requirements.txt