from CoolProp.CoolProp import get_global_param_string, PropsSI


def get_available_fluids() -> str:
    return get_global_param_string("predefined_mixtures").split(',')


def get_numeric_property(output, name1, prop1, name2, prop2, fluid_name: str):
    result = PropsSI(output, name1, prop1, name2, prop2, fluid_name)
    return result
