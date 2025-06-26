from typing import List

from fastapi import APIRouter

from app.majors.dao import MajorsDAO
from app.majors.schemas import SchemaMajorAdd, SchemaMajorUpdate, SchemaMajor

router = APIRouter(prefix="/majors", tags=["Работа с факультетами"])

@router.get("/", summary="Получить все факультеты")
async def get_majors() -> List[SchemaMajor]:
    majors = await MajorsDAO.find_all()
    return  majors

@router.post("/add/", summary="Добавить новый факультет")
async def add_major(major: SchemaMajorAdd) -> dict:
    check = await MajorsDAO.add(**major.dict())
    if check:
        return {"message": "Факультет был успешно добавлен!", "major": major}
    return {"message": "Произошла ошибка при добавлении нового факультета!"}

@router.put("/update_description/", summary="Обновить описание факультета")
async def update_major_desc(major: SchemaMajorUpdate) -> dict:
    check = await MajorsDAO.update(
        filter_by={"major_name": major.major_name},
        major_description=major.major_description
    )

    if check:
        return {"message": "Описание факультета было успешно изменено!", "major": major}
    return {"message": f"Произошла ошибка при обновлении описания факультета {major.major_name}!"}

@router.delete("/major/{major_id}", summary="Удалить факультет по id")
async def delete_major(major_id: int) -> dict:
    check = await MajorsDAO.delete(id=major_id)

    if check:
        return {"message": f"Факультет с id {major_id} был удален!"}
    return {"message": f"Произошла ошибка при удалении факультета"}