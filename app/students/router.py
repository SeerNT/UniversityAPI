from fastapi import APIRouter
from fastapi.params import Depends

from app.students.dao import StudentDAO
from app.students.rb import RequestBodyStudent
from app.students.schemas import SchemaStudent, SchemaStudentAdd, SchemaStudentUpdate

router = APIRouter(prefix='/students', tags=['Работа со студентами'])

@router.get("/", summary="Получить всех студентов")
async def get_all_students(request_body: RequestBodyStudent = Depends()) -> list[SchemaStudent]:
    return await StudentDAO.find_full_data(**request_body.to_dict())

@router.get("/by_filter", summary="Получить студента по фильтру")
async def get_student_by_filter(request_body: RequestBodyStudent = Depends()) -> SchemaStudent | dict:
    result = await StudentDAO.find_one_or_none(**request_body.to_dict())
    if result is None:
        return {"message" : "Студент с указанными параметрами был не найден!"}
    return result

@router.get("/{student_id}", summary="Получить студента по id")
async def get_student_by_id(student_id: int) -> SchemaStudent | dict:
    result = await StudentDAO.find_full_data_by_id(student_id)
    if result is None:
        return {"message" : f"Студент с id: {student_id} не был найден!"}
    return result

@router.post("/add/", summary="Добавить нового студента")
async def add_student(student: SchemaStudentAdd) -> dict:
    check = await StudentDAO.add_student(**student.dict())
    if check:
        return {"message": "Студент успешно добавлен!", "student": student}
    else:
        return {"message": "Ошибка при добавлении студента!"}

@router.delete("/del/{student_id}", summary="Удалить студента по id")
async def del_student_by_id(student_id: int) -> dict:
    check = await StudentDAO.delete_student_by_id(student_id=student_id)
    if check:
        return {"message": f"Студент с ID {student_id} удален!"}
    else:
        return {"message": "Ошибка при удалении студента!"}

@router.put("/{student_id}", summary="Обновить информацию о студенте")
async def update_student(student_id: int, request_body: RequestBodyStudent = Depends()) -> dict:
    check = await StudentDAO.update(
        filter_by={"id": student_id},
        **request_body.to_dict()
    )

    if check:
        return {"message": "Информация о студенте была успешно изменена!"}
    return {"message": f"Произошла ошибка при обновлении информации о студенте с id {student_id}!"}