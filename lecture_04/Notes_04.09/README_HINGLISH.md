# 🚀 Lecture 04.09: Python Dictionaries (Hash Tables)

## 📌 Executive Summary (Saransh)
Dictionary key-value pairs ka collection hoti hai. Yeh internally **Hash Table** use karti hai jisse data search karna bahut tez ($\mathcal{O}(1)$ time) hota hai.

---

## 🔬 Deep Technical Concepts

### 1. Key-Value Structure
Har value ka ek unique naam (Key) hota hai: `{"name": "Shradha", "age": 21}`. Keys hamesha unique aur immutable (jaise string ya number) honi chahiye.

### 2. Insertion Order
Python 3.7+ mein dictionary items ka wahi order maintain rehta hai jis order mein unhe add kiya gaya tha.

---

## 💻 Code Example

```python
student = {
    "name": "Shradha",
    "marks": 95,
    "course": "AI/ML Prime"
}

# Access karna
print("Student Name:", student["name"])

# Naya data add karna
student["city"] = "Delhi"
print("Updated Dict:", student)
```
