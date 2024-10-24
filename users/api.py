from ninja import router, Router

users_router = Router()

@users_router.post('/',response={200: dict})
def creater_user(request):
    return {'ok': 'ok'}