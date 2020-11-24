#%%
#import requests

#auth_url = "https://login.microsoftonline.com/common/oauth2/authorize?resource=49dea0e2-a807-4dba-b41c-189445491a5b"

#%%
url = "https://digitwin-test.api.weu.digitaltwins.azure.net"

#%%
import azure.identity
import azure.digitaltwins.core

#%%
cred = azure.identity.DefaultAzureCredential()

#%%
client = azure.digitaltwins.core.DigitalTwinsClient(url, cred)

#%%
temp_model = {
  "@context": "dtmi:dtdl:context;2",
  "@id": "dtmi:com:example:EV;1",
  "@type": "Interface",
  "displayName": "EV",
  "contents": [
    {
      "@type": "Telemetry",
      "name": "chargingRate",
      "schema": "double"
    },
    {
      "@type": "Property",
      "name": "isCharging",
      "schema": "boolean"
    },
    {
      "@type": "Property",
      "name": "soc",
      "schema": "float"
    }
  ]
}


#%%
client.create_models(temp_model)
## PROBLEEM: Ei Suuda ära autentida