## Dev install steps

### Install virtualenvwrapper
``` bash
pip3 install virtualenvwrapper
```

In your shell config file (.zshrc, .bashrc, etc)
``` bash
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
```

### Create the virtualenv
``` bash
mkvirtualenv multiple_score_bot
```

``` bash
workon multiple_score_bot
```

### Install dependencies dependency
``` bash
pip3 install -r requirements.txt
```
