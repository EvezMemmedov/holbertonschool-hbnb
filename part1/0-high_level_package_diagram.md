# 0. High-Level Package Diagram

The system follows a **Layered Architecture** composed of three main layers:
1. Presentation Layer
2. Business Logic Layer
3. Persistence Layer

A **Facade Pattern** is used to simplify interactions between layers.

---

## Diagram

```mermaid
graph TD

subgraph PresentationLayer
  API["API Services / User Interface"]
end

subgraph BusinessLogicLayer
  Facade["HBnBFacade"]
  Models["Models: User, Place, Review, Amenity"]
end

subgraph PersistenceLayer
  Database["Database Access / Repository"]
end

API --> Facade
Facade --> Models
Models --> Database
