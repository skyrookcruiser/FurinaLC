from limbus.requests import Cs, ReqNull
from limbus.responses import Sc, RspNull
from limbus.formats import SynchronizedFormat, NoticeFormat
from server.config import CUSTOM_NOTICE

FURINA_NOTICE_TITLE = "Welcome to FurinaLC"
FURINA_NOTICE_CONTENT = r"""
{
    "list": [
        {
            "formatKey": "SubTitle",
            "formatValue": "<FurinaLC>"
        },
        {
            "formatKey": "Text",
            "formatValue": "Greetings, Dear manager. Have fun playing in this private server."
        },
        {
            "formatKey": "HyperLink",
            "formatValue": "https://github.com/LEAGUE-OF-NINE/FurinaLC/"
        },
        {
            "formatKey": "SubTitle",
            "formatValue": "<Credits>"
        },
        {
            "formatKey": "Text",
            "formatValue": "Private Server Developer: Yulian"
        },
        {
            "formatKey": "Text",
            "formatValue": "Middleware Encryption: League of Nine"
        }
    ]
}
"""


async def handle(req: Cs[ReqNull]):
    if CUSTOM_NOTICE:
        notice_ps = NoticeFormat(
            id=200001,
            version=219,
            type=0,
            startDate="2023-01-01T00:00:00.000Z",
            endDate="2098-12-31T21:00:00.000Z",
            sprNameList=["200001"],
            title_EN=FURINA_NOTICE_TITLE,
            content_EN=FURINA_NOTICE_CONTENT,
            title_KR=FURINA_NOTICE_TITLE,
            content_KR=FURINA_NOTICE_CONTENT,
            title_JP=FURINA_NOTICE_TITLE,
            content_JP=FURINA_NOTICE_CONTENT,
        )

        sync = SynchronizedFormat(version=513, noticeList=[notice_ps])

        return Sc[RspNull](synchronized=sync, result=RspNull())
    else:
        return Sc[RspNull](result=RspNull())
