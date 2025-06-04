from flask import Flask, request, abort

from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage,
    FlexMessage,
    FlexContainer,
    QuickReply,
    QuickReplyItem,
    MessageAction
    
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent,
)
import json
import os

app = Flask(__name__)

configuration = Configuration(access_token=os.getenv('CHANNEL_ACCESS_TOKEN'))
line_handler = WebhookHandler(os.getenv('CHANNEL_SECRET'))#更改

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        line_handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

#訊息事件
@line_handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    text = event.message.text.lower()#新增的

    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        
    
        if '活動'in text:
            line_flex_json={
                "type": "carousel",
                "contents": [
                    {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://www.niusnews.com/upload/posts/posts_image3_82019_1567389429.jpg",
                        "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "cover"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "期末系週會",
                            "weight": "bold",
                            "size": "xl"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "text",
                                "text": "轉眼間就來到學期的尾聲惹"
                            },
                            {
                                "type": "text",
                                "text": "講到學期末，就會想到我們的期末系週會啦～ 這次我們也會提供飲料給大家喔",
                                "wrap": True,
                                "margin": "md"
                            },
                            {
                                "type": "separator",
                                "margin": "lg",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "margin": "lg",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "時間",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 3
                                },
                                {
                                    "type": "text",
                                    "text": "6/4（三）14:30-15:10",
                                    "wrap": True,
                                    "color": "#666666",
                                    "size": "sm",
                                    "flex": 7
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "地點",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 3
                                },
                                {
                                    "type": "text",
                                    "text": "正心0211",
                                    "wrap": True,
                                    "color": "#666666",
                                    "size": "sm",
                                    "flex": 7
                                }
                                ]
                            }
                            ]
                        },
                        {
                            "type": "text",
                            "text": "※ 若想要喝飲料的同學記得要幫我填表單喔！！",
                            "margin": "xxl",
                            "color": "#66B3FF",
                            "wrap": True
                        }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "uri",
                            "label": "報名表單",
                            "uri": "https://docs.google.com/forms/d/e/1FAIpQLSd1ucUPdmLZcmCneOsudFU5CL2qs0WzMG3bdHWeBySqHzxQZQ/viewform?fbclid=PAQ0xDSwKnYitleHRuA2FlbQIxMQABp83NOWekqoGJ04DJyvGt_kdL1313PpaDImVBQ9rURxg5qmcsOB5kHY5mw_ta_aem_vD0z1fyFEarZunNdN-K7cA"
                            }
                        }
                        ],
                        "flex": 0
                    }
                    },
                    {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://imageproxy.pixnet.cc/imgproxy?url=https://pic.pimg.tw/redcloud2810/1622814320-111389135-g.jpg",
                        "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "cover"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "送舊晚會",
                            "weight": "bold",
                            "size": "xl"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "text",
                                "text": "「鐘聲響起 誰說離別是結局」"
                            },
                            {
                                "type": "text",
                                "text": "這學期的重頭戲活動要來啦！有小遊戲、獎品和精美餐點等著你，而且還可以和我們一起歡送學長姐呢！",
                                "wrap": True,
                                "margin": "md"
                            },
                            {
                                "type": "separator",
                                "margin": "md",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "margin": "lg",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "時間",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 3
                                },
                                {
                                    "type": "text",
                                    "text": "5/28（三）18:30-21:00",
                                    "wrap": True,
                                    "color": "#666666",
                                    "size": "sm",
                                    "flex": 7
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "spacing": "sm",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "入場時間",
                                        "color": "#aaaaaa",
                                        "size": "sm",
                                        "flex": 3
                                    },
                                    {
                                        "type": "text",
                                        "text": "18:00",
                                        "wrap": True,
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 7
                                    }
                                    ]
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "地點",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 3
                                },
                                {
                                    "type": "text",
                                    "text": "天圓地方-台中市東區復興路四段186號 11F儷影一廳（大魯閣新時代）",
                                    "wrap": True,
                                    "color": "#666666",
                                    "size": "sm",
                                    "flex": 7
                                }
                                ]
                            }
                            ]
                        },
                        {
                            "type": "text",
                            "text": "※ 有報名的同學記得要準時參與喔~",
                            "margin": "lg",
                            "color": "#66B3FF"
                        }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "uri",
                            "label": "地點",
                            "uri": "https://maps.app.goo.gl/bp9Exg2SwnEg7qwX6"
                            }
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "uri",
                            "label": "報名表單",
                            "uri": "https://docs.google.com/forms/d/e/1FAIpQLSePHpo3-UglZpYK74GpKxYUZ1fniEgABlBO2JKJqs2VbFUQYA/viewform"
                            }
                        }
                        ],
                        "flex": 0
                    }
                    }
                ]
            }
            line_flex_str=json.dumps(line_flex_json) #新增的               
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_str))]
                )
            )

        if text == '我想認識醫資系':
            quickReply = QuickReply(
                items=[
                    QuickReplyItem(
                        action=MessageAction(
                            label="師資",
                            text="師資陣容"
                            
                        ), 
                    ),
                    QuickReplyItem(
                        action=MessageAction(
                            label="系秘",
                            text="醫資系系秘"
                        ),  
                    ),
                    QuickReplyItem(
                        action=MessageAction(
                            label="畢業門檻",
                            text="畢業門檻"
                        ), 
                    )
                ]
            )
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(
                        text='想了解以下哪方面的內容呢~',
                        quick_reply=quickReply
                    )]
                )
            )

        if '繳費'in text:
            message = TextMessage(
                text="繳費連結如下:\nhttps://ebill.chb.com.tw/eBill/cs/student_logi\n\n登入後選擇繳費方式,進行繳費即可。詳情請校網查詢。\nhttps://account.csmu.edu.tw/var/file/2/1002/img/972/352583426.pdf"
            )
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[message]
                )
            )



        if text == '我想了解課程資訊':
            quickReply = QuickReply(
                items=[
                    QuickReplyItem(
                        action=MessageAction(
                            label="大一上",
                            text="大一上的課程"
                            
                        ), 
                    ),
                    QuickReplyItem(
                        action=MessageAction(
                            label="大一下",
                            text="大一下的課程"
                        ),  
                    ),
                ]
            )
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(
                        text='想了解大一哪個學期的課程呢',
                        quick_reply=quickReply
                    )]
                )
            )  

        if '大一上的課程'in text or '大一上課程'in text:
            quickReply = QuickReply(
                items=[
                    QuickReplyItem(
                        action=MessageAction(
                            label="全部",
                            text="查詢大一上全部課程"
                            
                        ), 
                    ),
                    QuickReplyItem(
                        action=MessageAction(
                            label="必修",
                            text="查詢大一上必修課程"
                        ),  
                    ),
                    QuickReplyItem(
                        action=MessageAction(
                            label="選修",
                            text="查詢大一上選修課程"
                        ),  
                    ),
                ]
            )
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(
                        text='請選擇你想查詢的課程類型：',
                        quick_reply=quickReply
                    )]
                )
            )  

        if '大一下的課程'in text or '大一上課程'in text:
            quickReply = QuickReply(
                items=[
                    QuickReplyItem(
                        action=MessageAction(
                            label="全部",
                            text="查詢大一下全部課程"
                            
                        ), 
                    ),
                    QuickReplyItem(
                        action=MessageAction(
                            label="必修",
                            text="查詢大一下必修課程"
                        ),  
                    ),
                    QuickReplyItem(
                        action=MessageAction(
                            label="選修",
                            text="查詢大一下選修課程"
                        ),  
                    ),
                ]
            )
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(
                        text='請選擇你想查詢的課程類型：',
                        quick_reply=quickReply
                    )]
                )
            ) 



        if '慶祥' in text and '實驗室' in text or '賴慶祥老師的lab'in text:
            line_flex_json={
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "賴慶祥 老師",
                        "size": "xl",
                        "weight": "bold",
                        "margin": "md"
                    },
                    {
                        "type": "text",
                        "text": "實驗室資訊",
                        "color": "#1DB446",
                        "margin": "none"
                    },
                    {
                        "type": "separator",
                        "color": "#888888",
                        "margin": "md"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                            },
                            {
                                "type": "text",
                                "text": "實驗室研究主題與方向",
                                "weight": "bold",
                                "margin": "sm",
                                "flex": 0
                            }
                            ]
                        },
                        {
                            "type": "text",
                            "text": "1.研究主題主要以統計資料分析(機率) 為主，建議對老師實驗室內容感興趣的學生再進來。 ",
                            "wrap": True
                        },
                        {
                            "type": "text",
                            "text": "2.實驗室的主要活動是專題研究。想要升學的會鼓勵撰寫論文、參與研討會等活動。",
                            "wrap": True
                        },
                        {
                            "type": "separator",
                            "color": "#888888"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                                },
                                {
                                    "type": "text",
                                    "text": "實驗室已發表的專題或計畫",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "flex": 0
                                }
                                ]
                            },
                            {
                                "type": "text",
                                "text": "1.中風病人復健研究：",
                                "wrap": True,
                                "color": "#008888"
                            },
                            {
                                "type": "text",
                                "text": " 與醫院睡眠中心及復健科醫師合作，分析中風病人在復健期間的進步情況（使用巴氏量表評估），比較有無使用呼吸器對復原的影響。",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "2.輪班司機健康狀況研究：",
                                "wrap": True,
                                "color": "#008888"
                            },
                            {
                                "type": "text",
                                "text": "比較有輪班（跑夜車）與無輪班（台鐵司機）的司機，他們的體檢及生理指標差異。研究發現輪班者的健康狀況普遍較差。",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "※ 詳細內容可自行尋找或詢問老師",
                                "color": "#46A3FF",
                                "margin": "xl"
                            },
                            {
                                "type": "separator",
                                "color": "#888888",
                                "margin": "xl"
                            }
                            ]
                        }
                        ],
                        "spacing": "sm"
                    },
                    
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                                },
                                {
                                    "type": "text",
                                    "text": "實驗室其他細項",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "flex": 0
                                }
                                ]
                            },
                            {
                                "type": "text",
                                "text": "1.彈性出入制度：",
                                "wrap": True,
                                "color": "#008888"
                            },
                            {
                                "type": "text",
                                "text": "實驗室沒有嚴格的出勤規定，學生可依個人時間安排彈性進出。",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "2.討論時間須守信：",
                                "color": "#008888"
                            },
                            {
                                "type": "text",
                                "text": "若有與老師約定討論進度，無論是否已有明確成果，都應如期出席。臨時取消或無故缺席將影響彼此信任與後續指導安排。",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "3.溝通需主動誠實：",
                                "color": "#008888"
                            },
                            {
                                "type": "text",
                                "text": "遇到困難或進度落後時，應主動並如實向老師反映，避免逃避或隱瞞情況，以維持良好的溝通與指導品質。",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "4.會議頻率：",
                                "color": "#008888"
                            },
                            {
                                "type": "text",
                                "text": "實驗室開會時間不固定，通常每兩週一次，主要用於學生進度報告與問題討論。",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "5.問題協助來源：",
                                "color": "#008888"
                            },
                            {
                                "type": "text",
                                "text": "若研究主題或方法與學長姐相近，學生可先尋求學長姐協助；若主題較獨特或問題較難，則會直接由老師協助解決。",
                                "wrap": True
                            },
                            {
                                "type": "separator",
                                "color": "#888888"
                            }
                            ]
                        }
                        ]
                    },

                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                                },
                                {
                                    "type": "text",
                                    "text": "進老師實驗室須具備的能力",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "flex": 0
                                }
                                ]
                            },
                            {
                                "type": "text",
                                "text": "什麼都不會也沒關係，若還不會可重頭開始學習！",
                                "wrap": True
                            },
                            {
                                "type": "separator",
                                "color": "#888888"
                            }
                            ]
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                                },
                                {
                                    "type": "text",
                                    "text": "老師對於大一大二生提早進入實驗室的看法",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "wrap": True
                                }
                                ]
                            },
                            {
                                "type": "text",
                                "text": "越早越好！學生才有機會了解老師的研究方向，如果不適合也可以盡快換老師。",
                                "wrap": True
                            }
                            ]
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "color": "#00AAAA",
                        "margin": "xxl",
                        "action": {
                        "type": "uri",
                        "label": "老師相關資訊",
                        "uri": "https://mi.csmu.edu.tw/p/405-1033-66036,c89.php?Lang=zh-tw"
                        }
                    }
                    ]
                }
                
            }

            line_flex_str=json.dumps(line_flex_json) #新增的               
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_str))]
                )
            )
 
        if '麗蘋' in text and '實驗室' in text or '徐麗蘋老師的lab'in text:
            line_flex_json={
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "徐麗蘋 老師",
                        "size": "xl",
                        "weight": "bold",
                        "margin": "md"
                    },
                    {
                        "type": "text",
                        "text": "實驗室資訊",
                        "color": "#1DB446",
                        "margin": "none"
                    },
                    {
                        "type": "separator",
                        "color": "#888888",
                        "margin": "md"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                            },
                            {
                                "type": "text",
                                "text": "實驗室研究主題與方向",
                                "weight": "bold",
                                "margin": "sm",
                                "flex": 0
                            }
                            ]
                        },
                        {
                            "type": "text",
                            "text": "1.研究主軸以影像處理與辨識為核心，特別著重於醫療影像相關應用。",
                            "wrap": True
                        },
                        {
                            "type": "text",
                            "text": "2.老師鼓勵學生提出有興趣的研究題目，若該主題超出老師的專業領域，也會主動協助推薦適合的其他指導老師。",
                            "wrap": True,
                            "margin": "md"
                        },
                        {
                            "type": "separator",
                            "color": "#888888"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                                },
                                {
                                    "type": "text",
                                    "text": "實驗室其他細項",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "flex": 0
                                }
                                ]
                            },
                            {
                                "type": "text",
                                "text": "1.固定每週進行會議",
                                "wrap": True,
                                "color": "#008888"
                            },
                            {
                                "type": "text",
                                "text": "討論進度與研究方向，並協助學生尋找並報告相關論文。若時間充裕，老師會鼓勵學生將成果投稿或參與研討會發表。",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "2.會議內容視研究階段調整：",
                                "color": "#008888"
                            },
                            {
                                "type": "text",
                                "text": "初期：以文獻探討為主，由老師協助帶領閱讀與理解論文。  中後期：逐步推進研究、數據分析與論文撰寫。",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "3.實驗室空間為共用：",
                                "color": "#008888"
                            },
                            {
                                "type": "text",
                                "text": "與炎清老師共用同一實驗室空間，需配合其相關規範與要求。",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "4.問題協助來源：",
                                "color": "#008888"
                            },
                            {
                                "type": "text",
                                "text": "可向老師詢問研究與技術上的問題。目前實驗室學長姐皆已畢業，因此暫無學長姐可諮詢，學生需具備更高的自主學習能力。",
                                "wrap": True
                            },
                            {
                                "type": "separator",
                                "color": "#888888"
                            }
                            ]
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                                },
                                {
                                    "type": "text",
                                    "text": "進老師實驗室須具備的能力",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "flex": 0
                                }
                                ]
                            },
                            {
                                "type": "text",
                                "text": "1.建議先修課程：",
                                "wrap": True,
                                "color": "#008888"
                            },
                            {
                                "type": "text",
                                "text": "希望學生修過麗蘋老師的影像處理課程，具備影像分析的基本概念。",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "2.技術能力要求：",
                                "color": "#008888"
                            },
                            {
                                "type": "text",
                                "text": "需具備一定程度的程式設計（coding）能力，以利實作與研究推進。",
                                "wrap": True
                            },
                            {
                                "type": "separator",
                                "color": "#888888"
                            }
                            ]
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                                },
                                {
                                    "type": "text",
                                    "text": "老師對於大一大二生提早進入實驗室的看法",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "wrap": True
                                }
                                ]
                            },
                            {
                                "type": "text",
                                "text": "越早越好，大三下再找專題老師太慢了!!",
                                "wrap": True
                            }
                            ]
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "color": "#00AAAA",
                        "margin": "xxl",
                        "action": {
                        "type": "uri",
                        "label": "老師相關資訊",
                        "uri": "https://mi.csmu.edu.tw/p/405-1033-66041,c89.php?Lang=zh-tw"
                        }
                    }
                    ]
                }
            }
            line_flex_str=json.dumps(line_flex_json) #新增的               
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_str))]
                )
            )
            
        if '炎清' in text and '實驗室' in text or '張炎清老師的lab'in text:
            line_flex_json={
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "張炎清 老師",
                        "size": "xl",
                        "weight": "bold",
                        "margin": "md"
                    },
                    {
                        "type": "text",
                        "text": "實驗室資訊",
                        "color": "#1DB446",
                        "margin": "none"
                    },
                    {
                        "type": "separator",
                        "color": "#888888",
                        "margin": "md"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                            },
                            {
                                "type": "text",
                                "text": "實驗室研究主題與方向",
                                "weight": "bold",
                                "margin": "sm",
                                "flex": 0
                            }
                            ]
                        },
                        {
                            "type": "text",
                            "text": "1.本實驗室研究主題以深度學習與機器學習為核心",
                            "wrap": True
                        },
                        {
                            "type": "text",
                            "text": "2.加入實驗室後，學生將以自身感興趣的主題進行論文型研究，培養獨立思考與學術寫作能力。",
                            "wrap": True,
                            "margin": "md"
                        },
                        {
                            "type": "text",
                            "text": "3.老師採開放與支持的指導方式：若學生已有想法，老師會全力支持並提供資源。若尚未確定方向，老師也會協助提供初步建議與引導。",
                            "wrap": True,
                            "margin": "md"
                        },
                        {
                            "type": "separator",
                            "color": "#888888",
                            "margin": "md"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                                },
                                {
                                    "type": "text",
                                    "text": "實驗室已發表的專題與計畫",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "flex": 0
                                }
                                ]
                            },
                            {
                                "type": "text",
                                "text": "目前老師正在進行的研究主題之一是： 結合深度學習與密碼學技術，以提升資料處理與傳輸的安全性與效率。",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": " ※ 對此方向有興趣的同學，歡迎主動與炎清老師洽談，深入了解！",
                                "wrap": True,
                                "margin": "md"
                            },
                            {
                                "type": "separator",
                                "color": "#888888",
                                "margin": "md"
                            }
                            ]
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                                },
                                {
                                    "type": "text",
                                    "text": "實驗室其他細項",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "flex": 0
                                }
                                ]
                            },
                            {
                                "type": "text",
                                "text": "1.固定每週進行會議（中午時段）",
                                "wrap": True,
                                "color": "#008888"
                            },
                            {
                                "type": "text",
                                "text": "進行進度報告與交流。",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "2.會議內容彈性：",
                                "color": "#008888"
                            },
                            {
                                "type": "text",
                                "text": "以學生當前研究進展為主，有成果或想法便可於當週進行報告與討論。",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "3.遇到問題可透過 Email 或 LINE 聯繫老師",
                                "color": "#008888",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "也歡迎詢問學長姐，大家都很樂於協助。",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "4.學習資源來源：",
                                "color": "#008888"
                            },
                            {
                                "type": "text",
                                "text": "- 每週會議的報告與討論",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "- 可主動向老師請求參考資料、論文或研究工具",
                                "wrap": True
                            },
                            {
                                "type": "separator",
                                "color": "#888888",
                                "margin": "md"
                            }
                            ]
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                                },
                                {
                                    "type": "text",
                                    "text": "進老師實驗室須具備的能力",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "flex": 0
                                }
                                ]
                            },
                            {
                                "type": "text",
                                "text": "1.需要的不是專業，而是勇氣！",
                                "wrap": True,
                                "color": "#008888"
                            },
                            {
                                "type": "text",
                                "text": "只要你鼓起勇氣向老師表達想加入實驗室的意願，老師幾乎都會願意收。",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "2.沒有明確的門檻限制",
                                "color": "#008888"
                            },
                            {
                                "type": "text",
                                "text": "進實驗室前可以向已有經驗的同學諮詢，了解不同研究方向與實際情況。",
                                "wrap": True
                            },
                            {
                                "type": "separator",
                                "color": "#888888",
                                "margin": "md"
                            }
                            ]
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                                },
                                {
                                    "type": "text",
                                    "text": "老師對於大一大二生提早進入實驗室的看法",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "wrap": True
                                }
                                ]
                            },
                            {
                                "type": "text",
                                "text": "「越早進來越好！」 老師鼓勵學生在大一、大二就進入實驗室，不需等到修完所有基礎課程，只要有興趣、有想法或想嘗試，就勇敢提問、勇敢加入——問就對了！",
                                "wrap": True
                            }
                            ]
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "color": "#00AAAA",
                        "margin": "xxl",
                        "action": {
                        "type": "uri",
                        "label": "老師相關資訊",
                        "uri": "https://mi.csmu.edu.tw/p/405-1033-66038,c89.php?Lang=zh-tw"
                        }
                    }
                    ]
                }
            }
            line_flex_str=json.dumps(line_flex_json) #新增的               
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_str))]
                )
            )
        
        if '啟昌' in text and '實驗室' in text or '張啟昌老師的lab'in text:
            line_flex_json={
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "張啟昌 老師",
                        "size": "xl",
                        "weight": "bold",
                        "margin": "md"
                    },
                    {
                        "type": "text",
                        "text": "實驗室資訊",
                        "color": "#1DB446",
                        "margin": "none"
                    },
                    {
                        "type": "separator",
                        "color": "#888888",
                        "margin": "md"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                            },
                            {
                                "type": "text",
                                "text": "實驗室研究主題與方向",
                                "weight": "bold",
                                "margin": "sm",
                                "flex": 0
                            }
                            ]
                        },
                        {
                            "type": "text",
                            "text": "1.醫療行為的動態分析\n2.癌症復發因子的預測\n3.發展臨床預後指標與醫療科技評估\n4.健康資訊服務創新與管理\n5.醫療決策行為的動態分析\n6.統計和結構方程模式\n7.資料包絡分析法\n8.醫療服務品質模式\n9.環境與生理訊號\n10.睡眠與健康",
                            "wrap": True
                        },
                        {
                            "type": "separator",
                            "color": "#888888",
                            "margin": "md"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                                },
                                {
                                    "type": "text",
                                    "text": "實驗室已發表的專題與計畫",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "flex": 0
                                }
                                ]
                            },
                            {
                                "type": "text",
                                "text": "目前已有學長姊的論文可至碩博士論文網找來看看",
                                "wrap": True
                            },
                            {
                                "type": "separator",
                                "color": "#888888",
                                "margin": "md"
                            }
                            ]
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                                },
                                {
                                    "type": "text",
                                    "text": "實驗室其他細項與規定",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "flex": 0
                                }
                                ]
                            },
                            {
                                "type": "text",
                                "text": "由於老師並未參與訪談，請親自詢問老師或學長姐喔!",
                                "wrap": True
                            },
                            {
                                "type": "separator",
                                "color": "#888888",
                                "margin": "md"
                            }
                            ]
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                                },
                                {
                                    "type": "text",
                                    "text": "進老師實驗室須具備的能力",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "flex": 0
                                }
                                ]
                            },
                            {
                                "type": "text",
                                "text": "由於老師並未參與訪談，請親自詢問老師喔!",
                                "wrap": True
                            },
                            {
                                "type": "separator",
                                "color": "#888888",
                                "margin": "md"
                            }
                            ]
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                                },
                                {
                                    "type": "text",
                                    "text": "老師對於大一大二生提早進入實驗室的看法",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "wrap": True
                                }
                                ]
                            },
                            {
                                "type": "text",
                                "text": "由於老師並未參與訪談，請親自詢問老師哦!",
                                "wrap": True
                            }
                            ]
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "color": "#00AAAA",
                        "margin": "xxl",
                        "action": {
                        "type": "uri",
                        "label": "老師相關資訊",
                        "uri": "https://mi.csmu.edu.tw/p/405-1033-66039,c89.php?Lang=zh-tw"
                        }
                    }
                    ]
                }
            }
            line_flex_str=json.dumps(line_flex_json) #新增的               
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_str))]
                )
            )
       
        if '孝屏' in text and '實驗室' in text or '李孝屏老師的lab'in text:
            line_flex_json={
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "李孝屏 老師",
                        "size": "xl",
                        "weight": "bold",
                        "margin": "md"
                    },
                    {
                        "type": "text",
                        "text": "實驗室資訊",
                        "color": "#1DB446",
                        "margin": "none"
                    },
                    {
                        "type": "separator",
                        "color": "#888888",
                        "margin": "md"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                            },
                            {
                                "type": "text",
                                "text": "實驗室研究主題與方向",
                                "weight": "bold",
                                "margin": "sm",
                                "flex": 0
                            }
                            ]
                        },
                        {
                            "type": "text",
                            "text": "1.行動裝置系統開發\n2.網路應用\n3.身心障礙輔助科技\n4.智慧生活應用\n5.雲端計算\n6.功能性遊戲",
                            "wrap": True
                        },
                        {
                            "type": "separator",
                            "color": "#888888",
                            "margin": "md"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                                },
                                {
                                    "type": "text",
                                    "text": "實驗室已發表的專題與計畫",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "flex": 0
                                }
                                ]
                            },
                            {
                                "type": "text",
                                "text": "目前已有學長姊的論文可至碩博士論文網找來看看",
                                "wrap": True
                            },
                            {
                                "type": "separator",
                                "color": "#888888",
                                "margin": "md"
                            }
                            ]
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                                },
                                {
                                    "type": "text",
                                    "text": "實驗室其他細項與規定",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "flex": 0
                                }
                                ]
                            },
                            {
                                "type": "text",
                                "text": "由於老師並未參與訪談，請親自詢問老師或學長姐喔!",
                                "wrap": True
                            },
                            {
                                "type": "separator",
                                "color": "#888888",
                                "margin": "md"
                            }
                            ]
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                                },
                                {
                                    "type": "text",
                                    "text": "進老師實驗室須具備的能力",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "flex": 0
                                }
                                ]
                            },
                            {
                                "type": "text",
                                "text": "由於老師並未參與訪談，請親自詢問老師喔!",
                                "wrap": True
                            },
                            {
                                "type": "separator",
                                "color": "#888888",
                                "margin": "md"
                            }
                            ]
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                                },
                                {
                                    "type": "text",
                                    "text": "老師對於大一大二生提早進入實驗室的看法",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "wrap": True
                                }
                                ]
                            },
                            {
                                "type": "text",
                                "text": "由於老師並未參與訪談，請親自詢問老師哦!",
                                "wrap": True
                            }
                            ]
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "color": "#00AAAA",
                        "margin": "xxl",
                        "action": {
                        "type": "uri",
                        "label": "老師相關資訊",
                        "uri": "https://mi.csmu.edu.tw/p/405-1033-66042,c89.php?Lang=zh-tw"
                        }
                    }
                    ]
                }
            }
            line_flex_str=json.dumps(line_flex_json) #新增的               
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_str))]
                )
            )

        if '虹名' in text and '實驗室' in text or '紀虹名老師的lab'in text:
            line_flex_json={
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "紀虹名 老師",
                        "size": "xl",
                        "weight": "bold",
                        "margin": "md"
                    },
                    {
                        "type": "text",
                        "text": "實驗室資訊",
                        "color": "#1DB446",
                        "margin": "none"
                    },
                    {
                        "type": "separator",
                        "color": "#888888",
                        "margin": "md"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                            },
                            {
                                "type": "text",
                                "text": "實驗室研究主題與方向",
                                "weight": "bold",
                                "margin": "sm",
                                "flex": 0
                            }
                            ]
                        },
                        {
                            "type": "text",
                            "text": "1.研究主題以問卷資料分析與生醫訊號處理為主，並結合機器學習模型進行應用與探討。",
                            "wrap": True
                        },
                        {
                            "type": "text",
                            "text": "2.會建議學生選擇自身感興趣且老師能提供輔助資源的研究方向，讓研究過程更具效率與成就感。",
                            "wrap": True,
                            "margin": "md"
                        },
                        {
                            "type": "separator",
                            "color": "#888888",
                            "margin": "md"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                                },
                                {
                                    "type": "text",
                                    "text": "實驗室已發表的專題與計畫",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "flex": 0
                                }
                                ]
                            },
                            {
                                "type": "text",
                                "text": "社群媒體使用者行為分析：",
                                "wrap": True,
                                "color": "#008888"
                            },
                            {
                                "type": "text",
                                "text": "透過問卷生成模型，合成社群媒體使用者資料，進一步分析問題使用者的行為模式與情緒特徵。",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": " ※ 詳細資訊歡迎主動與老師洽談，深入了解！",
                                "wrap": True,
                                "margin": "md"
                            },
                            {
                                "type": "separator",
                                "color": "#888888",
                                "margin": "md"
                            }
                            ]
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                                },
                                {
                                    "type": "text",
                                    "text": "實驗室其他細項與規定",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "flex": 0
                                }
                                ]
                            },
                            {
                                "type": "text",
                                "text": "1.固定每週進行會議",
                                "wrap": True,
                                "color": "#008888"
                            },
                            {
                                "type": "text",
                                "text": "- 閱讀指定論文",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "- 製作投影片並上台報告"
                            },
                            {
                                "type": "text",
                                "text": "- 反思與分享從論文中學到的內容與尚未理解的地方",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "2.每週準時繳交報告投影片",
                                "color": "#008888"
                            },
                            {
                                "type": "text",
                                "text": "若無法出席，請提前向老師請假。",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "3.遇到問題可聯繫老師",
                                "color": "#008888",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "由於研究方向多元，學長姐與學弟妹之間的主題較少重疊，上下屆互動較少。",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "4.若學生有想研究的主題，歡迎主動提出構想，老師會盡力協助提供相關資料與指導資源。",
                                "wrap": True
                            },
                            {
                                "type": "separator",
                                "color": "#888888"
                            }
                            ]
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                                },
                                {
                                    "type": "text",
                                    "text": "進老師實驗室須具備的能力",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "flex": 0
                                }
                                ]
                            },
                            {
                                "type": "text",
                                "text": "1.具備基礎程式設計能力",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "2.邏輯思考能力與解決問題的習慣",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "3.能吃苦耐勞，主動學習"
                            },
                            {
                                "type": "text",
                                "text": "4.進實驗室前需與老師進行面談，了解彼此期待與研究方向是否契合。",
                                "wrap": True
                            },
                            {
                                "type": "separator",
                                "color": "#888888",
                                "margin": "md"
                            }
                            ]
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                                },
                                {
                                    "type": "text",
                                    "text": "老師對於大一大二生提早進入實驗室的看法",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "wrap": True
                                }
                                ]
                            },
                            {
                                "type": "text",
                                "text": "「只要有心，任何時候都可以開始做研究！」",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "- 對未來有意升學的學生而言，提早進入實驗室有助於建立研究經驗與方向感。",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "- 歡迎還未加入實驗室的同學以「旁聽」方式參與，與老師討論是否適合加入實驗室，提前規劃未來學術路徑。",
                                "wrap": True
                            }
                            ]
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "color": "#00AAAA",
                        "margin": "xxl",
                        "action": {
                        "type": "uri",
                        "label": "老師相關資訊",
                        "uri": "https://mi.csmu.edu.tw/p/405-1033-66043,c89.php?Lang=zh-tw"
                        }
                    }
                    ]
                }
            }
            line_flex_str=json.dumps(line_flex_json) #新增的               
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_str))]
                )
            )

        if '文馨' in text and '實驗室' in text or '許文馨老師的lab'in text:
            line_flex_json={
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "許文馨 老師",
                        "size": "xl",
                        "weight": "bold",
                        "margin": "md"
                    },
                    {
                        "type": "text",
                        "text": "實驗室資訊",
                        "color": "#1DB446",
                        "margin": "none"
                    },
                    {
                        "type": "separator",
                        "color": "#888888",
                        "margin": "md"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                            },
                            {
                                "type": "text",
                                "text": "實驗室研究主題與方向",
                                "weight": "bold",
                                "margin": "sm",
                                "flex": 0
                            }
                            ]
                        },
                        {
                            "type": "text",
                            "text": "1.本實驗室的核心研究領域為 (資訊安全)",
                            "wrap": True
                        },
                        {
                            "type": "text",
                            "text": "2.實驗室通常以投稿與參加競賽、研討會和撰寫論文等方面為主。",
                            "wrap": True,
                            "margin": "md"
                        },
                        {
                            "type": "separator",
                            "color": "#888888",
                            "margin": "md"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                                },
                                {
                                    "type": "text",
                                    "text": "實驗室已發表的專題與計畫",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "flex": 0
                                }
                                ]
                            },
                            {
                                "type": "text",
                                "text": "目前已有學長姊的論文可至碩博士論文網找來看看",
                                "wrap": True
                            },
                            
                            {
                                "type": "separator",
                                "color": "#888888",
                                "margin": "md"
                            }
                            ]
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                                },
                                {
                                    "type": "text",
                                    "text": "實驗室其他細項與規定",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "flex": 0
                                }
                                ]
                            },
                            {
                                "type": "text",
                                "text": "1.有嚴格的內規",
                                "wrap": True,
                                "color": "#008888"
                            },
                            {
                                "type": "text",
                                "text": "加入前請審慎評估自身是否能適應高度自律與高強度的運作",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "2.固定每周進行會議",
                                "color": "#008888"
                            },
                            {
                                "type": "text",
                                "text": "每位成員需報告個人研究進度，並進行小組成果彙整與討論",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "3.課外學習",
                                "color": "#008888"
                            },
                            {
                                "type": "text",
                                "text": "實驗室會配合學校開設的課程與外部活動，提升成員實力",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "4.遇到問題的解決方式",
                                "color": "#008888"
                            },
                            {
                                "type": "text",
                                "text": "鼓勵於會議中提出共同討論，也可諮詢有經驗的學長姊",
                                "wrap": True
                            },
                            {
                                "type": "separator",
                                "color": "#888888",
                                "margin": "md"
                            }
                            ]
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                                },
                                {
                                    "type": "text",
                                    "text": "進老師實驗室須具備的能力",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "flex": 0
                                }
                                ]
                            },
                            {
                                "type": "text",
                                "text": "1.基礎文書能力",
                                "wrap": True,
                                "color": "#008888"
                            },
                            {
                                "type": "text",
                                "text": "能夠撰寫報告、整理資料、撰寫論文初稿等",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "2.中階程式撰寫能力",
                                "wrap": True,
                                "color": "#008888"
                            },
                            {
                                "type": "text",
                                "text": "熟悉至少一種程式語言並能進行中等複雜度的專題開發",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "3.良好的口語表達能力",
                                "color": "#008888"
                            },
                            {
                                "type": "text",
                                "text": "能夠清楚有邏輯地報告研究進度與說明研究內容",
                                "wrap": True
                            },
                            {
                                "type": "separator",
                                "color": "#888888",
                                "margin": "md"
                            }
                            ]
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                                },
                                {
                                    "type": "text",
                                    "text": "老師對於大一大二生提早進入實驗室的看法",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "wrap": True
                                }
                                ]
                            },
                            {
                                "type": "text",
                                "text": "1.老師支持大一、大二學生提前進入實驗室，認為早一點接觸研究是養成學術能力的重要關鍵",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "2.然而也強調：學生應具備上述提及的三項基本能力，並且具備主動積極、態度認真的學習精神",
                                "wrap": True,
                                "margin": "md"
                            }
                            ]
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "color": "#00AAAA",
                        "margin": "xxl",
                        "action": {
                        "type": "uri",
                        "label": "老師相關資訊",
                        "uri": "https://mi.csmu.edu.tw/p/405-1033-66045,c89.php?Lang=zh-tw"
                        }
                    }
                    ]
                }
            }
            line_flex_str=json.dumps(line_flex_json) #新增的               
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_str))]
                )
            )
        
        if '明性' in text and '實驗室' in text or '曾明性老師的lab'in text:
            line_flex_json={
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "曾明性 老師",
                        "size": "xl",
                        "weight": "bold",
                        "margin": "md"
                    },
                    {
                        "type": "text",
                        "text": "實驗室資訊",
                        "color": "#1DB446",
                        "margin": "none"
                    },
                    {
                        "type": "separator",
                        "color": "#888888",
                        "margin": "md"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                            },
                            {
                                "type": "text",
                                "text": "實驗室研究主題與方向",
                                "weight": "bold",
                                "margin": "sm",
                                "flex": 0
                            }
                            ]
                        },
                        {
                            "type": "text",
                            "text": "1.資料探勘與機器學習\n2.人工智慧與深度學習\n3.健康照護與智慧醫療物聯網\n4.軟式計算與最佳化演算法\n5.空間資訊技術。",
                            "wrap": True
                        },
                        {
                            "type": "separator",
                            "color": "#888888",
                            "margin": "md"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                                },
                                {
                                    "type": "text",
                                    "text": "實驗室已發表的專題與計畫",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "flex": 0
                                }
                                ]
                            },
                            {
                                "type": "text",
                                "text": "目前已有學長姊的論文可至碩博士論文網找來看看",
                                "wrap": True
                            },
                            {
                                "type": "separator",
                                "color": "#888888",
                                "margin": "md"
                            }
                            ]
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                                },
                                {
                                    "type": "text",
                                    "text": "實驗室其他細項與規定",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "flex": 0
                                }
                                ]
                            },
                            {
                                "type": "text",
                                "text": "由於老師並未參與訪談，請親自詢問老師或學長姐喔!",
                                "wrap": True
                            },
                            {
                                "type": "separator",
                                "color": "#888888",
                                "margin": "md"
                            }
                            ]
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                                },
                                {
                                    "type": "text",
                                    "text": "進老師實驗室須具備的能力",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "flex": 0
                                }
                                ]
                            },
                            {
                                "type": "text",
                                "text": "由於老師並未參與訪談，請親自詢問老師喔!",
                                "wrap": True
                            },
                            {
                                "type": "separator",
                                "color": "#888888",
                                "margin": "md"
                            }
                            ]
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                                },
                                {
                                    "type": "text",
                                    "text": "老師對於大一大二生提早進入實驗室的看法",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "wrap": True
                                }
                                ]
                            },
                            {
                                "type": "text",
                                "text": "由於老師並未參與訪談，請親自詢問老師哦!",
                                "wrap": True
                            }
                            ]
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "color": "#00AAAA",
                        "margin": "xxl",
                        "action": {
                        "type": "uri",
                        "label": "老師相關資訊",
                        "uri": "https://mi.csmu.edu.tw/p/405-1033-66037,c89.php?Lang=zh-tw"
                        }
                    }
                    ]
                }
            }
            line_flex_str=json.dumps(line_flex_json) #新增的               
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_str))]
                )
            )

        if '偉誌' in text and '實驗室' in text or '沈偉誌老師的lab'in text:
            line_flex_json={
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "沈偉誌 老師",
                        "size": "xl",
                        "weight": "bold",
                        "margin": "md"
                    },
                    {
                        "type": "text",
                        "text": "實驗室資訊",
                        "color": "#1DB446",
                        "margin": "none"
                    },
                    {
                        "type": "separator",
                        "color": "#888888",
                        "margin": "md"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                            },
                            {
                                "type": "text",
                                "text": "實驗室研究主題與方向",
                                "weight": "bold",
                                "margin": "sm",
                                "flex": 0
                            }
                            ]
                        },
                        {
                            "type": "text",
                            "text": "目前似乎不收學生\n相關事宜再請跟老師詢問 謝謝！",
                            "wrap": True
                        },
                        {
                            "type": "separator",
                            "color": "#888888",
                            "margin": "md"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                                },
                                {
                                    "type": "text",
                                    "text": "實驗室已發表的專題與計畫",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "flex": 0
                                }
                                ]
                            },
                            {
                                "type": "text",
                                "text": "暫無資料",
                                "wrap": True
                            },
                            {
                                "type": "separator",
                                "color": "#888888",
                                "margin": "md"
                            }
                            ]
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                                },
                                {
                                    "type": "text",
                                    "text": "實驗室其他細項與規定",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "flex": 0
                                }
                                ]
                            },
                            {
                                "type": "text",
                                "text": "暫無資料",
                                "wrap": True
                            },
                            {
                                "type": "separator",
                                "color": "#888888",
                                "margin": "md"
                            }
                            ]
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                                },
                                {
                                    "type": "text",
                                    "text": "進老師實驗室須具備的能力",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "flex": 0
                                }
                                ]
                            },
                            {
                                "type": "text",
                                "text": "暫無資料",
                                "wrap": True
                            },
                            {
                                "type": "separator",
                                "color": "#888888",
                                "margin": "md"
                            }
                            ]
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                                },
                                {
                                    "type": "text",
                                    "text": "老師對於大一大二生提早進入實驗室的看法",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "wrap": True
                                }
                                ]
                            },
                            {
                                "type": "text",
                                "text": "暫無資料",
                                "wrap": True
                            }
                            ]
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "color": "#00AAAA",
                        "margin": "xxl",
                        "action": {
                        "type": "uri",
                        "label": "老師相關資訊",
                        "uri": "https://mi.csmu.edu.tw/p/405-1033-66040,c89.php?Lang=zh-tw"
                        }
                    }
                    ]
                }
                }
            line_flex_str=json.dumps(line_flex_json) #新增的               
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_str))]
                )
            )
        
        if '實驗室'in text:
            quickReply = QuickReply(
                items=[
                    QuickReplyItem(
                        action=MessageAction(
                            label="賴慶祥",
                            text="賴慶祥老師的lab"
                        ), 
                    ),
                    QuickReplyItem(
                        action=MessageAction(
                            label="徐麗蘋",
                            text="徐麗蘋老師的lab"
                        ),  
                    ),
                    QuickReplyItem(
                        action=MessageAction(
                            label="張炎清",
                            text="張炎清老師的lab"
                        ), 
                    ),
                    QuickReplyItem(
                        action=MessageAction(
                            label="張啟昌",
                            text="張啟昌老師的lab"
                        ), 
                    ),
                    QuickReplyItem(
                        action=MessageAction(
                            label="李孝屏",
                            text="李孝屏老師的lab"
                        ), 
                    ),
                    QuickReplyItem(
                        action=MessageAction(
                            label="紀虹名",
                            text="紀虹名老師的lab"
                        ), 
                    ),
                    QuickReplyItem(
                        action=MessageAction(
                            label="許文馨",
                            text="許文馨老師的lab"
                        ), 
                    ),
                    QuickReplyItem(
                        action=MessageAction(
                            label="曾明性",
                            text="曾明性老師的lab"
                        ), 
                    ),
                    QuickReplyItem(
                        action=MessageAction(
                            label="沈偉誌",
                            text="沈偉誌老師的lab"
                        ), 
                    )
                ]
            )
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(
                        text='想了解哪位老師的實驗室呢~',
                        quick_reply=quickReply
                    )]
                )
            )
        


        if '師資'in text or '老師' in text:
            line_flex_json={
                "type": "carousel",
                "contents": [
                    {
                    "type": "bubble",
                    "header": {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "image",
                            "url": "https://mi.csmu.edu.tw/var/file/33/1033/pictures/991/m/mczh-tw400x400_small66036_69759506810.jpg",
                            "flex": 3,
                            "aspectRatio": "170:250",
                            "aspectMode": "fit",
                            "size": "5xl",
                            "align": "center"
                        }
                        ],
                        "borderColor": "#8E8E8E",
                        "justifyContent": "center",
                        "offsetStart": "45px",
                        "offsetTop": "xxl",
                        "borderWidth": "none",
                        "maxHeight": "200px",
                        "maxWidth": "200px",
                        "cornerRadius": "500px",
                        "alignItems": "center"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "賴慶祥 老師",
                            "weight": "bold",
                            "size": "xl",
                            "margin": "xxl",
                            "offsetStart": "70px"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "臨床醫學資料分析",
                                "margin": "md",
                                "wrap": False,
                                "flex": 6,
                                "decoration": "none",
                                "color": "#2894FF"
                            },
                            {
                                "type": "text",
                                "text": "結構方程模式",
                                "flex": 4,
                                "color": "#2894FF"
                            }
                            ],
                            "margin": "xl"
                        },
                        {
                            "type": "text",
                            "text": "管理績效評估",
                            "align": "center",
                            "margin": "md",
                            "color": "#2894FF"
                        },
                        {
                            "type": "separator",
                            "margin": "md",
                            "color": "#000000"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "margin": "lg",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "電話：",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 3
                                },
                                {
                                    "type": "text",
                                    "text": "(04)2473-0022 分機12213",
                                    "wrap": True,
                                    "color": "#000000",
                                    "size": "sm",
                                    "flex": 7
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "spacing": "sm",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "Email：",
                                        "color": "#aaaaaa",
                                        "size": "sm",
                                        "flex": 3
                                    },
                                    {
                                        "type": "text",
                                        "text": "liay@csmu.edu.tw",
                                        "wrap": True,
                                        "color": "#000000",
                                        "size": "sm",
                                        "flex": 7
                                    }
                                    ]
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "辦公室：",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 3
                                },
                                {
                                    "type": "text",
                                    "text": "正心樓12樓1253C",
                                    "wrap": True,
                                    "color": "#000000",
                                    "size": "sm",
                                    "flex": 7
                                }
                                ]
                            }
                            ]
                        }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "uri",
                            "label": "個人連結",
                            "uri": "https://message.csmu.edu.tw/HumanResources/open/HRKindOpenEP.asp?UIDNO=t00755"
                            }
                        }
                        ],
                        "flex": 0
                    }
                    },{
                    "type": "bubble",
                    "header": {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "image",
                            "url": "https://mi.csmu.edu.tw/var/file/33/1033/pictures/700/m/mczh-tw400x400_small66041_312096707057.jpg",
                            "flex": 3,
                            "aspectRatio": "170:250",
                            "aspectMode": "fit",
                            "size": "5xl",
                            "align": "center"
                        }
                        ],
                        "borderColor": "#8E8E8E",
                        "justifyContent": "center",
                        "offsetStart": "45px",
                        "offsetTop": "xxl",
                        "borderWidth": "none",
                        "maxHeight": "200px",
                        "maxWidth": "200px",
                        "cornerRadius": "500px",
                        "alignItems": "center"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "徐麗蘋 老師",
                            "weight": "bold",
                            "size": "xl",
                            "margin": "xxl",
                            "offsetStart": "70px"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "電腦輔助診斷系統",
                                "margin": "md",
                                "wrap": False,
                                "flex": 6,
                                "decoration": "none",
                                "color": "#2894FF"
                            },
                            {
                                "type": "text",
                                "text": "影像處理",
                                "flex": 4,
                                "color": "#2894FF"
                            }
                            ],
                            "margin": "xl"
                        },
                        {
                            "type": "text",
                            "text": "電腦圖形識別",
                            "align": "center",
                            "margin": "md",
                            "color": "#2894FF"
                        },
                        {
                            "type": "separator",
                            "margin": "md",
                            "color": "#000000"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "margin": "lg",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "電話：",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 3
                                },
                                {
                                    "type": "text",
                                    "text": "(04)2473-0022 分機12217",
                                    "wrap": True,
                                    "color": "#000000",
                                    "size": "sm",
                                    "flex": 7
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "spacing": "sm",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "Email：",
                                        "color": "#aaaaaa",
                                        "size": "sm",
                                        "flex": 3
                                    },
                                    {
                                        "type": "text",
                                        "text": "apple@csmu.edu.tw",
                                        "wrap": True,
                                        "color": "#000000",
                                        "size": "sm",
                                        "flex": 7
                                    }
                                    ]
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "辦公室：",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 3
                                },
                                {
                                    "type": "text",
                                    "text": "正心樓12樓1253G",
                                    "wrap": True,
                                    "color": "#000000",
                                    "size": "sm",
                                    "flex": 7
                                }
                                ]
                            }
                            ]
                        }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "uri",
                            "label": "個人連結",
                            "uri": "https://message.csmu.edu.tw/HumanResources/open/HRKindOpenEP.asp?UIDNO=t00609"
                            }
                        }
                        ],
                        "flex": 0
                    }
                    },{
                    "type": "bubble",
                    "header": {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "image",
                            "url": "https://mi.csmu.edu.tw/var/file/33/1033/img/2194/770690581.jpg",
                            "flex": 3,
                            "aspectRatio": "170:250",
                            "aspectMode": "fit",
                            "size": "5xl",
                            "align": "center"
                        }
                        ],
                        "borderColor": "#8E8E8E",
                        "justifyContent": "center",
                        "offsetStart": "45px",
                        "offsetTop": "xxl",
                        "borderWidth": "none",
                        "maxHeight": "200px",
                        "maxWidth": "200px",
                        "cornerRadius": "500px",
                        "alignItems": "center"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "張炎清 老師",
                            "weight": "bold",
                            "size": "xl",
                            "margin": "xxl",
                            "offsetStart": "70px"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "機器學習與深度學習",
                                "margin": "md",
                                "wrap": False,
                                "flex": 6,
                                "decoration": "none",
                                "color": "#2894FF"
                            },
                            {
                                "type": "text",
                                "text": "醫學影像處理",
                                "flex": 4,
                                "color": "#2894FF"
                            }
                            ],
                            "margin": "xl"
                        },
                        {
                            "type": "text",
                            "text": "生醫訊號處理",
                            "align": "center",
                            "margin": "md",
                            "color": "#2894FF"
                        },
                        {
                            "type": "separator",
                            "margin": "md",
                            "color": "#000000"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "margin": "lg",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "電話：",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 3
                                },
                                {
                                    "type": "text",
                                    "text": "(04)2473-0022分機12212",
                                    "wrap": True,
                                    "color": "#000000",
                                    "size": "sm",
                                    "flex": 7
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "spacing": "sm",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "Email：",
                                        "color": "#aaaaaa",
                                        "size": "sm",
                                        "flex": 3
                                    },
                                    {
                                        "type": "text",
                                        "text": "nicholas@csmu.edu.tw",
                                        "wrap": True,
                                        "color": "#000000",
                                        "size": "sm",
                                        "flex": 7
                                    }
                                    ]
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "辦公室：",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 3
                                },
                                {
                                    "type": "text",
                                    "text": "正心樓12樓1253B",
                                    "wrap": True,
                                    "color": "#000000",
                                    "size": "sm",
                                    "flex": 7
                                }
                                ]
                            }
                            ]
                        }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "uri",
                            "label": "個人連結",
                            "uri": "https://message.csmu.edu.tw/HumanResources/open/HRKindOpenEP.asp?UIDNO=t01358"
                            }
                        }
                        ],
                        "flex": 0
                    }
                    },{
                    "type": "bubble",
                    "header": {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "image",
                            "url": "https://mi.csmu.edu.tw/var/file/33/1033/img/2194/Chang_photo.jpg",
                            "flex": 3,
                            "aspectRatio": "170:250",
                            "aspectMode": "fit",
                            "size": "5xl",
                            "align": "center"
                        }
                        ],
                        "borderColor": "#8E8E8E",
                        "justifyContent": "center",
                        "offsetStart": "45px",
                        "offsetTop": "xxl",
                        "borderWidth": "none",
                        "maxHeight": "200px",
                        "maxWidth": "200px",
                        "cornerRadius": "500px",
                        "alignItems": "center"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "張啟昌 老師",
                            "weight": "bold",
                            "size": "xl",
                            "margin": "xxl",
                            "offsetStart": "70px"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "多發惡性腫瘤",
                                "margin": "md",
                                "wrap": False,
                                "flex": 6,
                                "decoration": "none",
                                "color": "#2894FF"
                            },
                            {
                                "type": "text",
                                "text": "癌症復發",
                                "flex": 4,
                                "color": "#2894FF"
                            }
                            ],
                            "margin": "xl"
                        },
                        {
                            "type": "text",
                            "text": "數位中醫",
                            "align": "center",
                            "margin": "md",
                            "color": "#2894FF"
                        },
                        {
                            "type": "separator",
                            "margin": "md",
                            "color": "#000000"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "margin": "lg",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "電話：",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 3
                                },
                                {
                                    "type": "text",
                                    "text": "(04)2473-0022分機12218",
                                    "wrap": True,
                                    "color": "#000000",
                                    "size": "sm",
                                    "flex": 7
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "spacing": "sm",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "Email：",
                                        "color": "#aaaaaa",
                                        "size": "sm",
                                        "flex": 3
                                    },
                                    {
                                        "type": "text",
                                        "text": "threec@csmu.edu.tw",
                                        "wrap": True,
                                        "color": "#000000",
                                        "size": "sm",
                                        "flex": 7
                                    }
                                    ]
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "辦公室：",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 3
                                },
                                {
                                    "type": "text",
                                    "text": "正心樓12樓1253H",
                                    "wrap": True,
                                    "color": "#000000",
                                    "size": "sm",
                                    "flex": 7
                                }
                                ]
                            }
                            ]
                        }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "uri",
                            "label": "個人連結",
                            "uri": "https://message.csmu.edu.tw/HumanResources/open/HRKindOpenEP.asp?UIDNO=t00895"
                            }
                        }
                        ],
                        "flex": 0
                    }
                    },{
                    "type": "bubble",
                    "header": {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "image",
                            "url": "https://mi.csmu.edu.tw/var/file/33/1033/img/2194/Lee_photo.jpg.jpg",
                            "flex": 3,
                            "aspectRatio": "170:250",
                            "aspectMode": "fit",
                            "size": "5xl",
                            "align": "center"
                        }
                        ],
                        "borderColor": "#8E8E8E",
                        "justifyContent": "center",
                        "offsetStart": "45px",
                        "offsetTop": "xxl",
                        "borderWidth": "none",
                        "maxHeight": "200px",
                        "maxWidth": "200px",
                        "cornerRadius": "500px",
                        "alignItems": "center"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "李孝屏 老師",
                            "weight": "bold",
                            "size": "xl",
                            "margin": "xxl",
                            "offsetStart": "70px"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "身心障礙資訊輔具",
                                "margin": "md",
                                "wrap": False,
                                "flex": 6,
                                "decoration": "none",
                                "color": "#2894FF"
                            },
                            {
                                "type": "text",
                                "text": "生物資訊",
                                "flex": 4,
                                "color": "#2894FF"
                            }
                            ],
                            "margin": "xl"
                        },
                        {
                            "type": "text",
                            "text": "行動計算、雲端計算",
                            "align": "center",
                            "margin": "md",
                            "color": "#2894FF"
                        },
                        {
                            "type": "separator",
                            "margin": "md",
                            "color": "#000000"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "margin": "lg",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "電話：",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 3
                                },
                                {
                                    "type": "text",
                                    "text": "(04)2473-0022分機12211",
                                    "wrap": True,
                                    "color": "#000000",
                                    "size": "sm",
                                    "flex": 7
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "spacing": "sm",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "Email：",
                                        "color": "#aaaaaa",
                                        "size": "sm",
                                        "flex": 3
                                    },
                                    {
                                        "type": "text",
                                        "text": "ping@csmu.edu.tw",
                                        "wrap": True,
                                        "color": "#000000",
                                        "size": "sm",
                                        "flex": 7
                                    }
                                    ]
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "辦公室：",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 3
                                },
                                {
                                    "type": "text",
                                    "text": "正心樓12樓1253A",
                                    "wrap": True,
                                    "color": "#000000",
                                    "size": "sm",
                                    "flex": 7
                                }
                                ]
                            }
                            ]
                        }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "uri",
                            "label": "個人連結",
                            "uri": "https://message.csmu.edu.tw/HumanResources/open/HRKindOpenEP.asp?UIDNO=t00538"
                            }
                        }
                        ],
                        "flex": 0
                    }
                    },{
                    "type": "bubble",
                    "header": {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "image",
                            "url": "https://mi.csmu.edu.tw/var/file/33/1033/img/2194/696204427.jpg",
                            "flex": 3,
                            "aspectRatio": "170:250",
                            "aspectMode": "fit",
                            "size": "5xl",
                            "align": "center"
                        }
                        ],
                        "borderColor": "#8E8E8E",
                        "justifyContent": "center",
                        "offsetStart": "45px",
                        "offsetTop": "xxl",
                        "borderWidth": "none",
                        "maxHeight": "200px",
                        "maxWidth": "200px",
                        "cornerRadius": "500px",
                        "alignItems": "center"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "紀虹名 老師",
                            "weight": "bold",
                            "size": "xl",
                            "margin": "xxl",
                            "offsetStart": "70px"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "生醫訊號處理",
                                "margin": "md",
                                "wrap": False,
                                "flex": 6,
                                "decoration": "none",
                                "color": "#2894FF"
                            },
                            {
                                "type": "text",
                                "text": "網路成癮",
                                "flex": 4,
                                "color": "#2894FF"
                            }
                            ],
                            "margin": "xl"
                        },
                        {
                            "type": "text",
                            "text": "遊戲成癮",
                            "align": "center",
                            "margin": "md",
                            "color": "#2894FF"
                        },
                        {
                            "type": "separator",
                            "margin": "md",
                            "color": "#000000"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "margin": "lg",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "電話：",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 3
                                },
                                {
                                    "type": "text",
                                    "text": "(04)2473-0022分機11736",
                                    "wrap": True,
                                    "color": "#000000",
                                    "size": "sm",
                                    "flex": 7
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "spacing": "sm",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "Email：",
                                        "color": "#aaaaaa",
                                        "size": "sm",
                                        "flex": 3
                                    },
                                    {
                                        "type": "text",
                                        "text": "t03723@csmu.edu.tw",
                                        "wrap": True,
                                        "color": "#000000",
                                        "size": "sm",
                                        "flex": 7
                                    }
                                    ]
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "辦公室：",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 3
                                },
                                {
                                    "type": "text",
                                    "text": "正心樓12樓1253F",
                                    "wrap": True,
                                    "color": "#000000",
                                    "size": "sm",
                                    "flex": 7
                                }
                                ]
                            }
                            ]
                        }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "uri",
                            "label": "個人連結",
                            "uri": "https://message.csmu.edu.tw/HumanResources/open/HRKindOpenEP.asp?UIDNO=t03723"
                            }
                        }
                        ],
                        "flex": 0
                    }
                    },{
                    "type": "bubble",
                    "header": {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "image",
                            "url": "https://mi.csmu.edu.tw/var/file/33/1033/img/2194/S__17981495.jpg",
                            "flex": 3,
                            "aspectRatio": "170:250",
                            "aspectMode": "fit",
                            "size": "5xl",
                            "align": "center"
                        }
                        ],
                        "borderColor": "#8E8E8E",
                        "justifyContent": "center",
                        "offsetStart": "45px",
                        "offsetTop": "xxl",
                        "borderWidth": "none",
                        "maxHeight": "200px",
                        "maxWidth": "200px",
                        "cornerRadius": "500px",
                        "alignItems": "center"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "許文馨 老師",
                            "weight": "bold",
                            "size": "xl",
                            "margin": "xxl",
                            "offsetStart": "70px"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "多媒體技術",
                                "margin": "md",
                                "wrap": False,
                                "flex": 6,
                                "decoration": "none",
                                "color": "#2894FF"
                            },
                            {
                                "type": "text",
                                "text": "資訊安全",
                                "flex": 4,
                                "color": "#2894FF"
                            }
                            ],
                            "margin": "xl"
                        },
                        {
                            "type": "text",
                            "text": "醫學資訊",
                            "align": "center",
                            "margin": "md",
                            "color": "#2894FF"
                        },
                        {
                            "type": "separator",
                            "margin": "md",
                            "color": "#000000"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "margin": "lg",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "電話：",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 3
                                },
                                {
                                    "type": "text",
                                    "text": "(04)2473-0022 分機11735",
                                    "wrap": True,
                                    "color": "#000000",
                                    "size": "sm",
                                    "flex": 7
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "spacing": "sm",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "Email：",
                                        "color": "#aaaaaa",
                                        "size": "sm",
                                        "flex": 3
                                    },
                                    {
                                        "type": "text",
                                        "text": "wshsu@csmu.edu.tw",
                                        "wrap": True,
                                        "color": "#000000",
                                        "size": "sm",
                                        "flex": 7
                                    }
                                    ]
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "辦公室：",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 3
                                },
                                {
                                    "type": "text",
                                    "text": "正心樓12樓1227",
                                    "wrap": True,
                                    "color": "#000000",
                                    "size": "sm",
                                    "flex": 7
                                }
                                ]
                            }
                            ]
                        }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "uri",
                            "label": "個人連結",
                            "uri": "https://message.csmu.edu.tw/HumanResources/open/HRKindOpenEP.asp?UIDNO=t03670"
                            }
                        }
                        ],
                        "flex": 0
                    }
                    },{
                    "type": "bubble",
                    "header": {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "image",
                            "url": "https://mi.csmu.edu.tw/var/file/33/1033/img/1744365505500.jpg",
                            "flex": 3,
                            "aspectRatio": "170:250",
                            "aspectMode": "fit",
                            "size": "5xl",
                            "align": "center"
                        }
                        ],
                        "borderColor": "#8E8E8E",
                        "justifyContent": "center",
                        "offsetStart": "45px",
                        "offsetTop": "xxl",
                        "borderWidth": "none",
                        "maxHeight": "200px",
                        "maxWidth": "200px",
                        "cornerRadius": "500px",
                        "alignItems": "center"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "曾明性 老師",
                            "weight": "bold",
                            "size": "xl",
                            "margin": "xxl",
                            "offsetStart": "70px"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "人工智慧與深度學習",
                                "margin": "md",
                                "wrap": False,
                                "flex": 6,
                                "decoration": "none",
                                "color": "#2894FF"
                            },
                            {
                                "type": "text",
                                "text": "大數據分析",
                                "flex": 4,
                                "color": "#2894FF"
                            }
                            ],
                            "margin": "xl"
                        },
                        {
                            "type": "text",
                            "text": "機器學習與資料探勘",
                            "align": "center",
                            "margin": "md",
                            "color": "#2894FF"
                        },
                        {
                            "type": "separator",
                            "margin": "md",
                            "color": "#000000"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "margin": "lg",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "電話：",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 3
                                },
                                {
                                    "type": "text",
                                    "text": "(04)2473-0022分機12214",
                                    "wrap": True,
                                    "color": "#000000",
                                    "size": "sm",
                                    "flex": 7
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "spacing": "sm",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "Email：",
                                        "color": "#aaaaaa",
                                        "size": "sm",
                                        "flex": 3
                                    },
                                    {
                                        "type": "text",
                                        "text": "mht@csmu.edu.tw",
                                        "wrap": True,
                                        "color": "#000000",
                                        "size": "sm",
                                        "flex": 7
                                    }
                                    ]
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "辦公室：",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 3
                                },
                                {
                                    "type": "text",
                                    "text": "正心樓12樓1253D",
                                    "wrap": True,
                                    "color": "#000000",
                                    "size": "sm",
                                    "flex": 7
                                }
                                ]
                            }
                            ]
                        }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "uri",
                            "label": "個人連結",
                            "uri": "https://message.csmu.edu.tw/HumanResources/open/HRKindOpenEP.asp?UIDNO=t00949"
                            }
                        }
                        ],
                        "flex": 0
                    }
                    },{
                    "type": "bubble",
                    "header": {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "image",
                            "url": "https://mi.csmu.edu.tw/var/file/33/1033/img/2194/Sheng_photo.jpg",
                            "flex": 3,
                            "aspectRatio": "170:250",
                            "aspectMode": "fit",
                            "size": "5xl",
                            "align": "center"
                        }
                        ],
                        "borderColor": "#8E8E8E",
                        "justifyContent": "center",
                        "offsetStart": "45px",
                        "offsetTop": "xxl",
                        "borderWidth": "none",
                        "maxHeight": "200px",
                        "maxWidth": "200px",
                        "cornerRadius": "500px",
                        "alignItems": "center"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "沈偉誌 老師",
                            "weight": "bold",
                            "size": "xl",
                            "margin": "xxl",
                            "offsetStart": "70px"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "資料庫與資料工程",
                                "margin": "md",
                                "wrap": False,
                                "flex": 6,
                                "decoration": "none",
                                "color": "#2894FF"
                            },
                            {
                                "type": "text",
                                "text": "影像處理",
                                "flex": 4,
                                "color": "#2894FF"
                            }
                            ],
                            "margin": "xl"
                        },
                        {
                            "type": "text",
                            "text": "人工智慧",
                            "align": "center",
                            "margin": "md",
                            "color": "#2894FF"
                        },
                        {
                            "type": "separator",
                            "margin": "md",
                            "color": "#000000"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "margin": "lg",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "電話：",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 3
                                },
                                {
                                    "type": "text",
                                    "text": "(04)2473-0022 分機26132",
                                    "wrap": True,
                                    "color": "#000000",
                                    "size": "sm",
                                    "flex": 7
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "spacing": "sm",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "Email：",
                                        "color": "#aaaaaa",
                                        "size": "sm",
                                        "flex": 3
                                    },
                                    {
                                        "type": "text",
                                        "text": "wcshen@gmail.com",
                                        "wrap": True,
                                        "color": "#000000",
                                        "size": "sm",
                                        "flex": 7
                                    }
                                    ]
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "辦公室：",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 3
                                },
                                {
                                    "type": "text",
                                    "text": "誠愛樓12樓81218室",
                                    "wrap": True,
                                    "color": "#000000",
                                    "size": "sm",
                                    "flex": 7
                                }
                                ]
                            }
                            ]
                        }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "uri",
                            "label": "個人連結",
                            "uri": "https://message.csmu.edu.tw/HumanResources/open/HRKindOpenEP.asp?UIDNO=t03480"
                            }
                        }
                        ],
                        "flex": 0
                    }
                 }
                ]
            }
            line_flex_str=json.dumps(line_flex_json) #新增的               
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_str))]
                )
            )

        if '系秘'in text:
            message = TextMessage(
                text="王武雄先生\n\n電話：04-24730022 (校內分機：11733)\n\n辦公室：誠愛樓11樓81128室 (系辦)\n\nE-mail：cs1331@csmu.edu.tw"
            )
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[message]
                )
            )
        
        if '畢業門檻'in text:
            line_flex_json={
                "type": "bubble",
                "size": "mega",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "醫資系畢業門檻",
                        "wrap": True,
                        "weight": "bold",
                        "size": "xl",
                        "color": "#3366CC"
                    },
                    {
                        "type": "text",
                        "text": "最低畢業學分：128學分",
                        "wrap": True,
                        "weight": "bold"
                    },
                    {
                        "type": "text",
                        "text": "1. 必修：65學分\n2. 通識：20學分\n3. 體育：4學分\n4. 選修：39學分",
                        "wrap": True
                    },
                    {
                        "type": "separator"
                    },
                    {
                        "type": "text",
                        "text": "通識課程說明：",
                        "wrap": True,
                        "weight": "bold"
                    },
                    {
                        "type": "text",
                        "text": "・基礎通識：6學分\n・博雅通識：16學分",
                        "wrap": True
                    },
                    {
                        "type": "text",
                        "text": "系選修至少27學分，並須通過程式設計能力檢定，方可畢業。",
                        "wrap": True
                    },
                    {
                        "type": "separator"
                    },
                    {
                        "type": "text",
                        "text": "英文畢業門檻：",
                        "wrap": True,
                        "weight": "bold"
                    },
                    {
                        "type": "text",
                        "text": "參加校外官方英文能力檢定或CEPT校內英文檢定考試，並於每學期開學後繳交通過之成績證明文件至各系登錄，以作為畢業資格審定之依據。",
                        "wrap": True
                    },
                    {
                        "type": "separator"
                    },
                    {
                        "type": "text",
                        "text": "百分百門檻：",
                        "wrap": True,
                        "weight": "bold"
                    },
                    {
                        "type": "text",
                        "text": "依「中山醫大深化醫能力百分百實施辦法」累積至100點。",
                        "wrap": True
                    },
                    {
                        "type": "separator"
                    },
                    {
                        "type": "text",
                        "text": "雙主修 / 輔系 / 跨域課程",
                        "wrap": True,
                        "weight": "bold"
                    },
                    {
                        "type": "text",
                        "text": "須擇一修畢並符合修習規範。\n\n跨域微學程學分不可與以下重複：\n1. 其他跨域微學程之科目\n2. 主系科目(必修、選修、專業選修) 與通識課",
                        "wrap": True
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "更多資訊",
                        "uri": "https://mi.csmu.edu.tw/p/412-1033-120.php?Lang=zh-tw"
                        }
                    }
                    ],
                    "flex": 0
                }
            }
            line_flex_str=json.dumps(line_flex_json) #新增的               
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_str))]
                )
            )
        
        #7
        if '大一上'in text and '全' in text and '課' in text:
            line_flex_json={
                "type": "carousel",
                "contents": [
                    {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/085/75/0010857557.jpg&v=5eb1402ak&w=375&h=375",
                        "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "fit",
                        "backgroundColor": "#DDDDDD"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "管理學",
                            "weight": "bold",
                            "size": "xl",
                            "contents": [
                            {
                                "type": "span",
                                "text": "管理學"
                            },
                            {
                                "type": "span",
                                "text": " (大一上必修)",
                                "size": "md"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "margin": "md",
                            "contents": [
                            {
                                "type": "icon",
                                "size": "sm",
                                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                            },
                            {
                                "type": "icon",
                                "size": "sm",
                                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                            },
                            {
                                "type": "icon",
                                "size": "sm",
                                "url": "https://developers-resource.landpress.line.me/fx/img/review_gray_star_28.png"
                            },
                            {
                                "type": "text",
                                "text": "學分數",
                                "size": "sm",
                                "color": "#999999",
                                "margin": "md",
                                "flex": 0
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "margin": "lg",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "授課老師",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 3
                                },
                                {
                                    "type": "text",
                                    "text": "張啟昌",
                                    "wrap": True,
                                    "color": "#000000",
                                    "size": "sm",
                                    "flex": 7
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "授課方式",
                                    "color": "#aaaaaa",
                                    "flex": 3,
                                    "size": "sm"
                                },
                                {
                                    "type": "text",
                                    "text": "課本、PPT(英文)、小組討論與報告",
                                    "flex": 7,
                                    "size": "sm",
                                    "color": "#000000",
                                    "wrap": True
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "margin": "md",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "課程內容",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 3
                                },
                                {
                                    "type": "text",
                                    "text": "向學生介紹管理人員的角色和職能，內容包括組織介紹以及管理的必要性和性質。對管理四項職能進行詳細調查：計劃和決策、組織、領導和激勵以及控制",
                                    "wrap": True,
                                    "color": "#000000",
                                    "size": "sm",
                                    "flex": 7
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "margin": "md",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "評分方式",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 3,
                                    "wrap": True
                                },
                                {
                                    "type": "text",
                                    "text": "出席/12%，隨堂考/48%，書面報告/20%，口頭報告/20% (僅供參考)",
                                    "size": "sm",
                                    "flex": 7,
                                    "wrap": True,
                                    "color": "#000000"
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "學長姐建議",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 3
                                },
                                {
                                    "type": "text",
                                    "text": "考試若要拿高分可多參考考古題！課程會經常報告，要好好準備！",
                                    "flex": 7,
                                    "size": "sm",
                                    "color": "#000000",
                                    "wrap": True
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "參考書目",
                                    "flex": 3,
                                    "size": "sm",
                                    "color": "#aaaaaa"
                                },
                                {
                                    "type": "text",
                                    "text": "Stephen P. Robbins., David De Cenzo, and Mary Coulter (2020) Fundamentals of Management (GE) 11/e  (如上圖)",
                                    "flex": 7,
                                    "size": "sm",
                                    "color": "#000000",
                                    "wrap": True
                                }
                                ]
                            }
                            ]
                        }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "uri",
                            "label": "課程綱要查詢",
                            "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                            }
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [],
                            "margin": "sm"
                        }
                        ],
                        "flex": 0
                    }
                    },{
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/092/21/0010922111.jpg&v=6256a679k&w=348&h=348",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#FFFFFF"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "醫學資訊概論",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": "醫學資訊概論"
                        },
                        {
                            "type": "span",
                            "text": " (大一上必修)",
                            "size": "md"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "徐麗蘋",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "PPT + 板書",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "深入介紹電腦之運作和組織，了解電腦且具有對新軟硬體變化的學習潛能，介紹資訊趨勢之相關知識，介紹資訊應用於醫學方面之知識與相關系統概念",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "重視出席，期中考，期末考 (僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "上課筆記很重要，要認真抄！",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "最新計算機概論 陳惠貞\n(如上圖)",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ],
                            "margin": "md"
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                    }
                    },{
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://m.media-amazon.com/images/I/51fzy0l6mKL._AC_UF1000,1000_QL80_.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#DDDDDD"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "微積分",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": "微積分"
                        },
                        {
                            "type": "span",
                            "text": " (大一上必修)",
                            "size": "md"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gray_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "紀虹名",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "PPT (英文) + 板書",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "重要微積分觀念、定義和定理，輔以範例解釋計算方式和應用層面，包含函數、極限、導數、微分",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "出席/15%，隨堂考/25%，期中考/30%，期末考/30% (僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "多練習課本習題以及老師給的題目！",
                                "flex": 7,
                                "wrap": True,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "Applied Calculus for the Managerial Life and Social Sciences 10/e T. (如上圖)",
                                "flex": 7,
                                "size": "sm",
                                "wrap": True,
                                "color": "#000000"
                            }
                            ]
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
                },{
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://cdn.cybassets.com/media/W1siZiIsIjI1OTY2L3Byb2R1Y3RzLzQzNTM4MjI5LzE3MDE2Njk4MTlfZTVkZmZhYTBkYzQ3NTM3MzVlNTguanBlZyJdLFsicCIsInRodW1iIiwiMjA0OHgyMDQ4Il1d.jpeg?sha=8dd42d25e0624747",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#DDDDDD"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "管理數學",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": "管理數學"
                        },
                        {
                            "type": "span",
                            "text": " (大一上選修)",
                            "size": "md"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gray_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "賴慶祥",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "PPT + 板書",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "(1)線性模式的基礎理論\n(2)單形法之運算及線性模式在管理上的應用\n(3)以線性模式解決各類問題的建模及求解\n(4)線性模式在管理上所扮演的重要角色。",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "出席10%，作業依題數每題1%。考試每次25%，缺席每次扣1分。總分55-59者調整為60 (限無缺席且無缺交作業者)。 (僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "作業認真寫，多練習課本習題很有用！",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "作業研究(第十五版)\n [廖經芳譯(Anderson)] 9789579282901 (如上圖)",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                    }
                    },{
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcRorZN0iYrXosREGfzmKefupIkvbwwrrux8p7zX9AOmm3COEkxVZIiTKybmPUYypJPIHDq0386cMGYHq2icN-iO0Z2q5woabyrT0F2NHFtv6HucaDXmrN9J3w&usqp=CAc",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#DDDDDD"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "C語言",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": "C語言"
                        },
                        {
                            "type": "span",
                            "text": " (大一上選修)",
                            "size": "md"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gray_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "張炎清",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "課本、電腦操作",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "C 程式語言教學，全英授課",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "期中指定考/15%，期中考/25%，期末指定考/15%，期末考/25%，平時/20% \n(僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "上課認真聽，有問題當天下課問老師，只要有認真上課就可以PASS!! 若英文、程式能力較弱，建議可以先找中文書進行預習，這樣上課時會比較有個概念且容易理解！",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "C HOW TO PROGRAM\n(如上圖)",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ],
                            "margin": "md"
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
                },{
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://sl.bing.net/cRZK5JjqguG",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#9D9D9D"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "醫療數位孿生概論",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": "醫療數位孿生概論"
                        }
                        ]
                    },
                    {
                        "type": "text",
                        "text": " (大一上選修)",
                        "weight": "bold"
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "張啟昌",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "課本、PPT(英文)、小組討論與報告",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "概述數位醫學孿生技術的最新發展，使學生能夠深入了解健康個體或患者產生的健康和醫療數據，並強調該技術在醫療保健領域的重要性。",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "隨堂考/20%，書面報告/40%，口頭報告/40% (僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "無",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "無",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
                },{
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#DDDDDD",
                    "url": "https://sl.bing.net/cRZK5JjqguG"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "健康資訊輔具概論",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": "健康資訊輔具概論"
                        }
                        ]
                    },
                    {
                        "type": "text",
                        "text": " (大一上選修)",
                        "weight": "bold"
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "李孝屏",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "PPT講解",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "將教導學生了解身心障礙者與老年人在資訊取得方面的困難、可應用於解決問題的資訊技術以及資訊輔助系統的現況與未來發展。",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "書面報告/50%，口頭報告/50% (僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "讀熟老師上課PPT",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "老師的PPT",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
                }
            ]
            }
            line_flex_str=json.dumps(line_flex_json) #新增的               
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_str))]
                )
            )
        #3
        if '大一上'in text and '必修' in text and '課' in text:
            line_flex_json={
                "type": "carousel",
                "contents": [
                    {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/085/75/0010857557.jpg&v=5eb1402ak&w=375&h=375",
                        "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "fit",
                        "backgroundColor": "#DDDDDD"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "管理學",
                            "weight": "bold",
                            "size": "xl",
                            "contents": [
                            {
                                "type": "span",
                                "text": "管理學"
                            },
                            {
                                "type": "span",
                                "text": " (大一上必修)",
                                "size": "md"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "margin": "md",
                            "contents": [
                            {
                                "type": "icon",
                                "size": "sm",
                                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                            },
                            {
                                "type": "icon",
                                "size": "sm",
                                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                            },
                            {
                                "type": "icon",
                                "size": "sm",
                                "url": "https://developers-resource.landpress.line.me/fx/img/review_gray_star_28.png"
                            },
                            {
                                "type": "text",
                                "text": "學分數",
                                "size": "sm",
                                "color": "#999999",
                                "margin": "md",
                                "flex": 0
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "margin": "lg",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "授課老師",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 3
                                },
                                {
                                    "type": "text",
                                    "text": "張啟昌",
                                    "wrap": True,
                                    "color": "#000000",
                                    "size": "sm",
                                    "flex": 7
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "授課方式",
                                    "color": "#aaaaaa",
                                    "flex": 3,
                                    "size": "sm"
                                },
                                {
                                    "type": "text",
                                    "text": "課本、PPT(英文)、小組討論與報告",
                                    "flex": 7,
                                    "size": "sm",
                                    "color": "#000000",
                                    "wrap": True
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "margin": "md",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "課程內容",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 3
                                },
                                {
                                    "type": "text",
                                    "text": "向學生介紹管理人員的角色和職能，內容包括組織介紹以及管理的必要性和性質。對管理四項職能進行詳細調查：計劃和決策、組織、領導和激勵以及控制",
                                    "wrap": True,
                                    "color": "#000000",
                                    "size": "sm",
                                    "flex": 7
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "margin": "md",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "評分方式",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 3,
                                    "wrap": True
                                },
                                {
                                    "type": "text",
                                    "text": "出席/12%，隨堂考/48%，書面報告/20%，口頭報告/20% (僅供參考)",
                                    "size": "sm",
                                    "flex": 7,
                                    "wrap": True,
                                    "color": "#000000"
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "學長姐建議",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 3
                                },
                                {
                                    "type": "text",
                                    "text": "考試若要拿高分可多參考考古題！課程會經常報告，要好好準備！",
                                    "flex": 7,
                                    "size": "sm",
                                    "color": "#000000",
                                    "wrap": True
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "參考書目",
                                    "flex": 3,
                                    "size": "sm",
                                    "color": "#aaaaaa"
                                },
                                {
                                    "type": "text",
                                    "text": "Stephen P. Robbins., David De Cenzo, and Mary Coulter (2020) Fundamentals of Management (GE) 11/e  (如上圖)",
                                    "flex": 7,
                                    "size": "sm",
                                    "color": "#000000",
                                    "wrap": True
                                }
                                ]
                            }
                            ]
                        }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "uri",
                            "label": "課程綱要查詢",
                            "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                            }
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [],
                            "margin": "sm"
                        }
                        ],
                        "flex": 0
                    }
                    },{
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/092/21/0010922111.jpg&v=6256a679k&w=348&h=348",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#FFFFFF"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "醫學資訊概論",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": "醫學資訊概論"
                        },
                        {
                            "type": "span",
                            "text": " (大一上必修)",
                            "size": "md"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "徐麗蘋",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "PPT + 板書",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "深入介紹電腦之運作和組織，了解電腦且具有對新軟硬體變化的學習潛能，介紹資訊趨勢之相關知識，介紹資訊應用於醫學方面之知識與相關系統概念",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "重視出席，期中考，期末考 (僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "上課筆記很重要，要認真抄！",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "最新計算機概論 陳惠貞\n(如上圖)",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ],
                            "margin": "md"
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                    }
                    },{
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://m.media-amazon.com/images/I/51fzy0l6mKL._AC_UF1000,1000_QL80_.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#DDDDDD"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "微積分",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": "微積分"
                        },
                        {
                            "type": "span",
                            "text": " (大一上必修)",
                            "size": "md"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gray_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "紀虹名",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "PPT (英文) + 板書",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "重要微積分觀念、定義和定理，輔以範例解釋計算方式和應用層面，包含函數、極限、導數、微分",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "出席/15%，隨堂考/25%，期中考/30%，期末考/30% (僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "多練習課本習題以及老師給的題目！",
                                "flex": 7,
                                "wrap": True,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "Applied Calculus for the Managerial Life and Social Sciences 10/e T. (如上圖)",
                                "flex": 7,
                                "size": "sm",
                                "wrap": True,
                                "color": "#000000"
                            }
                            ]
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
                }
            ]
            }
            line_flex_str=json.dumps(line_flex_json) #新增的               
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_str))]
                )
            )
        #4
        if '大一上'in text and '選修' in text and '課' in text:
            line_flex_json={
                "type": "carousel",
                "contents": [
                {
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://cdn.cybassets.com/media/W1siZiIsIjI1OTY2L3Byb2R1Y3RzLzQzNTM4MjI5LzE3MDE2Njk4MTlfZTVkZmZhYTBkYzQ3NTM3MzVlNTguanBlZyJdLFsicCIsInRodW1iIiwiMjA0OHgyMDQ4Il1d.jpeg?sha=8dd42d25e0624747",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#DDDDDD"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "管理數學",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": "管理數學"
                        },
                        {
                            "type": "span",
                            "text": " (大一上選修)",
                            "size": "md"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gray_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "賴慶祥",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "PPT + 板書",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "(1)線性模式的基礎理論\n(2)單形法之運算及線性模式在管理上的應用\n(3)以線性模式解決各類問題的建模及求解\n(4)線性模式在管理上所扮演的重要角色。",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "出席10%，作業依題數每題1%。考試每次25%，缺席每次扣1分。總分55-59者調整為60 (限無缺席且無缺交作業者)。 (僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "作業認真寫，多練習課本習題很有用！",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "作業研究(第十五版)\n [廖經芳譯(Anderson)] 9789579282901 (如上圖)",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                    }
                    },{
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcRorZN0iYrXosREGfzmKefupIkvbwwrrux8p7zX9AOmm3COEkxVZIiTKybmPUYypJPIHDq0386cMGYHq2icN-iO0Z2q5woabyrT0F2NHFtv6HucaDXmrN9J3w&usqp=CAc",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#DDDDDD"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "C語言",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": "C語言"
                        },
                        {
                            "type": "span",
                            "text": " (大一上選修)",
                            "size": "md"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gray_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "張炎清",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "課本、電腦操作",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "C 程式語言教學，全英授課",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "期中指定考/15%，期中考/25%，期末指定考/15%，期末考/25%，平時/20% \n(僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "上課認真聽，有問題當天下課問老師，只要有認真上課就可以PASS!! 若英文、程式能力較弱，建議可以先找中文書進行預習，這樣上課時會比較有個概念且容易理解！",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "C HOW TO PROGRAM\n(如上圖)",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ],
                            "margin": "md"
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
                },{
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://sl.bing.net/cRZK5JjqguG",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#9D9D9D"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "醫療數位孿生概論",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": "醫療數位孿生概論"
                        }
                        ]
                    },
                    {
                        "type": "text",
                        "text": " (大一上選修)",
                        "weight": "bold"
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "張啟昌",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "課本、PPT(英文)、小組討論與報告",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "概述數位醫學孿生技術的最新發展，使學生能夠深入了解健康個體或患者產生的健康和醫療數據，並強調該技術在醫療保健領域的重要性。",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "隨堂考/20%，書面報告/40%，口頭報告/40% (僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "無",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "無",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
                },{
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#DDDDDD",
                    "url": "https://sl.bing.net/cRZK5JjqguG"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "健康資訊輔具概論",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": "健康資訊輔具概論"
                        }
                        ]
                    },
                    {
                        "type": "text",
                        "text": " (大一上選修)",
                        "weight": "bold"
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "李孝屏",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "PPT講解",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "將教導學生了解身心障礙者與老年人在資訊取得方面的困難、可應用於解決問題的資訊技術以及資訊輔助系統的現況與未來發展。",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "書面報告/50%，口頭報告/50% (僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "讀熟老師上課PPT",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "老師的PPT",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
                }
            ]
            }
            line_flex_str=json.dumps(line_flex_json) #新增的               
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_str))]
                )
            )

        #10
        if '大一下'in text and '全' in text and '課' in text:
            line_flex_json={
                "type": "carousel",
                "contents": [
                    {
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://m.media-amazon.com/images/I/51fzy0l6mKL._AC_UF1000,1000_QL80_.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#DDDDDD"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "微積分",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": "微積分"
                        },
                        {
                            "type": "span",
                            "text": " (大一上、下必修)",
                            "size": "md"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gray_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "紀虹名",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "PPT (英文) + 板書",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "重要微積分觀念、定義和定理，輔以範例解釋計算方式和應用層面，包含函數、極限、導數、微分",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "出席/15%，隨堂考/25%，期中考/30%，期末考/30% (僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "多練習課本習題以及老師給的題目！",
                                "flex": 7,
                                "wrap": True,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "Applied Calculus for the Managerial Life and Social Sciences 10/e T. (如上圖)",
                                "flex": 7,
                                "size": "sm",
                                "wrap": True,
                                "color": "#000000"
                            }
                            ]
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
                },{
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS6N4n10G3Oz8CKMW5W6APWqf0jJyC13OQoMw&s",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#FFFFFF"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "物件導向程式設計一",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": "物件導向程式設計一"
                        }
                        ]
                    },
                    {
                        "type": "text",
                        "text": "(大一下必修)",
                        "weight": "bold"
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "李孝屏",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "PPT (中文)",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "主要介紹JAVA程式語言內容涵蓋：Java簡介、變數、運算子、從鍵盤讀取資料、條件分支、迴圈、陣列",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "書面報告/80%，期中考/10%，期末考/10% (僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "上課聽課，課後多練習",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "可參考老師提供的簡報，或其他相關書籍",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ],
                            "margin": "md"
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
                },{
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/068/79/0010687971.jpg&v=55dc43edk&w=348&h=348",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#FFFFFF"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "計算機組織與結構",
                        "size": "xl",
                        "weight": "bold"
                    },
                    {
                        "type": "text",
                        "text": " (大一下必修)",
                        "weight": "bold"
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "徐麗蘋",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "PPT + 板書",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "計算機組織與結構的概況，觀查電腦設計、檢視電腦之主元件及互連系統、檢視CPU的內部結構和組織、CPU的內部結構和微程式運作及平行組織等",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "重視出席，期中考，期末考 (僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "上課筆記很重要！要認真抄！",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "計算機組織與結構：效能設計 Stallings: Computer Organization and Architecture 9/E (如上圖)",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ],
                            "margin": "md"
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                    }
                    },{
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT9iiLOv3FWaZTMfD-I3Uk1xnAxZzFcjkdcow&s",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#DDDDDD"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "醫務管理概論",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": "醫務管理概論"
                        },
                        {
                            "type": "span",
                            "text": " (大一下必修)",
                            "size": "md"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "張啟昌",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "課本、PPT(英文)、小組討論與報告",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "向學生介紹組織理論和組織行為及其在醫療保健組織管理中的應用。以最新的組織理論和研究為基礎，探討如何將組織理論應用於現實世界中。",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "出席/10%，隨堂考/40%，書面報告/25%，口頭報告/25% (僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "要拿高分多練習考古題！考試可帶書，答案都會在課本或老師的PPT內找的到，此外，課堂上經常會有報告、小組討論",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "Management in Health Care Practice \nISBN: 978-89918-175-3\n(如上圖)",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
                },{
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://m.media-amazon.com/images/I/51N-+aF6zWL.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#DDDDDD"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "線性代數",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": "線性代數"
                        },
                        {
                            "type": "span",
                            "text": " (大一下必修)",
                            "size": "md"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gray_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "賴慶祥",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "PPT + 板書",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "線性的代數原理，以矩陣運算的方式處理線性方面的問題",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "出席15%；  作業 20% (每次10%)；  考試75% (每次25%)。合計 110%。\n分數調整標準：總分57-59 無缺席 & 無作業缺交，調整為 60。 (僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "作業認真寫，多練習課本習題非常有用！",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "DeFranza, J. & Gagliardi, D. (2009), Introduction to Linear Algebra with Applications, McGraw-Hill. (如上圖)",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                    }
                },{
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://sl.bing.net/cRZK5JjqguG",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#9D9D9D"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "MATLAB程式設計",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": "MATLAB程式設計"
                        }
                        ]
                    },
                    {
                        "type": "text",
                        "text": " (大一下選修)",
                        "weight": "bold"
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gray_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "張炎清",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "全英文授課、電腦操作",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "學習MATLAB語言的基本語法，並以MATLAB來實踐機器學習和深度學習的相關應用。",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "期中指定考/15%，期中考/25%，期末指定考/15%，期末考/25%，平時/20%\n(僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "上課認真聽，並跟上老師的操作步驟，有問題當天問老師，老師喜歡認真上進的學生喔!",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "MATLAB文件說明 (PDF和線上)",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ],
                            "margin": "md"
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
                },{
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://s2.eslite.com/unsafe/fit-in/x900/s.eslite.com/Upload/Product/201909/o/637045653210310000.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#FFFFFF"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": ". NET程式設計",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": ". NET程式設計"
                        },
                        {
                            "type": "span",
                            "text": " (大一下選修)",
                            "size": "md"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "徐麗蘋",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "PPT + DEMO",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "以C#.net程式設計軟體為例, 讓初學程式設計之同學,能在windows介面環境中學習設計一般實用的功能之程式",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "重視出席，期中考，期末考，期末成果發表 (僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "多上機做練習，對提升程式能力很有幫助！語法、觀念可多參考書籍內容",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "新觀念microsoft Visual C# 程式設計範例教本(第五版) 陳會安(如上圖)",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ],
                            "margin": "md"
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
                },{
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://sl.bing.net/cRZK5JjqguG",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#9D9D9D"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "影像醫學 (大一下選修)",
                        "weight": "bold",
                        "size": "xl",
                        "wrap": True
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0,
                            "wrap": True
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "沈偉誌",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "PPT、電腦操作",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "margin": "md",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "透過理論講解與實務操作建立學生對醫學影像的基本概念",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "margin": "md",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "待確認 (僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "上課要認真聽，才能跟上老師講解的操作步驟！",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "無",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ],
                            "margin": "md"
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
                },{
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://sl.bing.net/cRZK5JjqguG",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#9D9D9D"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "智慧醫療概論",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": "智慧醫療概論"
                        },
                        {
                            "type": "span",
                            "text": " (大一下選修)",
                            "size": "md"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gray_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "沈偉誌",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "課堂講解",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "透過基本理論介紹，讓學生了解所需的學理基礎與資訊技術，為日後學習建構學習地圖",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "期末報告 (僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "老師在課堂上會提及一些與技術相關的專有名詞，若對智慧醫療有興趣，或已有自己的見解與想法，老師非常鼓勵課堂中積極與老師互動、討論。不過，如果對相關領域完全不熟悉，初學者可能會感到稍有難度，但事先建立基本概念，其實也能幫助未來更順利地跟上課程內容。",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "無",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
                },{
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://sl.bing.net/cRZK5JjqguG",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#9D9D9D"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": "疾病與診斷概論"
                        }
                        ]
                    },
                    {
                        "type": "text",
                        "text": " (大一下選修)",
                        "weight": "bold"
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gray_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "紀虹名",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "PPT + 講解",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "課程會簡介臨床常見疾病，疾病引發的生理與心理反應，以及診斷與評估的方式，並且閱讀最近10年醫學資訊應用相關的文獻。",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "出席/20%，書面報告/30% (1次)，口頭報告/50% (1次)\n(僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "無",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "老師課堂講義",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ],
                            "margin": "md"
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
                }
            ]
            }
            line_flex_str=json.dumps(line_flex_json) #新增的               
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_str))]
                )
            )
        #5
        if '大一下'in text and '必修' in text and '課' in text:
            line_flex_json={
                "type": "carousel",
                "contents": [
                    {
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://m.media-amazon.com/images/I/51fzy0l6mKL._AC_UF1000,1000_QL80_.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#DDDDDD"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "微積分",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": "微積分"
                        },
                        {
                            "type": "span",
                            "text": " (大一上、下必修)",
                            "size": "md"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gray_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "紀虹名",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "PPT (英文) + 板書",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "重要微積分觀念、定義和定理，輔以範例解釋計算方式和應用層面，包含函數、極限、導數、微分",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "出席/15%，隨堂考/25%，期中考/30%，期末考/30% (僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "多練習課本習題以及老師給的題目！",
                                "flex": 7,
                                "wrap": True,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "Applied Calculus for the Managerial Life and Social Sciences 10/e T. (如上圖)",
                                "flex": 7,
                                "size": "sm",
                                "wrap": True,
                                "color": "#000000"
                            }
                            ]
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
                },{
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS6N4n10G3Oz8CKMW5W6APWqf0jJyC13OQoMw&s",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#FFFFFF"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "物件導向程式設計一",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": "物件導向程式設計一"
                        }
                        ]
                    },
                    {
                        "type": "text",
                        "text": "(大一下必修)",
                        "weight": "bold"
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "李孝屏",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "PPT (中文)",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "主要介紹JAVA程式語言內容涵蓋：Java簡介、變數、運算子、從鍵盤讀取資料、條件分支、迴圈、陣列",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "書面報告/80%，期中考/10%，期末考/10% (僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "上課聽課，課後多練習",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "可參考老師提供的簡報，或其他相關書籍",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ],
                            "margin": "md"
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
                },{
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/068/79/0010687971.jpg&v=55dc43edk&w=348&h=348",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#FFFFFF"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "計算機組織與結構",
                        "size": "xl",
                        "weight": "bold"
                    },
                    {
                        "type": "text",
                        "text": " (大一下必修)",
                        "weight": "bold"
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "徐麗蘋",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "PPT + 板書",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "計算機組織與結構的概況，觀查電腦設計、檢視電腦之主元件及互連系統、檢視CPU的內部結構和組織、CPU的內部結構和微程式運作及平行組織等",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "重視出席，期中考，期末考 (僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "上課筆記很重要！要認真抄！",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "計算機組織與結構：效能設計 Stallings: Computer Organization and Architecture 9/E (如上圖)",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ],
                            "margin": "md"
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                    }
                    },{
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT9iiLOv3FWaZTMfD-I3Uk1xnAxZzFcjkdcow&s",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#DDDDDD"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "醫務管理概論",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": "醫務管理概論"
                        },
                        {
                            "type": "span",
                            "text": " (大一下必修)",
                            "size": "md"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "張啟昌",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "課本、PPT(英文)、小組討論與報告",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "向學生介紹組織理論和組織行為及其在醫療保健組織管理中的應用。以最新的組織理論和研究為基礎，探討如何將組織理論應用於現實世界中。",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "出席/10%，隨堂考/40%，書面報告/25%，口頭報告/25% (僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "要拿高分多練習考古題！考試可帶書，答案都會在課本或老師的PPT內找的到，此外，課堂上經常會有報告、小組討論",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "Management in Health Care Practice \nISBN: 978-89918-175-3\n(如上圖)",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
                },{
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://m.media-amazon.com/images/I/51N-+aF6zWL.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#DDDDDD"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "線性代數",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": "線性代數"
                        },
                        {
                            "type": "span",
                            "text": " (大一下必修)",
                            "size": "md"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gray_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "賴慶祥",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "PPT + 板書",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "線性的代數原理，以矩陣運算的方式處理線性方面的問題",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "出席15%；  作業 20% (每次10%)；  考試75% (每次25%)。合計 110%。\n分數調整標準：總分57-59 無缺席 & 無作業缺交，調整為 60。 (僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "作業認真寫，多練習課本習題非常有用！",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "DeFranza, J. & Gagliardi, D. (2009), Introduction to Linear Algebra with Applications, McGraw-Hill. (如上圖)",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                    }
                }
            ]
            }
            line_flex_str=json.dumps(line_flex_json) #新增的               
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_str))]
                )
            )
        #5
        if '大一下'in text and '選修' in text and '課' in text:
            line_flex_json={
                "type": "carousel",
                "contents": [
                    {
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://sl.bing.net/cRZK5JjqguG",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#9D9D9D"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "MATLAB程式設計",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": "MATLAB程式設計"
                        }
                        ]
                    },
                    {
                        "type": "text",
                        "text": " (大一下選修)",
                        "weight": "bold"
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gray_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "張炎清",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "全英文授課、電腦操作",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "學習MATLAB語言的基本語法，並以MATLAB來實踐機器學習和深度學習的相關應用。",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "期中指定考/15%，期中考/25%，期末指定考/15%，期末考/25%，平時/20%\n(僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "上課認真聽，並跟上老師的操作步驟，有問題當天問老師，老師喜歡認真上進的學生喔!",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "MATLAB文件說明 (PDF和線上)",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ],
                            "margin": "md"
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
                },{
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://s2.eslite.com/unsafe/fit-in/x900/s.eslite.com/Upload/Product/201909/o/637045653210310000.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#FFFFFF"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": ". NET程式設計",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": ". NET程式設計"
                        },
                        {
                            "type": "span",
                            "text": " (大一下選修)",
                            "size": "md"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "徐麗蘋",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "PPT + DEMO",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "以C#.net程式設計軟體為例, 讓初學程式設計之同學,能在windows介面環境中學習設計一般實用的功能之程式",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "重視出席，期中考，期末考，期末成果發表 (僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "多上機做練習，對提升程式能力很有幫助！語法、觀念可多參考書籍內容",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "新觀念microsoft Visual C# 程式設計範例教本(第五版) 陳會安(如上圖)",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ],
                            "margin": "md"
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
                },{
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://sl.bing.net/cRZK5JjqguG",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#9D9D9D"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "影像醫學 (大一下選修)",
                        "weight": "bold",
                        "size": "xl",
                        "wrap": True
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0,
                            "wrap": True
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "沈偉誌",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "PPT、電腦操作",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "margin": "md",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "透過理論講解與實務操作建立學生對醫學影像的基本概念",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "margin": "md",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "待確認 (僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "上課要認真聽，才能跟上老師講解的操作步驟！",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "無",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ],
                            "margin": "md"
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
                },{
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://sl.bing.net/cRZK5JjqguG",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#9D9D9D"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "智慧醫療概論",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": "智慧醫療概論"
                        },
                        {
                            "type": "span",
                            "text": " (大一下選修)",
                            "size": "md"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gray_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "沈偉誌",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "課堂講解",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "透過基本理論介紹，讓學生了解所需的學理基礎與資訊技術，為日後學習建構學習地圖",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "期末報告 (僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "老師在課堂上會提及一些與技術相關的專有名詞，若對智慧醫療有興趣，或已有自己的見解與想法，老師非常鼓勵課堂中積極與老師互動、討論。不過，如果對相關領域完全不熟悉，初學者可能會感到稍有難度，但事先建立基本概念，其實也能幫助未來更順利地跟上課程內容。",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "無",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
                },{
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://sl.bing.net/cRZK5JjqguG",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#9D9D9D"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": "疾病與診斷概論"
                        }
                        ]
                    },
                    {
                        "type": "text",
                        "text": " (大一下選修)",
                        "weight": "bold"
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gray_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "紀虹名",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "PPT + 講解",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "課程會簡介臨床常見疾病，疾病引發的生理與心理反應，以及診斷與評估的方式，並且閱讀最近10年醫學資訊應用相關的文獻。",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "出席/20%，書面報告/30% (1次)，口頭報告/50% (1次)\n(僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "無",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "老師課堂講義",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ],
                            "margin": "md"
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
                }
            ]
            }
            line_flex_str=json.dumps(line_flex_json) #新增的               
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_str))]
                )
            )


        #大一下必修
        if '微積分'in text:
            line_flex_json={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://m.media-amazon.com/images/I/51fzy0l6mKL._AC_UF1000,1000_QL80_.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#DDDDDD"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "微積分",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": "微積分"
                        },
                        {
                            "type": "span",
                            "text": " (大一上、下必修)",
                            "size": "md"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gray_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "紀虹名",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "PPT (英文) + 板書",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "重要微積分觀念、定義和定理，輔以範例解釋計算方式和應用層面，包含函數、極限、導數、微分",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "出席/15%，隨堂考/25%，期中考/30%，期末考/30% (僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "多練習課本習題以及老師給的題目！",
                                "flex": 7,
                                "wrap": True,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "Applied Calculus for the Managerial Life and Social Sciences 10/e T. (如上圖)",
                                "flex": 7,
                                "size": "sm",
                                "wrap": True,
                                "color": "#000000"
                            }
                            ]
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
            }
            line_flex_str=json.dumps(line_flex_json) #新增的               
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_str))]
                )
            )
        
        if "物件導向程式設計"in text:
            line_flex_json={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS6N4n10G3Oz8CKMW5W6APWqf0jJyC13OQoMw&s",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#FFFFFF"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "物件導向程式設計一",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": "物件導向程式設計一"
                        }
                        ]
                    },
                    {
                        "type": "text",
                        "text": "(大一下必修)",
                        "weight": "bold"
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "李孝屏",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "PPT (中文)",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "主要介紹JAVA程式語言內容涵蓋：Java簡介、變數、運算子、從鍵盤讀取資料、條件分支、迴圈、陣列",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "書面報告/80%，期中考/10%，期末考/10% (僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "上課聽課，課後多練習",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "可參考老師提供的簡報，或其他相關書籍",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ],
                            "margin": "md"
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
                }
            line_flex_str=json.dumps(line_flex_json) #新增的               
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_str))]
                )
            )
        
        if "計算機組織與結構"in text:
            line_flex_json={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/068/79/0010687971.jpg&v=55dc43edk&w=348&h=348",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#FFFFFF"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "計算機組織與結構",
                        "size": "xl",
                        "weight": "bold"
                    },
                    {
                        "type": "text",
                        "text": " (大一下必修)",
                        "weight": "bold"
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "徐麗蘋",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "PPT + 板書",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "計算機組織與結構的概況，觀查電腦設計、檢視電腦之主元件及互連系統、檢視CPU的內部結構和組織、CPU的內部結構和微程式運作及平行組織等",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "重視出席，期中考，期末考 (僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "上課筆記很重要！要認真抄！",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "計算機組織與結構：效能設計 Stallings: Computer Organization and Architecture 9/E (如上圖)",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ],
                            "margin": "md"
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
            }
            line_flex_str=json.dumps(line_flex_json) #新增的               
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_str))]
                )
            )
        
        if "醫務管理概論"in text:
            line_flex_json={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT9iiLOv3FWaZTMfD-I3Uk1xnAxZzFcjkdcow&s",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#DDDDDD"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "醫務管理概論",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": "醫務管理概論"
                        },
                        {
                            "type": "span",
                            "text": " (大一下必修)",
                            "size": "md"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "張啟昌",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "課本、PPT(英文)、小組討論與報告",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "向學生介紹組織理論和組織行為及其在醫療保健組織管理中的應用。以最新的組織理論和研究為基礎，探討如何將組織理論應用於現實世界中。",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "出席/10%，隨堂考/40%，書面報告/25%，口頭報告/25% (僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "要拿高分多練習考古題！考試可帶書，答案都會在課本或老師的PPT內找的到，此外，課堂上經常會有報告、小組討論",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "Management in Health Care Practice \nISBN: 978-89918-175-3\n(如上圖)",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
                }
            line_flex_str=json.dumps(line_flex_json) #新增的               
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_str))]
                )
            )
        
        if "線性代數"in text:
            line_flex_json={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://m.media-amazon.com/images/I/51N-+aF6zWL.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#DDDDDD"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "線性代數",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": "線性代數"
                        },
                        {
                            "type": "span",
                            "text": " (大一下必修)",
                            "size": "md"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gray_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "賴慶祥",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "PPT + 板書",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "線性的代數原理，以矩陣運算的方式處理線性方面的問題",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "出席15%；  作業 20% (每次10%)；  考試75% (每次25%)。合計 110%。\n分數調整標準：總分57-59 無缺席 & 無作業缺交，調整為 60。 (僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "作業認真寫，多練習課本習題非常有用！",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "DeFranza, J. & Gagliardi, D. (2009), Introduction to Linear Algebra with Applications, McGraw-Hill. (如上圖)",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
            }
            line_flex_str=json.dumps(line_flex_json) #新增的               
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_str))]
                )
            )
        
        #大一下選修
        if "matlab"in text:
            line_flex_json={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://sl.bing.net/cRZK5JjqguG",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#9D9D9D"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "MATLAB程式設計",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": "MATLAB程式設計"
                        }
                        ]
                    },
                    {
                        "type": "text",
                        "text": " (大一下選修)",
                        "weight": "bold"
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gray_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "張炎清",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "全英文授課、電腦操作",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "學習MATLAB語言的基本語法，並以MATLAB來實踐機器學習和深度學習的相關應用。",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "期中指定考/15%，期中考/25%，期末指定考/15%，期末考/25%，平時/20%\n(僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "上課認真聽，並跟上老師的操作步驟，有問題當天問老師，老師喜歡認真上進的學生喔!",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "MATLAB文件說明 (PDF和線上)",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ],
                            "margin": "md"
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
            }
            line_flex_str=json.dumps(line_flex_json) #新增的               
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_str))]
                )
            )
        
        if ".net"in text:
            line_flex_json={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://s2.eslite.com/unsafe/fit-in/x900/s.eslite.com/Upload/Product/201909/o/637045653210310000.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#FFFFFF"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": ". NET程式設計",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": ". NET程式設計"
                        },
                        {
                            "type": "span",
                            "text": " (大一下選修)",
                            "size": "md"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "徐麗蘋",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "PPT + DEMO",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "以C#.net程式設計軟體為例, 讓初學程式設計之同學,能在windows介面環境中學習設計一般實用的功能之程式",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "重視出席，期中考，期末考，期末成果發表 (僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "多上機做練習，對提升程式能力很有幫助！語法、觀念可多參考書籍內容",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "新觀念microsoft Visual C# 程式設計範例教本(第五版) 陳會安(如上圖)",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ],
                            "margin": "md"
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
            }
            line_flex_str=json.dumps(line_flex_json) #新增的               
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_str))]
                )
            )
        
        if "影像醫學"in text:
            line_flex_json={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://sl.bing.net/cRZK5JjqguG",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#9D9D9D"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "影像醫學 (大一下選修)",
                        "weight": "bold",
                        "size": "xl",
                        "wrap": True
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0,
                            "wrap": True
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "沈偉誌",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "PPT、電腦操作",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "margin": "md",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "透過理論講解與實務操作建立學生對醫學影像的基本概念",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "margin": "md",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "待確認 (僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "上課要認真聽，才能跟上老師講解的操作步驟！",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "無",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ],
                            "margin": "md"
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
            }
            line_flex_str=json.dumps(line_flex_json) #新增的               
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_str))]
                )
            )
        
        if "智慧醫療概論"in text:
            line_flex_json={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://sl.bing.net/cRZK5JjqguG",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#9D9D9D"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "智慧醫療概論",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": "智慧醫療概論"
                        },
                        {
                            "type": "span",
                            "text": " (大一下選修)",
                            "size": "md"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gray_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "沈偉誌",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "課堂講解",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "透過基本理論介紹，讓學生了解所需的學理基礎與資訊技術，為日後學習建構學習地圖",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "期末報告 (僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "老師在課堂上會提及一些與技術相關的專有名詞，若對智慧醫療有興趣，或已有自己的見解與想法，老師非常鼓勵課堂中積極與老師互動、討論。不過，如果對相關領域完全不熟悉，初學者可能會感到稍有難度，但事先建立基本概念，其實也能幫助未來更順利地跟上課程內容。",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "無",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
                }
            line_flex_str=json.dumps(line_flex_json) #新增的               
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_str))]
                )
            )
        
        if "疾病與診斷概論"in text:
            line_flex_json={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://sl.bing.net/cRZK5JjqguG",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#9D9D9D"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": "疾病與診斷概論"
                        }
                        ]
                    },
                    {
                        "type": "text",
                        "text": " (大一下選修)",
                        "weight": "bold"
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gray_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "紀虹名",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "PPT + 講解",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "課程會簡介臨床常見疾病，疾病引發的生理與心理反應，以及診斷與評估的方式，並且閱讀最近10年醫學資訊應用相關的文獻。",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "出席/20%，書面報告/30% (1次)，口頭報告/50% (1次)\n(僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "無",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "老師課堂講義",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ],
                            "margin": "md"
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
                }
            line_flex_str=json.dumps(line_flex_json) #新增的               
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_str))]
                )
            )

        #大一上必修(還有微積分)
        if "管理學"in text:
            line_flex_json={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/085/75/0010857557.jpg&v=5eb1402ak&w=375&h=375",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#DDDDDD"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "管理學",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": "管理學"
                        },
                        {
                            "type": "span",
                            "text": " (大一上必修)",
                            "size": "md"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gray_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "張啟昌",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "課本、PPT(英文)、小組討論與報告",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "向學生介紹管理人員的角色和職能，內容包括組織介紹以及管理的必要性和性質。對管理四項職能進行詳細調查：計劃和決策、組織、領導和激勵以及控制",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "出席/12%，隨堂考/48%，書面報告/20%，口頭報告/20% (僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "考試若要拿高分可多參考考古題！課程會經常報告，要好好準備！",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "Stephen P. Robbins., David De Cenzo, and Mary Coulter (2020) Fundamentals of Management (GE) 11/e  (如上圖)",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
                }
            line_flex_str=json.dumps(line_flex_json) #新增的               
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_str))]
                )
            )
        
        if "醫學資訊概論"in text:
            line_flex_json={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/092/21/0010922111.jpg&v=6256a679k&w=348&h=348",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#FFFFFF"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "醫學資訊概論",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": "醫學資訊概論"
                        },
                        {
                            "type": "span",
                            "text": " (大一上必修)",
                            "size": "md"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "徐麗蘋",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "PPT + 板書",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "深入介紹電腦之運作和組織，了解電腦且具有對新軟硬體變化的學習潛能，介紹資訊趨勢之相關知識，介紹資訊應用於醫學方面之知識與相關系統概念",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "重視出席，期中考，期末考 (僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "上課筆記很重要，要認真抄！",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "最新計算機概論 陳惠貞\n(如上圖)",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ],
                            "margin": "md"
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
                }
            line_flex_str=json.dumps(line_flex_json) #新增的               
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_str))]
                )
            )
        
        #大一上選修
        if "管理數學"in text:
            line_flex_json={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://cdn.cybassets.com/media/W1siZiIsIjI1OTY2L3Byb2R1Y3RzLzQzNTM4MjI5LzE3MDE2Njk4MTlfZTVkZmZhYTBkYzQ3NTM3MzVlNTguanBlZyJdLFsicCIsInRodW1iIiwiMjA0OHgyMDQ4Il1d.jpeg?sha=8dd42d25e0624747",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#DDDDDD"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "管理數學",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": "管理數學"
                        },
                        {
                            "type": "span",
                            "text": " (大一上選修)",
                            "size": "md"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gray_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "賴慶祥",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "PPT + 板書",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "(1)線性模式的基礎理論\n(2)單形法之運算及線性模式在管理上的應用\n(3)以線性模式解決各類問題的建模及求解\n(4)線性模式在管理上所扮演的重要角色。",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "出席10%，作業依題數每題1%。考試每次25%，缺席每次扣1分。總分55-59者調整為60 (限無缺席且無缺交作業者)。 (僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "作業認真寫，多練習課本習題很有用！",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "作業研究(第十五版)\n [廖經芳譯(Anderson)] 9789579282901 (如上圖)",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
            }
            line_flex_str=json.dumps(line_flex_json) #新增的               
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_str))]
                )
            )
        
        if "c"in text:
            line_flex_json={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcRorZN0iYrXosREGfzmKefupIkvbwwrrux8p7zX9AOmm3COEkxVZIiTKybmPUYypJPIHDq0386cMGYHq2icN-iO0Z2q5woabyrT0F2NHFtv6HucaDXmrN9J3w&usqp=CAc",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#DDDDDD"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "C語言",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": "C語言"
                        },
                        {
                            "type": "span",
                            "text": " (大一上選修)",
                            "size": "md"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gray_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "張炎清",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "課本、電腦操作",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "C 程式語言教學，全英授課",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "期中指定考/15%，期中考/25%，期末指定考/15%，期末考/25%，平時/20% \n(僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "上課認真聽，有問題當天下課問老師，只要有認真上課就可以PASS!! 若英文、程式能力較弱，建議可以先找中文書進行預習，這樣上課時會比較有個概念且容易理解！",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "C HOW TO PROGRAM\n(如上圖)",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ],
                            "margin": "md"
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
            }
            line_flex_str=json.dumps(line_flex_json) #新增的               
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_str))]
                )
            )
        
        if "醫療數位孿生概論"in text:
            line_flex_json={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://sl.bing.net/cRZK5JjqguG",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#9D9D9D"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "醫療數位孿生概論",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": "醫療數位孿生概論"
                        }
                        ]
                    },
                    {
                        "type": "text",
                        "text": " (大一上選修)",
                        "weight": "bold"
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "張啟昌",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "課本、PPT(英文)、小組討論與報告",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "概述數位醫學孿生技術的最新發展，使學生能夠深入了解健康個體或患者產生的健康和醫療數據，並強調該技術在醫療保健領域的重要性。",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "隨堂考/20%，書面報告/40%，口頭報告/40% (僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "無",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "無",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
                }
            line_flex_str=json.dumps(line_flex_json) #新增的               
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_str))]
                )
            )
        
        if "健康資訊輔具概論"in text: 
            line_flex_json={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "backgroundColor": "#DDDDDD",
                    "url": "https://sl.bing.net/cRZK5JjqguG"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "健康資訊輔具概論",
                        "weight": "bold",
                        "size": "xl",
                        "contents": [
                        {
                            "type": "span",
                            "text": "健康資訊輔具概論"
                        }
                        ]
                    },
                    {
                        "type": "text",
                        "text": " (大一上選修)",
                        "weight": "bold"
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "學分數",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課老師",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "李孝屏",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授課方式",
                                "color": "#aaaaaa",
                                "flex": 3,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "PPT講解",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "課程內容",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "將教導學生了解身心障礙者與老年人在資訊取得方面的困難、可應用於解決問題的資訊技術以及資訊輔助系統的現況與未來發展。",
                                "wrap": True,
                                "color": "#000000",
                                "size": "sm",
                                "flex": 7
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "評分方式",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3,
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "書面報告/50%，口頭報告/50% (僅供參考)",
                                "size": "sm",
                                "flex": 7,
                                "wrap": True,
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "學長姐建議",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 3
                            },
                            {
                                "type": "text",
                                "text": "讀熟老師上課PPT",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000"
                            }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "參考書目",
                                "flex": 3,
                                "size": "sm",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": "老師的PPT",
                                "flex": 7,
                                "size": "sm",
                                "color": "#000000",
                                "wrap": True
                            }
                            ]
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "課程綱要查詢",
                        "uri": "https://student.csmu.edu.tw/guest/NoneLogon1.aspx"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
                }
            line_flex_str=json.dumps(line_flex_json) #新增的               
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_str))]
                )
            )
        
        else:
            line_bot_api.reply_message_with_http_info(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="感謝您的訊息！\n非常抱歉，本系統無法理解您的訊息><\n建議多使用以下的圖文選單進行詢問或是輸入關鍵字詞哦！")]
                )
            )

        
if __name__ == "__main__":
    app.run(debug=True, threaded=True) 