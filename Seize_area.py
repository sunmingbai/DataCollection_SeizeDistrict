# 调取百度 API抓取小区所在的行政区域
#  seizearea(小区名称，城市，信令)
import pandas as pd
import numpy as np
import requests
import json
def seizearea(query,region,ak):
    url='http://api.map.baidu.com/place/v2/search?query='+query+'&region='+region+'&output=json&ak='+ak
    get_content=requests.get(url,'json')

    # status code=200 means get what we want successfllly
    # else print waring message
    # and then exit the function
    if get_content.status_code!=200:
        print("Warning! The return content maybe wrong!")
        return;

    # pharse the json data
    loads_object=json.loads(get_content.text)
    tar_area=loads_object['results'][1]['area']
    return tar_area

if __name__=='__main__':
    query='莘松二村'
    region='上海'
    ak='nboZEDUp7FzFu9FfCWtk3TcLzE8GtVWL'
    areaout=seizearea(query,region,ak)
    print(areaout)
        