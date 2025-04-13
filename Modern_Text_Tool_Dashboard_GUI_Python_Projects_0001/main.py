import uv
from uv import State  # ✅ Importing only 'State' correctly

class TextToolDashboard:
    def __init__(self):
        self.text = State("")
        self.result = State("")

    def analyze_text(self):
        text = self.text.get()
        word_count = len(text.split())
        char_count = len(text)
        self.result.set(f"Words: {word_count}, Characters: {char_count}")

    def transform_text(self, mode):
        text = self.text.get()
        if mode == "uppercase":
            self.result.set(text.upper())
        elif mode == "lowercase":
            self.result.set(text.lower())
        elif mode == "titlecase":
            self.result.set(text.title())
        elif mode == "remove_spaces":
            self.result.set(text.replace(" ", ""))

    def render(self):
        return uv.html.div(  # ✅ Using `uv.html.div`
            uv.html.h1("Text Tool Dashboard"),
            uv.html.textarea(value=self.text, placeholder="Enter your text here"),
            uv.html.button("Analyze", on_click=self.analyze_text),
            uv.html.button("Uppercase", on_click=lambda: self.transform_text("uppercase")),
            uv.html.button("Lowercase", on_click=lambda: self.transform_text("lowercase")),
            uv.html.button("Title Case", on_click=lambda: self.transform_text("titlecase")),
            uv.html.button("Remove Spaces", on_click=lambda: self.transform_text("remove_spaces")),
            uv.html.p(self.result)
        )

app = TextToolDashboard()
uv.run(app.render)  # ✅ Using `uv.run()`
