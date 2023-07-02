from pydantic import BaseModel

class User(BaseModel):
	name: str
	edad: int

user1 = {'name': 'Yoshio', 'edad': 21}
persona = User(**user1)

print(persona.name)
print(persona.edad)