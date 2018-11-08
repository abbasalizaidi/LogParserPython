import random
from random import getrandbits
import datetime
from ipaddress import IPv4Address
#import pdb; pdb.set_trace()

# Method to generate random IP addresses
def get_rand_ip():
    bits = getrandbits(32) # generates an integer with 32 random bits
    addr = IPv4Address(bits) # instances an IPv4Address object from those bits
    addr_str = str(addr) # get the IPv4Address object's string representation
    return addr_str

# Code to create generate random request uri
def get_rand_url():
    request_items = ["favicon","index.php","index.html", "style.css", "login.php","logout.php"]
    request_methods = ["GET","POST","HEAD"]
    request_codes = ["504","200","404","503","500","302","301"]
    uri = get_rand_ip() + " " +  str(datetime.datetime.utcnow()) + " " + random.choice(request_methods) + " "+ "/" + random.choice(request_items) + "/" + " " + random.choice(request_codes) + " " + str(random.randint(0,2000))
    return uri

def write_log_files(num_of_file,num_of_lines):
    while num_of_file > 0:
        filename = datetime.datetime.now().strftime("%Y%m%d-%H%M%S%f")
        file = open("access_logs_%s.txt" % filename, "w")
        for i in range(0,num_of_lines):
            file.write(get_rand_url()+"\n")
        file.close()
        num_of_file-=1


number_of_file = int(input("Enter the number of files to be created?"))
number_of_lines = int(input("Enter the number of lines in a file?"))
write_log_files(number_of_file,number_of_lines)
