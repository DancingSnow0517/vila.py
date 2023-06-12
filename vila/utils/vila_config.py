from ruamel import yaml

from .. import constants

class VilaConfig:
    bot_id: str
    bot_secret: str

    def __init__(self, **kwargs) -> None:
        self.bot_id = kwargs.get('bot_id', '')
        self.bot_secret = kwargs.get('bot_secret', '')

    @classmethod
    def load(cls, path=constants.CONFIG_PATH):
        with open(path, 'r', encoding='utf-8') as f:
            data = yaml.round_trip_load(f)
        return cls(**data)

