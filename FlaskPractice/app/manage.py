################################################################################
# manage.py                                                                    #
#                                                                              #
# Manages database migrations.                                                 #
#                                                                              #
# Copyright 2016 University of Nevada, Reno                                    #
################################################################################


from app import manager
from main import *

if __name__ == '__main__':
    manager.run()
