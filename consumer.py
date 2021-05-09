#!/usr/bin/env python
import multiprocessing
from producer import sleep
import pika

def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost')
    )

    channel =  connection.channel()

    def callback(ch, method, properties,body):
        print("[x] Recebido objeto: %r" % body.decode('ascii'))

    channel.basic_consume(
        queue='object', on_message_callback=callback, auto_ack=True
    )

    print('[*]Esperando por mensagens para sair pressione ctrl + c ou espere o programa fechar.')
    channel.start_consuming()


if __name__ == "__main__":
    p = multiprocessing.Process(target=main, name="Main")
    p.start()
    sleep(40)
    p.terminate()
    p.join()