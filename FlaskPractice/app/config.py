################################################################################
# config.py                                                                    #
#                                                                              #
# Configuration variables for the Flask app.                                   #
#                                                                              #
# Copyright 2016 University of Nevada, Reno                                    #
################################################################################

import os


class Configuration(object):
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    STATIC_DIR = os.path.join(APPLICATION_DIR, 'static')
    IMAGES_DIR = os.path.join(STATIC_DIR, 'images')
    DEBUG = False
    SECRET_KEY = "Alohomora"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/blog.db' % APPLICATION_DIR
    SQLALCHEMY_TRACK_MODIFICATIONS = False

