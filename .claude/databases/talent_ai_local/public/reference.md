# Database: talent_ai_local (public schema)
Last updated: 2025-11-21 10:35:32

## Table List
- django_migrations (4 columns)
- django_content_type (3 columns)
- auth_permission (4 columns)
- auth_group (2 columns)
- auth_group_permissions (3 columns)
- auth_user (11 columns)
- auth_user_groups (3 columns)
- auth_user_user_permissions (3 columns)
- account_emailaddress (5 columns)
- account_emailconfirmation (5 columns)
- accounts_clientgroup (9 columns)
- accounts_loginlog (9 columns)
- accounts_userclientrole (8 columns)
- accounts_userrole (3 columns)
- accounts_delegatedpermission (10 columns)
- accounts_userprofile (12 columns)
- django_admin_log (8 columns)
- ai_models_modeldefaultparameters (11 columns)
- ai_models_promptrecipe (16 columns)
- ai_models_promptordering (4 columns)
- ai_models_modelparameterset (10 columns)
- ai_models_aimodel (16 columns)
- ai_models_unifiedendpoint (12 columns)
- ai_models_prompt (15 columns)
- ai_models_apisecret (9 columns)
- storage_storedfile (15 columns)
- chat_conversation (9 columns)
- chat_message (12 columns)
- conversion_conversionjob (16 columns)
- conversion_convertedimage (12 columns)
- extraction_document (16 columns)
- extraction_extractionjob (20 columns)
- extraction_extractedcontent (13 columns)
- mcq_test_testattempt (9 columns)
- mcq_test_questiontracking (13 columns)
- mcq_test_testable_skills (4 columns)
- mcq_test_question (18 columns)
- mcq_test_testconfiguration (12 columns)
- mcq_test_candidateresponse (13 columns)
- django_session (3 columns)
- django_site (3 columns)
- skill_ontology_relationship (9 columns)
- skill_ontology_skillclassificationissue (10 columns)
- skill_ontology_word (9 columns)
- skill_ontology_normalizedform (9 columns)
- skill_ontology_skillclassificationrequest (12 columns)
- skill_ontology_skillclassificationrequest_search_candidates6fbc (3 columns)
- socialaccount_socialaccount (7 columns)
- socialaccount_socialapp (8 columns)
- socialaccount_socialapp_sites (3 columns)
- socialaccount_socialtoken (6 columns)
- authtoken_token (3 columns)
- file_audit_logs (20 columns)
- debug_toolbar_historyentry (3 columns)
- celery_task_status (11 columns)
- audit_logs_soc2 (13 columns)
- resume_parsing_jobs (28 columns)
- educations (20 columns)
- certifications (16 columns)
- locations (17 columns)
- parsed_resumes (21 columns)
- work_experiences (21 columns)
- resume_skill_scores (12 columns)
- resume_change_logs (13 columns)
- job_roles_normalized_locations (3 columns)
- job_skill_requirements (14 columns)
- job_roles (44 columns)
- job_parsing_jobs (30 columns)
- job_role_change_logs (13 columns)
- pipeline_history (11 columns)
- pipeline_entry (10 columns)
- stage_registry (10 columns)
- pipeline_config (9 columns)
- matching_stage_config (4 columns)
- matching_job (5 columns)
- communications_trackedemailthread (8 columns)
- sourcing_event (12 columns)
- sourcing_config (9 columns)
- direct_upload_record (5 columns)
- communications_mockcandidate (5 columns)
- jobdiva_audit_logs (21 columns)
- health_check_db_testmodel (2 columns)
- candidates_candidateexperience (18 columns)
- failed_candidate_creations (17 columns)
- candidates_candidate (33 columns)
- candidate_documents (13 columns)
- document_types (9 columns)
- candidates_candidateeducation (14 columns)
- candidates_majorcategory (10 columns)
- candidates_degreetype (11 columns)
- candidates_companycategory (10 columns)

## Schema Details

TABLE: django_migrations
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | 1 | 2
  app | VARCHAR(255) | NOT NULL | "matching" | "mcq_test"
  name | VARCHAR(255) | NOT NULL | "0007_alter_validators_add_error_messages" | "0007_jobparsingjob_external_job_id_and_more"
  applied | TIMESTAMP | NOT NULL | 2025-10-13 12:23:29.806476+00:00 | 2025-10-20 22:23:49.866674+00:00

TABLE: django_content_type
  [Column | Type | Constraints | Sample1 | Sample2]
  id | INTEGER | PRIMARY KEY, NOT NULL | 1 | 2
  app_label | VARCHAR(100) | NOT NULL, UNIQUE | "account" | "accounts"
  model | VARCHAR(100) | NOT NULL, UNIQUE | "clientgroup" | "promptrecipe"

TABLE: auth_permission
  [Column | Type | Constraints | Sample1 | Sample2]
  id | INTEGER | PRIMARY KEY, NOT NULL | 1 | 2
  name | VARCHAR(255) | NOT NULL | "Can delete Relationship" | "Can add Conversion Job"
  content_type_id | INTEGER | NOT NULL, UNIQUE, FOREIGN KEY -> django_content_type(id) | 1 | 2
  codename | VARCHAR(100) | NOT NULL, UNIQUE | "delete_testconfiguration" | "change_certification"

TABLE: auth_group
  [Column | Type | Constraints | Sample1 | Sample2]
  id | INTEGER | PRIMARY KEY, NOT NULL | - | -
  name | VARCHAR(150) | NOT NULL, UNIQUE | - | -

TABLE: auth_group_permissions
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | - | -
  group_id | INTEGER | NOT NULL, UNIQUE, FOREIGN KEY -> auth_group(id) | - | -
  permission_id | INTEGER | NOT NULL, UNIQUE, FOREIGN KEY -> auth_permission(id) | - | -

TABLE: auth_user
  [Column | Type | Constraints | Sample1 | Sample2]
  id | INTEGER | PRIMARY KEY, NOT NULL | 17 | 20
  password | VARCHAR(128) | NOT NULL | "!7c7c0Bjvk1Z3jYwdKmYdkxYhDiOBsbImtfQ4qp26" | ""
  last_login | TIMESTAMP | - | 2025-11-21 14:35:48.657174+00:00 | -
  is_superuser | BOOLEAN | NOT NULL | False | True
  username | VARCHAR(150) | NOT NULL, UNIQUE | "model_change_test" | "michaelbrown7284@gmail.com"
  first_name | VARCHAR(150) | NOT NULL | "Alex" | "Michael"
  last_name | VARCHAR(150) | NOT NULL | "Tester" | "Jones"
  email | VARCHAR(254) | NOT NULL | "audit_test@example.com" | "model_change@example.com"
  is_staff | BOOLEAN | NOT NULL | False | True
  is_active | BOOLEAN | NOT NULL | False | True
  date_joined | TIMESTAMP | NOT NULL | 2025-10-24 00:34:57.072129+00:00 | 2025-10-24 00:06:58.532347+00:00

TABLE: auth_user_groups
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | - | -
  user_id | INTEGER | NOT NULL, UNIQUE, FOREIGN KEY -> auth_user(id) | - | -
  group_id | INTEGER | NOT NULL, UNIQUE, FOREIGN KEY -> auth_group(id) | - | -

TABLE: auth_user_user_permissions
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | - | -
  user_id | INTEGER | NOT NULL, UNIQUE, FOREIGN KEY -> auth_user(id) | - | -
  permission_id | INTEGER | NOT NULL, UNIQUE, FOREIGN KEY -> auth_permission(id) | - | -

TABLE: account_emailaddress
  [Column | Type | Constraints | Sample1 | Sample2]
  id | INTEGER | PRIMARY KEY, NOT NULL | 5 | 6
  email | VARCHAR(254) | NOT NULL, UNIQUE | "alexjones2847@gmail.com" | "emilydavis4829@gmail.com"
  verified | BOOLEAN | NOT NULL | False | -
  primary | BOOLEAN | NOT NULL | True | -
  user_id | INTEGER | NOT NULL, UNIQUE, FOREIGN KEY -> auth_user(id) | 15 | 16

TABLE: account_emailconfirmation
  [Column | Type | Constraints | Sample1 | Sample2]
  id | INTEGER | PRIMARY KEY, NOT NULL | - | -
  created | TIMESTAMP | NOT NULL | - | -
  sent | TIMESTAMP | - | - | -
  key | VARCHAR(64) | NOT NULL, UNIQUE | - | -
  email_address_id | INTEGER | NOT NULL, FOREIGN KEY -> account_emailaddress(id) | - | -

TABLE: accounts_clientgroup
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | 1 | 2
  created_at | TIMESTAMP | NOT NULL | 2025-10-13 12:27:32.693411+00:00 | 2025-10-24 00:50:36.832193+00:00
  updated_at | TIMESTAMP | NOT NULL | 2025-10-13 12:27:32.693430+00:00 | 2025-10-24 00:50:36.842953+00:00
  name | VARCHAR(100) | NOT NULL | "All" | "Test Audit Group"
  code | VARCHAR(50) | NOT NULL, UNIQUE | "all" | "TEST_AUDIT_001"
  description | TEXT | NOT NULL | "Updated test group description" | "Default group for all users"
  is_default | BOOLEAN | NOT NULL | False | True
  active | BOOLEAN | NOT NULL | False | True
  created_by_id | INTEGER | FOREIGN KEY -> auth_user(id) | - | -

TABLE: accounts_loginlog
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | 1 | 3
  created_at | TIMESTAMP | NOT NULL | 2025-10-28 22:11:18.842675+00:00 | 2025-10-28 22:11:18.622334+00:00
  updated_at | TIMESTAMP | NOT NULL | 2025-10-28 22:11:18.685579+00:00 | 2025-10-28 22:11:18.818731+00:00
  ip_address | INET | - | "203.0.113.45" | "192.168.1.100"
  user_agent | TEXT | NOT NULL | "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" | "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
  login_time | TIMESTAMP | NOT NULL | 2025-10-28 16:36:18.621878+00:00 | 2025-10-28 18:46:18.621878+00:00
  success | BOOLEAN | NOT NULL | False | True
  failure_reason | VARCHAR(255) | NOT NULL | "Staff users must authenticate via SSO" | ""
  user_id | INTEGER | NOT NULL, FOREIGN KEY -> auth_user(id) | 9 | -

TABLE: accounts_userclientrole
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | 9 | 11
  created_at | TIMESTAMP | NOT NULL | 2025-10-24 00:34:57.080727+00:00 | 2025-10-31 14:42:09.165194+00:00
  updated_at | TIMESTAMP | NOT NULL | 2025-10-24 00:34:57.080738+00:00 | 2025-10-24 00:06:58.550329+00:00
  assigned_at | TIMESTAMP | NOT NULL | 2025-10-31 14:44:13.011728+00:00 | 2025-10-31 14:43:27.841346+00:00
  assigned_by_id | INTEGER | FOREIGN KEY -> auth_user(id) | 20 | -
  client_group_id | BIGINT | NOT NULL, UNIQUE, FOREIGN KEY -> accounts_clientgroup(id) | 1 | -
  role_id | BIGINT | NOT NULL, FOREIGN KEY -> accounts_userrole(id) | 1 | 3
  user_id | INTEGER | NOT NULL, UNIQUE, FOREIGN KEY -> auth_user(id) | 9 | 11

