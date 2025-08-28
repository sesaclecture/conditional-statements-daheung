"""
Implement User Management System
"""

from typing import Tuple, Any, Callable
from enum import Enum
import json

class UserRole(str, Enum):
    ADMIN = 'adnim'
    EDITOR = 'editor'
    VIEWER = 'viewer'

class UserTask(str, Enum):
    RT_Create = "1"
    RT_Update = "2"
    RT_Delete = "3"
    RT_Read = "4"
    RT_UserUpdate = "5"
    RT_UserDelete = "6"

# 10명의 사용자 정보 샘플 데이터 (이전과 동일)
user_info = {
    "john_doe": {
        "name": "John Doe",
        "birth_date": "1995-03-15",
        "user_id": "john_doe",
        "password": "password123",
        'role': UserRole.ADMIN
    },
    "jane_smith": {
        "name": "Jane Smith",
        "birth_date": "1989-07-22",
        "user_id": "jane_smith",
        "password": "securepassword",
        'role': UserRole.EDITOR
    },
    "peter_jones": {
        "name": "Peter Jones",
        "birth_date": "1980-11-30",
        "user_id": "peter_jones",
        "password": "mypassword",
        'role': UserRole.EDITOR
    },
    "susan_lee": {
        "name": "Susan Lee",
        "birth_date": "2001-01-20",
        "user_id": "susan_lee",
        "password": "userpass",
        'role': UserRole.VIEWER
    },
    "michael_kim": {
        "name": "Michael Kim",
        "birth_date": "1992-09-05",
        "user_id": "michael_kim",
        "password": "kimpass123",
        'role': UserRole.VIEWER
    },
    "emily_park": {
        "name": "Emily Park",
        "birth_date": "1994-06-18",
        "user_id": "emily_park",
        "password": "parkemily",
        'role': UserRole.VIEWER
    },
    "david_choi": {
        "name": "David Choi",
        "birth_date": "1986-12-01",
        "user_id": "david_choi",
        "password": "choi1986",
        'role': UserRole.VIEWER
    },
    "lisa_jung": {
        "name": "Lisa Jung",
        "birth_date": "1997-04-10",
        "user_id": "lisa_jung",
        "password": "lisajung",
        'role': UserRole.VIEWER
    },
    "brian_kang": {
        "name": "Brian Kang",
        "birth_date": "1983-02-25",
        "user_id": "brian_kang",
        "password": "kangbrian",
        'role': UserRole.VIEWER
    },
    "olivia_yoon": {
        "name": "Olivia Yoon",
        "birth_date": "1999-08-08",
        "user_id": "olivia_yoon",
        "password": "yoonolivia",
        'role': UserRole.VIEWER
    },
}

