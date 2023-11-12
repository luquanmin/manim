from manim import *

class NewtonSecondLaw(Scene):
    def construct(self):
        # 添加文本
        title = Tex("牛顿第二定律")
        title.scale(1.5)
        self.play(Write(title))

        # 添加物体和箭头
        object = Circle(radius=0.5, color=BLUE)
        object.move_to(LEFT * 3)
        arrow = Arrow(LEFT * 3, RIGHT * 3)
        self.play(Create(object), Create(arrow))

        # 添加标签
        object_label = Tex("物体")
        object_label.next_to(object, DOWN)
        arrow_label = Tex("力")
        arrow_label.next_to(arrow, DOWN)
        self.play(Write(object_label), Write(arrow_label))

        # 添加方程
        equation = Tex("F", "=", "m", "\\cdot", "a")
        equation.next_to(arrow, RIGHT)
        self.play(Write(equation))

        # 添加解释
        explanation = Tex("力等于物体的质量乘以加速度")
        explanation.next_to(equation, DOWN)
        self.play(Write(explanation))

        self.wait(2)