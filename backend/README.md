## How to Add new Models:

### 1. Create Your Models
- Add your models in the `core/models` folder.
- Each model should inherit from `Base`.

### 2. Register Your Models
- Import all your new models in core/models/__init__.py.

### 3. Generate a Migration
- Open a terminal and navigate to the backend folder:
```bash
cd backend
```
- Run Alembic autogeneration to create a migration file:
```bash
alembic revision --autogenerate -m "add description of your models"
```

### 4. Apply the Migration
- Upgrade your database to apply the new schema:
```bash
alembic upgrade head
```