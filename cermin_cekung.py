import pygame
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

pygame.init()

def draw_line(canvas, x1, y1, x2, y2, r, g ,b):
    # menentukan selisih dari titik awal dan akhir
    dx = x2 - x1
    dy = y2 - y1

    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)

    x_increment = dx / steps
    y_increment = dy / steps

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

    if abs(dx) > abs(dy):
        if abs(dx) == 0:
            steps = 1
        else:
            steps = abs(dx)
    else:
        if abs(dy) == 0:
            steps = -1
        else:
            steps = abs(dy)
        
    x_increment = dx / steps
    y_increment = dy / steps

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

def pembesaran(jarak_benda, titik_fokus):
	varDummy = jarak_benda
	if ZeroDivisionError():
		varDummy += 0.1
		M = jarak_bayangan(jarak_benda, titik_fokus)/(varDummy)
		return (M)
	else:
		M = jarak_bayangan()/(jarak_benda)
		return (M)

def tinggi_bayangan(tinggi_benda, jarak_benda, titik_fokus):
    tinggi_bayang = pembesaran(jarak_benda, titik_fokus)*(tinggi_benda)
    return tinggi_bayang

def draw_cermin_cekung(canvas, R, G, B):
    width, height = canvas.get_width(), canvas.get_height()
    color = (R, G, B)
    h, k = 375, 300     # titik x dan y
    a = 30              # Besar sumbu horizontal
    b = 200             # Besar sumbu vertikal

    for y in range(k - b, k + b + 1):
        x = h + int((a * ((1 - ((y - k) / b)**2))**0.5))
        if 0 <= x < width and 0 <= y < height:
            pygame.draw.circle(canvas, color, (x, y), 1)

def gambar_garis_vertikal_dan_horizontal(canvas, width, height):
    #vertikal
    x1, y1 = int(width / 2), 0
    x2, y2 = int(width / 2), height
    draw_line(canvas, x1, y1, x2, y2, 0, 0, 0)
    
    R, G, B = 0,0,0
    draw_cermin_cekung(canvas, R, G, B)

    #horizontal
    x1, y1 = 0, height / 2
    x2, y2 = width, height / 2
    draw_line(canvas, x1, y1, x2, y2, 0, 0, 0)

def gambar_titik_fokus(canvas, red, width, height, titik_fokus, font):
    x1, y1 = konv_layar(titik_fokus, 1, width, height)
    pygame.draw.circle(canvas, red, (x1, height // 2), 3)
    
    #Label
    label_titik_fokus = font.render("F", True, (0, 0, 0))
    text_rect = label_titik_fokus.get_rect(center=(x1, y1 - 10))
    canvas.blit(label_titik_fokus, text_rect)

def titik_R(canvas, red, titik_fokus, width, height, font):
    x1, y1 =  konv_layar((2*titik_fokus), 1, width, height )
    pygame.draw.circle(canvas, red, (x1, y1), 3)

    label_titik_R = font.render("R", True, (0, 0, 0))
    text_rect = label_titik_R.get_rect(center=(x1, y1 - 10))
    canvas.blit(label_titik_R, text_rect)


def gambar_benda(canvas, width, height, jarak_benda, tinggi_benda, font):
    x1, y1 = konv_layar(jarak_benda, 0, width, height)
    x2, y2 = konv_layar(jarak_benda, tinggi_benda, width, height)
    draw_line(canvas, x1, y1, x2, y2, 255,0,0)

    label_benda = font.render("Object", True, (255, 0, 0))
    text_rect = label_benda.get_rect(center=(x1, y1 - (tinggi_benda + 10)))
    canvas.blit(label_benda, text_rect)

    #Gambar segitiga
    x1, y1 = konv_layar(jarak_benda, tinggi_benda, width, height)
    x2, y2 = konv_layar((jarak_benda - 30), 0, width, height)
    draw_line(canvas, x1, y1, x2, y2, 255,0,0)

    x1, y1 = konv_layar(jarak_benda, tinggi_benda, width, height)
    x2, y2 = konv_layar((jarak_benda + 30), 0, width, height)
    draw_line(canvas, x1, y1, x2, y2, 255,0,0)
    
def gambar_bayangan(canvas, width, height, jarakBayangan, tinggiBayangan, font):
    x1, y1 = konv_layar(jarakBayangan, 0, width, height)
    x2, y2 = konv_layar(jarakBayangan, -tinggiBayangan, width, height)
    draw_line(canvas, x1, y1, x2, y2, 255,0,0,)

    label_bayangan = font.render("Shadow", True, (255, 0, 0))
    text_rect = label_bayangan.get_rect(center=(x1, y1 + (tinggiBayangan + 10)))
    canvas.blit(label_bayangan, text_rect)

    #Gambarnya
    x1, y1 = konv_layar(jarakBayangan, -tinggiBayangan, width, height)
    x2, y2 = konv_layar((jarakBayangan - 30), 0, width, height)
    draw_line(canvas, x1, y1, x2, y2, 255,0,0,)

    x1, y1 = konv_layar(jarakBayangan, -tinggiBayangan, width, height)
    x2, y2 = konv_layar((jarakBayangan + 30), 0, width, height)
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
    draw_line_modif(canvas, x1, y1, x2, y2, 66, 66, 245)

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

    font = pygame.font.Font(None, 20)

    slider_jarakBenda = Slider(canvas, 40, 20, 300, 10, min=10, max=410, step=1)
    output_jarakBenda = TextBox(canvas, 750, 20, 34, 31, fontSize=16)

    slider_tinggiBenda = Slider(canvas, 40, 50, 300, 10, min=10, max=170, step=1)
    output_tinggiBenda = TextBox(canvas, 750, 50, 34, 31, fontSize=16)

    slider_jarakFokus = Slider(canvas, 40, 80, 300, 10, min=10, max=210, step=1)
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
        tinggiBayangan = int(tinggi_bayangan(tinggi_benda, jarak_benda, titik_fokus))

        #menggambar 
        gambar_garis_vertikal_dan_horizontal(canvas, width, height)
        gambar_titik_fokus(canvas, red, width, height, titik_fokus, font)
        titik_R(canvas, red, titik_fokus, width,height, font)
        gambar_benda(canvas, width, height, jarak_benda, tinggi_benda, font)
        gambar_bayangan(canvas, width, height, jarakBayangan, tinggiBayangan, font)
        gambar_garis_istimewa_1(canvas, width, height, titik_fokus, jarak_benda, tinggi_benda, jarakBayangan, tinggiBayangan)
        gambar_garis_istimewa_2(canvas, width, height, titik_fokus, jarak_benda, tinggi_benda, jarakBayangan, tinggiBayangan)

        # draw_half_ellipse(canvas, 255,0,0,)
        pygame.display.flip()

if __name__== "__main__":
    main()
