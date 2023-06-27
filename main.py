import pygame
import random

# Inisialisasi pygame
pygame.init()

# Definisikan warna
white = (255,255,255)
yellow = (255,255,102)
black = (0,0,0)
red = (213,50,80)
green =(0,255,0)
blue = (50,153,213)

# Tentukan ukuran layar 
dis_width = 600
dis_height = 600

# Buat layar dengan ukuran yg ditentukan
dis = pygame.display.set_mode((dis_width, dis_height))

# Beri judul pada layar 
pygame.display.set_caption("Snake Game")

# Buat clock
clock = pygame.time.Clock()

# tentukan ukuran blok snake
snake_block = 10
snake_speed = 5

# Tentukan font style
font_style = pygame.font.SysFont("bahnschrift", 30)
score_font = pygame.font.SysFont("comicsansms", 40)

# definisikan fungsi menampilkan skor
def your_score(score): 
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0,0])

# definisikan fungsi menggambar snake
def snake_shape(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

# definisikan fungsi untuk menampilkan pesan
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/6, dis_height/3])

# Fungsi utama game
def gameLoop():
    # memeriksa game sudah selesai atau belum
    game_over = False
    game_close = False

    #x1 dan y1 adalah koordinat awal kepala ular
    x1 = dis_width/2
    y1 = dis_height/2

    # variabel untuk mengubah posisi kepala ular
    x1_change = 0
    y1_change = 0

    # daftar kosong yang akan digunakan untuk menyimpan koordinat tubuh ular
    snake_list = []

    # panjang awal ular 
    length_of_snake = 1

    # koordinat makanan 
    foodx = round(random.randrange(0, dis_width - snake_block / 10.0)) *10.0
    foody = round(random.randrange(0, dis_height - snake_block / 10.0)) *10.0

    # looping untuk tidak game over
    while not game_over:
        # looping ketika game close
        while game_close==True:
            # mengisi layar dengan warna biru
            dis.fill(blue)

            # menampilkan pesan kalah dalam game
            message('You lost! Press C-play Again or Q-Quit', red)

            # Menampilkan skor
            your_score(length_of_snake - 1)

            # Update tampilan
            pygame.display.update()

            # Memeriksa event
            for event in pygame.event.get():
                # jika menekan Q
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                    if event.key ==pygame.K_c:
                        gameLoop()
        # Memeriksa event dengan looping
        for event in pygame.event.get():
            # Jika pengguna menutup jendela, permainan berakhir
            if event.type == pygame.QUIT:
                game_over = True
            # Jika pengguna menekan tombol di keyboard, ular bergerak sesuai dengan arah yang ditentukan
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Memeriksa apakah ular menabrak dinding
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        # Menggerakkan ular
        x1 += x1_change
        y1 += y1_change

        # Mengisi layar dengan warna biru
        dis.fill(blue)

        # Menggambar makanan
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        # Menambahkan kepala ular ke dalam daftar ular
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)

        # Jika panjang ular lebih besar dari panjang yang ditentukan, hapus ekor ular
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Memeriksa apakah ular menabrka diri sendiri
        for x in snake_list[:-1]:
            if x == snake_Head:
                game_close =True

        # Menggambar ular
        snake_shape(snake_block, snake_list)
        your_score(length_of_snake-1)
        
        # update tampilan
        pygame.display.update()

        # jika ular memakan kotak hijau, maka ukurannya akan bertambah dan menghasilkan kotak baru
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0,dis_width - snake_block)/10.0) * 10.0
            foody = round(random.randrange(0,dis_height - snake_block)/10.0) * 10.0
            length_of_snake+=1

        # menentukan kecepatan game
        clock.tick(snake_speed)     
    pygame.quit()
    quit()

gameLoop()