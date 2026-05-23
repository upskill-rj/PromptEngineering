# 🚀 LLD Case Studies Using OOPS + Design Patterns

## Architect Interview Preparation

These are the most commonly asked Low-Level Design problems in:

* Deloitte
* Accenture
* Amazon
* Uber
* Product companies & FinTech

---

# 📚 What Interviewers Evaluate in LLD

| Area                | Expectation                |
| ------------------- | -------------------------- |
| OOPS                | Encapsulation, abstraction |
| Design Patterns     | Factory, Strategy          |
| Relationships       | Composition, inheritance   |
| Scalability         | Extensible design          |
| Clean Code          | Maintainability            |
| Real-world thinking | Edge cases                 |

---

# 🚗 CASE STUDY 1 — Parking Lot System

---

# 🎯 Requirements

Design a parking lot system supporting:

* Car
* Bike
* Truck

Features:

* Park vehicle
* Remove vehicle
* Calculate parking fee
* Multiple floors

---

# 🏗️ HLD View

```text id="h5v6sf"
Parking Lot
    ↓
Parking Floors
    ↓
Parking Slots
    ↓
Vehicles
```

---

# 🧠 Step 1 — Identify Classes

| Entity         | Responsibility  |
| -------------- | --------------- |
| Vehicle        | Base class      |
| Car/Bike/Truck | Vehicle types   |
| ParkingSlot    | Slot details    |
| ParkingFloor   | Multiple slots  |
| ParkingLot     | Main system     |
| Ticket         | Parking receipt |

---

# 🔥 OOPS Design

---

# 🔹 Vehicle (Abstraction)

```java id="r8v8lx"
public abstract class Vehicle {

    protected String number;

    public Vehicle(String number) {
        this.number = number;
    }

    public abstract double getRate();
}
```

---

# 🔹 Car

```java id="vq0e8w"
public class Car extends Vehicle {

    public Car(String number) {
        super(number);
    }

    public double getRate() {
        return 50;
    }
}
```

---

# 🔹 Bike

```java id="m2w5wd"
public class Bike extends Vehicle {

    public Bike(String number) {
        super(number);
    }

    public double getRate() {
        return 20;
    }
}
```

---

# 🔹 Parking Slot

```java id="1szggk"
public class ParkingSlot {

    private int slotNumber;

    private boolean occupied;

    private Vehicle vehicle;

    public boolean park(Vehicle vehicle) {

        if(!occupied) {

            this.vehicle = vehicle;

            occupied = true;

            return true;
        }

        return false;
    }
}
```

---

# 🔹 Parking Lot

```java id="afz3gx"
public class ParkingLot {

    private List<ParkingSlot> slots;

    public boolean parkVehicle(
        Vehicle vehicle) {

        for(ParkingSlot slot : slots) {

            if(slot.park(vehicle))
                return true;
        }

        return false;
    }
}
```

---

# 🎯 Design Patterns Used

| Pattern   | Usage           |
| --------- | --------------- |
| Factory   | Create vehicle  |
| Strategy  | Fee calculation |
| Singleton | Parking manager |

---

# 🧠 Interview Discussion Points

## Scalability

* Multi-floor support
* Redis cache for available slots

## Concurrency

* Multiple users parking simultaneously

## DB Design

* Ticket table
* Slot table

---

# 🎬 CASE STUDY 2 — BookMyShow System

---

# 🎯 Requirements

Design movie booking system:

* Search movies
* Select seats
* Book tickets
* Payment integration

---

# 🏗️ HLD

```text id="c2vb2l"
User
   ↓
Movie Service
   ↓
Theatre
   ↓
Show
   ↓
Seat Booking
```

---

# 🧠 Step 1 — Identify Classes

| Class   | Responsibility     |
| ------- | ------------------ |
| Movie   | Movie details      |
| Theatre | Screens            |
| Show    | Timing             |
| Seat    | Seat state         |
| Booking | Reservation        |
| Payment | Payment processing |

---

# 🔥 OOPS Design

---

# 🔹 Movie

```java id="bq0k2y"
public class Movie {

    private String name;

    private String genre;
}
```

---

# 🔹 Seat

```java id="1o3x5i"
public class Seat {

    private int seatNo;

    private boolean booked;

    public boolean book() {

        if(!booked) {

            booked = true;

            return true;
        }

        return false;
    }
}
```

