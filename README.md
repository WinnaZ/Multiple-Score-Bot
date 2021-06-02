## Dev config instructions

### Install virtualenvwrapper
```
pip3 install virtualenvwrapper
```

In your shell config file (.zshrc, .bashrc, etc)
```
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
```

### Create the virtualenv
```
mkvirtualenv multiple_score_bot
```

```
workon multiple_score_bot
```

### Install dependencies dependency
```
pip3 install -r requirements.txt
```
