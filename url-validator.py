import requests

def validate_url(url):
    valid_protocols = ['http', 'https', 'ftp']
    valid_tlds = ['.com', '.net', '.org']

    protocol = url.split('://')[0]
    tld = url[-4:]

    if protocol in valid_protocols:
        protocol_is_valid = True
        print(f'Valid protocol: {protocol}')
    else:
        protocol_is_valid = False
        print(f'Invalid protocol: {protocol}')

    if tld in valid_tlds:
        tldn_is_valid = True
        print(f'Valid top level domain: {tld}')
    else:
        tldn_is_valid = False
        print(f'Invalid top level domain: {tld}')
    
    if tldn_is_valid and protocol_is_valid:
        return True


url = input('Enter URL: ')
if validate_url(url):
    print('URL is valid')
else:
    print('URL is NOT valid')
