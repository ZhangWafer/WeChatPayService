from flask import Flask,render_template,request
import wzhifuSDK
from wzhifuSDK import order_num

app = Flask(__name__)

# 微信支付信息
APP_ID = "wx689b069eb440eed1"  # 你公众账号上的appid
MCH_ID = "1521585261"  # 你的商户号
API_KEY = "zh43be9fe2fd47a8171zhga21e123713"  # 微信商户平台(pay.weixin.qq.com) -->账户设置 -->API安全 -->密钥设置，设置完成后把密钥复制到这里
APP_SECRECT = "f82a881cd1a9da63c279120b0d167333"
UFDODER_URL = "https://api.mch.weixin.qq.com/pay/micropay"  # 该url是微信下单api

NOTIFY_URL = "http://www.baidu.com/"  # 微信支付结果回调接口，需要改为你的服务器上处理结果回调的方法路径
CREATE_IP = 'xxx'  # 你服务器的IP

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET': #如果请求方法时GET,返回login.html模板页面
        dict1 = {'appid': APP_ID, 'mchid': MCH_ID, 'nonce_str': wzhifuSDK.random_str(32), 'body': '午餐',
                 'detail': "{'cost_price': 608800,'receipt_id': 'wx123','goods_detail': '[{'goods_id': '商品编码','goods_name': '','quantity': 1,'price': 528800},{'goods_id': '商品编码','goods_name': 'iPhone6s 32G','quantity': 1,'price': 608800}]}'}",
                 'out_trade_no': order_num('13631240780'), 'total_fee': '888', 'spbill_create_ip': '192.168.117.70',
                 'notify_url': NOTIFY_URL, 'trade_type': 'JSAPI'}

        Sign = wzhifuSDK.get_sign(dict1, API_KEY)

        Sign = 'F63AEAD518AEC1FF685A8FA838F2ADB7'

        dict2 = {'appid': APP_ID, 'mchid': MCH_ID, 'nonce_str': wzhifuSDK.random_str(32), 'sign': Sign, 'body': '午餐',
                 'detail': "{'cost_price': 608800,'receipt_id': 'wx123','goods_detail': '[{'goods_id': '商品编码','goods_name': '','quantity': 1,'price': 528800},{'goods_id': '商品编码','goods_name': 'iPhone6s 32G','quantity': 1,'price': 608800}]}'}",
                 'out_trade_no': order_num('13631240780'), 'total_fee': '888', 'spbill_create_ip': '192.168.117.70',
                 'notify_url': NOTIFY_URL, 'trade_type': 'JSAPI'}

        response = wzhifuSDK.wx_pay_unifiedorde(dict2, UFDODER_URL)

        return request.values.get('username')+'1456461616'



if __name__ == '__main__':
    app.run(port=5000,debug=True)
