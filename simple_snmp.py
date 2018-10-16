from snmp_helper import snmp_get_oid, snmp_extract

COMMUNITY_STRING = 'galileo'
SNMP_PORT = 161

device_ip_list = (
    '184.105.247.70', 
    '184.105.247.71')    

oid_list = ('1.3.6.1.2.1.1.5.0', '1.3.6.1.2.1.1.1.0')

for device in device_ip_list:
    a_device = (device, COMMUNITY_STRING, SNMP_PORT)
    for OID in oid_list:
        snmp_data = snmp_get_oid(a_device, oid=OID)
        output = snmp_extract(snmp_data)
        print output + '\n\n'


