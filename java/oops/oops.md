**OOPS (Object-Oriented Programming System)** is a programming paradigm (way of writing code) that organizes software design around **objects** instead of functions and logic.

An **object** represents a real-world entity and contains:

* **Data (attributes / variables)**
* **Behavior (methods / functions)**

---

## 🔑 Core Concepts of OOPS

### 1. **Class**

A **class** is a blueprint or template to create objects.

👉 Example:
Think of a *Car* as a class — it defines properties like color, speed, engine.

---

### 2. **Object**

An **object** is an instance of a class.

👉 Example:
A specific car like *Honda City (Red)* is an object of the Car class.

---

### 3. **Encapsulation**

Wrapping data (variables) and methods into a single unit (class) and restricting direct access.

👉 Benefit:

* Data hiding
* Better control

👉 Example:

```java
class BankAccount {
    private double balance;

    public void deposit(double amount) {
        balance += amount;
    }
}
```

---

### 4. **Inheritance**

One class can acquire properties and behavior of another class.

👉 Benefit:

* Code reuse

👉 Example:

```java
class Vehicle {
    void start() {}
}

class Car extends Vehicle {
    void drive() {}
}
```

---

### 5. **Polymorphism**

One action, many forms.

👉 Types:

* **Compile-time** (method overloading)
* **Runtime** (method overriding)

👉 Example:

```java
void add(int a, int b) {}
void add(double a, double b) {}
```

---

### 6. **Abstraction**

Hiding implementation details and showing only essential features.

👉 Example:

* You drive a car without knowing how the engine works.

---

## 🎯 Why OOPS is Important

* Makes code **modular**
* Improves **reusability**
* Easier **maintenance**
* Helps in building **scalable systems** (very important for your Java/Spring Boot work)

---

## 💡 Real-Life Example

Think of a **Bank System**:

* Class → Account
* Object → Rahul’s Account
* Encapsulation → Balance is private
* Inheritance → SavingsAccount, CurrentAccount
* Polymorphism → Different interest calculation
* Abstraction → User doesn’t see backend logic

-------

