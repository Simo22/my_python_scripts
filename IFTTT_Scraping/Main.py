from ServicesParser import *
from RulesParser import *

def main():
    my_url = "https://ifttt.com/search/services"
    url_list = create_url_list(my_url)
    print(len(url_list))
    print("List of URLs: " + str(url_list))
    print("Getting rules.....")
    rules_list = get_all_rules(url_list,1)


main()
