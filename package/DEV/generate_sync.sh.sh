#!/bin/bash

#define parameters which are passed in.
NAME=$1
PORT=$2
SSH=$3


cat  << EOF
rsync -av --exclude-from=sync_ignore.txt ../$NAME-DEV/ ../$NAME-DEPLOY/
rsync -av ../$NAME-DEPLOY/ $SSH:~/$NAME-DEPLOY/

ssh $SSH <<ENDSSH
cd ~/$NAME-DEPLOY
bash rebuild.sh
ENDSSH
EOF