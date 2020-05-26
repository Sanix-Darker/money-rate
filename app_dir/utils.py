# coding: utf-8

from flask import jsonify
import requests
import json
from app_dir.SeleniumScrap import SeleniumScrap

from app_dir.settings import *

def core(amount, from_, to_):
    if amount is not None and from_ is not None and to_ is not None:
        r_content = json.loads(requests.get(SCRAP_HOST + "?amount=" + amount + "&from=" + from_ + "&to=" + to_).content.decode())
        if r_content["status"] == "success":
            response = jsonify(
                {
                    'status':'success',
                    'result': r_content["result"]
                }
            )
        else:
            response = jsonify(
                {
                    'status':'error',
                    'result': r_content["message"]
                }
            )
    else:
        response = jsonify(
            {
                'status':'error',
                'message': 'some parameters are missing amount:{}, from:{}, to:{} '.format(amount, from_, to_) 
            }
        )

    return response

def core_scrap(amount, from_, to_):
    if amount is not None and from_ is not None and to_ is not None:
        s = SeleniumScrap("//span[@class='converterresult-toAmount']")
        result = s.fetch("https://www.xe.com/currencyconverter/convert/?Amount="+str(amount)+"&From="+str(from_)+"&To="+str(to_)+"")

        response = jsonify(
            {
                'status':'success',
                'result': result
            }
        )
    else:
        response = jsonify(
            {
                'status':'error',
                'message': 'some parameters are missing amount:{}, from:{}, to:{} '.format(amount, from_, to_) 
            }
        )

    return response