from limbus.requests import Cs, ReqNull
from limbus.responses import Sc, RspGetTermsOfUseStateAll
from limbus.formats import TermsOfUseState, TERMSOFUSE_STATE


async def handle(req: Cs[ReqNull]):
    state = TermsOfUseState(
        uid=req.userAuth.uid,
        version=1,
        state=TERMSOFUSE_STATE.AGREE,
    )
    rsp = RspGetTermsOfUseStateAll(version=1, termsOfUseStateList=[state])

    return Sc[RspGetTermsOfUseStateAll](result=rsp)
