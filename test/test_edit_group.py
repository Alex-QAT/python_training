from model.group import Group


def test_edit_1st_group_full(app):
    # проверка предусловия (если группы отсутствуют - то создать группу, иначе ничего не делать)
    if app.group.count_gr() == 0:
        app.group.create(Group("test-group"))
    # получаем список групп
    old_groups = app.group.get_gr_list()
    # задаём переменную в которую кладём объект Group с заданным набором значений
    # нам это надо чтобы эту переменную использовать как в методе редактирования edit_1st так и чтобы положить её в старый список
    # на место первой группы, чтобы потом впоследствии сравнить старый и новый списки
    group = Group(name="!Начальники", header="что-то написать", footer="что-то шрлмавлд")
    # запоминаем id первой группы в старом списке
    group.id = old_groups[0].id
    # вызываем метод редактирования первой группы в списке с переменной group (которую задали на предыдущем шаге) в качестве параметра
    app.group.edit_1st(group)
    # получаем новый список групп (после редактирования)
    new_groups = app.group.get_gr_list()
    # сравниваем списки по размеру (должны быть равны)
    assert len(old_groups) == len(new_groups)
    # первой группе в старом списке присваиваем тоже самое значение что и при редактировании
    old_groups[0] = group
    # проверяем на равенство отсортированные по ID списки групп (старый и новый)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_edit_1st_group_name(app):
    if app.group.count_gr() == 0:
        app.group.create(Group("test-group"))
    old_groups = app.group.get_gr_list()
    group = Group(name="New Name_Group")
    group.id = old_groups[0].id
    app.group.edit_1st(group)
    new_groups = app.group.get_gr_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_edit_1st_group_header(app):
    if app.group.count_gr() == 0:
        app.group.create(Group("test-group"))
    old_groups = app.group.get_gr_list()
    group = Group(header="New Header")
    group.id = old_groups[0].id
    group.name = old_groups[0].name
    app.group.edit_1st(group)
    new_groups = app.group.get_gr_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_edit_1st_group_footer(app):
    if app.group.count_gr() == 0:
        app.group.create(Group("test-group"))
    old_groups = app.group.get_gr_list()
    group = Group(footer="New Footer")
    group.id = old_groups[0].id
    group.name = old_groups[0].name
    app.group.edit_1st(group)
    new_groups = app.group.get_gr_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
