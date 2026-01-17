import requests


def GetBiliBili(url, name):
    headers = {
        "Cookie": "buvid3=0FDA4820-6409-2578-67F7-74953ECD164866001infoc; b_nut=1768631066; b_lsid=2178F5410_19BCAA07003; bsource=search_bing; _uuid=CFDA10E76-E7D1-EBEA-BACB-4E9C106D7BD7B70744infoc; buvid_fp=73f08c51ff588abb7f73b24f5fb84f62; bmg_af_switch=1; bmg_src_def_domain=i0.hdslb.com; home_feed_column=5; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Njg4OTAyNzUsImlhdCI6MTc2ODYzMTAxNSwicGx0IjotMX0.3N43AXAbryylw7Lzb8EVvF8cB1Y-ZM8Ayws-3hpunq8; bili_ticket_expires=1768890215; buvid4=A355F05D-1A43-6CDE-DD16-FA74988FF87875808-026011714-yrcRy8RkASrdxUnEjdl2Iw%3D%3D; SESSDATA=d908ad92%2C1784183101%2C1f4f3%2A11CjBvY0qKdCXNA1g7nKrCT7J2BrRzjRJDtcH7Ee7HSCs34VTm2dTlJOAZV2T6xTt7hbUSVk9VQzE0OHowVEZMR1pwSVU0bFdncDdEaTRidEs1NFE0ODNwdVQ5cEY5U0t6SmRiUXVYMGdVZnhXQjdNN0tETkhCNkF2b0p1MUE2cVdvbzlnQ2dhMkFBIIEC; bili_jct=1890102b05562fb4831fe46bb593b028; DedeUserID=3493094756452662; DedeUserID__ckMd5=5b9e35bbe670dc9b; sid=pnr37vlh; browser_resolution=1536-340",
        "Referer": "https://www.bilibili.com/video/BV1MEeJzrE9j/?spm_id_from=333.1391.0.0&vd_source=03b66f43059f5c88221eded30a651db1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
    }
    resp = requests.get(url, headers=headers)
    with open(f'{name}.mp4', 'wb') as f:
        f.write(resp.content)
    print("爬取好啦！请在c盘用户页面查收")


GetBiliBili(url=input("输入想要爬取b站上的视频所在url~:"), name=input("输入想要爬取b站上的视频的名字~:"))
