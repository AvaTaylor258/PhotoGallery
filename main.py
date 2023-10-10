from kivy.app import App
from kivy.uix.screenmanager import Screen

images = ["chick.jpg", "grogu.jpg"]
index = 0

class PhotoGalleryApp(App):
    pass

class Display(Screen):
    global index
    global images
    def display_image(self):
        return images[index]
    def advance(self):
        if index < len(images):
            index += 1
        else:
            index = 0
    def backwards(self):
        if index > len(images):
            index = 0
        else:
            index -= 1


PhotoGalleryApp().run()