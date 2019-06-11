from kivy.animation import Animation
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import NumericProperty, ObjectProperty, OptionProperty, StringProperty, ListProperty, ReferenceListProperty
from kivy.lang.builder import Builder
from kivy.clock import Clock
from math import sqrt


Builder.load_string("""
<FingerDot>:
    size_hint: None, None
    height: self.diameter
    width: self.diameter
    left: -self.width / 2 + self.anim_off_x
    bottom: -self.height / 2 + self.anim_off_y
    right: self.width / 2 + self.anim_off_x
    top: self.height / 2 + self.anim_off_y
    label: key_label
    canvas.before:
        Color:
            rgba: self.background_color
        Ellipse:
            pos: self.left, self.bottom
            size: self.height, self.height
            angle_start: 180
            angle_end: 360
        Rectangle:
            pos: self.left + self.height / 2, self.bottom
            size: self.width - self.height, self.height
        Ellipse:
            pos: self.right - self.height, self.bottom
            size: self.height, self.height
            angle_start: 0
            angle_end: 180
        Color:
            rgba: self.outline_color
        Line:
            width: self.outline_width
            rounded_rectangle: self.left + self.outline_width, self.bottom + self.outline_width, self.width - self.outline_width * 2, self.height - self.outline_width * 2, (self.height - self.outline_width * 2) / 2
    Label:
        id: key_label
        opacity: 0
        color: app.colors['background'] #root.font_color
        bold: True
        text: root.name
        font_size: root.font_size
        pos: -self.width / 2 + root.anim_off_x, -self.height / 2 + root.anim_off_y
""")


class FingerDot(RelativeLayout):
    diameter = NumericProperty(20)
    background_color = ListProperty()
    outline_color = ListProperty()
    outline_width = NumericProperty(2)
    open_time = NumericProperty(0)
    transition_time = NumericProperty(.6)
    label = ObjectProperty()
    name = StringProperty('<?>')
    dot_state = OptionProperty('collapsed', options=['collapsed', 'expanded', 'expanding', 'collapsing'])
    font_size = NumericProperty()
    anim_off_x = NumericProperty()
    anim_off_y = NumericProperty()
    anim_off = ReferenceListProperty(anim_off_x, anim_off_y)
    offset_x = NumericProperty(0.)
    offset_y = NumericProperty(0.)
    offset = ReferenceListProperty(offset_x, offset_y)
    mode = NumericProperty(0)
    left = NumericProperty()
    top = NumericProperty()
    right = NumericProperty()
    bottom = NumericProperty()

    def collide_point(self, x, y):
        distance = sqrt(x**2 + y**2)
        if distance <= self.height / 2:
            return True
        return False

    def on_dot_state(self, *args):
        if self.dot_state in ('collapsed', 'expanded'):
            self.size = self._set_dimensions(self.dot_state)
            self.label.opacity = 0. if self.dot_state == 'collapsed' else 1.
        else:
            pass

    def on_touch_down(self, touch):
        if self.collide_point(*self.to_local(*touch.pos)):
            if self.dot_state == 'collapsed':
                self._expand()
                Clock.schedule_once(self._collapse, 2* self.transition_time + self.open_time)
            elif self.dot_state == 'expanded':
                self._collapse()
            else:
                pass
            return True
        return False

    def on_diameter(self, *args):
        if self.dot_state in ('collapsed', 'expanded'):
            self.size = self._set_dimensions(self.dot_state)
        else:
            Clock.schedule_once(self.on_diameter, .3)

    def on_offset(self, *args):
        if self.dot_state == 'collapsed':
            self.anim_off = (0., 0.)
        elif self.dot_state == 'expanded':
            self.anim_off = self.offset
        else:
            Clock.schedule_once(self.on_offset, .3)

    def _expand(self, *args):
        self.dot_state = 'expanding'

        target_width, target_height = self._set_dimensions('expanded')
        transition = 'out_elastic'

        background_anim = Animation(width=target_width, duration=self.transition_time, transition=transition)
        background_anim &=Animation(height=target_height, duration=self.transition_time, transition=transition)
        background_anim &=Animation(anim_off=self.offset, duration=self.transition_time, transition=transition)
        background_anim.bind(on_complete=self._expanded)

        label_anim = Animation(opacity=1., duration=self.transition_time, transition=transition)

        background_anim.start(self)
        label_anim.start(self.label)

    def _expanded(self, *args):
        self.dot_state = 'expanded'

    def _collapse(self, *args):
        self.dot_state = 'collapsing'

        target_width, target_height = self._set_dimensions('collapsed')
        transition = 'out_elastic'

        background_anim = Animation(width=target_width, duration=self.transition_time, transition=transition)
        background_anim &=Animation(height=target_height, duration=self.transition_time, transition=transition)
        background_anim &=Animation(anim_off=(0., 0.), duration=self.transition_time, transition=transition)
        background_anim.bind(on_complete=self._collapsed)

        label_anim = Animation(opacity=0., duration=self.transition_time, transition=transition)

        background_anim.start(self)
        label_anim.start(self.label)

    def _collapsed(self, *args):
        self.dot_state = 'collapsed'

    def get_offset(self):
        return (self.offset_x, self.offset_y)

    def _set_dimensions(self, state):
        if state == 'collapsed':
            height = self.diameter
            width = self.diameter
            return width, height
        if state == 'expanded':
            height = self.label.texture_size[1] * 1.1
            if height < self.diameter:
                height = self.diameter
            width = height * .7 + self.label.texture_size[0]
            if width < height:
                width = height
            return width, height




if __name__ == '__main__':
    from kivy.app import App
    from kivy.properties import DictProperty
    import json

    with open('config.json', 'r') as config_file:
        configuration = json.load(config_file)

    class FingerDotApp(App):
        colors = DictProperty(configuration['colors'])

        def build(self):
            root = FloatLayout()
            dot = FingerDot(pos=(200, 200),
                            diameter=50,
                            font_size= 70,
                            dot_state='collapsed',
                            background_color=self.colors['major'],
                            outline_color=self.colors['font'][:3] + [.0],
                            offset=(10, 10)
                            )
            root.add_widget(dot)
            return root

    FingerDotApp().run()