TABLE: accounts_userrole
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | 1 | 2
  role | VARCHAR(20) | NOT NULL, UNIQUE | "admin" | "external"
  description | TEXT | NOT NULL | "Superuser - Platform owner" | "External - Limited access for external users"

TABLE: accounts_delegatedpermission
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | - | -
  created_at | TIMESTAMP | NOT NULL | - | -
  updated_at | TIMESTAMP | NOT NULL | - | -
  can_delegate | BOOLEAN | NOT NULL | - | -
  expires_at | TIMESTAMP | - | - | -
  active | BOOLEAN | NOT NULL | - | -
  client_group_id | BIGINT | NOT NULL, UNIQUE, FOREIGN KEY -> accounts_clientgroup(id) | - | -
  delegator_id | INTEGER | NOT NULL, UNIQUE, FOREIGN KEY -> auth_user(id) | - | -
  granted_by_id | INTEGER | FOREIGN KEY -> auth_user(id) | - | -
  max_assignable_role_id | BIGINT | NOT NULL, FOREIGN KEY -> accounts_userrole(id) | - | -

TABLE: accounts_userprofile
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | 17 | 20
  created_at | TIMESTAMP | NOT NULL | 2025-10-31 14:42:09.145771+00:00 | 2025-11-03 19:54:18.141049+00:00
  updated_at | TIMESTAMP | NOT NULL | 2025-10-24 00:34:57.082934+00:00 | 2025-10-24 00:06:58.555759+00:00
  phone | VARCHAR(20) | NOT NULL | "" | -
  department | VARCHAR(100) | NOT NULL | "" | -
  title | VARCHAR(100) | NOT NULL | "" | -
  profile_picture | VARCHAR(100) | - | "" | -
  mfa_enabled | BOOLEAN | NOT NULL | False | -
  last_login_ip | INET | - | - | -
  login_count | INTEGER | NOT NULL | 0 | -
  user_id | INTEGER | NOT NULL, UNIQUE, FOREIGN KEY -> auth_user(id) | 17 | 20
  is_external_user | BOOLEAN | NOT NULL | False | True

TABLE: django_admin_log
  [Column | Type | Constraints | Sample1 | Sample2]
  id | INTEGER | PRIMARY KEY, NOT NULL | 8 | -
  action_time | TIMESTAMP | NOT NULL | 2025-11-21 02:07:30.935568+00:00 | -
  object_id | TEXT | - | "5" | -
  object_repr | VARCHAR(200) | NOT NULL | "Bharathku Tamilarasu - Bharathkumar" | -
  action_flag | SMALLINT | NOT NULL | 2 | -
  change_message | TEXT | NOT NULL | "[{"changed": {"fields": ["First name"]}}]" | -
  content_type_id | INTEGER | FOREIGN KEY -> django_content_type(id) | 64 | -
  user_id | INTEGER | NOT NULL, FOREIGN KEY -> auth_user(id) | 20 | -

TABLE: ai_models_modeldefaultparameters
  [Column | Type | Constraints | Sample1 | Sample2]
  sort_order | INTEGER | - | - | -
  active | BOOLEAN | NOT NULL | True | -
  created_at | TIMESTAMP | NOT NULL | 2025-11-04 16:31:51.752889+00:00 | -
  updated_at | TIMESTAMP | NOT NULL | 2025-11-04 16:31:51.760270+00:00 | -
  id | INTEGER | PRIMARY KEY, NOT NULL | 1 | -
  temperature | DOUBLE PRECISION | NOT NULL | 0.7 | -
  max_tokens | INTEGER | NOT NULL | 2000 | -
  top_p | DOUBLE PRECISION | NOT NULL | 1.0 | -
  frequency_penalty | DOUBLE PRECISION | NOT NULL | 0.0 | -
  presence_penalty | DOUBLE PRECISION | NOT NULL | 0.0 | -
  stream | BOOLEAN | NOT NULL | True | -

TABLE: ai_models_promptrecipe
  [Column | Type | Constraints | Sample1 | Sample2]
  sort_order | INTEGER | - | - | -
  active | BOOLEAN | NOT NULL | True | -
  created_at | TIMESTAMP | NOT NULL | 2025-11-04 16:31:53.014776+00:00 | 2025-11-04 16:31:51.932999+00:00
  updated_at | TIMESTAMP | NOT NULL | 2025-11-04 16:31:53.014786+00:00 | 2025-11-04 16:31:51.933010+00:00
  id | INTEGER | PRIMARY KEY, NOT NULL | 1 | 2
  name | VARCHAR(200) | NOT NULL, UNIQUE | "Chat Only" | "Code Review Workflow"
  description | TEXT | NOT NULL | "Simple chat interaction without additional processing" | "Complete analysis workflow with extraction, analysis, and generation"
  recipe_header | TEXT | NOT NULL | "Review the provided code with the following steps:" | ""
  add_header_newline | BOOLEAN | NOT NULL | False | True
  recipe_footer | TEXT | NOT NULL | "Focus on the most important points and be concise." | "Ensure all suggestions follow best practices and include examples."
  add_footer_newline | BOOLEAN | NOT NULL | False | True
  recipe_content | TEXT | NOT NULL | "Provide a comprehensive summary of the following document:

{document}

Include:
1. Main topics covered
2. Key findings or conclusions
3. Important details
4. Action items (if any)

