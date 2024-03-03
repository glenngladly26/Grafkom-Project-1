import pygame
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

pygame.init()

def draw_line(canvas, x1, y1, x2, y2, r, g ,b):
    # menentukan selisih dari titik awal dan akhir
    dx = x2 - x1
    dy = y2 - y1

    # menentukan 
    steps = max(abs(dx), abs(dy))
    
    if steps != 0:
        x_increment = dx / steps
        y_increment = dy / steps
    else:
        x_increment = y_increment = 0

    # inisialisasi koordinat awal
    x = x1
    y = y1

    warna = (r,g,b)
    for _ in range(steps):
        canvas.set_at((int(x), int(y)), warna)
        x += x_increment
        y += y_increment

def draw_line_modif(canvas, x1, y1, x2, y2, r, g ,b):
    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))
    
    if steps != 0:
        x_increment = dx / steps
        y_increment = dy / steps
    else:
        x_increment = y_increment = 0

    x = x1
    y = y1

    warna = (r,g,b)
    width, height = 800, 600
    
    while 0 <= round(x) < width and 0 <= round(y) < height:
        canvas.set_at((int(x), int(y)), warna)
        x += x_increment
        y += y_increment

def konv_layar(x_kartesian, y_kartesian, lebar_layar, tinggi_layar):
    x_layar = lebar_layar // 2 + x_kartesian * (-1)
    y_layar = tinggi_layar // 2 + y_kartesian * (-1)
    return x_layar, y_layar

def jarak_bayangan(jarak_benda, titik_fokus):
	varDummy = jarak_benda
	fokusDummy = titik_fokus
	if ZeroDivisionError():
		varDummy += 0.1
		fokusDummy -= 0.1
		s = 1/(1/(fokusDummy) - 1/(varDummy))
		return s
	else:
		s = 1/(1/(titik_fokus) - 1/(jarak_benda))
		return s

def tinggi_bayangan(d, h, dB):
    try:
        hB = (dB / d) * h
        return max(1, hB)
    except ZeroDivisionError:
        return 1

def gambar_garis_vertikal_dan_horizontal(canvas, width, height):
    x1, y1 = int(width / 2), 0
    x2, y2 = int(width / 2), height
    draw_line(canvas, x1, y1, x2, y2, 0, 0, 0)

    x1, y1 = 0, height / 2
    x2, y2 = width, height / 2
    draw_line(canvas, x1, y1, x2, y2, 0, 0, 0)

def gambar_titik_fokus(canvas, red, width, height, titik_fokus):
    x1, y1 = konv_layar(titik_fokus, 1, width, height)
    x2, y2 = konv_layar(titik_fokus, -1, width, height)
    pygame.draw.line(canvas, red, (x1,y1), (x2,y2), 5)

def gambar_benda(canvas, width, height, jarak_benda, tinggi_benda):
    x1, y1 = konv_layar(jarak_benda, 0, width, height)
    x2, y2 = konv_layar(jarak_benda, tinggi_benda, width, height)
    draw_line(canvas, x1, y1, x2, y2, 255,0,0)

def gambar_bayangan(canvas, width, height, jarakBayangan, tinggiBayangan):
    x1, y1 = konv_layar(jarakBayangan, 0, width, height)
    x2, y2 = konv_layar(jarakBayangan, -tinggiBayangan, width, height)
    draw_line(canvas, x1, y1, x2, y2, 255,0,0,)

def gambar_garis_istimewa_1(canvas, width, height, titik_fokus, jarak_benda, tinggi_benda, jarakBayangan, tinggiBayangan):
    x1, y1 = konv_layar(0, tinggi_benda, width, height)
    x2, y2 = konv_layar(jarak_benda,tinggi_benda,width, height)
    draw_line_modif(canvas, x1, y1, x2, y2, 66, 66, 245)

    x1, y1 = konv_layar(0, tinggi_benda, width, height)
    x2, y2 = konv_layar(titik_fokus, 0, width, height)
    draw_line_modif(canvas, x1, y1, x2, y2, 66, 66, 245)

    x1, y1 = konv_layar(titik_fokus, 0, width, height)
    x2, y2 = konv_layar(jarakBayangan, -tinggiBayangan, width, height)
    draw_line(canvas, x1, y1, x2, y2, 66, 66, 245)

def gambar_garis_istimewa_2(canvas, width, height, titik_fokus, jarak_benda, tinggi_benda, jarakBayangan, tinggiBayangan):
    x1, y1 = konv_layar(titik_fokus, 0, width, height)
    x2, y2 = konv_layar(jarak_benda, tinggi_benda, width, height)
    draw_line_modif(canvas, x1, y1, x2, y2, 1, 117, 24)

    x1, y1 = konv_layar(titik_fokus, 0, width, height)
    x2, y2 = konv_layar(0, -tinggiBayangan, width, height)
    draw_line(canvas, x1, y1, x2, y2, 1, 117, 24)

    x1, y1 = konv_layar(0, -tinggiBayangan, width, height)
    x2, y2 = konv_layar(jarakBayangan, -tinggiBayangan, width, height)
    draw_line_modif(canvas, x1, y1, x2, y2, 1, 117, 24)

def main():
    width, height = 800, 600
    canvas = pygame.display.set_mode((width, height))
    bg_color = (255, 255, 255)
    canvas.fill(bg_color)
    red = (255,0,0)

    slider_jarakBenda = Slider(canvas, 40, 20, 300, 10, min=0, max=400, step=1)
    output_jarakBenda = TextBox(canvas, 750, 20, 34, 31, fontSize=16)

    slider_tinggiBenda = Slider(canvas, 40, 50, 300, 10, min=0, max=300, step=1)
    output_tinggiBenda = TextBox(canvas, 750, 50, 34, 31, fontSize=16)

    slider_jarakFokus = Slider(canvas, 40, 80, 300, 10, min=0, max=200, step=1)
    output_jarakFokus = TextBox(canvas, 750, 80, 34, 31, fontSize=16)

    output_jarakBenda.disable()
    output_tinggiBenda.disable()
    output_jarakFokus.disable()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

        canvas.fill(bg_color)
        pygame_widgets.update(event)

        output_jarakBenda.setText(str(slider_jarakBenda.getValue()))
        output_tinggiBenda.setText(str(slider_tinggiBenda.getValue()))
        output_jarakFokus.setText(str(slider_jarakFokus.getValue()))

        jarak_benda = slider_jarakBenda.getValue()
        tinggi_benda = slider_tinggiBenda.getValue()
        titik_fokus = slider_jarakFokus.getValue()
        jarakBayangan = int(jarak_bayangan(jarak_benda, titik_fokus))
        tinggiBayangan = int(tinggi_bayangan(jarak_benda, tinggi_benda, jarakBayangan))

        #menggambar 
        gambar_garis_vertikal_dan_horizontal(canvas, width, height)
        gambar_titik_fokus(canvas, red, width, height, titik_fokus)
        gambar_benda(canvas, width, height, jarak_benda, tinggi_benda)
        gambar_bayangan(canvas, width, height, jarakBayangan, tinggiBayangan)
        gambar_garis_istimewa_1(canvas, width, height, titik_fokus, jarak_benda, tinggi_benda, jarakBayangan, tinggiBayangan)
        gambar_garis_istimewa_2(canvas, width, height, titik_fokus, jarak_benda, tinggi_benda, jarakBayangan, tinggiBayangan)

        pygame.display.flip()

if __name__== "__main__":
    main()
