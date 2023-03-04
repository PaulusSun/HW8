from X_clients_API_employee import X_clients_API_employee
from X_clients_API_auth import X_clients_API_auth
from X_clients_API_company import X_clients_API_company
import pytest

base_url = "https://x-clients-be.onrender.com"

# Валидный login_password
login_password = {
    "username": "stella", 
    "password": "sun-fairy"
    }

x_clients_API_auth = X_clients_API_auth(base_url, login_password)
x_clients_API_company = X_clients_API_company(base_url)
x_clients_API_employee = X_clients_API_employee(base_url)

# Валидный новый сотрудник
new_employee = {
            "companyId": str(x_clients_API_company.GET_id_company()),
            "firstName": "Герман",
            "lastName": "Субботин",
            "middleName": "Альбертович",
            "phone": "89008005021",
            "url": "нет сайта"
            }

# Валидные изменения для нового сотрудника
new_employee_correctly = {
            "lastName": "Воскресный",
            "email": "gervos@mail.ru",
            "url": "www.gervos.ru",
            "isActive": True
            }


@pytest.mark.parametrize('id_company, result', [(x_clients_API_company.GET_id_company(), 200), (None, 500)])
def test_GET_employee(id_company, result):
    assert x_clients_API_employee.GET_employee_from_id_company(id_company)[-1] == result

@pytest.mark.parametrize('auth, new_employee, id_company, result', [
    (x_clients_API_auth.auth(), new_employee, x_clients_API_company.GET_id_company(), True),
    (None, new_employee, x_clients_API_company.GET_id_company(), False),
    (x_clients_API_auth.auth(), None, x_clients_API_company.GET_id_company(), False),
    (x_clients_API_auth.auth(), new_employee, None, False)
    ])
def test_POST_employee(auth, new_employee, id_company, result):
    before_created_employee = len(x_clients_API_employee.GET_employee_from_id_company(id_company)[0])
    try:
        x_clients_API_employee.POST_employee(auth, new_employee)
        after_created_employee = len(x_clients_API_employee.GET_employee_from_id_company(id_company)[0])
    except KeyError:
        after_created_employee = before_created_employee
    
    print(int(after_created_employee) - int(before_created_employee))
    assert result == (int(after_created_employee) - int(before_created_employee) == 1)

@pytest.mark.parametrize('employee_id, result', [
    (x_clients_API_employee.POST_employee(x_clients_API_auth.auth(), new_employee), True),
    (None, False)
    ])
def test_GET_employee_id(employee_id, result):
    try:
        employee = len(x_clients_API_employee.GET_employee_id(employee_id))
    except KeyError:
        employee = 0
    assert (employee > 0) == result

@pytest.mark.parametrize('employee_id, auth, new_employee_correctly, result', [
    (x_clients_API_employee.POST_employee(x_clients_API_auth.auth(), new_employee), x_clients_API_auth.auth(), new_employee_correctly, True),
    (None, x_clients_API_auth.auth(), new_employee_correctly, False),
    (x_clients_API_employee.POST_employee(x_clients_API_auth.auth(), new_employee), None, new_employee_correctly, False),
    (x_clients_API_employee.POST_employee(x_clients_API_auth.auth(), new_employee), x_clients_API_auth.auth(), None, False),
    ])    
def test_PATCH_employee_id(employee_id, auth, new_employee_correctly, result):
    try:
        status_employee_correctly = x_clients_API_employee.PATCH_employee_id(employee_id, auth, new_employee_correctly)
    except KeyError:
        status_employee_correctly = 'err'
    assert (status_employee_correctly == 200) == result
