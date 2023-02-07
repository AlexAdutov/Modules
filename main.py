from application.salary import calculate_salary
from application.db.people import Employer
from datetime import datetime
import pandas

if __name__ == '__main__':
    print('Start')
    worker = Employer('Алексей', 'Путин', 10)
    # get_employees()
    salary = calculate_salary(worker.get_employees(),1000)
    print(salary)
    #print(datetime.now())
    print(f'По состоянию на {datetime.date(datetime.now())} работнику {worker.name} {worker.surname},\nимеющему {worker.grade} грейд начисляется зарплата в размере {salary} руб. в месяц')
    print('Finish')
