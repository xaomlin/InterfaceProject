# -*- coding: utf-8 -*-
# @Project : InterfaceProject

import subprocess
from settings import conf
import time
class AllureHandler(object):

    def execute_command(self):
        time.sleep(1)
        subprocess.call(conf.ALLURE_COMMAND, shell=True)

