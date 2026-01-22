import json
from strategies.base import BaseTask

class MakeJoke(BaseTask):

    def __init__(self) -> None:
        super().__init__()

    def run(self):
        dialog_sequence = True
        while dialog_sequence:
            print("Silakan pilih joke dari daftar berikut:")

            data = []
            with open(self.file_data) as f:
                data = json.loads(f.read())

            jokes = data['jokes']
            print(f"Ada {len(jokes)} yang tersedia:")

            for idx, joke in enumerate(jokes):
                print(f"{idx}. {joke['about']}")

            select_joke = input("Silakan pilih sesuai nomornya, ya!:")

            if int(select_joke) >= len(jokes):
                print("Pilihan kamu tidak ada dalam daftar, silahkan masukkan pilihan yang tertera")

            print(f"{jokes[int(select_joke)]['joke']}")
            print(f"jawabannya: {jokes[int(select_joke)]['answer']}")

            ask_again = input('Mau lagi? (y/n)')
            if ask_again not in ['y','n']:
                print('Silakan ketik Y atau N untuk melanjutkan')

            if ask_again == 'n':
                dialog_sequence = False
                break
