## Вопросы для самопроверки

**1. Что такое класс? Как он объявляется?**  
Класс — это шаблон (структура), по которому создаются объекты.  
Объявляется с помощью ключевого слова `class`:
```python
class MyClass:
    pass
```

**2. Как объявить метод класса? Чем он отличается от функции?**  
Метод — это функция, объявленная внутри класса.  
Отличие: метод всегда первым параметром принимает `self` — ссылку на текущий объект:
```python
class MyClass:
    def my_method(self):
        print("Это метод")
```

**3. Как построить набор не соединенных линиями точек на графике?**  
Используя `matplotlib.pyplot.scatter`:
```python
plt.scatter([x1, x2], [y1, y2])
```

**4. Как создать словарь?**  
С помощью фигурных скобок и пар ключ–значение:
```python
menu = {"борщ": 300, "салат": 200}
```

**5. Чем отличается словарь от списка?**  
Словарь хранит данные по ключу, список — по индексу.  
Словарь — неупорядоченная коллекция, список — упорядоченная.

**6. Что такое «ключ» в словаре?**  
Ключ — уникальное имя, по которому можно получить значение:
```python
цена = menu["борщ"]
```

**7. Что такое «виджет»?**  
Виджет — элемент интерфейса (кнопка, текстовое поле, список и т.д.).

**8. Какие виджеты вы использовали?**  
- `QLineEdit` — поле ввода  
- `QPushButton` — кнопка  
- `QLabel` — текстовая метка  
- `QListWidget` — список  
- `QPlainTextEdit` — многострочное поле текста

**9. Какой тип данных вводится в «QLineEdit»?**  
Строка (`str`). Если нужно число — преобразуем:
```python
value = float(self.lineEdit.text())
```

**10. Как поменять имя в элементе в «Qt Designer»?**  
В окне **Object Inspector** выбрать элемент → в **Property Editor** изменить свойство `objectName`.

**11. Что такое слот и сигнал? Что они делают?**  
Сигнал — событие (например, нажатие кнопки).  
Слот — функция, вызываемая при срабатывании сигнала.  
Пример соединения:
```python
self.button.clicked.connect(self.handler)
```

**12. Какой метод записывает текст в элемент «QLabel»?**  
Метод `setText()`:
```python
self.label.setText("Привет")
```

**13. Что такое «QListWidget»? Как он работает?**  
`QListWidget` — виджет, отображающий список элементов.  
Позволяет добавлять, удалять, выбирать строки:
```python
self.listWidget.addItem("Элемент")
self.listWidget.currentItem().text()
```
