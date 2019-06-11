from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ListProperty, StringProperty, NumericProperty
from fingerdot import FingerDot
from kivy.lang.builder import Builder



Builder.load_string("""
#:import sqrt math.sqrt

<StringView>:
    dots: (key_dot0, key_dot1, key_dot2, key_dot3, key_dot4, key_dot5, key_dot6, key_dot7)
    # dots: (key_dot0, )
    # dots: (key_dot0, key_dot1, )
    string_width: sqrt(self.width**2 + self.height**2) *.004
    diameter: self.string_width * 10
    space: self.string_width * 8
    canvas.before:
        Color:
            rgba: app.colors['background']
        Rectangle:
            pos: self.pos
            size: self.size
        Color:
            rgba: app.colors['frame']
        Line:
            width: self.string_width
            points: (self.x, self.center_y, self.x + self.width, self.center_y) if self.orientation == 'horizontal' else (self.center_x, self.y, self.center_x, self.y + self.height)
        Rectangle:
            pos: self.pos if self.orientation == 'horizontal' else (self.x, self.y + self.height - self.space) 
            size: (self.space, self.height) if self.orientation == 'horizontal' else (self.width, self.space)
        Color:
            rgba: app.colors['background']
        Rectangle:
            pos: self.pos if self.orientation == 'horizontal' else (self.x, self.y + self.height - self.space) 
            size: (self.space, self.height) if self.orientation == 'horizontal' else (self.width, self.space)
            source: 'images/left_gradient.png' if self.orientation == 'horizontal' else 'images/upper_gradient.png'
        Rectangle:
            pos: (self.x + self.width - self.space, self.y) if self.orientation == 'horizontal' else self.pos
            size: (self.space, self.height) if self.orientation == 'horizontal' else (self.width, self.space)
            source: 'images/right_gradient.png' if self.orientation == 'horizontal' else 'images/lower_gradient.png' 
    FingerDot:
        id: key_dot0
        mode: 0
        diameter: root.string_width * 5 if self.mode == 0 else root.diameter
        offset: (self.label.texture_size[0] * .6, 0)  if root.orientation == 'horizontal' else (0, -self.label.texture_size[1] * .2)
        font_size: root.string_width * 15
        background_color: app.colors[root.colors[self.mode]]
        pos: (root.x + root.space, root.center_y) if root.orientation == 'horizontal' else (root.center_x, root.y + root.height - root.space)
    FingerDot:
        id: key_dot1
        mode: 0
        diameter: root.string_width * 5 if self.mode == 0 else root.diameter
        font_size: root.string_width * 15
        background_color: app.colors[root.colors[self.mode]]
        pos: (root.x + root.space + (root.width - 3 * root.space) * 1 / 7, root.center_y) if root.orientation == 'horizontal' else (root.center_x, root.y + root.height - root.space - (root.height - 3 * root.space) * 1 / 7)
    FingerDot:
        id: key_dot2
        mode: 0
        diameter: root.string_width * 5 if self.mode == 0 else root.diameter
        font_size: root.string_width * 15
        background_color: app.colors[root.colors[self.mode]]
        pos: (root.x + root.space + (root.width - 3 * root.space) * 2 / 7, root.center_y) if root.orientation == 'horizontal' else (root.center_x, root.y + root.height - root.space - (root.height - 3 * root.space) * 2 / 7)
    FingerDot:
        id: key_dot3
        mode: 0
        diameter: root.string_width * 5 if self.mode == 0 else root.diameter
        font_size: root.string_width * 15
        background_color: app.colors[root.colors[self.mode]]
        pos: (root.x + root.space + (root.width - 3 * root.space) * 3 / 7, root.center_y) if root.orientation == 'horizontal' else (root.center_x, root.y + root.height - root.space - (root.height - 3 * root.space) * 3 / 7)
    FingerDot:
        id: key_dot4
        mode: 0
        diameter: root.string_width * 5 if self.mode == 0 else root.diameter
        font_size: root.string_width * 15
        background_color: app.colors[root.colors[self.mode]]
        pos: (root.x + root.space + (root.width - 3 * root.space) * 4 / 7, root.center_y) if root.orientation == 'horizontal' else (root.center_x, root.y + root.height - root.space - (root.height - 3 * root.space) * 4 / 7)
    FingerDot:
        id: key_dot5
        mode: 0
        diameter: root.string_width * 5 if self.mode == 0 else root.diameter
        font_size: root.string_width * 15
        background_color: app.colors[root.colors[self.mode]]
        pos: (root.x + root.space + (root.width - 3 * root.space) * 5 / 7, root.center_y) if root.orientation == 'horizontal' else (root.center_x, root.y + root.height - root.space - (root.height - 3 * root.space) * 5 / 7)
    FingerDot:
        id: key_dot6
        mode: 0
        diameter: root.string_width * 5 if self.mode == 0 else root.diameter
        font_size: root.string_width * 15
        background_color: app.colors[root.colors[self.mode]]
        pos: (root.x + root.space + (root.width - 3 * root.space) * 6 / 7, root.center_y) if root.orientation == 'horizontal' else (root.center_x, root.y + root.height - root.space - (root.height - 3 * root.space) * 6 / 7)
    FingerDot:
        id: key_dot7
        mode: 0
        diameter: root.string_width * 5 if self.mode == 0 else root.diameter
        offset: (-self.label.texture_size[0] * .2, 0) if root.orientation == 'horizontal' else (0, 0)
        font_size: root.string_width * 15
        background_color: app.colors[root.colors[self.mode]]
        pos: (root.x + root.space + (root.width - 3 * root.space), root.center_y) if root.orientation == 'horizontal' else (root.center_x, root.y + root.height - root.space - (root.height - 3 * root.space))
""")



class StringView(FloatLayout):
    orientation = StringProperty('horizontal')
    fingers = ListProperty()
    names = ListProperty()
    space = NumericProperty(.03)
    diameter = NumericProperty(30)
    string_width = NumericProperty(0.009)
    colors = ListProperty(['frame', 'font', 'major', 'minor'])
    dots = ListProperty()

    def on_orientation(self, *args):
        if self.orientation not in ('horizontal', 'vertical'):
            self.orientation = 'horizontal'

    def on_fingers(self, *args):
        limit = 8
        if len(self.fingers) < limit:
            self.fingers += [0 for i in range(limit)]
        if len(self.fingers) > limit:
            self.fingers = self.fingers[:limit]
        for i in range(limit):
            self.dots[i].mode = self.fingers[i]

    def on_names(self, *args):
        limit = 8
        if len(self.names) < limit:
            self.names += ['<key>' for i in range(limit)]
        if len(self.names) > limit:
            self.names = self.names[:limit]
        for i in range(limit):
            self.dots[i].name = self.names[i]


if __name__ == '__main__':
    from kivy.app import App
    from kivy.properties import DictProperty
    import json

    with open('config.json', 'r') as config_file:
        configuration = json.load(config_file)

    class StringViewApp(App):
        colors = DictProperty(configuration['colors'])
        def build(self):
            string = StringView(orientation='horizontal')
            string.fingers = configuration['fingers'][-1]
            string.names = ['g', 'gis', 'a', 'b', 'h', 'c', 'cis', 'dis']
            return string

    StringViewApp().run()