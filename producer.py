#!/usr/bin/env python
import pika
from json_dowloader import pokedex, load_json
from time import sleep
from random import randint

class Publisher:
    def __init__(self, pokemon_num):
        self.__pokemon_num = pokemon_num
        self.__object1 = None
        self.__object2 = None
        self.__object3 = None
        self.__object4 = None

    def set_json_objects(self):
        pokedex(self.__pokemon_num)
        data = load_json(json_file='./json/pokemon.json')
        self.__object1 = str(data["name"])
        self.__object2 = str(data["types"])
        self.__object3 = str(data["abilities"])
        self.__object4 = str(data["weight"])
        self.__object5 = str(data["moves"])
        self.__object6 = str(data["held_items"])
        self.__object7 = str(data["species"])
        self.__object8 = str(data["stats"])

    def publish(self):
        objects = [self.__object1, self.__object2, self.__object3,
                    self.__object4, self.__object5, self.__object6,
                    self.__object7, self.__object8]
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost')
        )
        for obj in objects:
            sleep(5)
            channel = connection.channel()
            channel.queue_declare(queue = 'object')
            channel.basic_publish(exchange='', routing_key='object', body=obj)
        channel.close()


def main():
    publish1 = Publisher(pokemon_num=randint(1,932))
    publish1.set_json_objects()
    publish1.publish()

if __name__ == "__main__":
    main()