
#!/usr/bin/env python
"""The module contains a custom class that will compress the file in zip format.
"""
import logging
import glob
import sys
import os
import os.path
import shutil

import pdsdwwf.config as cfg
from pdsdwwf.wf_custom_step import WfCustomStep

logger = logging.getLogger()

class Zip():
    def __init__(self, config, parent):
        super().__init__(config)

        new_file = shutil.make_archive("/mnt/pdsdw/ingest/dexyp_sales_activity_export/dexyp_booking_export.zip","zip","/mnt/pdsdw/ingest/dexyp_sales_activity_export/*.txt" )

        # print(new_file)

        # print(shutil.get_archive_formats("C:\\Users\\virendrapatel\\PycharmProjects\\python_learning\\test.zip"))
        # f = open("test.txt", 'w')

        # print(f.read())

        # print(zipfile.zipfile(f))
        #full_cmd =""
        #file_path = "/mnt/pdsdw/ingest/dexyp_sales_activity_export/*.txt"


