class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def get_info(self):
        return f"Сотрудник: {self.name}, ID: {self.id}"
class Manager(Employee):
    def __init__(self, name, id, department):
        Employee.__init__(self, name, id)
        self.department = department
        self.project = "Нет проекта"
    def manage_project(self, project_name):
        self.project = project_name
        return f"Менеджер {self.name} управляет проектом: {project_name}"
    def get_info(self):
        base_info = Employee.get_info(self)
        return f"{base_info}, Отдел: {self.department}, Проект: {self.project}"
class Technician(Employee):
    def __init__(self, name, id, specialization):
        Employee.__init__(self, name, id)
        self.__specialization = specialization
        self.maintenance_status = False
    def perform_maintenance(self):
        self.maintenance_status = True
        return f"Техник {self.name} выполнил обслуживание ({self.__specialization})"
    def get_info(self):
        base_info = Employee.get_info(self)
        status = "Выполнено" if self.maintenance_status else "Не выполнено"
        return f"{base_info}, Специализация: {self.__specialization}, Обслуживание: {status}"
    def get_specialization(self): ###
        return self.__specialization
class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        Manager.__init__(self, name, id, department)
        Technician.__init__(self, name, id, specialization)
        self.project = "Нет проекта"
        self.maintenance_status = False
        self.team = []
    def add_employee(self, employee):
        self.team.append(employee)
        return f"{employee.name} добавлен в команду {self.name}"
    def get_team_info(self):
        if not self.team:
            return "В команде пока нет сотрудников"
        result = f"Команда {self.name}:\n"
        for i, employee in enumerate(self.team, 1):
            result += f"{i}. {employee.get_info()}\n"
        return result
    def get_info(self):
        info = f"TechManager: {self.name}, ID: {self.id}"
        info += f", Отдел: {self.department}"
        info += f", Проект: {self.project}"
        info += f", Специализация: {Technician.get_specialization(self)}"
        status = "Выполнено" if self.maintenance_status else "Не выполнено"
        info += f", Обслуживание: {status}"
        return info
    def manage_project(self, project_name):
        self.project = project_name
        return f"TechManager {self.name} проект: {project_name}"
    def perform_maintenance(self):
        self.maintenance_status = True
        return f"TechManager {self.name} выполнил обслуживание"


def create_employee():
    print("\n--- Создание обычного сотрудника ---")
    name = input("Введите имя сотрудника: ")
    emp_id = input("Введите ID сотрудника: ")
    employee = Employee(name, emp_id)
    print(f"Создан сотрудник: {employee.get_info()}")
    return employee


def create_manager():
    print("\n--- Создание менеджера ---")
    name = input("Введите имя менеджера: ")
    emp_id = input("Введите ID менеджера: ")
    department = input("Введите отдел менеджера: ")
    manager = Manager(name, emp_id, department)
    print(f"Создан менеджер: {manager.get_info()}")

    project_choice = input("Хотите назначить проект менеджеру? (да/нет): ").lower()
    if project_choice == 'да':
        project_name = input("Введите название проекта: ")
        print(manager.manage_project(project_name))

    print(f"Менеджер полная информация: {manager.get_info()}")
    return manager


def create_technician():
    print("\n--- Создание техника ---")
    name = input("Введите имя техника: ")
    emp_id = input("Введите ID техника: ")
    specialization = input("Введите специализацию техника: ")
    technician = Technician(name, emp_id, specialization)
    print(f"Создан техник: {technician.get_info()}")

    maintenance_choice = input("Хотите, чтобы техник выполнил обслуживание? (да/нет): ").lower()
    if maintenance_choice == 'да':
        print(technician.perform_maintenance())

    print(f"Техник полная информация: {technician.get_info()}")
    return technician


def create_tech_manager():
    print("\n--- Создание TechManager ---")
    name = input("Введите имя TechManager: ")
    emp_id = input("Введите ID TechManager: ")
    department = input("Введите отдел TechManager: ")
    specialization = input("Введите специализацию TechManager: ")
    tech_manager = TechManager(name, emp_id, department, specialization)
    print(f"Создан TechManager: {tech_manager.get_info()}")

    project_choice = input("Хотите назначить проект TechManager? (да/нет): ").lower()
    if project_choice == 'да':
        project_name = input("Введите название проекта: ")
        print(tech_manager.manage_project(project_name))

    maintenance_choice = input("Хотите, чтобы TechManager выполнил обслуживание? (да/нет): ").lower()
    if maintenance_choice == 'да':
        print(tech_manager.perform_maintenance())

    print(f"\nTechManager характеристика с обслуживанием:")
    print(tech_manager.get_info())
    return tech_manager


def add_employees_to_team(tech_manager):
    print("\n--- Добавление сотрудников в команду ---")
    while True:
        add_more = input("Добавить сотрудника в команду? (да/нет): ").lower()
        if add_more != 'да':
            break

        print("\nКого добавить в команду?")
        print("1. Обычный сотрудник")
        print("2. Менеджер")
        print("3. Техник")
        print("4. Вернуться назад")

        choice = input("Выберите тип сотрудника (1-4): ")

        if choice == '1':
            employee = create_employee()
            print(tech_manager.add_employee(employee))
        elif choice == '2':
            manager = create_manager()
            print(tech_manager.add_employee(manager))
        elif choice == '3':
            technician = create_technician()
            print(tech_manager.add_employee(technician))
        elif choice == '4':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


def main():
    print("=== Система управления сотрудниками ===")
    employees = []

    while True:
        print("\n=== Главное меню ===")
        print("1. Создать обычного сотрудника")
        print("2. Создать менеджера")
        print("3. Создать техника")
        print("4. Создать TechManager")
        print("5. Показать всех созданных сотрудников")
        print("6. Выйти из программы")

        choice = input("Выберите действие (1-6): ")

        if choice == '1':
            employee = create_employee()
            employees.append(("Сотрудник", employee))

        elif choice == '2':
            manager = create_manager()
            employees.append(("Менеджер", manager))

        elif choice == '3':
            technician = create_technician()
            employees.append(("Техник", technician))

        elif choice == '4':
            tech_manager = create_tech_manager()
            employees.append(("TechManager", tech_manager))

            team_choice = input("Хотите добавить сотрудников в команду TechManager? (да/нет): ").lower()
            if team_choice == 'да':
                add_employees_to_team(tech_manager)
                print("\nИнформация о команде:")
                print(tech_manager.get_team_info())

        elif choice == '5':
            if not employees:
                print("\nПока нет созданных сотрудников.")
            else:
                print("\n=== Все созданные сотрудники ===")
                for i, (emp_type, emp) in enumerate(employees, 1):
                    print(f"{i}. [{emp_type}] {emp.get_info()}")

        elif choice == '6':
            print("Выход из программы...")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()