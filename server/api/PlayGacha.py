from limbus.requests import Cs, ReqPlayGacha
from limbus.responses import Sc, RspPlayGacha
from limbus.formats import GachaLogDetail, STR_ELEMENT_TYPE, ELEMENT_TYPE, Element


# RECV:     {"userAuth":{"uid":1,"dbid":0,"authCode":"furinalc","version":"1.63.1","synchronousDataVersion":521},"parameters":{"gachaId":199,"paymentId":3}}
# SEND:     {"detail":"Not Found"}


async def handle(req: Cs[ReqPlayGacha]):
    return Sc[RspPlayGacha](
        result=RspPlayGacha(
            # this contains what we get from the gacha
            gachaLogDetails=[
                GachaLogDetail(
                    # in this example, we're simply returning
                    # a singular yisang
                    type=STR_ELEMENT_TYPE.PERSONALITY,
                    _type=ELEMENT_TYPE.PERSONALITY,
                    id=10101,
                    # one of these things is for
                    # giving shards when you
                    # get dupes
                    ex=Element(),
                    origin=Element(),
                )
            ]
        )
    )
