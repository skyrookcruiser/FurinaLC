from enum import IntEnum, StrEnum
from pydantic import BaseModel
from typing import List, Optional


class MISSION_CATEGORY(IntEnum):
    NONE = 0
    EVENT_NEWYEAR_2024_NORMAL = 1
    EVENT_NEWYEAR_2024_HARD = 2
    EVENT_NEWYEAR_2024_COMMON = 3
    EVENT_WALPU3_NORMAL = 4
    EVENT_WALPU3_HARD = 5
    EVENT_WALPU3_COMMON = 6
    EVENT_WALPU4_NORMAL = 7
    EVENT_WALPU4_HARD = 8
    EVENT_WALPU4_COMMON = 9
    NEWBIE = 90000001
    RETURN = 90000101
    UNRECOGNIZED = -1


class MISSION_CONDITION_TYPE(IntEnum):
    NONE = 0
    KILL_ENEMY_ONCE_BATTLE = 1
    CLEAR_ALIVE_ALL = 2
    CLEAR_EQUANNIMITY_ALL = 3
    KILL_ENEMY_ONCE_ATTACK_SKILL = 4
    TL_DAMAGE_ATTACK_SKILL = 5
    MISSION_ALL_CLEAR = 6
    KILL_ENEMY_COUNT_BY_ATTACK_SKILL = 7
    CLEAR = 8
    CLEAR_WITHIN_TURN = 9
    CLEAR_WITHOUT_KILLED_ENEMY_BY_ENEMY = 10
    ENEMY_KILLED_BY_ENEMY = 11
    ENEMY_KILLED_BY_ENEMY_WITHIN_ONE_TURN = 12
    ENEMY_NEGATIVE_SINBUFFED = 13
    ENEMY_KILLED_BY_NEGAIVE_SINBUFF = 14
    ENEMY_KILLED_BY_PLAYER_WITH_BUFF = 15
    ENEMY_SKILL_NOTUSED = 16
    ENEMY_DAMAGED_COUNT_BY_NEGATIVE_SINBUFF = 17
    ENEMY_KILLED_BY_ONE_SKILL_HP_RATIO_80 = 18
    ENEMY_NEGATIVE_BUFFED_ONE_TURN = 19
    ENEMY_MULTIKILLED_ONE_TURN = 20
    ENEMY_KILLED_BY_PARTICIPANT_ORDER = 21
    ENEMY_KILLED_ALL = 22
    USE_PERSONALITY_ATKTYPE = 10000001
    USE_PERSONALITY_SKILL = 10000002
    USE_PERSONALITY_DEFENSE_SKILL = 10000003
    USE_EGO_SKILL = 10000004
    USE_FRIEND_SUPPORT = 10000005
    CHECK_BATTLE_PASS = 10000006
    CHECK_PASSIVE_SKILL = 10000007
    STAGE_CLEAR = 10000008
    ACQUIRE_STAGE_PROGRESS_REWARD = 10000009
    PERSONALITY_LEVEL_UP = 10000010
    PERSONALITY_GACKSUNG = 10000011
    EGO_GACKSUNG = 10000012
    USER_LEVEL_UP = 10000013
    ACQUIRE_PERSONALITY = 10000014
    ACQUIRE_EGO = 10000015
    GACHA = 10000016
    BATTLE_PASS_MISSION_CLEAR = 10000017
    PURCHASE_ENKEPHALINE_MODULE = 10000018
    CONSUME_ENKEPHALINE = 10000019
    UPDATE_USER_PROFILE = 10000020
    LUXCAVATION_DUNGEON_CLEAR = 10000021
    LUXCAVATION_DUNGEON_SKIP = 10000022
    EXP_DUNGEON_CLEAR = 10000023
    EXP_DUNGEON_SKIP = 10000024
    THREAD_DUNGEON_CLEAR = 10000025
    THREAD_DUNGEON_SKIP = 10000026
    MIRROR_DUNGEON_ENTER = 10000027
    MIRROR_DUNGEON_CLEAR_NODE = 10000028
    MIRROR_DUNGEON_CLEAR = 10000029
    RAILWAY_DUNGEON_ENTER = 10000030
    RAILWAY_DUNGEON_CLEAR_NODE = 10000031
    RAILWAY_DUNGEON_CLEAR = 10000032
    USE_ITEM = 10000033
    UPDATE_FORMATION = 10000034
    EXCHANGE_TWINE = 10000035
    VENDING_MACHINE = 10000036
    NEW_USER = 10000037
    RETURN_USER = 10000038
    BATTLE_PASS_LEVEL_UP = 10000039
    UNRECOGNIZED = -1


class MISSION_STATE(IntEnum):
    NONE = 0
    OPENED = 1
    ACHIEVED = 2
    REWARDED = 3
    UNRECOGNIZED = -1


class DANTE_ABILITY_CATEGORY(IntEnum):
    DEFAULT = 0
    RAILWAY_DUNGEON = 1
    UNRECOGNIZED = -1


class ELEMENT_TYPE(IntEnum):
    NONE = -1
    ITEM = 0
    EXP = 1
    CHARACTER = 2
    PERSONALITY = 3
    EGO = 4
    STAMINA = 5
    BATTLEPASS_POINT = 6
    ELEMENT_VENDING_MACHINE = 7
    ANNOUNCER = 8
    EGO_GIFT = 9
    ELEMENT_GACHA = 10
    USERBANNER = 11
    VENDING_MACHINE_PERSONALITY = 12
    VENDING_MACHINE_CHARACTER = 13
    SEASONAL_R_BOX = 14
    SEASONAL_O_BOX = 15
    SEASONAL_PIECE = 16
    SEASONAL_GLOBAL_GROWTH_PIECE = 17
    EVENT_ITEM = 18
    USER_TICKET_DECO_LEFT = 19
    USER_TICKET_DECO_RIGHT = 20
    USER_TICKET_DECO_EGOBG = 21
    USER_TICKET_DECO_FOR_UI = 22
    MIRRORDUNGEON_COST = 23
    UNLOCK_CODE = 24
    CHANCE = 25
    UNRECOGNIZED = -1


