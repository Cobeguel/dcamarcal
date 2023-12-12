import math
from dataclasses import dataclass
from typing import List

def round_up(number, decimals):
    multiplier = 10**decimals
    return math.ceil(number * multiplier) / multiplier

@dataclass
class DCAMartingaleOrder:
    order: int
    deviation: float
    size: float
    volume: float
    price: float
    average_price: float
    required_price: float
    required_change: float
    total_size: float
    total_volume: float


@dataclass
class DCAMartingale():
    base_order_size: float
    order_size: float
    max_orders: int
    price_deviation: float
    target_profit: float
    order_scale: float
    volume_scale: float
    minimum_trade_decimals: int = 0
    initial_price: float = 100

    def calculate_table(self, price: float) -> List[DCAMartingaleOrder]:
        self.initial_price = price
        table = []

        order = 0
        deviation = 0
        size = self.base_order_size / self.initial_price
        size = round_up(size, self.minimum_trade_decimals)
        volume = self.initial_price * size
        price = self.initial_price
        average_price = price
        required_price = average_price * (1 + self.target_profit / 100)
        required_change = (required_price / price - 1) * 100
        total_size = size
        total_volume = volume
        row = DCAMartingaleOrder(order, deviation, size, volume, price, average_price, required_price, required_change, total_size, total_volume)
        table.append(row)

        for i in range(1, self.max_orders + 1):
            order = i
            deviation = table[i - 1].deviation * self.order_scale + self.price_deviation
            price = self.initial_price - self.initial_price * (deviation * 0.01)
            volume_aux = self.order_size * self.volume_scale**(i - 1)
            size = round_up(
                volume_aux / price,
                self.minimum_trade_decimals)
            volume = size * price
            total_size = table[i - 1].total_size + size
            total_volume = table[i - 1].total_volume + volume
            average_price = total_volume / total_size
            required_price = average_price * (1 + self.target_profit / 100)
            required_change = ((required_price / price) - 1) * 100
            row = DCAMartingaleOrder(order, deviation, size, volume, price, average_price, required_price, required_change, total_size, total_volume)
            table.append(row)

        return table
