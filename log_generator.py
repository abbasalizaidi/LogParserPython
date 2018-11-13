import random
import datetime
import configparser
import io
from random import getrandbits
from ipaddress import IPv4Address
#import pdb; pdb.set_trace()

config = {}

# Method to generate random IP addresses
def get_rand_ip():
    bits = getrandbits(32) # generates an integer with 32 random bits
    addr = IPv4Address(bits) # instances an IPv4Address object from those bits
    addr_str = str(addr) # get the IPv4Address object's string representation
    return addr_str

# Code to create generate random request uri
def get_rand_url():
    if not config :
        print ("Configuration is not available! Please check config.ini")
        exit()
    else:
        request_items = config.get('log_generator','request_items')
        request_items = request_items.split(",")
        request_methods = config.get('log_generator','request_methods')
        request_methods = request_methods.split(",")
        response_codes = config.get('log_generator','response_codes')
        response_codes = response_codes.split(",")
        uri = get_rand_ip() + " " +  str(datetime.datetime.utcnow()) + " " + random.choice(request_methods) + " "+ "/" + random.choice(request_items) + "/" + " " + random.choice(response_codes) + " " + str(random.randint(0,2000))
        return uri

def write_log_files(num_of_file,num_of_lines):
    filename_prefix = config.get('log_generator','filename_prefix')
    filename_suffix = config.get('log_generator','filename_suffix')
    while num_of_file > 0:
        filename = datetime.datetime.now().strftime(filename_suffix)
        file = open("%s_%s.txt" % (filename_prefix,filename), "w")
        for i in range(0,num_of_lines):
            file.write(get_rand_url()+"\n")
        file.close()
        num_of_file-=1

file = open("config.ini")
sample_config = file.read()
config = configparser.ConfigParser()
config.read_string(sample_config)
write_log_files(int(config['log_generator']['num_of_files']),int(config['log_generator']['num_of_lines']))
file.close()
