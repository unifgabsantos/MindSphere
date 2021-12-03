# santos.gabriel@siemens.com
# https://www.linkedin.com/in/gabriellopes8/
import json,base64,requests,datetime
class MindSphere():
    def __init__(self,app_Name:str,app_Version:str,tenant:str,gateway_URL:str,client_ID:str,client_Secret:str) -> None:
        self.app_Name = app_Name
        self.app_Version = app_Version
        self.tenant = tenant
        self.gateway_URL = gateway_URL
        self.client_ID = client_ID
        self.client_Secret = client_Secret
    def getToken(self):
        if("" in [self.client_ID,self.client_Secret]):
            print("Please set your credentials")
            return False
        secret = (base64.b64encode(f"{self.client_ID}:{self.client_Secret}".encode())).decode()
        headers = {
            "Content-Type":"application/json",
            "X-SPACE-AUTH-KEY":f"Bearer {secret}"
        }
        response = requests.post(f"{self.gateway_URL}api/technicaltokenmanager/v3/oauth/token?appName={self.app_Name}&appVersion={self.app_Version}&hostTenant={self.tenant}&userTenant={self.tenant}",headers=headers)
        return json.loads(response.text)['access_token'] 
    def getAssetList(self):
        headers = {
            "Authorization":'bearer '+self.getToken(),
            "Content-Type":"'application/json'",
        }
        return json.loads(requests.get(f"{self.gateway_URL}api/assetmanagement/v3/assets",headers=headers).text)['_embedded']['assets']
    def putTimeSeriesData(self,assetId:str,aspectName:str,payload:dict):
        '''Create a dictionary and send the payload parameter, in the dictionary create a _time key and set its value to None
        
        Example:
        
            putTimeSeriesData(assetId,aspectName,{"_time":None,"Temperature":90.50})
        '''
        headers = {
            "Authorization":'bearer '+self.getToken(),
            "Content-Type":"application/json",
        }
        url = f"{self.gateway_URL}api/iottimeseries/v3/timeseries/{assetId}/{aspectName}"
        payload.update({"_time":datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()})
        print(requests.put(url,json=[payload],headers=headers).status_code)
    def getAspectName(self,assetId):
        headers = {
            "Authorization":'bearer '+self.getToken(),
            "Content-Type":"application/json",
        }
        url = f'{self.gateway_URL}api/assetmanagement/v3/assets/{assetId}/aspects'
        return requests.get(url,headers=headers).text
