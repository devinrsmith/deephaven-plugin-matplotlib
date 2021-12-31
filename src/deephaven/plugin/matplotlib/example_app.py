ID = 'deephaven.plugin.matplotlib.example_app'
NAME = 'matplotlib.example_app'

def id() -> str:
    return ID

def name() -> str:
    return NAME

def initialize_into(state):
    import matplotlib.pyplot as plt
    from deephaven.TableTools import emptyTable as empty_table

    x = [0, 2, 4, 6]
    y = [1, 3, 4, 8]
    plt.plot(x, y)
    plt.xlabel('x values')
    plt.ylabel('y values')
    plt.title('plotted x and y values')
    plt.legend(['line 1'])
    my_plt = plt.gcf()
    state.set_field('my_plt', my_plt)
    state.set_field('my_table', empty_table(1).view("X=`hello, from example_app`"))
