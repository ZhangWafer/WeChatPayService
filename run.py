import wzhifuSDK
from wzhifuSDK import order_num

app_id='wx689b069eb440eed1'
mch_id='1521585261'
ramdom32_before=wzhifuSDK.random_str(8)
detail_before='{"cost_price":1000,"receipt_id":"wx123","goods_detail":[{"goods_id":"78","goods_name":"lunch","quantity":1,"price":1000},{"goods_id":"666","goods_name":"lunch","quantity":2,"price":1}]}'

APP_ID =  "<![CDATA[wx689b069eb440eed1]]>" # 你公众账号上的appid
MCH_ID = "1521585261" # 你的商户号
API_KEY = "zh43be9fe2fd47a8171zhga21e123713"  # 微信商户平台(pay.weixin.qq.com) -->账户设置 -->API安全 -->密钥设置，设置完成后把密钥复制到这里
APP_SECRECT = "f82a881cd1a9da63c279120b0d167333"
UFDODER_URL = " https://zhga.bryzf.com/unifiedorder"  # 该url是微信下单api

NOTIFY_URL_before='https://www.baidu.com/'
NOTIFY_URL = "<![CDATA[https://www.baidu.com/]]>"  # 微信支付结果回调接口，需要改为你的服务器上处理结果回调的方法路径
CREATE_IP = 'xxx'  # 你服务器的IP

random32="<![CDATA["+ramdom32_before+"]]>"
out_trade_no_before=order_num('13631240700')
out_trade_no='<![CDATA['+out_trade_no_before+']]>'
detail='<![CDATA[{"cost_price":1000,"receipt_id":"wx123","goods_detail":[{"goods_id":"78","goods_name":"lunch","quantity":1,"price":1000},{"goods_id":"666","goods_name":"lunch","quantity":2,"price":1}]}]]>'
spIp_before='127.0.0.1'
spIp='<![CDATA[127.0.0.1]]>'



#加签之前的字典数据
dict1 = {'appid' : app_id, 'mch_id' : mch_id,'nonce_str': ramdom32_before,'body':'body',
     'detail':detail_before,'device_info':'013467007045764',
    'out_trade_no':out_trade_no_before,'total_fee':'888','spbill_create_ip':spIp_before,'notify_url':NOTIFY_URL_before,'trade_type':'JSAPI'}

Sign="<![CDATA["+wzhifuSDK.get_sign(dict1,API_KEY)+"]]>"


dict2 = {'appid' : APP_ID, 'mch_id' : MCH_ID,'nonce_str': random32,'sign':Sign,'body':'<![CDATA[body]]>',
     'detail':detail,'device_info':'013467007045764',
    'out_trade_no':out_trade_no,'total_fee':'888','spbill_create_ip':spIp,'notify_url':NOTIFY_URL,'trade_type':'JSAPI'}

response=wzhifuSDK.wx_pay_unifiedorde(dict2,UFDODER_URL)

print("ssss");

