# User Diary Multi-Class Planned Design Recipe

## 1. Describe the Problem

```markdown
As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries
```

## 2. Design the Class System

```acsii
             ┌────────────────────────────────────────────────┐
┌────────────┴────────────┐     ┌────────────────┐            │
│ User Diary              │     │TodoList        │     ┌──────▼──────┐
│  Diary Entries          │     │ List of Tasks  │     │Contact List │
│  Add Entry              ├─────► Mark Tasks as  │     │ Contacts    │
│  Read Older Entries     │     │   Complete     │     │ Add Contact │
│  Find Entries Matching  │     │ Return list of │     └──────┬──────┘
│    User Reading Speed   │     │   Tasks        │            │
└────────────┬────────────┘     └────────┬───────┘            │
             │                  ┌────────▼───────┐            │
      ┌──────▼──────┐           │Todo            │     ┌──────▼──────┐
      │ Diary Entry │           │ Task           │     │Contact      │
      │  Title      │           │ Status         │     │ Name        │
      │  Text       │           │ Mark Task as   │     │ Number      │
      └─────────────┘           │   Complete     │     └─────────────┘
                                └────────────────┘
```
