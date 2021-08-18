from Thread import Job, signal_handler, ProgramKilled
from bot import Bot
import time, signal
from datetime import timedelta, datetime



class ShoppingBot:


    def __init__(self):
        self.bot = Bot()
        self.delay_seconds = 30
        self.count = 1


    def display_info(self):
        print('--------- INFO ---------', self.count)
        print('time:', datetime.now().strftime("%m/%d/%Y %H:%M:%S"))

        self.count += 1


    def run(self):
        signal.signal(signal.SIGTERM, signal_handler)
        signal.signal(signal.SIGINT, signal_handler)
        # multiple jobs below
        jobs = [
            Job(interval=timedelta(seconds=self.delay_seconds), execute=self.display_info),
            Job(interval=timedelta(seconds=self.delay_seconds), execute=self.bot.check_product_page),
            Job(interval=timedelta(seconds=self.delay_seconds), execute=self.bot.check_order_by_item_number_page)
        ]

        for job in jobs:
            job.start()

        while True:
            try:
                time.sleep(0.1)
            except (ProgramKilled, Exception) as e:
                print("Program killed: running cleanup code")
                print(e)
                for job in jobs:
                    job.stop()
                break




bot = ShoppingBot()
bot.run()