import streamlit as st
import numpy as np
import sympy as sp

# Вхідні дані
i = 1  # Номер варіанта
x = sp.Symbol("x")

# Оголошення функції
f_x = (i + x) / (-i + 2.5 * i + x) + sp.sin(x + sp.pi / 2) ** (i + 1)

# Інтерактивний ввод значення x
x_val = st.number_input("Введіть значення x:", min_value=-100.0, max_value=100.0, value=0.0)

# Обчислення функції
result = f_x.subs(x, x_val)

# Вивід результату
st.title("Обчислення значення функції")
st.write(f"Функція: {f_x}")
st.write(f"Значення при x = {x_val}: **{result}**")
