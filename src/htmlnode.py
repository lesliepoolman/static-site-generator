class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props is None:
            return
        result = ""
        for key, value in self.props.items():
            result += f" {key}=\"{value}\""
        return result
    
    def __repr__(self):
        result = f"tag={self.tag} | props={self.props} | value={self.value} | children="
        if self.children and len(self.children) > 0:
            for child in self.children:
                result += f"\n->-> {child}"
        return result
    