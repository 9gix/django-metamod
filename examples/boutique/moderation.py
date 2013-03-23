import metamod
from boutique.models import Cloth, Accessory

class ClothModeration(metamod.ModelModeration):
    fields = ['name', 'brand']
    action = ['approve', 'reject', 'defer']


metamod.panel.register(Cloth, ClothModeration)
metamod.panel.register(Accessory)
