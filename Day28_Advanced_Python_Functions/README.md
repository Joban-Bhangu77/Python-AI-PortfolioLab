# 🌟 Day 28 – Advanced Python Functions  
Part of the **Python & AI – 90 Days Journey**

Today was all about mastering **advanced Python functions** — the tools that make your code clean, reusable, and powerful.  
Functions are the foundation for AI, ML pipelines, modular automation, and large-scale applications.

---

## 🧠 What I Learned Today

### 🔹 1. Returning Multiple Values
Python allows returning multiple values as a tuple.

```python
def student_profile(name, age, country):
    return name, age, country
```

---

### 🔹 2. `*args` – Unlimited Positional Arguments  
Useful for unknown number of inputs.

```python
def sum_numbers(*nums):
    return sum(nums)
```

---

### 🔹 3. `**kwargs` – Unlimited Keyword Arguments  
Perfect for flexible functions.

```python
def describe_person(**details):
    for key, value in details.items():
        print(key, value)
```

---

### 🔹 4. Lambda Functions  
Small, one-line mini functions often used in ML.

```python
square = lambda x: x * x
```

---

### 🔹 5. Nested Functions  
Used heavily in decorators & closures.

```python
def outer(a):
    def inner(b):
        return a + b
    return inner
```

---

### 🔹 6. Real-Life Example – Discount Calculator

```python
def apply_discount(price, discount_percent):
    return price - (price * discount_percent / 100)
```

---

## 🧪 Hands-on Practice  
Below is the full script I built today:

📄 **Day28_Functions_Advanced.py**  
(See code inside repository.)

---

## 🏆 Key Takeaways

💎 Functions make code reusable and clean  
💎 `*args` + `**kwargs` make functions flexible  
💎 Lambdas appear everywhere in AI/ML feature engineering  
💎 Nested functions help in memory-efficient operations  
💎 Today’s concepts are used in Pandas, NumPy, Scikit-Learn, PyTorch  

---

## 🚀 Mini Project of the Day (Simple & Practical)

### **🛒 Shopping Cart Price Calculator**

Build a function that:

- Accepts unlimited items using `*args`
- Applies a coupon using `**kwargs`
- Uses lambda to format prices
- Returns total value

This will look amazing on GitHub.

---

## 📚 Files Completed Today

| File Name | Description |
|----------|-------------|
| `Day28_Functions_Advanced.py` | Main code for Day 28 |
| `README.md` | Documentation for GitHub |

---

## 🔗 Progress  
Day 28/90 Completed ✔  
Next → Day 29 (Coming Tomorrow 🚀)

---
 
