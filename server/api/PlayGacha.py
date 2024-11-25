from limbus.requests import Cs, ReqPlayGacha
from limbus.responses import Sc, RspPlayGacha
from limbus.formats import GachaLogDetail, STR_ELEMENT_TYPE, ELEMENT_TYPE, Element
from resources.parser.gacha.data import fetch_random_gacha_element_ids


async def handle(req: Cs[ReqPlayGacha]):
    gacha_id = req.parameters.gachaId
    payment_id = req.parameters.paymentId
    
    # Current implementation isn't scalable
    # A good implementation lets you decide chances for each banner and shit
    # But idgaf
    # This is also currently hardcoded to only pull personalities
    # Go fork and impl a better one yourself if you want to say
    # that the code is shit (i agree tho btw)
    # Oh and, currently doesn't do anything with the DB or Ideality
    # Should be easy to do, but I'm not gonna bother
    ids = fetch_random_gacha_element_ids(id=gacha_id, payment_id=payment_id)

    gacha_log_details = []

    for element_id in ids:
        gacha_log_detail = GachaLogDetail(
            type=STR_ELEMENT_TYPE.PERSONALITY,
            _type=ELEMENT_TYPE.PERSONALITY,
            id=element_id,
            # One of these returns the shards
            # in scenarios where u get dupes.
            # Too lazy to check which one does.
            ex=Element(),
            origin=Element(),
        )
        gacha_log_details.append(gacha_log_detail)

    return Sc[RspPlayGacha](result=RspPlayGacha(gachaLogDetails=gacha_log_details))
