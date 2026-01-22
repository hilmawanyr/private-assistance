from strategies import BaseTask
from strategies.factory import TaskFactory

class Assistance:
    def __init__(self) -> None:
        pass

    @classmethod
    def run(cls) -> None:
        task_sequence = True
        while task_sequence:
            prompt = input("""Hai! Silakan pilih tugas dari daftar nomor berikut sesuai kebutuhanmu:
                1. Ubah Nama
                2. Buat Jadwal
                3. Lihat Jadwal
                4. Kirim Email
                5. Beri Lelucon
                6. Keluar
                """)

            avail_list = ['1','2','3','4','5','6']
            if prompt not in avail_list:
                print(f"Nomor {prompt} yang kamu masukkan tidak ada dalam daftar, silakan coba kembali")

            if prompt in avail_list:
                task: BaseTask
                if prompt == '1':
                    task = TaskFactory.create('change_name')
                elif prompt == '2':
                    task = TaskFactory.create('create_schedule')
                elif prompt == '3':
                    task = TaskFactory.create('view_schedule')
                elif prompt == '4':
                    task = TaskFactory.create('send_email')
                elif prompt == '5':
                    task = TaskFactory.create('make_joke')
                else:
                    print('Sampai jumpa lagi!')
                    task_sequence = False
                    break

                task.run()

                return_task = True
                while return_task:
                    ask_again = input('Pilih tugas lagi? (y/n)')
                    if ask_again not in ['y','n']:
                        print('Pilihan kamu tidak tersedia. Silakan Pilih "y" atau "n" untuk melanjutkan')

                    if ask_again == 'n':
                        return_task = False

                    if ask_again == 'y':
                        break

                if not return_task:
                    print('Terimakasih, sampai jumpa!')
                    break
