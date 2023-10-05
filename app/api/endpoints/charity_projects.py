from fastapi import APIRouter

router = APIRouter(prefix='/charity_project', tags=['charity projects'])


@router.get('/')
def get_projects():
    return {'Hello': 'projects'}


@router.post('/')
def create_projects():
    return {'Hello': 'projects'}


@router.delete('/')
def delete_projects():
    return {'Hello': 'projects'}


@router.patch('/')
def update_projects():
    return {'Hello': 'projects'}
