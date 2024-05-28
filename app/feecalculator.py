import math

from .constants import Constants


class FeeCalculator:
    def __init__(self, cart_value, delivery_distance, number_of_items, time) -> None:
        self.cart_value = cart_value
        self.delivery_distance = delivery_distance
        self.number_of_items = number_of_items
        self.time = time
        self.delivery_fee = Constants.BASE_FEE
        self.rush_hour = Constants.RUSH_HOUR
        self.calculate_delivery_fee()

    def get_delivery_fee(self):
        return self.delivery_fee

    def calculate_delivery_fee(self):
        self.calculate_small_order_fee()
        self.calculate_delivery_fee_by_distance()
        self.calculate_extra_item_fee()
        self.calculate_rush_hour_fee()
        self.check_if_over_max_delivery_fee()
        self.check_if_eligible_for_free_delivery()

    def calculate_small_order_fee(self):
        self.delivery_fee += max(Constants.MIN_ORDER_VALUE - self.cart_value, 0)

    def calculate_delivery_fee_by_distance(self):
        extra_distance = max(self.delivery_distance - Constants.BASE_DISTANCE, 0)
        extra_distance_fee = (
            int(math.ceil(extra_distance / Constants.ADDITIONAL_DISTANCE))
            * Constants.ADDITIONAL_DISTANCE_FEE
        )
        self.delivery_fee += extra_distance_fee

    def calculate_extra_item_fee(self):
        extra_items = max(self.number_of_items - Constants.ITEMS_WITHOUT_SURCHARGE, 0)
        self.delivery_fee += extra_items * Constants.EXTRA_ITEM_FEE
        if self.number_of_items > Constants.ITEMS_COUNT_FOR_BULK_FEE:
            self.delivery_fee += Constants.EXTRA_BULK_FEE

    def calculate_rush_hour_fee(self):
        for key, value in self.rush_hour.items():
            if self.time.isoweekday() == key and self.time.hour in value:
                self.delivery_fee = int(
                    self.delivery_fee * Constants.RUSH_HOUR_MULTIPLIER
                )

    def check_if_over_max_delivery_fee(self):
        if self.delivery_fee > Constants.MAX_DELIVERY_FEE:
            self.delivery_fee = Constants.MAX_DELIVERY_FEE

    def check_if_eligible_for_free_delivery(self):
        if self.cart_value >= Constants.FREE_DELIVERY_CART_VALUE:
            self.delivery_fee = 0
