from fastapi import APIRouter

router = APIRouter(prefix='/donation', tags=['Donations'])


@router.get('/')
def get_donations():
    return {'Hello': 'projects'}


@router.post('/')
def create_donation():
    return {'Hello': 'projects'}


@router.get('/my')
def get_my_donations():
    return {'Hello': 'projects'}
