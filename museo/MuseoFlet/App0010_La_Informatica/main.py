import flet as ft
from flet import AppBar, ElevatedButton, View

def main(page: ft.Page):
    page.title = "La historia de la Informática"
    page.bgcolor = "#7FFFD4"
    page.window_width = 650
    page.window_height = 800
    
    image_width_Portada = 800
    image_height_Portada = 400
    
    img_height = 100
    img_width = 100
    border_radius = 25  # Ajusta el valor para el radio del borde

    # Audios Padres de la informática
    intro = ft.Audio(src="Intro.mp3", volume=1, balance=0)
    page.overlay.append(intro)
    
    Pascal = ft.Audio(src="Pascal.mp3", volume=1, balance=0)
    page.overlay.append(Pascal)
    
    Leibniz = ft.Audio(src="Leibniz.mp3", volume=1, balance=0)
    page.overlay.append(Leibniz)
    
    Babbage = ft.Audio(src="Babbage.mp3", volume=1, balance=0)
    page.overlay.append(Babbage)
    
    Lovelace = ft.Audio(src="Lovelace.mp3", volume=1, balance=0) 
    page.overlay.append(Lovelace)
    
    Hollerith = ft.Audio(src="Hollerith.mp3", volume=1, balance=0)
    page.overlay.append(Hollerith)
    
    Turing = ft.Audio(src="Turing.mp3", volume=1, balance=0)
    page.overlay.append(Turing)
    
    Neumann = ft.Audio(src="Neumann.mp3", volume=1, balance=0)
    page.overlay.append(Neumann)
    
    Shannon = ft.Audio(src="shannon.mp3", volume=1, balance=0)
    page.overlay.append(Shannon)
    
    Hopper = ft.Audio(src="Hopper.mp3", volume=1, balance=0)
    page.overlay.append(Hopper)
    
    McCarthy = ft.Audio(src="McCarthy.mp3", volume=1, balance=0)
    page.overlay.append(McCarthy)
    
    Berners = ft.Audio(src="Berners.mp3", volume=1, balance=0)
    page.overlay.append(Berners)
    
    Ritchie = ft.Audio(src="Ritchie.mp3", volume=1, balance=0)
    page.overlay.append(Ritchie)
    
    Thompson = ft.Audio(src="Thompson.mp3", volume=1, balance=0)
    page.overlay.append(Thompson)
    
    Gosling = ft.Audio(src="Gosling.mp3", volume=1, balance=0)
    page.overlay.append(Gosling)
    
    Jobs = ft.Audio(src="Jobs.mp3", volume=1, balance=0)
    page.overlay.append(Jobs)
    
    Wozniak= ft.Audio(src="Wozniak.mp3", volume=1, balance=0)
    page.overlay.append(Wozniak)
    
    Gates = ft.Audio(src="Gates.mp3", volume=1, balance=0)
    page.overlay.append(Gates)
    
    Zuckerberg = ft.Audio(src="Zuckerberg.mp3", volume=1, balance=0)
    page.overlay.append(Zuckerberg)
    
    Pages = ft.Audio(src="Pages.mp3", volume=1, balance=0)
    page.overlay.append(Pages)
    
    Brin = ft.Audio(src="Brin.mp3", volume=1, balance=0)
    page.overlay.append(Brin)

    #Audios de la historia de las computadoras
    primerageneracion = ft.Audio(src="Primera generacion.mp3", volume=1, balance=0)
    page.overlay.append(primerageneracion)
    segundageneracion = ft.Audio(src="Segunda generacion.mp3", volume=1, balance=0)
    page.overlay.append(segundageneracion)
    tercerageneracion = ft.Audio(src="Tercera generacion.mp3", volume=1, balance=0)
    page.overlay.append(tercerageneracion)
    cuartageneracion = ft.Audio(src="Cuarta generacion.mp3", volume=1, balance=0)
    page.overlay.append(cuartageneracion)
    quintageneracion = ft.Audio(src="Quinta generacion.mp3",volume=1, balance=0)
    page.overlay.append(quintageneracion)
    sextageneracion = ft.Audio(src="Sexta generacion.mp3", volume=1, balance= 0)
    page.overlay.append(sextageneracion)
    
    #audios lenguajes relevantes
    c = ft.Audio(src="C#.mp3", volume=1, balance=0)
    page.overlay.append(c)
    html = ft.Audio(src="HTML.mp3", volume=1, balance=0)
    page.overlay.append(html)
    java = ft.Audio(src="JAVA.mp3", volume=1, balance=0)
    page.overlay.append(java)
    javas = ft.Audio(src="javascript.mp3", volume=1, balance=0)
    page.overlay.append(javas)
    perl = ft.Audio(src="PERL.mp3", volume=1, balance=0)
    page.overlay.append(perl)
    python = ft.Audio(src="python.mp3", volume=1, balance=0)
    page.overlay.append(python)
    rust = ft.Audio(src="RUST.mp3", volume=1, balance=0)
    page.overlay.append(rust)
    sql = ft.Audio(src="SQL.mp3", volume=1, balance=0)
    page.overlay.append(sql)
    swift = ft.Audio(src="SWIFT.mp3", volume=1, balance=0)
    page.overlay.append(swift)
    
    #Tecnologia en el futuro audios
    
    seguridad = ft.Audio(src="ciberseguridad.mp3", volume=1, balance=0)
    page.overlay.append(seguridad)
    cuantica = ft.Audio(src="Computacion cuantica.mp3", volume=1, balance=0)
    page.overlay.append(cuantica)
    block = ft.Audio(src="computacionblockchain.mp3", volume=1, balance=0)
    page.overlay.append(block)
    software = ft.Audio(src="Desarrollo de Software Low-Code y No-Code.mp3", volume=1, balance=0)
    page.overlay.append(software)
    etica = ft.Audio(src="ETICA Y REGULACION.mp3", volume=1, balance=0)
    page.overlay.append(etica)
    ia = ft.Audio(src="ia EN UNOS AÑOS.mp3", volume=1, balance=0)
    page.overlay.append(ia)
    internet = ft.Audio(src="INTERNET DE LAS COSAS.mp3", volume=1, balance=0)
    page.overlay.append(internet)
    
        #Audios Evolucion de lenguajes

    Definición = ft.Audio(src="Definición.mp3", volume=1, balance=0)
    page.overlay.append(Definición)

    primer1843 = ft.Audio(src="primer1843.mp3", volume=1, balance=0)
    page.overlay.append(primer1843)
    
    Assembler = ft.Audio(src="Assembler.mp3", volume=1, balance=0)
    page.overlay.append(Assembler)
    
    Fortran = ft.Audio(src="Fortran.mp3", volume=1, balance=0)
    page.overlay.append(Fortran)
    
    List= ft.Audio(src="List.mp3", volume=1, balance=0)
    page.overlay.append(List)
    
    Cobol = ft.Audio(src="Cobol.mp3", volume=1, balance=0) 
    page.overlay.append(Cobol)
    
    Basic = ft.Audio(src="Basic.mp3", volume=1, balance=0)
    page.overlay.append(Basic)
    
    C = ft.Audio(src="C.mp3", volume=1, balance=0)
    page.overlay.append(C)
    
    Pascal1970 = ft.Audio(src="Pascal1970.mp3", volume=1, balance=0)
    page.overlay.append(Pascal1970)
    
    Ada1980 = ft.Audio(src="Ada1980.mp3", volume=1, balance=0)
    page.overlay.append(Ada1980)
    
    Cmasmas = ft.Audio(src="Cmasmas.mp3", volume=1, balance=0)
    page.overlay.append(Cmasmas)
    
    Perl = ft.Audio(src="Perl.mp3", volume=1, balance=0)
    page.overlay.append(Perl)
    
    Python = ft.Audio(src="Python.mp3", volume=1, balance=0)
    page.overlay.append(Python)
    
    VisualBasic = ft.Audio(src="VisualBasic.mp3", volume=1, balance=0)
    page.overlay.append(VisualBasic)
    
    Ruby = ft.Audio(src="Ruby.mp3", volume=1, balance=0)
    page.overlay.append(Ruby)
    
    PHP = ft.Audio(src="PHP.mp3", volume=1, balance=0)
    page.overlay.append(PHP)
    
    Java = ft.Audio(src="Java.mp3", volume=1, balance=0)
    page.overlay.append(Java)
    
    Javascript= ft.Audio(src="Javascript.mp3", volume=1, balance=0)
    page.overlay.append(Javascript)
    
    Csharp = ft.Audio(src="Csharp.mp3", volume=1, balance=0)
    page.overlay.append(Csharp)
    
    Scala = ft.Audio(src="Scala.mp3", volume=1, balance=0)
    page.overlay.append(Scala)
    
    RubyOnRails = ft.Audio(src="RubyOnRails.mp3", volume=1, balance=0)
    page.overlay.append(RubyOnRails)
    
    def StopAll():
        intro.pause()
        Pascal.pause()
        Leibniz.pause()
        Babbage.pause()
        Lovelace.pause()
        Hollerith.pause()
        Turing.pause()
        Neumann.pause()
        Shannon.pause()
        Hopper.pause()
        McCarthy.pause()
        Berners.pause()
        Ritchie.pause()
        Thompson.pause()
        Gosling.pause()
        Jobs.pause()
        Wozniak.pause()
        Gates.pause()
        Zuckerberg.pause()
        Pages.pause()
        Brin.pause()
        primerageneracion.pause()
        segundageneracion.pause()
        tercerageneracion.pause()
        cuartageneracion.pause()
        quintageneracion.pause()
        sextageneracion.pause()
        c.pause()
        html.pause()
        java.pause()
        javas.pause()
        perl.pause()
        rust.pause()
        sql.pause()
        python.pause()
        swift.pause()
        seguridad.pause()
        cuantica.pause()
        block.pause()
        software.pause()
        etica.pause()
        ia.pause()
        internet.pause()
        Definición.pause()
        primer1843.pause()
        Assembler.pause()
        Fortran.pause()
        List.pause()
        Cobol.pause()
        Pascal1970.pause()
        Ada1980.pause()
        Cmasmas.pause()
        Perl.pause()
        Python.pause()
        VisualBasic.pause()
        Ruby.pause()
        PHP.pause()
        Java.pause()
        Javascript.pause()
        Csharp.pause()
        Scala.pause()
        RubyOnRails.pause()
    
    def play_intro(e):
        StopAll()
        intro.play()
        
    def play_pascal(e):
        StopAll()
        Pascal.play()
        
    def play_leibniz(e):
        StopAll()
        Leibniz.play()
        
    def play_babbage(e):
        StopAll()
        Babbage.play()
        
    def play_lovelace(e):    
        StopAll()
        Lovelace.play()
        
    def play_hollerith(e):
        StopAll()
        Hollerith.play()
        
    def play_turing(e):
        StopAll()
        Turing.play()
    
    def play_neumann(e):
        StopAll()
        Neumann.play()
        
    def play_shannon(e):
        StopAll()
        Shannon.play()
    
    def play_hopper(e):
        StopAll()
        Hopper.play()
    
    def play_mccarthy(e):
        StopAll()
        McCarthy.play()
    
    def play_berners(e):
        StopAll()
        Berners.play()
    
    def play_ritchie(e):
        StopAll()
        Ritchie.play()
        
    def play_thompson(e):
        StopAll()
        Thompson.play()
        
    def play_gosling(e):
        StopAll()
        Gosling.play()
        
    def play_jobs(e):
        StopAll()
        Jobs.play()
        
    def play_wozniak(e):
        StopAll()
        Wozniak.play()
        
    def play_gates(e):
        StopAll()
        Gates.play()
    
    def play_zuckerberg(e):
        StopAll()
        Zuckerberg.play()
    
    def play_pages(e):
        StopAll()
        Pages.play()
    
    def play_brin(e):
        StopAll()
        Brin.play()
        
    def play_primerageneracion(e):
        StopAll()
        primerageneracion.play()
        
    def play_segundageneracion(e):
        StopAll()
        segundageneracion.play()
        
    def play_tercerageneracion(e):
        StopAll()
        tercerageneracion.play()
        
    def play_cuartageneracion(e):
        StopAll()
        cuartageneracion.play()
        
    def play_quintageneracion(e):
        StopAll()
        quintageneracion.play()
        
    def play_sextageneracion(e):
        StopAll()
        sextageneracion.play()
    
    def play_c(e):
        StopAll()
        c.play()    
        
    def play_html(e):
        StopAll()
        html.play()
        
    def play_java(e):
        StopAll()
        java.play()
        
    def play_javas(e):
        StopAll()
        javas.play()
        
    def play_perl(e):
        StopAll()
        perl.play()
        
    def play_python(e):
        StopAll()
        python.play()
        
    def play_rust(e):
        StopAll()
        rust.play()
        
    def play_sql(e):
        StopAll()
        sql.play()
    
    def play_swift(e):
        StopAll()
        swift.play()
        
    def play_seguridad(e):
        StopAll()
        seguridad.play()
    
    def play_cuantica(e):
        StopAll()
        cuantica.play()
        
    def play_block(e):
        StopAll()
        block.play()
        
    def play_software(e):
        StopAll()
        software.play()
        
    def play_etica(e):
        StopAll()
        etica.play()
        
    def play_ia(e):
        StopAll()
        ia.play()
        
    def play_internet(e):
        StopAll()
        internet.play()
    
    def play_Definicion(e):
        StopAll()
        Definición.play()
        
    def play_primer1843(e):
        StopAll()
        primer1843.play()

    def play_Assembler(e):
        StopAll()
        Assembler.play()

    def play_Fortran(e):
        StopAll()
        Fortran.play()

    def play_List(e):
        StopAll()
        List.play()

    def play_Cobol(e):
        StopAll()
        Cobol.play()

    def play_Pascal1970(e):
        StopAll()
        Pascal1970.play()

    def play_Ada1980(e):
        StopAll()
        Ada1980.play()

    def play_Cmasmas(e):
        StopAll()
        Cmasmas.play()

    def play_Perl(e):
        StopAll()
        Perl.play()

    def play_Python(e):
        StopAll()
        Python.play()

    def play_VisualBasic(e):
        StopAll()
        VisualBasic.play()

    def play_Ruby(e):
        StopAll()
        Ruby.play()

    def play_PHP(e):
        StopAll()
        PHP.play()

    def play_Java(e):
        StopAll()
        Java.play()

    def play_Javascript(e):
        StopAll()
        Javascript.play()

    def play_Csharp(e):
        StopAll()
        Csharp.play()

    def play_Scala(e):
        StopAll()
        Scala.play()

    def play_RubyOnRails(e):
        StopAll()
        RubyOnRails.play()

        
    # Botones Padres de la informática con imágenes y etiquetas semánticas
    btn1 = ElevatedButton(content=ft.Image(src="Pascal.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Blaise Pascal"), on_click=play_pascal)
    btn2 = ElevatedButton(content=ft.Image(src="Leibniz.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Gottfried Wilhelm Leibniz"), on_click=play_leibniz)
    btn3 = ElevatedButton(content=ft.Image(src="babbage.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Charles Babbage"), on_click=play_babbage)
    btn4 = ElevatedButton(content=ft.Image(src="Lovelace.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Ada Lovelace"), on_click=play_lovelace)
    btn5 = ElevatedButton(content=ft.Image(src="Hollerith.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Herman Hollerith"), on_click=play_hollerith)
    btn6 = ElevatedButton(content=ft.Image(src="Turing.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Alan Turing"), on_click=play_turing)
    btn7 = ElevatedButton(content=ft.Image(src="Neumann.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="John von Neumann"), on_click=play_neumann)
    btn8 = ElevatedButton(content=ft.Image(src="shannon.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Claude Shannon"), on_click=play_shannon)
    btn9 = ElevatedButton(content=ft.Image(src="Hopper.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Grace Hopper"), on_click=play_hopper)
    btn10 = ElevatedButton(content=ft.Image(src="McCarthy.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="John McCarthy"), on_click=play_mccarthy)
    btn11 = ElevatedButton(content=ft.Image(src="Berners.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Tim Berners-Lee"), on_click=play_berners)
    btn12 = ElevatedButton(content=ft.Image(src="Ritchie.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Dennis Ritchie"), on_click=play_ritchie)
    btn13 = ElevatedButton(content=ft.Image(src="Thompson.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Ken Thompson"), on_click=play_thompson)
    btn14= ElevatedButton(content=ft.Image(src="Gosling.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="James Gosling"), on_click=play_gosling)
    btn15 = ElevatedButton(content=ft.Image(src="Jobs.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Steve Jobs"), on_click=play_jobs)
    btn16 = ElevatedButton(content=ft.Image(src="Wozniak.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Steve Wozniak"), on_click=play_wozniak)
    btn17 = ElevatedButton(content=ft.Image(src="Gates.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Bill Gates"), on_click=play_gates)
    btn18 = ElevatedButton(content=ft.Image(src="Zuckerberg.webp", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Mark Zuckerberg"), on_click=play_zuckerberg)
    btn19 = ElevatedButton(content=ft.Image(src="Pages.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Larry Page"), on_click=play_pages)
    btn20 = ElevatedButton(content=ft.Image(src="Brin.webp", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Sergey Brin"), on_click=play_brin)
    
    #Botones historia de las computadoras 
    btn21 = ElevatedButton(content=ft.Image(src="Primera generacion.png.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Primera Generacion"),on_click=play_primerageneracion)
    btn22 = ElevatedButton(content=ft.Image(src="Segunda generacion.png.webp",width=img_width, height=img_height, border_radius=border_radius, semantics_label="Segunda generacion"), on_click=play_segundageneracion)
    btn23 = ElevatedButton(content=ft.Image(src="Tercera generacion.png.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Tercera generacion"), on_click=play_tercerageneracion)
    btn24 = ElevatedButton(content=ft.Image(src="Cuarta generacion.png.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Cuarta generacion"), on_click=play_cuartageneracion)
    btn25 = ElevatedButton(content=ft.Image(src="Quinta generacion.png.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Quinta generacion"), on_click =play_quintageneracion)
    btn26 = ElevatedButton(content=ft.Image(src="Sexta generacion.png.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Sexta generacion"), on_click =play_sextageneracion)
    
    #botones de lenguajes
    btn27 = ElevatedButton(content=ft.Image(src="C.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="C#"), on_click =play_c)
    btn28 = ElevatedButton(content=ft.Image(src="html.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="HTML"), on_click =play_html)
    btn29 = ElevatedButton(content=ft.Image(src="java.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="JAVA"), on_click =play_java)
    btn30 = ElevatedButton(content=ft.Image(src="javascrip.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="JavaScript"), on_click =play_javas)
    btn31 = ElevatedButton(content=ft.Image(src="perl.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Perl"), on_click =play_perl)
    btn32 = ElevatedButton(content=ft.Image(src="python.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Python"), on_click =play_python)
    btn33 = ElevatedButton(content=ft.Image(src="rust.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="RUST"), on_click =play_rust)
    btn34 = ElevatedButton(content=ft.Image(src="sql.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="SQL"), on_click =play_sql)
    btn35 = ElevatedButton(content=ft.Image(src="swift.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Swift"), on_click =play_swift)
    btn36 = ElevatedButton(content=ft.Image(src="Ciberseguridad.webp", width=img_width, height=img_height, border_radius=border_radius, semantics_label="CiberSeguridad"), on_click =play_seguridad)    
    btn37 = ElevatedButton(content=ft.Image(src="Computacion Blockchain.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Blockchain"), on_click =play_block)            
    btn38 = ElevatedButton(content=ft.Image(src="computacion cuantica.webp", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Computacion cuantica"), on_click =play_cuantica)
    btn39 = ElevatedButton(content=ft.Image(src="Desarrollo de Sofware Low-Code y No-Code.webp", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Desarrollo de software"), on_click =play_software)
    btn40 = ElevatedButton(content=ft.Image(src="Etica y Regulacion.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Reguylacion y etica"), on_click =play_etica)
    btn41 = ElevatedButton(content=ft.Image(src="IA en unos años.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="IA"), on_click =play_ia)
    btn42 = ElevatedButton(content=ft.Image(src="Internet en las cosas.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Internet"), on_click =play_internet)

    #Botones de evolucion de lenguajes
    btn43 = ElevatedButton(content=ft.Image(src="Definición.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Definición"), on_click=play_Definicion)
    btn44 = ElevatedButton(content=ft.Image(src="primer1843.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="primer1843"), on_click=play_primer1843)
    btn45 = ElevatedButton(content=ft.Image(src="Assembler.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Assembler"), on_click=play_Assembler)
    btn46 = ElevatedButton(content=ft.Image(src="Fortran.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Fortran"), on_click=play_Fortran)
    btn47 = ElevatedButton(content=ft.Image(src="List.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="List"), on_click=play_List)
    btn48 = ElevatedButton(content=ft.Image(src="Cobol.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Cobol"), on_click=play_Cobol)
    btn49 = ElevatedButton(content=ft.Image(src="Pascal1970.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Pascal1970"), on_click=play_Pascal1970)
    btn50 = ElevatedButton(content=ft.Image(src="Ada1980.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Ada1980"), on_click=play_Ada1980)
    btn51 = ElevatedButton(content=ft.Image(src="Cmasmas.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Cmasmas"), on_click=play_Cmasmas)
    btn52 = ElevatedButton(content=ft.Image(src="Perl.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Perl"), on_click=play_Perl)
    btn53 = ElevatedButton(content=ft.Image(src="Python.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Pyhton"), on_click=play_Python)
    btn54 = ElevatedButton(content=ft.Image(src="VisualBasics.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="VisualBasics1991"), on_click=play_VisualBasic)
    btn55 = ElevatedButton(content=ft.Image(src="Ruby.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Ruby"), on_click=play_Ruby)
    btn56 = ElevatedButton(content=ft.Image(src="PHP.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="PHP"), on_click=play_PHP)
    btn57 = ElevatedButton(content=ft.Image(src="Java.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Java"), on_click=play_Java)
    btn58 = ElevatedButton(content=ft.Image(src="Javascript.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Javascript"), on_click=play_Javascript)
    btn59 = ElevatedButton(content=ft.Image(src="Csharp.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Csharp"), on_click=play_Csharp)
    btn60 = ElevatedButton(content=ft.Image(src="Scala.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Scala"), on_click=play_Scala)
    btn61 = ElevatedButton(content=ft.Image(src="RubyOnRails.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="RubyOnRails"), on_click=play_RubyOnRails)

# Manejo del cambio de ruta
    def route_change(route):
        # Limpia las vistas anteriores
        page.views.clear()
        
        # Vista de portada
        if page.route == '/':
            page.views.append(
                View(
                    "/",
                    controls=[
                        AppBar(
                            title=ft.Text("Historia de las computadoras"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver al inicio',
                                        on_click=lambda _: page.go('/')
                                    ),
                                    
                                    ft.Text("Los lenguajes de programación han evolucionado a lo largo de la historia, aquí te presentamos algunos de los más importantes:"),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn21,btn22, btn23, btn24
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn25, btn26
                                        ]
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )

    # Manejo del cambio de ruta
    def route_change(route):
    
        # Limpia las vistas anteriores
        page.views.clear()
        
        # Vista de portada
        if page.route == '/':
            page.views.append(
                View(
                    "/",
                    controls=[
                        AppBar(
                            title=ft.Text("La historia de la Informática"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Los padres de la informática',
                                        on_click=lambda _: [StopAll(), page.go('/padres')]),
                                    ft.ElevatedButton(
                                        "la evolucion de los lenguajes de programacion",
                                        on_click=lambda _: [StopAll(), page.go('/lenguajes'),]),
                                    ft.ElevatedButton(
                                        'Lenguajes más usados',
                                        on_click=lambda _: [StopAll(), page.go('/imp')]),
                                    ft.ElevatedButton(
                                        'La evolución de las computadoras',
                                        on_click=lambda _: [StopAll(), page.go('/computadoras')]),
                                    ft.ElevatedButton(
                                        'Tecnología en el futuro',
                                        on_click=lambda _: [StopAll(), page.go('/futuro')]),
                                    ft.Image(
                                        src="Portada.png",
                                        width=image_width_Portada,
                                        height=image_height_Portada,
                                        fit="cover"
                                    ),
                                    ElevatedButton(
                                        "Escucha el intro",
                                        on_click=play_intro
                                    ),
                                    
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ],
                    bgcolor=page.bgcolor
                )
            )
        # Vista de los padres de la informática
        elif page.route == '/padres':
            page.views.append(
                View(
                    "/padres",
                    controls=[
                        AppBar(
                            title=ft.Text("Los padres de la informática"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver al inicio',
                                        on_click=lambda _: page.go('/')
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn1, btn2, btn3,btn4
                                        ]
                                    ),
                                    ft.Row(
                                      alignment="center",
                                      controls=[
                                        btn5, btn6, btn7,btn8
                                      ]  
                                    ),
                                    ft.Row(
                                       alignment="center",
                                        controls=[
                                          btn9, btn10, btn11,btn12
                                        ] 
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                          btn13,btn14,btn15,btn16
                                        ] 
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                          btn17,btn18,btn19,btn20
                                        ] 
                                    ),
                                    
                                ],
                                alignment=ft.MainAxisAlignment.CENTER
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
        if page.route == '/computadoras':
            page.views.append(
                View(
                    "/computadoras",
                    controls=[
                        AppBar(
                            title=ft.Text("Historia de las computadoras"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver al inicio',
                                        on_click=lambda _: page.go('/')
                                    ),
                                    
                                    ft.Text("La evolucion de la tecnologia ha avanzado mucho, y las computadoras han tenido un gran aporte ha este avance, aqui te presentamos la historia de las computadoras:"),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn21,btn22, btn23, btn24
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn25, btn26
                                        ]
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
        # Vista de la evolución de los lenguajes de programación
        elif page.route == '/lenguajes':
            page.views.append(
                View(
                    "/lenguajes",
                    controls=[
                        AppBar(
                            title=ft.Text("La evolución de los lenguajes de programación"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver al inicio',
                                        on_click=lambda _: page.go('/')
                                    ),
                                    ft.Text("Los lenguajes de programación han evolucionado a lo largo de la historia, aquí te presentamos algunos de los más importantes:"),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn43, btn44, btn45, btn46
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn47, btn48, btn49, btn50
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn51, btn52, btn53, btn54
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn55, btn56, btn57, btn58
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn59, btn60, btn61
                                        ]
                                    ),
                                    
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
        #leguajes importantes
        if page.route == '/imp':
            page.views.append(
                View(
                    "/imp",
                    controls=[
                        AppBar(
                            title=ft.Text("Lenguajes más usados actualmente"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver al inicio',
                                        on_click=lambda _: page.go('/')
                                    ),
                                    
                                    ft.Text("Hay muchos, muchos lenguajes de programación para poder usar, pero estos son los más conocidos y con los que puedes trabajar:"),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn27,btn28, btn29, btn30
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn31, btn32, btn33, btn34
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn35
                                        ]
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
        

        #viata de la las nuevas tecnologias
        elif page.route == '/futuro':
            page.views.append(
                View(
                    "/futuro",
                    controls=[
                        AppBar(
                            title=ft.Text("Tecnología en el futuro"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver al inicio',
                                        on_click=lambda _: page.go('/')
                                    ),
                                    
                                    ft.Text("La tecnología avanza mucho y muy rápido, te presentamos los posibles avances que habran en unos años en lo que abarca la tecnología:"),
                                    # Aquí puedes agregar el contenido específico para la sección de lenguajes de programación
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn36,btn37, btn38, btn39
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn40, btn41, btn42
                                        ]
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
        page.update()
    
    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main, assets_dir="assets")
#ft.app(target=main,view=ft.WEB_BROWSER, assets_dir="assets")

