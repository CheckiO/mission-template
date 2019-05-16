#!/bin/sh

SCRIPT=`realpath $0`
SCRIPTPATH=`dirname $SCRIPT`
cd $SCRIPTPATH
export NODE_PATH=/lib/node_modules/:$SCRIPTPATH
touch userModule.js
chmod a+rw userModule.js
touch userModule.ts
chmod a+rw userModule.ts
ln -s /lib/node_modules node_modules
node --harmony main.js $1 $2
