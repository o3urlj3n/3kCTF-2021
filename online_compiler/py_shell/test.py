#!/usr/bin/env python
from pathlib import Path
from subprocess import PIPE, Popen

def check_file(filename):
    if Path(filename).is_file():
        return True
    else:
        return False



filename = '-c 2+2; whoami; #py'


def compile():
    if (filename[-2:]=='py'):
        if (check_file('./'+filename)):
            cmd='python3 '+filename
            p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
            stdout, stderr = p.communicate()
            return stdout
        else:
            return 'failed'
    else:
        return 'noop'
    print('stdout:', stdout)
    print('stderr:', stderr)



print('compile returned:', compile())
