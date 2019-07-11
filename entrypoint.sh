#!/bin/sh
cat hosts >> /etc/hosts
pybot -v ENV:$ENV -d report -e test .