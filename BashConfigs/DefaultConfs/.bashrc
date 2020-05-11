#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls -a --color=auto'
PS1='[\u@\h \W]\$ '
export EDITOR='/bin/nvim'
alias pacman='sudo pacman'
alias n='sudo nvim'
