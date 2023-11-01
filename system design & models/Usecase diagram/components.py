from manim import *
from manim.mobject.geometry.tips import ArrowTriangleTip
from colour import Color


class NameCart(VMobject):
    def __init__(self,
                 name: str = 'no name',
                 roll: str = 'YYDDDRRR',
                 dept: str = 'department',
                 scale_factor: float = 1,
                 ):
        super().__init__()
        self.paragraph = Paragraph(
            name,
            roll,
            dept,
            font='Segoe UI Historic',
            alignment='center',
            weight=BOLD,
        ).scale(scale_factor)
        self.add(self.paragraph)


class Actor(VMobject):
    def __init__(self,
                 actor_name,
                 body_shape_svg: str = 'human.svg'):
        super().__init__()
        self.actor_body = SVGMobject(body_shape_svg). \
            set(color=[DARK_BLUE, PURE_BLUE, DARK_BLUE]).scale(0.6)
        self.actor_name = Text(actor_name).scale(0.27)
        self.actor_name.next_to(self.actor_body, DOWN, buff=0.2)
        self.add(self.actor_body, self.actor_name)


class UseCase(VMobject):
    def __init__(self,
                 case_text: str = 'no text\nprovided',
                 text_alignment: str = 'center',
                 buff: float = 0.8,
                 surround_color: Color = BLUE_D,
                 scale_factor: float = 1):
        super().__init__()
        self.case = Paragraph(case_text, alignment=text_alignment)
        self.container = Ellipse(height=self.case.height + buff,
                                 width=self.case.width + 1.6 * buff,
                                 color=surround_color)
        self.case.move_to(self.container)
        self.add(self.container, self.case)
        self.scale(scale_factor)


class Include(DashedLine):
    def __init__(self,
                 _from=LEFT,
                 _to=RIGHT,
                 tip_data: str = 'no data provided',
                 bg_color=BLACK,
                 add_include_string: bool = True,
                 include_string_scale_factor: float = 0.2,
                 dash_length: float = 0.1,
                 dashed_ratio: float = 0.80,
                 tip_width: float = 0.05,
                 tip_length: float = 0.2,
                 tip_shape=ArrowTriangleTip):
        super().__init__(start=_from, end=_to, dash_length=dash_length, dashed_ratio=dashed_ratio)
        self.add_tip(tip_width=tip_width, tip_length=tip_length, tip_shape=tip_shape)
        if add_include_string:
            self.tip = Text('<< include >>', color=PURE_RED). \
                scale(include_string_scale_factor).move_to(self.get_center())
            self.tip_bg = BackgroundRectangle(self.tip, fill_color=bg_color, fill_opacity=1, buff=0.05). \
                set_y(self.get_y())
            self.add(self.tip_bg, self.tip.set_y(self.get_y()))


class Extend(VMobject):
    def __init__(self,
                 _from=LEFT,
                 _to=RIGHT,
                 tip_data: str = 'no data provided',
                 bg_color=BLACK,
                 path_arc=None):
        super().__init__()

        self._from = _from
        self._to = _to

        self.extend = DashedLine(start=self._from,
                                 end=self._to,
                                 path_arc=path_arc,
                                 buff=0.01,
                                 dash_length=0.2,
                                 dashed_ratio=0.82). \
            add_tip(tip_width=0.2, tip_length=0.2, tip_shape=ArrowTriangleTip, )
        self.tip = Text('<< extend >>', color=PURE_RED).scale(0.2).move_to(self.extend)
        self.tip_bg = BackgroundRectangle(self.tip, fill_color=bg_color, fill_opacity=1, buff=0.05)
        self.add(self.extend, self.tip_bg, self.tip)