class STR_ELEMENT_TYPE(StrEnum):
    NONE = "NONE"
    ITEM = "ITEM"
    EXP = "EXP"
    CHARACTER = "CHARACTER"
    PERSONALITY = "PERSONALITY"
    EGO = "EGO"
    STAMINA = "STAMINA"
    BATTLEPASS_POINT = "BATTLEPASS_POINT"
    ELEMENT_VENDING_MACHINE = "ELEMENT_VENDING_MACHINE"
    ANNOUNCER = "ANNOUNCER"
    EGO_GIFT = "EGO_GIFT"
    ELEMENT_GACHA = "ELEMENT_GACHA"
    USERBANNER = "USERBANNER"
    VENDING_MACHINE_PERSONALITY = "VENDING_MACHINE_PERSONALITY"
    VENDING_MACHINE_CHARACTER = "VENDING_MACHINE_CHARACTER"
    SEASONAL_R_BOX = "SEASONAL_R_BOX"
    SEASONAL_O_BOX = "SEASONAL_O_BOX"
    SEASONAL_PIECE = "SEASONAL_PIECE"
    SEASONAL_GLOBAL_GROWTH_PIECE = "SEASONAL_GLOBAL_GROWTH_PIECE"
    EVENT_ITEM = "EVENT_ITEM"
    USER_TICKET_DECO_LEFT = "USER_TICKET_DECO_LEFT"
    USER_TICKET_DECO_RIGHT = "USER_TICKET_DECO_RIGHT"
    USER_TICKET_DECO_EGOBG = "USER_TICKET_DECO_EGOBG"
    USER_TICKET_DECO_FOR_UI = "USER_TICKET_DECO_FOR_UI"
    MIRRORDUNGEON_COST = "MIRRORDUNGEON_COST"
    UNLOCK_CODE = "UNLOCK_CODE"
    CHANCE = "CHANCE"
    UNRECOGNIZED = "UNRECOGNIZED"


class LinkAuthState(IntEnum):
    OK = 0
    INVALID = 1
    GUEST_USER = 2
    TRY_COUNT = 3
    ACCOUNT = 4
    UNRECOGNIZED = -1


class TERMSOFUSE_STATE(IntEnum):
    NONE = 0
    AGREE = 1
    DISAGREE = 2
    UNRECOGNIZED = -1


class MIRRORDUNGEON_EGOGIFT_KEYWORD(IntEnum):
    NONE = 0
    Combustion = 1
    Laceration = 2
    Vibration = 3
    Burst = 4
    Sinking = 5
    Breath = 6
    Charge = 7
    Slash = 8
    Penetrate = 9
    Hit = 10
    Random = 11
    UNRECOGNIZED = -1


class MIRRORDUNGEON_EGOGIFT_TAG(IntEnum):
    NONE = -1
    NORMAL = 0
    START = 1
    FLOORBOSS = 2
    TIER_1 = 3
    TIER_2 = 4
    TIER_3 = 5
    TIER_4 = 6
    TIER_5 = 7
    NO_SALE = 8
    EXTRA = 9
    EXTRA_TIER1 = 10
    EXTRA_TIER2 = 11
    EXTRA_TIER3 = 12
    EXTRA_TIER4 = 13
    UNRECOGNIZED = -1


class STR_MIRRORDUNGEON_EGOGIFT_KEYWORD(StrEnum):
    NONE = "NONE"
    Combustion = "Combustion"
    Laceration = "Laceration"
    Vibration = "Vibration"
    Burst = "Burst"
    Sinking = "Sinking"
    Breath = "Breath"
    Charge = "Charge"
    Slash = "Slash"
    Penetrate = "Penetrate"
    Hit = "Hit"
    Random = "Random"
    UNRECOGNIZED = "UNRECOGNIZED"


class STR_MIRRORDUNGEON_EGOGIFT_TAG(StrEnum):
    NONE = "NONE"
    NORMAL = "NORMAL"
    START = "START"
    FLOORBOSS = "FLOORBOSS"
    TIER_1 = "TIER_1"
    TIER_2 = "TIER_2"
    TIER_3 = "TIER_3"
    TIER_4 = "TIER_4"
    TIER_5 = "TIER_5"
    NO_SALE = "NO_SALE"
    EXTRA = "EXTRA"
    EXTRA_TIER1 = "EXTRA_TIER1"
    EXTRA_TIER2 = "EXTRA_TIER2"
    EXTRA_TIER3 = "EXTRA_TIER3"
    EXTRA_TIER4 = "EXTRA_TIER4"
    UNRECOGNIZED = "UNRECOGNIZED"


class EGO_TYPE(IntEnum):
    ZAYIN = 0
    TETH = 1
    HE = 2
    WAW = 3
    ALEPH = 4
    UNRECOGNIZED = -1


class STR_EGO_TYPE(StrEnum):
    ZAYIN = "ZAYIN"
    TETH = "TETH"
    HE = "HE"
    WAW = "WAW"
    ALEPH = "ALEPH"
    UNRECOGNIZED = "UNRECOGNIZED"


class ATTRIBUTE_TYPE(IntEnum):
    CRIMSON = 0
    SCARLET = 1
    AMBER = 2
    SHAMROCK = 3
    AZURE = 4
    INDIGO = 5
    VIOLET = 6
    WHITE = 7
    BLACK = 8
    SPECIAL_RED = 9
    SPECIAL_PALE = 10
    NEUTRAL = 11
    ATTRIBUTE_TYPE_NONE = 12
    UNRECOGNIZED = -1


class STR_ATTRIBUTE_TYPE(StrEnum):
    CRIMSON = "CRIMSON"
    SCARLET = "SCARLET"
    AMBER = "AMBER"
    SHAMROCK = "SHAMROCK"
    AZURE = "AZURE"
    INDIGO = "INDIGO"
    VIOLET = "VIOLET"
    WHITE = "WHITE"
    BLACK = "BLACK"
    SPECIAL_RED = "SPECIAL_RED"
    SPECIAL_PALE = "SPECIAL_PALE"
    NEUTRAL = "NEUTRAL"
    ATTRIBUTE_TYPE_NONE = "ATTRIBUTE_TYPE_NONE"
    UNRECOGNIZED = "UNRECOGNIZED"


class ENCOUNTER(IntEnum):
    START = 0
    BATTLE = 1
    HARD_BATTLE = 2
    EVENT = 3
    SAVE = 4
    AB_BATTLE = 5
    BOSS = 6
    EVENT_BATTLE = 7
    EVENT_HARD_BATTLE = 8
    EVENT_AB_BATTLE = 9
    MIRROR_SHOP = 10
    MIRROR_SELECT_EVENT = 11
    STAIRS = 12
    STORY = 13
    UNRECOGNIZED = -1


