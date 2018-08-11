""" Models for Securities """

from decimal import Decimal
from typing import List


#@dataclass
class StockAnalysisInputModel: #pylint: disable=invalid-name
    """ Input model for Stock Analysis """
    def __init__(self):
        self.symbol: str = None


class SecurityAnalysisRefModel:
    """ Reference data for input form """
    def __init__(self):
        self.securities = []


class SecurityYieldModel:
    """ Yiel view model """
    def __init__(self):
        self.symbol = None
        self.average_price = None
        self.price = None
        self.profit_loss = None
        self.quantity = None
        self.security = None
        self.total_paid = None
        self.value = None
        self.income = None
        self.income_perc = None
        self.total_return = None
        self.profit_loss_perc = None
        self.total_return_perc = None
