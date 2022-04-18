def update(Factories):
    """Вызывает обновления состояния всех аереданных фабрик"""
    for i in Factories:
        if i:
            i.update()