class STR_ENCOUNTER(StrEnum):
    START = "START"
    BATTLE = "BATTLE"
    HARD_BATTLE = "HARD_BATTLE"
    EVENT = "EVENT"
    SAVE = "SAVE"
    AB_BATTLE = "AB_BATTLE"
    BOSS = "BOSS"
    EVENT_BATTLE = "EVENT_BATTLE"
    EVENT_HARD_BATTLE = "EVENT_HARD_BATTLE"
    EVENT_AB_BATTLE = "EVENT_AB_BATTLE"
    MIRROR_SHOP = "MIRROR_SHOP"
    MIRROR_SELECT_EVENT = "MIRROR_SELECT_EVENT"
    STAIRS = "STAIRS"
    STORY = "STORY"
    UNRECOGNIZED = "UNRECOGNIZED"


class UNIT_KEYWORD(IntEnum):
    ERROR = 0
    BASE_APPEARANCE = 1
    CRAPCRAB = 2
    FAIRY_LIQUOR = 3
    MACHINE_BOUND_ORGANISM = 4
    MERMAID = 5
    WHITE_PARASITE = 6
    KILLER_WHALE = 7
    TETRAPOD = 8
    DESTROYED_TETRAPOD = 9
    WALKING_PEARL = 10
    GREEN_SLIME = 11
    SkinProphet = 12
    CANDLE = 13
    SPIRAL_OF_CONTEMPT = 14
    GRASP = 15
    BONGE_CHICKEN = 16
    MACHINE = 17
    NONE_BLOOD = 18
    ARDOR_BLOSSOM_MOTH = 19
    ON_THE_LAKE = 20
    PEQUOD_CAPTAIN = 21
    GLASS_ENEMY = 22
    BUTLER = 23
    CATHERINE = 24
    LEFT_ARM = 25
    RIGHT_ARM = 26
    SHADOW_ENEMY = 27
    LOBOTOMY_HEAD = 28
    LOBOTOMY_BRANCH = 29
    FIXER = 30
    CLAN = 31
    BACK_STREET = 32
    BLOODBAG = 33
    BLOODFIEND = 34
    DEPENDENT = 35
    THIRD_DEPENDENT = 36
    SECOND_DEPENDENT = 37
    FIRST_DEPENDENT = 38
    SMALL = 39
    REGULAR = 40
    LARGE = 41
    EXTRA_LARGE = 42
    WILD_HUNT_HEATH = 43
    ABNORMALITY_EROSION = 44
    LIMBUS_COMPANY = 45
    L_CORP = 46
    N_CORP = 47
    K_CORP = 48
    G_CORP = 49
    W_CORP = 50
    R_CORP = 51
    T_CORP = 52
    SEVEN = 53
    CINQ = 54
    ZWEI = 55
    BLADE_LINEAGE = 56
    BLACK_CLOUD = 57
    LIU = 58
    SHI = 59
    KONG_KONG = 60
    MARIACHI = 61
    TIEQIU = 62
    CASINO_SECURITY = 63
    BACKSTREET_COOK = 64
    TROUBLE_SHOOTER = 65
    ATL = 66
    MOLAR = 67
    DIECI = 68
    HOOK_OFFICE = 69
    DUAL_HOOK_PIRATE = 70
    MIDDLE_FINGER = 71
    PEQUOD_CREW = 72
    OUFI = 73
    LINTON = 74
    WUTHERING_HEIGHTS = 75
    DEAD_RABBITS = 76
    RING_FINGER = 77
    WILD_HUNT = 78
    DAWN = 79
    YURODIVY = 80
    MULTI_CRACK = 81
    N_CORP_FNATIC = 82
    DEVYAT = 83
    FANG_HUNT = 84
    FAMILY_GA = 85
    FAMILY_GA_CANDIDATE = 86
    UNRECOGNIZED = -1


class STR_UNIT_KEYWORD(StrEnum):
    ERROR = "ERROR"
    BASE_APPEARANCE = "BASE_APPEARANCE"
    CRAPCRAB = "CRAPCRAB"
    FAIRY_LIQUOR = "FAIRY_LIQUOR"
    MACHINE_BOUND_ORGANISM = "MACHINE_BOUND_ORGANISM"
    MERMAID = "MERMAID"
    WHITE_PARASITE = "WHITE_PARASITE"
    KILLER_WHALE = "KILLER_WHALE"
    TETRAPOD = "TETRAPOD"
    DESTROYED_TETRAPOD = "DESTROYED_TETRAPOD"
    WALKING_PEARL = "WALKING_PEARL"
    GREEN_SLIME = "GREEN_SLIME"
    SkinProphet = "SkinProphet"
    CANDLE = "CANDLE"
    SPIRAL_OF_CONTEMPT = "SPIRAL_OF_CONTEMPT"
    GRASP = "GRASP"
    BONGE_CHICKEN = "BONGE_CHICKEN"
    MACHINE = "MACHINE"
    NONE_BLOOD = "NONE_BLOOD"
    ARDOR_BLOSSOM_MOTH = "ARDOR_BLOSSOM_MOTH"
    ON_THE_LAKE = "ON_THE_LAKE"
    PEQUOD_CAPTAIN = "PEQUOD_CAPTAIN"
    GLASS_ENEMY = "GLASS_ENEMY"
    BUTLER = "BUTLER"
    CATHERINE = "CATHERINE"
    LEFT_ARM = "LEFT_ARM"
    RIGHT_ARM = "RIGHT_ARM"
    SHADOW_ENEMY = "SHADOW_ENEMY"
    LOBOTOMY_HEAD = "LOBOTOMY_HEAD"
    LOBOTOMY_BRANCH = "LOBOTOMY_BRANCH"
    FIXER = "FIXER"
    CLAN = "CLAN"
    BACK_STREET = "BACK_STREET"
    BLOODBAG = "BLOODBAG"
    BLOODFIEND = "BLOODFIEND"
    DEPENDENT = "DEPENDENT"
    THIRD_DEPENDENT = "THIRD_DEPENDENT"
    SECOND_DEPENDENT = "SECOND_DEPENDENT"
    FIRST_DEPENDENT = "FIRST_DEPENDENT"
    SMALL = "SMALL"
    REGULAR = "REGULAR"
    LARGE = "LARGE"
    EXTRA_LARGE = "EXTRA_LARGE"
    WILD_HUNT_HEATH = "WILD_HUNT_HEATH"
    ABNORMALITY_EROSION = "ABNORMALITY_EROSION"
    LIMBUS_COMPANY = "LIMBUS_COMPANY"
    L_CORP = "L_CORP"
    N_CORP = "N_CORP"
    K_CORP = "K_CORP"
    G_CORP = "G_CORP"
    W_CORP = "W_CORP"
    R_CORP = "R_CORP"
    T_CORP = "T_CORP"
    SEVEN = "SEVEN"
    CINQ = "CINQ"
    ZWEI = "ZWEI"
    BLADE_LINEAGE = "BLADE_LINEAGE"
    BLACK_CLOUD = "BLACK_CLOUD"
    LIU = "LIU"
    SHI = "SHI"
    KONG_KONG = "KONG_KONG"
    MARIACHI = "MARIACHI"
    TIEQIU = "TIEQIU"
    CASINO_SECURITY = "CASINO_SECURITY"
    BACKSTREET_COOK = "BACKSTREET_COOK"
    TROUBLE_SHOOTER = "TROUBLE_SHOOTER"
    ATL = "ATL"
    MOLAR = "MOLAR"
    DIECI = "DIECI"
    HOOK_OFFICE = "HOOK_OFFICE"
    DUAL_HOOK_PIRATE = "DUAL_HOOK_PIRATE"
    MIDDLE_FINGER = "MIDDLE_FINGER"
    PEQUOD_CREW = "PEQUOD_CREW"
    OUFI = "OUFI"
    LINTON = "LINTON"
    WUTHERING_HEIGHTS = "WUTHERING_HEIGHTS"
    DEAD_RABBITS = "DEAD_RABBITS"
    RING_FINGER = "RING_FINGER"
    WILD_HUNT = "WILD_HUNT"
    DAWN = "DAWN"
    YURODIVY = "YURODIVY"
    MULTI_CRACK = "MULTI_CRACK"
    N_CORP_FNATIC = "N_CORP_FNATIC"
    DEVYAT = "DEVYAT"
    FANG_HUNT = "FANG_HUNT"
    FAMILY_GA = "FAMILY_GA"
    FAMILY_GA_CANDIDATE = "FAMILY_GA_CANDIDATE"
    UNRECOGNIZED = "UNRECOGNIZED"


