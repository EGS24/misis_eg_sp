from fastapi import FastAPI
import uvicorn

app = FastAPI()
tasks = []


@app.get("/")
def read_root():  # начальное приветствие
    return {"Welcome": "To-Do List"}


@app.get("/tasks")  # показываю все задачи
def get_tasks():
    return {"tasks": tasks}


@app.post("/tasks")  # добавляю задачу
def add_task(task: str):
    tasks.append(task)
    return {"task": task}


@app.delete("/tasks/{task_id}")
# удалить 1 задачу по порядку (писать 1(индекс 0), 2(индекс 1), 3(индекс 2)), как расположены в списке
def delete_task(task_id: int):
    if task_id < len(tasks):
        task = tasks.pop(task_id - 1)
        return {"task": task}
    else:
        return {"error": "Task not found"}


@app.delete("/tasks")  # удалить все задачи
def delete_all_tasks():
    tasks.clear()
    return "All tasks delete"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

