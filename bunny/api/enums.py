# Normal libraries
from enum import IntEnum


class DefaultErrorType(IntEnum):
    """
    An enumerable object for the default errors that occur with interaction creation.

    .. note::
        This is a port from v3's errors, which basically delegate errors to a unique error code.
        This enum's purpose is to help remember error codes. Importing this class is not required.

        i.e. : raise InteractionException(1) == raise InteractionException(REQUEST_FAILURE)
    """

    BASE = 0
    REQUEST_FAILURE = 1
    INCORRECT_FORMAT = 2
    DUPLICATE_COMMAND = 3
    DUPLICATE_CALLBACK = 4
    DUPLICATE_SLASH_CLIENT = 5
    CHECK_FAILURE = 6
    INCORRECT_TYPE = 7
    INCORRECT_GUILD_ID_TYPE = 8
    INCORRECT_COMMAND_DATA = 9
    ALREADY_RESPONDED = 10


class OpCodeType(IntEnum):
    """
    An enumerable object for the Gateway's OPCODE result state.
    This is representative of the OPCodes generated by the WebSocket.

    .. note::
        Equivalent of `Gateway Opcodes <https://discord.com/developers/docs/topics/opcodes-and-status-codes#gateway-opcodes>`_ in the senpai API.
    """

    DISPATCH = 0
    HEARTBEAT = 1
    IDENTIFY = 2
    PRESENCE = 3
    VOICE_STATE = 4
    VOICE_PING = 5
    RESUME = 6
    RECONNECT = 7
    REQUEST_MEMBERS = 8
    INVALIDATE_SESSION = 9
    HELLO = 10
    HEARTBEAT_ACK = 11
    GUILD_SYNC = 12


class WSCloseCodeType(IntEnum):
    """
    An enumerable object for the Gateway's closing connection codes.
    This is representative of the Gateway responses generated by the WebSocket.

    .. note::
        Equivalent of `Gateway Close Event Codes <https://discord.com/developers/docs/topics/opcodes-and-status-codes#gateway-gateway-close-event-codes>`_ in the senpai API.
    """

    UNKNOWN_ERROR = 4000
    UNKNOWN_OPCODE = 4001
    DECODE_ERROR = 4002
    NOT_AUTHENTICATED = 4003
    AUTHENTICATION_FAILED = 4004
    ALREADY_AUTHENTICATED = 4005
    INVALID_SEQ = 4007
    RATE_LIMITED = 4008
    SESSION_TIMED_OUT = 4009
    INVALID_SHARD = 4010
    SHARDING_REQUIRED = 4011
    INVALID_API_VERSION = 4012
    INVALID_INTENTS = 4013
    DISALLOWED_INTENTS = 4014


class HTTPResponseType(IntEnum):
    """
    An enumerable object for the HTTP response codes senpai gives out.

    .. note::
        This enumerable does not list the documented "5xx", as it may vary.
    """

    OK = 200
    CREATED = 201
    NO_CONTENT = 204
    NOT_MODIFIED = 304
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    TOO_MANY_REQUESTS = 429
    GATEWAY_UNAVAILABLE = 502


