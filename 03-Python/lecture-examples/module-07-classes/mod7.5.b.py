class WebBrowser:
    geo_coordinates = {"lat": -4.764813, "lng": 16.131331 }

    def __init__(self, page):
        self.history = [page]
        self.current_page = page
        self.is_incognito = False
    
    def navigate(self, new_page):
        self.current_page = new_page
        if not self.is_incognito:
            self.history.append(new_page)
    
    def clear_history(self):
        self.history[:-1] = []    
    
    @classmethod
    def with_incognito(cls, page):
        instance = cls(page)
        instance.is_incognito = True
        instance.history = []
        return instance
    
    @classmethod
    def change_geo_coordinates(cls, new_coordinates):
        if new_coordinates["lat"] > 90 or new_coordinates["lat"] < -90:
            print("Invalid value for latitude. Should be within the range from -90 to 90 degrees.")
            return None
        if new_coordinates["lng"] > 180 or new_coordinates["lng"] < -180:
            print("Invalid value for longitude. Should be within the range from -180 to 180 degrees.")
            return None
        cls.geo_coordinates = new_coordinates


firefox = WebBrowser("www.org")

WebBrowser.change_geo_coordinates({"lat": 31, "lng": 123})

print(firefox.geo_coordinates)
