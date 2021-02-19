import requests
import json


input_data= {
    
    "Id": 1461,
    "MSSubClass": 20,
    "MSZoning": "RH",
    "LotFrontage": 80,
    "LotArea": 11622, 
    "Street": "Pave",
    "Alley": "NA",
    "LotShape": "Reg",
    "LandContour": "Lvl",
    "Utilities": "AllPub",
    "LotConfig": "Inside",
    "LandSlope": "Gtl",
    "Neighborhood" : "NAmes",
    "Condition1" : "Feedr",
    "Condition2" : "Norm",
    "BldgType" : "1Fam",
    "HouseStyle" : "1Story",
    "OverallQual" : 5,
    "OverallCond" : 6,
    "YearBuilt": 1961 ,  
    "YearRemodAdd" : 1961,    
    "RoofStyle" : "Gable",
    "RoofMatl" : "CompShg" ,   
    "Exterior1st" : "VinylSd" ,
    "Exterior2nd"  : "VinylSd",
    "MasVnrType" : "None" ,
    "MasVnrArea" : 0 ,
    "ExterQual"  : "TA" ,
    "ExterCond" : "TA"  ,
    "Foundation" : "CBlock" , 
    "BsmtQual"   : "TA",
    "BsmtCond"   : "TA" ,
    "BsmtExposure"   : "No" ,
    "BsmtFinType1"   : "Rec" ,
    "BsmtFinSF1" : 468 ,
    "BsmtFinType2" : "LwQ",
    "BsmtFinSF2" : 44 ,
    "BsmtUnfSF" : 270  , 
    "TotalBsmtSF" : 882,
    "Heating" : "GasA",
    "HeatingQC" : "TA"  ,
    "CentralAir" : "Y" ,
    "Electrical" : "SBrkr",  
    "1stFlrSF" : 896   ,
    "2ndFlrSF" : 0   ,
    "LowQualFinSF"  : 0  , 
    "GrLivArea"  : 896 ,
    "BsmtFullBath"  : 0  ,
    "BsmtHalfBath"  : 0  ,
    "FullBath"  : 1  ,
    "HalfBath"  : 0  ,
    "BedroomAbvGr" : 2  ,  
    "KitchenAbvGr" : 1  , 
    "KitchenQual" : "TA",
    "TotRmsAbvGrd"  : 5  , 
    "Functional" : "Typ" ,
    "Fireplaces"  : 0,
    "FireplaceQu" : "NA",
    "GarageType" : "Attchd", 
    "GarageYrBlt"  : 1961,
    "GarageFinish"  : "Unf" , 
    "GarageCars"  : 1,
    "GarageArea"  : 730,
    "GarageQual" : "TA"  ,
    "GarageCond"  : "TA" ,
    "PavedDrive"  : "Y",
    "WoodDeckSF"  : 140,
    "OpenPorchSF" : 0,
    "EnclosedPorch"  : 0 ,
    "3SsnPorch"  : 0 ,
    "ScreenPorch" : 120,
    "PoolArea"  : 0  ,
    "PoolQC" : "NA" ,
    "Fence"  : "MnPrv" ,
    "MiscFeature" : "NA",
    "MiscVal" : 0,
    "MoSold"  : 6,
    "YrSold" : 2010 ,
    "SaleType"  : "WD"  ,
    "SaleCondition"  : "Normal" ,
    "SalePrice" : 208500
    
}



url = "https://q0cl1wwzb7.execute-api.us-east-2.amazonaws.com/dev/joke"

r = requests.post(url, json=input_data)
print("result without securely key: ", r.json())



# key = {'x-api-key': 'tI95Zb3Ikr5l8jK1o3DDN4BOzFDLi13y3GYZ5uDW'}


# r = requests.post(url, json.dumps(input_data), headers=key)
# res = json.loads(r.content)
# print("result with securely key: ", res)













