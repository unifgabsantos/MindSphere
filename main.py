from MindSphere import MindSphere

mindsphere = MindSphere(app_Name="",
                        app_Version="",
                        tenant="",
                        gateway_URL="",
                        client_ID="",
                        client_Secret=""
                        )
assetId = None
aspectName = None
fromDateTime = "2023-10-04T00:00:00Z"
toDateTime = "2023-10-04T10:00:00Z"
print(mindsphere.getTimeSeries(assetId,aspectName,fromDateTime,toDateTime))


#mindsphere.putTimeSeriesData(assetId,aspectName,{"_time":None,"Temperature":90.50})