class ITEM_USE_TYPE(IntEnum):
    UNUSABLE = -1
    NONE = 0
    PACKAGE_BOXED = 1
    PACKAGE_RANDOM = 2
    PACKAGE_OPTIONAL = 3
    ENKEPHALINE = 4
    LEAPUP_TICKET = 5
    USE_SINGLE = 6
    ACQUIRE_PERSONALITY = 7
    ACQUIRE_EGO = 8


class STR_ITEM_USE_TYPE(StrEnum):
    UNUSABLE = "UNUSABLE"
    NONE = "NONE"
    PACKAGE_BOXED = "PACKAGE_BOXED"
    PACKAGE_RANDOM = "PACKAGE_RANDOM"
    PACKAGE_OPTIONAL = "PACKAGE_OPTIONAL"
    ENKEPHALINE = "ENKEPHALINE"
    LEAPUP_TICKET = "LEAPUP_TICKET"
    USE_SINGLE = "USE_SINGLE"
    ACQUIRE_PERSONALITY = "ACQUIRE_PERSONALITY"
    ACQUIRE_EGO = "ACQUIRE_EGO"


class SEASONAL_ITEM_TYPE(IntEnum):
    PACKAGE_RANDOM = 0
    PACKAGE_OPTIONAL = 1
    UNRECOGNIZED = -1


class STR_SEASONAL_ITEM_TYPE(StrEnum):
    PACKAGE_RANDOM = "PACKAGE_RANDOM"
    PACKAGE_OPTIONAL = "PACKAGE_OPTIONAL"
    UNRECOGNIZED = "UNRECOGNIZED"


class ITEM_CONTENTS_OPEN_TYPE(IntEnum):
    NONE = 0
    PACKAGE_BOXED = 1
    PACKAGE_RANDOM = 2
    PACKAGE_OPTIONAL = 3
    UNRECOGNIZED = -1


class STR_ITEM_CONTENTS_OPEN_TYPE(StrEnum):
    NONE = "NONE"
    PACKAGE_BOXED = "PACKAGE_BOXED"
    PACKAGE_RANDOM = "PACKAGE_RANDOM"
    PACKAGE_OPTIONAL = "PACKAGE_OPTIONAL"
    UNRECOGNIZED = "UNRECOGNIZED"


class ITEM_USE_FUNC_TYPE(IntEnum):
    NONE = 0
    PERSONALITY_EXP = 1
    PERSONALITY_LEVEL_TO = 2
    PERSONALITY_GACKSUNG_TO = 3
    EGO_GACKSUNG_TO = 4
    CHECK_IS_NOT_EGO_TYPE = 5
    UNRECOGNIZED = -1


class STR_ITEM_USE_FUNC_TYPE(StrEnum):
    NONE = "NONE"
    PERSONALITY_EXP = "PERSONALITY_EXP"
    PERSONALITY_LEVEL_TO = "PERSONALITY_LEVEL_TO"
    PERSONALITY_GACKSUNG_TO = "PERSONALITY_GACKSUNG_TO"
    EGO_GACKSUNG_TO = "EGO_GACKSUNG_TO"
    CHECK_IS_NOT_EGO_TYPE = "CHECK_IS_NOT_EGO_TYPE"
    UNRECOGNIZED = "UNRECOGNIZED"


class Element(BaseModel):
    type: STR_ELEMENT_TYPE = STR_ELEMENT_TYPE.NONE
    _type: ELEMENT_TYPE = ELEMENT_TYPE.NONE
    id: int = 0
    num: int = 0
    tags: List[str] = []


class PartResistFormat(BaseModel):
    id: int = 0
    attr: List[int] = []
    atkr: List[int] = []


class AbnormalityUnlockInformationFormat(BaseModel):
    id: int = 0
    k: int = 0
    s: List[int] = []
    p: List[int] = []
    ps: List[PartResistFormat] = []


class UserMirrorDungeonShopDataFormat(BaseModel):
    ph: int = 0
    pup: int = 0
    upid: int = 0
    peg: List[int] = []
    pcf: int = 0
    pabu: int = 0
    pueg: int = 0
    egpool: List[int] = []
    pseg: int = 0
    rc: int = 0
    fre: int = 0


class ExpDungeonClearInfoFormat(BaseModel):
    dungeonid: int = 0
    clearnumber: int = 0


class ThreadDungeonClearInfoFormat(BaseModel):
    dungeonid: int = 0
    clearnumber: int = 0
    dungeonlevel: int = 0


class DailyLoginRewardStateFormat(BaseModel):
    weekid: int = 0
    id: int = 0


class UserProfileBorderFormat(BaseModel):
    id: int = 0
    date: str = ""


