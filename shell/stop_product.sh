#!/bin/sh
ps -ef | grep 'uwsgi -x /mnt/users/briapp/apps/nicedesign/django_product.xml'| grep -v grep | awk '{print $2}' | xargs kill