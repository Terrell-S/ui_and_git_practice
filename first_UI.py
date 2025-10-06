import flet as flt

def myapp(page: flt.Page):
    page.theme_mode = flt.ThemeMode.DARK
    text = flt.TextField(label='yo mama', 
                         value ='cool kids', 
                         color=flt.Colors.BLUE, 
                         text_size=30,
                         border_color= flt.Colors.WHITE
                         )
    text2 = flt.TextField(label='not yo mama', 
                         value ='cooler kids', 
                         color=flt.Colors.RED, 
                         text_size=50,
                         border_color= flt.Colors.WHITE
                         )
    page.add(text,text2)

    page.update()

flt.app(target=myapp)