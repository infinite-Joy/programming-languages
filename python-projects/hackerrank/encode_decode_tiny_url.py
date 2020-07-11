"""
https://leetcode.com/problems/encode-and-decode-tinyurl/
we can make the total length
0-9, a-z, A-Z
take the ascii numbers of the url and multiply them together. if the total number of digits is odd then make it negative.
then divide the number 6 times with 62 and get the modulus. we should get the hash
we will compute the hash and then make the hash the key and then value the dictionary
=============

"""
from functools import reduce
class Codec:
    base_chars = string.digits + string.ascii_letters
    base = len(base_chars)
    hashes = {}
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        full_url = longUrl.split("/")
        long_url = full_url[-1]
        long_url2 = [ord(ch) for ch in long_url]
        long_url1 = map(lambda x: x + 100, long_url2)
        multiplied = reduce(lambda a, b: a * b, long_url1, 1)
        total = sum(multiplied)
        hash_list = []
        for i in range(6):
            hash  = total % base
            total = (total - hash) // base
            hash_list.append(self.base_chars[hash])
        hash_list = reversed(hashes)
        this_hash = “”.join(hash_list)
        self.hashes[this_hash] = long_url
        return  “/”.join(full_url[:-1] + [this_hash])
    def decode(self, shortUrl: str) -> str:
            """Decodes a shortened URL to its original URL."""
        full_url = shortUrl.split("/")
        hash = full_url[-1]
        url = self.hashes[hash]
        long_url = full_url[:-1] + [url]
        return “/”.join(long_url)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

