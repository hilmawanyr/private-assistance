from strategies.base import BaseTask
from pathlib import Path
import json

class ChangeName(BaseTask):

    def run(self):
        data = []
        with open(self.file_data) as f:
            data = json.loads(f.read())

        dialog_sequence = True
        while dialog_sequence:
            change_dialog = input(f"Nama Anda saat ini adalah {data["name"]}. Ingin mengubahnya? (y/n)\n")
            allowed_answer = ['y','n']
            if change_dialog not in allowed_answer:
                print('Pilihan jawaban hanya "y" dan "n"\n')

            if change_dialog == 'n':
                break

            new_name = input("Masukkan nama Anda:")
            data['name'] = new_name

            Path(self.file_data).write_text(json.dumps(data, indent=4))

            new_data = []
            with open(self.file_data) as f:
                new_data = json.loads(f.read())

            print(f"Nama Anda sekarang adalah {new_data["name"]}")
            dialog_sequence = False
