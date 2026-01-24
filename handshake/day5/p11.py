#Use **kwargs to display student info.
def employee_info(**kwargs):
    for key,value in kwargs.items():
        print(key,":",value)
employee_info(
    empid="r4347",
    name="sarita"

)
employee_info(
    name="ayhgs",
    id=24343435,
    saary=200000,
)