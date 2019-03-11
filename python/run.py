import main
import server

from threading import Thread

if __name__ == "__main__":

    t1 = Thread(target=main.start_speedtest)
    t2 = Thread(target=server.httpd.serve_forever)

    t1.setDaemon(True)
    t2.setDaemon(True)

    t1.start()
    t2.start()
    while True:
        pass