class UserProfileEgobackgroundFormat(BaseModel):
    id: int = 0
    date: str = ""


class ItemFormat(BaseModel):
    item_id: int = 0
    num: int = 0


class SeasonLogFormat(BaseModel):
    seasonTo: int = 0
    seasonFrom: int = 0
    unreceivedBattlePassRewards: List[Element] = []
    lostPieces: List[ItemFormat] = []
    acquiredFromLostPieces: List[ItemFormat] = []
    lostPackages: List[ItemFormat] = []
    acquiredFromLostPackages: List[ItemFormat] = []
    lostGlobalPieces: List[ItemFormat] = []
    acquiredFromLostGlobalPieces: List[ItemFormat] = []
    date: str = ""


class MailContentFormat(BaseModel):
    id: int = 0
    version: int = 0
    senderSprName: str = ""
    content_KR: str = ""
    sender_KR: str = ""
    content_EN: str = ""
    sender_EN: str = ""
    content_JP: str = ""
    sender_JP: str = ""


class NoticeFormat(BaseModel):
    id: int = 0
    version: int = 0
    type: int = 0
    startDate: str = ""
    endDate: str = ""
    sprNameList: List[str] = []
    title_KR: str = ""
    content_KR: str = ""
    title_EN: str = ""
    content_EN: str = ""
    title_JP: str = ""
    content_JP: str = ""


class SynchronizedFormat(BaseModel):
    version: int = 0
    noticelist: List[NoticeFormat] = []
    mailContentList: List[MailContentFormat] = []


class ContentFormat(BaseModel):
    formatKey: str = ""
    formatValue: str = ""


class PriceTierFormat(BaseModel):
    tier: int = 0
    version: int = 0
    USD_cent: int = 0
    KRW: int = 0
    JPY: int = 0


class EventRewardStateFormat(BaseModel):
    eventID: int = 0
    rewardID: int = 0
    count: int = 0


class MissionFormat(BaseModel):
    category: MISSION_CATEGORY = MISSION_CATEGORY.NONE
    id: int = 0
    state: MISSION_STATE = MISSION_STATE.NONE
    initconditionvalue: int = 0
    conditionvalue: int = 0
    expiredate: str = ""


class MissionConditionFormat(BaseModel):
    id: int = 0
    value: int = 0


class MissionConditionContextFormat(BaseModel):
    type: MISSION_CONDITION_TYPE = MISSION_CONDITION_TYPE.NONE
    target1: int = 0
    target2: int = 0
    target3: int = 0
    value: int = 0


class UserBannerDataFormat(BaseModel):
    id: int = 0
    acquiretime: str = ""
    value: int = 0
    value2: int = 0


class DungeonMapNodeFormat(BaseModel):
    f: int = 0
    s: int = 0
    nid: int = 0


class DungeonMapEgoGiftFormat(BaseModel):
    id: int = 0
    pids: List[int] = []
    un: int = 0
    ul: int = 0


class DungeonEgoFormat(BaseModel):
    id: int = 0
    g: int = 0
    idx: int = 0


class DungeonSaveUnitInfoFormat(BaseModel):
    pid: int = 0
    ch: int = 0
    cm: int = 0
    mhos: int = 0
    g: int = 0
    l: int = 0
    es: List[DungeonEgoFormat] = []
    isp: int = 0


class DungeonEgoSkillStockFormat(BaseModel):
    t: str = ""
    n: int = 0


class DungeonChoiceEventSaveDataFormat(BaseModel):
    sl: List[int] = []
    cs: int = 0
    ri: int = 0


class DungeonCurrentInfoFormat(BaseModel):
    cn: DungeonMapNodeFormat = DungeonMapNodeFormat()
    egs: List[DungeonMapEgoGiftFormat] = []
    pnids: List[int] = []
    nr: int = 0
    pce: List[DungeonChoiceEventSaveDataFormat] = []
    ess: List[DungeonEgoSkillStockFormat] = []
    dn: int = 0


class DungeonStatisticsDataFormat(BaseModel):
    id: int = 0
    gd: int = 0
    rd: int = 0


class StoryDungeonSaveUnitInfoFormat(BaseModel):
    sp: int = 0
    gi: int = 0


class StoryDungeonCurrentInfoFormat(BaseModel):
    dul: List[StoryDungeonSaveUnitInfoFormat] = []
    scpn: DungeonMapNodeFormat = DungeonMapNodeFormat()
    scpegl: List[DungeonMapEgoGiftFormat] = []
    opn: List[int] = []


class StoryDungeonSaveInfoFormat(BaseModel):
    dungeonid: int = 0
    currentinfo: StoryDungeonCurrentInfoFormat = StoryDungeonCurrentInfoFormat()


class UserPublicBannerFormat(BaseModel):
    id: int = 0
    value: int = 0
    value2: int = 0
    idx: int = 0


class UserPublicProfileFormat(BaseModel):
    public_uid: str = ""
    illust_id: int = 0
    illust_gacksung_level: int = 0
    leftborder_id: int = 0
    rightborder_id: int = 0
    egobackground_id: int = 0
    sentence_id: int = 0
    word_id: int = 0
    banners: List[UserPublicBannerFormat] = []
    level: int = 0
    date: str = ""


class ProfileEgoFormat(BaseModel):
    id: int = 0
    g: int = 0


class ProfileEgoContainIndexFormat(BaseModel):
    idx: int = 0
    id: int = 0
    g: int = 0


class SupportPersonalityFormat(BaseModel):
    pid: int = 0
    l: int = 0
    egos: List[ProfileEgoContainIndexFormat] = []
    gl: int = 0
    gi: int = 0


class SupportPersonalitySlotFormat(BaseModel):
    idx: int = 0
    pid: int = 0
    l: int = 0
    egos: List[ProfileEgoContainIndexFormat] = []
    gl: int = 0
    gi: int = 0


class UserPublicProfileWithSupportersFormat(BaseModel):
    support_personalities: List[SupportPersonalitySlotFormat] = []


class BattlePassParameterFormat(BaseModel):
    enemyKillCount: int = 0
    abnormalityKillCount: int = 0
    isUsedDailyChar: bool = False
    isUsedSeasonEgo: bool = False
    isUsedSeasonAnnouncer: bool = False


