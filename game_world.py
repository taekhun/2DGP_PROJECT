# game world
# layer 0: Background Object
# layer 1: Foreground Object

world = [[], []]


def add_object(o, depth):  # 객체 생성
    world[depth].append(o)


def add_objects(ol, depth):  # 많은 객체 생성
    world[depth] += ol


def remove_object(o):  # 객체 제거
    for layer in world:
        if o in layer:
            layer.remove(o)
            del o
            return


def all_objects():
    for layer in world:
        for o in layer:
            yield o


def clear():
    for o in all_objects():
        del o
    for layer in world:
        layer.clear()
