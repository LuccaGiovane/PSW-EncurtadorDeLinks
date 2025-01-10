from ninja import Router
from .schemas import LinkSchema
from .models import Links
from django.shortcuts import get_object_or_404

shortener_router = Router()

@shortener_router.post('create/', response={200: LinkSchema, 409: dict})
def create(request, link_schema: LinkSchema):
    data = link_schema.to_model_data()
    
    redirect_link = data['redirect_link']
    token = data['token']
    expiration_time = data['expiration_time']
    max_uniques_cliques = data['max_uniques_cliques']

    

    if token and Links.objects.filter(token=token).exists():
        return 409, {'error': 'Token já em uso. Crie outro'}
    
    # da para usar : link = Links(**data) que funciona como as linhas abaixo antes do save
    link = Links(
        redirect_link = redirect_link,
        expiration_time = expiration_time,
        max_uniques_cliques = max_uniques_cliques,
        token = token
    )

    link.save()

    return 200, LinkSchema.from_model(link)

@shortener_router.get('/{token}', response={200: None, 404: dict})
def redirect_link(request, token):
    link = get_object_or_404(Links, token=token, active=True)

    if link.expired():
        return 404, {'error': 'Link expirado'}