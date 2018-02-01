from jinja2 import Environment, FileSystemLoader
import yaml
import os
from os.path import isdir,expanduser

class SceptreResource():

    def __init__(self, sceptre_user_data):
        """Init method."""
        # super(SceptreResource, self).__init__()
        self.SCEPTRE_USER_DATA = sceptre_user_data

    home = expanduser('~')
    ENV = Environment(loader=FileSystemLoader('./'))



    def print_temp(self):
        template = self.ENV.get_template("templates/subnets.yaml")
        return template.render(config=self.SCEPTRE_USER_DATA)


    

def sceptre_handler(sceptre_user_data):
    p = SceptreResource(sceptre_user_data)
    # return SceptreResource(sceptre_user_data).template.to_json()
    return p.print_temp()