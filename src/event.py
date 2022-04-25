def update(Factories):
    """Вызывает обновления состояния всех переданных фабрик"""
    for i in Factories:
        if i:
            i.update()

