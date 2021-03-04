#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 Michael Edie / @tankmek
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from py3cw.request import Py3CW
import sys
import getopt
import json

### API INFO
api_key = ''
api_secret = ''
##################


##################---------------
# DO NOT EDIT BELOW THIS LINE UNLESS YOU
# KNOW WHAT YOU ARE DOING. YOU HAVE BEEN WARNED
###-------------------------------------#############

def usage():
    print("Usage: " + sys.argv[0] + ' [ -b | -u <blacklist_file> ]')
    print("-b, --show-blacklist (show blacklist [default])")
    print("-u, --update-blacklist (update blacklist)")
    exit(2)

def get_blacklist(api):
    error, data = api.request(
        entity='bots', 
        action='pairs_black_list',
        action_id=''
    )

    if not error:
        return data
    else:
        print(error)
        exit(2)

def remove_blacklist(data, pair):
#TODO
    print("Removing")
    # future work

def show_blacklist(data):
    bl = data['pairs']
    print(*bl, sep=" ")
    print("\nThere are " + str(len(bl)) + " pairs in the black list", file=sys.stderr)

# 3Commas API only support destructive updates
# we save the current blacklist and then append the new list
def update_blacklist(api, pairs_file):
#TODO: add validation checks for pairs in file
    blacklist = get_blacklist(api)

    with open(pairs_file) as f:
        pairs = f.read().split()

    s_count = len(blacklist)
    blacklist = set(blacklist['pairs'])
    
    blacklist.update(pairs)
    n_count = len(blacklist)

    m_payload = {
            "pairs": []
            }
    for i in blacklist:
        m_payload['pairs'].append(i)

    error, data  = api.request(
        entity='bots', 
        action='update_pairs_black_list', 
        payload=m_payload
    )

    if data:
        print("\nUpdated " + str(n_count - s_count) + " pairs in the black list")
    else:
        print(error)


def main(argv):
    api = Py3CW(
      key=api_key, 
      secret=api_secret,
      request_options={
        'request_timeout': 10,
        'nr_of_retries': 1,
        'retry_status_codes': [502]
      }
    )

    try:
        opts, args = getopt.getopt(argv,'bu:', ['show-blacklist', 'update-blacklist='])
    except getopt.GetoptError:
        usage()

    for opt, arg in opts:
        if opt in ('-b', '--show-blacklist'):
            show_blacklist(get_blacklist(api))

        elif opt in ('-u', '--update-blacklist'):
            update_blacklist(api, arg)
 
    if not opts:
        show_blacklist(get_blacklist(api))
 
if __name__ == "__main__":
    main(sys.argv[1:])