# 20개의 할 일 목록 샘플 데이터 (요청하신 형식으로 변경)
todo_list = {
    "john_doe": {
        "item1": {
            "title": "저녁 장보기",
            "content": "우유, 계란, 빵 사기",
            "date": "2025-08-28",
            "good": 15,
        },
        "item2": {
            "title": "운동하기",
            "content": "공원에서 30분 조깅",
            "date": "2025-08-29",
            "good": 32,
        },
    },
    "jane_smith": {
        "item1": {
            "title": "프로젝트 제안서 작성",
            "content": "1차 초안 완성 후 팀에 공유",
            "date": "2025-09-01",
            "good": 58,
        },
        "item2": {
            "title": "병원 예약",
            "content": "정기 검진 예약하기",
            "date": "2025-09-03",
            "good": 8,
        },
    },
    "peter_jones": {
        "item1": {
            "title": "책 읽기",
            "content": "'파이썬 마스터' 챕터 3까지 읽기",
            "date": "2025-08-28",
            "good": 41,
        },
        "item2": {
            "title": "세차하기",
            "content": "주말에 자동 세차장 방문",
            "date": "2025-08-30",
            "good": 22,
        },
    },
    "susan_lee": {
        "item1": {
            "title": "영화 예매",
            "content": "이번 주 개봉작 '코드 브레이커' 예매",
            "date": "2025-08-29",
            "good": 76,
        },
        "item2": {
            "title": "친구 생일 선물 고르기",
            "content": "온라인 쇼핑몰에서 찾아보기",
            "date": "2025-09-05",
            "good": 19,
        },
    },
    "michael_kim": {
        "item1": {
            "title": "이메일 답장하기",
            "content": "협력업체에서 온 메일 3개 답장",
            "date": "2025-08-28",
            "good": 5,
        },
        "item2": {
            "title": "화분에 물 주기",
            "content": "베란다 식물들 관리",
            "date": "2025-08-28",
            "good": 33,
        },
    },
    "emily_park": {
        "item1": {
            "title": "블로그 포스팅",
            "content": "맛집 탐방 후기 작성",
            "date": "2025-09-02",
            "good": 120,
        },
        "item2": {
            "title": "강아지 산책",
            "content": "저녁 식사 후 1시간",
            "date": "2025-08-28",
            "good": 88,
        },
    },
    "david_choi": {
        "item1": {
            "title": "차량 정비 맡기기",
            "content": "엔진오일 교체 및 타이어 점검",
            "date": "2025-09-10",
            "good": 4,
        },
        "item2": {
            "title": "주말 계획 세우기",
            "content": "가족과 함께 갈 곳 찾아보기",
            "date": "2025-08-29",
            "good": 29,
        },
    },
    "lisa_jung": {
        "item1": {
            "title": "자격증 시험 공부",
            "content": "정보처리기사 필기 2과목 복습",
            "date": "2025-08-28",
            "good": 64,
        },
        "item2": {
            "title": "방 청소",
            "content": "책상 정리 및 바닥 청소",
            "date": "2025-08-31",
            "good": 47,
        },
    },
    "brian_kang": {
        "item1": {
            "title": "회의 자료 준비",
            "content": "다음 주 월요일 주간 회의 발표 자료",
            "date": "2025-09-04",
            "good": 11,
        },
        "item2": {
            "title": "부모님께 안부 전화",
            "content": "저녁 8시에 전화드리기",
            "date": "2025-08-28",
            "good": 95,
        },
    },
    "olivia_yoon": {
        "item1": {
            "title": "새로운 레시피 도전",
            "content": "유튜브 보고 파스타 만들기",
            "date": "2025-08-30",
            "good": 72,
        },
        "item2": {
            "title": "가계부 정리",
            "content": "8월 지출 내역 정리하기",
            "date": "2025-09-01",
            "good": 13,
        },
    },
}


def check_id(check) -> bool:
    return check in list(user_info.keys())

def check_role(name, role) -> bool:
    return user_info[name]['role'] == role

def check_task(name, task) -> bool:
    match task:
        case UserTask.RT_UserUpdate:
            return not check_role(name, UserRole.VIEWER)
        case UserTask.RT_UserDelete:
            return     check_role(name, UserRole.ADMIN)
        case _:
            return True

def check_date(date: str) -> bool:
    date_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year, month, day = date.split("-")
    if (year  > "2025"): 
        return False
    
    if (month > "12"  ): 
        return False
    
    if (day   > date_per_month[int(month) - 1]): 
        return False
    
    return True

def check_password(check: str) -> bool:
    check_len = len(check) > 10
    check_validation = not check.isalnum()
    return check_len and check_validation

def select_todo(name, predicate: Callable[[dict], bool]) -> Tuple[str, dict[str, Any]]:
    return [item for item in list(todo_list[name].items()) if predicate(item[1])]

def select_by_date(name, date) -> Tuple[str, dict[str, Any]]:
    return select_todo(name, lambda item: item['date'] == date)


def register_user_info():
    user_id = input("Enter your new id: ")
    if not check_id(user_id):
        print(f"your id '{user_id}' is already exist.")
        return False

    password = input("Enter your new password: ")
    if not check_password(password):
        print(f"Invalid password.")
        return False
    
    name = input("Enter your new name: ")
    birthday = input("Enter your birth-day: ")
    if not check_date(birthday):
        print(f"Invalid date.")
        return False
        
    user_info[user_info] = {
        "name": name,
        "birth_date": birthday,
        "user_id": user_id,
        "password": password,
        'role': UserRole.VIEWER
    }

