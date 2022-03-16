from abc import ABC, abstractmethod

from customer_dao.customer_dao_interface import CustomerDAOInterface
from entities.customer_class import Customer


class CustomerServiceInterface(ABC):

    def __init__(self, customer_dao: CustomerDAOInterface):
        self.customer_dao = customer_dao

    @abstractmethod
    def service_create_customer_record(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def service_delete_customer_record(self, customer_id: int) -> bool:
        pass
