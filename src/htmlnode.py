class HTMLNode():
    def __init__(self, tag=None, value=None):
        self.tag = tag
        self.value = value
        self.__children = []
        self.__props = {}

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.__props is None:
            return
        result = ""
        for key, value in self.__props.items():
            result += f" {key}=\"{value}\""
        return result
    
    def __repr__(self):
        result = f"tag={self.tag} | props={self.__props} | value={self.value} | children="
        if len(self.__children) > 0:
            for child in self.__children:
                result += f"\n->-> {child}"
        return result
    
    def add_child(self, child):
        if child is None:
            return
        self.__children.append(child)
    
    def add_props(self, properties):
        if properties is None:
            return
        for key, value in properties.items():
            if key in self.__props.keys():
                self.__props[key] += f" {value}"
            else:
                self.__props[key] = value
