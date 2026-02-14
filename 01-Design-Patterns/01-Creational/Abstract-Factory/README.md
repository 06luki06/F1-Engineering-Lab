# Pattern Specification: Abstract Factory

## 🏎️ F1 Context: The Power Unit Ecosystem

Modern F1 cars run on complex Power Units. A Power Unit is not a single block but a system of tightly coupled components:

1. **The ICE (Internal Combustion Engine):** The V6 Turbo.
2. **The ERS (Energy Recovery System):** The battery and electric motors (MGU-K, MGU-H).

**The Problem:**
A team cannot mix and match. If Haas buys a Ferrari ICE, they *must* also use the Ferrari ERS. The components must be compatible.

## 🎯 Objective

Provide an interface for creating families of related or dependent objects (ICE + ERS) without specifying their concrete classes.

---

## 🛠️ Functional Requirements

### 1. Abstract Products

Define interfaces for the individual components.

* **`ICE` (Interface):**
  * Method `start()`: Returns a sound string.
* **`ERS` (Interface):**
  * Method `recover_energy()`: Returns a status string (e.g., "Recovering 2MJ").

### 2. Abstract Factory

Define the interface that creates the suite of products.

* **`TeamFactory` (Interface):**
  * Method `create_ice()` -> Returns an `ICE` object.
  * Method `create_ers()` -> Returns an `ERS` object.

### 3. Concrete Factories (The Families)

* **`FerrariFactory`**: Creates `FerrariICE` and `FerrariERS`.
* **`MercedesFactory`**: Creates `MercedesICE` and `MercedesERS`.

### 4. Client Code

The client (The Chassis) asks for a factory (e.g., "Ferrari") and then uses that factory to assemble the car. It never uses `new FerrariICE()` directly.

---

## 📊 Diagrams

### Class Diagram

Notice how the factories group the products into vertical "families".

```mermaid
classDiagram
    %% Abstract Factory
    class TeamFactory {
        <<Interface>>
        +create_ice() ICE
        +create_ers() ERS
    }

    %% Concrete Factories
    class FerrariFactory {
        +create_ice() FerrariICE
        +create_ers() FerrariERS
    }
    class MercedesFactory {
        +create_ice() MercedesICE
        +create_ers() MercedesERS
    }

    %% Relationships
    TeamFactory <|-- FerrariFactory
    TeamFactory <|-- MercedesFactory

    %% Abstract Products
    class ICE { <<Interface>> +start() }
    class ERS { <<Interface>> +recover_energy() }

    %% Concrete Products
    class FerrariICE
    class FerrariERS
    class MercedesICE
    class MercedesERS

    ICE <|-- FerrariICE
    ICE <|-- MercedesICE
    ERS <|-- FerrariERS
    ERS <|-- MercedesERS

    %% Dependency Lines
    FerrariFactory ..> FerrariICE : creates
    FerrariFactory ..> FerrariERS : creates
    MercedesFactory ..> MercedesICE :create
    MercedesFactory ..> MercedesERS : create
```

### Sequence Diagram

The client gets a factory and then requests both parts.

```mermaid
sequenceDiagram
    participant Client as F1 Team
    participant Factory as FerrariFactory
    participant Engine as FerrariICE
    participant Battery as FerrariERS

    Note over Client, Factory: Client holds reference to Abstract Factory

    Client->>Factory: create_ice()
    Factory-->>Client: returns FerrariICE
    
    Client->>Factory: create_ers()
    Factory-->>Client: returns FerrariERS

    Note right of Client: Parts are guaranteed to be compatible
```
