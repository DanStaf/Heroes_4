from apscheduler.schedulers.background import BackgroundScheduler


def print_hello():
    print("HELLO")


def start_scheduler():
    scheduler = BackgroundScheduler()

    if not scheduler.get_jobs():
        scheduler.add_job(print_hello, 'interval', seconds=10)

    if not scheduler.running:
        scheduler.start()
