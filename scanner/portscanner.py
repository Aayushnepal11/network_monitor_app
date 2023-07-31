import nmap
import ipaddress
import pickle



def read_binary(filename):
    with open(f'scanner/reports/simpleScan/{filename}.pickle', 'rb') as handle:
        seraialized_file = pickle.load(handle)
    return seraialized_file

def write_binary(ip,*args):
    with open(f'scanner/reports/simpleScan/{ip}.pickle', 'wb') as handle:
        serialized_file =  pickle.dump(args, handle)   
    return serialized_file

def simpleScan(ip, **kwargs):
    try:
        if not ipaddress.IPv4Address(ip):
            return "This is not a valid ip".format(ip)
    except ipaddress.AddressValueError as ip_addressError:
        return ip_addressError
    nm = nmap.PortScanner()
    result = nm.scan(ip, arguments='-p1-1025 -sV')
    for key, value in result.items():
        kwargs[key] = value
    try:
        write_binary(ip, result)
    except FileNotFoundError as fileMesssage:
        pass
        return fileMesssage
    return kwargs.values()