---

# 🔹 Booking Service

```java id="3z7a8u"
public class BookingService {

    public boolean reserveSeat(Seat seat) {

        return seat.book();
    }
}
```

---

# 🎯 Critical Interview Discussion

---

# 🔥 Concurrency Problem

Two users booking same seat.

---

# ✅ Solution

Use:

* optimistic locking
* distributed lock
* DB transaction

---

# 🔥 Example

```java id="jlwm0n"
@Version
private Long version;
```

---

# 🎯 Design Patterns Used

| Pattern   | Usage           |
| --------- | --------------- |
| Factory   | Payment methods |
| Strategy  | Pricing         |
| Observer  | Notifications   |
| Singleton | Booking manager |

---

# 🔥 Real Production Thinking

| Concern         | Solution         |
| --------------- | ---------------- |
| High traffic    | Redis caching    |
| Seat locking    | Distributed lock |
| Async email     | Kafka            |
| Payment failure | Saga pattern     |

---

# 🚖 CASE STUDY 3 — Uber System

---

# 🎯 Requirements

Design ride booking system:

* Book ride
* Match nearby drivers
* Real-time location tracking
* Fare calculation
* Payment

---

# 🏗️ HLD

```text id="3ezd8h"
Passenger App
      ↓
API Gateway
      ↓
Ride Service
Driver Service
Location Service
Payment Service
      ↓
Kafka
      ↓
Notification Service
```

---

# 🧠 Step 1 — Identify Classes

| Class     | Responsibility  |
| --------- | --------------- |
| User      | Base user       |
| Driver    | Driver details  |
| Passenger | Rider           |
| Ride      | Ride details    |
| Location  | Coordinates     |
| Payment   | Fare processing |

---

# 🔥 OOPS Design

---

# 🔹 User Base Class

```java id="jlwm1p"
public abstract class User {

    protected String name;

    protected String phone;
}
```

---

# 🔹 Driver

```java id="jlwm2q"
public class Driver extends User {

    private Location currentLocation;

    private boolean available;
}
```

---

# 🔹 Passenger

```java id="jlwm3r"
public class Passenger extends User {
}
```

---

# 🔹 Ride

```java id="jlwm4s"
public class Ride {

    private Driver driver;

    private Passenger passenger;

    private double fare;
}
```

---

# 🔥 Strategy Pattern (Fare Calculation)

```java id="jlwm5t"
public interface FareStrategy {

    double calculateFare(double distance);
}
```

---

# 🔹 Surge Pricing

```java id="jlwm6u"
public class SurgePricing
implements FareStrategy {

    public double calculateFare(
        double distance) {

        return distance * 20;
    }
}
```

---

# 🔹 Normal Pricing

```java id="jlwm7v"
public class NormalPricing
implements FareStrategy {

    public double calculateFare(
        double distance) {

        return distance * 10;
    }
}
```

---

# 🎯 Interview Discussion Points

---

# 🔥 Real-Time Driver Matching

Use:

* GeoHash
* Redis GEO
* Elasticsearch

---

# 🔥 Real-Time Tracking

Use:

* WebSocket
* Kafka streams

---

# 🔥 Scalability

Use:

* Kubernetes auto-scaling
* Redis caching

---

# 🎯 Design Patterns Used

| Pattern   | Usage              |
| --------- | ------------------ |
| Strategy  | Fare calculation   |
| Observer  | Ride notifications |
| Factory   | Vehicle creation   |
| Singleton | Driver manager     |
| Saga      | Payment workflow   |

---

# 🔥 Common LLD Interview Questions

---

## ❓ Why interfaces?

👉 Achieve:

* abstraction
* loose coupling
* testability

---

## ❓ Why composition over inheritance?

👉 Better flexibility.

---

## ❓ Why design patterns?

👉 Improve:

* maintainability
* scalability
* extensibility

---

# 🧠 Architect-Level Interview Answer

> “In LLD interviews, I first identify entities, relationships, APIs, and workflows. Then I apply OOPS principles like abstraction, encapsulation, inheritance, and polymorphism. I use design patterns such as Strategy, Factory, Observer, and Repository to create scalable and maintainable systems. I also consider concurrency, scalability, distributed transactions, and production-level concerns like caching and asynchronous communication.”

---


