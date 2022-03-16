from customer_dao.customer_dao_imp import CustomerDAOImp
from customer_service_layer.service_imp import CustomerServiceImp
from entities.bad_customer_info import BadCustomerInfo
from entities.customer_class import Customer

customer_dao = CustomerDAOImp()
customer_service = CustomerServiceImp(customer_dao)

"""
create service tests
"""


def test_catch_non_string_first_name():
    try:
        customer = Customer(0, 49, "Jimmy")
        customer_service.service_create_customer_record(customer)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "invalid customer input, please try again"


def test_catch_non_string_last_name():
    try:
        customer = Customer(0, "timmy", 49)
        customer_service.service_create_customer_record(customer)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "invalid customer input, please try again"


def test_first_name_too_long():
    try:
        customer = Customer(0, "this string is too long for our method", "Jimmy")
        customer_service.service_create_customer_record(customer)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "invalid customer input, please try again"


def test_last_name_too_long():
    try:
        customer = Customer(0, "Timmy", "this string is too long for our method")
        customer_service.service_create_customer_record(customer)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "invalid customer input, please try again"


"""
delete service test
"""

def test_catch_non_typcastable_id():
    try:
        customer_service.service_delete_customer_record("one")
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "invalid customer input, please try again"
