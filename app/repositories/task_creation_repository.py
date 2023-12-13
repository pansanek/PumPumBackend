import enum
import random
from uuid import UUID

from app.models.task import Task
from app.models.task import TaskDifficulty

import uuid
from random import randint, uniform, choice
from typing import List

# Создаем тестовый набор данных
tasks: List[Task] = []


def generate_tasks():
    for i in range(30):
        task_type = choice(["vector", "parallelepiped", "probability", "defects", "equation", "increasing_intervals",
                            "resonance_frequency", "stock", "intersection_point", "function_max", "equation_solve"])
        task = Task(
            id=uuid.uuid4(),
            statement="",
            difficulty=choice(list(TaskDifficulty)),
            answer=""
        )
        if task_type == "vector":
            task = Task(
                id=uuid.uuid4(),
                statement="Две стороны прямоугольника ABCD равны 6 и 8. Найдите длину вектора AC",
                difficulty=choice(list(TaskDifficulty)),
                answer="10"
            )

        elif task_type == "parallelepiped":
            task = Task(
                id=uuid.uuid4(),
                statement="Дан прямоугольный параллелепипед, стороны основания которого равны 4 и 5 , а боковое ребро равно 3 . Найдите наибольшую площадь его грани.",
                difficulty=choice(list(TaskDifficulty)),
                answer="20"
            )

        elif task_type == "probability":

            task = Task(
                id=uuid.uuid4(),
                statement="В фирме такси в данный момент свободно 15 машин: 2 красных, 9 желтых и 4 зеленых. По вызову выехала одна из машин, случайно оказавшихся ближе всего к заказчице. Найдите вероятность того, что к ней приедет желтое такси.",
                difficulty=choice(list(TaskDifficulty)),
                answer="0.6"

            )

        elif task_type == "defects":
            task = Task(
                id=uuid.uuid4(),
                statement="На фабрике керамической посуды 10% произведённых тарелок имеют дефект. При контроле "
                          "качества продукции выявляется 80% дефектных тарелок. Остальные тарелки поступают в "
                          "продажу. Найдите вероятность того, что случайно выбранная при покупке тарелка не имеет "
                          "дефектов.",
                difficulty=choice(list(TaskDifficulty)),
                answer=""

            )
        elif task_type == "equation":
            task = Task(
                id=uuid.uuid4(),
                statement="Решите уравнение x^2 - 4x + 4 = 0. В ответе напишите наибольший отрицательный корень.",
                difficulty=choice(list(TaskDifficulty)),
                answer="2"

            )

        elif task_type == "increasing_intervals":
            task = Task(
                id=uuid.uuid4(),
                statement="На рисунке изображен график производной функции f(x) определенной на интервале (a, "
                          "b). Найдите промежутки возрастания функции f(x). В ответе укажите сумму целых точек, "
                          "входящих в эти промежутки.",
                difficulty=choice(list(TaskDifficulty)),
                answer="15"

            )
        elif task_type == "resonance_frequency":
            task = Task(
                id=uuid.uuid4(),
                statement="Амплитуда колебаний маятника зависит от частоты вынуждающей силы, определяемой по формуле "
                          "A = k / (sqrt((f_r^2 - f^2)^2 + (f * b)^2)), где f_r — резонансная частота. Найдите "
                          "максимальную частоту f меньшую резонансной, для которой амплитуда колебаний превосходит "
                          "величину A не более чем на B. Ответ выразите в f_r.",
                difficulty=choice(list(TaskDifficulty)),
                answer=""

            )
        elif task_type == "stock":
            task = Task(
                id=uuid.uuid4(),
                statement="Амплитуда колебаний маятника зависит от частоты вынуждающей силы, определяемой по формуле A(w) = A0 * ωр² / | ωр² - ω |, где ω – частота вынуждающей силы (в ), A0 – постоянный параметр, ωр – резонансная частота. Найдите максимальную частоту ω, меньшую резонансной, для которой амплитуда колебаний превосходит величину A0 не более чем на 12.5%.",
                difficulty=choice(list(TaskDifficulty)),
                answer="120"

            )
        elif task_type == "intersection_point":
            task = Task(
                id=uuid.uuid4(),
                statement="На рисунке изображены графики двух линейных функций. Найдите абсциссу точки пересечения "
                          "графиков.",
                difficulty=choice(list(TaskDifficulty)),
                answer="-5"

            )
        elif task_type == "function_max":
            task = Task(
                id=uuid.uuid4(),
                statement="Найдите наибольшее значение функции f(x) = -2x^2 + 4x - 3 на отрезке [1, 4].",
                difficulty=choice(list(TaskDifficulty)),
                answer="-1"

            )
        elif task_type == "equation_solve":
            task = Task(
                id=uuid.uuid4(),
                statement="Решите уравнение 2x^2 - 8x + 6 = 0. Найдите решения уравнения, принадлежащие отрезку [3; 5].",
                difficulty=choice(list(TaskDifficulty)),
                answer="Нет решений"

            )

        tasks.append(task)


class TaskCreationRepo:
    def __init__(self, clear: bool = False) -> None:
        if clear:
            tasks.clear()

    def get_n_tasks(self, n: int) -> List[Task]:
        generate_tasks()
        return [task for task in tasks[:n]]

    def get_task_by_id(self, id: UUID) -> Task:
        generate_tasks()
        for t in tasks:
            if t.id == id:
                return t

        raise KeyError

    def get_random_task(self) -> Task:
        generate_tasks()
        return random.choice(tasks)

    def get_all_tasks(self) -> List[Task]:
        generate_tasks()
        return tasks
