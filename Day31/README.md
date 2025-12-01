# 🌟 Day 31 — Python OOP: Classes & Objects  
Part of the **Python & AI – 90 Days Journey**

## 📘 Overview  
Today marks a major milestone — diving into **Object-Oriented Programming (OOP)**, one of the most essential concepts in Python and modern software development.

OOP allows code to be:
- Modular  
- Scalable  
- Reusable  
- Organized like real-world systems  

Every major AI/ML framework (TensorFlow, PyTorch, Scikit-Learn) is built using OOP, so mastering it early strengthens the foundation for future AI and automation projects.

---

## 🧠 What I Learned Today

### 🔹 1. What is a Class?
A class is a **blueprint** to create objects.

```python
class Student:
    pass

🔹 2. Constructor & Attributes

The __init__() method initializes object data automatically.

class Student:
    def __init__(self, name, program):
        self.name = name
        self.program = program

🔹 3. Creating Objects

Objects are instances built from the class.

s1 = Student("Joban", "Computer Science")

🔹 4. Methods

Functions inside a class define the behavior.

def introduce(self):
    print(f"My name is {self.name}")

🔹 Practical Example from Today
student1 = Student("Jobanjit", "Computer Science & AI", 2025)
student1.introduce()
student1.progress()

🧪 Output Summary

✔ Created a custom class
✔ Added attributes & methods
✔ Used constructor to initialize objects
✔ Created multiple student objects
✔ Learned how OOP structures real applications

🏁 Conclusion

Day 31 introduced the fundamentals of Object-Oriented Programming, a core building block for developing structured, maintainable, and scalable Python applications.

This knowledge is essential for:

AI model classes

Data pipelines

Automation tools

Backend systems

Real-world project architecture

Today’s progress sets the stage for more advanced OOP topics in the coming days.

🔑 Key Takeaways

A class defines structure; an object is the actual instance

The __init__ constructor runs automatically

OOP makes large projects manageable

Methods define how objects behave

This concept is everywhere in AI, DevOps, and software engineering

🚀 What’s Next?

Tomorrow I’ll explore:

Inheritance

Encapsulation

Polymorphism

Real-world OOP mini-project