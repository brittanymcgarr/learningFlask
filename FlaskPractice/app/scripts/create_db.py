################################################################################
# create_db.py                                                                 #
#                                                                              #
# Creates and initializes the database.                                        #
#                                                                              #
# Copyright 2016 University of Nevada, Reno                                    #
################################################################################


import os
import sys
sys.path.append(os.getcwd())

from app.main import db

if __name__ == '__main__':
    db.create_all()
