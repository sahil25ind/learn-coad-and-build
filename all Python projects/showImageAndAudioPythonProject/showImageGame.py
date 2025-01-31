import sys,pygame,tkinter
from PyQt5.QtCore import Qt,QTimer
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QPushButton
from PyQt5.QtGui import QPixmap,QIcon

class SahilGame(QWidget):
    def __init__(self):
        super().__init__()
        self.i = 0
        self.a = 0
        self.j = 5
        self.timer_label = QLabel(self)
        self.image_label = QLabel(self)
        self.start_button = QPushButton("Start",self.image_label)
        self.image_timer = QTimer()
        self.counter_timer = QTimer()

        self.initUI()


    def initUI(self):
        self.setGeometry(700,150,500,700)
        self.timer_label.setGeometry(0,0,self.width(),50)
        self.image_label.setGeometry(0,((self.height())-(self.height()-self.timer_label.height())),self.width(),(self.height()-self.timer_label.height()))
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.start_button.setStyleSheet("font-size: 50px;")
        self.start_button.resize(250,70)
        self.start_button.move((self.image_label.width() - self.start_button.width())//2,(self.image_label.height() - self.start_button.height())//2)
        self.start_button.clicked.connect(self.start)

    def start(self):
        self.start_button.deleteLater()     #this deletes the button permanently
        self.timer_label.setStyleSheet("background-color: green;font-size: 35px;")

        self.counter_timer.timeout.connect(self.count_timer)
        self.count_timer()
        self.counter_timer.start(1000)

        self.image_timer.timeout.connect(self.display_image)
        self.display_image()
        # self.image_timer.start(10000)

    def count_timer(self):
        if self.j > 0:
            self.timer_label.setStyleSheet("background-color: green;font-size: 35px;")
            self.timer_label.setText(f"{self.j}")
            self.j -= 1
        else:
            self.timer_label.setText("Playing Audio...")
            self.timer_label.setStyleSheet("background-color: red;font-size: 35px;")
            self.check_num_a()
            self.play_song()
            self.j = 5

    def play_song(self):
        
        if not self.a > 70:
            #play my audio here # i want to play my audio that i created its japnese hiragana alphabate sounds that i recorded my self
            pygame.mixer.init()
            pygame.mixer.music.load(f"audio_files/{self.a}.mp3")
            pygame.mixer.music.play()

            self.a += 1

            self.check_timer = QTimer()
            self.check_timer.timeout.connect(self.check_audio)
            self.check_timer.start(100)

    def restart_game(self):

        self.counter_timer.stop()
        self.image_timer.stop()
        self.check_timer.stop()

        self.close()    #close the old instance of the class and free the memory please avoid memory leackage
       

    def check_num_a(self):

        if self.a > 70:
            self.image_timer.stop()
            self.counter_timer.stop()
            self.check_timer.stop()
            self.restart_game()
            
        else:
            print(f"{self.i} {self.a}")

    def check_audio(self):
        # i need this to wait until it finished playing
        if pygame.mixer.music.get_busy():
            self.image_timer.stop()
            self.counter_timer.stop()
            
        if not pygame.mixer.music.get_busy():
            self.display_image()
            self.image_timer.start(10000)
            self.counter_timer.start(1000)
            self.check_timer.stop()

    #i created both audios and images it took about 7 and (1/2) hour to make them
    def display_image(self):
        if not self.i > 70:
            #here i want to display my image that i created my self # its japnese hiragana alphabates images i made them myself 
            image_path = f"Images/{self.i}.png"
            qPixmap = QPixmap(image_path)
            self.image_label.setPixmap(qPixmap)

            self.i += 1
        
def main():
    app = QApplication(sys.argv)
    sahil_game = SahilGame()
    sahil_game.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()