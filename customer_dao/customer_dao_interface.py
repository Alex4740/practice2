from abc import ABC, abstractmethod
from typing import List

from entities.customer_class import Customer


@abstractmethod
class CustomerDAOInterface(ABC):
    pass

    @abstractmethod
    def create_customer_record(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def delete_customer_record(self, customer_id: int) -> bool:
        pass
