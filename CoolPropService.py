from CoolProp.CoolProp import get_global_param_string, PropsSI


def get_available_fluids() -> str:
    return get_global_param_string("predefined_mixtures").split(',')


def get_numeric_property(output, name1, prop1, name2, prop2, fluid_name: str):
    result = PropsSI(output, name1, prop1, name2, prop2, fluid_name)
    # print("output: "+str(output)+" name1 "+str(name1)+" name2 "+str(name2)+" fluid "+str(fluid_name)+" prop1 "+str(prop1)+" prop2 "+str(prop2)+" res "+str(result))
    return result
