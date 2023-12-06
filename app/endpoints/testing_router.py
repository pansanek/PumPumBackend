from typing import Dict, List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, Body

from app.models.user import User, CreateUserRequest
from app.services.testing_service import TestingService

testing_router = APIRouter(prefix='/testing', tags=['Testing'])


# нужно обратиться за правильными ответами к сервису решений
@testing_router.post('/check-answers')
def check_answers(user: CreateUserRequest, user_answers: list[int],
                  testing_service: TestingService = Depends(TestingService)) -> \
        list[int]:
    right_answers = user_answers

    return testing_service.check_answers(user=User(id=user.id, name=user.name), user_answers=user_answers,
                                         right_answers=right_answers)


@testing_router.get('/get-all-results')
def get_all_results(testing_service: TestingService = Depends(TestingService)) -> Dict[UUID, List[int]]:
    return testing_service.get_all_results()


@testing_router.post('/get-users-last-answers-check')
def get_users_last_answers_check(
        user: CreateUserRequest,
        testing_service: TestingService = Depends(TestingService)
) -> list[int]:
    try:
        return testing_service.get_users_last_answers_check(user=User(id=user.id, name=user.name))
    except KeyError:
        raise HTTPException(400, f'User with id={id} doesnt have any tests')


@testing_router.post('/get-result-of-last-users-test-in-percentages')
def get_result_of_last_users_test_in_percentages(user: CreateUserRequest,
                                                 testing_service: TestingService = Depends(TestingService)) -> int:
    return testing_service.get_result_of_last_users_test_in_percentages(user=User(id=user.id, name=user.name))
