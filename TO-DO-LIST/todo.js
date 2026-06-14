function addTask() {
    let taskInput = document.getElementById("taskInput");
    let taskText = taskInput.value.trim();

    if(taskText === ""){
        alert("Please enter a task");
        return;
    }

    let li = document.createElement("li");

    li.innerHTML = `
    <span>${taskText}</span>

    <div class="actions">
        <button class="complete-btn" onclick="completeTask(this)">✓</button>

        <button class="edit-btn" onclick="editTask(this)">Edit</button>

        <button class="delete-btn" onclick="deleteTask(this)">✕</button>
    </div>
    `;

    document.getElementById("taskList").appendChild(li);

    taskInput.value = "";
}

function completeTask(button){
      let li = button.parentElement.parentElement;
      li.classList.toggle("completed");
}

function deleteTask(button){
      let li = button.parentElement.parentElement;
      li.remove();
}

function editTask(button){
      let li = button.parentElement.parentElement;
      let span = li.querySelector("span");

      let newTask = prompt("Modify your task:", span.innerText);

      if(newTask !== null && newTask.trim() !== ""){
        span.innerText = newTask;
      }
}