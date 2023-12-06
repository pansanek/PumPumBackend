from typing import Dict, List
from uuid import UUID

from fastapi import Depends

from app.models.task import Task
from app.models.user import User
from app.repositories.testing_repository import TestingRepo


class TestingService():
    testing_repo: TestingRepo

    def __init__(self, testing_repo: TestingRepo = Depends(TestingRepo)) -> None:
        self.testing_repo = testing_repo

    def get_all_results(self) -> Dict[UUID, List[int]]:
        return self.testing_repo.get_all_results()

    def check_answers(self, user: User, user_answers: list[int], right_answers: list[int]) -> list[int]:
        return self.testing_repo.get_binary_testing_matrix(
            user=user,
            user_answers=user_answers,
            right_answers=right_answers
        )

    def get_users_last_answers_check(self, user: User) -> list[int]:
        return self.testing_repo.get_binary_testing_matrix_by_user(user)

    def get_result_of_last_users_test_in_percentages(self, user: User) -> int:
        return self.testing_repo.get_percentage_of_last_test_completion(user=user)