class JSONResponseType(IntEnum):
    """
    An enumerable object for the JSON error response codes senpai gives out.

    .. note::
        Equivalent of `JSON Error Codes <https://discord.com/developers/docs/topics/opcodes-and-status-codes#json-json-error-codes>`_ in the senpai API.
    """

    GENERIC_ERROR = 0

    UNKNOWN_ACCOUNT = 10001
    UNKNOWN_APPLICATION = 10002
    UNKNOWN_CHANNEL = 10003
    UNKNOWN_GUILD = 10004
    UNKNOWN_INTEGRATION = 10005
    UNKNOWN_INVITE = 10006
    UNKNOWN_MEMBER = 10007
    UNKNOWN_MESSAGE = 10008
    UNKNOWN_OVERWRITE = 10009
    UNKNOWN_PROVIDER = 10010
    UNKNOWN_ROLE = 10011
    UNKNOWN_TOKEN = 10012
    UNKNOWN_USER = 10013
    UNKNOWN_EMOJI = 10014
    UNKNOWN_WEBHOOK = 10015
    UNKNOWN_WEBHOOK_SERVICE = 10016
    UNKNOWN_SESSION = 10020
    UNKNOWN_BAN = 10026
    UNKNOWN_SKU = 10027
    UNKNOWN_STORE_LISTING = 10028
    UNKNOWN_ENTITLEMENT = 10029
    UNKNOWN_TEAM = 10030
    UNKNOWN_LOBBY = 10031
    UNKNOWN_BRANCH = 10032
    UNKNOWN_STORE_DIRECTORY_LAYOUT = 10033
    UNKNOWN_REDISTRIBUTABLE = 10036
    UNKNOWN_GIFT_CODE = 10038
    UNKNOWN_STREAM = 10049
    UNKNOWN_GUILD_BOOST_COOLDOWN = 10050
    UNKNOWN_GUILD_TEMPLATE = 10057
    UNKNOWN_DISCOVERY_CATEGORY = 10059
    UNKNOWN_STICKER = 10060
    UNKNOWN_INTERACTION = 10062
    UNKNOWN_APPLICATION_COMMAND = 10063
    UNKNOWN_APPLICATION_COMMAND_PERMISSIONS = 10066
    UNKNOWN_STAGE = 10067
    UNKNOWN_GUILD_MEMBER_VERIFICATION_FORM = 10068
    UNKNOWN_GUILD_WELCOME_SCREEN = 10069
    UNKNOWN_SCHEDULED_EVENT = 10070
    UNKNOWN_SCHEDULED_EVENT_USER = 10071

    BOTS_NOT_ALLOWED = 20001
    ONLY_BOTS_ALLOWED = 20002
    EXPLICIT_CONTENT = 20009
    USER_NOT_AUTHORIZED_FOR_APPLICATION = 20012
    ACCOUNT_DISABLED = 20013
    RATE_LIMIT_SLOWMODE = 20016
    TEAM_OWNERSHIP_REQUIRED = 20018
    RATE_LIMIT_ANNOUNCEMENT_MESSAGE_EDIT = 20022
    RATE_LIMIT_CHANNEL_WRITE = 20028
    NAME_CONTAINS_DISALLOWED_WORD = 20031
    GUILD_SUBSCRIPTION_LEVEL_TOO_LOW = 20035

    MAX_GUILDS = 30001
    MAX_FRIENDS = 30002
    MAX_PINS = 30003
    MAX_RECIPIENTS = 30004
    MAX_ROLES = 30005
    MAX_WEBHOOKS = 30007
    MAX_EMOJIS = 30008
    MAX_REACTIONS = 30010
    MAX_CHANNELS = 30013
    MAX_ATTACHMENTS = 30015
    MAX_INVITES = 30016
    MAX_ANIMATED_EMOJIS = 30018
    MAX_GUILD_MEMBERS = 30019
    MAX_GUILD_DISCOVERY_CATEGORY = 30030
    GUILD_HAS_TEMPLATE = 30031
    MAX_THREAD_PARTICIPANTS = 30033
    MAX_BANS = 30035
    MAX_BAN_FETCHES = 30037
    MAX_STICKERS = 30039
    RATE_LIMIT_PRUNE = 30040

    UNAUTHORIZED = 40001
    EMAIL_VERIFICATION_REQUIRED = 40002
    RATE_LIMIT_PRIVATE_CHANNEL_OPENING = 40003
    REQUEST_TOO_LARGE = 40005
    FEATURE_DISABLED = 40006
    USER_BANNED = 40007
    USER_NOT_CONNECTED_TO_VOICE = 40032
    MESSAGE_CROSSPOSTED = 40033
    USER_IDENTITY_VERIFICATION_PROCESSING = 40035
    USER_IDENTITY_VERIFICATION_SUCCEEDED = 40036
    APPLICATION_NAME_USED = 40041

    MISSING_ACCESS = 50001
    INVALID_ACCOUNT_TYPE = 50002
    INVALID_ACTION_FOR_PRIVATE_CHANNEL = 50003
    WIDGET_DISABLED = 50004
    CANNOT_EDIT_MESSAGE_OF_OTHER_USER = 50005
    CANNOT_CREATE_EMPTY_MESSAGE = 50006
    CANNOT_MESSAGE_USER = 50007
    CANNOT_SEND_MESSAGE_TO_NON_TEXT_CHANNEL = 50008
    CHANNEL_VERIFICATION_LEVEL_TOO_HIGH = 50009
    OAUTH2_APPLICATION_HAS_NO_BOT = 50010
    OAUTH2_APPLICATION_LIMIT_REACHED = 50011
    INVALID_OAUTH2_STATE = 50012
    MISSING_PERMISSIONS = 50013
    INVALID_TOKEN = 50014
    NOTE_TOO_LONG = 50015
    BULK_DELETE_AMOUNT_OUT_OF_RANGE = 50016
    CANNOT_PIN_MESSAGE_IN_DIFFERENT_CHANNEL = 50019
    INVITE_CODE_INVALID_OR_TAKEN = 50020
    INVALID_ACTION_FOR_SYSTEM_MESSAGE = 50021
    INVALID_ACTION_FOR_THIS_CHANNEL_TYPE = 50024
    INVALID_OAUTH2_ACCESS_TOKEN = 50025
    MISSING_OAUTH2_SCOPE = 50026
    INVALID_WEBHOOK_TOKEN = 50027
    INVALID_ROLE = 50028
    INVALID_RECIPIENTS = 50033
    BULK_DELETE_MESSAGE_TOO_OLD = 50034
    INVALID_FORM_BODY = 50035
    CANNOT_ADD_USER_TO_GUILD_WHERE_BOT_IS_NOT_IN = 50036
    INVALID_API_VERSION = 50041
    ASSET_SIZE_TOO_LARGE = 50045
    INVALID_ASSET = 50046
    CANNOT_SELF_REDEEM_THIS_GIFT = 50054
    PAYMENT_SOURCE_REQUIRED_TO_REDEEM_GIFT = 50070
    CANNOT_DELETE_COMMUNITY_CHANNEL = 50074
    INVALID_STICKER_SENT = 50081
    INVALID_ACTION_FOR_ARCHIVED_THREAD = 50083
    INVALID_THREAD_NOTIFICATION_SETTING = 50084
    BEFORE_VALUE_EARLIER_THAN_CREATION_TIME = 50085
    INVALID_COUNTRY_CODE = 50095
    GUILD_MONETIZATION_REQUIRED = 50097
    MORE_BOOSTS_REQUIRED = 50101

    MFA_REQUIRED = 60003

    NO_USERS_WITH_TAG_EXISTS = 80004

    REACTION_BLOCKED = 90001

    RESOURCE_OVERLOADED = 130000

    STAGE_ALREADY_OPEN = 150006

    MESSAGE_HAS_THREAD = 160004
    THREAD_LOCKED = 160005
    MAX_ACTIVE_THREADS = 160006
    MAX_ACTIVE_ANNOUNCEMENT_THREADS = 160007

    INVALID_LOTTIE_JSON = 170001
    NO_RASTERIZED_IMAGES_IN_LOTTIE = 170002
    STICKER_MAXIMUM_FRAMERATE_EXCEEDED = 170003
    STICKER_FRAME_COUNT_OVER_1000 = 170004
    STICKER_MAXIMUM_DIMENSIONS_EXCEEDED = 170005
    STICKER_FRAME_RATE_OUT_OF_EXPECTED_RANGE = 170006
    STICKER_ANIMATION_DURATION_EXCEEDS_5_SECOND = 170007
