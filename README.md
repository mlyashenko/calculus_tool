# calculus_tool

Учебный проект: мини‑утилита для базовых вычислений математического анализа (пределы, производные, интегралы) на базе SymPy. Проект подготовлен под критерии задания «Публикация проекта на GitHub».

## Возможности
- Вычисление предела выражения: `limit`
- Производная n‑го порядка: `derivative`
- Неопределённый/определённый интеграл: `integral`
- CLI‑интерфейс через `argparse`
- Простой пользовательский UI (файл `main.py`)

## Установка
Требуется Python 3.10+.

```bash
git clone https://github.com/<user>/calculus_tool.git
cd calculus_tool
python -m venv calculus_venv
# Windows: calculus_venv\\Scripts\\activate
# macOS/Linux: source calculus_venv/bin/activate
pip install -r requirements.txt