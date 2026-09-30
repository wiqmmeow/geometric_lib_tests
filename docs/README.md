# Документация проекта Geometric Lib

## Общее описание
Geometric Lib — учебный проект на Python, в котором для каждой из четырёх фигур (круг, квадрат, прямоугольник, треугольник) есть отдельный модуль. В каждом модуле две функции: `area` считает площадь фигуры, а `perimeter` — периметр (для круга это длина окружности). Функции принимают размеры фигуры в виде чисел и возвращают результат вычисления.

## Math formulas

### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah/2

### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2(a + b)
- Square: P = 4a
- Triangle: P = a + b + c

## Описание функций

### circle.py
- `area(r)`: площадь круга. Вызов: `circle.area(4)`
- `perimeter(r)`: длина окружности. Вызов: `circle.perimeter(4)`
 
### square.py
- `area(a)`: площадь квадрата. Вызов: `square.area(8)`
- `perimeter(a)`: периметр квадрата. Вызов: `square.perimeter(8)`

### rectangle.py
- `area(a, b)`: площадь прямоугольника. Вызов: `rectangle.area(4, 9)`
- `perimeter(a, b)`: периметр прямоугольника. Вызов: `rectangle.perimeter(4, 9)`

### triangle.py
- `area(a, h)`: площадь треугольника. Вызов: `triangle.area(5, 2)`
- `perimeter(a, b, c)`: периметр треугольника. Вызов: `triangle.perimeter(3, 3, 5)`

## История изменений
- `34006b3`: rectangle.py was created
- `f9e78e4`: Исправлена ошибка в rectangle.py (добавлен triangle.py)
- `55315f5`: Added docstrings to all functions
- Добавлена документация в docs/README.md