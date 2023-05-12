```mermaid
classDiagram

Duck  --|> Animal

class Animal{
+int id
+string name
}

class Duck{
+int id
+string text
+int person_id (fk)
}
```