print(json.dumps(user_info, indent=2, ensure_ascii=False))
login_succeed = False
while not login_succeed:
    register = input("Sign-in or Sign-up: [Y/N]")
    register = True if register == "N" else False
    if (register):
        register_user_info()

    # 로그인 기능 구현
    user_id = input("\rEnter user id: ")    
    if (user_info.get(user_id) is None):
        print(f"can not find user id: {user_id}. Try again")
        continue

    password = input("Enter user password: ")
    local_user_info = user_info[user_id]
    if local_user_info['password'] != password:
        print(f"Incorrect password. Try again.")
        continue

    break

print(f"Hello {user_id}!")

task_run = True
while task_run:
    status = input("Create:1, Update:2, Delete:3, Read:4 => ")
    # 2 리스트 아이템 추가, 수정, 삭제, 조회 기능
    
    if not check_task(user_id, status):
        print(f"Task denied.")
        continue

    match status:
        case "1": 
            current_date = "2025-08-28"
            title = input("Enter your todo title: ")
            content = input("Enter your todo detail content: ")
            
            id_keys = list(todo_list[user_id].keys())
            new_id = "item" + str(int(id_keys[-1].replace("item", "")) + 1)

            todo_list[user_id][new_id] = {
                "title": title,
                "content": content,
                "date": current_date,
                "good": 0,
            }

        case "2": 
            for idx, todo in enumerate(todo_list[user_id].values()):
                search_id = "item" + str(idx + 1)
                print(f"[{idx}/{len(todo)}] - title: {todo['title']} date: {todo['date']}")

            target_date = input("Enter date: ")

            todo_cur_date_list = [item for item in todo_list[user_id].values() if item["date"] == target_date]
            todo_cur_date_list_len = len(todo_cur_date_list)
            if todo_cur_date_list_len < 2:
                title = input("Enter your new todo title: ")
                content = input("Enter your new todo detail content: ")

                todo_list[user_id]['item1'] = {
                    "title": title,
                    "content": content,
                    "date": target_date,
                    "good": 0,
                }
            else:
                print(f"your todo list is not unique.")
                for idx, cur_todo_list in enumerate(todo_cur_date_list):
                    print(f"[{idx + 1}/{todo_cur_date_list_len}] - title: {cur_todo_list['title']}")
                
                target_idx = int(input("Enter number: "))
                target_id = 'item' + str(target_idx)

                title = input("Enter your new todo title: ")
                content = input("Enter your new todo detail content: ")
                todo_list[user_id][target_id] = {
                    "title": title,
                    "content": content,
                    "date": current_date,
                    "good": 0,
                }

        case "3": 
            target_date = input("Enter date: ")

            todo_cur_date_list = [item for item in list(todo_list[user_id].items()) if item[1]["date"] == target_date]
            todo_cur_date_list_len = len(todo_cur_date_list)
            if todo_cur_date_list_len < 2:
                if todo_cur_date_list_len == 0:
                    print('Todo lost is empty.')
                    continue

                todo_list[user_id].pop("item1")
            else:
                print(f"your todo list is not unique.")
                for idx, (id, cur_todo_list) in enumerate(todo_cur_date_list):
                    print(f"[{idx + 1}/{todo_cur_date_list_len}] - title: {cur_todo_list['title']}")
                
                target_idx = int(input("Enter number: "))
                target_id = todo_cur_date_list[target_idx][0]
                todo_list[user_id].pop(target_id)
        
        case "4":
            print(json.dumps(todo_list[user_id], indent=2, ensure_ascii=False))

        case "5":
            target_id = input("Enter target id: ")
            new_id = input("Enter new id: ")
            new_name = input("Enter new name: ")
            new_birthday = input("Enter new birthday: ")
            new_password = input("Enter new password: ")
            new_role = input("Enter new role: ")

            # 사용자 정보 삭제
            user_info.pop(target_id)

            # 사용자 정보 추가
            user_info[new_id] = {
                "name": new_name,
                "birth_date": new_birthday,
                "user_id": new_id,
                "password": new_password,
                'role': new_role
            }
        
        case "6":
            target_id = input("Enter target id: ")
            user_info.pop(target_id)

        case _: 
            print("Invalid input. Please input 1 to 4.")
            continue