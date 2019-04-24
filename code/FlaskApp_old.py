import xml.etree.ElementTree as ET
from flask import Flask,render_template,request,jsonify
import wzhifuSDK
from wzhifuSDK import order_num

app = Flask(__name__)


print("启动程序！")
# 微信支付信息
#加签前信息
APP_ID = "wx19d346a2910ab88e"  # 你公众账号上的appid
MCH_ID = "1523807111"  # 你的商户号
API_KEY = "Cv1D2rLD4K6bnlzu3kOZasf24YfsTiOf"  # 微信商户平台(pay.weixin.qq.com) -->账户设置 -->API安全 -->密钥设置，设置完成后把密钥复制到这里
APP_SECRECT = "dc71b5f497d9a35162e7606a8dff6f78"
UFDODER_URL = "https://api.mch.weixin.qq.com/pay/unifiedorder"  # 该url是微信下单api
ramdom8_before=wzhifuSDK.random_str(8)
detail_before='{"cost_price":1000,"receipt_id":"wx123","goods_detail":[{"goods_id":"78","goods_name":"lunch","quantity":1,"price":1000},{"goods_id":"666","goods_name":"lunch","quantity":2,"price":1}]}'
out_trade_no_before=order_num('13631240700')
spIp_before='219.131.222.91'
NOTIFY_URL_before='https://www.zhgaft.top:7029/'


@app.route('/',methods=['GET','POST'])
def hallo():
    return 'Hallo!!'

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST': #如果请求方法时GET,返回login.html模板页面
        dict1 = {'appid': APP_ID, 'mch_id': MCH_ID, 'nonce_str': ramdom8_before, 'body': 'body',
                 'detail': detail_before, 'device_info': '013467007045764',
                 'out_trade_no': out_trade_no_before, 'total_fee': '666', 'spbill_create_ip': spIp_before,
                 'notify_url': NOTIFY_URL_before, 'trade_type': 'MWEB'}

        Sign = wzhifuSDK.get_sign(dict1, API_KEY)

        dict2 = {'appid': APP_ID, 'mch_id': MCH_ID, 'nonce_str': ramdom8_before, 'sign': Sign, 'body': '<![CDATA[body]]>',
                 'detail': detail_before, 'device_info': '013467007045764',
                 'out_trade_no': out_trade_no_before, 'total_fee': '666', 'spbill_create_ip': spIp_before, 'notify_url': NOTIFY_URL_before,
                 'trade_type': 'MWEB'}

        response = wzhifuSDK.wx_pay_unifiedorde(dict2, UFDODER_URL)
        print(response.decode())
        root=ET.fromstring(response.decode())
        returnUrl=root.find('mweb_url').text
        print(returnUrl)

        return jsonify(webUrl=returnUrl)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers','Content-Type,Authorization,session_id')
    response.headers.add('Access-Control-Allow-Headers', 'GET,PUT,POST,DELETE,OPTIONS,HEAD')
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=7000,debug=True)