class StageNormalReqResultFormat(BaseModel):
    mainchapterid: int = 0
    subchapterid: int = 0
    nodeid: int = 0
    stageid: int = 0
    iswin: bool = False
    turn: int = 0
    formationid: int = 0
    supportCharacterId: int = 0
    supportPersonalityId: int = 0
    supportEgoIds: List[int] = []
    supportParticipate: bool = False
    battlePassParameters: BattlePassParameterFormat = BattlePassParameterFormat()
    abnormalityLogs: List[AbnormalityUnlockInformationFormat] = []
    missionConditionContexts: List[MissionConditionContextFormat] = []
    usedDanteAbilityCount: int = 0


class StageDungeonReqResultFormat(BaseModel):
    mainchapterid: int = 0
    subchapterid: int = 0
    nodeid: int = 0
    stageid: int = 0


class StageStoryReqResultFormat(BaseModel):
    mainchapterid: int = 0
    subchapterid: int = 0
    nodeid: int = 0
    stageid: int = 0


class StagePersonalityInfoFormat(BaseModel):
    personalityid: int = 0
    prevlevel: int = 0
    totaladdexp: int = 0


class NodeStateFormat(BaseModel):
    id: int = 0
    ct: int = 0
    cn: int = 0
    dn: int = 0


class SubChapterStateFormat(BaseModel):
    id: int = 0
    nss: List[NodeStateFormat] = []
    rss: List[int] = []


class MainChapterStateFormat(BaseModel):
    id: int = 0
    subcss: List[SubChapterStateFormat] = []


class MirrorDungeonGetCharacterInfoFormat(BaseModel):
    pid: int = 0
    egos: List[DungeonEgoFormat] = []


class RandomDungeonLevelUpPersonalityInfoFormat(BaseModel):
    pid: int = 0
    ego: DungeonEgoFormat = DungeonEgoFormat()


class StoryMirrorDungeonLevelUpPersonalityInfoFormat(BaseModel):
    pid: int = 0
    egos: List[DungeonEgoFormat] = []


class RandomDungeonEncounterRewardEventInfoFormat(BaseModel):
    rt: str = ""
    se: int = 0
    sh: int = 0
    pool: List[int] = []
    pool_v2: List[int] = []
    pool_v3: List[int] = []


class MirrorDungeonFormationEgoFormat(BaseModel):
    prevEgoId: int = 0
    nextEgoId: int = 0


class MirrorDungeonFormationFormat(BaseModel):
    pervPersonalityId: int = 0
    nextPersonalityId: int = 0
    egos: List[MirrorDungeonFormationEgoFormat] = []


class MirrorDungeonStartBuffInfoFormat(BaseModel):
    dungeonid: int = 0
    bufstate: List[int] = []
    specialbufstate: List[int] = []
    disabled: List[int] = []
    chip: int = 0


class MirrorDungeonClearInfoFormat(BaseModel):
    dungeonid: int = 0
    idx: int = 0
    clearnumber: int = 0
    defeatnumber: int = 0


class MirrorDungeonPersonalityRestStatusFormat(BaseModel):
    pid: int = 0
    cnt: int = 0


class MirrorDungeonPrevPlayRecordFormat(BaseModel):
    pids: List[int] = []
    epsId: int = 0
    prevtfids: List[int] = []
    tfids: List[int] = []


class MirrorDungeonHistoryFormat(BaseModel):
    dungeonid: int = 0
    restStatuses: List[MirrorDungeonPersonalityRestStatusFormat] = []
    prevPlayRecord: MirrorDungeonPrevPlayRecordFormat = (
        MirrorDungeonPrevPlayRecordFormat()
    )


class MirrorDungeonAcquiredChipFormat(BaseModel):
    clearFloorChip: int = 0
    clearNodeChip: int = 0
    battleWinCount: int = 0
    battleWinChip: int = 0
    acquiredEgoGiftChip: int = 0
    difficultyProb: int = 0
    startEgoGiftPoolSetBonusChip: int = 0
    personalityRestBonusChip: int = 0
    bonusChipReward: int = 0
    themeBonusChip: int = 0
    consumedChip: int = 0
    totalChip: int = 0


class MirrorDungeonAcquiredRewardFormat(BaseModel):
    useWeeklyRewardChance: bool = False
    useWeeklyHardRewardChance: bool = False
    acquiredUserExp: int = 0
    rewardList: List[Element] = []


class MirrorDungeonExitRewardFormat(BaseModel):
    chanceConsumption: int = 0
    rewardList: List[Element] = []
    moduleConsumption: int = 0


class SaveData_Rail_Line2_Format(BaseModel):
    hps: List[int] = []
    lastWave: int = 0
    lastPhase: List[int] = []
    isSkillUsed: List[bool] = []


class SaveDataForBS(BaseModel):
    section: int = 0
    isActive: bool = False


class SaveDataForPart(BaseModel):
    partHp: int = 0
    bs: List[SaveDataForBS] = []
    originBs: List[SaveDataForBS] = []


class SaveDataForEach(BaseModel):
    abnormalityHp: int = 0
    abnormalityMaxHp: int = 0
    abnormalityMp: int = 0
    partsData: List[SaveDataForPart] = []
    lastPhase: int = 0
    checkList: List[bool] = []


class SaveDataForRailwayDungeon(BaseModel):
    lastWave: int = 0
    lastTurn: int = 0
    abnoSaveDataList: List[SaveDataForEach] = []


class RailwayUnitInfoFormat(BaseModel):
    pid: int = 0
    g: int = 0
    l: int = 0
    es: List[DungeonEgoFormat] = []
    sp: int = 0
    gi: int = 0


class RailwayUnitSinFormat(BaseModel):
    sp: List[int] = []
    cs: List[int] = []
    rs: int = 0


class RailwayUnitStatusFormat(BaseModel):
    pid: int = 0
    hp: int = 0
    mp: int = 0
    isp: int = 0
    sin: RailwayUnitSinFormat = RailwayUnitSinFormat()
    egos: List[DungeonEgoFormat] = []
    sp: int = 0
    lv: int = 0
    g: int = 0
    gi: int = 0


class RailwayEGOStockFormat(BaseModel):
    t: str = ""
    n: int = 0


class RailwayStatisticsDataFormat(BaseModel):
    id: int = 0
    gd: int = 0
    rd: int = 0


class RailwayDetailStatisticsDataFormat(BaseModel):
    collectionId: int = 0
    personalities: List[RailwayUnitInfoFormat] = []
    statistics: List[RailwayStatisticsDataFormat] = []


class RailwayBuffFormat(BaseModel):
    id: int = 0
    count: int = 0
    targetids: List[int] = []


class RailwayBuffSetFormat(BaseModel):
    setid: int = 0
    buffs: List[RailwayBuffFormat] = []
    recentbuffid: int = 0
    currentbuffids: List[int] = []


