class CONFIG:
    VERSION = "2.1.12"
    PRINT_URL = 'http://im.memobird.cn/ashx/DesClientInterface.ashx/'
    APP_URL = 'http://im.memobird.cn/wse/wsesmart.asmx'
    SETTING_URL = 'http://im.memobird.cn/ashx/DesClientInterface.ashx/'
    USER_AGENT = '%E5%92%95%E5%92%95%E6%9C%BA/5 CFNetwork/897.15 Darwin/17.5.0'
    XML_TEMPLATE = '<?xml version="1.0" encoding="utf-8"?>\n<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">\n<soap:Header><Mysoapheader xmlns="http://tempuri.org/"><UserID>adming</UserID><PassWord>admin20151010Memobird</PassWord></Mysoapheader></soap:Header>\n<soap:Body><OPERATION xmlns="http://tempuri.org/"><msg>MESSAGE</msg></OPERATION></soap:Body></soap:Envelope>\n'
    LOGIN_MESSAGE_TEMPLATE = '{"type": "0","strUserPwd": "PASSWORD","remark": "iPhone","userCode": "USERNAME","ip": "192.168.1.1","version": "1.4.4"}'
    BIND_MACHINE_MESSAGE_TEMPLATE = '{"strGuid":"GUID","intUserID":"USERID"}'
    SOAP_HEADER = '{"SOAPAction": "http://tempuri.org/OPERATION", "User-Agent": "' + USER_AGENT + '", "Content-Type": "text/xml; charset=utf-8", "Accept-Language": "en-us"}'
    XML_RESPONSE_LOCATOR = '{http://schemas.xmlsoap.org/soap/envelope/}Body/{http://tempuri.org/}OPERATIONResponse/{http://tempuri.org/}OPERATIONResult'
