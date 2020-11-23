import sys

class Hamming:

    nr_bits = []

    def calcRedundantBits(self, m): 
        for i in range(m): 
            if(2**i >= m + i + 1): 
                return i 
    
    def posRedundantBits(self, data, r): 
        j = 0
        k = 1
        m = len(data) 
        res = '' 
        for i in range(1, m + r+1): 
            if(i == 2**j): 
                res = res + '0'
                j += 1
            else: 
                res = res + data[-1 * k] 
                k += 1

        return res[::-1] 

    def calcParityBits(self, arr, r): 
        n = len(arr) 
        for i in range(r): 
            val = 0
            for j in range(1, n + 1): 
                if(j & (2**i) == (2**i)): 
                    val = val ^ int(arr[-1 * j]) 
            arr = arr[:n-(2**i)] + str(val) + arr[n-(2**i)+1:] 

        return arr 
    
    
    def detectError(self, arr): 
        n = len(arr) 
        res = 0
        for i in range(4): # in range(nr)
            val = 0
            for j in range(1, n + 1): 
                if(j & (2**i) == (2**i)): 
                    val = val ^ int(arr[-1 * j]) 
            res = res + val*(10**i) 

        if res == 0:
            return 0
        idx = int(str(res), 2)
        if arr[len(arr)-idx] == '1':
            farr = arr[:len(arr)-idx] + '0' + arr[len(arr)-idx+1:]
            return farr
        farr = arr[:len(arr)-idx] + '1' + arr[len(arr)-idx+1:]

        return farr

    def data_extract(self, data_bytes):
        j = 0
        final_bytes = data_bytes
        for i in range(len(data_bytes)):
            if (i == 2**j):
                final_bytes = final_bytes[:len(final_bytes)-i] + '-' + final_bytes[len(final_bytes)-i+1:]
                j = j + 1
        final_bytes = final_bytes.replace('-', '')
        final_bytes = '0b' + final_bytes
        final_bytes = int(final_bytes, 2)
        return final_bytes.to_bytes(1, byteorder=sys.byteorder).decode('utf-8')

    def make_bytes(self, msg):
        final_bytes = ''
        msg = bytes(msg, 'utf-8')
        for byte in msg:
            tbyte = bin(byte).replace('0b','')
            r = self.calcRedundantBits(len(tbyte))
            self.nr_bits.append(r)
            arr = self.posRedundantBits(tbyte, r)
            arr = self.calcParityBits(arr, r)
            final_bytes = arr + '/' + final_bytes

        return final_bytes