# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 23:01:00 2021

@author: SHUBHAM
"""

import math

def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5

def testsquare():
    num = 7
    assert 7*7 == 49

def tesequality():
    assert 11 == 11

# num=25
# assert math.sqrt(num) == 5


# num = 7
# assert 7*7 == 49

# import os
# import json
# import requests
# from requests.auth import HTTPBasicAuth
# import pandas as pd


# def download():
    
#     # Path where data will be downloaded
#     main_path='U:\\planet_data_check'
    
#     # API Key
#     PLANET_API_KEY = '74eadbb19b61411cb3bb3360b3e2f566'
    
    
#     item_type = "PSScene4Band"
    
    
    
    
#     search_result = \
#       requests.get(
#         'https://api.planet.com/basemaps/v1/mosaics',
#         auth=HTTPBasicAuth(PLANET_API_KEY,''))
        
#     #assert search_result.status_code==200
    
#     result=search_result.json()
    
#     #bbox coordinates
#     # Maharashtra
#     # lx=72.6
#     # ly=15.6
#     # ux=80.8
#     # uy=22.0
    
#     # #Indapur
#     # lx=74.6
#     # ly=17.8
#     # ux=75.1
#     # uy=18.3
    
#     f_date=result['mosaics'][8]['first_acquired']
#     e_date=result['mosaics'][8]['last_acquired']
    
#     bbox=pd.read_csv('U:\\Taluka_bbox_updated.csv',index_col=False)
#     bbox=bbox[(bbox['Taluka']=='Akole') | (bbox['Taluka']=='Igatpuri')]
    
#     clist=[]              #all titles list
#     quad_list=[]          #Non overlapping titles
#     for row in bbox.iterrows():
        
#         taluk=row[1]['Taluka']
#         print('Taluka is {}'.format(taluk))
        
#         lx=row[1]['lx']
#         ly=row[1]['ly']
#         ux=row[1]['ux']
#         uy=row[1]['uy']
        
#         quad=result['mosaics'][8]['_links']['quads']
#         quad=quad.replace('lx','').replace('ly','').replace('ux','').replace('uy','').format(lx,ly,ux,uy)
        
#         search_result2 = \
#         requests.get(
#         quad,
#         auth=HTTPBasicAuth(PLANET_API_KEY,''))
    
        
    
#         quad_result=search_result2.json()
        
#         if os.path.exists(os.path.join(main_path,taluk))==False:
#                 os.mkdir(os.path.join(main_path,taluk))
             
#         print(len(quad_result['items']))        
#         for i in range(len(quad_result['items'])):
            
#             download=quad_result['items'][i]['_links']['download']
#             dat_id=quad_result['items'][i]['id']
            
            
#             clist.append(dat_id)
            
                    
#             if dat_id not in quad_list:
                
#                 print(dat_id)
                
#                 response=requests.get(download,auth=HTTPBasicAuth(PLANET_API_KEY,''))
#                 assert response.status_code==200
#                 title=response.headers['content-disposition'].split('=')[1].strip('"')
                
#                 open(os.path.join(main_path,taluk,title),'wb').write(response.content)  
#                 quad_list.append(dat_id)
                
#             else:
#                 print("Duplicate id{} ".format(dat_id))
            
            
            
#     #############Metadata editing in the files###################################    
#     #edit_path contains the path of gdal_edit.py file
#     #Change these paths for metadata change
#     #Directory structure example
#     #-D:
#     #--planet_data
#     #---folder with Taluka name
#     #----data in the form of tif files
#     edit_path='C:\\ProgramData\\Anaconda3\\Lib\\site-packages\\osgeo\\scripts\\gdal_edit.py'
#     #directory where the Planet data is stored
#     filedir='U:\\planet_data_check\\'
#     from os import path
#     from subprocess import Popen,PIPE
#     c=0
    
#     assert os.listdir(filedir)!=[]
    
#     for j in os.listdir(filedir):
        
#         fdir=os.path.join(filedir,j)
        
#         if len(os.listdir(fdir))!=0:
#             print("{} is not empty".format(j))
            
            
#             for i in os.listdir(fdir):
                
                
#                 cmd1 = ['python',path.normpath(edit_path),path.normpath(fdir+"\\"+i),'-mo','MOSAIC_START_DATE={}'.format(f_date),'-mo','MOSAIC_END_DATE={}'.format(e_date)]
#                 process = Popen(cmd1, stdout=PIPE, stderr=PIPE)
#                 print(process.communicate())
#                 c+=1
#                 print("Counter : {}".format(c))
                
#         else:
#             print("{} empty".format(j))
            
#     return [search_result.status_code,response.status_code]
            
# def test_m():
#     assert download()==[200,200]
    
           
            
