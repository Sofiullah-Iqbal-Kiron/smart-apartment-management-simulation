from manim import *
from components import Actor, UseCase, Extend, Include, NameCart


class Main(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        Paragraph.set_default(color=BLACK)
        Rectangle.set_default(color=BLACK)
        Line.set_default(color=RED)

        self.wait(1)

        # slide-1

        background = Rectangle(height=config.frame_height, width=config.frame_width). \
            set_color([GREEN_A, GREEN_B, GREEN_C]). \
            set_opacity(0.5)
        self.bring_to_back(background)
        self.play(FadeIn(background, run_time=0.5))

        heading = Group(
            Text('Smart Apartment Management Simulation', font='Lucida Fax', color=DARK_BLUE, weight=ULTRABOLD),
            Text('Digital দারোয়ান', font='Nirmala UI Semilight', color=DARK_GRAY, weight=SEMIBOLD)
        ).arrange(DOWN, buff=0.4).scale(0.8).move_to(UP * 3)

        heading_surrounder = RoundedRectangle(corner_radius=0.1, height=heading.height + 0.25,
                                              width=heading.width + 1.3, color=PURE_GREEN).move_to(heading)
        self.play(DrawBorderThenFill(heading[0]), DrawBorderThenFill(heading[1]), Create(heading_surrounder))

        subtitle = Text('Team Members', color=DARK_BROWN).scale(0.5).move_to(UP * 1.3)
        self.play(Write(subtitle))

        kiron = NameCart('Md. Kazi Iqbal Hossen', '18CSE265', 'Department of CSE', 0.5).set_opacity(0)
        mamlot = NameCart('Mamlot Ali', '18CSE234', 'Department of CSE', 0.5)
        shanto = NameCart('Solaiman Hossain', '18CSE220', 'Department of CSE', 0.5).set_opacity(0)

        self.play(
            kiron.animate.shift(LEFT * 5).set_opacity(1),
            GrowFromPoint(mamlot, ORIGIN),
            shanto.animate.shift(RIGHT * 5).set_opacity(1),

            run_time=1.7
        )

        logo = ImageMobject('Logo-removebg-preview.png').move_to(DOWN * 2.6).scale(0.8)
        self.play(FadeIn(logo))

        self.wait(3)

        self.clear()

        # slide-2

        features_heading = Text("Features").move_to(UP * 2.4)
        self.play(Write(features_heading))
        list_data_1 = "Simulate record system of residents entry/exit for security purpose."
        list_data_2 = "View and manage all residents profile."
        list_data_3 = "Residents raises issues and admin-owner handles them from complain page at admin-view."
        features = BulletedList(
            list_data_1,
            list_data_2,
            list_data_3
        ).scale(0.65)
        features.set_color_by_tex(list_data_1, PURE_RED)
        features.set_color_by_tex(list_data_2, PURE_GREEN)
        features.set_color_by_tex(list_data_3, PURE_BLUE)
        self.play(Create(features, run_time=4))

        self.wait(2)

        self.clear()

        # slide-3

        self.play(ShowCreationThenFadeOut(Text('Module - 0: Entire Overview of the System'), run_time=1.5))

        cases_text = [
            "Login",  # 0
            "Record\nresidents/guests\nentry/exit",  # 1
            "Register/Unregister\na resident/guard",  # 2
            "Request for\na temporary token",  # 3
            "Generate and return\na temporary token",  # 4
            "Verify\nresident, guest, token",  # 5
            "Handle Issues",  # 6
            "Pay rent\nand utility bills",  # 7
            "Manage\nresident/guest data"  # 8
        ]

        cases = [UseCase(case, 0.5).scale(0.5) for case in cases_text]
        cases[0].move_to([0, 2.5, 0])
        cases[1].move_to([-2, 1.5, 0])
        cases[2].move_to([-2, -2.5, 0])
        cases[3].move_to([2, 1.5, 0])
        cases[4].move_to([2, 0, 0])
        cases[5].move_to([2, -2.5, 0])
        cases[6].move_to([-2, 0, 0])
        cases[7].move_to([2, -1.18, 0])
        cases[8].move_to([-2, -1.18, 0])

        system_heading = Text("Smart Apartment Management Simulation",
                              weight=BOLD,
                              font_size=18,
                              font='Lucida Sans Typewriter',
                              color=DARK_GRAY).next_to(Group(*cases), UP * 1.6)
        system = Group(*cases, system_heading)
        system_rectangle = RoundedRectangle(corner_radius=0.1, height=system.height + 1.1, width=system.width + 0.5). \
            surround(system).set_stroke(width=4, opacity=1)
        self.play(GrowFromCenter(Group(system, system_rectangle).move_to(ORIGIN)))

        # Actors.
        guard_or_ai_detector = Group(Actor('Guard'), Actor('AI Detector')).arrange(RIGHT, buff=0.3)
        guard_or_ai_detector_container = RoundedRectangle(corner_radius=0.1, height=guard_or_ai_detector.height + 0.5,
                                                          width=guard_or_ai_detector.width + 0.3). \
            move_to([-6, 1.5, 0])
        guard_or_ai_detector.move_to(guard_or_ai_detector_container)
        admin = Actor('Admin or Owner').move_to([-6, -1.5, 0])
        resident = Actor('Resident').move_to([6, 1.5, 0])
        backend_server = Actor('Backend Server').move_to([6, -1.5, 0])
        self.play(FadeIn(guard_or_ai_detector),
                  FadeIn(guard_or_ai_detector_container),
                  FadeIn(admin),
                  FadeIn(resident),
                  FadeIn(backend_server),
                  run_time=2)

        associations = [
            (guard_or_ai_detector_container.get_right(), cases[0].get_left()),
            (guard_or_ai_detector_container.get_right(), cases[1].get_left()),
            (admin.get_right(), cases[2].get_left()),
            (admin.get_right(), cases[6].get_left()),
            (admin.get_right(), cases[8].get_left()),
            (resident.get_left(), cases[0].get_right()),
            (resident.get_left(), cases[3].get_right()),
            (resident.get_left(), cases[7].get_right()),
            (backend_server.get_left(), cases[4].get_right()),
            (backend_server.get_left(), cases[5].get_right()),
        ]

        for association in associations:
            self.play(Create(Line(start=association[0], end=association[1], buff=0.02, color='#0891b2')))

        relations = [
            {"_from": cases[4].get_top(), "_to": cases[3].get_bottom(), "type": "exclude"},
            {"_from": cases[0].get_bottom(), "_to": cases[5].get_corner(UL), "type": "include"},
            {"_from": cases[3].get_left(), "_to": cases[0].get_right(), "type": "exclude"},
            {"_from": cases[1].get_right(), "_to": cases[0].get_left(), "type": "exclude"},
        ]

        for relation in relations:
            if relation['type'] == 'include':
                self.play(FadeIn(Include(relation['_from'], relation['_to'], bg_color=WHITE)))
            else:
                self.play(FadeIn(Extend(relation['_from'], relation['_to'], bg_color=WHITE)))

        self.wait(4)

        self.clear()

        # slide-4
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        Paragraph.set_default(color=BLACK)
        Rectangle.set_default(color=BLACK)
        Line.set_default(color=RED)

        self.play(ShowCreationThenFadeOut(Text('Module - 1: ResidentView'), run_time=1.5))

        # usecases
        cases_text = [
            "Login",  # 0
            "Request for a\ntemp token",  # 1
            "Verify\nCredentials",  # 2
            "Generate and\nreturn token",  # 3
            "Pay rent and\nutility bills",  # 4
            "Raise an issue",  # 5
            "Handle issues",  # 6
        ]

        cases = [UseCase(case, width=6.5, height=3.2).scale(0.30) for case in cases_text]
        cases[0].move_to([0, 3, 0])
        cases[1].move_to([-3, 2, 0])
        cases[2].move_to([3, 2, 0])
        cases[3].move_to([3, 0, 0])
        cases[4].move_to([-3, 0, 0])
        cases[5].move_to([-3, -2, 0])
        cases[6].move_to([3, -2, 0])

        cases_group = Group(*cases)
        system_heading = Text("Module-1: ResidentView",
                              weight=BOLD,
                              font_size=18,
                              font='Lucida Sans Typewriter',
                              color=DARK_GRAY).next_to(cases_group, UP * 1.6)
        system = Group(cases_group, system_heading)
        system_rectangle = RoundedRectangle(corner_radius=0.1, height=system.height + 1.1, width=system.width + 0.8). \
            surround(system).set_stroke(width=4, opacity=1)
        # self.add(Group(system, system_rectangle).move_to(ORIGIN))
        self.play(GrowFromCenter(Group(system, system_rectangle).move_to([0, 0, 0])))

        # actors
        resident = Actor('Resident').move_to([-6, 0, 0])
        backend_server = Actor('Backend Server').move_to([6, 1.5, 0])
        admin = Actor('Admin or Owner').move_to([6, -1.5, 0])
        # self.add(resident, backend_server, admin)
        self.play(FadeIn(resident),
                  FadeIn(backend_server),
                  FadeIn(admin),
                  run_time=2)

        # associations
        self.play(Create(
            Line(start=resident.get_right(), end=cases[0].get_left(), path_arc=-1.7, buff=0.02, color='#0891b2')))
        associations = [
            (resident.get_right(), cases[1].get_left()),
            (resident.get_right(), cases[4].get_left()),
            (resident.get_right(), cases[5].get_left()),
            (backend_server.get_left(), cases[2].get_right()),
            (backend_server.get_left(), cases[3].get_right()),
            (admin.get_left(), cases[6].get_right())
        ]

        for association in associations:
            self.play(Create(Line(start=association[0], end=association[1], buff=0.02, color='#0891b2')))
            # self.add(Line(start=association[0], end=association[1], buff=0.02, color='#0891b2'))

        relations = [
            {"_from": cases[0].get_right(), "_to": cases[2].get_left(), "type": "include"},
            {"_from": cases[1].get_right(), "_to": cases[0].get_left(), "type": "exclude"},
            {"_from": cases[4].get_right(), "_to": cases[0].get_bottom(), "type": "exclude"},
            {"_from": cases[3].get_left(), "_to": cases[1].get_bottom(), "type": "exclude"},
            {"_from": cases[6].get_left(), "_to": cases[5].get_right(), "type": "exclude"},
        ]

        for relation in relations:
            if relation['type'] == 'include':
                self.play(Create(Include(relation['_from'], relation['_to'], bg_color=WHITE)))
            else:
                self.play(Create(Extend(relation['_from'], relation['_to'], bg_color=WHITE)))

        self.wait(4)

        self.clear()

        background = Rectangle(height=config.frame_height, width=config.frame_width). \
            set_color([TEAL_B, GREEN, TEAL_E]). \
            set_opacity(0.7)
        self.play(FadeIn(background, run_time=0.5))
        self.bring_to_back(background)

        Paragraph.set_default(color=WHITE, alignment='left')
        Text.set_default(color=BLACK, weight=BOLD)

        t0 = MobjectTable(
            table=[
                [
                    Paragraph(
                        "Request for a temporary token(login first)\nto allow his guests inside the apartment.\nProvide this token to his guest using any 3'rd party medium.").scale(
                        0.6)
                ],
                [
                    Paragraph(
                        "Pays room rent and other utility bills via any banking system\nand provide transaction number to this system as a proof.").
                    scale(0.6)
                ],
                [
                    Paragraph("Write a complain in details at the complain box\nand submit to the admin/owner.").
                    scale(0.6)
                ],
            ],
            row_labels=[
                Text("Request for a\n temp token").scale(0.6),
                Text("Pay rent\nand utility bills").scale(0.6),
                Text("Raise an issue").scale(0.6),
            ],
            col_labels=[
                Text("Description")
            ],
            top_left_entry=Text("Usecase"),
            include_outer_lines=True,
            line_config={"color": PURE_BLUE, "stroke_width": 4},
        ).scale(0.6)

        caption = Text(
            "ResidentView: Table description",
            font="Consolas",
            font_size=40,
            weight=ULTRABOLD,
            color=YELLOW).next_to(t0, UP, buff=MED_LARGE_BUFF)

        Group(caption, t0).move_to(ORIGIN)
        self.play(Write(caption))
        self.play(DrawBorderThenFill(t0))

        self.wait(3)

        self.clear()

        # slide-5
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        Paragraph.set_default(color=BLACK)
        Rectangle.set_default(color=BLACK)
        Line.set_default(color=RED)

        self.play(ShowCreationThenFadeOut(Text('Module - 2: AdminView'), run_time=1.5))

        # usecases
        cases_text = [
            "Resigter a\nguard/resident",  # 0
            "Allot a block\nto a resident",  # 1
            "Manage/edit/delete\nand save\nguard/residents data",  # 2
            "Raise an issue",  # 3
            "Handle an issue",  # 4
        ]

        cases = [UseCase(case, width=7.5, height=3.9).scale(0.25) for case in cases_text]
        cases[0].move_to([0, 3, 0])
        cases[1].move_to([-3, 1.5, 0])
        cases[2].move_to([0, 0, 0])
        cases[3].move_to([3, 0, 0])
        cases[4].move_to([0, -3, 0])

        cases_group = Group(*cases)
        system_heading = Text("Module-2: AdminView",
                              weight=BOLD,
                              font_size=18,
                              font='Lucida Sans Typewriter',
                              color=DARK_GRAY).next_to(cases_group, UP * 1.6)
        system = Group(cases_group, system_heading)
        system_rectangle = RoundedRectangle(corner_radius=0.1, height=system.height + 0.5, width=system.width + 0.5). \
            surround(system).set_stroke(width=4, opacity=1)
        # self.add(Group(system, system_rectangle).move_to(ORIGIN))
        self.play(GrowFromCenter(Group(system, system_rectangle).move_to([0, 0, 0])))

        # actors
        admin = Actor('Admin or Owner').move_to([-6, -0.25, 0])
        resident = Actor('Resident').move_to([6, -0.25, 0])
        # self.add(admin, resident)
        self.play(FadeIn(admin), FadeIn(resident))

        # associations
        self.play(
            Create(Line(start=admin.get_right(), end=cases[0].get_left(), path_arc=-1.7, buff=0.02, color='#0891b2')))
        associations = [
            (admin.get_right(), cases[1].get_left()),
            (admin.get_right(), cases[2].get_left()),
            (admin.get_right(), cases[4].get_left()),
            (resident.get_left(), cases[3].get_right()),
        ]

        for association in associations:
            self.play(Create(Line(start=association[0], end=association[1], buff=0.02, color='#0891b2')))
            # self.add(Line(start=association[0], end=association[1], buff=0.02, color='#0891b2'))

        relations = [
            {"_from": cases[1].get_right(), "_to": cases[0].get_left(), "type": "exclude", "path_arc": None},
            {"_from": cases[2].get_top(), "_to": cases[0].get_bottom(), "type": "exclude", "path_arc": None},
            {"_from": cases[4].get_right(), "_to": cases[3].get_bottom(), "type": "exclude", "path_arc": None},
        ]

        for relation in relations:
            if relation['type'] == 'include':
                self.play(Create(Include(relation['_from'], relation['_to'], bg_color=WHITE)))
            else:
                self.play(
                    Create(Extend(relation['_from'], relation['_to'], bg_color=WHITE, path_arc=relation['path_arc'])))

        self.wait(4)

        self.clear()

        background = Rectangle(height=config.frame_height, width=config.frame_width). \
            set_color([TEAL_B, GREEN, TEAL_E]). \
            set_opacity(0.7)
        self.play(FadeIn(background, run_time=0.5))
        self.bring_to_back(background)

        Paragraph.set_default(color=WHITE, alignment='left')
        Text.set_default(color=BLACK, weight=BOLD)

        t0 = MobjectTable(
            table=[
                [
                    Paragraph(
                        "Gather information about guard/residents\nand enter into the system database.").scale(
                        0.6)
                ],
                [
                    Paragraph(
                        "Allocate and assign a block from apartment to the\nresident who has already registered.").scale(
                        0.6)],
                [Paragraph("Manage/Edit/Delete/Save resident/guards data from Admin-Panel.").scale(
                    0.6)],
                [Paragraph(
                    "View issues from issues panel and\ntake necessary action to resolve this particular problem.").scale(
                    0.6)],
            ],
            row_labels=[
                Text("Register a guard/resident").scale(0.6),
                Text("Allot a block\nto a resident").scale(0.6),
                Text("Manage\nresident/guards data").scale(0.6),
                Text("Handle issues").scale(0.6),
            ],
            col_labels=[
                Text("Description")
            ],
            top_left_entry=Text("Usecase"),
            include_outer_lines=True,
            line_config={"color": PURE_BLUE, "stroke_width": 4},
        ).scale(0.6)

        caption = Text(
            "AdminView: Table description",
            font="Consolas",
            font_size=40,
            weight=ULTRABOLD,
            color=YELLOW).next_to(t0, UP, buff=MED_LARGE_BUFF)

        Group(caption, t0).move_to(ORIGIN)
        self.play(Write(caption))
        self.play(DrawBorderThenFill(t0))

        self.wait(3)

        self.clear()

        # slide-5
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        Paragraph.set_default(color=BLACK)
        Rectangle.set_default(color=BLACK)
        Line.set_default(color=RED)

        self.play(ShowCreationThenFadeOut(Text('Module - 3: GuardView'), run_time=1.5))

        # usecases
        cases_text = [
            "Login",  # 0
            "Record residents\nentry/exit",  # 1
            "Verify credentials",  # 2
            "Sought temp\ntoken from guest",  # 3
            "Take guests\nphoto, nid\nthen save",  # 4
            "Record guests\nentry/exit",  # 5
            "Verify token",  # 6
        ]

        cases = [UseCase(case, width=6.9, height=3.4).scale(0.25) for case in cases_text]
        cases[0].move_to([0, 3, 0])
        cases[1].move_to([-3, 2, 0])
        cases[2].move_to([3, 2, 0])
        cases[3].move_to([-3, 0.7, 0])
        cases[4].move_to([-3, -1.5, 0])
        cases[5].move_to([-3, -3, 0])
        cases[6].move_to([3, -2, 0])

        cases_group = Group(*cases)
        system_heading = Text("Module-3: GuardView",
                              weight=BOLD,
                              font_size=18,
                              font='Lucida Sans Typewriter',
                              color=DARK_GRAY).next_to(cases_group, UP * 1.6)
        system = Group(cases_group, system_heading)
        system_rectangle = RoundedRectangle(corner_radius=0.1, height=system.height + 0.6, width=system.width + 0.5). \
            surround(system).set_stroke(width=4, opacity=1)
        # self.add(Group(system, system_rectangle).move_to(ORIGIN))
        self.play(GrowFromCenter(Group(system, system_rectangle).move_to([0, 0, 0])))

        # actors
        guard = Actor('Guard').move_to([-6, -0.25, 0])
        backend_server = Actor('Backend Server').move_to([6, -0.25, 0])
        # self.add(guard, backend_server)
        self.play(FadeIn(guard), FadeIn(backend_server))

        # associations
        self.play(
            Create(Line(start=guard.get_right(), end=cases[0].get_left(), path_arc=-1.7, buff=0.02, color='#0891b2')))
        associations = [
            (guard.get_right(), cases[1].get_left()),
            (guard.get_right(), cases[3].get_left()),
            (guard.get_right(), cases[4].get_left()),
            (guard.get_right(), cases[5].get_left()),
            (backend_server.get_left(), cases[2].get_right()),
            (backend_server.get_left(), cases[6].get_right()),
        ]

        for association in associations:
            self.play(Create(Line(start=association[0], end=association[1], buff=0.02, color='#0891b2')))
            # self.add(Line(start=association[0], end=association[1], buff=0.02, color='#0891b2'))

        relations = [
            {"_from": cases[0].get_bottom(), "_to": cases[2].get_left(), "type": "include", "path_arc": 1},
            {"_from": cases[3].get_right(), "_to": cases[6].get_left(), "type": "include", "path_arc": None},
            {"_from": cases[4].get_top(), "_to": cases[3].get_bottom(), "type": "exclude", "path_arc": 0.5},
            {"_from": cases[5].get_right(), "_to": cases[4].get_right(), "type": "exclude", "path_arc": 0.9},
        ]

        for relation in relations:
            if relation['type'] == 'include':
                self.play(Create(Include(relation['_from'], relation['_to'], bg_color=WHITE)))
            else:
                self.play(
                    Create(Extend(relation['_from'], relation['_to'], bg_color=WHITE, path_arc=relation['path_arc'])))

        self.wait(4)

        self.clear()

        background = Rectangle(height=config.frame_height, width=config.frame_width). \
            set_color([TEAL_B, GREEN, TEAL_E]). \
            set_opacity(0.7)
        self.play(FadeIn(background, run_time=0.5))
        self.bring_to_back(background)

        Paragraph.set_default(color=WHITE, alignment='left')
        Text.set_default(color=BLACK, weight=BOLD)

        t0 = MobjectTable(
            table=[
                [
                    Paragraph(
                        "Search a resident/guest by his access-token/resident-id\nand record their entry/exit with a timestamp\nusing guard interface.").scale(
                        0.6)
                ],
                [
                    Paragraph(
                        "Sought temp token from a guest who wants to access entry into\nthe apartment.").
                    scale(0.6)
                ],
                [Paragraph(
                    "Take guest information, photo, nid and save into the database\nif guests temp token is valid.").
                    scale(0.6)
                 ],
                [Paragraph(
                    "If all above are verified and done,\nrecord guests entry/exit.").
                    scale(0.6)
                 ],
            ],
            row_labels=[
                Text("Record residents\nentry/exit").scale(0.6),
                Text("Sought temp token\nfrom guest").scale(0.6),
                Text("Take guest photo, nid\nthen save").scale(0.6),
                Text("Record guests entry/exit").scale(0.6),
            ],
            col_labels=[
                Text("Description")
            ],
            top_left_entry=Text("Usecase"),
            include_outer_lines=True,
            line_config={"color": PURE_BLUE, "stroke_width": 4},
        ).scale(0.6)

        caption = Text(
            "GuardView: Table description",
            font="Consolas",
            font_size=40,
            weight=ULTRABOLD,
            color=YELLOW).next_to(t0, UP, buff=MED_LARGE_BUFF)

        Group(caption, t0).move_to(ORIGIN)
        self.play(Write(caption))
        self.play(DrawBorderThenFill(t0))

        self.wait(3)
        self.clear()
        thank_you = Text("Thank You.", font_size=54)
        self.play(SpiralIn(thank_you))
        self.play(Circumscribe(thank_you, buff=0.6))
        self.wait(3)


class TitleTest(Scene):
    def construct(self):
        self.wait(0.5)
        title = Title("Manim Title",
                      include_underline=True,
                      match_underline_width_to_text=False,
                      underline_buff=SMALL_BUFF)
        self.play(Create(title))
        self.play(SpiralIn(Text("Kiron Here PackUP.")))
        self.play(Write(Line(start=LEFT * 3, end=RIGHT * 3).shift(DOWN * 2.5)))
        self.wait(2)


class Test(Scene):
    def construct(self):
        self.camera.background_color = DARKER_GREY

        self.add(UseCase("Hello\nWorld"))
