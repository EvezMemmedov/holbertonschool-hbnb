## Class Diagram

```mermaid
classDiagram
    class User {
        +UUID id
        +String first_name
        +String last_name
        +String email
        +String password
        +Boolean is_admin
        +DateTime created_at
        +DateTime updated_at
        +register()
        +update_profile()
        +delete_account()
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

    User --> Place : owns >
    User --> Review : writes >
    Place *-- Review : has >
    Place *-- Amenity : includes >
