#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    #set outseide to define deploy environ
    #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vcf_server2.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
