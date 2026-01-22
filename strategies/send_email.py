import json
import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from strategies.base import BaseTask

load_dotenv()

class SendEmail(BaseTask):

    def run(self):
        dialog_sequence = True
        while dialog_sequence:
            data = []
            with open(self.file_data) as f:
                data = json.loads(f.read())

            email_list = data['email_receiver']
            print("Berikut daftar alamat email penerima:")
            for idx, rcv in enumerate(email_list):
                print(f"{idx}. {rcv}")

            choose_rcvr = input("Pilih alamat penerima yang sesuai dengan nomor urutnya:\n")

            try:
                receiver = email_list[int(choose_rcvr)]
                print(f"Pesan akan dikirimkan ke {receiver}")

                input_subject = input('Silakan masukkan subjek pesan Anda:\n')
                input_message = input('Silakan masukkan pesan Anda:\n')

                message = MIMEMultipart()
                message['From'] = data['own_email']
                message['To'] = receiver
                message['Subject'] = input_subject
                message.attach(MIMEText(input_message, "plain"))

                smtp_pass = os.getenv('SMTP_PASS','')
                smtp_server = os.getenv('SMTP_SERVER','smtp.gmail.com')
                smtp_port = int(os.getenv('SMTP_PORT','587'))

                server = smtplib.SMTP(smtp_server, smtp_port)
                try:
                    server.starttls()
                    server.login(data['own_email'], smtp_pass)

                    text = message.as_string()
                    server.sendmail(data['own_email'], receiver, text)

                    print("email berhasil dikirimkan!")

                    send_again = input('Kirim email lagi? (y/n)')
                    if send_again not in ['y','n']:
                        print('Pilihan Anda tidak ada dalam opsi, silakan pilih Y atau N')

                    if send_again != 'y':
                        dialog_sequence = False
                        break

                except Exception as e:
                    print(f"error while send email {e}")
                finally:
                    server.quit()

            except IndexError:
                print("Pilihan Anda tidak tersedia")
