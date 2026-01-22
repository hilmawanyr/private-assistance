from strategies.base import BaseTask
from strategies.change_name import ChangeName
from strategies.create_schedule import CreateSchedule
from strategies.view_schedule import ViewSchedule
from strategies.make_joke import MakeJoke
from strategies.send_email import SendEmail

class TaskFactory:
    @classmethod
    def create(cls, task: str) -> 'BaseTask':
        if task == 'change_name':
            return ChangeName()
        elif task == 'create_schedule':
            return CreateSchedule()
        elif task == 'make_joke':
            return MakeJoke()
        elif task == 'send_email':
            return SendEmail()
        elif task == 'view_schedule':
            return ViewSchedule()
        else:
            raise ValueError('undefined task')
