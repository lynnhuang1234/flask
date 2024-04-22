from flask import Flask, jsonify
import os

app = Flask(__name__)
data = [
  { 
"userid":"388223204",
"ride_id": '五五八四',
"cancel_status":1,
"pay_status":2,
"refund_status":-1,
"payment_channel":'待支付',
  },
  { 
"userid":"144145319",
"ride_id": '七一九六',
"cancel_status":1,
"pay_status":2,
"refund_status":-1,
"payment_channel":'待支付',
  },
  
  {
"userid":"193396841",
"ride_id": '三六一二',
"cancel_status":1,
"pay_status":1,
"refund_status":2,
"payment_channel":'支付宝',
  },
  {
"userid":"18289256",
"ride_id": '七四四二',
"cancel_status":1,
"pay_status":1,
"refund_status":2,
"payment_channel":'微信',
  },
      {
"userid":"19073022",
"ride_id": '三零五六',
"cancel_status":1,
"pay_status":1,
"refund_status":1,
"payment_channel":'微信',
  },
      {
"userid":"122071328",
"ride_id": '三零八四',
"cancel_status":1,
"pay_status":1,
"refund_status":1,
"payment_channel":'微信',
  },
  {
"userid":"377320321",
"ride_id":"六三八三",
"cancel_status":"-1",
"pay_status":"-1",
"refund_status":"-1",
"payment_channel":"微信",
"ride_status":"5",
"is_pay":"1",
"status":"-1",
"have_goods":"0",
"have_passenger_compensation":"1",
"compensation_account":"6",
"good_price":"",
  },
    {
"userid":"171090251",
"ride_id":"七六一四",
"cancel_status":"-1",
"pay_status":"-1",
"refund_status":"-1",
"payment_channel":"支付宝",
"ride_status":"5",
"is_pay":"1",
"status":"-1",
"have_goods":"0",
"have_passenger_compensation":"1",
"compensation_account":"6",
"good_price":"",
  },
      {
"userid":"316097900",
"ride_id":"七九二一",
"cancel_status":"-1",
"pay_status":"-1",
"refund_status":"-1",
"payment_channel":"支付宝",
"ride_status":"5",
"is_pay":"1",
"status":"1000",
"have_goods":"1",
"have_passenger_compensation":"1",
"compensation_account":"6",
"good_price":"12.9",
  },
      {
"userid":"216751796",
"ride_id":"一七五七",
"cancel_status":"-1",
"pay_status":"-1",
"refund_status":"-1",
"payment_channel":"支付宝",
"ride_status":"5",
"is_pay":"1",
"status":"1000",
"have_goods":"1",
"have_passenger_compensation":"1",
"compensation_account":"2.1",
"good_price":"3.9",
  },
      {
"userid":"48929454",
"ride_id":"八六五二",
"cancel_status":"-1",
"pay_status":"-1",
"refund_status":"-1",
"payment_channel":"支付宝",
"ride_status":"5",
"is_pay":"1",
"status":"1001",
"have_goods":"1",
"have_passenger_compensation":"1",
"compensation_account":"6",
"good_price":"5.9",
  },
      {
"userid":"34660074",
"ride_id":"四八一七",
"cancel_status":"-1",
"pay_status":"-1",
"refund_status":"-1",
"payment_channel":"支付宝",
"ride_status":"5",
"is_pay":"1",
"status":"1002",
"have_goods":"1",
"have_passenger_compensation":"0",
"compensation_account":"-1",
"good_price":"7.9",
  },
      {
"userid":"242423379",
"ride_id":"八八三四",
"cancel_status":"-1",
"pay_status":"-1",
"refund_status":"-1",
"payment_channel":"支付宝",
"ride_status":"5",
"is_pay":"1",
"status":"1001",
"have_goods":"1",
"have_passenger_compensation":"0",
"compensation_account":"-1",
"good_price":"2.9",
  },
      {
"userid":"238893885",
"ride_id":"二四一二",
"cancel_status":"-1",
"pay_status":"-1",
"refund_status":"-1",
"payment_channel":"支付宝",
"ride_status":"5",
"is_pay":"1",
"status":"1001",
"have_goods":"1",
"have_passenger_compensation":"0",
"compensation_account":"-1",
"good_price":"10.9",
  },
  {
"userid":"22742643",
"fromtitle":"顺风车车主",
  },
  {
"userid":"41875212",
"fromtitle":"顺风车车主",
  },
      {
"userid":"98629842",
"fromtitle":"顺风车车主",
  },
      {
"userid":"98629844",
"fromtitle":"顺风车车主",
  },
      {
"userid":"98629845",
"fromtitle":"顺风车车主",
  },
      {
"userid":"98629846",
"fromtitle":"顺风车车主",
  },
      {
"userid":"98629847",
"fromtitle":"顺风车车主",
  },
          {
"userid":"98629848",
"fromtitle":"顺风车车主",
  },
          {
"userid":"98629849",
"fromtitle":"顺风车车主",
  },
          {
"userid":"98629850",
"fromtitle":"顺风车车主",
  },
          {
"userid":"98629851",
"fromtitle":"顺风车车主",
  },
          {
"userid":"98629852",
"fromtitle":"顺风车车主",
  },
              {
"userid":"98629853",
"fromtitle":"顺风车车主",
  },
              {
"userid":"98629854",
"fromtitle":"顺风车车主",
  },
              {
"userid":"98629855",
"fromtitle":"顺风车车主",
  },
              {
"userid":"98629856",
"fromtitle":"顺风车车主",
  },
              {
"userid":"98629857",
"fromtitle":"顺风车车主",
  },
                  {
"userid":"98629858",
"fromtitle":"顺风车车主",
  },
                  {
"userid":"98629859",
"fromtitle":"顺风车车主",
  },
                      {
"userid":"68716181",
"fromtitle":"顺风车乘客",
  },
                          {
"userid":"57730772",
"fromtitle":"顺风车乘客",
  },
                          {
"userid":"53601931",
"fromtitle":"顺风车乘客",
  },
                          {
"userid":"49473090",
"fromtitle":"顺风车乘客",
  },
                          {
"userid":"45344249",
"fromtitle":"顺风车乘客",
  },
                          {
"userid":"41215408",
"fromtitle":"顺风车乘客",
  },
                          {
"userid":"37086567",
"fromtitle":"顺风车乘客",
  },
                          {
"userid":"32957726",
"fromtitle":"顺风车乘客",
  },
                      {
"userid":"28828885",
"fromtitle":"顺风车乘客",
  },
                          {
"userid":"24700044",
"fromtitle":"顺风车乘客",
  },
                          {
"userid":"20571203",
"fromtitle":"顺风车乘客",
  },
  {
"userid": "22742643",
"ride_id": "二六四三",
"fromtitle": "顺风车车主"
},
{
"userid": "41875212",
"ride_id": "五二一二",
"fromtitle": "顺风车车主"
},
{
"userid": "98629842",
"ride_id": "九八四二",
"fromtitle": "顺风车车主"
},
{
"userid": "98629844",
"ride_id": "九八四四",
"fromtitle": "顺风车车主"
},
{
"userid": "98629845",
"ride_id": "九八四五",
"fromtitle": "顺风车车主"
},
{
"userid": "98629846",
"ride_id": "九八四六",
"fromtitle": "顺风车车主"
},
{
"userid": "98629847",
"ride_id": "九八四七",
"fromtitle": "顺风车车主"
},
{
"userid": "98629848",
"ride_id": "九八四八",
"fromtitle": "顺风车车主"
},
{
"userid": "98629849",
"ride_id": "九八四九",
"fromtitle": "顺风车车主"
},


{
"userid": "98629850",
"ride_id": "九八五十",
"fromtitle": "顺风车车主"
},
{
"userid": "98629851",
"ride_id": "九八五一",
"fromtitle": "顺风车车主"
},
{
"userid": "98629852",
"ride_id": "九八五二",
"fromtitle": "顺风车车主"
},
{
"userid": "98629853",
"ride_id": "九八五三",
"fromtitle": "顺风车车主"
},
{
"userid": "98629854",
"ride_id": "九八五四",
"fromtitle": "顺风车车主"
},
{
"userid": "98629855",
"ride_id": "九八五五",
"fromtitle": "顺风车车主"
},
{
"userid": "98629856",
"ride_id": "九八五六",
"fromtitle": "顺风车车主"
},
{
"userid": "98629857",
"ride_id": "九八五七",
"fromtitle": "顺风车车主"
},
{
"userid": "98629858",
"ride_id": "九八五八",
"fromtitle": "顺风车车主"
},
{
"userid": "98629859",
"ride_id": "九八五九",
"fromtitle": "顺风车车主"
},
{
"userid": "68716181",
"ride_id": "六一八一",
"fromtitle": "顺风车乘客"
},
{
"userid": "57730772",
"ride_id": "零七七二",
"fromtitle": "顺风车乘客"
},
{
"userid": "53601931",
"ride_id": "一九三一",
"fromtitle": "顺风车乘客"
},
{
"userid": "49473090",
"ride_id": "三零九零",
"fromtitle": "顺风车乘客"
},
{
"userid": "45344249",
"ride_id": "四二四九",
"fromtitle": "顺风车乘客"
},
{
"userid": "41215408",
"ride_id": "五四零八",
"fromtitle": "顺风车乘客"
},
{
"userid": "37086567",
"ride_id": "六五六七",
"fromtitle": "顺风车乘客"
},
{
"userid": "32957726",
"ride_id": "七七二六",
"fromtitle": "顺风车乘客"
},
{
"userid": "28828885",
"ride_id": "八八八五",
"fromtitle": "顺风车乘客"
},
{
"userid": "24700044",
"ride_id": "零零四四",
"fromtitle": "顺风车乘客"
},
{
"userid": "20571203",
"ride_id": "一二零三",
"fromtitle": "顺风车乘客"
},
{
    'user_id': 232431465, 
  'is_responsible': 1, 
  'feedback_status': 0, 
  'activity_rate': '-1', 
  'rideid': 1490130331397783810, 
  'ride_id': '三八一零'
  }, 
  {
    'user_id': 367478331, 
  'is_responsible': 1, 
  'feedback_status': 0, 
  'activity_rate': '-1', 
  'rideid': 1484775384762286347, 
  'ride_id': '六三四七'
  }, 
  {
    'user_id': 148082541, 
  'is_responsible': 0, 
  'feedback_status': 1, 
  'activity_rate': '-1', 
  'rideid': 1486441643228791311, 
  'ride_id': '一三一一'
  }, 
  {
    'user_id': 265858710, 
  'is_responsible': 0, 
  'feedback_status': 1, 
  'activity_rate': '-1', 
  'rideid': 1492046798217282063, 
  'ride_id': '二零六三'
  }, 
  {
    'user_id': 121379317, 
    'is_responsible': 1, 
    'feedback_status': 0, 
    'activity_rate': '-1', 
    'rideid': 1491728694081749517, 
    'ride_id': '九五一七'
    }, 
    {
      'user_id': 149921558, 
      'is_responsible': 0, 
      'feedback_status': 1, 
      'activity_rate': '-1', 
      'rideid': 1492061012881309697, 
      'ride_id': '九六九七'
      }, 
      {
        'user_id': 300581173, 
        'is_responsible': 1, 
        'feedback_status': 0, 
        'activity_rate': '-1', 
        'rideid': 1483428808898904076, 
        'ride_id': '四零七六'
        }, 
        {
          'user_id': 384390182, 
          'is_responsible': 1, 
          'feedback_status': 0, 
          'activity_rate': '-1', 
          'rideid': 1491361457198072591, 
          'ride_id': '二五九一'
          }, 
          {
            'user_id': 394731332, 
            'is_responsible': 1, 
            'feedback_status': 0, 
            'activity_rate': '-1', 
            'rideid': 1492076818629394433, 
            'ride_id': '四四三三'
            }, 
            {
              'user_id': 20889299, 
              'is_responsible': 0, 
              'feedback_status': 1, 
              'activity_rate': '-1', 
              'rideid': 1492190635128521218, 
              'ride_id': '一二一八'
              }, 
              {
                'user_id': 40521235, 
                'is_responsible': 1, 
                'feedback_status': 0, 
                'activity_rate': '-1', 
                'rideid': 1484133587866353922, 
                'ride_id': '三九二二'
                }, 
                {
                  'user_id': 47691683, 
                  'is_responsible': 1, 
                  'feedback_status': 0, 
                  'activity_rate': '-1', 
                  'rideid': 1486376460456296460, 
                  'ride_id': '六四六零'
                  }, 
                  {
                    'user_id': 350097783, 
                    'is_responsible': 1, 
                    'feedback_status': 0, 
                    'activity_rate': '-1', 
                    'rideid': 1490544228806164992, 
                    'ride_id': '四九九二'
                    }, 
                    {
                      'user_id': 143208643, 
                      'is_responsible': 1, 
                      'feedback_status': 0, 
                      'activity_rate': '-1', 
                      'rideid': 1492224439675258368, 
                      'ride_id': '八三六八'
                      }, 
                      {
                        'user_id': 132862620, 
                        'is_responsible': 1, 
                        'feedback_status': 0, 
                        'activity_rate': '-1', 
                        'rideid': 1490794960943841793, 
                        'ride_id': '一七九三'
                        }, 
                        {
                          'user_id': 17715008, 
                          'is_responsible': 1, 
                          'feedback_status': 0, 
                          'activity_rate': '-1', 
                          'rideid': 1489541069937836558, 
                          'ride_id': '六五五八'
                          }, 
                          {
                            'user_id': 51865013, 
                            'is_responsible': 1, 
                            'feedback_status': 0, 
                            'activity_rate': '-1', 
                            'rideid': 1492079810543878157, 
                            'ride_id': '八一五七'
                            }, 
                            {
                              'user_id': 367180191, 
                            'is_responsible': 1, 
                            'feedback_status': 0, 
                            'activity_rate': '-1', 
                            'rideid': 1492260050524176642, 
                            'ride_id': '六六四二'
                            }, 
                            {
                              'user_id': 33917253, 
                              'is_responsible': 1, 
                              'feedback_status': 0, 
                              'activity_rate': '-1', 
                              'rideid': 1486886101409857551, 
                              'ride_id': '七五五一'}, {'user_id': 126372699, 'is_responsible': 1, 'feedback_status': 0, 'activity_rate': '-1', 'rideid': 1492087169903232013, 'ride_id': '二零一三'}, {'user_id': 203780524, 'is_responsible': 1, 'feedback_status': 0, 'activity_rate': '-1', 'rideid': 1492190285692666626, 'ride_id': '六六二六'}, {'user_id': 167622449, 'is_responsible': 1, 'feedback_status': 0, 'activity_rate': '-1', 'rideid': 1491643218930958348, 'ride_id': '八三四八'}, {'user_id': 8299010, 'is_responsible': 1, 'feedback_status': 0, 'activity_rate': '-1', 'rideid': 1492294617830261518, 'ride_id': '一五一八'}, {'user_id': 142559250, 'is_responsible': 1, 'feedback_status': 0, 'activity_rate': '-1', 'rideid': 1492293430741566976, 'ride_id': '六九七六'}, {'user_id': 377497068, 'is_responsible': 1, 'feedback_status': 0, 'activity_rate': '-1', 'rideid': 1492133332815708929, 'ride_id': '八九二九'}, {'user_id': 343220084, 'is_responsible': 0, 'feedback_status': 0, 'activity_rate': 1.0, 'rideid': 1492308121207439631, 'ride_id': '九六三一'}, {'user_id': 207799703, 'is_responsible': 1, 'feedback_status': 0, 'activity_rate': '-1', 'rideid': 1492220021898740224, 'ride_id': '零二二四'}, {'user_id': 154838415, 'is_responsible': 1, 'feedback_status': 0, 'activity_rate': '-1', 'rideid': 1492254751943819265, 'ride_id': '九二六五'}, {'user_id': 394824853, 'is_responsible': 0, 'feedback_status': 1, 'activity_rate': '-1', 'rideid': 1492298002868470799, 'ride_id': '零七九九'}, {'user_id': 373793956, 'is_responsible': 0, 'feedback_status': 0, 'activity_rate': 1.0, 'rideid': 1492275581058810894, 'ride_id': '零八九四'}, {'user_id': 350016323, 'is_responsible': 1, 'feedback_status': 0, 'activity_rate': '-1', 'rideid': 1492325731177333259, 'ride_id': '三二五九'}, {'user_id': 358006382, 'is_responsible': 0, 'feedback_status': 0, 'activity_rate': 1.0, 'rideid': 1492316170580132875, 'ride_id': '二八七五'}, {'user_id': 259741409, 'is_responsible': 1, 'feedback_status': 0, 'activity_rate': '-1', 'rideid': 1492144567443521547, 'ride_id': '一五四七'}, {'user_id': 149474699, 'is_responsible': 1, 'feedback_status': 0, 'activity_rate': '-1', 'rideid': 1491756629354348545, 'ride_id': '八五四五'}, {'user_id': 31574599, 'is_responsible': 1, 'feedback_status': 0, 'activity_rate': '-1', 'rideid': 1485043081551020289, 'ride_id': '零二八九'}, {'user_id': 337488005, 'is_responsible': 1, 'feedback_status': 0, 'activity_rate': '-1', 'rideid': 1486415639349297421, 'ride_id': '七四二一'}, {'user_id': 150057146, 'is_responsible': 0, 'feedback_status': 0, 'activity_rate': 1.0, 'rideid': 1492349256726480397, 'ride_id': '零三九七'}, {'user_id': 366743995, 'is_responsible': 0, 'feedback_status': 0, 'activity_rate': 0.0, 'rideid': 1492140008268627983, 'ride_id': '七九八三'}, {'user_id': 21111606, 'is_responsible': 1, 'feedback_status': 0, 'activity_rate': '-1', 'rideid': 1492354094201832204, 'ride_id': '二二零四'}, {'user_id': 326441335, 'is_responsible': 1, 'feedback_status': 0, 'activity_rate': '-1', 'rideid': 1492184725589065730, 'ride_id': '五七三零'}

]

@app.route('/<ride_id>', methods = ['GET'])
def index(ride_id:str):
    for d in data:
        if 'ride_id' in d and d['ride_id'] == ride_id:
            return jsonify(d)

    return jsonify({ 'error': 'Employee does not exist.' }), 404


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
