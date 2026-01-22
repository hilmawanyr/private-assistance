import json
from pathlib import Path
from strategies.base import BaseTask

class CreateSchedule(BaseTask):

    def run(self):
        dialog_sequence = True
        while dialog_sequence:
            new_sch = input("Silakan masukkan jadwal baru Anda:\n")

            data = []
            with open(self.file_data) as f:
                data = json.loads(f.read())

            curr_schedule = data['schedules']
            curr_schedule.append(new_sch)

            data['schedules'] = curr_schedule

            Path(self.file_data).write_text(json.dumps(data, indent=4))

            new_data = []
            with open(self.file_data) as f:
                new_data = json.loads(f.read())

            print(f"Berikut adalah daftar jadwal terbaru Anda: {new_data['schedules']}")

            ask_again = input("Apakah Anda ingin menambahkan jadwal lainnya? (y/n)\n")
            if ask_again not in ['y','n']:
                print("Silakan pilih 'y' untuk melanjutkan atau 'n' untuk berhenti")

            if ask_again == 'n':
                break
