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
            difficulty=choice(list(TaskDifficulty))
                    )
        if task_type == "vector":
            task = Task(
                id=uuid.uuid4(),
                statement="На координатной плоскости изображены векторы a и b. Вектор a разложен по двум "
                          "неколлинеарным векторам i и j. Найдите коэффициент разложения k.",
                difficulty=choice(list(TaskDifficulty))
            )

        elif task_type == "parallelepiped":
            task = Task(
                id=uuid.uuid4(),
                statement="Одна из граней прямоугольного параллелепипеда — квадрат. Диагональ параллелепипеда равна d "
                          "и образует с плоскостью этой грани угол 45°. Найдите объем параллелепипеда.",
                difficulty=choice(list(TaskDifficulty))
            )

        elif task_type == "probability":

            task = Task(
                id=uuid.uuid4(),
                statement="В классе 26 учащихся, среди них два друга — Андрей и Сергей. Учащихся случайным образом "
                          "разбивают на 2 равные группы. Найдите вероятность того, что Андрей и Сергей окажутся в "
                          "одной группе.",
                difficulty=choice(list(TaskDifficulty))
            )

        elif task_type == "defects":
            task = Task(
                id=uuid.uuid4(),
                statement="На фабрике керамической посуды 10% произведённых тарелок имеют дефект. При контроле "
                          "качества продукции выявляется 80% дефектных тарелок. Остальные тарелки поступают в "
                          "продажу. Найдите вероятность того, что случайно выбранная при покупке тарелка не имеет "
                          "дефектов.",
                difficulty=choice(list(TaskDifficulty))
            )
        elif task_type == "equation":
            task = Task(
                id=uuid.uuid4(),
                statement="Решите уравнение x^2 - 4x + 4 = 0. В ответе напишите наибольший отрицательный корень.",
                difficulty=choice(list(TaskDifficulty))
            )

        elif task_type == "increasing_intervals":
            task = Task(
                id=uuid.uuid4(),
                statement="На рисунке изображен график производной функции f(x) определенной на интервале (a, "
                          "b). Найдите промежутки возрастания функции f(x). В ответе укажите сумму целых точек, "
                          "входящих в эти промежутки.",
                difficulty=choice(list(TaskDifficulty))
            )
        elif task_type == "resonance_frequency":
            task = Task(
                id=uuid.uuid4(),
                statement="Амплитуда колебаний маятника зависит от частоты вынуждающей силы, определяемой по формуле "
                          "A = k / (sqrt((f_r^2 - f^2)^2 + (f * b)^2)), где f_r — резонансная частота. Найдите "
                          "максимальную частоту f меньшую резонансной, для которой амплитуда колебаний превосходит "
                          "величину A не более чем на B. Ответ выразите в f_r.",
                difficulty=choice(list(TaskDifficulty))
            )
        elif task_type == "stock":
            task = Task(
                id=uuid.uuid4(),
                statement="В понедельник акции компании подорожали на некоторое количество процентов, а во вторник "
                          "подешевели на то же самое количество процентов. В результате они стали стоить на C "
                          "дешевле, чем при открытии торгов в понедельник. На сколько процентов подорожали акции "
                          "компании в понедельник?",
                difficulty=choice(list(TaskDifficulty))
            )
        elif task_type == "intersection_point":
            task = Task(
                id=uuid.uuid4(),
                statement="На рисунке изображены графики двух линейных функций. Найдите абсциссу точки пересечения "
                          "графиков.",
                difficulty=choice(list(TaskDifficulty))
            )
        elif task_type == "function_max":
            task = Task(
                id=uuid.uuid4(),
                statement="Найдите наибольшее значение функции f(x) = -2x^2 + 4x - 3 на отрезке [1, 4].",
                difficulty=choice(list(TaskDifficulty))
            )
        elif task_type == "equation_solve":
            task = Task(
                id=uuid.uuid4(),
                statement="Решите уравнение 2x^2 - 8x + 6 = 0. Найдите решения уравнения, принадлежащие отрезку [3; 5].",
                difficulty=choice(list(TaskDifficulty))
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




