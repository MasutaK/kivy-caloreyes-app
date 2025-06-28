from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from camera_interface import take_picture
from food_analysis import analyze_image

class NutritionApp(App):
    def build(self):
        self.img_path = None
        self.layout = BoxLayout(orientation='vertical')
        self.img = Image(size_hint=(1, 0.5))
        self.result_label = Label(text="Résultat ici", size_hint=(1, 0.3))
        self.btn = Button(text="📸 Prendre une photo", size_hint=(1, 0.2))
        self.btn.bind(on_press=self.capture)
        self.layout.add_widget(self.img)
        self.layout.add_widget(self.btn)
        self.layout.add_widget(self.result_label)
        return self.layout

    def capture(self, instance):
        take_picture(self.process_image)

    def process_image(self, path):
        self.img_path = path
        self.img.source = path
        self.img.reload()
        self.result_label.text = "Analyse en cours..."
        Clock.schedule_once(lambda dt: self.run_analysis(), 0.5)

    def run_analysis(self):
        result = analyze_image(self.img_path)
        self.result_label.text = result

if __name__ == '__main__':
    NutritionApp().run()
