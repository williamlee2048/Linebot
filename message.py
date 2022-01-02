main_menu = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/lFq9NTg.jpg",
        "size": "full",
        "aspectMode": "fit",
        "aspectRatio": "1.25:1"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "進入State1",
              "text": "go to state1"
            },
            "height": "md",
            "color": "#ff9900",
            "style": "primary"
          },          
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "進入State2",
              "text": "go to state2"
            },
            "height": "md",
            "color": "#ff9900",
            "style": "primary"
          },          
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "進入字卡",
              "text": "wordcard"
            },
            "height": "md",
            "color": "#ff9900",
            "style": "primary"
          },          
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "顯示單字表",
              "text": "wordlist"
            },
            "height": "md",
            "color": "#ff9900",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    }
  ]
}

user_menu = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "開始進入主選單吧！",
            "weight": "bold",
            "align": "center",
            "size": "lg"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "GOGO",
              "text": "menu"
            },
            "height": "md",
            "color": "#00d66c",
            "style": "primary"
          },
        {
            "type": "button",
            "action": {
              "type": "message",
              "label": "先不要",
              "text": "先不要"
            },
            "height": "md",
            "color": "#00d66c",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    }
  ]
}

GA_menu = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "我勸你是不要皮喔",
            "weight": "bold",
            "align": "center",
            "size": "lg"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "對不起",
              "text": "menu"
            },
            "height": "md",
            "color": "#00d66c",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    }
  ]
}

test_package = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "鬼吧",
            "weight": "bold",
            "align": "center",
            "size": "lg"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "Ghostlike",
              "text": "menu"
            },
            "height": "md",
            "color": "#00d66c",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    }
  ]
}

wordcard_interface = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "字卡說明  1.要記錄的字  2.定義",
            "weight": "bold",
            "align": "center",
            "size": "lg"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "Start",
              "text": "wordsave_activate"
            },
            "height": "md",
            "color": "#00d66c",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    }
  ]
}

Saving_End = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "完成紀錄，即將返回Menu",
            "weight": "bold",
            "align": "center",
            "size": "lg"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "返回菜單",
              "text": "menu"
            },
            "height": "md",
            "color": "#00d66c",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    }
  ]
}