class RailwayTurnsPerNode(BaseModel):
    nid: int = 0
    turn: int = 0


class RailwayLogDataFormat(BaseModel):
    idx: int = 0
    personalities: List[RailwayUnitInfoFormat] = []
    statistics: List[RailwayStatisticsDataFormat] = []
    detailstatistics: List[RailwayDetailStatisticsDataFormat] = []
    clearturn: int = 0
    turnspernode: List[RailwayTurnsPerNode] = []
    clearrotation: int = 0
    buffsets: List[RailwayBuffSetFormat] = []
    date: str = ""
    deadunitnumber: int = 0


class RailwayExtraRewardStateFormat(BaseModel):
    id: int = 0
    isRewarded: bool = False


class RailwayDungeonSaveInfoFormat(BaseModel):
    id: int = 0
    prevclearnode: int = 0
    currentnode: int = 0
    lastclearnode: int = 0
    personalities: List[RailwayUnitInfoFormat] = []
    payreward: int = 0
    rewardstate: int = 0
    extrarewardstate: List[RailwayExtraRewardStateFormat] = []
    firstcleardate: str = ""
    currentclearrotation: int = 0
    lastenternodeid: int = 0
    lastclearrotation: int = 0
    buffsets: List[RailwayBuffSetFormat] = []
    initseed: int = 0
    currentseed: int = 0
    enemySaveData: SaveDataForRailwayDungeon = SaveDataForRailwayDungeon()


class RailwayNodeDataFormat(BaseModel):
    nodeid: int = 0
    egostocks: List[RailwayEGOStockFormat] = []
    status: List[RailwayUnitStatusFormat] = []
    clearturn: int = 0
    playturn: int = 0
    statistics: List[RailwayStatisticsDataFormat] = []
    enemy: SaveDataForRailwayDungeon = SaveDataForRailwayDungeon()
    nodestate: int = 0


class RailwayBuffSetRequestFormat(BaseModel):
    setId: int = 0
    buffId: int = 0
    targetId: int = 0


class AnnouncerFormat(BaseModel):
    announcer_ids: List[int] = []
    cur_announcer_ids: List[int] = []


class UserAuthFormat(BaseModel):
    uid: int = 0
    public_id: int = 0
    db_id: int = 0
    auth_code: str = ""
    last_login_date: str = ""
    last_update_date: str = ""
    data_version: int = 0


class LinkAuthFormat(BaseModel):
    public_id: int = 0
    password: str = ""
    expiry_date: str = ""
    details: str = ""


class AccountInfoFormat(BaseModel):
    uid: int = 0
    google_account: str = ""
    apple_account: str = ""
    steam_account: str = ""
    unlink_date: str = ""


class BattlePassMissionState(BaseModel):
    id: int = 0
    count: int = 0
    state: int = 0


class BattlePassFormat(BaseModel):
    is_limbus: bool = False
    level: int = 0
    exp: int = 0
    today_rand_value: int = 0
    ex_reward_level: int = 0
    limbus_apply_level: int = 0
    rewards_state: List[int] = []
    missions_state: List[BattlePassMissionState] = []
    special_product_state: int = 0
    ex_reward_limbus_level: int = 0


class ChanceFormat(BaseModel):
    id: int = 0
    value: int = 0


class DanteAbilityFormat(BaseModel):
    category: DANTE_ABILITY_CATEGORY = DANTE_ABILITY_CATEGORY.DEFAULT
    abilityids: List[int] = []
    remaincount: int = 0


class EgoFormat(BaseModel):
    ego_id: int = 0
    gacksung: int = 0
    acquire_time: str = ""


class EgoContainIndexFormat(BaseModel):
    index: int = 0
    ego_id: int = 0
    gacksung: int = 0
    acquire_time: str = ""


class FormationNameElement(BaseModel):
    k: int = 0
    v: int = 0


class FormationDetailFormat(BaseModel):
    personalityId: int = 0
    egos: List[int] = []
    isParticipated: bool = False
    participationOrder: int = 0


class FormationFormat(BaseModel):
    id: int = 0
    formationDetails: List[FormationDetailFormat] = []
    formationNameFormat: List[FormationNameElement] = []


class GachaRecordFormat(BaseModel):
    gachaId: int = 0
    pityPoint: int = 0


class LobbyCgDetailFormat(BaseModel):
    id: int = 0
    g: int = 0


class LobbyCgFormat(BaseModel):
    characterId: int = 0
    lobbycgdetails: List[LobbyCgDetailFormat] = []
    isShowProfile: bool = False


class MailFormat(BaseModel):
    mail_id: int = 0
    sent_date: str = ""
    expiry_date: str = ""
    content_id: int = 0
    attachments: List[Element] = []
    parameters: List[str] = []


class MembershipFormat(BaseModel):
    iap_id: int = 0
    expiry_date: str = ""


class PersonalityFormat(BaseModel):
    personality_id: int = 0
    level: int = 0
    exp: int = 0
    gacksung: int = 0
    order_id: int = 0
    gacksung_illust_type: int = 0
    acquire_time: str = ""


class UserProfileFormat(BaseModel):
    illust_id: int = 0
    illust_gacksung_level: int = 0
    sentence_id: int = 0
    word_id: int = 0
    banner_ids: List[int] = []
    support_personalities: List[SupportPersonalityFormat] = []
    leftborder: int = 0
    rightborder: int = 0
    egobackground: int = 0


class AbnormalityKillLogFormat(BaseModel):
    id: int = 0
    number: int = 0


class StoryMirrorDungeonSaveUnitInfoFormat(BaseModel):
    sp: int = 0
    upidx: List[int] = []
    mlos: int = 0


class StageNodeFormat(BaseModel):
    nodeid: int = 0


class RandomDungeonMapNodeFormatForMapFormat(BaseModel):
    f: int = 0
    s: int = 0
    nid: int = 0
    e: int = 0
    eid: int = 0
    nnids: List[int] = []


class RandomDungeonMapFormat(BaseModel):
    ns: List[RandomDungeonMapNodeFormatForMapFormat] = []


class MirrorDungeonPrevUnitInfoFormat(BaseModel):
    pid: int = 0
    upidx: List[int] = []


class ThemeFloorPool(BaseModel):
    tfid: int = 0
    egs: List[int] = []
    upegs: List[int] = []


class RandomDungeonMapThemeFormat(BaseModel):
    f: int = 0
    tid: int = 0
    tfid: int = 0
    egs: List[int] = []


