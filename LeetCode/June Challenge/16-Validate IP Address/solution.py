class Solution:
    def validIPAddress(self, IP: str) -> str:
        # Function to check IPv4
        def isIPv4(ipstr):
            groups = ipstr.split('.')
            
            if len(groups) != 4:
                return False
            for g in groups:
                if len(g) == 0:
                    return False
                
                if g[0] == '0' and len(g) > 1:
                    return False
                
                if not g.isdigit() or int(g) < 0 or int(g) > 255:
                    return False
                
            return True
        
        # Function to check IPv6
        def isIPv6(ipstr):
            groups = ipstr.split(":")
            
            # IPv6 have 8 gropus
            if len(groups) != 8:
                return False
            
            for g in groups:
                if len(g) > 4 or len(g) < 1:
                    return False
                
                #hex only
                for char in g:
                    if char not in string.hexdigits:
                        return False
            return True
        
        # Main Code
        if isIPv4(IP):
            return "IPv4"
        if isIPv6(IP):
            return "IPv6"
        return "Neither"
