from unittest.mock import patch

from customer_dao.customer_dao_imp import CustomerDAOImp
from entities.connection_problem import ConnectionProblem
from entities.customer_class import Customer
from entities.nothing_deleted import NothingDeleted

customer_dao = CustomerDAOImp()
test_customer = Customer(0, "Timmy", "Jimmy")


def test_create_customer_success():
    customer = Customer(0, "first", "last")
    result = customer_dao.create_customer_record(customer)
    assert result.customer_id != 0


def test_create_customer_with_malformed_id():
    # when wrong data id provided in the customer object, the method still work
    customer = Customer("one", "bad", "id")
    result = customer_dao.create_customer_record(customer)
    assert result.customer_id != 0


def test_delete_customer_success():
    result = customer_dao.delete_customer_record(-1)
    assert result


def test_no_customer_to_delete():
    try:
        customer_dao.delete_customer_record(-1000)
        assert False

    except NothingDeleted as e:
        assert str(e) == "There was no customer with the given Id"
