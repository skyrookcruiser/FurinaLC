from limbus.requests import Cs, ReqNull
from limbus.responses import Sc, RspNull
from limbus.formats import SynchronizedFormat, NoticeFormat, UpdatedFormat


async def handle(req: Cs[ReqNull]):
    notice_ps = NoticeFormat(
        id=200001,
        version=219,
        type=0,
        startDate="2023-01-01T00:00:00.000Z",
        endDate="2098-12-31T21:00:00.000Z",
        sprNameList=["200001"],
        title_EN="Welcome to FurinaLC",
        content_EN=r"""
        {
            "list": [
                {
                    "formatKey": "Text",
                    "formatValue": "Greetings, Dear Manager. Have fun playing in this private server."
                },
                {
                    "formatKey": "SubTitle",
                    "formatValue": "<Official Discord>"
                },
                {
                    "formatKey": "Text",
                    "formatValue": "League of Littérateurs"
                },
                {
                    "formatKey": "HyperLink",
                    "formatValue": "https://discord.gg/invite/fqGyDdSx"
                }
            ]
        }
        """,
        title_KR="Welcome to FurinaLC",
        content_KR=r"""
        {
            "list": [
                {
                    "formatKey": "Text",
                    "formatValue": "Greetings, Dear Manager. Have fun playing in this private server."
                },
                {
                    "formatKey": "SubTitle",
                    "formatValue": "<Official Discord>"
                },
                {
                    "formatKey": "Text",
                    "formatValue": "League of Littérateurs"
                },
                {
                    "formatKey": "HyperLink",
                    "formatValue": "https://discord.gg/invite/fqGyDdSx"
                }
            ]
        }
        """,
        title_JP="Welcome to FurinaLC",
        content_JP=r"""
        {
            "list": [
                {
                    "formatKey": "Text",
                    "formatValue": "Greetings, Dear Manager. Have fun playing in this private server."
                },
                {
                    "formatKey": "SubTitle",
                    "formatValue": "<Official Discord>"
                },
                {
                    "formatKey": "Text",
                    "formatValue": "League of Littérateurs"
                },
                {
                    "formatKey": "HyperLink",
                    "formatValue": "https://discord.gg/invite/fqGyDdSx"
                }
            ]
        }
        """,
    )

    sync = SynchronizedFormat(version=513, noticeList=[notice_ps])

    return Sc[RspNull](
        updated=UpdatedFormat(isInitialized=True),
        synchronized=sync,
        result=None,
    )
