import enum
import random
from uuid import UUID

from app.models.task import Task
from app.models.user import User
from app.models.task import TaskDifficulty

import uuid
from random import randint, uniform, choice
from typing import List, Dict


class TestingRepo:

    def __init__(self):
        self.results_dict: Dict[UUID, List[int]] = {
            UUID("551b5eb4-b4cf-4694-9e57-f00a8b27aa55"): [1, 0, 1, 1, 0]
        }

    def get_all_results(self) -> Dict[UUID, List[int]]:
        return self.results_dict

    def get_binary_testing_matrix(self, user: User, user_answers: List[int], right_answers: List[int]) -> List[int]:
        # Проверяем, что длины списков совпадают
        if len(user_answers) != len(right_answers):
            raise ValueError("Длины списков не совпадают")

        # Создаем бинарную матрицу, где 1 - верный ответ, 0 - неверный ответ
        binary_matrix = [1 if user == right else 0 for user, right in zip(user_answers, right_answers)]

        self.results_dict[user.id] = binary_matrix

        return binary_matrix

    def get_binary_testing_matrix_by_user(self, user: User) -> List[int]:
        return self.results_dict[user.id]

    def get_percentage_of_last_test_completion(self, user: User) -> int:
        print("ffsdfmsdlfsm")
        binary_matrix = self.get_binary_testing_matrix_by_user(user)
        # Считаем процент правильных ответов
        if binary_matrix:
            total_questions = len(binary_matrix)
            correct_answers = sum(binary_matrix)
            percentage = int((correct_answers / total_questions) * 100)
        else:
            percentage = 0  # В случае отсутствия данных возвращаем 0%

        return percentage
