# Lecture 05: Assignment 4 Questions Aur Systems Case Studies (हिंग्लिश)

Is document mein **Lecture 05: Object-Oriented Programming (OOP) in Python** ke official **Assignment 4** ke sabhi 10 questions aur 3 systems engineering case studies ka detailed Hinglish explanation diya gaya hai.

Har question ke andar do vishesh sections hain:
1. `### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?` (Numbered bullet points)
2. `### 🔍 Har Ek Bullet Point Ka Detailed Explanation` (Deep conceptual aur practical breakdown)

---

## 📋 Table of Contents

- [Question 01: BankAccount Encapsulated Ledger Class](#question-01-bankaccount-encapsulated-ledger-class)
- [Question 02: Book Reviews Catalog Class](#question-02-book-reviews-catalog-class)
- [Question 03: Encapsulated Student Record With Validations](#question-03-encapsulated-student-record-with-validations)
- [Question 04: Polymorphic Shape Hierarchy & Area Method Overriding](#question-04-polymorphic-shape-hierarchy--area-method-overriding)
- [Question 05: Vehicle Inheritance (Car & Bike Subclasses)](#question-05-vehicle-inheritance-car--bike-subclasses)
- [Question 06: Abstract Employee Class & Payroll Subclasses](#question-06-abstract-employee-class--payroll-subclasses)
- [Question 07: Constructor Overloading Simulation (Default Parameters)](#question-07-constructor-overloading-simulation-default-parameters)
- [Question 08: Player Class & Global Player Count Variable](#question-08-player-class--global-player-count-variable)
- [Question 09: Multiple Inheritance (Herbivore, Carnivore & Bear)](#question-09-multiple-inheritance-herbivore-carnivore--bear)
- [Question 10: Mini-Project – OOP Chat System](#question-10-mini-project--oop-chat-system)
- [Systems Case Study 1: CPython Object Memory Aur \_\_slots\_\_ Architecture](#systems-case-study-1-cpython-object-memory-aur---slots---architecture)
- [Systems Case Study 2: Diamond Inheritance Aur C3 Linearization (MRO)](#systems-case-study-2-diamond-inheritance-aur-c3-linearization-mro)
- [Systems Case Study 3: Dynamic Attribute Lookup Protocol Aur Descriptors](#systems-case-study-3-dynamic-attribute-lookup-protocol-aur-descriptors)

---

## Question 01: BankAccount Encapsulated Ledger Class

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. Ek class `BankAccount` create karni hai jisme teen attributes ho: `account_number`, `owner_name`, aur `balance`.
2. Balance mein paise jama karne ke liye `deposit(amount)` method banana hai jo positive amount ko balance mein add kare.
3. Balance se paise nikalne ke liye `withdraw(amount)` method banana hai jo check kare ki kya balance sufficient hai; agar paise kam hain toh transaction reject kare.
4. Current account balance check karne aur print karne ke liye `check_balance()` method implement karna hai.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. Class Blueprint Aur Constructor
`BankAccount` class ke `__init__(self, account_number, owner_name, initial_balance=0.0)` constructor mein attributes assign kiye jaate hain. Har object ek unique bank account represent karta hai.

#### 2. Deposit Method Ki Invariant Logic
Deposit karte waqt amount strictly positive ($>0$) hona chahiye:

$$
B_{t+1} = B_t + \Delta, \quad \Delta > 0
$$

Agar koi negative ya zero amount deposit karne ki koshish kare, toh method ko warning print karke transaction reject karni chahiye.

#### 3. Overdraft Protection Withdraw Logic
Withdrawal ke dauran check karna zaroori hai ki:

$$
0 < \Delta \le B_t
$$

Agar user ke paas sirf $\$500$ hain aur woh $\$800$ withdraw karna chahe, toh method balance ko negative nahi hone dega, balki "Insufficient funds" ka error dega.

#### 4. Balance Invariant
Balance hamesha $\ge 0$ maintain rehna chahiye, jisse accounting integrity bani rahe.

---

## Question 02: Book Reviews Catalog Class

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. Ek `Book` class design karni hai jisme `title`, `author`, aur reviews store karne ke liye ek internal `list` attribute ho.
2. Naya book review add karne ke liye `add_review(review_text)` method implement karna hai.
3. Book par kul kitne reviews aa chuke hain unka total count return karne ke liye `count_reviews()` method banana hai.
4. Sabhi recorded reviews ko terminal par numbered list mein display karne ke liye `display_reviews()` method banana hai.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. Dynamic Attribute Aggregation
Constructor mein `self.reviews = []` initialize kiya jaata hai. Yeh ek container data structure hai jo multiple review strings ko dynamically grow hone deta hai.

#### 2. Adding Reviews
`add_review(self, review: str)` method review string ko validate karta hai aur `self.reviews.append(review)` call karke $\mathcal{O}(1)$ time mein store kar leta hai.

#### 3. Counting Reviews
Reviews ki count nikalne ke liye built-in `len(self.reviews)` use hota hai jo $\mathcal{O}(1)$ time complexity guarantee karta hai.

#### 4. Formatting Display
`display_reviews()` loop chala kar f-string format mein cleanly output deta hai, jaise:
- `1. Excellent explanation of data structures!`
- `2. Must read for AI engineers.`

---

## Question 03: Encapsulated Student Record With Validations

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. `Student` class create karni hai jisme teen private attributes ho: `_name`, `_roll_no`, aur `_marks`.
2. Python ke standard `@property` decorators ka upyog karke getters aur setters define karne hain.
3. Har setter ke andar strict validation rules enforce karne hain:
   - Marks negative nahi ho sakte ($\text{marks} \ge 0$).
   - Roll number 1 se 100 ke beech hona chahiye ($1 \le \text{roll\_no} \le 100$).
   - Name empty string nahi ho sakta ($|\text{name}| > 0$).
4. Agar validation fail ho, toh descriptive `ValueError` raise karna hai.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. Encapsulation & Private Attributes
Direct access `s.marks = -50` ko prevent karne ke liye attributes ko single underscore `_name`, `_roll_no`, `_marks` ke sath private/protected banaya jata hai.

#### 2. Property Getters Aur Setters
Getters read access dete hain aur Setters write access dete hain:
```python
@property
def marks(self):
    return self._marks

@marks.setter
def marks(self, val):
    if val < 0:
        raise ValueError("Marks cannot be negative")
    self._marks = val
```

#### 3. Invariant Boundaries
Validation constraints mathematically define hote hain:

$$
\text{marks} \in [0, \infty), \quad \text{roll\_no} \in [1, 100] \subset \mathbb{Z}, \quad \text{name} \neq \epsilon
$$

#### 4. Robust Security
Isse koi bhi external code object ke internal state ko corrupt nahi kar sakta.

---

## Question 04: Polymorphic Shape Hierarchy & Area Method Overriding

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. Ek generalized base class `Shape` banani hai jisme method `area()` define ho.
2. Teen specialized subclasses derive karni hain: `Circle`, `Rectangle`, aur `Triangle`.
3. Har subclass ke andar `area()` method ko override karke us shape ka exact mathematical formula implement karna hai:
   - Circle: $\pi r^2$
   - Rectangle: $\text{width} \times \text{height}$
   - Triangle: $\frac{1}{2} \times \text{base} \times \text{height}$
4. Polymorphism ko demonstrate karne ke liye alag-alag shapes ki list par loop chala kar unka area dynamically compute karna hai.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. Base Class Interface
Base class `Shape` ek common polymorphic protocol define karti hai. Iska `area()` method `raise NotImplementedError` throw karta hai agar koi subclass use override na kare.

#### 2. Mathematical Formulations

$$
\mathcal{A}_{\text{circle}} = \pi r^2, \quad \mathcal{A}_{\text{rect}} = w \cdot h, \quad \mathcal{A}_{\text{tri}} = \frac{1}{2} b \cdot h
$$

#### 3. Dynamic Dispatch Execution
Jab hum `shapes = [Circle(3), Rectangle(4, 5), Triangle(6, 4)]` banate hain aur `for s in shapes: s.area()` call karte hain:
Python runtime par object ki type inspect karta hai aur automatically sahi subclass ke formula ko execute karta hai.

#### 4. Unified Client Code
Caller code ko `if isinstance(s, Circle):` check karne ki zaroorat nahi padti; polymorphism dynamic routing handle karta hai.

---

## Question 05: Vehicle Inheritance (Car & Bike Subclasses)

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. Ek parent base class `Vehicle` create karni hai jisme common attributes `brand` aur `model` ho.
2. Ek child class `Car` banani hai jo `Vehicle` se inherit kare aur naya attribute `seats` add kare.
3. Ek doosri child class `Bike` banani hai jo `Vehicle` se inherit kare aur naya attribute `engine_cc` add kare.
4. Dono child classes ke constructors mein `super().__init__(brand, model)` ka use karke base attributes initialize karne hain.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. IS-A Taxonomic Relationship
Inheritance real-world taxonomy ko model karta hai:
- `Car` IS-A `Vehicle`
- `Bike` IS-A `Vehicle`

#### 2. Base Class Code Reuse
`brand` aur `model` ko baar-baar har class mein define karne ke bajaye humne use ek common `Vehicle` base class mein encapsulate kar diya.

#### 3. `super()` Constructor Chaining
Child class ke andar:
```python
class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats
```
`super()` ensure karta hai ki parent class ka initialization logic properly trigger ho.

#### 4. Attribute Specialization
Child class apne extra unique attributes (`seats` ya `engine_cc`) ko safely add kar leti hai.

---

## Question 06: Abstract Employee Class & Payroll Subclasses

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. Python ke `abc` module ka use karke ek abstract class `Employee` create karni hai.
2. Uske andar ek `@abstractmethod` declare karna hai: `calculate_salary()`.
3. Teen concrete subclasses derive karni hain:
   - `Intern`: Fixed stipend return kare.
   - `FullTimeEmployee`: Base salary + bonus ($S = \text{base} + \text{bonus}$) return kare.
   - `ContractEmployee`: Hourly rate $\times$ hours ($S = \text{rate} \times \text{hours}$) return kare.
4. Verify karna hai ki `Employee` ka direct object create nahi ho sakta (`TypeError`).

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. Abstract Base Class Definition
```python
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
```
Abstract class ek blueprint contract hoti hai jo kehti hai: "Jo bhi employee banega, use apna salary calculation method zaroor banana padega."

#### 2. Subclass Implementations
- `Intern` fixed stipend model use karta hai.
- `FullTimeEmployee` salaried contract calculate karta hai.
- `ContractEmployee` gig/hourly billing calculate karta hai.

#### 3. Compile-Time Contract Enforcement
Agar koi subclass `calculate_salary()` likhna bhool jaaye, toh Python uska instance create karte waqt hi `TypeError` raise kar deta hai.

#### 4. Polymorphic Payroll Engine
Company payroll system ek single list `employees = [intern1, fte1, contract1]` ko iterate karke sabki salary compute kar sakta hai.

---

## Question 07: Constructor Overloading Simulation (Default Parameters)

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. Ek class `Person` banani hai jiska constructor teen alag-alag configurations mein kaam kare:
   - Sirf name: `Person("Alice")`
   - Name aur age: `Person("Bob", 25)`
   - Name, age, aur address: `Person("Charlie", 30, "Delhi")`
2. Python mein multiple constructors allowed nahi hote, isliye **default parameters** (`age=None`, `address=None`) ka use karke overloading simulate karni hai.
3. Person ke details ko clean format mein print karne ka method likhna hai.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. Why Python Lacks Native Constructor Overloading
C++ ya Java mein parameter types ke aadhar par compiler function signature identify karta hai. Python dynamic language hai jaha function dictionary keys hote hain, isliye doosra `__init__` pehle wale ko replace kar deta hai.

#### 2. Default Parameters Simulation
Constructor signature:
```python
def __init__(self, name: str, age: Optional[int] = None, address: Optional[str] = None):
    self.name = name
    self.age = age
    self.address = address
```

#### 3. Dynamic Representation
Agar `age` ya `address` pass nahi kiya gaya, toh woh `None` rehta hai aur string display method conveniently `"Age: N/A"` show kar sakta hai.

#### 4. Clean Caller API
User apni requirement ke hisab se 1, 2, ya 3 arguments pass karke object instantiate kar sakta hai.

---

## Question 08: Player Class & Global Player Count Variable

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. Ek `Player` class banani hai jisme do instance variables ho: `name` aur `level`.
2. Ek class variable `player_count` create karna hai jo shuru mein 0 ho.
3. Jab bhi naya `Player` object instantiate ho, automatically `Player.player_count` 1 se badhna chahiye.
4. Total players count check karne ke liye ek `@classmethod` provide karna hai.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. Class Variable vs Instance Variable
- `player_count` class-level par rehta hai (single memory location across all objects).
- `name` aur `level` har player ke instance dictionary mein alag-alag store hote hain.

#### 2. Auto-Increment Mechanics In `__init__`
Constructor ke andar:
```python
def __init__(self, name: str, level: int = 1):
    self.name = name
    self.level = level
    Player.player_count += 1
```
Har baar jab naya object banta hai, shared counter $C_{t+1} = C_t + 1$ badh jata hai.

#### 3. Class Method Retrieval
```python
@classmethod
def get_total_players(cls):
    return cls.player_count
```
`cls.player_count` access karne se code clean aur subclass-friendly rehta hai.

#### 4. Instance Tracking Verification
10 players banane ke baad `Player.get_total_players()` exactly 10 return karega.

---

## Question 09: Multiple Inheritance (Herbivore, Carnivore & Bear)

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. Ek `Herbivore` class create karni hai jisme plant-eating behaviors aur attributes ho.
2. Ek `Carnivore` class create karni hai jisme meat-hunting behaviors aur attributes ho.
3. Ek `Bear` (ya `Omnivore`) class banani hai jo dono `Herbivore` aur `Carnivore` se ek saath inherit kare.
4. Multiple inheritance ke kaam karne ke tareeqe aur Python ke Method Resolution Order (MRO) ko explain karna hai.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. Multiple Inheritance Syntax
```python
class Bear(Herbivore, Carnivore):
    pass
```
`Bear` class dono parent classes ke attributes aur methods ko inherit kar leti hai, isliye bhalu ghaas/berries bhi kha sakta hai aur shikaar bhi kar sakta hai.

#### 2. Method Resolution Order (MRO)
Agar dono parents ke paas same method name ho (jaise `eat()`), toh Python pehle `Herbivore` ko dekhega kyunki woh pehle listed hai (left-to-right order):

$$
L(\text{Bear}) = [\text{Bear}, \text{Herbivore}, \text{Carnivore}, \text{object}]
$$

#### 3. The `mro()` Inspection Method
Python mein `Bear.mro()` call karke exact linearization path terminal par print kiya ja sakta hai.

#### 4. Diamond Problem Avoidance
CPython C3 Linearization use karta hai jo kabhi bhi circular ya ambiguous inheritance hierarchy allow nahi karta.

---

## Question 10: Mini-Project – OOP Chat System

### 📋 Is Question Mein Aapse Kya Pucha Gaya Hai?
1. Ek complete Object-Oriented Chat System design karna hai jisme teen classes ho: `Message`, `User`, aur `ChatRoom`.
2. `Message` class: Message id (auto-incrementing), sender user, content, aur string formatting `(id) username: content`.
3. `User` class: Username, current chatroom pointer, `join_chatroom()`, `leave_chatroom()`, aur `send_message()`.
4. `ChatRoom` class: Room name, users list, messages history, `add_user()`, `remove_user()`, `broadcast()`, aur `show_chat_history()`.

### 🔍 Har Ek Bullet Point Ka Detailed Explanation

#### 1. System Architecture & Entity Relationships
- `ChatRoom` contains multiple `User` objects (Aggregation).
- `ChatRoom` contains multiple `Message` objects (Composition).
- `User` points to active `ChatRoom` reference.

#### 2. Message Class Mechanics
Class variable `message_counter = 1` rakha jata hai. Har naye message par `self.id = Message.message_counter` assign hota hai aur counter badh jata hai.

#### 3. User Actions
- `join_chatroom(room)`: Room ke `add_user` ko call karta hai aur `self.chatroom = room` set karta hai.
- `leave_chatroom()`: Room se remove hota hai aur reference `None` kar deta hai.
- `send_message(text)`: Room ke `broadcast` method ko trigger karta hai.

#### 4. ChatRoom Broadcast Engine
Jab koi user message bhejta hai, `broadcast()` naya `Message` object banata hai, history mein append karta hai, aur sabhi members ko print karke display karta hai.

---

## Systems Case Study 1: CPython Object Memory Aur \_\_slots\_\_ Architecture

### 📋 Is Case Study Mein Aapse Kya Pucha Gaya Hai?
1. CPython ke internal `PyObject` structure ka memory model study karna.
2. Compare karna standard `__dict__` dynamic hash table memory vs `__slots__` fixed C pointer array memory.
3. 100,000 objects instantiate karke RAM memory savings benchmark karna (~65% reduction).
4. 300 DPI high-resolution memory comparison graph plot karna.

---

## Systems Case Study 2: Diamond Inheritance Aur C3 Linearization (MRO)

### 📋 Is Case Study Mein Aapse Kya Pucha Gaya Hai?
1. Classic Diamond Problem inheritance graph ka mathematical model banana.
2. C3 Linearization merge algorithm $L(C) = C + \text{merge}(...)$ ko step-by-step trace karna.
3. Explain karna ki Python 2.3+ ne purani depth-first MRO ko discard karke C3 Linearization kyu adopt kiya.
4. Diamond inheritance graph aur MRO resolution trajectory ka 300 DPI visualizer render karna.

---

## Systems Case Study 3: Dynamic Attribute Lookup Protocol Aur Descriptors

### 📋 Is Case Study Mein Aapse Kya Pucha Gaya Hai?
1. CPython ke `__getattribute__` internal resolution hierarchy ka study karna.
2. Data Descriptor (`__set__`), Instance `__dict__`, Non-Data Descriptor (Methods), Class `__dict__`, aur `__getattr__` fallback ki priority chain explain karna.
3. Bound method vs unbound method transformation mechanics analyze karna.
4. Attribute lookup decision tree ka 300 DPI flow chart graph render karna.
