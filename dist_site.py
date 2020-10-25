class DistSite:
    def __init__(self, name: str, search_param, search_url, aditional_params=None):
        if aditional_params is None:
            aditional_params = dict()

        self.name = name
        self.search_param = search_param
        self.search_url = search_url
        self.aditional_params = aditional_params
