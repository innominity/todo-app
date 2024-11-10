<template>
  <div class="wrapper">
    <header></header>
    <main>
      <div class="todo-form flex flex-col max-w-2xl mx-auto">
        <div class="flex flex-row">
          <div class="text-neutral-50 text-3xl font-medium mb-4">
            <span>TO</span><span class="text-sky-500">DO</span>
          </div>
        </div>
        <div class="mb-12 flex rounded-lg shadow-sm">
          <input
            placeholder="Введите что-нибудь"
            type="text"
            class="border rounded-s-lg block w-full p-2.5 px-4 bg-gray-700 border-gray-600 placeholder-gray-500 text-gray-200 outline-none"
            v-model="title"
            v-on:keyup.enter="createTask()"
          />
          <button
            type="button"
            @click="createTask()"
            class="w-[2.875rem] h-[2.875rem] shrink-0 inline-flex justify-center items-center gap-x-2 text-sm font-semibold rounded-e-md border border-transparent bg-sky-800 text-white hover:bg-sky-900 focus:outline-none"
          >
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" height="18px" width="18px" className="size-6">
            <path strokeLinecap="round" strokeLinejoin="round" d="m8.25 4.5 7.5 7.5-7.5 7.5" />
          </svg>
          </button>
        </div>
        <div v-if="tasks.length > 0" class="flex flex-col">
          <div v-for="task in tasks" :key="task.id" class="task-item flex flex-row p-2.5 px-4 bg-gray-700 last:border-b-0 border-b-2 border-sky-900 items-center first:rounded-t-lg last:rounded-b-lg">
            <div class="inline-flex items-center mr-4">
              <label class="flex items-center cursor-pointer relative">
                <input type="checkbox" @change="updateStatus(task)" :checked="task.status == STATUS_DONE" class="peer h-5 w-5 cursor-pointer transition-all appearance-none rounded-full bg-slate-300 shadow hover:shadow-md border border-slate-300 checked:bg-slate-900 checked:border-slate-900" id="check-custom-style" />
                <span class="absolute text-white opacity-0 peer-checked:opacity-100 top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" viewBox="0 0 20 20" fill="currentColor" stroke="currentColor" stroke-width="1">
                  <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
                </svg>
                </span>
              </label>
            </div>
            <span :class="{'line-through text-gray-500': task.status == STATUS_DONE}" class="text-gray-400 select-none grow" >{{ task.title }}</span>
            <span class="task-item__del text-gray-400 hover:text-red-600 ml-4 cursor-pointer" @click="removeTask(task)" title="Удалить задачу">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={10.5} stroke="currentColor" height="18px" width="18px" className="size-6">
                <path strokeLinecap="round" strokeLinejoin="round" d="M6 18 18 6M6 6l12 12" />
              </svg>
            </span>
          </div>
        </div>
      </div>
    </main>
    <footer></footer>
  </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios';

const STATUS_ACTIVE = 1;
const STATUS_DONE = 2;

export default {
  name: "HomeView",

  data() {
    return {
      STATUS_ACTIVE: STATUS_ACTIVE,
      STATUS_DONE: STATUS_DONE,

      title: '',
      tasks: [],
    };
  },
  methods: {
    /**
     * Получаем список задач из базы данных
     */
    getTasks() {
      axios.get("/api/v1/todo/tasks/")
        .then(response => {
          this.tasks = response.data.data;
        })
        .catch(error => {
          console.log(error);
        })
    },
    /**
     * Создать задачу
     */
    createTask() {
      if(this.title.length == 0) {
        alert("Введите название задачи!")
      }

      const form = new FormData();
      form.append('title', this.title);
      axios({
        method: 'post',
        url: '/api/v1/todo/task/create/',
        data: form
      })
      .then(response => {
        let task = response.data.task;
        this.tasks.unshift(task);
        this.title = '';
      })
      .catch(error => {
        console.log(error);
      })
    },
    /**
     * Изменение статуса задачи
     */
    updateStatus(task) {
      let taskStatusUpdate = task.status == this.STATUS_DONE? this.STATUS_ACTIVE : this.STATUS_DONE;
      const form = new FormData();
      form.append('task_status', taskStatusUpdate);
      axios({
        method: 'post',
        url: `/api/v1/todo/task/update-status/${task.id}/`,
        data: form
      })
      .then(response => {
        let taskUpdate = response.data.task;
        task.status = taskUpdate.status;
      })
      .catch(error => {
        console.log(error);
      })
    },
    /**
     * Удаление задачи
     */
    removeTask(task) {
      const form = new FormData();
      form.append('task_id', task.id);
      axios({
        method: 'post',
        url: '/api/v1/todo/task/remove/',
        data: form
      })
      .then(response => {
        let task_id = response.data.task_id;
        let index_del = this.tasks.map(t => t.id).indexOf(task_id);
        this.tasks.splice(index_del, 1)
      })
      .catch(error => {
        console.log(error);
      })
    }
  },
  mounted() {
    this.getTasks();
  },
  components: {},
};
</script>

<style scoped>
.wrapper {
  display: flex;
  flex-flow: column nowrap;
  min-height: 100vh;
  background-color: #242633;
}

header {
  flex: 0 0 auto;
}

main {
  flex: 1 1 auto;
  padding: 15vh 1rem 2rem 1rem;
}

.task-item__del {
  visibility: collapse;  
}

.task-item:hover .task-item__del,
.task-item:focus .task-item__del {
  visibility: visible;  
}
</style>