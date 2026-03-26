# Database: example_db (public schema)
Last updated: 2025-11-18 15:30:00

## Table List
- users (5 columns)
- orders (7 columns)
- products (4 columns)

## Schema Details

TABLE: users
  [Column | Type | Constraints | Sample1 | Sample2]
  id | INTEGER | PRIMARY KEY, NOT NULL | 1 | 42
  email | VARCHAR(255) | UNIQUE, NOT NULL | "john@example.com" | "jane@example.com"
  username | VARCHAR(100) | UNIQUE, NOT NULL | "john_doe" | "jane_smith"
  created_at | TIMESTAMP | NOT NULL | "2025-01-15 10:23:45" | "2025-01-16 08:12:33"
  profile_data | JSONB | - | {"name": "John", "age": 30, "preferences": {"theme": "dark", "notifications": true}} | {"name": "Jane", "age": 28, "bio": "Software engineer passionate about..."}

TABLE: orders
  [Column | Type | Constraints | Sample1 | Sample2]
  id | INTEGER | PRIMARY KEY, NOT NULL | 1001 | 1002
  user_id | INTEGER | FOREIGN KEY -> users(id), NOT NULL | 1 | 42
  product_id | INTEGER | FOREIGN KEY -> products(id), NOT NULL | 5 | 8
  quantity | INTEGER | NOT NULL | 2 | 1
  total_price | NUMERIC(10, 2) | NOT NULL | 49.99 | 129.99
  status | VARCHAR(50) | NOT NULL | "pending" | "completed"
  created_at | TIMESTAMP | NOT NULL | "2025-11-01 14:22:10" | "2025-11-02 09:15:33"

TABLE: products
  [Column | Type | Constraints | Sample1 | Sample2]
  id | INTEGER | PRIMARY KEY, NOT NULL | 5 | 8
  name | VARCHAR(200) | NOT NULL | "Wireless Headphones" | "Smart Watch"
  price | NUMERIC(10, 2) | NOT NULL | 79.99 | 199.99
  description | TEXT | - | "High-quality wireless headphones with noise cancellation and 30-hour battery life. Features Bluetooth 5.0 connectivity and comfortable over-ear design perfect for travel and daily use." | "Advanced fitness tracker with heart rate monitoring, GPS, and waterproof design. Track your..."
