class BaseSearchBackend:
    def __init__(self, connection_alias, **connection_options):
        self.connection_alias = connection_alias
        self.timeout = connection_options.get("TIMEOUT", 10)
        self.include_spelling = connection_options.get("INCLUDE_SPELLING", False)
        self.batch_size = connection_options.get("BATCH_SIZE", 1000)
        self.silently_fail = connection_options.get("SILENTLY_FAIL", True)
        self.distance_available = connection_options.get("DISTANCE_AVAILABLE", False)

    def update(self, index, iterable, commit=True):
        raise NotImplementedError

    def remove(self, obj_or_string):
        raise NotImplementedError

    def clear(self, models=None, commit=True):
        raise NotImplementedError

    def search(self, query_string, **kwargs):
        raise NotImplementedError
