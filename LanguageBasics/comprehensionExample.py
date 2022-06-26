from typing import Callable
from lxml import objectify

# Example helper method using list comprehension and dict comprehension
# convert list of xml objectified classes to list of dictionaries with string values


def order_data_to_dict(order_row_list: list) -> list:
    """
    Helper function to change order row data from the Order DBO GET call, into JSON serializable format
    :param order_row_list: list of orders
    :return: List containing dictionaries of orders
    """

    orders = [generate_order_row_dict(order_item) for order_item in order_row_list]
    return orders


def generate_order_row_dict(order_item):
    # Retrieve Required data and ensure values are cast to strings
    columns_of_interest = ["Id", "IsoCode"]

    new_dict = {column: order_item[column].text for column in columns_of_interest}
    return new_dict


# Sample helper methods to mock Order DBO Call


class OrderRow:
    # Properties of Class
    def __init__(self, order) -> None:
        self.Id = order.Id
        self.IsoCode = order.IsoCode


ORDERS_LIST = [{
    "Id": 1,
    "IsoCode": "LU"
}, {
    "Id": 2,
    "IsoCode": "LU"
}, {
    "Id": 3,
    "IsoCode": "NIKE"
}]


def dbo_order(orders_list: list = ORDERS_LIST) -> list:
    """
        helper to mock Order DBO
        :param orders_list: list of orders
    """

    response = [generate_order_row(order) for order in orders_list]
    return response


def generate_order_row(order) -> objectify.ObjectifiedElement:
    order_row_xml = objectify.fromstring('''
        <row>
            <Id> {Id} </Id>
            <IsoCode> {IsoCode} </IsoCode>
        </row>
    '''.format(**order))

    return order_row_xml


xml_orders = dbo_order()

example = order_data_to_dict(xml_orders)

print(xml_orders)

print(example)