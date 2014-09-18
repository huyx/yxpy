Python utils
************

callit
======

You can do::

    from __future__ import print_function

    print('x', 'y', sep=',')

But I can not do::

    from __future__ import print_function

    parameters = ('x', 'y', sep=',')
    print(parameters)

With callit, I can do similar thing::

    from __future__ import print_function
    from yxpy.callit import CallIt

    parameters = CallIt('x', 'y', sep=',')
    parameters(print)

Sometimes, you may use Parameters(similar to CallIt)::

    from __future__ import print_function
    from yxpy.callit import Parameters

    parameters = Parameters('x', 'y', sep=',')
    parameters(format)

loadit
======

Load or reload python object

import module::

    import loadit

load moudule::

    mod = loadit.load_it('mymodule')

load function::

    func = loadit.load_it('mymodule.func')

load class::

    MyClass = loadit.load_it('mymodule.MyClass')

reload module::

    new_mod = loadit.reload_it(mod)

reload function::

    new_func = loadit.reload_it(func)

reload class::

    NewMyClass = loadit.reload_it(MyClass)

yamlfile
========

load config from YAML file, add a include tag.

main.yaml::

    a: !include a.yaml

a.yaml::

    name: a

usage::

    from yxpy import yamlfile

    yamlfile.load('main.yaml')