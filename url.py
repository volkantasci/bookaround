from dist_site import DistSite


class Url:
    def __init__(self, dist_site: DistSite, searching_key: str):
        self.dist_site = dist_site
        self.searching_key = searching_key

    @property
    def query_url(self):
        url = self.dist_site.search_url + '?' + self.dist_site.search_param + '=' + self.searching_key

        if self.dist_site.aditional_params:
            for param in self.dist_site.aditional_params.keys():
                url += f"&{param}={self.dist_site.aditional_params[param]}"

        return url
