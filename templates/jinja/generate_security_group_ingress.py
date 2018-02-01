from jinja2 import Environment, FileSystemLoader
import yaml
import os
from os.path import isdir,expanduser

class SecGroupTemplate():

    def __init__(self, sceptre_user_data):
        """Init method."""
        # super(PocTemplate, self).__init__()
        self.SCEPTRE_USER_DATA = sceptre_user_data



    ENV = Environment(loader=FileSystemLoader('./'))


    # rules = content['sceptre_user_data']['rules']
    # new_dict = {}
    # new_dict['sceptre_user_data'] = ''
    # new_dict['rules'] = {}
    # new_dict['tags'] = conten;t['sceptre_user_data']['tags']
    def handle_user_data(self):
        rules = []
        for i, rule in enumerate(self.SCEPTRE_USER_DATA.get('rules')):
            rules.append(
                     {
                        'protocol' : rule.split(' ')[0],
                        'ip' : rule.split(' ')[1],
                        'from' : int(rule.split(' ')[2]),
                        'to' : int(rule.split(' ')[-1])
                    }
             )
        return rules



    # for rule in rules.items():
    #     print rule


    def print_temp(self):
        rules = self.handle_user_data()
        template = self.ENV.get_template("templates/security_group_ingress.yaml")
        return template.render(config=rules)




def sceptre_handler(sceptre_user_data):
    p = SecGroupTemplate(sceptre_user_data)
    # return PocTemplate(sceptre_user_data).template.to_json()

    return p.print_temp()