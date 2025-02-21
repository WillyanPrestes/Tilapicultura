from typing import Type

from Classes.item import Item


class Compraitem:
    def __init__(self, iditem=0, idcompra=0, valor=0.00, qtd=0, item=Item):
        self.__id_item = iditem
        self.__id_compra = idcompra
        self.__valor = valor
        self.__qtd = qtd
        self.__item = item

    def get_id_item(self) -> int:
        return self.__id_item

    def set_id_item(self, iditem: int):
        self.__id_item = iditem

    def get_id_compra(self) -> int:
        return self.__id_compra

    def set_id_compra(self, idcompra: int):
        self.__id_compra = idcompra

    def get_valor(self) -> float:
        return self.__valor

    def set_valor(self, valor: float):
        self.__valor = valor

    def get_qtd(self) -> int:
        return self.__qtd

    def set_qtd(self, qtd: int):
        self.__qtd = qtd

    def get_item(self) -> Type[Item]:
        return self.__item

    def set_item(self, item: Item):
        self.__item = item
