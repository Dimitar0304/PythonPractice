from ninja import NinjaAPI, Schema

api = NinjaAPI()

@api.get("/hello")
def hello(request, name):
    return F"Hello {name}"

#input in url args#
@api.get("/math")
def math(request, a:int,b:int):
    return {"add": a + b, "multiply": a * b, "substract": a - b}


#input in URL path#
@api.get("/math/{b}and{a}")
def math(request,a: int,b:int ):
        return{"add":a+b, "multiply":a*b, "substract":a-b}

#input in request body#
class HelloSchema(Schema):
    name: str = "world mitak"

@api.post("/hello")
def hello(request,data:HelloSchema):
     return f"Hello {data.name}"