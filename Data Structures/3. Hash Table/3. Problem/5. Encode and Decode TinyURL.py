import random
import string

class Codec:
    """
    Encode and decode URLs
    """
    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}
        self.base_url = "http://tinyurl.com/"
    
    def encode(self, longUrl):
        """Encode long URL to short URL"""
        if longUrl in self.url_to_code:
            return self.base_url + self.url_to_code[longUrl]
        
        # Generate random code
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        
        while code in self.code_to_url:
            code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        
        self.url_to_code[longUrl] = code
        self.code_to_url[code] = longUrl
        
        return self.base_url + code
    
    def decode(self, shortUrl):
        """Decode short URL to long URL"""
        code = shortUrl.replace(self.base_url, "")
        return self.code_to_url.get(code, "")

# Usage:
codec = Codec()
url = "https://leetcode.com/problems/design-tinyurl"
short = codec.encode(url)
print(short)  # http://tinyurl.com/4iQAx6
print(codec.decode(short))  # https://leetcode.com/problems/design-tinyurl