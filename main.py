from MindSphere import MindSphere

mindsphere = MindSphere(app_Name=None,
                        app_Version=None,
                        tenant=None,
                        gateway_URL=None,
                        client_ID=None,
                        client_Secret=None
                        )
assetId,aspectName = None,None

mindsphere.putTimeSeriesData(assetId,aspectName,{"_time":None,"Temperature":90.50})
