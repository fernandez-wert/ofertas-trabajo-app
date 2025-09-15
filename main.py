from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

Window.clearcolor = (0.95, 0.95, 0.95, 1)

class OfertasApp(App):
    def build(self):
        ofertas = [
            "💼 Desarrollador Python - $2000 - Remoto",
            "🎨 Diseñador UX/UI - $1800 - Bogotá", 
            "📊 Analista de Datos - $2200 - Medellín",
            "🔧 Soporte Técnico - $1500 - Cali",
            "📱 Desarrollador Móvil - $2100 - Remoto"
        ]
        
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        titulo = Label(
            text="🎯 OFERTAS DE TRABAJO",
            size_hint_y=0.1,
            font_size='24sp',
            bold=True,
            color=(0.2, 0.4, 0.8, 1)
        )
        layout.add_widget(titulo)
        
        scroll = ScrollView()
        content = BoxLayout(orientation='vertical', size_hint_y=None, spacing=8)
        content.bind(minimum_height=content.setter('height'))
        
        for oferta in ofertas:
            btn = Button(
                text=oferta,
                size_hint_y=None,
                height=80,
                background_color=(0.3, 0.6, 0.9, 1),
                color=(1, 1, 1, 1),
                font_size='16sp'
            )
            content.add_widget(btn)
        
        scroll.add_widget(content)
        layout.add_widget(scroll)
        
        return layout

if __name__ == '__main__':
    OfertasApp().run()