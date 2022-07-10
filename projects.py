import os
import datetime
import sys

from mdutils.mdutils import MdUtils
from mdutils import Html


def banner():
    print(f"*" * 49)
    print(f"*" + "      TIME TO MAKE LIFE IN TESTING EASIER      " + "*")
    print(f"*" * 49)


def general_info():
    info_list = []
    client_name = input("[*] Client Name: ")
    project_link = input("[*] Project's Sharepoint Link: ")
    project_name = input("[*] Project Name: ")
    testing_date = input("[*] Testing Window (YYYY-MM-DD): ")
    test_box = input("[*] Black/Grey Box: ").upper()
    environment = input("[*] UAT/Production: ").upper()
    filename = f"{testing_date}-{project_name}.md"
    fullfile = f"C:\\Users\\USER\\Desktop\\projecttest\\{filename}"
    file = open(f"{fullfile}", "w")
    file.write('hi')
    info_list.append(client_name)
    info_list.append(project_link)
    info_list.append(project_name)
    info_list.append(testing_date)
    info_list.append(test_box)
    info_list.append(environment)
    return info_list


def web_app():
    urls = []
    credentials = []
    roles = []
    web_list = []

    # Provide either URL or IP
    print("[*] Press Enter once no more URLs to enter")
    url = input("[*] Target URL: ")
    while url.lower() != '':
        urls.append(url)
        url = input("[*] Target URL: ")

    # Provide user roles if applicable
    available_role = input("[*] Any Available Roles (y/n): ")
    if available_role.lower() == 'y':
        print("[*] Press Enter once no more roles to enter")
        role = input("[*] Roles Available: ")
        while role.lower() != '':
            roles.append(role)
            role = input("[*] Roles Available: ")

    # Provide credentials if applicable
    available_cred = input("[*] Any Available Credentials (y/n): ")
    if available_cred.lower() == 'y':
        print("[*] Press Enter once no more credentials to enter")
        credential = input("[*] Credentials (user/pass): ")
        while credential.lower() != '':
            credentials.append(credential)
            credential = input("[*] Credentials (user/pass): ")
    pages = input("[*] How many static/dynamic pages: ")
    parameters = input("[*] How many parameters: ")
    web_list.append(urls)
    web_list.append(roles)
    web_list.append(credentials)
    web_list.append(pages)
    web_list.append(parameters)
    print("[*] Check with client for a proper user matrix if applicable")
    return web_list


def api():
    endpoints = []
    roles = []
    http_methods = []
    num_endpoints = int(input("[*] Total number of API Endpoints: "))
    api_list = []

    # Provide the API endpoints
    print("[*] Press Enter once no more APIs to enter ")
    endpoint = input("[*] API Endpoint: ")
    while endpoint.lower() != '':
        endpoints.append(endpoint)
        endpoint = input("[*] API Endpoint: ")

    # Provide the HTTP methods available
    print("[*] Press Enter once no more methods to enter")
    http_method = input("[*] Available HTTP Methods (PUT/DELETE/POST/GET): ").upper()
    while http_method != '':
        http_methods.append(http_method)
        http_method = input("[*] Available HTTP Methods (PUT/DELETE/POST/GET): ").upper()

    # Check for any Postman/Swagger file
    postman_swagger = input("[*] Any Postman/Swagger file (y/n): ")
    if postman_swagger.lower() == 'y':
        print("[*] Remember to import the file and route to burp")

    # Provide user roles if applicable
    role = input("[*] Available Roles (y/n): ")
    if role.lower() == 'y':
        print("[*] Press Enter once no more roles to enter")
        role = input("[*] Available Roles: ")
        while role.lower() != '':
            roles.append(role)
            role = input("[*] Available Roles: ")
    api_list.append(endpoints)
    api_list.append(num_endpoints)
    api_list.append(http_methods)
    api_list.append(postman_swagger)
    api_list.append(roles)
    return api_list


def network():
    internal_ips = []
    external_ips = []
    interface = input("[*] Interfaces in-scope (internal/external): ")
    while interface not in {'internal', 'external', 'both'}:
        print("[*] Invalid choice, try again")
        interface = input("[*] Interfaces in-scope (internal/external/both): ")
    print("[*] Press Enter once no more IP addresses to enter")
    if interface.lower() == 'internal':
        internal_ip = input("[*] Internal IP address/range/subnet: ")
        while internal_ip != '':
            internal_ips.append(internal_ip)
            internal_ip = input("[*] Internal IP address/range/subnet: ")
    elif interface.lower() == 'external':
        external_ip = input("[*] External IP address/range/subnet: ")
        while external_ip != '':
            external_ips.append(external_ip)
            external_ip = input("[*] External IP address/range/subnet: ")
    return internal_ips, external_ips


def mobile():
    phone_os = input("[*] iOS/Android/Both: ")
    other_types = int(input("[*] Available APIs in-scope: "))
    apis = []
    if other_types > 0 & other_types != 1:
        for x in range(other_types):
            apis.append(input("[*] APIs in-scope: "))
    else:
        apis.append("[*] API in-scope: ")
    roles = int(input("[*] Number of User Roles (Enter 0 if none): "))
    creds = []
    if roles > 0:
        for x in range(roles):
            creds.append(input("[*] What are the roles and credentials (testacc:password1)"))
    return phone_os, other_types, apis, creds


def special_note():
    notes = []
    print("[*] Press Enter once no more notes")
    note = input("[*] Any Special Notes: ")
    while note != '':
        notes.append(note)
        note = input("[*] Any Special Notes: ")
    return notes

'''
file_name = client_name + "_" + project_name
title_name = project_name + "_" + testing_date
mdfile = MdUtils(file_name=file_name, title=title_name)
'''

'''
def create_md():
    mdfile.new_header('Sharepoint Link')
    mdfile.write(project_link + '\n')
    mdfile.new_header(level=4, title='Project Name')
    mdfile.write(project_name + '\n')
    mdfile.new_header(level=4, title='Test Date')
    mdfile.write(testing_date + '\n')
    mdfile.new_header(level=4, title='URLs/Endpoints')
'''

def main():
    testing_type = input("[*] Security Assessment Type (Mobile/Web/API/Network/Multiple): ")
    while testing_type.lower() not in {'api', 'mobile', 'web', 'network'}:
        print("[*] Invalid choice, try again")
        testing_type = input("[*] Security Assessment Type (Mobile/Web/API/Network/Multiple): ")
    else:
        if testing_type.lower() == 'web':
            web_app()
        elif testing_type.lower() == 'api':
            api()
        elif testing_type.lower() == 'network':
            network()
        elif testing_type.lower() == 'mobile':
            mobile()
    special_note()


if __name__ == '__main__':
    banner()
    try:
        general_info()
        main()
    except KeyboardInterrupt:
        print("[*] Exiting Program")
        sys.exit()
