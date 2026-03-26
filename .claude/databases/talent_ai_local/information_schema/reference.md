# Database: talent_ai_local (information_schema schema)
Last updated: 2025-11-21 10:35:23

## Table List
- sql_parts (5 columns)
- sql_features (7 columns)
- sql_implementation_info (5 columns)
- sql_sizing (4 columns)

## Schema Details

TABLE: sql_parts
  [Column | Type | Constraints | Sample1 | Sample2]
  feature_id | DOMAIN | - | "3" | "10"
  feature_name | DOMAIN | - | "Multi-Dimensional Arrays (SQL/MDA)" | "Framework (SQL/Framework)"
  is_supported | DOMAIN | - | "NO" | -
  is_verified_by | DOMAIN | - | - | -
  comments | DOMAIN | - | "" | -

TABLE: sql_features
  [Column | Type | Constraints | Sample1 | Sample2]
  feature_id | DOMAIN | - | "B125" | "T615"
  feature_name | DOMAIN | - | "User authorization" | "SQL/JSON path language: item method"
  sub_feature_id | DOMAIN | - | "12" | "10"
  sub_feature_name | DOMAIN | - | "UNIQUE constraints of NOT NULL columns" | "LIKE predicate"
  is_supported | DOMAIN | - | "YES" | "NO"
  is_verified_by | DOMAIN | - | - | -
  comments | DOMAIN | - | "differences regarding literal interpretation" | "only some syntax variants supported"

TABLE: sql_implementation_info
  [Column | Type | Constraints | Sample1 | Sample2]
  implementation_info_id | DOMAIN | - | "18" | "2"
  implementation_info_name | DOMAIN | - | "CURSOR COMMIT BEHAVIOR" | "DBMS NAME"
  integer_value | DOMAIN | - | 0 | 1
  character_value | DOMAIN | - | "PostgreSQL" | "17.05.0000)"
  comments | DOMAIN | - | "stored in mixed case - case sensitive" | "all non-ASCII characters allowed"

TABLE: sql_sizing
  [Column | Type | Constraints | Sample1 | Sample2]
  sizing_id | DOMAIN | - | 25005 | 101
  sizing_name | DOMAIN | - | "MAXIMUM CATALOG NAME LENGTH" | "MAXIMUM COLUMN NAME LENGTH"
  supported_value | DOMAIN | - | 63 | 1600
  comments | DOMAIN | - | "Might be less, depending on character set." | -
