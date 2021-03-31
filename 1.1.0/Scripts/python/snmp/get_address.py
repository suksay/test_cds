
import json
import quicksnmp
from pysnmp import hlapi
from pyconfig import *
#from pyconfig import _MW_INVARIANT_ID_, _HUAWEI_MW_VERSION_ID_, _NEC_MW_VERSION_ID_
import os
from contextlib import contextmanager
import sys
import ipaddress
from multiprocessing import Pool
from  aai_requests import *
import json
from jinja2 import Environment, FileSystemLoader



global devices
devices = dict()

#Checking workspace
cwd = os.getcwd()
if cwd.split('/')[-1]!='snmp' : os.chdir("Scripts/python/snmp/")

env = Environment(loader=FileSystemLoader('./aai_templates/'))

#Network parameters
network = "172.20.183.128"
mask = "25"

hua_ne_id =  ".1.3.6.1.4.1.2011.2.25.3.40.2.1.1.0"

def create_dict(*args):
    return dict({i:eval(i) for i in args})

@contextmanager
def no_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout

#SNMP Ping + Chassis ID + Hostname + Vendor retrieving function
def get_hostname(ip):
    """
    inputs:
        ip (str) : Device IP address
    
    outputs:
        Tuple : (Chassis ID, [Device information])
    """ 
    global devices
    def create_dict(*args):
        return dict({i:eval(i) for i in args})
    try:
        with no_stdout():
            vendor=quicksnmp.get(str(ip), snmp_ping,credentials)
    except:
        return False
    else:
        address=str(ip)
        vendor=str(vendor[0][1])
        id=''
        if vendor=="Optix product" : 
            vendor="huawei"
            ne_id = str(quicksnmp.get_oid(str(ip), hua_ne_id,credentials)[0][-1])
            hostname = str(quicksnmp.get_oid(str(ip), huawei_sysname,credentials)[0][1])
            id='0x'+str(quicksnmp.get(str(ip), lldp_hua_id,credentials)[0][1]).replace('-','')
            return (id,[address,hostname,vendor,ne_id])            
        elif vendor=='ipe' : 
            vendor="nec-ipa"
            hostname = str(quicksnmp.get(str(ip), sysName_named_oid,credentials)[0][1])
            id=quicksnmp.get(str(ip), lldp_id,credentials)[0][1].prettyPrint()
        elif vendor=='-':
            try :
                #Checking the "Equipment Type" OID that return an integer >10000 for VR products
                if int(str(quicksnmp.get_oid(address,nec_vr_type,credentials)[0][1]))>10000:
                    vendor="nec-vr"
                    hostname = str(quicksnmp.get(str(ip), sysName_named_oid,credentials)[0][1])
                    id=quicksnmp.get(str(ip), lldp_id,credentials)[0][1].prettyPrint()
                else: raise ValueError('')
            except:
                return False
        if id=='': return False
        return (id,[address,hostname,vendor])



list_addr=ipaddress.IPv4Network(network+'/'+mask).hosts()

#Building a pool of subprocesses for each IP address (e.g : for /24 network, creates 254 subprocesses)
"""
This operation may require analysis in order to get the best optimized value here.
The subprocessing segmentation here is therefore guaranteed up to 1024 addresses.
"""
a_pool = Pool(2**(32-int(mask))-2)

#Subprocessing get_hostname() function for each addresses
db_hostname=a_pool.map(get_hostname,list_addr)

#Filtering successfully polled addresses
db=[host for host in db_hostname if host != False]

#Building and updating/creating Inventory file
for id,infos in db:
    address=infos[0]
    hostname=infos[1]
    vendor=infos[2]
    if vendor == "huawei" :
        ne_id = infos[3]
        devices[id]=create_dict('address','hostname','vendor', 'ne_id')
    else : 
        devices[id]=create_dict('address','hostname','vendor')


#print("DEVICES FOUND : ")
### Normalize data for AAI Task ###
aai_devices_data = dict()
aai_devices_data['devices'] = list()

for device_id in devices :
    devices[device_id]['device_id'] = device_id
    aai_devices_data['devices'].append(devices[device_id])

fp = open('inventory.json', 'w+') 
json.dump(aai_devices_data['devices'], fp)
fp.close()
print(aai_devices_data)

