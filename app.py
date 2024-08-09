from flask import Flask, request, jsonify # o request vem do Flask para recuperar informações
from models.task import Task

# CRUD
# Create, Read, Update and Delete

tasks = []
task_id_control = 1

app = Flask(__name__) 

@app.route('/tasks', methods=['POST'])
def creat_task():
    global task_id_control # Fazemos isso para ter acesso a uma variavel local
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data.get("title"), description=data.get("description"))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso", "id": new_task.id}) #Faz com que o retorno seja em json para seguir o API Rest


@app.route('/tasks', methods=['GET'])
def get_tasks():
    global task_id_control
    task_list = []

    for task in tasks:
        task_list.append(task.to_dict())

    output = {
                "tasks": task_list,
                "total_tasks": len(task_list)
            }
    return jsonify(output)

@app.route('/tasks/<int:id>', methods= ['GET']) #Colocamos o tipo de parâmetro e o nome que queremos dar a ele, se não convertemos ele sempre será string
def get_task(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())

    return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break
    
    if task == None:
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    print(task)
    return jsonify({"message": "Tarefa atualizada com sucesso"})

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break
    
    
    if task == None:
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404
    
    tasks.remove(task)
    return jsonify({"message": "Tarefa deletada com sucesso"})


if __name__ == "__main__": 
    app.run(debug=True) 
