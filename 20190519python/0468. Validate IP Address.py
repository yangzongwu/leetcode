class Solution:
    def validIPAddress(self, IP: str) -> str:
        if '.' in IP:
            return self.validIP4Address(IP)
        if ':' in IP:
            return self.validIP6Address(IP)
        return "Neither"
    
    def validIP4Address(self,IP):
        IP_list=IP.split('.')
        if len(IP_list)!=4 or ""  in IP_list:
            return "Neither"
        for ip in IP_list:
            if ip[0]=='0' and len(ip)>1:
                return "Neither"
            for s in ip:
                if s not in '1234567890':
                    return "Neither"
            if int(ip)>255:
                return "Neither"
        return "IPv4"
    
    def validIP6Address(self,IP):
        IP_list=IP.split(':')
        if len(IP_list)!=8 or '' in IP_list:
            return "Neither"
        for ip in IP_list:
            if len(ip)>4:
                return "Neither"
            for s in ip:
                if s not in '1234567890abcedfABCDEF':
                    return "Neither"
        return "IPv6"
