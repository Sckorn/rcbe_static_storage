#!/usr/bin/env python

import subprocess

def run_shellcommand(*args):
    '''run the provided command and return its stdout'''
    args = sum([(arg if type(arg) == list else [arg]) for arg in args], [])
    return subprocess.Popen(args,
                            stdout=subprocess.PIPE).communicate()[0].strip()

def split_words(text):
    '''return a list of lines where each line is a list of words'''
    return [line.strip().split() for line in text.split('\n')]

