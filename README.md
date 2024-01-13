# scc-engr-7
Repo containing code written for Engineering 7: Python Programming for Scientists and Engineers at Solano College.

## Setup

Choose **one** of the following options for installing the required Python modules.

### Install Dependencies System-Wide

To download the dependencies needed for the repo *directly to your system-wide Python environment*, use:
```bash
python3 -m pip install -r requirements.txt
```

### Install Dependencies in a Virtual Environment

To create a virtual environment for the repo, use:

```bash
python -m venv /path/to/desired/venv/location
source /path/to/desired/venv/location/bin/activate
```

The first line of Bash creates the virtual environment in the directory you specify. The second line activates that virtual environment. You can now install Python packages within this environment without affecting your system-wide Python install. Now, run
```bash
python3 -m pip install -r requirements.txt
```

When you are done using the project and want access to your global Python install again, just use
```bash
deactivate
```

And when you wish to use the virtual environment again, reactivate it with 
```bash
source /path/to/desired/venv/location/bin/activate
```

If you want to permanently delete the virtual environment, just delete it with
```bash
rm -rf /path/to/desired/venv/location/
```

---

### Bash Alias for Virtual Environments

To save time, copy the following into your `.bashrc` file:
```bash
alias venv-create='python -m venv /home/${USER}/.config/venv/${PWD##*/}'
alias venv-activate='source /home/${USER}/.config/venv/${PWD##*/}/bin/activate'
alias venv-deactivate="deactivate"
alias venv-remove='rm -rf /home/${USER}/.config/venv/${PWD##*/}'
```

Now all virtual environments are stored in `~/.config/venv/`.
