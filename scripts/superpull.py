#!/usr/bin/env python3

import subprocess
subprocess.check_call("git submodule foreach git pull".split())
subprocess.check_call("git pull".split())