Extract the following information from the provided document:
- {fie..." | "Please perform a comprehensive analysis of the following content:

---

## Data Extraction
Extract the following information from the provided document:
- {fields}

Return the extracted data in JSON format.

---

## Document Summary
Provide a compreh..."
  estimated_tokens | INTEGER | NOT NULL | 71 | 118
  is_default | BOOLEAN | NOT NULL | False | True
  separator | VARCHAR(100) | NOT NULL | "

### Next Step ###

" | "

---

"
  include_prompt_names | BOOLEAN | NOT NULL | False | True

TABLE: ai_models_promptordering
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | 1 | 2
  order | INTEGER | NOT NULL | 3 | 2
  prompt_id | INTEGER | NOT NULL, UNIQUE, FOREIGN KEY -> ai_models_prompt(id) | 1 | 2
  recipe_id | INTEGER | NOT NULL, UNIQUE, FOREIGN KEY -> ai_models_promptrecipe(id) | 1 | 2

TABLE: ai_models_modelparameterset
  [Column | Type | Constraints | Sample1 | Sample2]
  sort_order | INTEGER | - | - | -
  active | BOOLEAN | NOT NULL | True | -
  created_at | TIMESTAMP | NOT NULL | 2025-11-04 16:31:51.784099+00:00 | 2025-11-04 16:31:51.774726+00:00
  updated_at | TIMESTAMP | NOT NULL | 2025-11-04 16:31:51.818191+00:00 | 2025-11-04 16:31:51.810479+00:00
  id | INTEGER | PRIMARY KEY, NOT NULL | 1 | 2
  name | VARCHAR(100) | NOT NULL, UNIQUE | "Analytical" | "Balanced"
  description | TEXT | NOT NULL | "Optimized for generating code with consistent formatting" | "Consistent, reproducible outputs with no randomness"
  parameters | JSONB | NOT NULL | {"top_p": 0.95, "max_tokens": 4000, "temperature": 0.7, "presence_penalty": 0.1, "frequency_penalty": 0.1} | {"top_p": 1.0, "max_tokens": 2000, "temperature": 0, "presence_penalty": 0, "frequency_penalty": 0}
  is_default | BOOLEAN | NOT NULL | False | True
  parent_id | INTEGER | FOREIGN KEY -> ai_models_modelparameterset(id) | 1 | -

TABLE: ai_models_aimodel
  [Column | Type | Constraints | Sample1 | Sample2]
  sort_order | INTEGER | - | - | -
  active | BOOLEAN | NOT NULL | True | -
  created_at | TIMESTAMP | NOT NULL | 2025-11-04 16:31:51.741946+00:00 | -
  updated_at | TIMESTAMP | NOT NULL | 2025-11-04 16:31:51.741963+00:00 | -
  id | INTEGER | PRIMARY KEY, NOT NULL | 1 | -
  model_id | VARCHAR(100) | NOT NULL, UNIQUE | "gpt-4.1-mini" | -
  display_name | VARCHAR(200) | NOT NULL | "GPT-4.1 Mini" | -
  is_multimodal | BOOLEAN | NOT NULL | True | -
  is_embedding_model | BOOLEAN | NOT NULL | False | -
  deployment_name | VARCHAR(100) | - | "gpt-4.1-mini" | -
  max_tokens | INTEGER | NOT NULL | 8192 | -
  supports_functions | BOOLEAN | NOT NULL | True | -
  supports_streaming | BOOLEAN | NOT NULL | True | -
  is_default | BOOLEAN | NOT NULL | True | -
  default_parameter_set_id | INTEGER | FOREIGN KEY -> ai_models_modelparameterset(id) | - | -
  endpoint_id | INTEGER | NOT NULL, FOREIGN KEY -> ai_models_unifiedendpoint(id) | 1 | -

TABLE: ai_models_unifiedendpoint
  [Column | Type | Constraints | Sample1 | Sample2]
  sort_order | INTEGER | - | - | -
  active | BOOLEAN | NOT NULL | True | -
  created_at | TIMESTAMP | NOT NULL | 2025-11-04 16:31:51.726468+00:00 | -
  updated_at | TIMESTAMP | NOT NULL | 2025-11-04 16:31:51.726486+00:00 | -
  id | INTEGER | PRIMARY KEY, NOT NULL | 1 | -
  name | VARCHAR(150) | NOT NULL, UNIQUE | "Azure OpenAI Production" | -
  provider | VARCHAR(20) | NOT NULL | "azure" | -
  base_url | VARCHAR(512) | NOT NULL | "https://ai-svcs-w-openai.openai.azure.com" | -
  resource_name | VARCHAR(100) | - | "ai-svcs-w-openai" | -
  api_version | VARCHAR(20) | - | "2025-01-01-preview" | -
  organization_id | VARCHAR(100) | - | "" | -
  api_secret_id | INTEGER | NOT NULL, FOREIGN KEY -> ai_models_apisecret(id) | 1 | -

TABLE: ai_models_prompt
  [Column | Type | Constraints | Sample1 | Sample2]
  sort_order | INTEGER | - | - | -
  active | BOOLEAN | NOT NULL | True | -
  created_at | TIMESTAMP | NOT NULL | 2025-11-04 16:31:51.872410+00:00 | 2025-11-04 16:31:51.922017+00:00
  updated_at | TIMESTAMP | NOT NULL | 2025-11-04 16:31:51.911439+00:00 | 2025-11-04 16:31:51.922028+00:00
  id | INTEGER | PRIMARY KEY, NOT NULL | 1 | 2
  name | VARCHAR(200) | NOT NULL, UNIQUE | "Code Review" | "Content Generation"
  prompt_type | VARCHAR(255) | NOT NULL | "CHAT" | "GENERATION"
  content | TEXT | NOT NULL | "Provide a comprehensive summary of the following document:

{document}

Include:
1. Main topics covered
2. Key findings or conclusions
3. Important details
4. Action items (if any)" | "Extract the following information from the provided document:
- {fields}

Return the extracted data in JSON format."
  version | VARCHAR(20) | NOT NULL, UNIQUE | "1.0" | -
  description | TEXT | NOT NULL | "Extract structured data from documents" | "Summarize documents with structured output"
  tags | JSONB | NOT NULL | ["general", "chat"] | ["extraction", "data", "json"]
  expected_output_format | VARCHAR(50) | NOT NULL | "markdown" | "json"
  usage_count | INTEGER | NOT NULL | 0 | -
  last_used_at | TIMESTAMP | - | - | -
  model_id | INTEGER | FOREIGN KEY -> ai_models_aimodel(id) | 1 | -

TABLE: ai_models_apisecret
  [Column | Type | Constraints | Sample1 | Sample2]
  sort_order | INTEGER | - | - | -
  active | BOOLEAN | NOT NULL | True | -
  created_at | TIMESTAMP | NOT NULL | 2025-11-04 16:31:51.694958+00:00 | -
  updated_at | TIMESTAMP | NOT NULL | 2025-11-04 16:31:51.694971+00:00 | -
  id | INTEGER | PRIMARY KEY, NOT NULL | 1 | -
  name | VARCHAR(150) | NOT NULL, UNIQUE | "Azure OpenAI Key" | -
  storage_location | VARCHAR(30) | NOT NULL | "DATABASE" | -
  secret_value | TEXT | - | "REDACTED" | -
  external_identifier | VARCHAR(512) | - | "" | -

TABLE: storage_storedfile
  [Column | Type | Constraints | Sample1 | Sample2]
  sort_order | INTEGER | - | - | -
  active | BOOLEAN | NOT NULL | True | -
  created_at | TIMESTAMP | NOT NULL | 2025-11-14 01:40:48.855584+00:00 | 2025-11-20 22:07:39.431096+00:00
  updated_at | TIMESTAMP | NOT NULL | 2025-11-20 22:07:39.431116+00:00 | 2025-11-14 01:40:48.855601+00:00
  id | INTEGER | PRIMARY KEY, NOT NULL | 2 | 3
  file_key | VARCHAR(500) | NOT NULL, UNIQUE | "azure://ai-toolkit-dev/uploads/user-20/2025/11/20251114-014048_95c3_DurgeshNandanBirmiwal3y_0m.pdf" | "test_resume_Bharathkumar Tamilarasu.pdf"
  original_filename | VARCHAR(255) | NOT NULL | "DurgeshNandanBirmiwal[3y_0m].pdf" | "Bharathkumar Tamilarasu.pdf"
  storage_backend | VARCHAR(20) | NOT NULL | "local" | "azure_blob"
  storage_path | VARCHAR(1000) | NOT NULL | "ai-toolkit-dev/uploads/user-20/2025/11/20251114-014048_95c3_DurgeshNandanBirmiwal3y_0m.pdf" | "/home/cmoore/programming/talent_ai/Bharathkumar Tamilarasu.pdf"
  container_name | VARCHAR(100) | NOT NULL | "ai-toolkit-dev" | ""
  file_size | BIGINT | NOT NULL | 125285 | 167608
  content_type | VARCHAR(100) | NOT NULL | "application/pdf" | -
  file_hash | VARCHAR(64) | NOT NULL | "" | "0b7bad5c852096f2560d81a7085a4eaa109b50546d1013144f491daf57d00afd"
  status | VARCHAR(20) | NOT NULL | "ready" | -
  uploaded_by_id | INTEGER | FOREIGN KEY -> auth_user(id) | 20 | -

TABLE: chat_conversation
  [Column | Type | Constraints | Sample1 | Sample2]
  sort_order | INTEGER | - | - | -
  active | BOOLEAN | NOT NULL | - | -
  created_at | TIMESTAMP | NOT NULL | - | -
  updated_at | TIMESTAMP | NOT NULL | - | -
  id | INTEGER | PRIMARY KEY, NOT NULL | - | -
  title | VARCHAR(255) | NOT NULL | - | -
  parameters | JSONB | NOT NULL | - | -
  ai_model_id | INTEGER | FOREIGN KEY -> ai_models_aimodel(id) | - | -
  user_id | INTEGER | NOT NULL, FOREIGN KEY -> auth_user(id) | - | -

TABLE: chat_message
  [Column | Type | Constraints | Sample1 | Sample2]
  sort_order | INTEGER | - | - | -
  active | BOOLEAN | NOT NULL | - | -
  created_at | TIMESTAMP | NOT NULL | - | -
  updated_at | TIMESTAMP | NOT NULL | - | -
  id | INTEGER | PRIMARY KEY, NOT NULL | - | -
  role | VARCHAR(20) | NOT NULL | - | -
  content | TEXT | NOT NULL | - | -
  attachments | JSONB | NOT NULL | - | -
  prompt_tokens | INTEGER | - | - | -
  completion_tokens | INTEGER | - | - | -
  processing_time_ms | INTEGER | - | - | -
  conversation_id | INTEGER | NOT NULL, FOREIGN KEY -> chat_conversation(id) | - | -

TABLE: conversion_conversionjob
  [Column | Type | Constraints | Sample1 | Sample2]
  sort_order | INTEGER | - | - | -
  active | BOOLEAN | NOT NULL | - | -
  created_at | TIMESTAMP | NOT NULL | - | -
  updated_at | TIMESTAMP | NOT NULL | - | -
  id | INTEGER | PRIMARY KEY, NOT NULL | - | -
  document_type | VARCHAR(10) | NOT NULL | - | -
  output_format | VARCHAR(10) | NOT NULL | - | -
  max_height | INTEGER | - | - | -
  image_quality | INTEGER | NOT NULL | - | -
  status | VARCHAR(20) | NOT NULL | - | -
  error_message | TEXT | NOT NULL | - | -
  page_count | INTEGER | NOT NULL | - | -
  total_size_mb | DOUBLE PRECISION | NOT NULL | - | -
  started_at | TIMESTAMP | - | - | -
  completed_at | TIMESTAMP | - | - | -
  source_file_id | INTEGER | NOT NULL, FOREIGN KEY -> storage_storedfile(id) | - | -

TABLE: conversion_convertedimage
  [Column | Type | Constraints | Sample1 | Sample2]
  sort_order | INTEGER | - | - | -
  active | BOOLEAN | NOT NULL | - | -
  created_at | TIMESTAMP | NOT NULL | - | -
  updated_at | TIMESTAMP | NOT NULL | - | -
  id | INTEGER | PRIMARY KEY, NOT NULL | - | -
  page_number | INTEGER | NOT NULL, UNIQUE | - | -
  width | INTEGER | NOT NULL | - | -
  height | INTEGER | NOT NULL | - | -
  size_bytes | BIGINT | NOT NULL | - | -
  base64_data_url | TEXT | NOT NULL | - | -
  conversion_job_id | INTEGER | NOT NULL, UNIQUE, FOREIGN KEY -> conversion_conversionjob(id) | - | -
  image_file_id | INTEGER | NOT NULL, FOREIGN KEY -> storage_storedfile(id) | - | -

TABLE: extraction_document
  [Column | Type | Constraints | Sample1 | Sample2]
  sort_order | INTEGER | - | - | -
  active | BOOLEAN | NOT NULL | True | -
  created_at | TIMESTAMP | NOT NULL | 2025-11-14 01:40:48.911977+00:00 | 2025-10-24 00:50:36.809029+00:00
  updated_at | TIMESTAMP | NOT NULL | 2025-10-24 00:50:36.821348+00:00 | 2025-11-14 01:40:49.795977+00:00
  id | INTEGER | PRIMARY KEY, NOT NULL | 1 | 2
  document_id | UUID | NOT NULL, UNIQUE | 76dff95c-11f3-4fae-bd03-2ea8cdf1c85d | 8f9606cd-cd74-4a4e-a4cd-7c15a26d2e0a
  original_filename | VARCHAR(255) | NOT NULL | "DurgeshNandanBirmiwal[3y_0m].pdf" | "test_audit_resume.pdf"
  file_type | VARCHAR(10) | NOT NULL | "pdf" | -
  file_size | INTEGER | NOT NULL | 2048 | 167608
  document_type | VARCHAR(50) | - | "text_pdf" | -
  page_count | INTEGER | - | 1 | 5
  status | VARCHAR(20) | NOT NULL | "completed" | -
  uploaded_at | TIMESTAMP | NOT NULL | 2025-10-24 00:50:36.809081+00:00 | 2025-11-14 01:40:48.912033+00:00
  processed_at | TIMESTAMP | - | 2025-11-14 01:40:49.780542+00:00 | -
  stored_file_id | INTEGER | FOREIGN KEY -> storage_storedfile(id) | 2 | -
  uploaded_by_id | INTEGER | FOREIGN KEY -> auth_user(id) | 20 | -

TABLE: extraction_extractionjob
  [Column | Type | Constraints | Sample1 | Sample2]
  sort_order | INTEGER | - | - | -
  active | BOOLEAN | NOT NULL | True | -
  created_at | TIMESTAMP | NOT NULL | 2025-11-14 01:40:48.948022+00:00 | -
  updated_at | TIMESTAMP | NOT NULL | 2025-11-14 01:40:49.816205+00:00 | -
  job_id | UUID | PRIMARY KEY, NOT NULL | 71e413e7-b5ea-4172-bb4c-3da01029094b | -
  status | VARCHAR(20) | NOT NULL | "completed" | -
  started_at | TIMESTAMP | NOT NULL | 2025-11-14 01:40:48.948067+00:00 | -
  completed_at | TIMESTAMP | - | 2025-11-14 01:40:49.750515+00:00 | -
  pipeline_used | VARCHAR(100) | - | "PdfDocxPipeline" | -
  extraction_type | VARCHAR(50) | - | "text_pdf" | -
  processing_time | DOUBLE PRECISION | - | 0.724794864654541 | -
  retry_count | INTEGER | NOT NULL | 0 | -
  error_message | TEXT | NOT NULL | "" | -
  error_details | JSONB | - | - | -
  content_extracted | BOOLEAN | NOT NULL | True | -
  text_length | INTEGER | - | 3618 | -
  image_count | INTEGER | - | 0 | -
  table_count | INTEGER | - | 0 | -
  document_id | INTEGER | NOT NULL, FOREIGN KEY -> extraction_document(id) | 2 | -
  initiated_by_id | INTEGER | FOREIGN KEY -> auth_user(id) | 20 | -

TABLE: extraction_extractedcontent
  [Column | Type | Constraints | Sample1 | Sample2]
  sort_order | INTEGER | - | - | -
  active | BOOLEAN | NOT NULL | True | -
  created_at | TIMESTAMP | NOT NULL | 2025-11-14 01:40:49.751297+00:00 | 2025-11-14 01:40:49.767661+00:00
  updated_at | TIMESTAMP | NOT NULL | 2025-11-14 01:40:49.751312+00:00 | 2025-11-14 01:40:49.767678+00:00
  id | INTEGER | PRIMARY KEY, NOT NULL | 1 | 2
  content_type | VARCHAR(20) | NOT NULL | "text" | "xhtml"
  content | JSONB | NOT NULL | {"text": "\n============================================================\nPage 1\n============================================================\nDurgesh Nandan Birmiwal\nEmail: durgeshnandanbirmiwal@gmail.com\nPortfolio: durgesh-nandan-birmiwal.vercel... | {"xhtml": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\"\n    \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">\n<html xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n    <meta http-equiv...
  order | INTEGER | NOT NULL | 0 | 1
  page_number | INTEGER | - | - | -
  confidence_score | DOUBLE PRECISION | - | - | -
  extraction_method | VARCHAR(100) | - | "multi_format_process" | "PyMuPDF"
  document_id | INTEGER | NOT NULL, FOREIGN KEY -> extraction_document(id) | 2 | -
  job_id | UUID | NOT NULL, FOREIGN KEY -> extraction_extractionjob(job_id) | 71e413e7-b5ea-4172-bb4c-3da01029094b | -

TABLE: mcq_test_testattempt
  [Column | Type | Constraints | Sample1 | Sample2]
  id | INTEGER | PRIMARY KEY, NOT NULL | - | -
  started_at | TIMESTAMP | - | - | -
  status | VARCHAR(20) | NOT NULL | - | -
  submitted_at | TIMESTAMP | - | - | -
  created_at | TIMESTAMP | NOT NULL | - | -
  updated_at | TIMESTAMP | NOT NULL | - | -
  session_data | JSONB | NOT NULL | - | -
  performance_data | JSONB | NOT NULL | - | -
  test_id | BIGINT | NOT NULL, FOREIGN KEY -> mcq_test_testconfiguration(id) | - | -

TABLE: mcq_test_questiontracking
  [Column | Type | Constraints | Sample1 | Sample2]
  id | INTEGER | PRIMARY KEY, NOT NULL | - | -
  question_id | INTEGER | NOT NULL, UNIQUE | - | -
  question_version | INTEGER | NOT NULL | - | -
  created_at | TIMESTAMP | NOT NULL | - | -
  updated_at | TIMESTAMP | NOT NULL | - | -
  randomized_option_order | JSONB | NOT NULL | - | -
  visits | JSONB | NOT NULL | - | -
  final_selections | JSONB | NOT NULL | - | -
  selection_history | JSONB | NOT NULL | - | -
  total_time_spent_seconds | INTEGER | NOT NULL | - | -
  focus_lost_count | INTEGER | NOT NULL | - | -
  copy_paste_attempts | INTEGER | NOT NULL | - | -
  attempt_id | INTEGER | NOT NULL, UNIQUE, FOREIGN KEY -> mcq_test_testattempt(id) | - | -

TABLE: mcq_test_testable_skills
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | - | -
  normalized_form | VARCHAR(100) | NOT NULL, UNIQUE | - | -
  created_at | TIMESTAMP | NOT NULL | - | -
  updated_at | TIMESTAMP | NOT NULL | - | -

TABLE: mcq_test_question
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | - | -
  question_id | INTEGER | NOT NULL, UNIQUE | - | -
  version | INTEGER | NOT NULL, UNIQUE | - | -
  question_text | TEXT | NOT NULL | - | -
  question_type | VARCHAR(20) | NOT NULL | - | -
  max_points | INTEGER | NOT NULL | - | -
  max_selections | INTEGER | NOT NULL | - | -
  randomize_options | BOOLEAN | NOT NULL | - | -
  difficulty | VARCHAR(20) | NOT NULL | - | -
  tags | JSONB | NOT NULL | - | -
  author_email | VARCHAR(254) | NOT NULL | - | -
  is_active | BOOLEAN | NOT NULL | - | -
  is_draft | BOOLEAN | NOT NULL | - | -
  created_at | TIMESTAMP | NOT NULL | - | -
  updated_at | TIMESTAMP | NOT NULL | - | -
  options | JSONB | NOT NULL | - | -
  metadata | JSONB | NOT NULL | - | -
  testable_skill_id | BIGINT | FOREIGN KEY -> mcq_test_testable_skills(id) | - | -

TABLE: mcq_test_testconfiguration
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | - | -
  title | VARCHAR(255) | NOT NULL, UNIQUE | - | -
  description | TEXT | NOT NULL | - | -
  test_type | VARCHAR(20) | NOT NULL | - | -
  time_limit_minutes | INTEGER | NOT NULL | - | -
  is_active | BOOLEAN | NOT NULL | - | -
  randomize_questions | BOOLEAN | NOT NULL | - | -
  questions | JSONB | NOT NULL | - | -
  navigation_rules | JSONB | NOT NULL | - | -
  security_settings | JSONB | NOT NULL | - | -
  created_at | TIMESTAMP | NOT NULL | - | -
  updated_at | TIMESTAMP | NOT NULL | - | -

TABLE: mcq_test_candidateresponse
  [Column | Type | Constraints | Sample1 | Sample2]
  id | INTEGER | PRIMARY KEY, NOT NULL | - | -
  order_id | INTEGER | NOT NULL, UNIQUE | - | -
  question_id | INTEGER | NOT NULL, UNIQUE | - | -
  question_version | INTEGER | NOT NULL | - | -
  selected_options | JSONB | NOT NULL | - | -
  status | VARCHAR(20) | NOT NULL | - | -
  question_score | DOUBLE PRECISION | NOT NULL | - | -
  generated_at | TIMESTAMP | NOT NULL | - | -
  score_breakdown | JSONB | NOT NULL | - | -
  weight_info | JSONB | NOT NULL | - | -
  timing_stats | JSONB | NOT NULL | - | -
  attempt_id | INTEGER | NOT NULL, UNIQUE, FOREIGN KEY -> mcq_test_testattempt(id) | - | -
  time_allocated_seconds | INTEGER | - | - | -

TABLE: django_session
  [Column | Type | Constraints | Sample1 | Sample2]
  session_key | VARCHAR(40) | PRIMARY KEY, NOT NULL | "ycrntuz6yymawy8l1v5u605s191rbrg0" | "2jmpq41neegv7hg5yww7yewtza6nfsl6"
  session_data | TEXT | NOT NULL | ".eJyt0VtPwjAYxvHv0us5el7LHRo5iog4gxhCmq7Awo5dN42E7-7AjzCvn7z55Z_3DKpcxypRWud15naVU85UoH8GbhIN7sd2VfDZ5qCKZ9D_PIPC5tpU7Q6S_BBnwAORcgr0szpJPFCctNnpPDK7xth4Hxv7t1w8FHAoBWcM-YgQKtnWA2L4NFXvddFY8VZG8OE_gEAQHwkiGMKt4Mppka4awtZ5lqvwHxIkE4j6mEAMb4IO0585w68JS..." | ".eJxVjEEKgzAQRe8ya1MMmcSMVykiaYwYqE4xYzfi3auULrr7fN57OxSOOTxDjLwt0hcJkgq0-1HB7wubTGmRHINkXvo5ycTDydx3-G5o_ytwugKtbpw2WDvSN0OGnLUVvFZ-5yGtpzLnuHLh8cK3fEVqYxI9klaEtVFoNSk_oleuQaQhorce4eiOD6NOOkc:1vCPAp:SH-K3JNaBTVl8ds7yjBvp1s8fRhLQ--syih2O3KtUIA"
  expire_date | TIMESTAMP | NOT NULL | 2025-11-06 13:57:29.808744+00:00 | 2025-11-18 15:25:05.475105+00:00

TABLE: django_site
  [Column | Type | Constraints | Sample1 | Sample2]
  id | INTEGER | PRIMARY KEY, NOT NULL | 1 | -
  domain | VARCHAR(100) | NOT NULL, UNIQUE | "example.com" | -
  name | VARCHAR(50) | NOT NULL | "example.com" | -

TABLE: skill_ontology_relationship
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | - | -
  sort_order | INTEGER | - | - | -
  active | BOOLEAN | NOT NULL | - | -
  created_at | TIMESTAMP | NOT NULL | - | -
  updated_at | TIMESTAMP | NOT NULL | - | -
  relationship_score | INTEGER | NOT NULL | - | -
  reasoning | TEXT | NOT NULL | - | -
  child_id | BIGINT | NOT NULL, UNIQUE, FOREIGN KEY -> skill_ontology_normalizedform(id) | - | -
  parent_id | BIGINT | NOT NULL, UNIQUE, FOREIGN KEY -> skill_ontology_normalizedform(id) | - | -

TABLE: skill_ontology_skillclassificationissue
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | - | -
  sort_order | INTEGER | - | - | -
  active | BOOLEAN | NOT NULL | - | -
  created_at | TIMESTAMP | NOT NULL | - | -
  updated_at | TIMESTAMP | NOT NULL | - | -
  original_word | VARCHAR(255) | NOT NULL | - | -
  issue_type | VARCHAR(20) | NOT NULL | - | -
  issue_description | TEXT | NOT NULL | - | -
  suggested_alternative | VARCHAR(255) | NOT NULL | - | -
  explanation | TEXT | NOT NULL | - | -

TABLE: skill_ontology_word
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | - | -
  sort_order | INTEGER | - | - | -
  active | BOOLEAN | NOT NULL | - | -
  created_at | TIMESTAMP | NOT NULL | - | -
  updated_at | TIMESTAMP | NOT NULL | - | -
  original_word | VARCHAR(255) | NOT NULL, UNIQUE | - | -
  confidence_score | INTEGER | NOT NULL | - | -
  explanation | TEXT | NOT NULL | - | -
  normalized_form_id | BIGINT | NOT NULL, FOREIGN KEY -> skill_ontology_normalizedform(id) | - | -

TABLE: skill_ontology_normalizedform
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | - | -
  sort_order | INTEGER | - | - | -
  active | BOOLEAN | NOT NULL | - | -
  created_at | TIMESTAMP | NOT NULL | - | -
  updated_at | TIMESTAMP | NOT NULL | - | -
  normalized_form | VARCHAR(255) | NOT NULL, UNIQUE | - | -
  description | TEXT | NOT NULL | - | -
  category | VARCHAR(20) | NOT NULL | - | -
  embedding_v2 | NULL | - | - | -

TABLE: skill_ontology_skillclassificationrequest
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | - | -
  sort_order | INTEGER | - | - | -
  active | BOOLEAN | NOT NULL | - | -
  created_at | TIMESTAMP | NOT NULL | - | -
  updated_at | TIMESTAMP | NOT NULL | - | -
  original_word | VARCHAR(255) | NOT NULL, UNIQUE | - | -
  status | VARCHAR(20) | NOT NULL | - | -
  classification_type | VARCHAR(25) | - | - | -
  llm_response | JSONB | - | - | -
  processing_time_ms | INTEGER | - | - | -
  error_message | TEXT | NOT NULL | - | -
  search_parameters | JSONB | - | - | -

TABLE: skill_ontology_skillclassificationrequest_search_candidates6fbc
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | - | -
  skillclassificationrequest_id | BIGINT | NOT NULL, UNIQUE, FOREIGN KEY -> skill_ontology_skillclassificationrequest(id) | - | -
  normalizedform_id | BIGINT | NOT NULL, UNIQUE, FOREIGN KEY -> skill_ontology_normalizedform(id) | - | -

TABLE: socialaccount_socialaccount
  [Column | Type | Constraints | Sample1 | Sample2]
  id | INTEGER | PRIMARY KEY, NOT NULL | 2 | -
  provider | VARCHAR(200) | NOT NULL, UNIQUE | "microsoft" | -
  uid | VARCHAR(191) | NOT NULL, UNIQUE | "033e9be1-9403-4519-8f48-67449dc48584" | -
  last_login | TIMESTAMP | NOT NULL | 2025-11-21 14:35:48.520049+00:00 | -
  date_joined | TIMESTAMP | NOT NULL | 2025-11-03 20:02:50.821280+00:00 | -
  extra_data | JSONB | NOT NULL | {"id": "033e9be1-9403-4519-8f48-67449dc48584", "mail": "cmoore@bayone.com", "surname": "Moore", "jobTitle": "Director - AI", "givenName": "Colin", "companyName": null, "displayName": "Colin Moore", "mobilePhone": "1-9258041863", "mailNickname": "cmoo... | -
  user_id | INTEGER | NOT NULL, FOREIGN KEY -> auth_user(id) | 20 | -

TABLE: socialaccount_socialapp
  [Column | Type | Constraints | Sample1 | Sample2]
  id | INTEGER | PRIMARY KEY, NOT NULL | - | -
  provider | VARCHAR(30) | NOT NULL | - | -
  name | VARCHAR(40) | NOT NULL | - | -
  client_id | VARCHAR(191) | NOT NULL | - | -
  secret | VARCHAR(191) | NOT NULL | - | -
  key | VARCHAR(191) | NOT NULL | - | -
  provider_id | VARCHAR(200) | NOT NULL | - | -
  settings | JSONB | NOT NULL | - | -

TABLE: socialaccount_socialapp_sites
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | - | -
  socialapp_id | INTEGER | NOT NULL, UNIQUE, FOREIGN KEY -> socialaccount_socialapp(id) | - | -
  site_id | INTEGER | NOT NULL, UNIQUE, FOREIGN KEY -> django_site(id) | - | -

TABLE: socialaccount_socialtoken
  [Column | Type | Constraints | Sample1 | Sample2]
  id | INTEGER | PRIMARY KEY, NOT NULL | 2 | -
  token | TEXT | NOT NULL | "eyJ0eXAiOiJKV1QiLCJub25jZSI6IkdvaDhFdWp5ZmFFTEY1aW1naHA0ckYxR3dlU2c2WEx4eHNyLWRrWGgwOUkiLCJhbGciOiJSUzI1NiIsIng1dCI6InJ0c0ZULWItN0x1WTdEVlllU05LY0lKN1ZuYyIsImtpZCI6InJ0c0ZULWItN0x1WTdEVlllU05LY0lKN1ZuYyJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wM..." | -
  token_secret | TEXT | NOT NULL | "" | -
  expires_at | TIMESTAMP | - | 2025-11-21 15:39:02.835262+00:00 | -
  account_id | INTEGER | NOT NULL, UNIQUE, FOREIGN KEY -> socialaccount_socialaccount(id) | 2 | -
  app_id | INTEGER | UNIQUE, FOREIGN KEY -> socialaccount_socialapp(id) | - | -

TABLE: authtoken_token
  [Column | Type | Constraints | Sample1 | Sample2]
  key | VARCHAR(40) | PRIMARY KEY, NOT NULL | - | -
  created | TIMESTAMP | NOT NULL | - | -
  user_id | INTEGER | NOT NULL, UNIQUE, FOREIGN KEY -> auth_user(id) | - | -

TABLE: file_audit_logs
  [Column | Type | Constraints | Sample1 | Sample2]
  sort_order | INTEGER | - | - | -
  active | BOOLEAN | NOT NULL | True | -
  created_at | TIMESTAMP | NOT NULL | 2025-11-14 01:40:48.884276+00:00 | -
  updated_at | TIMESTAMP | NOT NULL | 2025-11-14 01:40:48.884301+00:00 | -
  id | BIGINT | PRIMARY KEY, NOT NULL | 1 | -
  username | VARCHAR(150) | NOT NULL | "cmoore" | -
  file_key | VARCHAR(500) | NOT NULL | "azure://ai-toolkit-dev/uploads/user-20/2025/11/20251114-014048_95c3_DurgeshNandanBirmiwal3y_0m.pdf" | -
  original_filename | VARCHAR(255) | NOT NULL | "DurgeshNandanBirmiwal[3y_0m].pdf" | -
  action | VARCHAR(20) | NOT NULL | "created" | -
  ip_address | INET | - | - | -
  user_agent | VARCHAR(500) | NOT NULL | "" | -
  success | BOOLEAN | NOT NULL | True | -
  error_message | TEXT | NOT NULL | "" | -
  old_value | JSONB | - | - | -
  new_value | JSONB | - | - | -
  reason | TEXT | NOT NULL | "" | -
  file_size | BIGINT | - | 167608 | -
  storage_backend | VARCHAR(20) | NOT NULL | "azure_blob" | -
  stored_file_id | INTEGER | FOREIGN KEY -> storage_storedfile(id) | 2 | -
  user_id | INTEGER | FOREIGN KEY -> auth_user(id) | 20 | -

TABLE: debug_toolbar_historyentry
  [Column | Type | Constraints | Sample1 | Sample2]
  request_id | UUID | PRIMARY KEY, NOT NULL | - | -
  data | JSONB | NOT NULL | - | -
  created_at | TIMESTAMP | NOT NULL | - | -

TABLE: celery_task_status
  [Column | Type | Constraints | Sample1 | Sample2]
  task_id | UUID | PRIMARY KEY, NOT NULL | 4b74465e-1422-452f-b759-42afe5bf7fca | e414d2f7-d070-437e-a808-0398c512384f
  task_name | VARCHAR(255) | NOT NULL | "process_document" | -
  status | VARCHAR(20) | NOT NULL | "completed" | -
  progress | INTEGER | NOT NULL | 100 | -
  submitted_at | TIMESTAMP | NOT NULL | 2025-10-23 21:35:36.240110+00:00 | 2025-10-23 21:43:15.361663+00:00
  started_at | TIMESTAMP | - | 2025-10-23 21:35:36.248724+00:00 | 2025-10-23 21:43:15.366164+00:00
  completed_at | TIMESTAMP | - | 2025-10-23 21:43:15.370963+00:00 | 2025-10-23 21:35:36.254164+00:00
  result_key | VARCHAR(500) | - | "{'test': 'success'}" | -
  error_message | TEXT | - | - | -
  metadata | JSONB | NOT NULL | {"mock": true, "queue": "default", "priority": 5} | -
  submitted_by_id | INTEGER | FOREIGN KEY -> auth_user(id) | - | -

TABLE: audit_logs_soc2
  [Column | Type | Constraints | Sample1 | Sample2]
  id | UUID | PRIMARY KEY, NOT NULL | 008f5c02-77fb-4714-9685-644a92c8b023 | 01621b6a-efb9-41e9-a38b-75ca10151e68
  created_at | TIMESTAMP | NOT NULL | 2025-10-24 00:06:58.563507+00:00 | 2025-10-24 00:06:58.580631+00:00
  username | VARCHAR(150) | NOT NULL | "system" | "test_marker"
  action | VARCHAR(50) | NOT NULL | "logout" | "delete"
  model_name | VARCHAR(100) | NOT NULL | "" | "candidate"
  record_id | VARCHAR(255) | NOT NULL | "None" | "12"
  description | TEXT | NOT NULL | "Test record 0 created by example_audited_command" | "Created ClientGroup (ID: 2)"
  ip_address | INET | - | "10.0.0.254" | "192.168.1.100"
  user_agent | VARCHAR(500) | - | "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36" | ""
  request_path | VARCHAR(500) | - | "/email/compose/" | "/accounts/users/"
  changed_fields | JSONB | NOT NULL | ["document_type", "page_count", "status", "processed_at"] | []
  changes_detail | JSONB | NOT NULL | {"args": [], "status": "success", "command": "test_decorator", "options": {"no_color": false, "settings": null, "traceback": false, "verbosity": 1, "audit_user": null, "pythonpath": null, "force_color": false, "skip_checks": false, "test_failure": fa... | {"user_id": "20", "logout_method": "manual"}
  user_id | INTEGER | FOREIGN KEY -> auth_user(id) | 9 | 20

TABLE: resume_parsing_jobs
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | 1 | -
  sort_order | INTEGER | - | - | -
  active | BOOLEAN | NOT NULL | True | -
  created_at | TIMESTAMP | NOT NULL | 2025-11-14 01:40:49.836555+00:00 | -
  updated_at | TIMESTAMP | NOT NULL | 2025-11-14 01:40:52.771745+00:00 | -
  source_channel | VARCHAR(20) | NOT NULL | "upload" | -
  raw_text | TEXT | NOT NULL | "
============================================================
Page 1
============================================================
Durgesh Nandan Birmiwal
Email: durgeshnandanbirmiwal@gmail.com
Portfolio: durgesh-nandan-birmiwal.vercel.app
Mobile:
+91..." | -
  raw_format | VARCHAR(10) | NOT NULL | "txt" | -
  content_hash | VARCHAR(64) | NOT NULL, UNIQUE | "58231d709b4a0bfe11b0732e19f32ad3cba47e767ae46f2f7ec97cded67ac7b9" | -
  current_stage | VARCHAR(50) | NOT NULL | "stage2_skill_extraction" | -
  status | VARCHAR(20) | NOT NULL | "failed" | -
  retry_count | INTEGER | NOT NULL | 1 | -
  stage1_raw_structured | JSONB | - | - | -
  stage2_skills_extracted | JSONB | - | - | -
  stage3_normalized_education | JSONB | - | - | -
  stage_timings | JSONB | NOT NULL | {} | -
  total_processing_time | INTEGER | - | - | -
  error_stage | VARCHAR(50) | - | "stage2_skill_extraction" | -
  error_message | TEXT | - | "Processing error at stage stage2_skill_extraction: ['Stage 1 data not available for Stage 2 processing']" | -
  error_details | JSONB | - | {"stage": "stage2_skill_extraction", "timestamp": "2025-11-14T01:40:52.771107", "traceback": "Traceback (most recent call last):\n  File \"/home/cmoore/programming/talent_ai/recruitment/resume_parser/services/resume_worker.py\", line 215, in process_... | -
  issues | JSONB | NOT NULL | [] | -
  manual_review_notes | TEXT | NOT NULL | "" | -
  reviewed_at | TIMESTAMP | - | - | -
  parsed_resume_id | BIGINT | UNIQUE, FOREIGN KEY -> parsed_resumes(id) | - | -
  reviewed_by_id | INTEGER | FOREIGN KEY -> auth_user(id) | - | -
  uploaded_by_id | INTEGER | FOREIGN KEY -> auth_user(id) | 20 | -
  stage_metadata | JSONB | - | - | -
  extraction_job_id | UUID | - | 71e413e7-b5ea-4172-bb4c-3da01029094b | -

TABLE: educations
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | - | -
  sort_order | INTEGER | - | - | -
  active | BOOLEAN | NOT NULL | - | -
  created_at | TIMESTAMP | NOT NULL | - | -
  updated_at | TIMESTAMP | NOT NULL | - | -
  degree | VARCHAR(200) | - | - | -
  field | VARCHAR(200) | - | - | -
  institution | VARCHAR(200) | - | - | -
  location | VARCHAR(200) | - | - | -
  degree_normalized | VARCHAR(200) | - | - | -
  degree_level | VARCHAR(50) | - | - | -
  field_normalized | VARCHAR(200) | - | - | -
  institution_normalized | VARCHAR(200) | - | - | -
  start_date_raw | VARCHAR(50) | - | - | -
  end_date_raw | VARCHAR(50) | - | - | -
  start_date | DATE | - | - | -
  end_date | DATE | - | - | -
  gpa | VARCHAR(20) | - | - | -
  honors | VARCHAR(200) | - | - | -
  parsed_resume_id | BIGINT | NOT NULL, FOREIGN KEY -> parsed_resumes(id) | - | -

TABLE: certifications
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | - | -
  sort_order | INTEGER | - | - | -
  active | BOOLEAN | NOT NULL | - | -
  created_at | TIMESTAMP | NOT NULL | - | -
  updated_at | TIMESTAMP | NOT NULL | - | -
  name | VARCHAR(200) | NOT NULL | - | -
  issuing_organization | VARCHAR(200) | - | - | -
  name_normalized | VARCHAR(200) | - | - | -
  issuing_organization_normalized | VARCHAR(200) | - | - | -
  date_obtained | VARCHAR(50) | - | - | -
  expiration_date | VARCHAR(50) | - | - | -
  date_obtained_normalized | DATE | - | - | -
  expiration_date_normalized | DATE | - | - | -
  credential_id | VARCHAR(100) | - | - | -
  is_active | BOOLEAN | NOT NULL | - | -
  parsed_resume_id | BIGINT | NOT NULL, FOREIGN KEY -> parsed_resumes(id) | - | -

TABLE: locations
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | - | -
  sort_order | INTEGER | - | - | -
  active | BOOLEAN | NOT NULL | - | -
  created_at | TIMESTAMP | NOT NULL | - | -
  updated_at | TIMESTAMP | NOT NULL | - | -
  raw_address | TEXT | NOT NULL, UNIQUE | - | -
  city | VARCHAR(100) | - | - | -
  state | VARCHAR(100) | - | - | -
  country | VARCHAR(100) | - | - | -
  postal_code | VARCHAR(20) | - | - | -
  latitude | NUMERIC(9, 6) | - | - | -
  longitude | NUMERIC(9, 6) | - | - | -
  formatted_address | TEXT | - | - | -
  geocoded | BOOLEAN | NOT NULL | - | -
  geocoded_at | TIMESTAMP | - | - | -
  geocoding_confidence | VARCHAR(20) | - | - | -
  geocoding_source | VARCHAR(50) | NOT NULL | - | -

TABLE: parsed_resumes
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | - | -
  sort_order | INTEGER | - | - | -
  active | BOOLEAN | NOT NULL | - | -
  created_at | TIMESTAMP | NOT NULL | - | -
  updated_at | TIMESTAMP | NOT NULL | - | -
  first_name | VARCHAR(100) | - | - | -
  last_name | VARCHAR(100) | - | - | -
  emails | ARRAY | NOT NULL | - | -
  phones | ARRAY | NOT NULL | - | -
  address_raw | TEXT | - | - | -
  linkedin_url | VARCHAR(200) | - | - | -
  portfolio_url | VARCHAR(200) | - | - | -
  github_url | VARCHAR(200) | - | - | -
  other_urls | JSONB | NOT NULL | - | -
  current_job_title | VARCHAR(200) | - | - | -
  current_company | VARCHAR(200) | - | - | -
  highest_degree | VARCHAR(50) | - | - | -
  total_years_experience | NUMERIC(5, 2) | - | - | -
  location_id | BIGINT | FOREIGN KEY -> locations(id) | - | -
  candidate_id | BIGINT | FOREIGN KEY -> candidates_candidate(id) | - | -
  stored_file_id | INTEGER | FOREIGN KEY -> storage_storedfile(id) | - | -

TABLE: work_experiences
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | - | -
  sort_order | INTEGER | - | - | -
  active | BOOLEAN | NOT NULL | - | -
  created_at | TIMESTAMP | NOT NULL | - | -
  updated_at | TIMESTAMP | NOT NULL | - | -
  title | VARCHAR(200) | - | - | -
  company | VARCHAR(200) | - | - | -
  location_raw | VARCHAR(200) | - | - | -
  start_date_raw | VARCHAR(50) | - | - | -
  end_date_raw | VARCHAR(50) | - | - | -
  start_date | DATE | - | - | -
  end_date | DATE | - | - | -
  is_current | BOOLEAN | NOT NULL | - | -
  duration_months | INTEGER | - | - | -
  responsibilities | TEXT | - | - | -
  skills | JSONB | NOT NULL | - | -
  location_id | BIGINT | FOREIGN KEY -> locations(id) | - | -
  parsed_resume_id | BIGINT | NOT NULL, FOREIGN KEY -> parsed_resumes(id) | - | -
  duration_weight | NUMERIC(4, 3) | - | - | -
  recency_weight | NUMERIC(4, 3) | - | - | -
  weights_calculated_at | TIMESTAMP | - | - | -

TABLE: resume_skill_scores
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | - | -
  sort_order | INTEGER | - | - | -
  active | BOOLEAN | NOT NULL | - | -
  created_at | TIMESTAMP | NOT NULL | - | -
  updated_at | TIMESTAMP | NOT NULL | - | -
  final_score | NUMERIC(5, 3) | NOT NULL | - | -
  contributing_work_experiences | JSONB | NOT NULL | - | -
  total_months_experience | INTEGER | NOT NULL | - | -
  most_recent_usage | DATE | NOT NULL | - | -
  calculated_at | TIMESTAMP | NOT NULL | - | -
  normalized_form_id | BIGINT | NOT NULL, UNIQUE, FOREIGN KEY -> skill_ontology_normalizedform(id) | - | -
  parsed_resume_id | BIGINT | NOT NULL, UNIQUE, FOREIGN KEY -> parsed_resumes(id) | - | -

TABLE: resume_change_logs
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | - | -
  sort_order | INTEGER | - | - | -
  active | BOOLEAN | NOT NULL | - | -
  created_at | TIMESTAMP | NOT NULL | - | -
  updated_at | TIMESTAMP | NOT NULL | - | -
  section | VARCHAR(50) | NOT NULL | - | -
  field_name | VARCHAR(100) | NOT NULL | - | -
  old_value | TEXT | - | - | -
  new_value | TEXT | - | - | -
  change_reason | TEXT | NOT NULL | - | -
  change_type | VARCHAR(20) | NOT NULL | - | -
  changed_by_id | INTEGER | FOREIGN KEY -> auth_user(id) | - | -
  parsed_resume_id | BIGINT | NOT NULL, FOREIGN KEY -> parsed_resumes(id) | - | -

TABLE: job_roles_normalized_locations
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | - | -
  jobrole_id | BIGINT | NOT NULL, UNIQUE, FOREIGN KEY -> job_roles(id) | - | -
  location_id | BIGINT | NOT NULL, UNIQUE, FOREIGN KEY -> locations(id) | - | -

TABLE: job_skill_requirements
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | - | -
  sort_order | INTEGER | - | - | -
  active | BOOLEAN | NOT NULL | - | -
  created_at | TIMESTAMP | NOT NULL | - | -
  updated_at | TIMESTAMP | NOT NULL | - | -
  priority | VARCHAR(20) | NOT NULL | - | -
  proficiency | VARCHAR(20) | - | - | -
  proficiency_score | NUMERIC(4, 3) | NOT NULL | - | -
  relevance_score | NUMERIC(4, 3) | NOT NULL | - | -
  final_score | NUMERIC(4, 3) | NOT NULL | - | -
  proficiency_source | VARCHAR(20) | NOT NULL | - | -
  job_role_id | BIGINT | NOT NULL, UNIQUE, FOREIGN KEY -> job_roles(id) | - | -
  normalized_form_id | BIGINT | NOT NULL, UNIQUE, FOREIGN KEY -> skill_ontology_normalizedform(id) | - | -
  original_skill_names | JSONB | NOT NULL | - | -

TABLE: job_roles
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | - | -
  sort_order | INTEGER | - | - | -
  active | BOOLEAN | NOT NULL | - | -
  created_at | TIMESTAMP | NOT NULL | - | -
  updated_at | TIMESTAMP | NOT NULL | - | -
  job_title | VARCHAR(200) | NOT NULL | - | -
  company_name | VARCHAR(200) | - | - | -
  experience_level | VARCHAR(20) | - | - | -
  employment_types | ARRAY | NOT NULL | - | -
  locations | ARRAY | NOT NULL | - | -
  remote_policy | TEXT | - | - | -
  reports_to | VARCHAR(200) | - | - | -
  team_size | INTEGER | - | - | -
  team_description | TEXT | - | - | -
  start_date | VARCHAR(100) | - | - | -
  urgency | VARCHAR(20) | NOT NULL | - | -
  salary_min | INTEGER | - | - | -
  salary_max | INTEGER | - | - | -
  salary_currency | VARCHAR(10) | - | - | -
  salary_notes | TEXT | - | - | -
  equity_offered | BOOLEAN | - | - | -
  equity_details | TEXT | - | - | -
  other_compensation | TEXT | - | - | -
  benefits | ARRAY | NOT NULL | - | -
  minimum_degree_level | VARCHAR(100) | - | - | -
  field_of_study | VARCHAR(200) | - | - | -
  minimum_years_experience | INTEGER | - | - | -
  skills | JSONB | NOT NULL | - | -
  requirements | ARRAY | NOT NULL | - | -
  responsibilities | ARRAY | NOT NULL | - | -
  company_and_culture | TEXT | - | - | -
  additional_info | ARRAY | NOT NULL | - | -
  ideal_candidate_profile | TEXT | - | - | -
  potential_job_titles | ARRAY | NOT NULL | - | -
  experience_indicators | JSONB | NOT NULL | - | -
  red_flag_indicators | ARRAY | NOT NULL | - | -
  clarifying_questions | JSONB | NOT NULL | - | -
  screening_questions | JSONB | NOT NULL | - | -
  interview_questions | JSONB | NOT NULL | - | -
  number_of_positions | INTEGER | NOT NULL | - | -
  status | VARCHAR(20) | NOT NULL | - | -
  remote_policy_category | VARCHAR(20) | NOT NULL | - | -
  search_vector | TSVECTOR | - | - | -
  role_embedding | NULL | - | - | -

TABLE: job_parsing_jobs
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | - | -
  sort_order | INTEGER | - | - | -
  active | BOOLEAN | NOT NULL | - | -
  created_at | TIMESTAMP | NOT NULL | - | -
  updated_at | TIMESTAMP | NOT NULL | - | -
  source_channel | VARCHAR(20) | NOT NULL | - | -
  raw_text | TEXT | NOT NULL | - | -
  raw_format | VARCHAR(10) | NOT NULL | - | -
  content_hash | VARCHAR(64) | NOT NULL, UNIQUE | - | -
  extraction_job_id | UUID | - | - | -
  current_stage | VARCHAR(50) | NOT NULL | - | -
  status | VARCHAR(20) | NOT NULL | - | -
  retry_count | INTEGER | NOT NULL | - | -
  stage1_extracted | JSONB | - | - | -
  stage2_candidate_profile | JSONB | - | - | -
  stage3_clarifying_questions | JSONB | - | - | -
  stage4_phone_screening | JSONB | - | - | -
  stage5_interview_questions | JSONB | - | - | -
  stage_timings | JSONB | NOT NULL | - | -
  total_processing_time | INTEGER | - | - | -
  error_stage | VARCHAR(50) | - | - | -
  error_message | TEXT | - | - | -
  error_details | JSONB | - | - | -
  parsed_job_id | BIGINT | UNIQUE, FOREIGN KEY -> job_roles(id) | - | -
  uploaded_by_id | INTEGER | FOREIGN KEY -> auth_user(id) | - | -
  stage_metadata | JSONB | NOT NULL | - | -
  external_job_id | VARCHAR(255) | NOT NULL | - | -
  external_job_url | VARCHAR(200) | - | - | -
  external_metadata | JSONB | NOT NULL | - | -
  external_source | VARCHAR(100) | NOT NULL | - | -

TABLE: job_role_change_logs
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | - | -
  sort_order | INTEGER | - | - | -
  active | BOOLEAN | NOT NULL | - | -
  created_at | TIMESTAMP | NOT NULL | - | -
  updated_at | TIMESTAMP | NOT NULL | - | -
  section | VARCHAR(50) | NOT NULL | - | -
  field_name | VARCHAR(100) | NOT NULL | - | -
  old_value | TEXT | - | - | -
  new_value | TEXT | - | - | -
  change_reason | TEXT | NOT NULL | - | -
  change_type | VARCHAR(20) | NOT NULL | - | -
  changed_by_id | INTEGER | FOREIGN KEY -> auth_user(id) | - | -
  job_role_id | BIGINT | NOT NULL, FOREIGN KEY -> job_roles(id) | - | -

TABLE: pipeline_history
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | - | -
  stage_status | VARCHAR(20) | NOT NULL | - | -
  entry_timestamp | TIMESTAMP | NOT NULL | - | -
  exit_timestamp | TIMESTAMP | - | - | -
  duration_seconds | INTEGER | - | - | -
  stage_session_object_id | INTEGER | NOT NULL | - | -
  notes | TEXT | NOT NULL | - | -
  actioned_by_id | INTEGER | FOREIGN KEY -> auth_user(id) | - | -
  pipeline_config_id | BIGINT | NOT NULL, FOREIGN KEY -> pipeline_config(id) | - | -
  pipeline_entry_id | BIGINT | NOT NULL, FOREIGN KEY -> pipeline_entry(id) | - | -
  stage_session_content_type_id | INTEGER | NOT NULL, FOREIGN KEY -> django_content_type(id) | - | -

TABLE: pipeline_entry
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | - | -
  overall_status | VARCHAR(20) | NOT NULL | - | -
  entry_date | TIMESTAMP | NOT NULL | - | -
  last_updated | TIMESTAMP | NOT NULL | - | -
  notes | TEXT | NOT NULL | - | -
  current_stage_object_id | BIGINT | FOREIGN KEY -> pipeline_history(id) | - | -
  job_role_id | BIGINT | NOT NULL, UNIQUE, FOREIGN KEY -> job_roles(id) | - | -
  last_action_by_id | INTEGER | FOREIGN KEY -> auth_user(id) | - | -
  parsed_resume_id | BIGINT | FOREIGN KEY -> parsed_resumes(id) | - | -
  resume_parsing_job_id | BIGINT | NOT NULL, UNIQUE, FOREIGN KEY -> resume_parsing_jobs(id) | - | -

TABLE: stage_registry
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | 1 | 2
  stage_name | VARCHAR(50) | NOT NULL, UNIQUE | "matching" | "sourcing"
  display_name | VARCHAR(100) | NOT NULL | "Matching & Ranking" | "Candidate Sourcing"
  description | TEXT | NOT NULL | "Evaluates candidate fit against job requirements and ranks candidates." | "Entry point for candidates. Supports direct upload, application links, recruiter search, and automated sourcing."
  is_mandatory | BOOLEAN | NOT NULL | True | -
  is_repeatable | BOOLEAN | NOT NULL | False | -
  default_order | INTEGER | - | 2 | 1
  orchestrator_class | VARCHAR(255) | NOT NULL | "recruitment.role_sourcing.services.SourcingOrchestrator" | "recruitment.matching.services.MatchingOrchestrator"
  created_date | TIMESTAMP | NOT NULL | 2025-11-13 19:06:27.634286+00:00 | 2025-11-13 19:06:27.636190+00:00
  modified_date | TIMESTAMP | NOT NULL | 2025-11-13 19:06:27.634298+00:00 | 2025-11-13 19:06:27.636205+00:00

TABLE: pipeline_config
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | - | -
  order | INTEGER | NOT NULL, UNIQUE | - | -
  is_active | BOOLEAN | NOT NULL | - | -
  created_date | TIMESTAMP | NOT NULL | - | -
  modified_date | TIMESTAMP | NOT NULL | - | -
  created_by_id | INTEGER | FOREIGN KEY -> auth_user(id) | - | -
  job_role_id | BIGINT | NOT NULL, UNIQUE, FOREIGN KEY -> job_roles(id) | - | -
  modified_by_id | INTEGER | FOREIGN KEY -> auth_user(id) | - | -
  stage_id | BIGINT | NOT NULL, UNIQUE, FOREIGN KEY -> stage_registry(id) | - | -

TABLE: matching_stage_config
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | - | -
  created_date | TIMESTAMP | NOT NULL | - | -
  modified_date | TIMESTAMP | NOT NULL | - | -
  pipeline_config_id | BIGINT | NOT NULL, UNIQUE, FOREIGN KEY -> pipeline_config(id) | - | -

TABLE: matching_job
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | - | -
  status | VARCHAR(20) | NOT NULL | - | -
  created_date | TIMESTAMP | NOT NULL | - | -
  completed_date | TIMESTAMP | - | - | -
  pipeline_entry_id | BIGINT | NOT NULL, FOREIGN KEY -> pipeline_entry(id) | - | -

TABLE: communications_trackedemailthread
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | - | -
  thread_id | VARCHAR(255) | NOT NULL, UNIQUE | - | -
  message_id | VARCHAR(255) | NOT NULL | - | -
  candidate_email | VARCHAR(254) | NOT NULL | - | -
  subject | VARCHAR(500) | NOT NULL | - | -
  created_at | TIMESTAMP | NOT NULL | - | -
  last_activity | TIMESTAMP | NOT NULL | - | -
  initiated_by_id | INTEGER | FOREIGN KEY -> auth_user(id) | - | -

TABLE: sourcing_event
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | - | -
  status | VARCHAR(20) | NOT NULL | - | -
  channel_details_id | INTEGER | NOT NULL | - | -
  sourced_date | TIMESTAMP | NOT NULL | - | -
  completed_date | TIMESTAMP | - | - | -
  notes | TEXT | NOT NULL | - | -
  channel_details_content_type_id | INTEGER | NOT NULL, FOREIGN KEY -> django_content_type(id) | - | -
  job_role_id | BIGINT | NOT NULL, FOREIGN KEY -> job_roles(id) | - | -
  parsed_resume_id | BIGINT | FOREIGN KEY -> parsed_resumes(id) | - | -
  pipeline_entry_id | BIGINT | UNIQUE, FOREIGN KEY -> pipeline_entry(id) | - | -
  resume_parsing_job_id | BIGINT | NOT NULL, FOREIGN KEY -> resume_parsing_jobs(id) | - | -
  sourced_by_id | INTEGER | FOREIGN KEY -> auth_user(id) | - | -

TABLE: sourcing_config
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | - | -
  direct_upload_enabled | BOOLEAN | NOT NULL | - | -
  application_link_enabled | BOOLEAN | NOT NULL | - | -
  recruiter_search_enabled | BOOLEAN | NOT NULL | - | -
  auto_search_enabled | BOOLEAN | NOT NULL | - | -
  created_date | TIMESTAMP | NOT NULL | - | -
  modified_date | TIMESTAMP | NOT NULL | - | -
  modified_by_id | INTEGER | FOREIGN KEY -> auth_user(id) | - | -
  pipeline_config_id | BIGINT | NOT NULL, UNIQUE, FOREIGN KEY -> pipeline_config(id) | - | -

TABLE: direct_upload_record
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | - | -
  original_filename | VARCHAR(255) | NOT NULL | - | -
  recruiter_notes | TEXT | NOT NULL | - | -
  upload_timestamp | TIMESTAMP | NOT NULL | - | -
  uploaded_by_id | INTEGER | FOREIGN KEY -> auth_user(id) | - | -

TABLE: communications_mockcandidate
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | - | -
  name | VARCHAR(200) | NOT NULL | - | -
  email | VARCHAR(254) | NOT NULL, UNIQUE | - | -
  created_at | TIMESTAMP | NOT NULL | - | -
  updated_at | TIMESTAMP | NOT NULL | - | -

TABLE: jobdiva_audit_logs
  [Column | Type | Constraints | Sample1 | Sample2]
  id | UUID | PRIMARY KEY, NOT NULL | - | -
  created_at | TIMESTAMP | NOT NULL | - | -
  user_email | VARCHAR(255) | NOT NULL | - | -
  service_account_used | VARCHAR(100) | NOT NULL | - | -
  endpoint | VARCHAR(255) | NOT NULL | - | -
  http_method | VARCHAR(10) | NOT NULL | - | -
  api_version | VARCHAR(10) | NOT NULL | - | -
  request_data | JSONB | NOT NULL | - | -
  response_status | INTEGER | - | - | -
  response_data | JSONB | NOT NULL | - | -
  response_time_ms | INTEGER | - | - | -
  success | BOOLEAN | NOT NULL | - | -
  jobdiva_entity_type | VARCHAR(50) | NOT NULL | - | -
  jobdiva_entity_id | VARCHAR(100) | NOT NULL | - | -
  request_id | UUID | NOT NULL | - | -
  operation_sequence | INTEGER | NOT NULL | - | -
  operation_action | VARCHAR(100) | NOT NULL | - | -
  ip_address | INET | - | - | -
  user_agent | VARCHAR(500) | - | - | -
  error_message | TEXT | NOT NULL | - | -
  user_id | INTEGER | FOREIGN KEY -> auth_user(id) | - | -

TABLE: health_check_db_testmodel
  [Column | Type | Constraints | Sample1 | Sample2]
  id | INTEGER | PRIMARY KEY, NOT NULL | - | -
  title | VARCHAR(128) | NOT NULL | - | -

TABLE: candidates_candidateexperience
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | - | -
  sort_order | INTEGER | - | - | -
  active | BOOLEAN | NOT NULL | - | -
  created_at | TIMESTAMP | NOT NULL | - | -
  updated_at | TIMESTAMP | NOT NULL | - | -
  retrieved_at | TIMESTAMP | NOT NULL | - | -
  jobdiva_synced_at | TIMESTAMP | - | - | -
  jobdiva_hash | VARCHAR(64) | NOT NULL | - | -
  is_active | BOOLEAN | NOT NULL | - | -
  job_title | VARCHAR(200) | NOT NULL | - | -
  company | VARCHAR(200) | NOT NULL | - | -
  start_date | DATE | - | - | -
  end_date | DATE | - | - | -
  is_present | BOOLEAN | NOT NULL | - | -
  description | TEXT | NOT NULL | - | -
  raw_details | VARCHAR(500) | NOT NULL | - | -
  raw_date | VARCHAR(100) | NOT NULL | - | -
  candidate_id | BIGINT | NOT NULL, FOREIGN KEY -> candidates_candidate(id) | - | -

TABLE: failed_candidate_creations
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | 1 | 2
  sort_order | INTEGER | - | - | -
  active | BOOLEAN | NOT NULL | True | -
  created_at | TIMESTAMP | NOT NULL | 2025-11-20 22:12:31.052951+00:00 | 2025-11-20 22:08:41.130872+00:00
  updated_at | TIMESTAMP | NOT NULL | 2025-11-20 22:11:04.591075+00:00 | 2025-11-20 22:10:09.871756+00:00
  jobdiva_candidate_id | VARCHAR(100) | NOT NULL | "16781429029709" | "unknown"
  error_type | VARCHAR(100) | NOT NULL | "db_error" | "unknown"
  error_message | TEXT | NOT NULL | "'str' object has no attribute 'get'" | "duplicate key value violates unique constraint "candidates_candidate_email_key"
DETAIL:  Key (email)=() already exists.
"
  error_traceback | TEXT | NOT NULL | "Traceback (most recent call last):
  File "/home/cmoore/programming/talent_ai/recruitment/candidates/services/candidate_creation.py", line 94, in create_candidate_from_resume
    upload_result = upload_resume_to_jobdiva(
                    ^^^^^^^^^..." | "Traceback (most recent call last):
  File "/home/cmoore/programming/talent_ai/recruitment/candidates/services/candidate_creation.py", line 120, in create_candidate_from_resume
    latest_resume = max(resumes, key=lambda r: r.get('DATECREATED', ''))
 ..."
  attempt_count | INTEGER | NOT NULL | 1 | -
  last_attempt_at | TIMESTAMP | NOT NULL | 2025-11-20 22:10:09.871781+00:00 | 2025-11-20 22:12:31.052995+00:00
  status | VARCHAR(50) | NOT NULL | "pending_retry" | -
  resolved_at | TIMESTAMP | - | - | -
  resolution_notes | TEXT | NOT NULL | "" | -
  parsed_resume_id | BIGINT | FOREIGN KEY -> parsed_resumes(id) | - | -
  resolved_by_id | INTEGER | FOREIGN KEY -> auth_user(id) | - | -
  stored_file_id | INTEGER | FOREIGN KEY -> storage_storedfile(id) | 3 | -

TABLE: candidates_candidate
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | 1 | 5
  sort_order | INTEGER | - | - | -
  active | BOOLEAN | NOT NULL | True | -
  created_at | TIMESTAMP | NOT NULL | 2025-11-07 02:13:45.427903+00:00 | 2025-11-20 22:34:37.711893+00:00
  updated_at | TIMESTAMP | NOT NULL | 2025-11-07 02:13:45.427980+00:00 | 2025-11-21 02:07:30.922359+00:00
  first_name | VARCHAR(100) | NOT NULL | "Bharathkumar" | "Test"
  last_name | VARCHAR(100) | NOT NULL | "Tamilarasu" | "User"
  email | VARCHAR(254) | NOT NULL, UNIQUE | "bharathkumar.t.17@gmail.com" | "test@test.com"
  job_title | VARCHAR(200) | NOT NULL | "" | "Bharathkumar"
  company | VARCHAR(200) | NOT NULL | "" | -
  location | VARCHAR(200) | NOT NULL | "" | -
  years_experience | INTEGER | NOT NULL | 0 | 5
  education | VARCHAR(300) | NOT NULL | "" | -
  skills | TEXT | NOT NULL | "" | "Python, Django, PostgreSQL, React, Docker"
  profile_picture | VARCHAR(200) | - | - | -
  good_fit | BOOLEAN | NOT NULL | False | -
  contacted | BOOLEAN | NOT NULL | False | -
  replied | BOOLEAN | NOT NULL | False | -
  smart_tags | TEXT | NOT NULL | "" | -
  search_vector | TSVECTOR | - | "'bharathkumar':1A,3A 'tamilarasu':2A" | -
  profile_embedding | NULL | - | - | -
  jobdiva_alternate_email | VARCHAR(254) | NOT NULL | "" | -
  jobdiva_cell_phone | VARCHAR(20) | NOT NULL | "" | -
  jobdiva_city | VARCHAR(100) | NOT NULL | "" | -
  jobdiva_country | VARCHAR(100) | NOT NULL | "US" | -
  jobdiva_created_at | TIMESTAMP | - | 2025-09-30 08:36:55+00:00 | -
  jobdiva_home_phone | VARCHAR(20) | NOT NULL | "" | -
  jobdiva_id | VARCHAR(50) | UNIQUE | "" | "16781429029709"
  jobdiva_last_synced_at | TIMESTAMP | - | 2025-11-21 02:09:19.379126+00:00 | -
  jobdiva_state | VARCHAR(50) | NOT NULL | "" | -
  jobdiva_sync_error_message | TEXT | NOT NULL | "" | -
  jobdiva_sync_status | VARCHAR(20) | NOT NULL | "never" | "synced"
  jobdiva_updated_at | TIMESTAMP | - | 2025-11-20 17:34:36+00:00 | -

TABLE: candidate_documents
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | 3 | -
  sort_order | INTEGER | - | - | -
  active | BOOLEAN | NOT NULL | True | -
  created_at | TIMESTAMP | NOT NULL | 2025-11-20 22:34:37.865553+00:00 | -
  updated_at | TIMESTAMP | NOT NULL | 2025-11-20 22:34:37.865567+00:00 | -
  jobdiva_file_id | VARCHAR(100) | - | "16781429029709_564_8" | -
  version | INTEGER | NOT NULL | 1 | -
  is_primary | BOOLEAN | NOT NULL | True | -
  notes | TEXT | NOT NULL | "" | -
  candidate_id | BIGINT | NOT NULL, FOREIGN KEY -> candidates_candidate(id) | 5 | -
  document_type_id | BIGINT | NOT NULL, FOREIGN KEY -> document_types(id) | 1 | -
  stored_file_id | INTEGER | FOREIGN KEY -> storage_storedfile(id) | 3 | -
  uploaded_by_id | INTEGER | FOREIGN KEY -> auth_user(id) | - | -

TABLE: document_types
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | 1 | 2
  active | BOOLEAN | NOT NULL | True | -
  created_at | TIMESTAMP | NOT NULL | 2025-11-20 02:25:34.104578+00:00 | 2025-11-20 02:25:34.108572+00:00
  updated_at | TIMESTAMP | NOT NULL | 2025-11-20 02:25:34.094110+00:00 | 2025-11-20 02:25:34.108580+00:00
  code | VARCHAR(50) | NOT NULL, UNIQUE | "certification" | "cover_letter"
  name | VARCHAR(100) | NOT NULL | "Other" | "Cover Letter"
  description | TEXT | NOT NULL | "Professional certification or license" | "Work sample or project example"
  is_active | BOOLEAN | NOT NULL | True | -
  sort_order | INTEGER | NOT NULL | 3 | 5

TABLE: candidates_candidateeducation
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | - | -
  sort_order | INTEGER | - | - | -
  active | BOOLEAN | NOT NULL | - | -
  created_at | TIMESTAMP | NOT NULL | - | -
  updated_at | TIMESTAMP | NOT NULL | - | -
  retrieved_at | TIMESTAMP | NOT NULL | - | -
  jobdiva_synced_at | TIMESTAMP | - | - | -
  jobdiva_hash | VARCHAR(64) | NOT NULL | - | -
  is_active | BOOLEAN | NOT NULL | - | -
  institution | VARCHAR(200) | NOT NULL | - | -
  major | VARCHAR(200) | NOT NULL | - | -
  degree | VARCHAR(100) | NOT NULL | - | -
  graduation_year | INTEGER | - | - | -
  candidate_id | BIGINT | NOT NULL, FOREIGN KEY -> candidates_candidate(id) | - | -

TABLE: candidates_majorcategory
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | 1 | 2
  sort_order | INTEGER | - | - | -
  active | BOOLEAN | NOT NULL | True | -
  created_at | TIMESTAMP | NOT NULL | 2025-11-21 00:18:35.930651+00:00 | 2025-11-21 00:18:35.931854+00:00
  updated_at | TIMESTAMP | NOT NULL | 2025-11-21 00:18:35.930664+00:00 | 2025-11-21 00:18:35.925485+00:00
  code | VARCHAR(50) | NOT NULL, UNIQUE | "arts" | "business"
  name | VARCHAR(100) | NOT NULL | "Health & Medicine" | "Business & Management"
  keywords | JSONB | NOT NULL | ["Graphic Design", "Design", "Visual Arts", "Fine Arts", "Industrial Design", "UX Design", "UI Design", "Product Design", "Interior Design", "Fashion Design", "Architecture", "Music", "Music Theory", "Music Performance", "Audio Engineering", "Theater... | ["Education", "Teaching", "Elementary Education", "Secondary Education", "Special Education", "Early Childhood Education", "Educational Leadership", "Curriculum Development", "Instructional Design", "Educational Technology", "Physical Education", "Mu...
  description | TEXT | NOT NULL | "Education and teaching disciplines" | "Humanities and social science disciplines"
  icon | VARCHAR(50) | NOT NULL | "🎨" | "🎓"

TABLE: candidates_degreetype
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | 1 | 2
  sort_order | INTEGER | - | 3 | 5
  active | BOOLEAN | NOT NULL | True | -
  created_at | TIMESTAMP | NOT NULL | 2025-11-21 00:18:35.902474+00:00 | 2025-11-21 00:18:35.911027+00:00
  updated_at | TIMESTAMP | NOT NULL | 2025-11-21 00:18:35.912016+00:00 | 2025-11-21 00:18:35.910246+00:00
  code | VARCHAR(50) | NOT NULL, UNIQUE | "associate" | "bachelors"
  name | VARCHAR(100) | NOT NULL | "Bachelor's Degree" | "Certificate / Certification"
  level | VARCHAR(50) | NOT NULL | "associate" | "certificate"
  rank | INTEGER | NOT NULL | 1 | 2
  variants | JSONB | NOT NULL | ["Certificate", "Certification", "Cert"] | ["MS", "M.S", "MA", "M.A", "Masters", "Master", "MBA", "M.B.A"]
  description | TEXT | NOT NULL | "Highest level of academic degree" | "Two-year degree"

TABLE: candidates_companycategory
  [Column | Type | Constraints | Sample1 | Sample2]
  id | BIGINT | PRIMARY KEY, NOT NULL | 1 | 2
  sort_order | INTEGER | - | - | -
  active | BOOLEAN | NOT NULL | True | -
  created_at | TIMESTAMP | NOT NULL | 2025-11-21 00:18:35.945812+00:00 | 2025-11-21 00:18:35.946793+00:00
  updated_at | TIMESTAMP | NOT NULL | 2025-11-21 00:18:35.947704+00:00 | 2025-11-21 00:18:35.938017+00:00
  code | VARCHAR(50) | NOT NULL, UNIQUE | "big_tech" | "consulting"
  name | VARCHAR(100) | NOT NULL | "Top Financial Institutions" | "Top Consulting Firms"
  companies | JSONB | NOT NULL | ["Meta", "Facebook", "FB", "Apple", "Amazon", "AWS", "Netflix", "Google", "Alphabet", "YouTube"] | ["SpaceX", "Stripe", "Databricks", "Epic Games", "Instacart", "Canva", "Klarna", "Revolut", "Nubank", "Checkout.com", "Plaid", "Chime", "Discord", "Notion", "Figma", "Gusto", "Grammarly", "GitLab", "HashiCorp", "Celonis", "UiPath", "Automation Anywhe...
  description | TEXT | NOT NULL | "Major technology companies beyond FAANG" | "Top management consulting and professional services firms"
  icon | VARCHAR(50) | NOT NULL | "🏦" | "🦄"
