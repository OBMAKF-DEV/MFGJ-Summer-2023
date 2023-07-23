import tomli


def load_config(_kw: str = None) -> dict | str | int | None:
    with open('../MFGJ-Summer-2023/source/config/config.toml', 'rb') as _file:
        _config = tomli.load(_file)
        config = _config['graphics']
    if _kw is None:
        return config
    try:
        return config[_kw]
    except KeyError as exc:
        raise KeyError(exc) from exc