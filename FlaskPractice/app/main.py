################################################################################
# main.py                                                                      #
#                                                                              #
# Entry point for the execution of the application.                            #
#                                                                              #
# Copyright 2016 University of Nevada, Reno                                    #
################################################################################

from app import app, db
import admin
import models
import views

from entries.blueprint import entries
app.register_blueprint(entries, url_prefix='/entries')

if __name__ == '__main__':
    app.run()
