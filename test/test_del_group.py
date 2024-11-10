from model.group import Group


def test_del_1st_gr(app):
    # предусловие если групп нет - то создаём, иначе ничего не делаем
    if app.group.count_gr() == 0:
        app.group.create(Group("test-group", "бла бла бла", "ту ту ту"))
    # получаем старый список групп
    old_groups = app.group.get_gr_list()
    # метод удаления группы
    app.group.del_1st_gr()
    # получаем новый список
    new_groups = app.group.get_gr_list()
    # сравниваем старый и новый список по количеству групп (старый на 1 больше)
    assert len(old_groups) - 1 == len(new_groups)
    #прибиваем в старом списке первую группу
    old_groups[0:1] = []
    #сравниваем списки (должны быть идентичны)
    assert old_groups == new_groups
