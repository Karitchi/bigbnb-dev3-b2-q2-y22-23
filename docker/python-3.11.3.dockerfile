from python:3.11.3

workdir /back

run apt update
run pip install --upgrade pip

run echo "PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '" >> /root/.bashrc
run echo "alias ls='ls --color=auto'" >> /root/.bashrc
run echo "alias dir='dir --color=auto'" >> /root/.bashrc
run echo "alias vdir='vdir --color=auto'" >> /root/.bashrc
run echo "alias grep='grep --color=auto'" >> /root/.bashrc
run echo "alias fgrep='fgrep --color=auto'" >> /root/.bashrc
run echo "alias egrep='egrep --color=auto'" >> /root/.bashrc

cmd pip install -r requirements.txt && tail -f /dev/null
