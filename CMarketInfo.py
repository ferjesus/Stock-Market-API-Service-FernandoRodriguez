import json
import httpx


class CMarketInfo():
     
    def __init__(self):
       self.pcParam  = None
       self.pcData   = None
       self.pcParams   = None
       self.pcError = None
       self.pcToken = None
       self.pcHttpCode = None

    def mxValParam(self):
        if not'MARKET'in self.pcParam :
            self.pcError = 'PARAMETER [MARKET] NOT DEFINED'
            return False
        if not'FUNCTION'in self.pcParam :
            self.pcError = 'PARAMETER [FUNCTION] NOT DEFINED'
            return False
        if not'SIZE'in self.pcParam :
            self.pcError = 'PARAMETER [SIZE] NOT DEFINED'
            return False
        if self.pcToken == '':
            self.pcError = 'PARAMETER [token] NOT DEFINED'
            return False
        return True

    def omMarketinfo(self):
        llOk = self.mxValParam()
        if not llOk:
            self.pcHttpCode = 400
            return False
        llOk = self.mxMarketinfo()
        if not llOk:
             self.pcError = 'ERROR IN THE QUERY'
             self.pcHttpCode = 500
             return False
        self.pcHttpCode = 200
        return llOk


    
    def mxMarketinfo(self):
        #r = httpx.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&outputsize=compact&apikey=X86NOH6II01P7R24')
        self.pcParams = {'function':  self.pcParam['FUNCTION'], 'symbol': self.pcParam['MARKET'], 'outputsize':  self.pcParam['SIZE'], 'apikey': self.pcToken}
        r = httpx.get('https://www.alphavantage.co/query', params=self.pcParams)
        self.pcData = r.json()
        return True
        
