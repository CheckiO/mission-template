#!/bin/sh

#if [[ "$OSTYPE" == "linux-gnu" ]]; then
#    SCRIPT=`realpath -s $0`
#    SCRIPTPATH=`dirname $SCRIPT`
#elif [[ "$OSTYPE" == "darwin"* ]]; then
#    SCRIPTPATH=$( cd "$( dirname "$BASH_SOURCE" )" && pwd )
#elif [[ "$OSTYPE" == "cygwin" ]]; then
#elif [[ "$OSTYPE" == "msys" ]]; then
#elif [[ "$OSTYPE" == "win32" ]]; then
#elif [[ "$OSTYPE" == "freebsd"* ]]; then
#else
#    SCRIPT=`realpath -s $0`
#    SCRIPTPATH=`dirname $SCRIPT`
#fi

SCRIPT=`realpath $0`
SCRIPTPATH=`dirname $SCRIPT`

python $SCRIPTPATH/main.py $1 $2
