# 1. Detailed Class Diagram for Business Logic Layer

This diagram shows the main entities of the HBnB application: **User**, **Place**, **Review**, and **Amenity**.  
Each class includes its key attributes, methods, and relationships with other classes.
```mermaid
classDiagram
    class User {
        +UUID id
        +String first_name
        +String last_name
        +String email
        +String password
        +Bolean is_admin
        +DataTime creadet_at
        +DataTime updated_at
        +reagister()
        +update_profile()
        +delete_acount()
    }

    class Place {
        +UUID id
        +String title
        +String description
        +Float price
        +Float latitude
        +Float longitude
        +DateTime created_at
        +DateTime updated_at
        +create()
        +update()
        +delete()
        +list_amenities()
    }

    class Review {
        +UUID id
        +Int rating
        +String comment
        +DateTime created_at
        +DateTime updated_at
        +create()
        +update()
        +delete()
    }

    class Amenity {
        +UUID id
        +String name
        +String description
        +DateTime created_at
        +DateTime updated_at
        +create()
        +update()
        +delete()
    }

    %% Relationships
    User "1" --> "many" Place : owns >
    User "1" --> "many" Review : writes >
    Place "1" --> "many" Review : has >
    Place "many" --> "many" Amenity : includes >
