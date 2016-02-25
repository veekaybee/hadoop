#dotfile settings for Cloudera Quickstart VM where all Hadoop files are under /usr/lib/hadoop
#http://bit.ly/1R4Gxp6

# User specific aliases and functions

alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi

#homebrew

export PATH="$HOME/.linuxbrew/bin:$PATH"
export MANPATH="$HOME/.linuxbrew/share/man:$MANPATH"
export INFOPATH="$HOME/.linuxbrew/share/info:$INFOPATH"

#Flume
export FLUME_HOME="/usr/lib/flume/"
export FLUME_CONF_DIR="$FLUME_HOME/conf"
export FLUME_CLASSPATH="$FLUME_CONF_DIR"

export PATH="$FLUME_HOME/bin:$PATH"
export PATH="~/Desktop/hip-2.0.0/bin:$PATH"

#Spark

export USER="cloudera"

# Hadoop

export HADOOP_PREFIX="/usr/lib/hadoop"
export HADOOP_HOME=$HADOOP_PREFIX
export HADOOP_COMMON_HOME=$HADOOP_PREFIX
export HADOOP_CONF_DIR=$HADOOP_PREFIX/etc/hadoop
export HADOOP_HDFS_HOME=$HADOOP_PREFIX
export HADOOP_MAPRED_HOME=$HADOOP_PREFIX
export HADOOP_YARN_HOME=$HADOOP_PREFIX
export PATH=$PATH:$HADOOP_PREFIX/sbin:$HADOOP_PREFIX/bin
