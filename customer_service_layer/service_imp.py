from customer_service_layer.service_interface import CustomerServiceInterface
from entities.bad_customer_info import BadCustomerInfo
from entities.customer_class import Customer


class CustomerServiceImp(CustomerServiceInterface):

    def service_create_customer_record(self, customer: Customer) -> Customer:
        if type(customer.first_name) != str or type(customer.last_name) != str:
            raise BadCustomerInfo("invalid customer input, please try again")
        elif len(customer.first_name) > 20 or len(customer.last_name) > 20:
            raise BadCustomerInfo("invalid customer input, please try again")
        else:
            return self.customer_dao.create_customer_record(customer)

    def service_delete_customer_record(self, customer_id: int) -> bool:
        try:
            return self.customer_dao.delete_customer_record(int(customer_id))
        except ValueError:
            raise BadCustomerInfo("invalid customer input, please try again")