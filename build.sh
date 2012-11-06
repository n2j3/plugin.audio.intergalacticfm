#!/bin/sh

PLUGIN_NAME=plugin.audio.intergalacticfm

mkdir $PLUGIN_NAME
cp *.txt *.xml *.py icon.png $PLUGIN_NAME/.
zip -rq $PLUGIN_NAME.zip $PLUGIN_NAME/
rm -r $PLUGIN_NAME/
