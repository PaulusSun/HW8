import requests


class X_clients_API_employee:
    def __init__(self, base_url):
        self.base_url = base_url
        
# - [GET] /employee Получить список сотрудников для компании
    def GET_employee_from_id_company(self, id_company):
        resp = requests.get(self.base_url+'/employee?company='+str(id_company))
        print('количество сотрудников',len(resp.json()))
        return [resp.json(), resp.status_code]
    
# - [POST] /employee Добавить нового сотрудника
    def POST_employee(self, auth, new_employee):
        resp = requests.post(self.base_url+'/employee', json = new_employee, headers = auth)
        employee_id = resp.json()['id']
        print('id нового сотрудника', str(employee_id))
        return employee_id

# - [GET] /employee/{id} Получить сотрудника по ID
    def GET_employee_id(self, employee_id):
        resp = requests.get(self.base_url+'/employee/'+str(employee_id))
        print(resp.json()["firstName"],resp.json()["middleName"],resp.json()["lastName"])
        return resp.json()

# [PATCH] /employee/{id} Изменить информацию о сотруднике
    def PATCH_employee_id(self, employee_id, auth, new_employee_correctly):
        resp = requests.patch(self.base_url+'/employee/'+str(employee_id), headers = auth, json = new_employee_correctly)
        print(resp.status_code)
        return resp.status_code
    
    
