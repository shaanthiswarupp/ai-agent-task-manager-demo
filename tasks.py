tasks = [
    {
        "id": 1,
        "title": "Learn Python",
        "description": "Practice Python basics",
        "status": "PENDING"
    },
    {
        "id": 2,
        "title": "Build API",
        "description": "Create a task manager API",
        "status": "COMPLETED"
    }
]


def get_tasks():
    return tasks


def create_task(title, description):
    new_id = max(task["id"] for task in tasks) + 1 if tasks else 1
    new_task = {
        "id": new_id,
        "title": title,
        "description": description,
        "status": "PENDING"
    }
    tasks.append(new_task)
    return new_task


if __name__ == "__main__":
    print(get_tasks())