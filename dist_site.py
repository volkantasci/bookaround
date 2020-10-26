class DistSite:
    def __init__(self, name: str, search_param, search_url, item_count_div_spec, page_size, pager_param, aditional_params=None):
        if aditional_params is None:
            aditional_params = dict()

        self.name = name
        self.search_param = search_param
        self.search_url = search_url
        self.item_count_div_spec = item_count_div_spec
        self.page_size = page_size
        self.pager_param = pager_param
        self.aditional_params = aditional_params