class MirrorDungeonEgoGiftPoolSetFormat(BaseModel):
    setId: int = 0
    keyword: str = ""
    pool: List[int] = []


class MirrorDungeonSaveUnitInfoFormat(BaseModel):
    upidx: List[int] = []
    mlos: int = 0


class MirrorDungeonCurrentInfoFormat(BaseModel):
    eid: int = 0
    dul: List[MirrorDungeonSaveUnitInfoFormat] = []
    sepsId: int = 0
    seps: List[MirrorDungeonEgoGiftPoolSetFormat] = []
    sepsCreated: int = 0
    tfs: List[RandomDungeonMapThemeFormat] = []
    tfps: List[ThemeFloorPool] = []
    tfpsCreated: int = 0
    rre: List[RandomDungeonEncounterRewardEventInfoFormat] = []
    ri: int = 0
    cost: int = 0
    shop: UserMirrorDungeonShopDataFormat = UserMirrorDungeonShopDataFormat()
    prevdul: List[MirrorDungeonPrevUnitInfoFormat] = []
    preves: List[int] = []
    leveladders: List[int] = []
    bonusChipReward: int = 0
    consumedChipIn: int = 0
    consumedChipOut: int = 0
    fundedChip: int = 0
    startKeyword: str = ""


class MirrorDungeonSaveInfoFormat(BaseModel):
    dungeonId: int = 0
    idx: int = 0
    currentInfo: MirrorDungeonCurrentInfoFormat = MirrorDungeonCurrentInfoFormat()
    dungeonMap: RandomDungeonMapFormat = RandomDungeonMapFormat()
    choiceEventList: List[int] = []
    addUserExp: int = 0
    statistics: List[DungeonStatisticsDataFormat] = []
    encounterstatistics: List[int] = []
    isEndDungeon: int = 0
    isReset: int = 0
    version: int = 0


class StoryMirrorDungeonCurrentInfoFormat(BaseModel):
    cn: DungeonMapNodeFormat = DungeonMapNodeFormat()
    egs: List[DungeonMapEgoGiftFormat] = []
    pnids: List[int] = []
    nr: int = 0
    pce: List[DungeonChoiceEventSaveDataFormat] = []
    ess: List[DungeonEgoSkillStockFormat] = []
    eid: int = 0
    dul: List[StoryMirrorDungeonSaveUnitInfoFormat] = []
    rre: List[RandomDungeonEncounterRewardEventInfoFormat] = []
    shop: UserMirrorDungeonShopDataFormat = UserMirrorDungeonShopDataFormat()
    cost: int = 0
    prevdul: List[MirrorDungeonPrevUnitInfoFormat] = []
    preves: List[int] = []
    seps: List[MirrorDungeonEgoGiftPoolSetFormat] = []
    sepsCreated: int = 0


class StoryMirrorDungeonSaveInfoFormat(BaseModel):
    dungeonid: int = 0
    currentinfo: StoryMirrorDungeonCurrentInfoFormat = (
        StoryMirrorDungeonCurrentInfoFormat()
    )
    map: RandomDungeonMapFormat = RandomDungeonMapFormat()
    choiceeventlist: List[int] = []
    statistics: List[DungeonStatisticsDataFormat] = []


class StoryMirrorDungeonGetCharacterInfoFormat(BaseModel):
    pid: int = 0
    egos: List[DungeonEgoFormat] = []
    sp: int = 0


class StoryMirrorDungeonGetCharacterInfoContainGacksungFormat(BaseModel):
    g: int = 0
    cl: int = 0
    pid: int = 0
    egos: List[DungeonEgoFormat] = []
    sp: int = 0


class UserTheaterInfoFormat(BaseModel):
    rewardedIDList: List[str] = []


class UnlockCodeFormat(BaseModel):
    unlockcode: int = 0
    expireDate: str = ""


class UserInfo(BaseModel):
    uid: int = 0
    level: int = 0
    exp: int = 0
    stamina: int = 0
    last_stamina_recover: str = ""


class Credits(BaseModel):
    private_server: str = "yuvlian"
    encryption: str = "League Of Nine"


class ServerInfo(BaseModel):
    version: str = "product"


class GachaLogDetail(BaseModel):
    type: STR_ELEMENT_TYPE = STR_ELEMENT_TYPE.NONE
    _type: ELEMENT_TYPE = ELEMENT_TYPE.NONE
    id: int = 0
    ex: Element = Element()
    origin: Element = Element()


class GachaLog(BaseModel):
    gachaId: int = 0
    gachaDate: str = ""
    paymentId: int = 0
    payments: List[ItemFormat] = []
    gachaLogDetails: List[GachaLogDetail] = []


class LinkDetails(BaseModel):
    level: int = 0
    lunacy: int = 0
    enkBox: int = 0
    enkModule: int = 0


class MailLog(BaseModel):
    maillog_id: int = 0
    sent_date: str = ""
    content_id: int = 0
    attachments: List[Element] = []
    unsealed_date: str = ""
    parameters: List[str] = []


class TermsOfUseState(BaseModel):
    version: int = 0
    state: TERMSOFUSE_STATE = TERMSOFUSE_STATE.NONE


class ServerUserAuth(BaseModel):
    uid: int = 0
    dbid: int = 0
    authCode: str = ""
    version: str = ""
    synchronousDataVersion: int = 0


class UpdatedFormat(BaseModel):
    isInitialized: bool = False
    userInfo: Optional[UserInfo] = None
    personalityList: Optional[List[PersonalityFormat]] = None
    egoList: Optional[List[EgoFormat]] = None
    formationList: Optional[List[FormationFormat]] = None
    lobbyCG: Optional[LobbyCgFormat] = None
    itemList: Optional[List[ItemFormat]] = None
    chanceList: Optional[List[ChanceFormat]] = None
    battlePass: Optional[BattlePassFormat] = None
    mainChapterStateList: Optional[List[MainChapterStateFormat]] = None
    mailList: Optional[List[MailFormat]] = None
    announcer: Optional[AnnouncerFormat] = None
    membershipList: Optional[List[MembershipFormat]] = None
    gachaList: Optional[List[GachaRecordFormat]] = None
    userUnlockCodeList: Optional[List[UnlockCodeFormat]] = None
    eventRewardStateList: Optional[List[EventRewardStateFormat]] = None
    isUpdateUserBanner: Optional[bool] = None
    isResetMirrorDungeon: Optional[bool] = None
    missionList: Optional[List[MissionFormat]] = None
    danteAbilityList: Optional[List[DanteAbilityFormat]] = None
