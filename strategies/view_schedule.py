import json
from strategies.base import BaseTask

class ViewSchedule(BaseTask):

    def run(self):
        data = []
        with open(self.file_data) as f:
            data = json.loads(f.read())

        print(f"Ada {len(data['schedules'])} jadwal Anda, berikut daftar jadwalnya:")
        for sch in data['schedules']:
            print(f"- {sch}")
