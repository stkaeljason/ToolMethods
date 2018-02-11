def prop_factory(name):
    """特性工程函数"""
    def get_prop(instance):
        return instance.__dict__[name]

    def set_prop(instance,value):
        if value > 0:                           # 此处排查条件根据具体需要设置
            instance.__dict__[name] = value
        else:
            print('error value')
    return property(get_prop, set_prop)