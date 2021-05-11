from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from e_book.models import EBook
from accounts.models import Users
from django.views.decorators.csrf import csrf_exempt
# from paytm import checksum
from paytm.checksum import generate_checksum, verify_checksum
# import PaytmChecksum
import requests
import json

MERCHANT_KEY = '0cZ3ZtIyd9aESQ69'
# Create your views here.

# e-Book Detail
def eBook_detail(request,e_book_id):
    e_book = EBook.objects.get(id = e_book_id)
    print(e_book_id)
    return render(request,"e-book/e-book.html",{"e_book":e_book})

def buyNow(request,e_book_id):
    user = Users.objects.get(email = request.session.get("email"))
    book = EBook.objects.get(id = e_book_id)

    # param_dict = {
    #     'MID': "WObEwr11636723206338",
    #     'ORDER_ID':book.id,
    #     'TXN_AMOUNT':str(book.eBook_price),
    #     'CUST_ID':user.email,
    #     'INDUSTRY_TYPE_ID':"retail",
    #     'WEBSITE':"WEBSTAGING",
    #     'CHANNEL_ID':"WEB",
    #     'CALLBACK_URL':"http://127.0.0.1:8000/home/e-book/1/handlerequest/",
    #     # "requestType"   : "Payment",
    #     # "mid"           : "WObEwr11636723206338",
    #     # "websiteName"   : "WEBSTAGING",
    #     # "orderId"       : book.id,
    #     # "callbackUrl"   : "http://127.0.0.1:8000/home/e-book/1/handlerequest/",
    #     # "txnAmount"     : {
    #     #     "value"     : str(book.eBook_price),
    #     #     "currency"  : "INR",
    #     # },
    #     # "userInfo"      : {
    #     #     "custId"    : user.email,
    #     # },
    # }
    # # param_dict["CHECKSUMHASE"] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
    # param_dict["CHECKSUMHASE"] = checksum
    # # param_dict["CHECKSUMHASE"] = check(param_dict, MERCHANT_KEY)



    # import checksum generation utility
    # You can get this utility from https://developer.paytm.com/docs/checksum/
    paytmParams = dict()
    MID = "ZbfxFl37233129758787"
    paytmParams = {
        # "requestType"   : "Payment",
        # "mid"           : MID,
        # "websiteName"   : "WEBSTAGING",
        # "orderId"       : book.id,
        # "callbackUrl"   : "http://127.0.0.1:8000/home/e-book/1/handlerequest/",
        # "txnAmount"     : {
        #     "value"     : book.eBook_price,
        #     "currency"  : "INR",
        # },
        # "userInfo"      : {
        #     "custId"    : user.email,
        # },
        'MID': MID,
        'ORDER_ID':str(book.id),
        'TXN_AMOUNT':str(book.eBook_price),
        'CUST_ID':user.email,
        'INDUSTRY_TYPE_ID':"Retail",
        'WEBSITE':"WEBSTAGING",
        'CHANNEL_ID':"WEB",
        'CALLBACK_URL':"http://127.0.0.1:8000/home/e-book/handlerequest/",
    }
    # Generate checksum by parameters we have in body
    # Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys 
    # checksum.generateSignature(json.dumps(paytmParams), MERCHANT_KEY)
    # paytmParams["head"] = {
    #     "signature"    : checksum.generateSignature(json.dumps(paytmParams), MERCHANT_KEY)
    #     # "signature"    : checksum.generateSignature(json.dumps(paytmParams), MERCHANT_KEY)
    # }
    # checksums = checksum.generateSignature(json.dumps(paytmParams), MERCHANT_KEY)
    checksum = generate_checksum(paytmParams, MERCHANT_KEY)
    paytmParams['CHECKSUMHASH'] = checksum
    print(paytmParams)

    # post_data = json.dumps(paytmParams)

    # for Staging
    # url = f"https://securegw-stage.paytm.in/theia/api/v1/initiateTransaction?mid={MID}&orderId={book.id}"

    # for Production
    # url = "https://securegw.paytm.in/theia/api/v1/initiateTransaction?mid=YOUR_MID_HERE&orderId=ORDERID_98765"
    # response = requests.post(url, data = post_data, headers = {"Content-type": "application/json"}).json()
    # print(response)

    return render(request,"e-book/paytm.html",{"param":paytmParams})

@csrf_exempt
def handlerequest(request):
    return HttpResponse("done")