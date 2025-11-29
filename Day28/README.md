# 🌟 Day 28 – Advanced Python Functions  
Part of the **Python & AI – 90 Days Journey**

Today’s session focused on mastering **advanced Python function concepts** that are widely used in automation, system design, and AI/ML workflows.  
These concepts make your code cleaner, more scalable, and more flexible — exactly how modern software and data pipelines operate.

---

## 🧠 What I Learned Today

### 🔹 1. Returning Multiple Values  
Python allows returning multiple values from a single function, often used in data preprocessing and ML model outputs.

```python
def student_profile(name, age, country):
    return name, age, country
```

---

### 🔹 2. `*args` – Flexible Positional Arguments  
Useful when the number of inputs isn't fixed.  
Commonly used in aggregations, utility functions, and mathematical operations.

```python
def sum_numbers(*nums):
    return sum(nums)
```

---

### 🔹 3. `**kwargs` – Flexible Keyword Arguments  
Perfect when function inputs need to remain dynamic.  
Common in configuration loading, API calls, and object initialization.

```python
def describe_person(**details):
    for key, value in details.items():
        print(key, value)
```

---

### 🔹 4. Lambda (Anonymous) Functions  
Compact, one-line functions used widely in AI/ML pipelines — sorting, mapping, filtering, feature engineering.

```python
square = lambda x: x * x
```

---

### 🔹 5. Nested Functions & Closures  
Inner functions allow encapsulation and memory-efficient operations.  
These form the base of decorators, a powerful Python feature used in frameworks like Flask, Django, FastAPI.

```python
def outer(a):
    def inner(b):
        return a + b
    return inner
```

---

### 🔹 6. Real-World Example – Pricing With Discount  
A practical implementation of function logic used in e-commerce, finance, and billing systems.

```python
def apply_discount(price, discount_percent):
    return price - (price * discount_percent / 100)
```

---

## 📄 Completed Script  
**File:** `Day28_Functions_Advanced.py`  
The full implementation includes:

- Multiple return values  
- `*args` numerical aggregation  
- `**kwargs` flexible input handling  
- Lambda expressions  
- Nested functions  
- Real-life discount calculator  

---

## 🚀 Mini Project of the Day – *Shopping Cart Price Calculator*

A small practical task to reinforce today's learning:

- Accept unlimited item prices using `*args`  
- Apply promotional coupon using `**kwargs`  
- Use lambda for formatting  
- Return total amount payable  

This will be an excellent addition to your GitHub portfolio.

---

## 🏆 Key Takeaways

💎 Advanced functions make your code modular and scalable  
💎 `*args` + `**kwargs` give unmatched flexibility  
💎 Lambdas are essential in data transformations  
💎 Nested functions power decorators and framework logic  
💎 Today’s concepts appear everywhere in AI, ML, and backend automation  

---

## 📚 Files Added Today

| File | Description |
|------|-------------|
| `Day28_Functions_Advanced.py` | Main Python script with all advanced function concepts |
| `README.md` | Documentation for Day 28 |

---

## 📅 Progress  
**Day 28/90 Completed ✔**  
Next → **Day 29 – Coming Up Tomorrow 🚀**

---

## 👨‍💻 Author  
**Jobanjit Singh**  
Python & AI – 90 Days Journey  
Canada 🇨🇦


---
 
