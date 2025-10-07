# do_it
an application that contains the list of tasks and way to complete them

1.a: Login Page
Estimated Time: 4-6 hours
Requirements:
•	Create a login form with username and password fields
•	Implement authentication using PostgreSQL database
•	Query users table to verify credentials
•	Add input validation (check for empty fields)
•	Display error messages for invalid credentials
•	On successful login, store user_id in session state and redirect to Dashboard
•	Use st.session_state to maintain login status

Database Operations:
•	Connect to PostgreSQL database
•	Query users table with username
•	Verify password 
•	Return user_id on successful authentication

Deliverables:
•	Working login page
•	Basic user validation
•	Session management implementation
________________________________________

Task 1.b: Dashboard Page

Estimated Time: 12-16 hours
This is the main application page with multiple components:
Component 1: Logout Button
Time: 1 hour
•	Place a logout button in the sidebar or top-right
•	Clear session state on logout
•	Redirect to login page
Component 2: Calendar (Date Selection)
Time: 2-3 hours
•	Add a date picker for task selection/filtering
•	Use st.date_input() for calendar functionality
•	Allow users to view tasks for selected dates
•	Default to today's date
Component 3: Todo Table
Time: 4-5 hours
•	Display todos in a table format using st.dataframe() or st.table()
•	Fetch todos from PostgreSQL database filtered by user_id
•	Include columns: Task Name, Description, Due Date, Status, Priority
•	Make it interactive (allow row selection)
•	Add filtering options (by status, priority, date)
•	Implement sorting functionality
•	Use SQL queries with WHERE, ORDER BY clauses for efficient filtering
Table Structure:
Task Name	Description	Due Date	Status	Priority
Example	Details	Date	Pending	High
Component 4: Save / Edit Functionality
Time: 5-6 hours
Add New Task:
•	Create input form with fields: 
o	Task name (text input)
o	Description (text area)
o	Due date (date picker)
o	Status dropdown (Pending, In Progress, Completed)
o	Priority dropdown (Low, Medium, High)
•	Add "Save" button to insert task into PostgreSQL database
•	Use parameterized queries to prevent SQL injection
•	Link task to current user via user_id from session state
Edit Existing Task:
•	Allow selection of existing task from table
•	Pre-fill form with selected task data from database
•	Update task in database on "Save" button using UPDATE query
•	Implement delete functionality using DELETE query
•	Add confirmation dialog before deletion
Component 5: Preview Section
Time: 2-3 hours
•	Create a preview panel that shows: 
o	Total tasks count for current user
o	Tasks by status (Pending, In Progress, Completed)
o	Today's tasks
o	Overdue tasks
•	Use SQL aggregate queries (COUNT, GROUP BY) for statistics
•	Use st.metric() for displaying statistics
Data Storage:
•	Use PostgreSQL database for data persistence
•	Create helper functions for database CRUD operations
•	Use connection pooling for efficient database access
